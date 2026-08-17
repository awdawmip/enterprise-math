#!/usr/bin/env python3
from __future__ import annotations
import hashlib, itertools, json, sys
from collections import defaultdict
from pathlib import Path

ACTIONS=("X","Y")
SINK=("SINK",)
PRIMARY_DEGREES=((1,0),(1,1))
B_VALUES=(1,2,3)
HORIZON=3
ROOT=(0,0)
EXPECTED_TABLE_HASHES={
 ((1,0),1):"af21a09428bca0b8234ea61ac2440a74e1bd4a19e53c6719e8c92520bc9d91a4",
 ((1,0),2):"1fb80551114a13e42ff292c55d962bdedd8107fa4d347332d3e3a74a900bf0e6",
 ((1,0),3):"1c0a01acbbed4f88be157846695867aa0fda1aa466ac65866e9bb818c1d95f81",
 ((1,1),1):"b81a0837069318937943bf29ed6713ff9c3f5158b1b970e97146d2d6ed575473",
 ((1,1),2):"be1f8e114e56443a41496e583b0149655869f8ae8fdad776e80c7c48aed2b891",
 ((1,1),3):"d9fc58d7b2d02b438f5af304721830852c9d473a84fd40fbf96fa91b4526a243",
}
EXPECTED_LAYER_COUNTS={
 ((1,0),1):(6,8,8,8), ((1,0),2):(12,11,11,11), ((1,0),3):(20,14,14,14),
 ((1,1),1):(9,13,13,13), ((1,1),2):(16,17,17,17), ((1,1),3):(25,21,21,21),
}
EXPECTED_FINE_SUFFIX={
 ((1,0),1):96, ((1,0),2):162, ((1,0),3):244,
 ((1,1),1):150, ((1,1),2):230, ((1,1),3):326,
}

class Audit:
    def __init__(self):
        self.passed=0; self.failed=0; self.failures=[]; self.categories=defaultdict(lambda:{"passed":0,"failed":0})
    def check(self, category, label, cond, detail=None):
        if bool(cond):
            self.passed += 1; self.categories[category]["passed"] += 1
        else:
            self.failed += 1; self.categories[category]["failed"] += 1
            self.failures.append({"category":category,"label":label,"detail":detail})
    def eq(self, category, label, got, expected):
        self.check(category,label,got==expected,{"got":got,"expected":expected} if got!=expected else None)

def load(root,name):
    return json.loads((root/"research_results"/name).read_text(encoding="utf-8"))

def exp_window(d,B): return tuple(range(-B,d+B+1))
def local_exponent(d,k,bit): return k if bit==0 else d-k
def chart_regular(a,b,r,s,chart):
    i,j=chart
    return local_exponent(a,r,i)>=0 and local_exponent(b,s,j)>=0
def reg_support(a,b,r,s):
    return tuple((i,j) for i in (0,1) for j in (0,1) if chart_regular(a,b,r,s,(i,j)))
def action_target_chart(chart,action):
    i,j=chart
    return (1-i,j) if action=="X" else (i,1-j)
def source_step(a,b,st,action):
    if st==SINK: return SINK
    r,s,i,j=st
    tc=action_target_chart((i,j),action)
    return (r,s,tc[0],tc[1]) if chart_regular(a,b,r,s,tc) else SINK
def source_initial_states(a,b,B,root=ROOT):
    return {(r,s,root[0],root[1]) for r in exp_window(a,B) for s in exp_window(b,B) if chart_regular(a,b,r,s,root)}
def generate_layers(a,b,B,root=ROOT,horizon=HORIZON):
    layers=[source_initial_states(a,b,B,root)]
    for _ in range(horizon):
        nxt=set()
        for st in layers[-1]:
            for act in ACTIONS: nxt.add(source_step(a,b,st,act))
        layers.append(nxt)
    return layers
def words(n): return tuple(tuple(w) for w in itertools.product(ACTIONS,repeat=n))
def execute(a,b,st,w):
    cur=st
    for act in w: cur=source_step(a,b,st,act)
    return cur
def obs(st): return "REJECT" if st==SINK else "ACCEPT"
def signature(a,b,st,remaining): return tuple(obs(execute(a,b,st,w)) for w in words(remaining))
def reg_key(a,b,st):
    if st==SINK:return ("SINK",)
    r,s,_,_=st
    return ("REGSUPP",)+reg_support(a,b,r,s)
def partition(states,keyfn):
    d=defaultdict(list)
    for st in sorted(states,key=repr): d[keyfn(st)].append(st)
    return d
def partset(d): return {frozenset(v) for v in d.values()}
def canonical_state(st):
    if st==SINK:return "⊥"
    r,s,e,j=st; return f"m({r},{s})@U{i}{j}"
