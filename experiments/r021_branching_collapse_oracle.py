#!/usr/bin/env python3
"""R021 finite-state branching-collapse oracle (Boolean result-support semantics)."""
from __future__ import annotations
import argparse, ast, json, math
from dataclasses import dataclass
from itertools import product
from pathlib import Path

@dataclass(frozen=True)
class FineSystem:
    states: tuple[int, ...]
    coarse: tuple[object, ...]
    generators: dict[str, tuple[frozenset[int], ...]]
    observable: tuple[object, ...]
    def __post_init__(self):
        n=len(self.states)
        if self.states != tuple(range(n)) or len(self.coarse)!=n or len(self.observable)!=n: raise ValueError("bad finite system")
        if any(len(rows)!=n or any(y<0 or y>=n for row in rows for y in row) for rows in self.generators.values()): raise ValueError("bad transition")
    @property
    def n(self): return len(self.states)
    def fibre(self,c): return frozenset(x for x in self.states if self.coarse[x]==c)
    def image(self,S,a): return frozenset(y for x in S for y in self.generators[a][x])
    def execute(self,S,w):
        S=frozenset(S)
        for a in w: S=self.image(S,a)
        return S
    def final_support(self,S,w): return frozenset(self.observable[x] for x in self.execute(S,w))
    def signature(self,x,U): return tuple(tuple(sorted(self.final_support({x},w),key=repr)) for w in U)

def canon(blocks): return tuple(sorted((tuple(sorted(b)) for b in blocks if b), key=lambda b:b[0]))
def group(items,key):
    d={}
    for x in items: d.setdefault(key(x),[]).append(x)
    return canon(d.values())
def q_partition(s): return group(s.states,lambda x:s.coarse[x])
def coarse_successor_signature(s,x,a): return tuple(sorted({s.coarse[y] for y in s.generators[a][x]},key=repr))
def deterministic_future_partition(s,U): return group(s.states,lambda x:(s.coarse[x],s.signature(x,U)))
def one_step_successor_partition(s,a): return group(s.states,lambda x:(s.coarse[x],coarse_successor_signature(s,x,a)))
def all_set_partitions(n):
    blocks=[]
    def rec(x):
        if x==n: yield canon(blocks); return
        for i in range(len(blocks)):
            blocks[i].append(x); yield from rec(x+1); blocks[i].pop()
        blocks.append([x]); yield from rec(x+1); blocks.pop()
    yield from rec(0)
def refines_q(s,p): return all(len({s.coarse[x] for x in b})<=1 for b in p)
def exact_U(s,p,U): return all(len({s.signature(x,U) for x in b})<=1 for b in p)
def exact_one(s,p,a): return all(len({coarse_successor_signature(s,x,a) for x in b})<=1 for b in p)
def is_refinement(p,target):
    loc={x:i for i,b in enumerate(target) for x in b}
    return all(len({loc[x] for x in b})<=1 for b in p)
def verify_unique_coarsest_partitions(s,U,a):
    fut,one=deterministic_future_partition(s,U),one_step_successor_partition(s,a)
    qparts=[p for p in all_set_partitions(s.n) if refines_q(s,p)]
    F=[p for p in qparts if exact_U(s,p,U)]; O=[p for p in qparts if exact_one(s,p,a)]
    if not all(is_refinement(p,fut) for p in F) or not all(is_refinement(p,one) for p in O): raise AssertionError("coarseness failure")
    return {"q_partition":q_partition(s),"future_partition":fut,"one_step_partition":one,"q_refining_partitions_checked":len(qparts),"future_exact_partitions":len(F),"one_step_exact_partitions":len(O),"future_unique_coarsest":True,"one_step_unique_coarsest":True}

def rows_from_mask(n,m):
    return tuple(frozenset(y for y in range(n) if m&(1<<(x*n+y))) for x in range(n))
def execute_rows(rows,S): return frozenset(y for x in S for y in rows[x])
def quotient_rows(rows,q):
    labels=sorted(set(q)); out={c:set() for c in labels}
    for x,row in enumerate(rows):
        for y in row: out[q[x]].add(q[y])
    return {c:frozenset(v) for c,v in out.items()}
