
# Results Framework

## Overview

The engine uses structured result contracts to separate:

- modelling mechanics
- analytics
- orchestration
- downstream processing

Result objects are intentionally designed as:

- explicit
- stable
- serialisable
- analytics-friendly
- reusable

Result objects are pure data containers.

---

# Current Result Flow

```text
Projection
→ ProjectionResult
→ Valuation
→ ValuationResult
→ Portfolio
→ PortfolioResult
```

---

# Projection Results

## ProjectionRow

Represents a single projected period.

Current outputs include:

- projection time
- attained age
- inforce probability
- mortality rate
- lapse rate
- expected premiums
- expected claims
- expected lapses
- expected expenses

Projection rows contain no modelling logic.

---

## ProjectionResult

Container for projected cashflows.

Responsibilities:

- hold projection rows
- support serialisation
- provide stable projection output contracts

ProjectionResult contains no actuarial calculations.

---

# Valuation Results

## ValuationRow

Represents valuation outputs for a single projection period.

Current outputs include:

- discount factor
- expected cashflows
- present value metrics
- expense present values
- cumulative emergence metrics

Valuation rows contain no valuation logic.

---

## ValuationResult

Represents the valuation output of a single policy.

Current outputs include:

- PV premiums
- PV claims
- PV expenses
- net value
- optional valuation breakdown

Current BEL framework:

```text
BEL = PV(claims + expenses - premiums)
```

Current PVFP framework:

```text
PVFP = -BEL
```

---

# Portfolio Results

## PortfolioResult

Represents aggregated portfolio valuation output.

Responsibilities:

- aggregate policy-level results
- support weighted model points
- provide portfolio-level breakdowns

Current outputs include:

- portfolio PV premiums
- portfolio PV claims
- portfolio PV expenses
- portfolio net value
- policy count

Portfolio aggregation intentionally contains no actuarial mechanics.

---

# Analytics Philosophy

Analytics consume structured outputs only.

Current analytics responsibilities include:

- dataframe conversion
- profit signature analysis
- summary metrics
- visualisation support

Analytics must remain external to core modelling mechanics.

---

# Future Direction

The results framework is expected to evolve toward:

```text
ScenarioResult
↓
SCRResult
↓
Capital Aggregation Results
```

while preserving stable contracts.
