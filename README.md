# Smart Log Intelligence System

A lightweight Python system for parsing logs, detecting anomalies, and triggering alerts.

## Features
- 📖 Parse structured logs into dictionaries
- 🔍 Detect anomalies (ERROR, CRITICAL)
- 🚨 Trigger alerts (stub for Slack/email/etc.)
- 🧪 Fully tested with pytest
- 🐳 Dockerized for easy deployment
- ⚡ CI pipeline with GitHub Actions

## Quick Start
```bash
git clone https://github.com/smarada-devops/smart-log-intelligence-system.git
cd smart-log-intelligence-system
pip install -r requirements.txt
python src/main.py
