# PROJECT_CONTEXT.md — Actuarial Life Model Engine

## Objective

Build a clean, modular Python-based life insurance model engine that replicates the core mechanics of traditional actuarial models (e.g. Prophet), focusing on clarity, transparency, and extensibility.

This project is intended to demonstrate:

* Understanding of actuarial modelling mechanics
* Ability to translate actuarial logic into structured Python code
* Clean software design principles

---

## Project Structure

actuarial_model_engine/
│
├── model/
│   ├── assumptions.py
│   ├── policy.py
│   ├── projection.py
│   ├── valuation.py
│
├── data/
├── notebooks/
├── README.md

---

## Architecture Overview

The model is built in layered components:

### 1. Assumptions Module ✅ COMPLETE

**File:** model/assumptions.py

**Purpose:**

* Define mortality and financial assumptions

**Implemented:**

* `qx(age)` → probability of death
* `px(age)` → probability of survival
* `discount_factor(t)` → present value discounting

**Notes:**

* Uses synthetic mortality curve
* Fully tested and working

---

### 2. Policy Module 🔄 CURRENT STEP

**File:** model/policy.py

**Purpose:**
Define the policy (model point) being projected.

**Planned fields:**

* age (int)
* term (int)
* sum_assured (float)
* premium (float)
* weight (int, default = 1)

**Design principle:**

* No projection logic inside this class
* Pure data container

---

### 3. Projection Module

**File:** model/projection.py

**Purpose:**

* Project expected cashflows over time

**Core logic will include:**

* Survival tracking
* Premium inflows
* Claim outflows

**Key concept:**
All cashflows are calculated using **unconditional probabilities**

---

### 4. Valuation Module ⏳ NOT STARTED

**File:** model/valuation.py

**Purpose:**

* Discount projected cashflows
* Calculate:

  * PV premiums
  * PV claims
  * Net value

---

### 5. Portfolio Layer (Future)

**Purpose:**

* Handle multiple policies
* Aggregate results

---

## Data Strategy

* Mortality:

  * Synthetic initially
  * Replace later with real tables (e.g. ONS)

* Interest rates:

  * Flat rate initially
  * Later upgrade to yield curve

---

## Assumptions Strategy (Future-Proofing)

The current implementation uses a single `Assumptions` class with synthetic formulas.

This will evolve into a more realistic and modular structure.

### Planned evolution:

#### Stage 1 (current)

* All assumptions defined in a single Python class
* Synthetic mortality and flat interest rate

#### Stage 2 (next upgrade)

* Split assumptions into logical components:

  * mortality
  * interest rates
  * lapses
  * expenses

* Possible structure:

```
assumptions/
    mortality.py
    interest.py
    lapse.py
    expenses.py
```

#### Stage 3 (data-driven assumptions)

* Move assumptions to external data sources (CSV or similar):

```
data/
    mortality_tables/
        ons_table.csv
    yield_curves/
        base_curve.csv
```

* Assumption classes will:

  * read from these files
  * provide clean interfaces (e.g. `qx(age)`)

#### Design principle:

> The model engine should not care where assumptions come from
> (formula, CSV, database, API)

It should only interact via a clean interface.

---

### Important constraint

Even as assumptions grow:

* Avoid creating a single large, unstructured “assumptions file”
* Keep assumptions modular and logically separated
* Maintain a consistent interface across all assumption types

---


## Development Principles

* Keep modules independent
* Separate assumptions from projection logic
* Keep calculations explicit and readable
* Build incrementally and test each component
* Avoid putting logic in notebooks
* Mirror structure of real actuarial systems

---

## Architecture Rules (Strict)

These rules must be followed at all times unless explicitly stated otherwise.

### 1. No hidden dependencies

* Modules must not instantiate their own dependencies internally.
* All external inputs (e.g. assumptions) must be passed explicitly.

✅ Correct:

```python
project_cashflows(policy, assumptions)
```

❌ Incorrect:

```python
assumptions = Assumptions()  # hidden inside function
```

