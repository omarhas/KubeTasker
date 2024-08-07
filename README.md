# KubeTasker

KubeTasker is a simple Flask-based To-Do application designed to demonstrate the DevOps lifecycle, including containerization with Docker, deployment to Kubernetes, and integration with a MySQL database. The project serves as an example of how to build, test, and deploy a Python web application using modern DevOps practices.

## Features

- Create, read, update, and delete (CRUD) tasks.
- RESTful API design.
- MySQL database integration.
- Containerized using Docker.
- Deployable to a Kubernetes cluster.


## Prerequisites

- Docker
- Docker Compose
- Kubernetes cluster (Minikube, GKE, AKS, EKS, etc.)
- kubectl (Kubernetes command-line tool)

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/omarhas/KubeTasker.git
cd KubeTasker  

#### 2. Set Up the Environment

Install the required Python dependencies:

```bash
pip install -r Python/requirements.txt

## 3. Running Locally with Docker Compose

Build and start the application using Docker Compose:

docker-compose up --build

This will:

Start a MySQL container for the database.
Build and start the Flask app container.
The app will be accessible at http://localhost:5000.

