# Contributing Guide  
How to set up, code, test, review, and release so contributions meet our Definition of Done.

---

## Code of Conduct
All contributors are expected to maintain professionalism, inclusivity, and respect in all communications (Discord, GitHub, Teams, and meetings).  
Violations such as harassment, unprofessional language, or discrimination will result in escalation to the TA and REVOBOTS project lead.  
Issues can be reported privately to **Justice Peyton** (Communication Lead) at peytonju@oregonstate.edu.

---

## Getting Started
### Prerequisites
- ROS2 Humble or later  
- Python 3.8+  

### Setup
1. Clone the repository:
```
   git clone https://github.com/revobots/palm.git  
   cd palm  
```

2. Create and activate a virtual environment:  
```
   python -m venv venv  
   source venv/bin/activate  (Windows: venv\Scripts\activate)  
```

3. Install dependencies:  
```
   pip install -r requirements.txt 
``` 

### Run Locally
ros2 launch palm main.launch.py

---

## Branching & Workflow
We use a **trunk-based workflow**:

- **Default branch:** main  
- **Feature branches:** feature/<short-description>  
- **Bug fixes:** fix/<short-description>  
- Always pull from main before pushing.  

**Example:**  
```
git checkout -b feature/feature99 
git commit -m "feat: implement feature 99"  
git push origin feature/azure-upload 
```

---

## Issues & Planning
All work begins as a GitHub Issue.

### Labels
- bug  
- enhancement  
- documentation  
- research  

### Practices
Issues are estimated collaboratively in team meetings and assigned by domain:  
- ROS2 — Justice  
- VR/AR — Luke  
- Storage/Vision — Andrew  

Triage meetings occur Fridays at 1:30pm.

---

## Commit Messages
We follow **Conventional Commits**.

**Examples:**  
feat: add ROS2 controller communication  
fix: reduce video latency under 50ms  
docs: update README with VR streaming setup  
refactor: simplify image upload handler  

Reference related issues:  
feat: add encrypted IP communication (#42)

---

## Code Style, Linting & Formatting
**Python:** flake8 
**Config Files:** .flake8 

**Commands:** 
```  
flake8 .  
```

All PRs must pass linting before review.

---

## Testing
### Required Tests
- Integration tests for ROS2 nodes before merge  
- Manual validation for robot communication and VR streaming  

### Recommended Tests
- Unit tests for all new modules/functions

**Run tests:**  
pytest --maxfail=1 --disable-warnings -q  
---

## Pull Requests & Reviews
### PR Template Includes
- Summary of changes  
- Linked issue number  
- Screenshots (if applicable)  
- Test results or verification steps  

### Checklist
- [ ] Code passes linting and tests  
- [ ] Documentation updated  
- [ ] No hardcoded secrets  
- [ ] All CI jobs passed  

### Review Rules
- Minimum **1 approving review** from a teammate  
- REVOBOTS staff review required for merge  

---

## CI/CD
CI runs on **GitHub Actions**.

### Jobs
- lint: flake8 
- test: pytest suite  
- build: ROS2 package build  
- deploy: Azure test deployment  

All jobs must pass before merge.  
View logs in the Actions tab.

---

## Security & Secrets
### Reporting
Report vulnerabilities to Justice or REVOBOTS directly.

### Rules
Do not:
- Commit .env or credentials 
- Commit large files or datasets 

---

## Documentation Expectations
The following must be updated for each new feature:
- README.md — Setup, usage, and dependencies  
- docs/ — Design, API, and architecture details  
- Inline docstrings (Google-style preferred)  

Documentation must meet REVOBOTS’ standards for clarity and reproducibility.

---

## Release Process
**Versioning:** Semantic Versioning (MAJOR.MINOR.PATCH)  

**Tagging:**  
git tag -a v1.0.0 -m "Initial VR + ROS2 remote control release"  
git push origin v1.0.0  

**Changelog Generation:**  
Automatically via git-chglog

**Rollback Process:**  
git revert <commit-hash>  
Re-run CI/CD validation before redeploying.

---

## Support & Contact
| Name | Role | Contact | Backup |
|------|------|----------|--------|
| Justice Peyton | ROS2 & Communication Lead | peytonju@oregonstate.edu | Luke |
| Luke Hashbarger | VR/AR & Notes | hashbarl@oregonstate.edu | Justice |
| Andrew Fief | Storage/Vision & Documentation | fiefa@oregonstate.edu | Luke |

Expected response window: within 24 hours (weekdays), within 48 hours (weekends).  
For urgent technical issues, use the team Discord “#urgent” channel.

---

## Links & Artifacts
- Meeting Notes Template → docs/templates/meeting_notes.md  
- CI Dashboard → GitHub Actions tab  
- Linter/Formatter Config → .flake8, .clang-format  
- Project Docs → docs/ directory  