---

### 2. Separation of responsibilities

Each module has a single responsibility:

* `policy.py` → data only (no logic)
* `assumptions.py` → model assumptions only
* `projection.py` → cashflow mechanics only
* `valuation.py` → discounting and aggregation only

No module should take on another module’s responsibility.

---

### 3. No shortcuts without explicit acknowledgement

If a simplified or temporary implementation is used:

* It must be explicitly stated:

  * why it is a shortcut
  * what the proper implementation will be
* A clear plan must exist to refactor it later

---

### 4. Keep assumptions external to the engine

* Projection and valuation logic must not hardcode:

  * mortality
  * interest rates
  * any behavioural assumptions

All assumptions must come from the `Assumptions` module (or its future extensions).

---

### 5. Design for extensibility from the start

When adding new features, consider:

* Will this support multiple scenarios?
* Can this scale to multiple policies?
* Does this mirror real actuarial systems?

Avoid designs that would require major refactoring later.

---

## How to Continue (for new chats)

When starting a new chat, use prompts like:

* "Refer to my project context. Let’s build policy.py (Step 2)"
* "Continue to Step 3: projection module"
* "Help me extend assumptions with lapse rates"

---

## Future Extensions

* Lapse modelling
* Expenses
* Stochastic scenarios
* Multiple model points
* API or UI layer

---

## How to Work With This Project (Instructions for ChatGPT)

When helping with this project, follow these guidelines:

### 1. Always align to project structure

* Respect the module-based design:

  * assumptions → policy → projection → valuation
* Do not introduce shortcuts that break this structure

---

### 2. Explain before coding (important while learning)

* Briefly explain:

  * what we are building
  * why it is structured this way
* Then provide the code

---

### 3. Keep code simple and explicit

* Avoid overly compact or “clever” code
* Prefer clarity over efficiency
* Use readable variable names (e.g. `prob_alive`, not `p`)

---

### 4. Build incrementally

* Do not jump ahead to future modules
* Focus only on the current step unless explicitly asked
* Ensure each component works before moving on

---

### 5. Connect to actuarial concepts

* Relate code to:

  * mortality (qx, px)
  * survival probabilities
  * expected cashflows
* Highlight how this mirrors real actuarial models

---

### 6. Provide testing steps

* After writing code, include:

  * how to run it
  * what output to expect
  * what “correct behaviour” looks like

---

### 7. Avoid overengineering

* No unnecessary abstractions
* No frameworks
* Keep it close to core actuarial logic

---

### 8. Be explicit about assumptions and limitations

* If something is simplified (e.g. synthetic mortality), say so
* Explain what would change in a real model

---

### 9. Prioritise understanding over speed

* Assume the user is learning
* Break down key concepts clearly
* Avoid skipping steps

---

### 10. Stay consistent with previous modules

* New code should align with:

  * naming conventions
  * structure
  * logic already implemented

---

### 11. Enforce architecture over convenience

* If a suggested solution violates the architecture, it should be rejected
* Prefer slightly more verbose but correct designs over quick shortcuts
* Always prioritise long-term structure over short-term speed
* Always import modules, never functions, during development

---

## How to Start a New Chat

At the beginning of a new chat, the user will say something like:

* "Refer to my PROJECT_CONTEXT.md. Let’s build policy.py."
* "Refer to my project. Continue Step 3."

Use the context file as the source of truth for:

* current step
* architecture
* design principles


## Notebook Development Workflow

A Jupyter notebook is used for testing, debugging, and analysing model outputs.

### Location

notebooks/model_testing.ipynb

### Purpose

- Run projections and valuations
- Inspect intermediate outputs (e.g. cashflows, survival)
- Debug model behaviour
- Perform scenario testing

### Rules

- The notebook must NOT contain core model logic
- All calculations must reside in `.py` modules
- The notebook only calls functions from the model

### Import Pattern (MANDATORY)

Always import modules (not functions):

```python
import model.valuation as valuation