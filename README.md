![Beware of the Leopard](images/leopard.jpg)


[![Security Checks](https://github.com/BeyondMachines/beware-of-the-leopard/actions/workflows/security-checks.yml/badge.svg)](https://github.com/BeyondMachines/beware-of-the-leopard/actions/workflows/security-checks.yml)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)


> *"But the plans were on display..."*  
> *"On display? I eventually had to go down to the cellar to find them."*  
> *"That's the display department."*  
> *"With a flashlight."*  
> *"Ah, well, the lights had probably gone."*  
> *"So had the stairs."*  
> *"But look, you found the notice, didn't you?"*  
> *"Yes," said Arthur, "yes I did. It was on display in the bottom of a locked filing cabinet stuck in a disused lavatory with a sign on the door saying **'Beware of the Leopard'**."*  
> 
> — Douglas Adams, *The Hitchhiker's Guide to the Galaxy*

---

## What is This?

This is a **demo repository** showcasing good security practices and automated security checks.

Unlike the plans for demolishing Arthur Dent's house, **this repository's security controls are NOT hidden in a locked filing cabinet**. 

They're right here, properly signposted, well-documented, and actively enforced.

---

## Features

This repository demonstrates:

### **Branch Protection**
- Minimum 1 code review required
- CODEOWNERS enforcement for critical files
- All security checks must pass
- Conversations must be resolved
- No force pushes allowed

### **Automated Security Scanning**
Every pull request automatically runs three security scans:

- **Gitleaks** - Detects hardcoded secrets, API keys, passwords, and credentials
- **Semgrep** - Identifies code vulnerabilities (SQL injection, XSS, weak crypto, etc.)
- **Checkov** - Validates infrastructure security (Dockerfiles, Kubernetes, Terraform, GitHub Actions)


---

## What Gets Blocked

---

## Local Security Checks with Pre-Commit Hooks

Before pushing code to GitHub, all security checks run **locally on your computer** to catch issues immediately.

### First-Time Setup (5 minutes)

1. **Install pre-commit** (one-time only)
```bash
pip install pre-commit
```

2. **Install the git hooks**
```bash
pre-commit install
```
That's it! Hooks are now active.

### How It Works

When you commit code:
```bash
git commit -m "your changes"
```

Pre-commit hooks run automatically and check for:
- **Secrets** (API keys, passwords, tokens) via Gitleaks
- **Code vulnerabilities** (SQL injection, XSS, weak crypto) via Semgrep
- **Infrastructure security** (Dockerfiles, Kubernetes, Terraform, GitHub Actions) via Checkov

### What Happens If Issues Are Found

If security issues are detected, your commit will be blocked:
```bash
# See what failed
git status

# Fix the security issue in your editor, then retry
git add .
git commit -m "your changes"
```

Once all checks pass, your commit succeeds.

### Common Commands
```bash
# Test all hooks manually
pre-commit run --all-files

# Test specific hook
pre-commit run gitleaks --all-files

# Update hooks to latest versions
pre-commit autoupdate

# Skip hooks (emergency only - not recommended!)
git commit --no-verify
```

### Example Workflow
```bash
# Make changes
echo 'API_KEY = "sk_test_123"' > api.py

# Try to commit
git add api.py
git commit -m "Add API integration"

# Gitleaks blocks it (detects hardcoded secret)

# Fix it
echo 'import os\nAPI_KEY = os.getenv("API_KEY")' > api.py

# Retry
git add api.py
git commit -m "Add API integration"

#  All checks pass! Commit successful.
```

### Troubleshooting

**Pre-commit command not found?**
- Reinstall: `pip install --upgrade pre-commit`
- Restart your terminal

**Hooks are slow on first run?**
- First run downloads all tools (1-2 minutes)
- Subsequent commits are much faster (5-15 seconds)

**I committed something bad before installing hooks?**
- The GitHub Actions will still catch it in your PR

---

### This PR will be blocked:

```python
# Hardcoded secret (Gitleaks catches this)
API_KEY = "sk-1234567890abcdef"

# SQL injection vulnerability (Semgrep catches this)
query = f"SELECT * FROM users WHERE id = {user_id}"
cursor.execute(query)
```

```dockerfile
# Insecure Docker config (Checkov catches this)
FROM node:latest
# Running as root, using :latest tag
CMD ["npm", "start"]
```

### This PR will pass:

```python
# Secret from environment (secure!)
import os
API_KEY = os.environ.get('API_KEY')

# Parameterized query (secure!)
query = "SELECT * FROM users WHERE id = ?"
cursor.execute(query, (user_id,))
```

```dockerfile
# Secure Docker config
FROM node:18.19.0-alpine
USER node
HEALTHCHECK CMD node healthcheck.js
CMD ["node", "server.js"]
```

---

## Testing

Try these tests:

```bash
# Test 1: Add a fake secret (will fail)
git checkout -b test-secret
echo 'PASSWORD = "test123"' > test.py
git add test.py
git commit -m "Test secret detection"
git push origin test-secret
# Create PR and watch Gitleaks catch it! 🔍

# Test 2: Add SQL injection (will fail)
git checkout -b test-sqli
echo 'db.execute(f"SELECT * FROM users WHERE id={user_id}")' > unsafe.py
git add unsafe.py
git commit -m "Test SQL injection detection"
git push origin test-sqli
# Create PR and watch Semgrep catch it! 🔎

# Test 3: Add insecure Dockerfile (will fail)
git checkout -b test-docker
echo 'FROM ubuntu:latest' > Dockerfile
git add Dockerfile
git commit -m "Test Docker security"
git push origin test-docker
# Create PR and watch Checkov catch it! 🏗️
```

## Support

Remember: **Don't Panic** 


- **Questions**: Open an issue
- **Security Officer**: Contact [contact@beyondmachines.com](mailto:contact@beyondmachines.com)


## Acknowledgments

- **Douglas Adams** - For the leopard
- **Gitleaks** - Secret detection ([gitleaks.io](https://gitleaks.io))
- **Semgrep** - Code security analysis ([semgrep.dev](https://semgrep.dev))
- **Checkov** - Infrastructure scanning ([checkov.io](https://www.checkov.io))


---

## Learn More

- [BeyondMachines](https://beyondmachines.net/)
- [YieldCat intentionally vulnerable platform](https://yieldcat.com/)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [CWE Top 25](https://cwe.mitre.org/top25/)
- [NIST Secure Software Development Framework](https://csrc.nist.gov/Projects/ssdf)
- [GitHub Security Best Practices](https://docs.github.com/en/code-security)

---

**Made by BeyondMachines**