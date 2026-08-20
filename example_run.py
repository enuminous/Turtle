import json
from turtle import TURTLEExperiment

with open("example_inputs.json","r",encoding="utf-8") as f:
    evidence=json.load(f)

exp=TURTLEExperiment(
    effect_scale=0.02,
    support_threshold=0.18,
    conditional_threshold=0.05,
    min_independent_groups=3,
)

print(json.dumps(exp.run(evidence),indent=2))
