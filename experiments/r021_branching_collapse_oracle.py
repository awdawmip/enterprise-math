"""R021 exact finite-state reference oracle.

Scope: Boolean/result-support semantics. Hidden branch/correlation metadata is charged.
No floating point. Bounded exhaustive searches are intentionally small.
"""
from dataclasses import dataclass
from itertools import combinations, product
from math import ceil, gcd, log2

@dataclass(frozen=True)
class FiniteSystem:
    states: tuple
    coarse: dict
    observable: dict
    generators: dict  # name -> state -> frozenset targets
    def fibre(self, a): return frozenset(x for x in self.states if self.coarse[x] == a)
    @property
    def labels(self): return tuple(dict.fromkeys(self.coarse[x] for x in self.states))
    @property
    def alphabet(self): return tuple(self.generators)

def deterministic_system(states, coarse, observable, generators):
    return FiniteSystem(tuple(states), dict(coarse), dict(observable),
                        {g:{x:frozenset({y}) for x,y in f.items()} for g,f in generators.items()})

def apply_generator(s, A, g):
    return frozenset(y for x in A for y in s.generators[g][x])

def execute_fine(s, A, word):
    A=frozenset(A)
    for g in word: A=apply_generator(s,A,g)
    return A

def observable_support(s,A): return frozenset(s.observable[x] for x in A)
def coarse_support(s,A): return frozenset(s.coarse[x] for x in A)
def result_support(s,A,w): return observable_support(s,execute_fine(s,A,w))

def words_upto(alphabet,h,include_empty=True):
    out=[()] if include_empty else []
    for n in range(1,h+1): out += list(product(tuple(alphabet),repeat=n))
    return tuple(out)

def future_signature(s,x,U):
    return tuple(tuple(sorted(result_support(s,{x},w),key=repr)) for w in U)

def support_signature(s,A,U):
    return tuple(tuple(sorted(result_support(s,A,w),key=repr)) for w in U)

def successor_support_signature(s,x,g):
    return tuple(sorted(coarse_support(s,s.generators[g][x]),key=repr))

def _partition_by_key(states,key):
    d={}
    for x in states: d.setdefault(key(x),set()).add(x)
    return tuple(sorted((frozenset(v) for v in d.values()),key=lambda b:tuple(sorted(map(repr,b)))))

def _partitions(items):
    items=tuple(items); blocks=[]
    if not items: yield (); return
    blocks.append([items[0]])
    def rec(i):
        if i==len(items):
            yield tuple(sorted((frozenset(b) for b in blocks),key=lambda b:tuple(sorted(map(repr,b)))))
            return
        x=items[i]
        for j in range(len(blocks)):
            blocks[j].append(x); yield from rec(i+1); blocks[j].pop()
        blocks.append([x]); yield from rec(i+1); blocks.pop()
    yield from rec(1)

def _refines(P,Q): return all(any(p<=q for q in Q) for p in P)

def exhaustive_coarsest_refinement(s,key):
    base=_partition_by_key(s.states,lambda x:s.coarse[x])
    sig=_partition_by_key(s.states,lambda x:(s.coarse[x],key(x)))
    valid=0; bad=[]
    for P in _partitions(s.states):
        if not _refines(P,base): continue
        if any(len({key(x) for x in b})>1 for b in P): continue
        valid+=1
        if not _refines(P,sig): bad.append(P)
    return {"signature_partition":sig,"valid_refinements":valid,
            "coarseness_violations":bad,"verified":not bad}

def naive_qrel(s,g):
    return {a:coarse_support(s,apply_generator(s,s.fibre(a),g)) for a in s.labels}

def execute_naive_quotient(s,labels,word):
    cur=frozenset(labels)
    for g in word:
        qr=naive_qrel(s,g); cur=frozenset(b for a in cur for b in qr[a])
    return cur

def _systems(n):
    X=tuple(range(n))
    for k in range(1,n+1):
        for qv in product(range(k),repeat=n):
            if set(qv)!=set(range(k)): continue
            q=dict(zip(X,qv))
            for fv in product(X,repeat=n):
                yield k,q,dict(zip(X,fv))

