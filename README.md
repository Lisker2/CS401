# 2023 Spring Term CS401

This is a repository including three projects assigned during the session.

## Project 1

Cloud computing and Big Data represent technically different terms, but they are often seen together because of the strong interaction between them. While Big Data simply refers to the capacity to deal with a large amount of data using parallel paradigms, cloud computing usually refers to the processing of anything, including Big Data programs. The cloud, however, provides the compute and storage resources needed to process large amounts of data using parallel paradigms. The cloud provides access to computational resources previously unavailable to many organizations.

In this project, students will get experience with Spark, one of the most popular Big Data frameworks that have been adopted for use in cloud systems to date.

### Statistics about songs duration
- Generate a table containing the minimum, average and maximum duration, in milliseconds, of the songs in the dataset.
- Compute the first and third quartiles.
- Compute the set of songs with durations that are not outliers, as defined by the IQRR methodology. 
- Using the IQRR methodology, how many songs would be considered outliers and removed from analysis? Generate a new table containing the minimum, average and maximum duration of the remaining songs.

### Finding the most popular artists over time
Finding popular artists can be interesting to analyze user tendencies and to inform organizations preparing advertising campaigns. In this task, find the five most popular artists ranked by the number of playlists they appear in. Create a chart that shows the number of playlists containing each of these five artists over the years. Consider that an artist is present in a playlist after each playlist's last modification date.

### Playlists's behavior

Playlist to collect different songs by user preference, musical genre, or a variety of other relationships. In this sense, your task is analyzing how playlists are being created. What is more common, playlists where there are many songs by the same artist or playlists with more diverse songs? To answer this question, compute the prevalence of the most frequent artist in each playlist, defined as the fraction of songs by the most frequent artist. Then create a Cumulative Distribution Function (CDF) plot containing the distribution of artist prevalence across all playlists.

## Project 2
DevOps is a combination of practices and tools that increases an organization's ability to deliver applications and services at high velocity: helping organizations evolve and improve products at a faster pace than other organizations using traditional software development and infrastructure management processes.

Cloud computing is an important technology that aids in just about every step of a successful DevOps operation. Cloud computing enables collaboration without all the downtime of sending files back and forth to team members. The cloud, along with other tools like version control (Git), containers (Docker and Kubernetes), and patterns like microservices allows for simultaneous development and advanced experimental test environments for quickly prototyping solutions, enabling frequent updates, and speeding up delivery.

Continuous integration is a practice where developers regularly merge their code changes into a central repository, after which automated builds and tests are run. The key goals of continuous integration are to find and address bugs quicker, improve software quality, and reduce the time it takes to validate and release new software updates. Continuous delivery complements of continuous integration. Continuous delivery consists of automating deployment actions that were previously performed manually.

### Playlist Rules Generator

#### ML

We will develop code to generate association rules for the recommendation system to use. More specifically, we will apply a Frequent Itemset Mining algorithm to find frequent patterns and their rules (if A, then B), which will ultimately allow the recommendation of playlists that users may enjoy.

#### REST API Server

We will also implement a server that receives requests for playlist recommendations through a REST API. Students are free to choose the framework and language used to build the REST API. In Python, Flask or Fast API are widely used to expose a REST interface and are a good fit for a microservice architecture. The server should expose a REST endpoint at http://<ip>:<port>/api/recommend that responds to requests. A request will contain a list of songs the user likes, and the response should contain playlist recommendations.

### Continuous Integration and Continuous Delivery

#### Create Docker Containers
You should create two Docker containers. One is the ML container, which will generate rules for the recommendation model and save them (e.g., using the pickle module). The other is the frontend container which will read the ML model and make it accessible through a REST API (e.g., by running Flask). Users will send requests to the frontend container when using the playlist recommendation service. This involves writing two Dockerfiles, one for each container.

The ML container should only contain the rule generation code, it should not include the dataset. Similarly, your frontend container should include only the REST API server code, it should not include the generated rules for playlist recommendation. (We will discuss below how each container will access their data.)
  
#### Configure the Kubernetes deployment and service