def full_generated_table(a,b,B,root=ROOT):
    layers=generate_layers(a,b,B,root)
    table={"params":{"a":a,"b":b,"B":B,"root":list(root)},"ambient_windows":{"r":list(exp_window(a,B)),"s":list(exp_window(b,B))},"layers":[],"transitions":[]}
    for idx,sts in enumerate(layers):
        table["layers"].append({"stage":idx,"states":[canonical_state(s)) for s in sorted(sts,key=repr)]})
        if idx<HORIZON:
            for st in sorted(sts,key=repr):
                for act in ACTIONS:
                    table["transitions"].append({"stage":idx,"state":canonical_state(st),"action":act,"target":canonical_state(source_step(a,b,st,act))})
    return table
def hash_json(o): return hashlib.sha256(json.dumps(o,ensure_ascii=False,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def swap_x(a,b,st):
    if st==SINK:return SINK
    r,s,i,j=st; return (a-r,s,1-i,j)
def swap_y(a,b,st):
    if st==SINK:return SINK
    r,s,i,j=st; return (r,b-s,i,1-j)
def swap_both(a,b,st): return swap_y(a,b,swap_x(a,b,st))
def factor_swap(st):
    if st==SINK:return SINK
    r,s,i,j=st; return (s,r,j,i)
def swap_action(act): return "Y" if act=="X" else "X"
def swap_word(w): return tuple(swap_action(a) for a in w)

def param_record(records, degree, B):
    for x in records:
        if tuple(x["degree"])==tuple(degree) and x["B"]==B:return x
    raise KeyError((degree,B))

def main():
    base=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(__file__).resolve().parents[1]
    A=Audit()
    source=load(base,"HODGE_H0E_ALGEBRAIC_SOURCE_SPEC.json")
    replay=load(base,"HODGE_H0E_ALGEBRAIC_GENERATION_REPLAY.json")
    params=load(base,"HODGE_H0E_PARAMETER_REGISTRY.json")
    multi=load(base,"HODGE_H0E_MULTISTEP_SOURCE_REGISTRY.json")
    baseline=load(base,"HODGE_H0E_ALGEBRAIC_BASELINE_SANDWICH.json")
    quotient=load(base,"HODGE_H0E_SUFFIX_OR_BEHAVIOR_QUOTIENT_REGISTRY.json")
    comparison=load(base,"HODGE_H0E_COMPARISON_THEOREM_REGISTRY.json")
    proof=load(base,"HODGE_H0E_PROOF_LEVERAGE_CERTIFICATE_REGISTRY.json")
    attrib=load(base,"HODGE_H0E_ATTRIBUTION_CERTIFICATE_REGISTRY.json")
    gaming=load(base,"HODGE_H0E_BASELINE_GAMING_CONTROL.json")
    nat=load(base,"HODGE_H0E_PRESENTATION_NATURALITY_LEDGER.json")
    fun=load(base,"HODGE_H0E_FUNCTORIALITY_LEDGER.json")
    novelty=load(base,"HODGE_H0E_PRIOR_ART_NOVELTY_LEDGER.json")
    leak=load(base,"HODGE_H0E_TARGET_LEAKAGE_LEDGER.json")
    rational=load(base,"HODGE_H0E_RATIONAL_BOUNDARY.json")
    r3=load(base,"HODGE_H0E_HODGE_R3_PREINTERFACE.json")
    cls=load(base,"HODGE_H0E_CLASSIFICATION.json")

    # Static protocol / parameter freeze gates
    A.eq("protocol","researcher-id",cls["researcher_id"],"EM-HODGE-H0E-73A6C4")
    A.eq("protocol","taskbook-source",cls["taskbook_source"],"89f058d618ad2d4834ed20b7917d17b4966267f2")
    A.eq("protocol","parent-H0D",cls["parent_h0d_head"],"102f6c73a099a97a412e72c810f8e63d2c370234")
    A.eq("protocol","degrees",params["degrees"],[[1,0],[1,1]])
    A.eq("protocol","B-values",params["B_values"],[1,2,3])
    A.eq("protocol","depth",params["depth"],3)
    A.eq("protocol","actions",params["actions"],["X","Y"])
    A.check("protocol","no-post-selection",params["post_selection"] is False)
    A.check("protocol","all-six-retained",params["all_six_primary_instances_retained"] is True)
    A.eq("protocol","baseline-frozen-status",baseline["status"],"FROZEN_BEFORE_SUCCESS_COUNTS")
    A.check("protocol","RegSupp-predeclared","RegSupp" in params["fair_standard_source_normal_form_predeclared"])
    A.eq("protocol","H0D-table-not-generator",multi["uses_h0d_table_as_generator"],False)
    A.eq("protocol","actual-algebraic-generation-flag",multi["actual_algebraic_generation_pass"],True)

    total_trans=0; total_suffix=0; total_raw=0
    qrecords=quotient["parameter_results"]
    mrecs=multi["parameter_instances"]
    rrecs=replay["parameters"]
    for degree in PRIMARY_DEGRES: 
        a,b=degree
        for B in B_VALUES:
            tag=f"Ob;a=a;b={b};B={B}"
            layers=generate_layers(a,b,B)
            rec=param_record(qrecords,degree,B)
            mrec=param_record(mrecs,degree,B)
            rrec=param_record(rrecs,degree,B)
            A.eq("generation",tag+":layer-counts",[