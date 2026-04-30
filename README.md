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

* **Valuation**

  * Discounted present value of premiums and claims
  * Net value calculation

* **Profit Emergence Analysis**

  * Period-by-period profit and cashflow
  * Cumulative profit and cashflow tracking
  * Profit signature (timing of profit recognition)

* **Structured Outputs**

  * Use of a `ValuationResult` object instead of ad-hoc dictionaries
  * Clear contract between valuation and analysis layers

* **Result Snapshotting**

  * Timestamped outputs (JSON + CSV) to track model changes over time

---

## Project Structure

```
actuarial_model_engine/

├── model/
│   ├── assumptions.py     # Mortality and financial assumptions
│   ├── policy.py          # Policy data (model point)
│   ├── projection.py      # Cashflow projection logic
│   ├── valuation.py       # Discounting and aggregation
│   ├── results.py         # ValuationResult object (structured output)
│   ├── analysis/
│       ├── profit.py      # Profit emergence and summary metrics
│
├── data/
│   └── results_snapshots/ # Stored model outputs (timestamped)
│
├── notebooks/
│   └── model_testing.ipynb
│
├── PROJECT_CONTEXT.md
└── README.md
```

---

## Architecture

The model is built using a layered approach:

* **Assumptions Layer**

  * Provides mortality and discounting functions
  * Fully externalised from model logic

* **Policy Layer**

  * Pure data container
  * No projection or valuation logic

* **Projection Layer**

  * Generates expected cashflows using survival probabilities

* **Valuation Layer**

  * Applies discounting
  * Produces structured outputs (`ValuationResult`)

* **Analysis Layer**

  * Interprets valuation results
  * Produces profit emergence and summary metrics

* **Notebook**

  * Orchestration and visualisation only
  * No core logic

---

## Example Outputs

Typical outputs include:

* Present value of premiums, claims, and net value
* Profit emergence table (per-period cashflows and profit)
* Profit signature (distribution of profit over time)
* Visualisations:

  * Cumulative cashflow vs cumulative profit
  * Profit signature chart

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

4. Run the notebook:

```bash
jupyter notebook notebooks/model_testing.ipynb
```

---

## Design Principles

This project enforces several core principles:

* **No hidden dependencies**

  * All inputs are explicitly passed between components

* **Separation of concerns**

  * Each module has a single responsibility

* **Extensibility**

  * Designed to support future features (portfolio modelling, scenarios, etc.)

* **Reproducibility**

  * Results can be persisted and compared over time

* **Clarity over shortcuts**

  * Preference for transparent logic over quick implementations

---

## Current Limitations

* Uses a synthetic mortality curve (not yet based on real data)
* Single-policy valuation only (no portfolio layer yet)
* Deterministic (no stochastic scenarios)
* Limited assumption set (no lapse, expenses, etc.)

---

## Roadmap

Planned extensions include:

* Portfolio layer (multiple policies and aggregation)
* Modular assumptions framework (mortality tables, yield curves)
* Additional metrics (e.g. BEL, IRR)
* Scenario and stress testing
* Performance improvements for larger datasets

---

## Disclaimer

This is a personal learning project intended to explore actuarial modelling concepts and software design. It is not intended for production or regulatory use.

---

## Feedback

This project is actively being developed, and feedback is very welcome.

In particular, I’d be interested in:

* Whether the structure reflects how models are implemented in practice
* Any gaps in valuation or profit emergence logic
* Suggestions for scaling or extending the model

---

## Author

Ajay Sehdev
