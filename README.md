# URL Health Checker

A Python-based DevOps tool that checks website availability and response times. The project is containerized with Docker and includes a GitHub Actions CI pipeline.

## Features

- Checks multiple URLs from a configuration file
- Reports HTTP status codes
- Measures response time
- Handles unreachable websites
- Creates health check logs
- Runs inside Docker
- Automated testing with GitHub Actions

## Project Structure
url-health-checker/
├── .github/
│ └── workflows/
│ └── ci.yml
├── Dockerfile
├── healthcheck.py
├── requirements.txt
├── urls.txt
└── README.md

## Technologies Used

- Python
- Docker
- Git
- GitHub Actions
- Linux

## Run Locally

Clone the repository:

```bash
git clone https://github.com/imagineer-ty/url-health-checker.git


#Enter project 
cd url-health-checker

#Install dependencies
python -m pip install -r requirements.txt

#Run the health checker
python healthcheck.py

# RUN WITH DOCKER---------------------------------------------

#Build the image
docker build -t url-health-checker

# Run the container
docker run --rm url-health-checker

CI Pipeline

GitHub Actions automatically runs when code is pushed to the main branch.

The pipeline:

Checks out the repository
Installs Python
Installs dependencies
Runs the health checker
Builds the Docker image
Tests the Docker container
Future Improvements
Add JSON reporting
Add Prometheus metrics
Add monitoring dashboard
Add scheduled health checks