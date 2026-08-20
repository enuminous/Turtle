from collections import defaultdict
import numpy as np

def group_adjust(records):
    """
    Closely related animals share an independence group.
    Each group contributes its weighted mean, not an unbounded number of votes.
    """
    groups=defaultdict(list)
    for r in records:
        if not r.get("applicable",True):
            continue
        groups[r.get("independence_group",r["framework"])].append(r)

    out={}
    for name,rs in groups.items():
        weights=np.array([r["weight"] for r in rs],dtype=float)
        vals=np.array([r["normalized_effect"] for r in rs],dtype=float)
        if weights.sum() <= 0:
            value=0.0
        else:
            value=float(np.average(vals,weights=weights))
        out[name]={
            "frameworks":[r["framework"] for r in rs],
            "group_effect":value,
            "group_weight":float(min(1.0, weights.max() if len(weights) else 0.0)),
        }
    return out

def contradiction_metrics(records):
    applicable=[r for r in records if r.get("applicable",True) and r["weight"]>0]
    if not applicable:
        return {
            "support_weight":0.0,
            "contradiction_weight":0.0,
            "neutral_weight":0.0,
            "agreement_rate":None,
        }

    support=sum(r["weight"] for r in applicable if r["normalized_effect"]>0)
    contra=sum(r["weight"] for r in applicable if r["normalized_effect"]<0)
    neutral=sum(r["weight"] for r in applicable if r["normalized_effect"]==0)
    directional=[r for r in applicable if r["normalized_effect"]!=0]
    agreement=max(support,contra)/(support+contra) if (support+contra)>0 else None

    return {
        "support_weight":float(support),
        "contradiction_weight":float(contra),
        "neutral_weight":float(neutral),
        "agreement_rate":float(agreement) if agreement is not None else None,
    }
