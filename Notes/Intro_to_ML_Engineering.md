# Chapter 1: Intro to ML Engineering

## Intro:
* The following chapter will cover 
    1. the different types od data roles relevant to machine learning(ML) engineering and why they are important
    2. how to use this knowledge to build and work within appropriate teams
    3. some key points to remember when building working ML products in the real world
    4. how to start to isolate appropraite problems for engineered ML solutions
    5. how to create your own high level ML system designs for a veriety of typical business problems
    
## Defining a Taxonomy of data disciplines:
* this chapter explores some of the main data disciplines that are consistent with any data project
    
### Data Scientist:
* faces the challenged of taking advanced anayltyics and ML into production 
* key areas of focus that should always be part of the data scientist's jobs profile:
    1. **Analysis**
        - a data scientist should be able to wrangle, munge, manipulate and consolidate datasets before performing calculations
        - the end result is knowledge of your dataset that you didnt have before
    2. **Modelling**
        - be able to apply satistical, maethematical, and ML techiniques to data, in order to explain processes or relationships contained within it and to perform some sort of **Prediction**
    3. Working with Customer or User
        - The role has some more business-directed elements
        - the previous points support decision making in an organization
        - done by presenting findings in Powerpoints or Jupyter notebooks
        - communincation and business acumen in a way that goes beyone classic tech roles

### ML Engineer:
* argued as most important role in tech
* data scienteist would usually focus on translating the business requirements into a working speech-to-text model, containing complex elements and showing it can be done in principle
* the engineer's job is to then turn it into a product, service, or tool that can be used in production
* building software to train, retrain, deploy, and track performance etc
* key areas:
    1. **Translation**
        - taking models and research code in a variety of formats and translating them into robust pieces of code
        - This can be done through *Oject Orientated Programming*, functional programming, a mix etc
        - taking the proof-of-concept work of the data scientist and turn it into something that is closer to production
    2. **Architecture**
        - deployment of software will involve lots of integrated parts
        - the ML engineer has to understand how the appropriate tools and processes link together
        - ensuring success at scale
    3. **Productionization**
        - deliver a solution and understand customer's requirements inside out
        - be able to understand how that effects project development

### ML Operations Engineer(MLO):
* emerging role wth the aim of enabling ML engineers to work with higher quality, greater pace, and at a larger scale
* building tools and capabilities that enable the taks of engineers and data scientists
* key areas:
    1. **Automation**
        - increasing the levels of automation across the workflowsw through techniques such as Infrastrcuture-as-Code
        - pre-package software that can be deployed to allow for smoother deployements of solutions
        - automation scripts or standardized templates
    2. **PLatform Engineering**
        - working to integrate a series of usefel services for the different data-driven teams to use
        - developing integrations across orchestration tools
    3. **Enabling key MLOps capabilities**
        - MLOps consists of a set of practices and techniques that enable the production of ML models by the other engineers
        - model management and model monitoring are enabled by the MLOps engineers in a way that can be used at scale across multiple projects

### Data Engineer:
* responsible for the getting the commodity that everything else in the preceding section is based on A to B
* ensuring high fidelity, appropriate latency, and as little effort on the part of other team members as possible 
* key areas
    1. **Quality**
        - Getting data from A to B is pointless if the data is garbled, fields are missing, or IDs are screwed up
        - use a variety of techniques and tools to ensure that the data that left the source system is what lands in the data storage layer
    2. **Stability**
        - ensure data pipelines are robust, reliable, and can be trusted to deliver when needed
    3. **Access**
        - use a variety of tech to use with the other engineers to help build appropriate models

## Working as an Effective Team
* this section will discuss important points to consider when forming a team or even working on a team
    1. nobody can do everything
    2. blended is best
        * within a project you will need mathematics, code, engineering, project management, communication etc
    3. tie your team structure to your projects in a dynamic way

## ML Engineering in the Real World
* here are some important aspects of ML Engineering in the real world
    1. the ultimate goal is to generate **value**
    2. to be a succesful ML engineer in the real world you have to understand the tech but also the business and the customer
    3. communcation is key

* ML is ideal for cases when you want to do a semi-routine task faster, with more accuracy, or at a far larger scale than is possible with other solutions
* ex : anomaly detection of energy pricing signals, forcasting consumption
* ML is usually the answer to well framed mathematical or statiscal problem
* ML at its core is a series of algorithms that can iterate some internal paramaters based on data

## What does an ML Solution Look Like?
* the power in ML does not only lie in voice assistance or visual recognition apps
* the power of ML lies in the fact that where there is data and an appropriate problem it can be *integral* to the solution
* ex: text completion is often using a natural language model *under* the hood
* social media reccomendations 
* app forcasting arrival time are using regression 
* loan applications are passed through a classifier


* we start by considering the broad elements that constitue to **any** ML solution
    1. Storage Layer
        * endpoint of data engineering process and beginning of ML process
        * includes data for training, results from models, artifcats, important metadata
        * also considered as layer for code
    2. Compute Layer
        * where the *magic* happens(and most of the book)
        * training, testing, predicting, transformation 
    3. Application Layer
        * this is where you share the ML solutions with other systems
        * aplication database insertion to API endpoints, message queues, visualization tools
        * the layer through which customer will eventually use results
        * must be engineered to provide clean and understandable outputs

## Examples of High-level ML System Design

### Ex 1: Batch Anomaly Detection Service
    * You work for a tech-savvy taxi ride company with a fleet of thousands of cars. The organization wants to start making ride times more consistent and understand longer journeys in order to improve the customer experience and, thereby, increase retention and return business. Your ML team is employed to create an anomaly detection service to find rides that have unusual ride time or ride length behaviors. You all get to work, and your data scientists find that if you perform clustering on sets of rides using the features of ride distance and time, you can clearly identify outliers worth investigating by the operations team. The data scientists present the findings to the CTO and other stakeholders before getting the go-ahead to develop this into a service that will provide an outlier flag as a new field in one of the main tables of the company’s internal analysis tool.