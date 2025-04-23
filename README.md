# RPG Character Style Recommender — MLOps Demo

A prompt-driven LLM service that recommends RPG character classes, gear, and backstory based on player preferences.  
**Every prompt change is tracked, tested, and deployed via a real MLOps pipeline.**

---

## 🏗️ Architecture Overview

- **Prompt-as-Model:** Prompts are versioned, tested, and promoted like ML models.
- **Pipeline:** DVC stages: generate → evaluate → package → deploy.
- **Experiment Tracking:** Weights & Biases logs prompt versions, latency, and quality.
- **CI/CD:** GitHub Actions runs lint/tests, DVC, and deploys to staging/prod.
- **Monitoring:** Logs API metrics, detects drift, and triggers alerts.

---

## 📁 Project Structure

```
mlops-demo/
├── .github/workflows/         # CI/CD pipelines
├── config/                    # Config files (env, registry, etc.)
├── data/                      # Input data (versioned by DVC)
│   └── test_inputs.json
├── outputs/                   # Model/prompt outputs (DVC tracked)
├── prompts/                   # Prompt templates (versioned)
│   └── recommend.txt
├── src/
│   ├── app.py                 # Flask API server
│   ├── generate.py            # Prompt runner + W&B logging
│   ├── evaluate.py            # Output quality checks
│   ├── registry.py            # Promotion/rollback logic
│   └── ...                    # Utilities, monitoring, etc.
├── tests/                     # Pytest suite (unit, regression)
├── dvc.yaml                   # Pipeline definition
├── pyproject.toml             # Poetry env
├── Dockerfile                 # Containerization
├── .gitignore
└── README.md
```

---

## 🚀 Quickstart

```bash
poetry install
dvc pull
dvc repro recommend
poetry run python src/app.py
```

---

## 🧪 Testing

```bash
pytest
```

---

## 🛠️ CI/CD

- PR: Lint, test, DVC, W&B log, deploy to staging
- Merge to main: Promote prompt, deploy to prod (canary)

---

## 📊 Monitoring

- API logs to W&B/Prometheus
- Drift detection and nightly eval

---

## 📜 License

MIT
