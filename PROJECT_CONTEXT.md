# PROJECT_CONTEXT.md — Actuarial Life Model Engine

## Objective

Build a clean, modular Python-based life insurance model engine that replicates the core mechanics of traditional actuarial models (e.g. Prophet), focusing on clarity, transparency, and extensibility.

This project demonstrates:

- Understanding of actuarial modelling mechanics  
- Ability to translate actuarial logic into structured Python code  
- Strong software design and development discipline  

---

## Project Structure

actuarial_model_engine/

├── model/  
│   ├── assumptions.py  
│   ├── policy.py  
│   ├── projection.py  
│   ├── valuation.py  
│  
├── data/  
├── notebooks/  
├── README.md  
├── PROJECT_CONTEXT.md  

---

## Architecture Overview

The model is built in layered components:

---

### 1. Assumptions Module ✅ COMPLETE

**File:** model/assumptions.py  

**Purpose:**

- Define mortality and financial assumptions  

**Implemented:**

- qx(age) → probability of death  
- px(age) → probability of survival  
- discount_factor(t) → present value discounting  

**Notes:**

- Uses synthetic mortality curve  
- Fully tested and working  

---

### 2. Policy Module ✅ COMPLETE

**File:** model/policy.py  

**Purpose:**

Defines the policy (model point).

**Fields:**

- age (int)  
- term (int)  
- sum_assured (float)  
- premium (float)  
- weight (int, default = 1)  

**Design principle:**

- Pure data container  
- No projection or valuation logic  

---

### 3. Projection Module ✅ COMPLETE

**File:** model/projection.py  

**Purpose:**

- Project expected cashflows over time  

**Core logic:**

- Survival tracking  
- Premium inflows  
- Claim outflows  

**Key concept:**

All cashflows are calculated using unconditional probabilities.

---

### 4. Valuation Module 🔄 IN PROGRESS

**File:** model/valuation.py  

**Purpose:**

- Discount projected cashflows  
- Calculate:
  - PV premiums  
  - PV claims  
  - Net value  

**Next extension:**

- Profit emergence analysis  

---

### 5. Portfolio Layer (Future)

**Purpose:**

- Handle multiple policies  
- Aggregate results  

---

## Data Strategy

- Mortality:
  - Synthetic initially  
  - Replace later with real tables (e.g. ONS)  

- Interest rates:
  - Flat rate initially  
  - Later upgrade to yield curve  

---

## Assumptions Strategy (Future-Proofing)

### Stage 1 (current)

- Single Assumptions class  
- Synthetic mortality + flat interest  

---

### Stage 2

Split into components:

assumptions/  
    mortality.py  
    interest.py  
    lapse.py  
    expenses.py  

---

### Stage 3 (data-driven)

data/  
    mortality_tables/  
    yield_curves/  

Assumption classes will:

- read from data sources  
- expose clean interfaces (e.g. qx(age))  

---

### Design Principle

The model engine must not care where assumptions come from  
(formula, CSV, database, API).

---

## Architecture Rules (Strict)

These must always be followed.

---

### 1. No hidden dependencies

Do NOT instantiate dependencies inside functions.

Correct:

project_cashflows(policy, assumptions)

Incorrect:

assumptions = Assumptions()

---

### 2. Separation of responsibilities

- policy.py → data only  
- assumptions.py → assumptions only  
- projection.py → cashflow mechanics  
- valuation.py → discounting and aggregation  

---

### 3. No shortcuts without explicit acknowledgement

If simplifying:

- explain why  
- define proper future version  
- plan refactor  

---

### 4. Keep assumptions external

Do not hardcode:

- mortality  
- interest rates  
- behaviour  

---

### 5. Design for extensibility

Always consider:

- multiple scenarios  
- scalability  
- alignment with real actuarial systems  

---

### 6. Enforce architecture over convenience

- Prefer clarity over speed  
- Reject designs that break structure  
- Always import modules, not functions  

---

## Development Principles

- Keep modules independent  
- Keep logic explicit and readable  
- Build incrementally  
- Avoid logic in notebooks  
- Mirror real actuarial systems  

---

## Development Environment & Session Discipline (CRITICAL)

Environment contamination is a major risk when working across multiple projects.

---

### Core Principle

Always assume you are switching from another project.  
Never trust the current terminal or environment state.

---

## Mandatory Startup Checklist (EVERY SESSION)

### 1. Open correct project folder

D:\actuarial_models\life_model_engine

---

### 2. Open a NEW terminal

Do not reuse an existing terminal.

---

### 3. Check Python BEFORE activation

Get-Command python

---

### 4. Activate venv

.\venv\Scripts\Activate

---

### 5. Verify Python AGAIN (CRITICAL)

Get-Command python

Expected:

D:\actuarial_models\life_model_engine\venv\Scripts\python.exe

If incorrect:

- STOP  
- Fix environment before continuing  

---

### 6. Sync Git

git pull

---

### 7. Open notebook & select kernel

Ensure kernel = project venv

---

### 8. Run all cells

Run → Run All

---

## Environment Rules

### 1. Never trust (venv) prompt

Always verify using:

Get-Command python

---

### 2. Never mix environments across projects

Each project must have:

- its own venv  
- its own dependencies  

---

### 3. Avoid Anaconda

Use:

- venv  
- requirements.txt  

---

### 4. Reset environment if inconsistent

deactivate  
Remove-Item venv -Recurse -Force  
python -m venv venv  
.\venv\Scripts\Activate  
pip install -r requirements.txt  

---

## Notebook Rules

- Notebook is for orchestration and analysis only  
- No core logic  
- Never rely on previous execution state  
- Always run full notebook  

---

## Git Discipline

- Always pull before starting work  
- Avoid committing unintended structural changes  
- Reset if unsure:

git fetch origin  
git reset --hard origin/main  
git clean -fd  

---

## Failure Handling Principle

Do not patch blindly.  
Reset to a clean state and verify.

---

## Notebook Development Workflow

Location:

notebooks/model_testing.ipynb

---

### Purpose

- Run projections and valuations  
- Inspect intermediate outputs  
- Debug model behaviour  
- Perform scenario testing  

---

### Rules

- No core logic in notebook  
- Notebook only calls module functions  

---

### Import Pattern (MANDATORY)

import model.valuation as valuation

---

## How to Continue (for new chats)

Use prompts like:

- "Refer to my PROJECT_CONTEXT.md. Continue valuation module"
- "Implement profit emergence"
- "Extend assumptions with lapse rates"

---

## Future Extensions

- Lapse modelling  
- Expenses  
- Stochastic scenarios  
- Portfolio aggregation  
- API or UI layer  

---

## Key Philosophy

This project enforces:

- No hidden dependencies (code and environment)  
- Clear separation of concerns  
- Full reproducibility at all times  