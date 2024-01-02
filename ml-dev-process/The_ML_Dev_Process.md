# Chapter 2: The Machine Learning Development Process

## Intro 
* the chapter will cover.
    - how to organize a successful ML Project
    - how to set up the tools for each stage of the process
    - highlet some important best practices with real ML code examples
    - Detailed examples of continous integration/continous deployment (CI/CD) using Github Actions
    - focus heavy on the 3 step methedology of *discover, play, develop, deploy* workflow
    - this will be compared with CRISP-DM methodology 
    - the appropriate development tooling and its config and integration for succesful project
    - consider version control strategies and their basic implementation
    - setting up CI/CD for your ML proj
    - introduce potential execution environemtns as the target destination for ML solutions
    - By the end of this chapter you will be set up for success in your Python ML engineering project

## Setting up Tools
* at a high level we need 4 things
    1. Somewhere to code
        - Pycharm
        - VS Code
    2. something to track our code changes
        - Github
    3. something to help manage our tasks
        - Jira
    4. somewhere to provision infrastructure and deploy our solution
        - Modern ML engineering is dependent on succesful implentation of cloud tech
        - AWS, Azure, GCP

## Concept to Solution in Four Steps
* all ML projects are unique in some way but broadly speaking, all successful ML projects actually have 4 things in common
    1. Discover
        * clarity on the business question
        * clear arguments for ML over another approach
        * Definiton of the KPIs and metrics you want to optimize
        * a sketch of the route to value
    2. PLay
        * Detailed understanding of the data
        * working proof of concept
        * agreement on the model/algo/logic that will solve the problem
        * evidence that a solution is doable within realistic resource scnearios
        * evidence that good ROI can be achieved
    3. Develop
        * a working solution that can be hosted on appropriate and available infrastructure
        * thorough test results and performance metrics ( for algos and software )
        * an agreed retraining and model deployment strategy
        * unit tests, integration tests, and regression tests
        * solution packaging and pipelines
    4. Deploy
        * a working and tested deployment process
        * provisioned infrastructure with appropriate security and performance characteristics
        * mode retraining and management processes
        * an end-to-end working solution 
    
## Comparison to CRISP-DM (Cross-Industry Standard Process for Data Mining)
* the high-level categorization of project steps that are outlined later have many similarities to CRISP-DM
* there are 6 different phases of activity
    1. Business Understanding - Discover
    2. Data Understanding - Discover
    3. Data preperation - Play
    4. Modeling - Play and Develop
    5. Evaluation  - Develop and Deploy
    6. Deployment - 

## Deep Dive into the Four Steps

### 1. Discover
* before working to build any solution it is important that you understand the problem 
* key things to do during the discovery phase
    * understand end user requirements in detail
    * document everything as you will be judged on how well you deliver against the requirements
    * define metrics that matter
    * start finding out where the data lives 

### 2. Play
* the aim to to work out whether solving the task is feasible
* may employ usual techniques of exploratory data analysis and explanatory modelling 
* explore realms of possibility 
* gaining in depth understanding of the data and the problem 
* do not worry if code is of highest quality as it is not production ready


### 3. Develop
* a lot of the best practices and techniques are reused from project to project
* below are examples of methodologies, processes, and considerations that can be deployed in the dev phase of our ML eng project

#### Waterfall methodologies
* covers project workflows that fit natrually with the idea of building something complex
* there are distinct and sequential phases of work
* ex: requirements, gathering, analysis, design, development, testing, deployment
* the key here is that when you are in one phase you only focus on that one thing

#### Agile
*  at the heart of Agile development are the ideas of flexibility, iteration, incremental updates, failing fast, and adapting to changing requirements
* finding the balance between experimentation and delivery
* two variants that are extremely popular: **Scrum** and **Kanban**
* Scrum projects are centered around short units of work called sprints: make additions to product from ideation through to deployment
* Kanban projects aim to achieve a steady flow of tasks from an organized backloh

### 4. Deploy
* to be succesfully deploy our solution we need to 
- first know our deployment options: what infrastructure is available and is appropriate for the task?
- then get the solution in our development environment onto a the production infrasctructure
* this is where the concepts of DevOps and MLOps come into play 

#### Knowing your Deployment Options

##### On Premises Deployment
* deploy our solutions in-house on owned infrasctructure
* popular for large institutions with legacy software and regulatory constraints on data location and processing
* requires alot more involvement from other teams 
* big advantage of security 
* requires larger investment upfront for hardware 

##### Infrasctructur-as-a-Service
* lowest levels of abstraction for cloud deployment
* based on concept of virtualization
* no need for maintenance
* allows for scalability by scaling up Iaas srequest
* maximizes control but minimizes ease 
* ex: AWS, S3, EC2

##### Platform-as-a-Service
* provides lots of capabilities without needing to understand the underlying structure
* focus solely on dev tasks that the platform supports
* ex : AWS Lambda functions

#### Understanding DevOps and MLOps
* powerful idea in modern software dev to continously update code (CI/CD)
* testing, integrating, building, packaaging, and deploying should be as automated as possible
* 3 lifecycle stages
1. Dev
    * Testing
        - Unit tests: tests aimed at testing the functionality smallest pieces of code. -> pytest or unittest
        - Integration tests: ensure that interfaces within the code and to other solutions work. -> Selenium
        - Acceptance tests: business focused tests. -> Behave
        - UI tests: ensuring any frontends behave as expected.
    * Linting
    * Formatting
    * Building
2. ML
    * Training
    * Predicting
    * Building
        - sklearn pipelines
        - spark ML
        - zenML
    * Staging
        - MLflow
        - Comet.ml
    * Monitoring
        - Seldon
        - Neptune.ai
        - Evidently.ai
        - Arthur.ai
3. Operations
    * Releasing
        - Twine
        - Pip
        - GitHub
        - BitBucket
    * Deploying
        - Docker
        - Github Actions
        - Jenkins
        - TravisCI
        CircleCI
    * Monitoring
        - DataDog
        - Dynatrace
        - Prometheus
    
#### Continous Model Performance Testing
* take some base reference data and start to build some different tests to give confidence that the model will perform
* before this we need a few things
    1. Within actions or tests you need to retrieve reference data for model validation
    2. Retrieve the models you wish to test
    3. define tests that you want to run that are not too senstitive but also not too geared towards the data set
