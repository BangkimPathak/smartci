# SmartCI - Automated CI Pipeline & Testing Framework

[![CI](https://github.com/BangkimPathak/smartci/actions/workflows/ci.yml/badge.svg)](https://github.com/BangkimPathak/smartci/actions/workflows/ci.yml)

## Student Information
- **Name:** Bangkim Pathak
- **USN:** 24BTRO006
- **Program:** B.Tech CSE (AI-Driven DevOps)
- **Course:** Cloud DevOps (24CSE538) &mdash; Unit III
- **Institution:** Jain (Deemed-to-be University), Faculty of Engineering and Technology

---

## Project Overview
`smartci` is an automated Continuous Integration (CI) and unit testing project built for **Cloud DevOps Labs 0, 1, and 2**. It demonstrates:
- Modular business logic (`pricing.py`, `cart.py`, `inventory.py`).
- Automated boundary, invalid input, and state edge-case unit testing with `pytest`.
- Fully automated CI pipeline triggered on `push` and `pull_request` via GitHub Actions.
- Build failure analysis ("Red Run" experiment), failure localization, and resolution tagging.

---

## Project Structure
```text
smartci/
├── .github/
│   └── workflows/
│       └── ci.yml              # GitHub Actions Baseline CI Workflow
├── .gitignore                  # Git ignore specification
├── pytest.ini                  # Pytest root path configuration
├── requirements.txt            # Project dependencies (pytest, requests)
├── src/
│   ├── __init__.py
│   ├── pricing.py              # apply_discount() and add_tax()
│   ├── cart.py                 # Cart items and total calculation
│   └── inventory.py            # Inventory stock management
├── tests/
│   ├── __init__.py
│   ├── test_pricing.py         # Unit & boundary tests for pricing
│   ├── test_cart.py            # Cart integration tests
│   └── test_inventory.py       # Stock edge-case & exception tests
├── scripts/                    # Automation scripts
├── ml/                         # Machine learning scaffolding
├── infra/                      # Infrastructure as Code
└── ansible/                    # Configuration management
```

---

## Local Development & Setup

### 1. Environment Setup
```bash
# Clone the repository
git clone https://github.com/BangkimPathak/smartci.git
cd smartci

# Create and activate virtual environment
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On Linux/macOS:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Running Automated Tests
```bash
pytest -v
```

Expected result:
```text
============================== 9 passed in 0.03s ==============================
```

---

## Continuous Integration Workflow (`.github/workflows/ci.yml`)
The workflow automatically executes on every commit and pull request on an ephemeral `ubuntu-latest` GitHub Actions runner VM:
1. **Checkout Repository:** `actions/checkout@v4` with `fetch-depth: 0` to retrieve complete Git commit history for diff-based analytics.
2. **Setup Python:** `actions/setup-python@v5` configured to Python 3.12.
3. **Install Dependencies:** `pip install -r requirements.txt`.
4. **Execute Tests & Log Capture:**
   ```bash
   set -o pipefail
   pytest 2>&1 | tee build.log
   ```

---

## Lab Checkpoints & Git Release Tags
| Tag | Commit Message | Description |
| :--- | :--- | :--- |
| `initial` | `Lab 0: project skeleton` | Project folder architecture and `.gitignore` |
| `lab1` | `Lab 1: app and tests` | Application modules and 9 passing unit tests |
| `lab2` | `Lab 2: Fix test assertion to restore green pipeline` | Baseline CI workflow, Red Run experiment & resolution |
