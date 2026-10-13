# TURTLE

<!-- ENUMINOUS-NETWORK:START -->
**eNuminous network:** [All repositories](https://enuminous.github.io/EFMW/repositories.html) · [EFMW](https://enuminous.github.io/EFMW/) · [102 equations](https://github.com/enuminous/Monolithic_102_EFMW) · [165 triplets](https://enuminous.github.io/FieldSpace/) · [Zoo](https://enuminous.github.io/Tortoise/) · [Lean](https://enuminous.github.io/Aristotle-102-Monolithic-Lean/) · [Engine](https://enuminous.github.io/Archimedes-Engine/) · [Papers](https://enuminous.github.io/medium/papers-essays-index.html) · [Audit](https://github.com/enuminous/EFMW_Post156_Zoo_Audit/blob/main/portfolio/INTERLOCK_AUDIT.md)

[Repository](https://github.com/enuminous/Turtle) · This repository is linked through its source; GitHub Pages is not enabled.

<details>
<summary>Recent repositories (9)</summary>

- [Oroboros](https://github.com/enuminous/Oroboros) · [README](https://github.com/enuminous/Oroboros/blob/main/README.md) · [Page](https://enuminous.github.io/Oroboros/)
- [P-NP](https://github.com/enuminous/P-NP) · [README](https://github.com/enuminous/P-NP/blob/main/README.md) · [Page](https://enuminous.github.io/P-NP/)
- [Research-Program](https://github.com/enuminous/Research-Program) · [README](https://github.com/enuminous/Research-Program/blob/main/README.md) · [Page](https://enuminous.github.io/Research-Program/)
- [I-Have-Guts](https://github.com/enuminous/I-Have-Guts) · [README](https://github.com/enuminous/I-Have-Guts/blob/main/README.md) · [Page](https://enuminous.github.io/I-Have-Guts/)
- [Wrights-Law](https://github.com/enuminous/Wrights-Law) · [README](https://github.com/enuminous/Wrights-Law/blob/main/README.md) · [Page](https://enuminous.github.io/Wrights-Law/)
- [Aristotle-eNuminous](https://github.com/enuminous/Aristotle-eNuminous) · [README](https://github.com/enuminous/Aristotle-eNuminous/blob/main/README.md) · [Page](https://enuminous.github.io/Aristotle-eNuminous/)
- [Multiverse-Simulator](https://github.com/enuminous/Multiverse-Simulator) · [README](https://github.com/enuminous/Multiverse-Simulator/blob/main/README.md) · [Page](https://enuminous.github.io/Multiverse-Simulator/)
- [accelerando-8192](https://github.com/enuminous/accelerando-8192) · [README](https://github.com/enuminous/accelerando-8192/blob/main/README.md) · [Page source](https://github.com/enuminous/accelerando-8192/blob/main/docs/index.html)
- [Codex-888](https://github.com/enuminous/Codex-888) · [README](https://github.com/enuminous/Codex-888/blob/main/README.md) · [Page](https://enuminous.github.io/Codex-888/)

</details>
<!-- ENUMINOUS-NETWORK:END -->

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