def find_min_naive_composition_counterexample(max_states=4):
    for n in range(1,max_states+1):
        X=tuple(range(n))
        for k,q,f in _systems(n):
            s=deterministic_system(X,q,q,{"f":f})
            for a in range(k):
                exact=coarse_support(s,execute_fine(s,s.fibre(a),("f","f")))
                naive=execute_naive_quotient(s,{a},("f","f"))
                if exact!=naive:
                    return {"n":n,"k":k,"coarse":q,"function":f,"start_label":a,
                            "one_step":naive_qrel(s,"f")[a],"exact_two_step":exact,"naive_two_step":naive}
    return None

def exhaustive_naive_composition_stats(max_states=3):
    by=[]; total=fail=0; first=None
    for n in range(1,max_states+1):
        X=tuple(range(n)); qseen=set(); systems=trials=bad=0
        for k,q,f in _systems(n):
            qseen.add((k,tuple(q.values()))); systems+=1
            s=deterministic_system(X,q,q,{"f":f})
            for a in range(k):
                trials+=1
                ex=coarse_support(s,execute_fine(s,s.fibre(a),("f","f")))
                nv=execute_naive_quotient(s,{a},("f","f"))
                if ex!=nv:
                    bad+=1
                    if first is None: first={"n":n,"k":k,"coarse":q,"function":f,"start_label":a,
                                           "exact_two_step":ex,"naive_two_step":nv}
        total+=trials; fail+=bad
        by.append({"n":n,"surjective_coarse_maps":len(qseen),"q_f_systems":systems,
                   "start_fibre_trials":trials,"composition_failures":bad})
    return {"max_states":max_states,"by_n":by,"total_trials":total,"total_failures":fail,
            "first_failure":first,"minimal_failure_states":None if first is None else first["n"]}

def _group_by_coarse(s,A):
    d={}
    for x in A: d.setdefault(s.coarse[x],set()).add(x)
    return [frozenset(v) for v in d.values()]

def _split_successor(s,A,g):
    d={}
    for x in A: d.setdefault(successor_support_signature(s,x,g),set()).add(x)
    return [frozenset(v) for v in d.values()]

def _token_bits(s,A):
    if not A:return 0
    labs={s.coarse[x] for x in A}
    if len(labs)!=1:return len(s.states)
    a=next(iter(labs)); F=s.fibre(a); lb=max(1,ceil(log2(max(2,len(s.labels)))))
    return lb if A==F else lb+len(F)  # charge strict-subset correlation bitmask

def branch_on_demand_exact(s,initial_support,word):
    branches=_group_by_coarse(s,frozenset(initial_support)); mw=len(branches); created=work=0
    peak=sum(_token_bits(s,b) for b in branches); trace=[]
    for i,g in enumerate(word,1):
        split=[]
        for b in branches:
            ps=_split_successor(s,b,g); created+=max(0,len(ps)-1); split+=ps; work+=len(b)
        mw=max(mw,len(split))
        target=frozenset(y for b in split for y in apply_generator(s,b,g))
        branches=_group_by_coarse(s,target); mw=max(mw,len(branches))
        bits=sum(_token_bits(s,b) for b in branches); peak=max(peak,bits)
        trace.append({"step":i,"generator":g,"split_width":len(split),"post_width":len(branches),
                      "support":tuple(sorted(target,key=repr)),"token_bits":bits})
    A=frozenset(x for b in branches for x in b)
    return {"final_fine_support":A,"final_observable_support":observable_support(s,A),
            "max_live_width":mw,"cumulative_branch_creations":created,"work_state_visits":work,
            "peak_token_bits":peak,"trace":trace}

def naive_reexpand_execution(s,initial_support,word):
    A=frozenset(initial_support); trace=[]
    for i,g in enumerate(word,1):
        img=apply_generator(s,A,g); labs=coarse_support(s,img)
        A=frozenset(x for a in labs for x in s.fibre(a))
        trace.append({"step":i,"labels":tuple(labs),"exact_image":tuple(img),"reexpanded":tuple(A)})
    return {"final_fine_support":A,"final_observable_support":observable_support(s,A),"trace":trace}

def safe_forgetful_merge(s,exact_union,hull,remaining_language):
    if not exact_union<=hull: raise ValueError("hull must contain exact union")
    return support_signature(s,exact_union,remaining_language)==support_signature(s,hull,remaining_language)

