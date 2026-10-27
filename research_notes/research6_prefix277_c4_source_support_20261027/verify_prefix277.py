"""PREFIX-277: exact C4 source-labeled BRC ordered-pair certificates.

Author-side verifier for the Stage50 *declared observer* only.
Not the Stage46/50 original bundle, not native heartbeat evolution.
The positive rational weights, integer source loads and Z/4 phase characters
remain separate; only the contracted detector result is a scalar.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import combinations, product
import json

C4 = ((1,0),(0,1),(-1,0),(0,-1))

@dataclass(frozen=True)
class SourcePath:
    load: int
    weight: Q
    phase: int
    def __post_init__(self):
        assert isinstance(self.load,int) and self.weight>0 and self.phase in range(4)


def pair_term(source:SourcePath, target:SourcePath):
    """Return weight_s*weight_t*conj(chi_t)*chi_s as Gaussian rationals."""
    sr,si=C4[source.phase]; tr,ti=C4[target.phase]
    w=source.weight*target.weight
    return (w*(sr*tr+si*ti), w*(si*tr-sr*ti))


def norm(source_paths):
    return sum((x.weight*x.weight for x in source_paths),Q(0))


def moment(source_paths,r):
    assert r>=0
    idx={p.load:p for p in source_paths}
    assert len(idx)==len(source_paths)
    numerator=(Q(0),Q(0))
    for a in source_paths:
        b=idx.get(a.load+r)
        if b is not None:
            t=pair_term(a,b)
            numerator=(numerator[0]+t[0],numerator[1]+t[1])
    den=norm(source_paths)
    return (numerator[0]/den, numerator[1]/den)


def detector(source_paths,r,p):
    assert 0<=p<4
    cr,ci=moment(source_paths,r)
    pr,pi=C4[p]
    return Q(5,18)*(1-(pr*cr-pi*ci))


def typed_paths(loads,weights,phases):
    return tuple(SourcePath(int(j),Q(w),int(p)) for j,w,p in zip(loads,weights,phases))


def below_sharp_bound(x):
    """Exact x < (2+sqrt(2))/8, for nonnegative rational x."""
    if Q(8)*x<=2:
        return True
    return (Q(8)*x-2)**2 < 2


def run():
    A=typed_paths((0,1),(1,1),(0,3))
    B=typed_paths((0,1,2),(2,1,1),(0,3,2))
    C=typed_paths((0,1,2,3),(1,1,4,2),(0,1,0,3))
    assert (norm(A),norm(B),norm(C))==(2,6,22)
    for v in (A,B,C):
        assert moment(v,0)==(1,0)
        assert moment(v,1)==(0,Q(1,2))
        assert [detector(v,1,p) for p in range(4)] == [Q(5,18),Q(5,12),Q(5,18),Q(5,36)]
    assert moment(A,2)==(0,0)
    assert moment(B,2)==(Q(-1,3),0)
    assert moment(C,2)==(Q(1,11),0)
    assert detector(C,2,0)==Q(25,99)
    assert detector(B,2,0)==Q(10,27)

    stats={"cases":0,"c1_match":0,"three_nonzero_match":0,"two_nonzero_match":0,
           "min_c2":None,"max_c2":None}
    # Every 2- or 3-load subset from {0,...,6}, weights 1..5 and all
    # relative C4 phases. A common phase is a gauge and may be fixed to zero.
    for count in (2,3):
        for loads in combinations(range(7),count):
            for weights in product(range(1,6),repeat=count):
                for phases_rest in product(range(4),repeat=count-1):
                    paths=typed_paths(loads,weights,(0,)+phases_rest)
                    stats["cases"]+=1
                    if moment(paths,1)!=(0,Q(1,2)):
                        continue
                    stats["c1_match"]+=1
                    x,y=moment(paths,2)
                    assert y==0 and x<=0
                    if count==3:
                        stats["three_nonzero_match"]+=1
                        # If a third source exists and contributes to the same
                        # c1, then all three loads must be consecutive.
                        assert loads[1]==loads[0]+1 and loads[2]==loads[1]+1
                        assert x<0 and below_sharp_bound(-x)
                    else:
                        stats["two_nonzero_match"]+=1
                        assert x==0
                    if stats["min_c2"] is None or x<stats["min_c2"]:
                        stats["min_c2"]=x
                    if stats["max_c2"] is None or x>stats["max_c2"]:
                        stats["max_c2"]=x
    # Explicit rational family from PREFIX-276; approaches sharp irrational
    # bound without attaining it. t-> 1-sqrt(2) approximated by rational t.
    ts=[Q(-2,5),Q(-5,12),Q(-12,29),Q(-29,70),Q(-70,169)]
    closeness=[]
    for t in ts:
        a=Q(2)/(1+t*t); c=-(t-1)*(t-1)/(1+t*t)
        v=(SourcePath(0,a,0), SourcePath(1,Q(1),3), SourcePath(2,-c,2))
        assert moment(v,1)==(0,Q(1,2))
        m=moment(v,2)
        assert m[1]==0 and m[0]<0 and below_sharp_bound(-m[0])
        closeness.append(str(m[0]))
    return {
      "status":"PREFIX277_AUTHOR_SIDE_EXACT_C4_BRC_PASS",
      "model":"Stage50 declared ordered source-load pair C4 observer; not native stage46/50 original source execution",
      "source_ensemble_domain":"at most 3 distinct integer source loads, C4 phase per load, positive rational path weights",
      "finite_exhaustive_domain":"2 or 3 distinct loads chosen in [0,6], integer weights 1..5, all relative C4 phases (first fixed 0)",
      "exhaustive":{**stats, "min_c2":str(stats['min_c2']),"max_c2":str(stats['max_c2'])},
      "witnesses":{
        "A_2_loads":{"amplitudes":"[1,-i]","Z":str(norm(A)),"c1":"i/2","c2":"0","p20":str(detector(A,2,0))},
        "B_3_loads":{"amplitudes":"[2,-i,-1]","Z":str(norm(B)),"c1":"i/2","c2":"-1/3","p20":str(detector(B,2,0))},
        "C_4_loads":{"amplitudes":"[1,i,4,-2i]","Z":str(norm(C)),"c1":"i/2","c2":"1/11","p20":str(detector(C,2,0))}},
      "r1_four_phase_readouts":[str(detector(A,1,p)) for p in range(4)],
      "rational_sharp_approach_c2":closeness,
      "exact_sharp_bound":"-((2+sqrt(2))/8)<c2<=0 for <=3 source loads, c1=i/2; irrational bound not attained by rational 3-load weights",
      "native_transfer":"not verified",
      "original_stage46_stage50_bundle_execution":"not executed"
    }

if __name__=='__main__':
    print(json.dumps(run(),sort_keys=True,ensure_ascii=False,indent=2))
