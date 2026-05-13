# Actuarial Life Model Engine (Python)

## Overview

This project is a modular Python-based life insurance model engine designed to replicate the core mechanics of traditional actuarial models (e.g. Prophet-style systems).

The focus is not just on producing results, but on building a clear, extensible, and well-structured modelling framework that reflects how real-world actuarial systems are designed.

Key objectives:

* Translate actuarial concepts into clean, structured Python code
* Enforce strong separation of concerns across model components
* Ensure transparency and reproducibility of results
* Build a foundation that can scale to more complex features over time

---

## Key Features

* **Cashflow Projection**

  * Expected premiums and claims based on survival probabilities
  * Multi-decrement projection framework
  * Mortality and lapse decrement support

* **Valuation**

  * Discounted present value of premiums and claims
  * Net value calculation

* **Profit Emergence Analysis**

  * Period-by-period profit and cashflow
  * Cumulative profit and cashflow tracking
  * Portfolio-level emergence analysis
  * Decrement emergence analysis

* **Portfolio Modelling**

  * Portfolio ingestion from CSV
  * Aggregated valuation and emergence analysis
  * Weighted model point support

* **Modular Assumptions Framework**

  * Structured assumptions subsystem
  * Modular mortality, interest, and lapse assumptions
  * CSV-driven lapse assumptions
  * Segmented duration-based lapse assumptions

* **Structured Outputs**

  * Structured result objects across projection and valuation layers
  * Clear contracts between modelling and analytics layers

* **Validation Layer**

  * Input validation for portfolio ingestion
  * Separation between ingestion and modelling logic

* **Result Snapshotting**

  * Timestamped outputs (JSON + CSV) to track model changes over time

---

## Project Structure

```text
actuarial_model_engine/

├── model/
│   ├── assumptions/
│   │   ├── __init__.py
│   │   ├── assumption_set.py
│   │   ├── mortality.py
│   │   ├── interest.py
│   │   ├── lapse.py
│   │   └── loaders.py
│   │
│   ├── policy.py
│   ├── projection.py
│   ├── valuation.py
│   ├── portfolio.py
│   ├── results.py
│   ├── validation.py
│   │
│   ├── analysis/
│   │   └── profit.py
│   │
│   └── data/
│       └── loader.py
│
├── data/
│   ├── lapse_rates.csv
│   └── results_snapshots/
│
├── notebooks/
│   ├── single_policy_run.ipynb
│   └── multiple_policy_run.ipynb
│
├── PROJECT_CONTEXT.md
└── README.md
```

---

## Architecture

The model is built using a layered approach:

* **Assumptions Layer**

  * Modular assumptions subsystem
  * Projection and valuation consume only clean assumption interfaces
  * Assumption source remains externalised from engine logic

* **Policy Layer**

  * Pure modelling data container
  * Supports segmentation-relevant attributes
  * No projection or valuation logic

* **Projection Layer**

  * Generates expected cashflows using multi-decrement projection mechanics
  * Consumes assumptions through abstract interfaces only

* **Valuation Layer**

  * Applies discounting
  * Produces structured outputs (`ValuationResult`)

* **Portfolio Layer**

  * Aggregates policy-level valuation results
  * Supports portfolio emergence analysis

* **Analysis Layer**

  * Interprets valuation results
  * Produces profit emergence and summary metrics

* **Loader / Validation Layer**

  * Handles CSV ingestion and validation
  * Keeps pandas and IO outside core modelling logic

* **Notebook Layer**

  * Orchestration and visualisation only
  * No core logic

---

## Example Outputs

Typical outputs include:

* Present value of premiums, claims, and net value
* Portfolio-level valuation summaries
* Profit emergence table (per-period cashflows and profit)
* Lapse emergence analysis
* Profit signature (distribution of profit over time)
* Visualisations:

  * Cumulative cashflow vs cumulative profit
  * Profit signature chart
  * Portfolio emergence charts
  * Persistency / runoff analysis

---

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/asehdev1994/actuarial-life-model-engine.git
cd actuarial-life-model-engine
```

2. Set up a virtual environment:

```bash
python -m venv venv
.\venv\Scripts\Activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the notebooks:

```bash
jupyter notebook
```

Then open:

* `notebooks/single_policy_run.ipynb`
* `notebooks/multiple_policy_run.ipynb`

---

## Design Principles

This project enforces several core principles:

* **No hidden dependencies**

  * All inputs are explicitly passed between components

* **Separation of concerns**

  * Each module has a single responsibility

* **Externalised assumptions**

  * Projection logic is agnostic to assumption source or structure

* **Object-oriented modelling**

  * Core modelling logic uses structured domain objects instead of raw dataframes

* **Extensibility**

  * Designed to support future features (stress testing, behavioural modelling, scenarios, etc.)

* **Reproducibility**

  * Results can be persisted and compared over time

* **Clarity over shortcuts**

  * Preference for transparent logic over quick implementations

---

## Current Limitations

* Uses synthetic mortality and lapse assumptions
* Deterministic only (no stochastic scenarios)
* No expenses or surrender value modelling yet
* Simplified lapse decrement framework
* No dynamic policyholder behaviour

---

## Roadmap

Planned extensions include:

* Mortality table ingestion from external data
* Yield curve and scenario support
* Assumption stress framework
* Solvency II style stress testing
* Additional behavioural modelling
* Scenario and stress testing
* Automated regression testing
* Performance improvements for larger datasets

---

## Disclaimer

This is a personal learning project intended to explore actuarial modelling concepts and software design. It is not intended for production or regulatory use.

---

## Feedback

This project is actively being developed, and feedback is very welcome.

In particular, I’d be interested in:

* Whether the structure reflects how actuarial systems are implemented in practice
* Any gaps in valuation, decrement, or emergence logic
* Suggestions for scaling or extending the architecture

---

## Author

Ajay Sehdev