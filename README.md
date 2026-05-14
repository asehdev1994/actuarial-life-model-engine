# Actuarial Life Model Engine

A modular Python-based actuarial life insurance modelling engine designed with institutional-style architecture principles.

The project focuses not only on actuarial mechanics, but also on building a clean, extensible modelling framework with stable interfaces, externalised assumptions, structured outputs, and disciplined separation of concerns.

The engine is intentionally evolving toward reusable actuarial and quantitative risk infrastructure rather than a notebook-centric prototype model.

---

# Core Objectives

- Build a modular actuarial modelling engine using clean software architecture principles
- Separate modelling mechanics from ingestion, analytics, and orchestration
- Externalise assumptions through provider-based interfaces
- Produce structured, reusable valuation outputs
- Preserve transparency and reproducibility of calculations
- Create a foundation for future scenario, stress, and risk infrastructure

---

# Current Architecture

The engine is built using layered structured outputs:

```text
Policy
→ ProjectionRow
→ ProjectionResult
→ ValuationRow
→ ValuationResult
→ Portfolio
→ PortfolioResult
```

Core modelling logic is intentionally isolated from:
- pandas
- CSV ingestion
- validation
- analytics
- notebook orchestration
- assumption source structure

---

# Current Features

## Projection Engine

- Expected cashflow projection using unconditional probabilities
- Multi-decrement runoff framework
- Mortality and lapse decrement support
- Structured projection outputs

Projection logic remains completely assumption-agnostic.

---

## Valuation Engine

- Discounted present value calculations
- Structured valuation outputs
- Profit emergence support
- Portfolio-level aggregation

Valuation consumes only abstract discount factor interfaces.

---

## Assumptions Infrastructure

### Mortality

- CSV-driven mortality ingestion
- Gender-segmented mortality tables
- Contextual mortality resolution
- Smoker mortality overlays

### Interest Rates

- CSV-driven yield curve ingestion
- Float maturity support
- Spot-rate discounting
- Terminal extrapolation beyond observable maturities

### Lapse

- CSV-driven lapse assumptions
- Product segmentation
- Smoker segmentation
- Duration-based lapse ranges

---

# Assumptions Architecture

The engine consumes only stable provider interfaces:

```python
assumptions.qx(policy, age)
assumptions.discount_factor(t)
assumptions.lapse_rate(policy, t)
```

Projection and valuation layers remain completely unaware of:
- CSV structure
- segmentation mechanics
- market-data formatting
- assumption source logic
- provider implementation details

This abstraction boundary is a core design principle of the project.

---

# Data Ingestion Architecture

Assumption ingestion follows the architecture below:

```text
CSV/Data
↓
Loader
↓
Validation
↓
Provider
↓
AssumptionSet
↓
Projection / Valuation
```

Validation occurs only at ingestion boundaries.

The core engine assumes validated structured inputs.

---

# Design Principles

## Stable Interfaces

Projection and valuation depend only on explicit assumption interfaces.

New assumption structures should integrate without requiring engine rewrites.

---

## Separation of Concerns

Distinct responsibilities are maintained across:
- modelling
- ingestion
- validation
- analytics
- orchestration

---

## No Pandas In Core Engine

Pandas is restricted to:
- ingestion
- validation
- analytics
- notebook layers

Core engine logic operates on structured domain objects only.

---

## Structured Result Contracts

Projection and valuation outputs are represented through structured result objects rather than raw dataframes.

This supports:
- analytics reuse
- serialisation
- debugging
- downstream extensions

---

## Externalised Assumptions

Mortality, lapse, and yield curve assumptions are externally configurable and provider-driven.

Projection and valuation remain assumption-source agnostic.

---

# Example Project Structure

```text
actuarial-life-model-engine/

├── model/
│
│   ├── assumptions/
│   │   ├── assumption_set.py
│   │   ├── mortality.py
│   │   ├── interest.py
│   │   ├── lapse.py
│   │   ├── assumption_loader.py
│   │   └── assumption_validation.py
│   │
│   ├── analysis/
│   │   └── profit.py
│   │
│   ├── data/
│   │   ├── loader.py
│   │   └── validation.py
│   │
│   ├── policy.py
│   ├── projection.py
│   ├── valuation.py
│   ├── portfolio.py
│   └── results.py
│
├── data/
│   ├── mortality_tables/
│   ├── mortality_parameters/
│   ├── yield_curves/
│   ├── lapse_tables/
│   ├── portfolios/
│   └── results_snapshots/
│
├── notebooks/
│
├── README.md
└── PROJECT_CONTEXT.md
```

---

# Example Workflow

```python
policy
→ projection
→ valuation
→ portfolio aggregation
→ analytics
```

---

# Current Scope

Implemented:
- deterministic projection engine
- multi-decrement cashflow modelling
- portfolio valuation
- structured result objects
- mortality table ingestion
- yield curve ingestion
- segmented lapse assumptions
- validation framework
- reusable analytics layer

---

# Current Intentional Limitations

The following are intentionally excluded from the current version:

- stochastic economic scenarios
- interpolation
- market calibration
- behavioural modelling
- expense modelling
- surrender value mechanics
- IFRS17 mechanics
- monthly projection timing

The current focus is architectural stability and modular extensibility before introducing additional modelling complexity.

---

# Planned Extensions

Potential future directions include:
- stochastic scenario infrastructure
- stress testing
- economic scenario overlays
- expense modelling
- ALM extensions
- vectorised portfolio valuation
- regression testing
- parallelised valuation frameworks

---

# Running The Project

## Clone repository

```bash
git clone https://github.com/asehdev1994/actuarial-life-model-engine.git
cd actuarial-life-model-engine
```

---

## Create virtual environment

```bash
python -m venv venv
```

Activate:

### Windows

```bash
.\venv\Scripts\activate
```

---

## Install dependencies

```bash
pip install -r requirements.txt
```

---

## Launch notebooks

```bash
jupyter notebook
```

Primary notebooks:
- `single_policy_run.ipynb`
- `multiple_policy_run.ipynb`

---

# Development Philosophy

The project prioritises:
- clarity over shortcuts
- explicitness over hidden behaviour
- stable interfaces over convenience
- incremental extensibility over premature complexity

The long-term objective is to evolve toward reusable actuarial and quantitative risk infrastructure while preserving modelling transparency and architectural discipline.

---

# Disclaimer

This is a personal engineering and actuarial modelling project intended for learning, experimentation, and architecture exploration.

It is not intended for production, regulatory, or financial reporting use.

---

# Author

Ajay Sehdev