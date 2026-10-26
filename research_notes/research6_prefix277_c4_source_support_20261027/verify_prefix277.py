"""PREFIX-277 source-labeled exact C4 path-pair BRC checker (author-side only).

Not Stage46/50 original source execution or physical H_n dynamics.
No floating point, π, trigonometry, Taylor, Padé, Cayley or propagator.
"""
from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import combinations, product
import json

C4 = ((1, 0), (0, 1), (-1, 0), (0, -1))

@dataclass(frozen=True)
class SourcePath:
    load: int
    weight: Q
    phase: int
    def __post_init__(self):
        assert isinstance(self.load, int) and self.weight > 0 and self.phase in range(4)

def pair_term(a, b):
    """weight_a*weight_b*conj(phase_b)*phase_a, preserving ordered source pair."""
    ar, ai = C4[a.phase]
    br, bi = C4[b.phase]
    w = a.weight * b.weight
    return (w * (ar*br + ai*bi), w * (ai*br - ar*bi))

def norm(paths):
    return sum((p.weight*p.weight for p in paths), Q(0))

def moment(paths, r):
    assert isinstance(r, int) and r >= 0
    index = {p.load:p for p in paths}
    assert len(index) == len(paths)
    real = imag = Q(0)
    for a in paths:
        b = index.get(a.load+r)
        if b is not None:
            x, y = pair_term(a,b)
            real += x
            imag += y
    z = norm(paths)
    return (real/z, imag/z)

def detector(paths, r, p):
    assert 0 <= p < 4
    real, imag = moment(paths,r)
    pr, pi = C4[p]
    return Q(5,18)*(1 - (pr*real - pi*imag))

def packet(loads, weights, phases):
    return tuple(SourcePath(int(j), Q(w), int(p)) for j,w,p in zip(loads,weights,phases))

def strictly_below_sharp(x):
    """Decide rational x < (2+sqrt(2))/8 without square-root approximation."""
    if 8*x <= 2:
        return True
    return (8*x-2)**2 < 2

def run():
    A=packet((0,1),(1,1),(0,3))
    B=packet((0,1,2),(2,1,1),(0,3,2))
    C=packet((0,1,2,3),(1,1,4,2),(0,1,0,3))
    assert [norm(v) for v in (A,B,C)] == [2,6,22]
    signature=[Q(5,18),Q(5,12),Q(5,18),Q(5,36)]
    for v in (A,B,C):
        assert moment(v,0) == (1,0)
        assert moment(v,1) == (0,Q(1,2))
        assert [detector(v,1,p) for p in range(4)] == signature
    assert moment(A,2) == (0,0)
    assert moment(B,2) == (Q(-1,3),0)
    assert moment(C,2) == (Q(1,11),0)
    assert detector(A,2,0)==Q(5,18)
    assert detector(B,2,0)==Q(10,27)
    assert detector(C,2,0)==Q(25,99)
    stats={"cases":0,"c1_match":0,"two_nonzero_match":0,"three_nonzero_match":0}
    lows=[]
    for count in (2,3):
        for loads in combinations(range(7),count):
            for weights in product(range(1,6),repeat=count):
                for rest in product(range(4), repeat=count-1):
                    paths=packet(loads,weights,(0,)+rest)
                    stats["cases"]+=1
                    if moment(paths,1)!=(0,Q(1,2)):
                        continue
                    stats["c1_match"]+=1
                    x,y=moment(paths,2)
                    assert y==0 and x<=0
                    if count==2:
                        stats["two_nonzero_match"]+=1
                        assert x==0 and loads[1]==loads[0]+1
                    else:
                        stats["three_nonzero_match"]+=1
                        assert loads[1]==loads[0]+1 and loads[2]==loads[1]+1
                        assert x<0 and strictly_below_sharp(-x)
                    lows.append(x)
    assert stats=={"cases":72100,"c1_match":60,"two_nonzero_match":30,"three_nonzero_match":30}
    ts=[Q(-2,5),Q(-5,12),Q(-12,29),Q(-29,70),Q(-70,169)]
    sequence=[]
    for t in ts:
        a=Q(2)/(1+t*t); c=-(t-1)*(t-1)/(1+t*t)
        v=(SourcePath(0,a,0),SourcePath(1,Q(1),3),SourcePath(2,-c,2))
        assert moment(v,1)==(0,Q(1,2))
        x,y=moment(v,2)
        assert y==0 and x<0 and strictly_below_sharp(-x)
        sequence.append(str(x))
    return {
        "status":"PREFIX277_AUTHOR_SIDE_EXACT_C4_BRC_PASS",
        "model":"Stage50 declared ordered source-load pair C4 observer; no native original execution",
        "domain":"2 or 3 occupied loads chosen from 0..6, integer weights 1..5 and all relative C4 phases",
        "exhaustive":{**stats,"min_c2":str(min(lows)),"max_c2":str(max(lows))},
        "r1_four_phase_readouts":[str(x) for x in signature],
        "witnesses":{
           "A_2_loads":{"amplitudes":"[1,-i]","Z":"2","c1":"i/2","c2":"0","p20":"5/18"},
           "B_3_loads":{"amplitudes":"[2,-i,-1]","Z":"6","c1":"i/2","c2":"-1/3","p20":"10/27"},
           "C_4_loads":{"amplitudes":"[1,i,4,-2i]","Z":"22","c1":"i/2","c2":"1/11","p20":"25/99"}},
        "rational_sharp_approach_c2":sequence,
        "strict_sharp_bound":"-(2+sqrt(2))/8<c2<=0 for <=3 source loads, c1=i/2",
        "native_transfer":"not verified",
        "original_stage46_stage50_bundle_execution":"not executed"
    }

if __name__=="__main__":
    print(json.dumps(run(),ensure_ascii=False,sort_keys=True,indent=2))
