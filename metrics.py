import numpy as np

def invariant_score(groups):
    if not groups:
        return 0.0
    effects=np.array([g["group_effect"] for g in groups.values()],dtype=float)
    weights=np.array([g["group_weight"] for g in groups.values()],dtype=float)
    if weights.sum()<=0:
        return 0.0
    mean=float(np.average(effects,weights=weights))
    # Penalize disagreement across independent groups.
    dispersion=float(np.average((effects-mean)**2,weights=weights))**0.5
    return float(mean*(1.0-min(1.0,dispersion)))

def replicated_support_fraction(records):
    supportive=[r for r in records if r.get("applicable",True) and r["normalized_effect"]>0]
    if not supportive:
        return 0.0
    return float(sum(1 for r in supportive if r.get("replicated",False))/len(supportive))

def provenance_adjusted_support(records):
    vals=[]
    weights=[]
    for r in records:
        if not r.get("applicable",True):
            continue
        vals.append(r["normalized_effect"])
        weights.append(r["weight"])
    if not vals or sum(weights)<=0:
        return 0.0
    return float(np.average(np.asarray(vals),weights=np.asarray(weights)))