def merge_inequivalent_states_mutation(s,a,b,U):
    for w in U:
        l=result_support(s,{a},w); r=result_support(s,{b},w)
        if l!=r:return {"states":(a,b),"separating_word":w,"left_support":l,"right_support":r,"mutation_detected":True}
    return {"states":(a,b),"separating_word":None,"left_support":None,"right_support":None,"mutation_detected":False}

def _min_cover(S,atoms):
    usable=[a for a in atoms if a and a<=S]
    if not S:return 0
    for r in range(1,len(usable)+1):
        if any(frozenset().union(*c)==S for c in combinations(usable,r)):return r
    return None

def bounded_branch_dictionary_frontier(n,required_supports):
    if n>4:raise ValueError("bounded search only n<=4")
    U=range(n); atoms=[frozenset(i for i in U if m&(1<<i)) for m in range(1,1<<n)]; feas=[]
    for mask in range(1,1<<len(atoms)):
        D=[atoms[i] for i in range(len(atoms)) if mask&(1<<i)]; ws=[_min_cover(S,D) for S in required_supports]
        if any(w is None for w in ws):continue
        feas.append({"K":len(D),"W":max(ws,default=0),"dictionary_bits":len(D)*n,"atoms":tuple(D)})
    front=[]
    for x in feas:
        if not any(y["K"]<=x["K"] and y["W"]<=x["W"] and (y["K"]<x["K"] or y["W"]<x["W"]) for y in feas):front.append(x)
    d={}
    for x in sorted(front,key=lambda z:(z["K"],z["W"])):d.setdefault((x["K"],x["W"]),x)
    return list(d.values())

