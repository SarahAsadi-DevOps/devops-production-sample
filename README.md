# FastAPI DevOps Portfolio

A production-ready FastAPI application demonstrating modern DevOps practices including Docker containerization, Kubernetes deployment with Helm, and automated CI/CD pipelines with GitHub Actions.

## Tech Stack

- **Backend**: FastAPI, Python 3.11
- **Containerization**: Docker, Docker Compose
- **Orchestration**: Kubernetes, Helm 3
- **CI/CD**: GitHub Actions
- **Testing**: Pytest, HTTPX

## Project Structure

├── .github/

│ └── workflows/

│ ├── ci.yaml

│ └── cd.yaml

├── app/

│ ├── init.py

│ ├── main.py

│ └── requirements.txt

├── helm/

│ └── fastapi/

│ ├── Chart.yaml

│ ├── values.yaml

│ ├── values-dev.yaml

│ ├── values-prod.yaml

│ └── templates/

│ ├── deployment.yaml

│ ├── service.yaml

│ ├── ingress.yaml

│ ├── hpa.yaml

│ └── \_helpers.tpl

├── k8s/

│ └── namespaces.yaml

├── tests/

│ ├── test_main.py

│ └── requirements-dev.txt

├── docker-compose.yaml

├── Dockerfile

├── LICENSE

└── README.md

---

## API Endpoints

| Method | Endpoint         | Description          |
| :----- | :--------------- | :------------------- |
| GET    | /                | Root welcome message |
| GET    | /health          | Health check         |
| GET    | /items/{item_id} | Get item by ID       |

---

## Run Locally

### With Docker Compose

```bash
docker compose up --build

App will be available at http://localhost:8000

Without Docker
cd app
pip install -r requirements.txt
uvicorn main:app --reload

Testing
pip install -r tests/requirements-dev.txt
pytest tests/ -v

Build
docker build -t fastapi-devops:latest .

Push to Docker Hub
docker tag fastapi-devops:latest <sarahasadi>/fastapi-devops:latest
docker push <sarahasadi>/fastapi-devops:latest

Kubernetes Deployment (Helm)
Prerequisites
Kubernetes cluster running locally (e.g., kind, minikube) or remotely
Helm 3 installed
1. Create Namespaces
Apply the necessary namespaces:
kubectl apply -f k8s/namespaces.yaml

2. Deploy
To Dev:
helm upgrade --install fastapi ./helm/fastapi \
  -f helm/fastapi/values-dev.yaml \
  --namespace dev

To Prod:
helm upgrade --install fastapi ./helm/fastapi \
  -f helm/fastapi/values-prod.yaml \
  --namespace prod

3. Verify Deployment
# Check pods in the 'dev' namespace
kubectl get pods -n dev

# Check services in the 'dev' namespace
kubectl get svc -n dev

# Check ingresses in the 'dev' namespace
kubectl get ingress -n dev

CI/CD
Automated pipelines are configured with GitHub Actions.

Workflows

```
