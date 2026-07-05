🚀 CloudOps Employee Portal — CI/CD Deployment on AWS EC2

📌 Project Overview
This project demonstrates a fully automated CI/CD pipeline for deploying a Flask-based Employee Management Web Application on an AWS EC2 instance using GitHub Actions and SSH-based deployment.

Every code push to the main branch automatically triggers deployment to the EC2 server, ensuring fast, reliable, and repeatable releases.

🏗️ Architecture

The system follows a simple CI/CD deployment workflow:
Developer pushes code to GitHub
GitHub Actions triggers CI/CD pipeline
SSH connects to AWS EC2 instance
Latest code is pulled and dependencies installed
Gunicorn service is restarted
Application is live instantly

📌 Architecture Diagram:

![Architecture Diagram](architecture.png)

⚙️ Tech Stack
🖥️ Backend
Python
Flask

☁️ Cloud & Deployment
AWS EC2 (Ubuntu)
GitHub Actions (CI/CD)
SSH Key-based Authentication

⚙️ Server Setup
Gunicorn (WSGI Server)
systemd (Service Management)

📦 Version Control
Git & GitHub

🚀 CI/CD Workflow
Developer pushes code to GitHub (main branch)
GitHub Actions workflow is triggered
Repository is cloned on runner
SSH connection established with EC2
Latest code is pulled from GitHub
Dependencies installed using pip
Gunicorn service is restarted

Application is live 🎉

📂 Project Structure
cloudops-employee-portal/
│
├── app.py
├── models.py
├── routes.py
├── config.py
├── requirements.txt
│
├── templates/
├── static/
├── uploads/
│
├── s3_config.py
├── database/
│
└── .github/workflows/
    └── deploy.yml


🔐 Security Features
SSH Key-based authentication (no password login)
Security Group controlled access (port 22, 5000)
Restricted EC2 access
Environment-based deployment

🖥️ Deployment Details
EC2 Setup
Ubuntu Server on AWS EC2
Gunicorn used as WSGI server
systemd ensures auto-restart on failure
Run Application Manually
python3 app.py
Production Run (Gunicorn)
gunicorn -w 4 -b 0.0.0.0:5000 app:app

🔄 GitHub Actions CI/CD
Workflow triggers on every push to main:
on:
  push:
    branches:
      - main
Deployment includes:
SSH connection to EC2
Git pull latest code
Install dependencies
Restart Gunicorn service

📊 Key Features

🔁 Fully automated deployment
☁️ Cloud-based AWS hosting
⚡ Fast deployment via GitHub Actions
🔐 Secure SSH authentication
📦 Production-ready Gunicorn setup
🎯 Learning Outcomes
AWS EC2 deployment
CI/CD pipeline design
GitHub Actions automation
Linux server management
Flask production deployment
SSH-based secure deployment

📸 Screenshots

Add your screenshots here:
GitHub Actions success
EC2 running instance
Live Flask app UI


👨‍💻 Author

Tarfi Ansari
Aspiring Cloud & DevOps Engineer

Skills: AWS | Linux | GitHub Actions | Python | Flask | CI/CD

⭐ If you like this project
Give it a ⭐ on GitHub and connect on LinkedIn!
