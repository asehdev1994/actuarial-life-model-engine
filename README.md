# Actuarial Life Model Engine

A modular Python-based actuarial life insurance modelling and capital engine designed using institutional-style software architecture principles.

The project focuses not only on actuarial mechanics, but also on building a clean, extensible modelling framework with stable interfaces, externalised assumptions, structured outputs, registry-driven extensibility, and disciplined separation of concerns.

The project has evolved beyond a traditional actuarial cashflow model toward a reusable actuarial projection, valuation, stress testing, and capital aggregation framework with configuration-driven execution and frontend orchestration.

---

# Core Objectives

* Build a modular actuarial modelling engine using clean software architecture principles
* Separate modelling mechanics from ingestion, analytics, orchestration, and presentation
* Externalise assumptions through provider-based interfaces
* Produce structured, reusable valuation and capital outputs
* Preserve transparency and reproducibility of calculations
* Build reusable scenario, stress, and capital aggregation infrastructure
* Support extensible registry-driven assumptions and stresses
* Provide a user-friendly execution interface through Streamlit

---

# Current Architecture

The engine is built using layered structured outputs:

```text
Streamlit Frontend
↓
CapitalWorkflowConfig
↓
Workflow Layer
↓
Portfolio
↓
ProjectionResult
↓
ValuationResult
↓
SCRResult
↓
AggregatedSCRResult
↓
CapitalWorkflowResult
```

Core modelling logic is intentionally isolated from:

* pandas
* CSV ingestion
* validation
* analytics
* frontend presentation
* assumption source structure
* stress calibration structure

---

# Current Architecture Status

The current architecture is considered structurally stable across:

* projection
* valuation
* assumptions infrastructure
* scenario execution
* stress infrastructure
* SCR generation
* capital aggregation
* workflow orchestration
* configuration-driven execution
* Streamlit frontend

Current development focus has shifted from core architecture toward:

* richer stresses
* reporting infrastructure
* asset-side modelling
* realism enhancements
* local AI tooling
* developer productivity

---

# Configuration Layer

The engine includes a dedicated configuration-driven execution layer.

Current workflow configuration architecture:

```text
CapitalWorkflowConfig
├── AssumptionConfig
├── ScenarioConfig
├── CorrelationConfig
└── execution settings
```

The configuration layer centralises:

* workflow execution inputs
* assumption ingestion ownership
* scenario calibration ownership
* correlation ownership

while preserving:

* provider abstraction
* stable modelling contracts
* scenario-agnostic projection
* scenario-agnostic valuation

Workflow orchestration is intentionally separated from actuarial mechanics.

---

# Registry Architecture

The engine uses registries to define extensible inventories.

## Assumption Registry

Available assumptions are defined through:

```python
ASSUMPTION_REGISTRY
```

Each assumption is represented by:

```python
AssumptionDefinition
```

containing metadata such as:

```python
name
display_name
description
config_attributes
loader
null_provider_factory
```

The registry is the single source of truth for available assumptions.

---

## Stress Registry

Available stresses are defined through:

```python
STRESS_REGISTRY
```

Each stress is represented by:

```python
StressDefinition
```

containing metadata describing:

* target assumption
* stress wrapper
* calibration ownership

Scenario execution dynamically applies stresses using registry metadata.

---

## Design Principle

Registries define inventories.

Good registry candidates:

* assumptions
* stresses

Poor registry candidates:

* workflow execution
* valuation sequencing
* result packaging

Workflow execution remains explicit.

---

# Current Features

## Projection Engine

* Expected cashflow projection using unconditional probabilities
* Multi-decrement runoff framework
* Mortality and lapse decrement support
* Structured projection outputs
* Explicit expense cashflow decomposition

Projection logic remains completely assumption-agnostic.

---

## Valuation Engine

* Discounted present value calculations
* Structured valuation outputs
* Explicit expense present value decomposition
* Profit emergence support
* Portfolio-level aggregation

Valuation consumes only abstract discount factor interfaces.

---

## Scenario & Capital Framework

The engine supports calibration-driven stress testing and hierarchical capital aggregation.

Current workflow:

```text
Base Assumptions
↓
Scenario Overlays
↓
Scenario-Adjusted Assumptions
↓
Projection
↓
Valuation
↓
Stressed BEL
↓
SCRResult
↓
Diversified Aggregation
↓
CapitalWorkflowResult
```

Projection and valuation remain completely scenario-agnostic.

Implemented scenario infrastructure:

* ScenarioDefinition
* scenario_loader
* scenario_validation
* STRESS_REGISTRY
* stressed assumption overlays

Implemented stressed providers:

* mortality stresses
* lapse stresses
* interest stresses
* expense stresses

Current capital framework supports:

* univariate SCR calculation
* life diversification
* market diversification
* BSCR aggregation
* dynamic correlation matrix subsetting

Aggregation is metadata-driven and consumes:

* SCRResult objects
* correlation matrices

The aggregation layer does NOT:

* apply stresses
* run projections
* run valuations

---

# Capital Aggregation

* Calibration-driven stress scenario execution
* Structured SCR result contracts
* Dynamic correlation matrix subsetting
* Life SCR aggregation
* Market SCR aggregation
* Hierarchical BSCR aggregation
* Metadata-driven diversification workflow

---

# Assumptions Infrastructure

## AssumptionSet

The engine consumes assumptions through:

```python
AssumptionSet
```