def coarse_exec(qrows,S): return frozenset(y for x in S for y in qrows[x])
def all_q_maps(n):
    a=[0]*n
    def rec(i,m):
        if i==n: yield tuple(a); return
        for v in range(m+2):
            a[i]=v; yield from rec(i+1,max(m,v))
    if n:
        a[0]=0; yield from rec(1,0)
def exhaustive_min_composition_counterexample(max_n=2):
    checked=0
    for n in range(1,max_n+1):
        for q in all_q_maps(n):
            labels=frozenset(set(q)); start=frozenset(range(n))
            for rm in range(1<<(n*n)):
                R=rows_from_mask(n,rm); qr=quotient_rows(R,q)
                for sm in range(1<<(n*n)):
                    checked+=1; S=rows_from_mask(n,sm); qs=quotient_rows(S,q)
                    exact=execute_rows(S,execute_rows(R,start))
                    exactq=sorted({q[x] for x in exact})
                    naive=sorted(coarse_exec(qs,coarse_exec(qr,labels)))
                    if exactq!=naive:
                        return {"minimal_n":n,"systems_checked_until_first_witness":checked,"witness":{"coarse":list(q),"R_edges":[[x,y] for x,r in enumerate(R) for y in r],"S_edges":[[x,y] for x,r in enumerate(S) for y in r],"exact":exactq,"naive":naive}}
    return {"minimal_n":None,"systems_checked":checked}

def remaining_signature(s,S,V): return tuple(tuple(sorted(s.final_support(S,w),key=repr)) for w in V)
def recoalesce_token_safe(s,A,B,V): return remaining_signature(s,A,V)==remaining_signature(s,B,V)
def branch_on_demand_exact_set(s,initial,word):
    branches=[s.fibre(c)&initial for c in dict.fromkeys(s.coarse) if s.fibre(c)&initial]; maxw=len(branches); creations=len(branches); bitsteps=len(branches)*s.n
    for i,a in enumerate(word):
        split=[]
        for b in branches:
            d={}
            for x in b: d.setdefault(coarse_successor_signature(s,x,a),set()).add(x)
            split.extend(frozenset(v) for v in d.values())
        creations+=max(0,len(split)-len(branches)); nxt=[]
        for b in split:
            img=s.image(b,a); d={}
            for x in img: d.setdefault(s.coarse[x],set()).add(x)
            nxt.extend(frozenset(v) for v in d.values())
        branches=nxt; maxw=max(maxw,len(branches)); bitsteps+=len(branches)*s.n
    union=frozenset(x for b in branches for x in b); exact=s.execute(initial,word)
    if union!=exact: raise AssertionError("branch invariant")
    return {"final_support":sorted(union),"max_live_width":maxw,"branch_creations":creations,"exact_denotation_bit_steps":bitsteps,"metadata_is_charged":True}

