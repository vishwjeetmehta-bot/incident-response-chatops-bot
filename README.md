<div align="center">

# 🤖 Enterprise Incident Response ChatOps Bot

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Slack Bolt](https://img.shields.io/badge/Slack-Bolt_SDK-4A154B?style=for-the-badge&logo=slack&logoColor=white)](https://slack.dev/bolt-python/)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-Client_Python-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)](https://kubernetes.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](./LICENSE)

<p align="center">
  <b>Asynchronous ChatOps bot for Slack and Microsoft Teams streamlining SRE incident triage, pod CrashLoopBackOff log tailing, and automated runbook remediations with RBAC verification.</b>
</p>

</div>

---

## ⚡ ChatOps Workflow

```
SRE Engineer: /sre triage production
                    │
                    ▼
┌──────────────────────────────────────┐
│ ChatOps Orchestrator                 │
│  - Authenticates Slack User via RBAC │
│  - Queries Kubernetes API Client     │
│  - Parses OOMKilled / CrashLoop logs │
└───────────────────┬──────────────────┘
                    │
                    ▼
Interactive Slack Card:
  [ Pod: payment-service | OOMKilled ]
  [ Action: 1-Click Remediate -> Scale Memory to 512Mi ]
```

---

## 📁 Repository Layout

```
incident-response-chatops-bot/
├── .github/workflows/
│   └── ci.yml               # Syntax and execution verification
├── src/
│   ├── bot.py               # Slack/Teams event listener & slash command dispatcher
│   └── k8s_client.py        # Kubernetes cluster diagnostics interface
├── config/
│   └── runbooks.yaml        # Allowed automated incident remediation actions
├── requirements.txt
└── README.md
```

---

## 👤 Author

**Vishwjeet Kumar Mehta**  
Senior DevOps & DevSecOps Consultant | Cloud & Infrastructure Architect  
- **LinkedIn**: [linkedin.com/in/vishwjeet-mehta](https://www.linkedin.com/in/vishwjeet-mehta/)  
- **GitHub**: [@vishwjeetmehta-bot](https://github.com/vishwjeetmehta-bot)

