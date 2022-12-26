# Simple Flask app
## Introduction
This project is a simple Flask app that serves as a practice for implementing CI/CD (continuous integration/continuous deployment) using GitHub Actions. The project demonstrates how to set up a pipeline to test, build, and push a Docker image to DockerHub.

## Setting Up
To use this project, you will need to have the following software installed:

* Python 3.6 or higher
* Flask
* Docker

You will also need to set up a few secrets in the repo settings in order to use GitHub Actions. Go to repo settings, in the "Secrets/Actions" section, create the following secrets:

* `DOCKER_USERNAME`: \<Your DockerHub username\>
* `DOCKER_PASSWORD`: \<Your DockerHub password\>
* `DOCKERHUB_REPO`: \<Your DockerHub username\>/\<Your repository\>
## Running the Project
To run the project locally, clone the repository and navigate to the root directory in a terminal. Then, run the following command:

```
flask run
```
This will start the Flask development server, and you should be able to access the app at http://127.0.0.1:5000/.

## GitHub Actions Workflow
The `.github/workflows` directory contains a configuration file for the GitHub Actions workflow. This workflow consists of the following steps:

1. Set up the environment. This installs any necessary dependencies and sets up the Python virtual environment.
2. Test the application. This runs the unit tests to ensure that the app is working as expected.
3. Build the Docker image. This builds a Docker image of the app, using the Dockerfile in the root directory.
4. Push the Docker image to DockerHub. This pushes the built Docker image to the specified DockerHub repository.

To run this workflow, simply push any changes to the repository. The workflow will automatically trigger, and the actions will be executed in the order specified.

## Deploying the App
To deploy the app, you can simply pull the Docker image from DockerHub and run it on any machine that has Docker installed. For example, to run the app on a server, you can use the following command:

```
docker run -d -p 5000:5000 <Your DockerHub username>/<Your repository>:latest
```
This will start the app in detached mode, listening on port 5000. You should be able to access the app at http://localhost:5000/.

## Conclusion
This project demonstrates a simple implementation of CI/CD using GitHub Actions and Docker. By setting up a pipeline to automatically test, build, and deploy the app, you can ensure that your app is always up to date and working as expected.
