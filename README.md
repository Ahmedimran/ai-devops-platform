# AI DevOps / MLOps Local Lab
Complete Local CI/CD + Kubernetes + Monitoring Platform

This project is a fully local DevOps/MLOps lab running on:

- Windows 11
- WSL2 Ubuntu
- Docker Desktop
- Minikube (Kubernetes)
- GitHub Actions (CI/CD)
- Prometheus + Grafana

It provides a production‑like environment for API development, containerization,
orchestration, monitoring, and future ML model deployment.

---

## Project Structure

```text
devops-lab/
├── app/
│   ├── __init__.py
│   └── main.py
│
├── tests/
│   └── test_api.py
│
├── k8s/
│   ├── config/
│   │   ├── configmap.yaml
│   │   └── secret.yaml
│   │
│   ├── postgres/
│   │   ├── secret.yaml
│   │   ├── pvc.yaml
│   │   ├── deployment.yaml
│   │   └── service.yaml
│   │
│   ├── deployment.yaml
│   ├── service.yaml
│   └── ingress.yaml
│
├── Dockerfile
├── requirements.txt
├── pytest.ini
│
└── .github/
    └── workflows/
        └── ci.yml
---

## 🚀 FastAPI Application

The API exposes a simple health endpoint:

GET /health → {"status": "healthy"}

### Test

pytest -v

---

## 🐳 Docker Setup

### Dockerfile

FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app/main.py .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

### Local Test

docker build -t ai-devops-api:latest .
docker run --rm -p 8001:8000 ai-devops-api:latest
curl http://localhost:8001/health

---

## ☸️ Kubernetes / Minikube

### Deployment Highlights

- 2 FastAPI replicas
- ClusterIP service
- NGINX ingress routing `/`
- PostgreSQL with PVC (2GiB)
- Secrets + ConfigMaps
- Readiness probe: `/health`

### Useful Commands

kubectl get pods
kubectl get services
kubectl rollout status deployment/ai-api
minikube image load ai-devops-api:latest
minikube addons enable ingress

---

## 📡 Ingress

Enable ingress:

minikube addons enable ingress

Forward ingress controller:

minikube service ingress-nginx-controller -n ingress-nginx --url

---

## 📊 Monitoring (Prometheus + Grafana)

Install monitoring stack:

helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
kubectl create namespace monitoring
helm install monitoring prometheus-community/kube-prometheus-stack --namespace monitoring

### Grafana

kubectl port-forward -n monitoring svc/monitoring-grafana 3000:80

### Prometheus

kubectl port-forward -n monitoring svc/monitoring-kube-prometheus-prometheus 9090:9090

---

## 🤖 GitHub Actions CI/CD

### CI (GitHub-hosted runner)

- Checkout
- Python setup
- Install dependencies
- Run tests
- Build Docker image

### CD (WSL2 self-hosted runner)

- Build Docker image
- Load into Minikube
- Apply Kubernetes manifests
- Rollout status
- Show pods/services/ingress

---

## 🖥️ Self-Hosted Runner

Installed under:

~/actions-runner

Runner name:

LAPTOP-75LBDB2H

Labels:

self-hosted, Linux, X64

Start runner:

./run.sh

---

## 📈 Current Status

| Component | Status |
|----------|--------|
| FastAPI app | Working |
| pytest | Passing |
| Docker build | Working |
| Docker test | Working |
| PostgreSQL | Working |
| Kubernetes | Working |
| Ingress | Working |
| Prometheus | Healthy |
| Grafana | Accessible |
| GitHub repo | Connected |
| CI | Configured |
| Self-hosted runner | Connected |
| CI/CD workflow | Working |

---

## 🔮 Next Steps (Recommended)

- Add deployment health checks
- Add namespaces or Kustomize
- Add application metrics
- Add ML model + inference endpoint
- Add model versioning
- Add validation tests
- Add drift monitoring
- Add Terraform
- Improve secrets management

---

## 📚 Useful Commands Reference

# Project
cd ~/devops-lab

# Tests
pytest -v

# Docker
docker build -t ai-devops-api:latest .
docker run --rm -p 8001:8000 ai-devops-api:latest

# Kubernetes
kubectl get pods
kubectl rollout status deployment/ai-api

# Minikube
minikube status
minikube image load ai-devops-api:latest

# Runner
cd ~/actions-runner
./run.sh

# Grafana
kubectl port-forward -n monitoring svc/monitoring-grafana 3000:80

# Prometheus
kubectl port-forward -n monitoring svc/monitoring-kube-prometheus-prometheus 9090:9090

---

## 🏁 Key Lessons

- CI/CD machines differ; artifacts aren’t shared automatically
- Minikube image loading keeps everything local
- Repository layout matters
- Ingress provides external routing
- PVC ensures DB persistence
- Self-hosted runner bridges GitHub → local cluster
- Deterministic dependencies matter

---

# End of README
