#!/usr/bin/env python3
"""R237 exact-rational endpoint certificate; standard library only."""
from fractions import Fraction as Q
from itertools import combinations
import json

C = Q(5, 18)
SIGMA = Q(197, 200)
LEFT = Q(39, 100)
RIGHT = Q(41, 100)
LOWER_R = Q(594323, 600000)

def t(s):
    return (1691*s - 2615)/(2615*s - 3539)

def parameters(s):
    a = [Q(1, 5), Q(1, 4), Q(3, 10), Q(9, 20), s, Q(2, 3), t(s)]
    b = [Q(13, 60)] + [C*abs(Q(1, 2)-v) for v in a[1:]]
    pi = [v/(1-u) for u, v in zip(a, b)]
    z = sum(pi[i]/(1-a[i]) for i in range(7))
    rho = [pi[i]/(1-a[i])/z for i in range(7)]
    return a, b, pi, rho

def contribution(s, j, x=SIGMA):
    a, b, _, _ = parameters(s)
    return b[j]/(x-a[j])

def secular(s, missing, x=SIGMA):
    return sum(contribution(s, j, x) for j in range(7) if j != missing)-1

def qtext(x):
    return str(x.numerator)+"/"+str(x.denominator)

def run():
    assert t(LEFT)<t(RIGHT)<Q(4,5)<SIGMA
    assert SIGMA>max(parameters(RIGHT)[0])
    f4max=secular(RIGHT,4)
    q4max=contribution(LEFT,4)
    assert f4max==Q(-34189956955753,43781593262648493)
    assert q4max==Q(55,1071) and f4max<0
    margins={}
    for j in (1,2,5,6):
        delta=contribution(LEFT,j)-q4max
        assert delta>0
        margins[str(j)]=qtext(delta)
    assert 1691*(-3539)+2615**2==853776
    assert LOWER_R>SIGMA and SIGMA/LOWER_R==Q(591000,594323)
    samples=[]
    for s in (LEFT,Q(2,5),RIGHT):
        a,b,pi,rho=parameters(s)
        assert sum(pi)==1 and sum(rho)==1
        assert all(0<aj<1 for aj in a)
        assert all(x>0 for x in pi)
        deletion={str(i):qtext(secular(s,i)) for i in range(1,7)}
        assert all(secular(s,i)<0 for i in (1,2,4,5,6))
        assert secular(s,3)>0
        mask_count=0
        for k in range(6):
            for U in combinations(range(1,7),k):
                D=set((0,)+U)
                if D=={0,1,2,4,5,6}:
                    continue
                assert any(i not in D for i in (1,2,4,5,6))
                mask_count+=1
        assert mask_count==62
        samples.append({"s":qtext(s),
            "stationary_normalization":qtext(sum(rho)),
            "secular_at_sigma_by_deleted_source":deletion,
            "other_masks_checked":mask_count})
    return {"result":"PASS",
        "arithmetic":"exact rational Fraction; continuum monotonicities in proof note",
        "scope":"R234 real s in (39/100,41/100); endpoint certificates and three rational samples",
        "sigma":qtext(SIGMA),
        "f_minus4_at_right_endpoint":qtext(f4max),
        "largest_source4_secular_contribution":qtext(q4max),
        "positive_source_contribution_margins":margins,
        "sharper_uniform_spectral_ratio_using_R236":qtext(SIGMA/LOWER_R),
        "samples":samples,
        "independent_math_review":"NOT_REVIEWED",
        "native_BRC_execution":"NOT_EXECUTED"}

if __name__=="__main__":
    print(json.dumps(run(),indent=2,ensure_ascii=False,sort_keys=True))
