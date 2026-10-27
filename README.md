# TURTLE

<!-- ENUMINOUS-UNIFIED-NAV:START -->
## Repository navigation

**eNuminous network:** [All public repositories](https://github.com/enuminous/EFMW/blob/main/REPOSITORY_NAVIGATION.md) · [EFMW](https://github.com/enuminous/EFMW) · [102 equations](https://github.com/enuminous/Monolithic_102_EFMW) · [Frozen Lean](https://github.com/enuminous/Monolithic-102-Zoo-Lean4) · [Zoo](https://github.com/enuminous/Tortoise) · [Papers](https://github.com/enuminous/papers) · [Quantum geometry](https://github.com/enuminous/Base888-Quantum-Geometry)

**This project:** [Repository home](https://github.com/enuminous/Turtle) · [Subject index](https://github.com/enuminous/EFMW/blob/main/REPOSITORY_NAVIGATION.md#zoo-index-and-agents)

<details open>
<summary><strong>On this page</strong></summary>

- [Intended use](#intended-use)
- [Core path](#core-path)
- [Flat-stack repository](#flat-stack-repository)
- [Scientific principle](#scientific-principle)
- [Evidence record](#evidence-record)
- [Core outputs](#core-outputs)
- [Final verdicts](#final-verdicts)
- [Important rule](#important-rule)
- [Suggested independence groups](#suggested-independence-groups)
- [Invariant signal](#invariant-signal)
- [Installation](#installation)
- [Run](#run)
- [Tests](#tests)
- [Freeze discipline](#freeze-discipline)
- [Veto conditions](#veto-conditions)
- [Negative results](#negative-results)
- [Status](#status)


</details>

**Related repositories:** [Tortoise](https://github.com/enuminous/Tortoise) · [Monolithic-Zoo-Lean4](https://github.com/enuminous/Monolithic-Zoo-Lean4) · [Monolithic-102-Zoo-Lean4](https://github.com/enuminous/Monolithic-102-Zoo-Lean4) · [Magpie](https://github.com/enuminous/Magpie) · [Dragon](https://github.com/enuminous/Dragon) · [Wolf](https://github.com/enuminous/Wolf) · [Crocodile](https://github.com/enuminous/Crocodile)

> **Evidence boundary:** A link between projects is navigation, not an assertion of proven equivalence, experimental validation, or shared authorship. See each repository’s own status and review notes.
<!-- ENUMINOUS-UNIFIED-NAV:END -->


**Top-level Unification of Recursive Transformations, Layers and Emergence**

TURTLE is the framework-of-frameworks in the EFMW animal stack.

Its job is not to replace the specialized animals.

Its job is:

> Run surviving specialized frameworks against the same system, normalize their evidence, identify what remains invariant across them, expose disagreements, and determine whether a coherent cross-framework signal survives.

## Intended use

TURTLE consumes outputs from specialized frameworks such as:

- TORTOISE
- OWL
- OCTOPUS
- GECKO
- HIVE
- EAGLE
- CRAB
- SHEPHERD
- PULSE
- CAT
- FOX
- SPIDER
- RAVEN
- DOLPHIN
- ANT
- MOTH
- SHARK
- PENGUIN
- BAT
- HEDGEHOG
- CROCODILE
- DRAGON

It does not assume all animals apply to every system.

## Core path

```text
specialized framework outputs
→ evidence normalization
→ applicability weighting
→ reliability weighting
→ direction alignment
→ agreement / contradiction map
→ invariant signal extraction
→ cross-framework residual
→ TURTLE composite verdict
```

## Flat-stack repository

```text
README.md
LICENSE
CITATION.cff
pyproject.toml
requirements.txt
turtle.py
normalize.py
consensus.py
metrics.py
freeze.py
framework_schema.json
example_inputs.json
example_config.yaml
example_run.py
test_turtle.py
MANIFEST.sha256
```

## Scientific principle

A framework-of-frameworks must not turn many correlated measurements into fake certainty.

TURTLE therefore separates:

- evidence strength
- applicability
- independence
- direction
- replication
- contradiction
- provenance quality

## Evidence record

Each animal contributes a record such as:

```json
{
  "framework": "BAT",
  "applicable": true,
  "direction": -1,
  "effect": -0.00006,
  "confidence": 0.90,
  "replicated": false,
  "independence_group": "baseline-falsification",
  "provenance_quality": 0.95
}
```

Direction convention:

- `+1` supports the candidate claim
- `0` neutral / null
- `-1` undermines the candidate claim

## Core outputs

TURTLE reports:

1. normalized evidence by framework
2. weighted support
3. weighted contradiction
4. agreement rate
5. independence-adjusted support
6. replicated-support fraction
7. provenance-adjusted support
8. cross-framework invariant score
9. residual disagreement
10. final verdict

## Final verdicts

- `COHERENTLY SUPPORTED`
- `CONDITIONALLY SUPPORTED`
- `MIXED / UNRESOLVED`
- `NOT SUPPORTED`
- `INSUFFICIENT EVIDENCE`

## Important rule

TURTLE is not a voting machine.

Ten weak correlated animals do not outweigh one strong falsification test.

Independence groups prevent multiple closely related frameworks from being counted as ten separate experiments.

## Suggested independence groups

Examples:

- early-warning
- distributed-state
- contradiction
- agent-reliability
- causality
- generalization
- falsification
- provenance
- regimes
- noise-ceiling
- temporal-structure
- mechanics
- logistics

These groupings must be frozen before final synthesis.

## Invariant signal

TURTLE defines a provisional invariant as:

> A directional effect that survives normalization, appears across multiple independent applicable framework groups, is not dominated by failed controls, and remains after provenance and replication weighting.

This is operational, not metaphysical.

## Installation

```bash
python -m pip install -r requirements.txt
```

## Run

```bash
python example_run.py
```

## Tests

```bash
pytest -q
```

## Freeze discipline

Before final synthesis, freeze:

- included frameworks
- applicability decisions
- independence groups
- evidence directions
- effect normalization
- weighting rules
- replication rule
- provenance rule
- veto conditions
- verdict thresholds
- exclusions

Then:

```bash
python freeze.py
```

## Veto conditions

A strong falsification failure can prevent an overall positive verdict even when several exploratory frameworks look positive.

Typical veto candidates include:

- BAT baseline failure
- OWL/provenance failure
- HEDGEHOG generalization failure
- CROCODILE placebo failure for causal claims

## Negative results

`NOT SUPPORTED` is a valid TURTLE output.

The purpose of unification is not to produce a positive conclusion. It is to determine what remains after the specialized tests disagree.

## Status

Research software. Experimental.
