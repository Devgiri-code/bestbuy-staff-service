# BestBuy Staff-Service Microservice

## Overview
The **BestBuy Staff-Service Microservice** is a lightweight RESTful application designed to manage staff information for Best Buy's internal system. It provides CRUD (Create, Read, Update, Delete) operations to handle staff details such as:

- **ID**: Unique identifier for each staff member.
- **Name**: Full name of the staff member.
- **Position**: Role of the staff member.
- **Department**: Department where the staff member works.
- **Email**: Contact email address.
- **Phone**: Contact phone number.

The microservice adheres to 12-factor app principles and is designed for cloud-native deployment.

---

## How to Use the Microservice

### Endpoints

#### 1. Create Staff
**POST** `/staff`
- **Description**: Add a new staff member.
- **Request Body** (JSON):
  ```json
  {
    "name": "John Doe",
    "position": "Manager",
    "department": "Sales",
    "email": "john.doe@bestbuy.com",
    "phone": "123-456-7890"
  }
  ```
- **Response**: Newly created staff member.

#### 2. Get All Staff
**GET** `/staff`
- **Description**: Retrieve a list of all staff members.
- **Response** (JSON):
  ```json
  [
    {
      "id": "1",
      "name": "John Doe",
      "position": "Manager",
      "department": "Sales",
      "email": "john.doe@bestbuy.com",
      "phone": "123-456-7890"
    }
  ]
  ```

#### 3. Get Staff by ID
**GET** `/staff/:id`
- **Description**: Retrieve details of a specific staff member by ID.
- **Response** (JSON):
  ```json
  {
    "id": "1",
    "name": "John Doe",
    "position": "Manager",
    "department": "Sales",
    "email": "john.doe@bestbuy.com",
    "phone": "123-456-7890"
  }
  ```

#### 4. Update Staff
**PUT** `/staff/:id`
- **Description**: Update details of a specific staff member.
- **Request Body** (JSON):
  ```json
  {
    "name": "Jane Smith",
    "position": "Assistant Manager",
    "department": "HR",
    "email": "jane.smith@bestbuy.com",
    "phone": "987-654-3210"
  }
  ```
- **Response**: Updated staff member details.

#### 5. Delete Staff
**DELETE** `/staff/:id`
- **Description**: Remove a staff member from the system.
- **Response**: Confirmation message.

---

## Tasks Completed

1. **Microservice Development**:
   - Created a RESTful service with endpoints for CRUD operations.
   - Used an in-memory data structure for storing staff details.
   - Followed 12-factor app principles, including the use of environment variables.

2. **Containerization**:
   - Developed a Dockerfile to containerize the microservice.
   - Built and pushed the Docker image to Docker Hub.

3. **Kubernetes Deployment**:
   - Created an AKS cluster using Azure CLI.
   - Wrote and deployed a Kubernetes deployment YAML file to expose the microservice.

4. **CI/CD Pipeline**:
   - Configured a GitHub Actions workflow for automated building, testing, and deployment.

5. **Documentation**:
   - Wrote comprehensive documentation in this README file.

---

## Technical Issues Encountered

1. **Issue**: Environment variables were not loading correctly in the containerized environment.
   - **Resolution**: Updated the Dockerfile to include environment variable configurations.

2. **Issue**: Kubernetes service not exposing the LoadBalancer.
   - **Resolution**: Ensured correct `type: LoadBalancer` was specified in the service YAML file and verified Azure resource configurations.

3. **Issue**: GitHub Actions workflow failing during Docker push step.
   - **Resolution**: Added Docker Hub credentials as secrets in the repository and configured the workflow accordingly.

---

## Deployment

- **Docker Image**: The Docker image is available at [Docker Hub](https://hub.docker.com/repository/docker/your-dockerhub-username/staff-service).
- **Kubernetes Cluster**: The microservice is deployed on an AKS cluster and exposed via a LoadBalancer.

---

## Getting Started

### Local Development

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/bestbuy-staff-service.git
   cd bestbuy-staff-service
   ```
2. Run the microservice:
   - Python: `python app.py`
   - Node.js: `node app.js`

### Docker

1. Build the Docker image:
   ```bash
   docker build -t staff-service:latest .
   ```
2. Run the container:
   ```bash
   docker run -p 5000:5000 staff-service:latest
   ```

### Kubernetes

1. Apply the deployment file:
   ```bash
   kubectl apply -f staff-service-deployment.yaml
   