def floor_translation_signature_classes(r,c,h):
    d={}
    for s in range(r): d.setdefault(tuple((s+t*c)//r for t in range(h+1)),[]).append(s)
    g=gcd(r,c); ev=r//g
    return {"r":r,"c":c,"gcd":g,"horizon":h,"classes":tuple(tuple(v) for v in d.values()),
            "class_count":len(d),"predicted_count":1+min(h,ev-1),"eventual_classes":ev,
            "full_residue_required_eventually":g==1}

def floor_translation_fibre_support_stats(r,c,h):
    widths=[]; phases=[]
    for t in range(h+1):
        lo=t*c; hi=r-1+t*c; widths.append(hi//r-lo//r+1); phases.append(lo%r)
    cyc=r//gcd(r,c)
    return {"max_coarse_branch_width":max(widths),"widths":tuple(widths),"phases":tuple(phases),
            "phase_cycle":cyc,"phase_token_bits":max(1,ceil(log2(max(2,cyc)))),
            "support_shape":"single integer interval of length r"}

def floor_p_root(n,p):
    lo=0; hi=1
    while hi**p<=n:hi*=2
    while lo+1<hi:
        m=(lo+hi)//2
        if m**p<=n:lo=m
        else:hi=m
    return lo

def pth_bracket(n,p):
    k=floor_p_root(n,p); a=k**p
    return (a,a) if a==n else (a,(k+1)**p)

def pth_cell_translation_stats(k,p,c,h):
    lo=k**p+1; hi=(k+1)**p-1
    widths=[len({pth_bracket(n,p) for n in range(lo+t*c,hi+t*c+1)}) for t in range(h+1)]
    groups={}
    for n in range(lo,hi+1):groups.setdefault(tuple(pth_bracket(n+t*c,p) for t in range(h+1)),[]).append(n)
    return {"cell":(lo,hi),"cell_size":hi-lo+1,"max_bracket_support_width":max(widths),"widths":tuple(widths),
            "pointwise_signature_classes":len(groups),"pointwise_classes":tuple(tuple(v) for v in groups.values()),
            "support_token":"translated interval [lo+t*c, hi+t*c] (two endpoints)","positive_translation_width_bound":3}

def _witnesses(n,c):return frozenset(d for d in range(2,c+1) if n%d==0)
def witness_cutoff_groups(numbers,low,high):
    lg={}
    for n in numbers:lg.setdefault(tuple(sorted(_witnesses(n,low))),[]).append(n)
    out=[]
    for sig,ns in lg.items():
        hg={}
        for n in ns:hg.setdefault(tuple(sorted(_witnesses(n,high))),[]).append(n)
        out.append({"low_signature":sig,"members":tuple(ns),"high_signature_count":len(hg),"high_groups":{k:tuple(v) for k,v in hg.items()}})
    return {"low":low,"high":high,"groups":out}

def middle_incidence_counterexample():
    R={("a","b1")}; S={("b2","c")}; comp={(a,c) for a,b in R for b2,c in S if b==b2}
    return {"R":R,"S":S,"exact_composition":comp,"coarse_marginal_predicts_path":bool(R) and bool(S),
            "required_correlation":"middle witness identity/intersection","minimum_identity_bits_for_two_middle_states":1}

def powerset_membership_pareto(n):
    # Closed form; bounded implementation check uses future-signature construction below for n<=8.
    X=tuple(range(1<<n)); q={m:0 for m in X}; o={m:int(m!=0) for m in X}
    gs={f"test_{i}":{m:m&(1<<i) for m in X} for i in range(n)}; s=deterministic_system(X,q,o,gs)
    U=tuple((f"test_{i}",) for i in range(n)); P=_partition_by_key(X,lambda x:future_signature(s,x,U)); assert len(P)==1<<n
    return {"n":n,"deterministic_future_states":1<<n,"deterministic_transition_entries":n*(1<<n),"branch_atoms":n,
            "branch_transition_cells":n*n,"branch_nonzero_edges":n,"max_live_width":n,"runtime_branch_config_bits":n,
            "deterministic_live_label_bits":n,"critical_path_per_symbol":1,"branch_work_per_symbol_worst":n,"deterministic_work_per_symbol":1}

def three_state_counterexample_system():
    X=("a","b","c"); q={"a":"A","b":"B","c":"B"}; f={"a":"b","b":"b","c":"a"}
    return deterministic_system(X,q,q,{"f":f})

def _jsonable(x):
    if isinstance(x,dict):return {repr(k) if not isinstance(k,(str,int,float,bool,type(None))) else k:_jsonable(v) for k,v in x.items()}
    if isinstance(x,(set,frozenset,tuple,list)):return [_jsonable(v) for v in (sorted(x,key=repr) if isinstance(x,(set,frozenset)) else x)]
    return x

def run_demo_suite():
    s=three_state_counterexample_system(); U=words_upto(("f",),2)
    req=[frozenset({0}),frozenset({1}),frozenset({2}),frozenset({0,1}),frozenset({0,2}),frozenset({1,2})]
    F=bounded_branch_dictionary_frontier(3,req)
    return {"minimal_counterexample":find_min_naive_composition_counterexample(3),"exhaustive_composition_stats_n3":exhaustive_naive_composition_stats(3),
            "one_step_coarsest":exhaustive_coarsest_refinement(s,lambda x:successor_support_signature(s,x,"f")),
            "future_signature_coarsest":exhaustive_coarsest_refinement(s,lambda x:future_signature(s,x,U)),
            "branch_exact":branch_on_demand_exact(s,s.fibre("A"),("f","f")),"mutation_reexpand":naive_reexpand_execution(s,s.fibre("A"),("f","f")),
            "mutation_merge":merge_inequivalent_states_mutation(s,"b","c",U),
            "dictionary_frontier":[{**{k:v for k,v in x.items() if k!="atoms"},"atoms":[tuple(sorted(a)) for a in x["atoms"]]} for x in F],
            "floor_r10_c1":[floor_translation_signature_classes(10,1,h) for h in (1,2,5,9,10)],"floor_support_r10_c1":floor_translation_fibre_support_stats(10,1,20),
            "floor_r12_c8":[floor_translation_signature_classes(12,8,h) for h in (1,2,3,5)],"pth_cube":pth_cell_translation_stats(3,3,5,8),
            "witness":witness_cutoff_groups([6,10,14,22,26],2,13),"incidence":middle_incidence_counterexample(),"powerset_n8":powerset_membership_pareto(8)}

if __name__=="__main__":
    import json
    print(json.dumps(_jsonable(run_demo_suite()),indent=2,sort_keys=True))
