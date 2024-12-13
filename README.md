# BestBuy Staff-Service Microservice

## Overview
The **Staff-Service Microservice** is a RESTful API designed to manage staff information for BestBuy's internal systems. It provides CRUD (Create, Read, Update, Delete) operations for managing staff data. The microservice adheres to the 12-Factor App principles and is deployed using Docker and Kubernetes on Azure Kubernetes Service (AKS).

## Features
- **Create Staff:** Add new staff members.
- **Retrieve Staff:** Fetch details of all staff or a specific staff member.
- **Update Staff:** Modify existing staff member information.
- **Delete Staff:** Remove staff members from the system.

## Endpoints
| HTTP Method | Endpoint               | Description                 |
|-------------|------------------------|-----------------------------|
| POST        | `/staff`              | Create a new staff member   |
| GET         | `/staff`              | Retrieve all staff members  |
| GET         | `/staff/<staff_id>`   | Retrieve a specific staff   |
| PUT         | `/staff/<staff_id>`   | Update a specific staff     |
| DELETE      | `/staff/<staff_id>`   | Delete a specific staff     |

## Prerequisites
- Python 3.11
- Docker
- Kubernetes CLI (kubectl)
- Azure CLI
- Docker Hub account

## Local Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd bestbuy-staff-service
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application locally:
   ```bash
   python app.py
   ```

4. Access the API at:
   ```
http://127.0.0.1:5000
   ```

## Docker Setup
1. Build the Docker image:
   ```bash
   docker build -t devgiri616/bestbuy-staff-service:latest .
   ```

2. Run the Docker container:
   ```bash
   docker run -p 5000:5000 devgiri616/bestbuy-staff-service:latest
   ```

3. Access the API at:
   ```
   http://127.0.0.1:5000
   ```

## Kubernetes Deployment
1. Deploy to AKS:
   ```bash
   az aks get-credentials --resource-group <resource-group> --name bestbuy-aks-cluster
   kubectl apply -f staff-service-deployment.yaml
   ```

2. Verify the deployment:
   ```bash
   kubectl get pods
   ```

3. Access the service using the external IP provided by the Kubernetes LoadBalancer.

## CI/CD Pipeline
The CI/CD pipeline automates building, testing, and deploying the microservice:
- **Build:** Docker image is built using GitHub Actions.
- **Push:** Image is pushed to Docker Hub.
- **Deploy:** Kubernetes deployment is applied to AKS.

### Workflow File
See `.github/workflows/ci_cd.yaml` for pipeline details.

## Docker Hub Image
The Docker image is available at:
- [devgiri616/bestbuy-staff-service:latest](https://hub.docker.com/r/devgiri616/bestbuy-staff-service)

## Technical Challenges
- **Missing `requirements.txt`:** Resolved by verifying file existence and adjusting Dockerfile.
- **Docker Build Context:** Ensured all necessary files were included in the build context.
- **Deployment Errors:** Addressed Kubernetes YAML misconfigurations and secrets management.

## Future Improvements
- Add database integration for persistent storage.
- Implement authentication and authorization for API endpoints.
- Enhance logging and monitoring for production use.



