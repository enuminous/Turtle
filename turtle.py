from dataclasses import dataclass
from normalize import normalized_record
from consensus import group_adjust, contradiction_metrics
from metrics import invariant_score, replicated_support_fraction, provenance_adjusted_support

@dataclass
class TURTLEExperiment:
    effect_scale: float=0.02
    support_threshold: float=0.18
    conditional_threshold: float=0.05
    min_independent_groups: int=3

    def run(self, evidence):
        records=[normalized_record(r,self.effect_scale) for r in evidence]
        applicable=[r for r in records if r.get("applicable",True)]

        if not applicable:
            return {
                "records":records,
                "groups":{},
                "summary":{
                    "verdict":"INSUFFICIENT EVIDENCE",
                    "invariant_score":0.0,
                }
            }

        groups=group_adjust(records)
        cm=contradiction_metrics(records)
        inv=invariant_score(groups)
        rep=replicated_support_fraction(records)
        prov=provenance_adjusted_support(records)

        positive_groups=sum(1 for g in groups.values() if g["group_effect"]>0)
        negative_groups=sum(1 for g in groups.values() if g["group_effect"]<0)

        # Veto logic: records can declare a hard-failure flag.
        vetoes=[
            r["framework"] for r in applicable
            if r.get("veto_on_failure",False) and r["normalized_effect"]<0
        ]

        if vetoes:
            verdict="NOT SUPPORTED"
        elif len(groups) < self.min_independent_groups:
            verdict="INSUFFICIENT EVIDENCE"
        elif inv >= self.support_threshold and positive_groups >= self.min_independent_groups:
            verdict="COHERENTLY SUPPORTED"
        elif inv >= self.conditional_threshold and positive_groups > negative_groups:
            verdict="CONDITIONALLY SUPPORTED"
        elif inv <= -self.conditional_threshold or negative_groups > positive_groups:
            verdict="NOT SUPPORTED"
        else:
            verdict="MIXED / UNRESOLVED"

        return {
            "records":records,
            "groups":groups,
            "contradiction":cm,
            "summary":{
                "independent_group_count":len(groups),
                "positive_group_count":positive_groups,
                "negative_group_count":negative_groups,
                "invariant_score":inv,
                "replicated_support_fraction":rep,
                "provenance_adjusted_support":prov,
                "vetoes":vetoes,
                "verdict":verdict,
            },
            "interpretation":(
                "TURTLE synthesizes independent evidence groups; it does not convert many correlated "
                "framework outputs into independent confirmation."
            )
        }