Write a YAML file specifying a Kubernetes deployment. A deployment specifies your application's pods (i.e., what containers each pod has) and how each should be deployed (e.g., the number of pod replicas). A deployment also specifies metadata that can be used to identify your application.

Write a YAML file specifying a Kubernetes service. A service specifies a publicly-accessible application. A service tells Kubernetes that requests to your port should be sent to your application's pods.
  
#### Configure Automatic Deployment in ArgoCD
Automate the deployment of your application in ArgoCD. Push the files containing the specifications of your deployment and service (previous step) to a Git repository. Then configure ArgoCD to monitor this repository and automatically deploy and update your application on the cluster whenever the files change. Note that your repository should point ArgoCD to changes in (i) the Kubernetes configuration (deployment and service files), (ii) code changes (identified by the tag in the Docker image), and (iii) dataset updates (identified by some property of the dataset like the date).
  
### Exercise and Evaluate Continuous Delivery

Perform tests on the CI/CD infrastructure and write a discussion in a PDF to submit on Sakai. In particular, test that ArgoCD redeploys your container when you update (i) your Kubernetes deployment (e.g., increase or reduce the number of replicas), (ii) your code, and (iii) the training dataset. Measure how long the CI/CD pipeline takes to update the deployment by continuously issuing requests using your client and checking for the update in the server's responses (either the version or dataset date). Estimate if and for how long your application stays offline (inaccessible) during the update.

## Project 3
Serverless Computing and Monitoring Dashboard
  
A serverless function is a function written by a software developer for a single purpose. It is a programmatic feature of serverless computing, where the general idea is to build a piece of business logic that is both stateless (does not maintain data) and ephemeral (is used and destroyed as needed). Serverless functions are hosted and managed on infrastructure provided by cloud computing companies. These companies take care of code maintenance and execution so that developers can deploy new code faster.

To use serverless functions, all a developer has to do is write the function code and deploy it to a managed environment. A typical serverless function process is exemplified in Figure 1.
The developer writes a function that fulfills a specific purpose in the application code, such as a form mailer or measurement analysis, and defines an event that will trigger the cloud-native service provider to execute the function (for instance, an HTTP request or a time interval). When an event is triggered, the cloud service provider starts a new instance of the function if none are running. Finally, the result of the executed function is sent to the user, another function, or persisted in storage.

This paradigm is supported in many cloud providers like Google Cloud Functions (Google), AWS Lambda (Amazon AWS), and Azure Functions (Microsoft Azure), and has been used in diverse use cases such as Web applications, data manipulation, stream processing at scale, and continuous integration pipelines.

### Serveless Function and Runtime
Your serverless function should compute two stateless metrics at each point in time: the percentage of outgoing traffic bytes and the percentage of memory caching content (given by the cached and buffer memory areas). Your function should also compute a moving average utilization of each CPU over the last minute.

Your function should return a JSON-encodable dictionary containing at least P + 2 keys, where P is the number of CPUs monitored. A dictionary can be encoded in JSON if its keys are strings and its values are of type None, int, float, str, list, and dict, where the contained lists and dicts are also JSON- encodable. The keys should describe the output metric (for example avg-util- cpu1-60sec or percent-network-egress), and the values should be JSON-encodable objects that can be consumed by a monitoring dashboard (see Task 2).
### Monitoring Dashboard
Choose one dashboarding framework. There are many libraries for dashboarding data. In Python, the Plotly Dash and Streamlit frameworks are popular solutions, but students are free to choose how to build the dashboard (including frameworks not written in Python, like D3.js). 
### Serverless Runtime
In this task you will build a container image to replace the runtime image provided by the instructors. Your container image should be able to call serverless functions, passing any relevant parameters to the function and forwarding any returned values to their destinations.

In the runtime provided for this assignment, data is periodically read from Redis and passed in as parameters to the function. When the function returns, results are stored on Redis, where they can be later be read by the dashboard.

You should implement a compatible container runtime. Your container runtime must be able to replace the provided runtime and still operate with any function implemented for this assignment (assuming the function itself satisfied the integration requirements in Task 1).

  