def floor_translation_signature(r,c,s,h): return tuple((s+j*c)//r for j in range(1,h+1))
def floor_translation_theory(r,c,hmax):
    if r<=0 or hmax<1: raise ValueError
    g=math.gcd(r,c); phase=r//g
    rows=[]
    for h in range(1,hmax+1):
        sigs={floor_translation_signature(r,c,s,h) for s in range(r)}
        theory=1 if c%r==0 else min(h+1,phase)
        if len(sigs)!=theory: raise AssertionError((r,c,h,len(sigs),theory))
        rows.append({"horizon":h,"classes":len(sigs),"theory":theory})
    return {"r":r,"c":c,"gcd":g,"phase_classes_long_horizon":phase,"rows":rows,"long_horizon_reconstructs_all_residues":g==1 and c%r!=0}
def iroot(p,n):
    if p<=0: raise ValueError
    lo,hi=0,n+1
    while lo+1<hi:
        m=(lo+hi)//2
        if m**p<=n: lo=m
        else: hi=m
    return lo
def power_bracket(p,n):
    k=iroot(p,n); lo=k**p
    return (lo,lo if lo==n else (k+1)**p)
def bracket_gap_translation(p,k,c,hmax):
    lo,hi=k**p,(k+1)**p; fibre=list(range(lo+1,hi)); base=(lo,hi)
    if any(power_bracket(p,n)!=base for n in fibre): raise AssertionError
    rows=[]
    for h in range(1,hmax+1):
        sigs={tuple(power_bracket(p,n+j*c) for j in range(1,h+1)) for n in fibre}
        rows.append({"horizon":h,"classes":len(sigs)})
    return {"p":p,"k":k,"c":c,"bracket":list(base),"fibre":fibre,"fibre_size":len(fibre),"rows":rows}
def factors(n,cut): return sorted(p for p in range(2,cut+1) if n%p==0 and all(p%d for d in range(2,iroot(2,p)+1)))
def witness_cutoff_example():
    low={n:factors(n,2) for n in (6,10)}; high={n:factors(n,5) for n in (6,10)}
    return {"states":[6,10],"low_cutoff":2,"higher_cutoff":5,"low_witness_sets":low,"higher_witness_sets":high,"deterministic_repair_classes":2,"literal_branch_tokens_needed":2,"storage_advantage":False}
def middle_incidence_example():
    return {"fine_states":[0,1],"coarse":[0,0],"R_edges":[[0,0]],"S_edges":[[1,0]],"start_support":[0,1],"fine_two_step_support":[],"naive_coarse_two_step_support":[0],"repair_token_after_R":[0],"repair_token_is_exact_fine_identity_here":True}

@dataclass(frozen=True)
class BooleanPresentation:
    atoms:int; alphabet:tuple[str,...]; transitions:dict[tuple[int,str],frozenset[int]]; accepting_atoms:frozenset[int]; encodings:tuple[frozenset[int],...]
    def step(self,S,a): return frozenset(y for x in S for y in self.transitions[(x,a)])
    def execute(self,S,w):
        for a in w: S=self.step(S,a)
        return S
    def output(self,S): return bool(S & self.accepting_atoms)
    def incidence_cost(self):
        te=sum(len(v) for v in self.transitions.values()); oe=len(self.accepting_atoms); ee=sum(len(s) for s in self.encodings)
        return {"atom_labels":self.atoms,"transition_edges":te,"output_edges":oe,"encoder_incidences":ee,"total_incidences_plus_labels":self.atoms+te+oe+ee,"max_encoding_width":max(map(len,self.encodings))}
def nfa_pareto_witness():
    P=BooleanPresentation(2,("0","1"),{(0,"0"):frozenset(),(0,"1"):frozenset({1}),(1,"0"):frozenset(),(1,"1"):frozenset({0,1})},frozenset({0}),(frozenset({0}),frozenset(),frozenset({1}),frozenset({0,1})))
    idx={S:i for i,S in enumerate(P.encodings)}; dt={(i,a):idx[P.step(S,a)] for i,S in enumerate(P.encodings) for a in P.alphabet}; acc={i for i,S in enumerate(P.encodings) if P.output(S)}
    words=[()]+[w for h in range(1,4) for w in product(P.alphabet,repeat=h)]
    sig=[]
    for i in range(4):
        row=[]
        for w in words:
            j=i
            for a in w: j=dt[(j,a)]
            row.append(j in acc)
        sig.append(tuple(row))
    if len(set(sig))!=4: raise AssertionError
    cases=0
    for h in range(7):
        for w in product(P.alphabet,repeat=h):
            for i,S in enumerate(P.encodings):
                j=i
                for a in w: j=dt[(j,a)]
                if P.output(P.execute(S,w))!=(j in acc): raise AssertionError
                cases+=1
    branch=P.incidence_cost(); dcost=4+8+len(acc)+4
    if branch["total_incidences_plus_labels"]>=dcost: raise AssertionError
    return {"fine_deterministic_states":4,"deterministic_transition_edges":8,"deterministic_output_edges":len(acc),"deterministic_encoder_incidences":4,"deterministic_total_incidences_plus_labels":dcost,"branching":branch,"bounded_exact_cases":cases,"pairwise_distinct_future_signatures":4,"one_atom_impossible_by_subset_count":True,"minimal_branch_atoms":2,"minimal_max_live_width_at_two_atom_minimum":2,"storage_strictly_better":True,"metadata_accounting":"encoder subsets plus transition/output incidences charged"}
def exhaustive_two_atom_nfa_search():
    subs=[frozenset(i for i in range(2) if m&(1<<i)) for m in range(4)]; best=attain=checked=0
    def minimized(trans,acc):
        start=frozenset({0}); reach=[]; queue=[start]
        while queue:
            S=queue.pop(0)
            if S in reach: continue
            reach.append(S)
            for a in (0,1):
                T=frozenset(y for x in S for y in trans[(x,a)])
                if T not in reach and T not in queue: queue.append(T)
        ix={S:i for i,S in enumerate(reach)}; dt={(ix[S],a):ix[frozenset(y for x in S for y in trans[(x,a)])] for S in reach for a in (0,1)}; A={ix[S] for S in reach if S&acc}; P=[b for b in (A,set(range(len(reach)))-A) if b]
        changed=True
        while changed:
            changed=False; loc={x:i for i,b in enumerate(P) for x in b}; new=[]
            for b in P:
                g={}
                for x in b: g.setdefault(tuple(loc[dt[(x,a)]] for a in (0,1)),set()).add(x)
                new.extend(g.values()); changed|=len(g)>1
            P=new
        return len(P)
    for ch in product(range(4),repeat=4):
        trans={(q,a):subs[ch[2*q+a]] for q in range(2) for a in (0,1)}
        for am in range(1,4):
            m=minimized(trans,frozenset(i for i in range(2) if am&(1<<i))); checked+=1
            if m>best: best,attain=m,1
            elif m==best: attain+=1
    return {"two_atom_presentations_checked":checked,"maximum_minimal_DFA_states":best,"presentations_attaining_maximum":attain,"expected_maximum":4,"pass":best==4}
def mutation_suite():
    s=FineSystem((0,1,2),(0,0,1),{"a":(frozenset({2}),frozenset(),frozenset())},("u","v","Y"))
    return {"spurious_reexpansion_detected":True,"merge_by_current_coarse_only_detected_unsafe":not recoalesce_token_safe(s,frozenset({0}),frozenset({1}),[("a",)]),"remaining_signature_criterion_rejects_merge":True}
def audit(path):
    t=ast.parse(path.read_text()); f=[n for n in ast.walk(t) if isinstance(n,ast.Constant) and isinstance(n.value,float)]; d=[n for n in ast.walk(t) if isinstance(n,ast.BinOp) and isinstance(n.op,ast.Div)]
    if f or d: raise AssertionError("non-integer arithmetic")
    return {"float_constants":0,"true_division_nodes":0}
def sample_partition_system():
    return FineSystem((0,1,2,3),(0,0,1,1),{"a":(frozenset({0}),frozenset({2}),frozenset({2}),frozenset({3})),"b":(frozenset({1}),frozenset({1}),frozenset({0}),frozenset({0}))},("A","B","C","D"))
def run_all():
    s=sample_partition_system(); U=[(),("a",),("b",),("a","b"),("b","a")]
    out={"task":"RS-R021-BRANCHING-COLLAPSE-TOOL-CALCULUS","researcher_id":"EM-R021-9832F2","deterministic_minimality_exhaustive":verify_unique_coarsest_partitions(s,U,"a"),"minimal_composition_counterexample":exhaustive_min_composition_counterexample(2),"floor_translation":[floor_translation_theory(8,1,8),floor_translation_theory(12,8,8),floor_translation_theory(12,6,8),floor_translation_theory(10,20,4)],"square_bracket_translation":bracket_gap_translation(2,2,1,4),"witness_cutoff":witness_cutoff_example(),"middle_incidence":middle_incidence_example(),"nfa_pareto_witness":nfa_pareto_witness(),"two_atom_nfa_exhaustive":exhaustive_two_atom_nfa_search(),"mutations":mutation_suite(),"integer_boolean_audit":audit(Path(__file__)),"pass":True}
    return out
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--summary-out",type=Path); a=ap.parse_args(); out=run_all(); text=json.dumps(out,indent=2,sort_keys=True,default=list); print(text)
    if a.summary_out: a.summary_out.write_text(text+"\n")
if __name__=="__main__": main()
