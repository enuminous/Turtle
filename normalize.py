import math

def normalize_effect(effect, scale=0.02):
    """
    Maps signed effect to approximately [-1,1].
    scale is the effect magnitude at which tanh begins to saturate.
    """
    if effect is None:
        return 0.0
    return math.tanh(float(effect) / max(float(scale), 1e-9))

def evidence_weight(record):
    if not record.get("applicable", True):
        return 0.0
    confidence=float(record.get("confidence", 0.5))
    provenance=float(record.get("provenance_quality", 0.5))
    replication=1.0 if record.get("replicated", False) else 0.70
    return max(0.0, min(1.0, confidence)) * max(0.0, min(1.0, provenance)) * replication

def normalized_record(record, scale=0.02):
    r=dict(record)
    direction=int(r.get("direction",0))
    effect_norm=normalize_effect(r.get("effect",0.0),scale)
    # If direction is supplied separately, align magnitude to declared direction.
    magnitude=abs(effect_norm)
    signed=magnitude*direction if direction in (-1,0,1) else effect_norm
    r["normalized_effect"]=float(signed)
    r["weight"]=float(evidence_weight(r))
    r["weighted_effect"]=float(signed*r["weight"])
    return r
