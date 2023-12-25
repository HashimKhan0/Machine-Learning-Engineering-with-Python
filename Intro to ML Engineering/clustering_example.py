'''
    first we define a function that will simulate ride distances
    we repeat lines to generate base data and anomalies in the data
'''

import numpy as np 
import pandas as pd
import datetime
from numpy.random import MT19937
from numpy.random import RandomState, SeedSequence

rs = RandomState(MT19937(SeedSequence(123456789)))

# define simulate ride data function

def simulate_ride_distance():
    ride_dists = np.concatenate(
        (
            10 * np.random.random(size=370),
            30 * np.random.random(size=10),
            10 * np.random.random(size=10),
            10 * np.random.random(size=10)
        )
    )
    return ride_dists

'''
    we now do the same for speeds
    splitting the taxis into sets of 370, 10, 10, and 10 so we can create some data with typical behaviour 
'''

def simulate_ride_speeds():
    ride_speeds = np.concatenate(
        (
            np.random.normal(loc=30,scale=5,size=370), # random values with Gaussian distribution with mean of 30 and standard dev of 5
            np.random.normal(loc=30, scale = 5, size = 10),
            np.random.normal(loc=50,scale=10,size=10),
            np.random.normal(loc=15,scale=4,size=10)
        )
    )

    return ride_speeds

'''
    we can now cxombine both functions to create a simulated dataset containing ride IDs, speeds, distances, and times
'''


def simulate_ride_data():
    ride_dists = simulate_ride_distance()
    ride_speeds = simulate_ride_speeds()
    ride_times = ride_dists / ride_speeds

    df = pd.DataFrame(
        {
            'ride_dist': ride_dists,
            'ride_time': ride_times,
            'ride_speed': ride_speeds
        }
    )

    ride_ids = datetime.datetime.now().strftime("%Y%m%d") +\
                df.index.astype(str)
    df['ride_id'] = ride_ids
    return df



import matplotlib.pyplot as plt

'''
    here is a function for plotting our cluster results
'''
def plot_cluster_results(data, labels, core_samples_mask,
                         n_clusters_):
    fig = plt.figure(figsize=(10, 10))
    # Black removed and is used for noise instead.
    unique_labels = set(labels)
    colors = [plt.cm.cool(each) for each in np.linspace(0, 1,
              len(unique_labels))]
    for k, col in zip(unique_labels, colors):
        if k == -1:
            # Black used for noise.
            col = [0, 0, 0, 1]
        class_member_mask = (labels == k)
        xy = data[class_member_mask & core_samples_mask]
        plt.plot(xy[:, 0], xy[:, 1], 'o',
                 markerfacecolor=tuple(col),
                 markeredgecolor='k', markersize=14)
        xy = data[class_member_mask & ~core_samples_mask]
        plt.plot(xy[:, 0], xy[:, 1], '^',
                 markerfacecolor=tuple(col),
                 markeredgecolor='k', markersize=14)
    plt.xlabel('Standard Scaled Ride Dist.')
    plt.ylabel('Standard Scaled Ride Time')
    plt.title('Estimated number of clusters: %d' % n_clusters_)
    plt.savefig('taxi-rides.png')

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
from sklearn import metrics

'''
    we can get to the core of what data scientist produce in their projects
    simple function that wraps sklearn code to return a dictionary with clustering run metadata and results
'''

def cluster_and_label(data, create_and_show_plot=True):
    data = StandardScaler().fit_transform(data)
    db = DBSCAN(eps=0.3, min_samples=10).fit(data)
    
    #finding labels from clustering
    core_samples_mask = np.zeros_like(db.labels_,dtype=bool)
    core_samples_mask[db.core_sample_indices_] = True
    labels = db.labels_

    # number of clusters in labels, ignoring noise
    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

    n_noise_ = list(labels).count(-1)
    run_metadata = {
        'nClusters': n_clusters_,
        'nNoise': n_noise_,
        'silhouetteCoefficient': metrics.silhouette_score(data, labels),
        'labels' : labels,
    }

    if create_and_show_plot:
        plot_cluster_results(data,labels,core_samples_mask,n_clusters_)
    else:
        pass
    return run_metadata
    

'''
    now we can bring it all together at the entry point of the program
'''

import logging
logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)

if __name__ == '__main__':
    import os
    #if data is present read it in
    file_path = 'taxi-rides.csv'
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
    else:
        logging.info('Simulating ride data')
        df = simulate_ride_data()
        df.to_csv(file_path, index=False)
    X = df[['ride_dist', 'ride_time']]

    logging.info('Cluster and labelling')
    results = cluster_and_label(X,create_and_show_plot=True)
    df['label'] = results['labels']

    logging.info('Outputting to json ...')
    df.to_json('taxi-lavels.json', orient='records')