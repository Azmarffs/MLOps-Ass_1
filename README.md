# ML App CI/CD Pipeline

This  repository contains a Flask-based ML web app with CI/CD using GitHub Actions and Jenkins.

## Quickstart

- Install dependencies:
```bash
pip install -r requirements.txt
```

- Train a simple model (expects `src/data/dataset.csv` with a `target` column):
```bash
python src/model/train.py
```

- Run the app locally:
```bash
python src/app.py
```

- Build and run Docker:
```bash
docker build -t ml-app:local .
docker run -p 5000:5000 ml-app:local
```

## Branching
- main/master: production
- test: pre-prod testing (PRs from dev)
- dev: default branch for features

## CI/CD
- Code quality on pushes/PRs to `dev`
- Unit tests on PRs targeting `test`
- Jenkins builds and pushes Docker image on merges to `master`, with email notifications
