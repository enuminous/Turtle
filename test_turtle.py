from turtle import TURTLEExperiment

def test_positive_independent_evidence_can_support():
    evidence=[
        {"framework":"A","applicable":True,"direction":1,"effect":0.03,"confidence":0.9,"replicated":True,"independence_group":"g1","provenance_quality":0.9},
        {"framework":"B","applicable":True,"direction":1,"effect":0.03,"confidence":0.9,"replicated":True,"independence_group":"g2","provenance_quality":0.9},
        {"framework":"C","applicable":True,"direction":1,"effect":0.03,"confidence":0.9,"replicated":True,"independence_group":"g3","provenance_quality":0.9},
    ]
    out=TURTLEExperiment().run(evidence)
    assert out["summary"]["verdict"] in {"COHERENTLY SUPPORTED","CONDITIONALLY SUPPORTED"}

def test_veto_overrides_positive_votes():
    evidence=[
        {"framework":"A","applicable":True,"direction":1,"effect":0.03,"confidence":0.9,"replicated":True,"independence_group":"g1","provenance_quality":0.9},
        {"framework":"B","applicable":True,"direction":1,"effect":0.03,"confidence":0.9,"replicated":True,"independence_group":"g2","provenance_quality":0.9},
        {"framework":"BAT","applicable":True,"direction":-1,"effect":-0.02,"confidence":0.95,"replicated":False,"independence_group":"falsification","provenance_quality":0.95,"veto_on_failure":True},
    ]
    out=TURTLEExperiment(min_independent_groups=2).run(evidence)
    assert out["summary"]["verdict"]=="NOT SUPPORTED"
    assert "BAT" in out["summary"]["vetoes"]

def test_correlated_group_is_not_multiple_groups():
    evidence=[
        {"framework":"A","applicable":True,"direction":1,"effect":0.02,"confidence":0.8,"replicated":False,"independence_group":"same","provenance_quality":0.8},
        {"framework":"B","applicable":True,"direction":1,"effect":0.02,"confidence":0.8,"replicated":False,"independence_group":"same","provenance_quality":0.8},
    ]
    out=TURTLEExperiment(min_independent_groups=3).run(evidence)
    assert out["summary"]["independent_group_count"]==1
    assert out["summary"]["verdict"]=="INSUFFICIENT EVIDENCE"