which acts as the single source of truth for available assumptions.

Assumptions are stored dynamically:

```python
providers: dict[str, Provider]
```

This allows new assumption types to be introduced without redesigning projection, valuation, or workflow execution.

---

## Mortality

* CSV-driven mortality ingestion
* Gender-segmented mortality tables
* Contextual mortality resolution
* Smoker mortality overlays

---

## Interest Rates

* CSV-driven yield curve ingestion
* Float maturity support
* Spot-rate discounting
* Terminal extrapolation beyond observable maturities

---

## Lapse

* CSV-driven lapse assumptions
* Product segmentation
* Smoker segmentation
* Duration-based lapse ranges

---

## Expenses

* CSV-driven expense assumptions
* Structured expense provider abstraction
* Acquisition and maintenance expense support
* Fixed and premium-linked expense mechanics

---

# Assumptions Architecture

The engine consumes only stable provider interfaces:

```python
assumptions.qx(policy, age)
assumptions.discount_factor(t)
assumptions.lapse_rate(policy, t)
assumptions.expenses(policy, t)
```

Projection and valuation remain unaware of:

* CSV structure
* segmentation mechanics
* market data formatting
* provider implementation details

This abstraction boundary is a core design principle of the project.

---

# Streamlit Frontend

The primary execution interface is now a Streamlit frontend.

Current capabilities:

* Portfolio upload
* Registry-driven assumption uploads
* Scenario upload
* Correlation matrix upload
* Workflow execution
* Results display
* Persistent file selection between application restarts

Current frontend structure:

```text
frontend/

├── app.py

├── tabs/
│   ├── inputs_tab.py
│   └── results_tab.py

├── components/
│   ├── portfolio_frontend.py
│   ├── assumptions_frontend.py
│   ├── scenarios_frontend.py
│   └── correlations_frontend.py

├── services/
│   ├── file_storage.py
│   ├── workflow_config_builder.py
│   ├── workflow_runner.py
│   └── user_config.py
```

Frontend responsibilities are intentionally limited to:

* upload handling
* persistence
* workflow configuration
* workflow execution
* result presentation

Actuarial mechanics remain entirely within the backend.

---

# Example Workflow

```text
Streamlit Frontend
↓
CapitalWorkflowConfig
↓
Workflow Layer
↓
Registry-Driven Assumption Loading
↓
Registry-Driven Scenario Execution
↓
Projection
↓
Valuation
↓
SCR Generation
↓
Aggregation
↓
CapitalWorkflowResult
↓
Results UI
```

---

# Running The Project

Tested using Python 3.11.

Dependencies are listed in `requirements.txt`.

## Clone Repository

```bash
git clone https://github.com/asehdev1994/actuarial-life-model-engine.git
cd actuarial-life-model-engine
```

## Create Virtual Environment

```bash
python -m venv venv
```

Activate:

### Windows

```bash
.\venv\Scripts\activate
```

### Mac / Linux

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Launch Frontend

```bash
streamlit run frontend/app.py
```

The frontend is now the primary execution interface.

---

# Notebook Execution

Most notebooks now act as analysis, experimentation, and diagnostic layers.

The primary maintained workflow notebook is:

```text
scenario_and_scr_workflow_registry.ipynb
```

which demonstrates:

* registry-driven assumption loading
* registry-driven stress execution
* valuation
* SCR generation
* diversification
* BSCR calculation

The frontend should be considered the primary execution path.

---

# Current Scope

Implemented:

* deterministic projection engine
* multi-decrement cashflow modelling
* portfolio valuation
* structured result objects
* mortality table ingestion
* yield curve ingestion
* segmented lapse assumptions
* expense assumption infrastructure
* validation framework
* scenario overlay infrastructure
* calibration-driven scenario loading
* registry-driven assumptions
* registry-driven stresses
* univariate SCR framework
* correlation matrix ingestion
* life SCR aggregation
* market SCR aggregation
* BSCR aggregation
* workflow orchestration layer
* configuration-driven execution architecture
* Streamlit frontend
* persistent frontend configuration

---

# Current Intentional Limitations

The following are intentionally excluded from the current version:

* stochastic economic scenarios
* curve-based interest stresses
* equity risk mechanics
* spread risk mechanics
* property risk mechanics
* worst-of lapse selection
* mass lapse mechanics
* dynamic policyholder behaviour
* IFRS 17 mechanics

The current focus remains architectural stability and modular extensibility before introducing additional modelling complexity.

---

# Future Development

Potential future directions include:

* stochastic scenario infrastructure
* advanced expense segmentation
* inflation-linked expense assumptions
* stochastic expense overlays
* asset-side modelling
* ALM extensions
* richer market risk framework
* reporting infrastructure
* capital attribution analytics
* regression testing infrastructure
* parallelised valuation frameworks
* repository-aware AI development tooling
* local coding assistant integration
* automated architecture documentation

---

# Development Philosophy

The project prioritises:

* clarity over shortcuts
* explicitness over hidden behaviour
* stable interfaces over convenience
* extensibility over hardcoding
* incremental evolution over premature complexity

The long-term objective is to evolve toward reusable actuarial and quantitative risk infrastructure while preserving modelling transparency and architectural discipline.

---

# Disclaimer

This is a personal engineering and actuarial modelling project intended for learning, experimentation, and architecture exploration.

It is not intended for production, regulatory, or financial reporting use.

---

# Author

Ajay Sehdev
