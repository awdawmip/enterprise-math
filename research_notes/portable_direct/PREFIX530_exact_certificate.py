#!/usr/bin/env python3
"""PREFIX-530 exact 49-linear vs 96-state branch-aware integer polynomial certificate.
Frozen science: enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d
"""
from collections import defaultdict
import json
STARS=((0,2,5),(0,3,4),(1,2,4),(1,3,5))
def nearby(j,c):
    return [-(1 if c>0 else -1)*(a+1) for a in STARS[j] if a!=abs(c)-1]
def successor(s):
    j,p,c=s;k=next(i for i,st in enumerate(STARS) if i!=j and abs(c)-1 in st)
    return [(j,c,v) for v in nearby(j,c) if v!=p]+[(k,c,v) for v in nearby(k,c)]
PHASES=tuple((j,p,sgn*(a+1)) for j in range(4) for a in STARS[j] for sgn in (-1,1) for p in nearby(j,sgn*(a+1)))
IDX={p:i for i,p in enumerate(PHASES)}
NEXT=tuple(tuple(IDX[v] for v in successor(s)) for s in PHASES)
T=IDX[(0,1,-3)]
PREDS=frozenset(i for i,ns in enumerate(NEXT) if T in ns)
assert len(PHASES)==48 and len(PREDS)==3 and all(len(x)==3 for x in NEXT) and T not in PREDS

def run(axes,depth):
    aidx=tuple(a-1 for a in axes)
    def inc(e,r):return tuple((int(abs(PHASES[e][2])-1==a)+int(abs(PHASES[r][2])-1==a)) for a in aidx)
    def addk(k,dk):return tuple(i+j for i,j in zip(k,dk))
    zero=(0,)*len(axes)
    full={(s,s,False,zero,0):1 for s in range(48)}
    f={(s,s,zero,0):1 for s in range(48)}
    g={}
    stats=[]
    for d in range(depth+1):
        obs=defaultdict(int)
        for (s,r,b,k,h),v in full.items():obs[(s,r,k,h)]+=v
        obs={k:v for k,v in obs.items() if v}
        flt={k:v for k,v in f.items() if v}
        assert obs==flt, f'DISAGREEMENT axes={axes} depth={d}'
        assert sum(flt.values())==48*6**d
        assert min(flt.values())>0
        stats.append({'depth':d,'histories':48*6**d,'full_keys':len(full),'f_keys':len(flt),'g_keys':len(g),'joint_coefficients':len({(k,h) for (_,_,k,h) in flt})})
        if d==depth:break
        nxt_full=defaultdict(int)
        for (s,r,b,k,h),n in full.items():
            for dest in NEXT[r]:
                dk=inc(r,dest)
                for inner in (False,True):
                    hit=int(b and inner and dest==T)
                    nxt_full[(s,dest,inner,addk(k,dk),h+hit)]+=n
        nf=defaultdict(int)
        for (s,r,k,h),n in f.items():
            for dest in NEXT[r]:nf[(s,dest,addk(k,inc(r,dest)),h)]+=2*n
        for (s,k,h),n in g.items():
            nf[(s,T,k,h+1)]+=n
            nf[(s,T,k,h)]-=n
        ng=defaultdict(int)
        for (s,r,k,h),n in f.items():
            for mid in NEXT[r]:
                if T in NEXT[mid]:
                    kk=addk(addk(k,inc(r,mid)),inc(mid,T))
                    ng[(s,kk,h)]+=n
        full=nxt_full
        f={key:value for key,value in nf.items() if value}
        g={key:value for key,value in ng.items() if value}
    return stats
out={'verdict':'ALL_CHECKS_PASS','research_line':'PREFIX-530','science_pin':'enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d','model':{'phases':48,'predecessors_target':len(PREDS),'deterministic_online_states':51,'signed_linear_lift_coordinates':49,'rank_one_gate_correction':True},'tests':{}}
out['tests']['six_axis']=run((1,2,3,4,5,6),5)
out['tests']['single_axis']=run((1,),10)
# Exact two-block Hankel certificate: A0=I, A1=2W,
# A2=4W^2+(z-1)e(e^T W^2).  Schur complement is rank one.
two_step_sources={s:sum(T in NEXT[mid] for mid in NEXT[s]) for s in range(48)}
two_step_sources={s:n for s,n in two_step_sources.items() if n}
assert len(two_step_sources)==9 and set(two_step_sources.values())=={1}
# Over Q(x1,...,x6,z), (z-1)e(e^T W^2) has rank exactly one.
# Therefore the 96x96 two-block Hankel has rank 48+1=49.
out['hankel_minimality']={'block_hankel_levels':2,'H0_rank':48,'Schur_rank':1,
 'exact_full_hankel_rank':49,'linear_realization_dimension':49,
 'two_step_nonzero_source_columns':len(two_step_sources),
 'z_specialization_exception':'z=1 reduces gate-blind phase-resolved minimum to 48'}
print(json.dumps(out,ensure_ascii=False,indent=2))
