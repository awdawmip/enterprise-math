#!/usr/bin/env python3
"""EC49N exact Fraction certificates: positive-rational two-source auxiliary BRC."""
import json
from fractions import Fraction as F
from itertools import product

ACTIONS=("ACCEPT","REJECT","A0","A1")
SECOND=("ACCEPT","REJECT","BUY")
WEIGHT={s:(F(1,2),F(1,2)) for s in ("P","Q")}
Y0={"P":(F(1,4),F(3,4)),"Q":(F(3,4),F(1,4))}
Y1INERT={s:(F(1,2),F(1,2)) for s in ("P","Q")}

def kernels(kind):
    if kind=="DISTORTED":
        return {s:(Y0[s],Y1INERT[s]) for s in ("P","Q")}
    if kind=="NEUTRAL":
        return {s:(Y0[s],Y0[s]) for s in ("P","Q")}
    raise ValueError(kind)

def atoms(kind):
    k=kernels(kind)
    return {s:{(w,y0,y1):F(1,2)*
                (k[s][0][w] if y0 else 1-k[s][0][w])*
                (k[s][1][w] if y1 else 1-k[s][1][w])
                for w,y0,y1 in product(range(2),repeat=3)}
            for s in ("P","Q")}

def observable(kind,first,second,terminal,memory=False):
    p=atoms(kind); totals=[]
    for s in ("P","Q"):
        accepted=F(0); cost=F(0)
        for (w,y0,y1),mass in p[s].items():
            initial=first[w]
            if initial=="ACCEPT":
                accepted+=mass
            elif initial=="REJECT":
                continue
            else:
                a=int(initial[-1]); y=y0 if a==0 else y1
                cost+=mass
                decision=second[(w,a) if memory else a]
                if decision=="ACCEPT":
                    accepted+=mass
                elif decision=="BUY":
                    cost+=mass
                    if terminal[(w,a,y) if memory else (a,y)]:
                        accepted+=mass
                else:
                    assert decision=="REJECT"
        totals.append((accepted,cost))
    return (totals[0][0],totals[1][0],totals[0][1],totals[1][1])

def compact(kind):
    best=F(-100); winner=None; vectors=set(); count=0
    for first in product(ACTIONS,repeat=2):
        for sec in product(SECOND,repeat=2):
            second=dict(enumerate(sec))
            for term in product((0,1),repeat=4):
                terminal={(a,y):term[2*a+y] for a in range(2) for y in range(2)}
                o=observable(kind,first,second,terminal)
                count+=1; vectors.add(o)
                if o[0]-o[1]>best:
                    best=o[0]-o[1]; winner=(first,sec,term,o)
    assert count==2304
    return best,winner,vectors,count

def local_plans():
    yield ("ACCEPT",None,None)
    yield ("REJECT",None,None)
    for a in (0,1):
        for second in ("ACCEPT","REJECT"):
            yield (f"A{a}",second,None)
        for term in product((0,1),repeat=2):
            yield (f"A{a}","BUY",term)

def full(kind):
    k=kernels(kind)
    plans=list(local_plans()); assert len(plans)==14
    best=F(-100); winner=None; vectors=set()
    for pair in product(plans,repeat=2):
        acc=[F(0),F(0)]; costs=[F(0),F(0)]
        for i,s in enumerate(("P","Q")):
            for w,(first,second,term) in enumerate(pair):
                mass=WEIGHT[s][w]
                if first=="ACCEPT":
                    acc[i]+=mass
                elif first=="REJECT":
                    continue
                else:
                    a=int(first[-1]); costs[i]+=mass
                    if second=="ACCEPT":
                        acc[i]+=mass
                    elif second=="BUY":
                        costs[i]+=mass
                        p1=k[s][a][w]
                        acc[i]+=mass*((1-p1)*term[0]+p1*term[1])
        o=(acc[0],acc[1],costs[0],costs[1])
        vectors.add(o)
        if o[0]-o[1]>best:
            best=o[0]-o[1]; winner=(pair,o)
    return best,winner,vectors,len(plans)**2

def main():
    for kind in ("DISTORTED","NEUTRAL"):
        masses=atoms(kind)
        assert all(len(masses[s])==8 and sum(masses[s].values())==1 for s in ("P","Q"))
        assert all(x>0 for s in ("P","Q") for x in masses[s].values())
    bc,wc,vc,nc=compact("DISTORTED")
    bf,wf,vf,nf=full("DISTORTED")
    assert (bc,bf,nc,nf)==(F(1,4),F(1,2),2304,196)
    assert vc.issubset(vf)
    first=("A0","A0")
    sec={(w,a):"BUY" for w,a in product(range(2),repeat=2)}
    term={(w,a,y):int((w==0 and y==0) or (w==1 and y==1))
          for w,a,y in product(range(2),repeat=3)}
    ov=observable("DISTORTED",first,sec,term,True)
    assert ov==(F(3,4),F(1,4),F(2),F(2))
    oc=observable("DISTORTED",("A0","A1"),{0:"BUY",1:"REJECT"},
                  {(0,0):1,(0,1):0,(1,0):0,(1,1):0})
    assert oc==(F(3,8),F(1,8),F(3,2),F(3,2))
    for pu,pv in product((F(0),F(1)),repeat=2):
        d=(pu-pv)/4
        for y in (0,1):
            observed=sum(
                WEIGHT["P"][w]*(pu if w==0 else pv)*
                (Y0["P"][w] if y else 1-Y0["P"][w])-
                WEIGHT["Q"][w]*(pu if w==0 else pv)*
                (Y0["Q"][w] if y else 1-Y0["Q"][w])
                for w in range(2))
            assert observed==(d if y==0 else -d)
    cb,_,cv,cn=compact("NEUTRAL")
    fb,_,fv,fn=full("NEUTRAL")
    assert cb==fb==F(1,2)
    assert cv==fv
    report={
      "schema":"EC49N_UNIFORM_MENU_EXACT_V1",
      "source_atoms_per_measure":8,
      "all_source_atoms_positive":True,
      "first_actions":list(ACTIONS),
      "post_action_choices":list(SECOND),
      "each_variant_compressed_pure_count":nc,
      "each_variant_full_induced_pure_count":nf,
      "total_pure_enumerations_both_variants":2*(nc+nf),
      "distorted":{
        "compact_distinct_vectors":len(vc),"full_distinct_vectors":len(vf),
        "compact_max_alpha_minus_beta":str(bc),"full_max_alpha_minus_beta":str(bf),
        "sharp_support_gap":str(bf-bc),
        "full_witness":[str(x) for x in ov],
        "compact_witness":[str(x) for x in oc],
        "early_accept_allowed":True},
      "neutral":{
        "compact_distinct_vectors":len(cv),"full_distinct_vectors":len(fv),
        "identical_pure_four_vector_sets":True,
        "support_both":str(cb),
        "entire_real_region_equality":"analytic action-coding theorem"},
      "status":"AUTHOR_EXACT_UNREVIEWED_NOT_ADMITTED",
      "scope":"positive-rational auxiliary BRC; no signed/native X6 inference"
    }
    print(json.dumps(report,sort_keys=True,indent=2))
if __name__=="__main__":
    main()
