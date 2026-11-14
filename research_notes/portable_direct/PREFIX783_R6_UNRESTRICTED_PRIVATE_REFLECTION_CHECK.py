"""PREFIX-783: exact-rational regression of the private-reflection symmetrization theorem.
External two-parameter Gamma-observer algebra only; no native BRC computation.
Python standard library; no scientific recurrence coefficients recomputed.
"""
from fractions import Fraction as F
from random import Random
import json

SIGNS = (1, -1, -1)

def distribute(value, budgets):
    assert abs(value) <= sum(budgets, F(0))
    remaining = abs(value)
    sign = 1 if value >= 0 else -1
    out = []
    for coeff, cap in zip(SIGNS, budgets):
        take = min(cap, remaining)
        out.append(sign * coeff * take)
        remaining -= take
    assert remaining == 0
    assert sum((a*b for a, b in zip(SIGNS, out)), F(0)) == value
    return out

def clamp(x, lo, hi):
    return min(hi, max(lo, x))

def criterion(x1, x2, b1, b2, c, delta):
    assert min(b1,b2,c,delta)>=0
    d = min(delta, 2*c)
    return abs(x1)<=b1+c and abs(x2)<=b2+c and abs(x1-x2)<=b1+b2+d

def construct(x1, x2, caps1, caps2, c, delta):
    b1=sum(caps1,F(0)); b2=sum(caps2,F(0))
    if not criterion(x1,x2,b1,b2,c,delta): return None
    r=max(F(0),abs(x1-x2)-b1-b2)
    assert r<=min(delta,2*c)
    low=max(-c+r/2,-x1-b1-r/2,-x2-b2-r/2)
    high=min(c-r/2,-x1+b1+r/2,-x2+b2+r/2)
    assert low<=high
    s=low; h=s+r/2; hp=s-r/2
    u1=clamp(-x1-s,-b1,b1); u2=clamp(-x2-s,-b2,b2)
    v1=distribute(u1,caps1);v2=distribute(u2,caps2)
    out=[x1+h+u1,x2+h+u2,-x1-hp-u1,-x2-hp-u2]
    assert all(a>=0 for a in out)
    assert abs(h)<=c and abs(hp)<=c and abs(h-hp)<=delta
    for v,caps in ((v1,caps1),(v2,caps2)):
        assert all(abs(e)<=cap for e,cap in zip(v,caps))
    return {'h':h,'hp':hp,'s':s,'r':r,'private1':v1,'private2':v2,'mixed':out}

def direct_interval_oracle(x1,x2,b1,b2,c,delta):
    d=min(delta,2*c)
    r=d
    intervals=[(-c+r/2,c-r/2),(-x1-b1-r/2,-x1+b1+r/2),
               (-x2-b2-r/2,-x2+b2+r/2)]
    return max(a for a,b in intervals)<=min(b for a,b in intervals)

def frac_str(x):return str(x.numerator)+'/'+str(x.denominator)

rng=Random(78320261114)
counts={'total':0,'sign_loss_feasible':0,'strict_two_sign_universal':0,
        'boundary_equalities':0,'constructed_exact_observers':0}
for j in range(4096):
    q=F(rng.randrange(1,81),rng.choice((10,20,40)))
    a1=F(rng.randrange(-15,31),20); a2=F(rng.randrange(-15,31),20)
    B1=F(rng.randrange(1,13),10); B2=B1+F(rng.randrange(1,13),10)
    x1=a1-q*B1;x2=a2-q*B2
    caps1=tuple(F(rng.randrange(0,7),20) for _ in range(3))
    caps2=tuple(F(rng.randrange(0,7),20) for _ in range(3))
    c=F(rng.randrange(0,7),20);delta=F(rng.randrange(0,9),20)
    s1=sum(caps1,F(0));s2=sum(caps2,F(0))
    yes=criterion(x1,x2,s1,s2,c,delta)
    assert yes == direct_interval_oracle(x1,x2,s1,s2,c,delta)
    obj=construct(x1,x2,caps1,caps2,c,delta)
    assert (obj is not None)==yes
    counts['total']+=1
    if yes:
        counts['sign_loss_feasible']+=1; counts['constructed_exact_observers']+=1
        if (abs(x1)==s1+c or abs(x2)==s2+c or
            abs(x1-x2)==s1+s2+min(delta,2*c)):
            counts['boundary_equalities']+=1
    else: counts['strict_two_sign_universal']+=1

A1,A2,B1,B2=F(1),F(2),F(2),F(3)
caps1=(F(1,10),F(1,20),F(1,20))
caps2=(F(1,20),F(1,20),F(1,20))
c=F(1,10)
assert not criterion(A1-F(3,5)*B1,A2-F(3,5)*B2,
                     sum(caps1),sum(caps2),c,F(0))
assert construct(A1-F(3,5)*B1,A2-F(3,5)*B2,caps1,caps2,c,F(1,10)) is not None
assert construct(A1-F(13,20)*B1,A2-F(13,20)*B2,caps1,caps2,c,F(0)) is not None
x1=A1-F(3,5)*B1;x2=A2-F(3,5)*B2
unequal=[x1+sum(caps1), x2-sum(caps2),-x1+sum(caps1),-x2-sum(caps2)]
assert unequal==[F(0),F(1,20),F(2,5),F(-7,20)]
assert max(unequal)>0>min(unequal)

out={
 'schema':'PREFIX783_R6_PRIVATE_REFLECTION_SYMMETRIZATION_RESULTS_V1',
 'model':'two adjacent Gamma auxiliary grid cells and reflected cells',
 'scientific_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'theorem':'Independent private reflected corner errors with pairwise equal budgets do not expand exact pointwise loss-of-both-strict-signs set; all sign-loss configurations symmetrize to identical private pairs.',
 'criterion':'abs(x1)<=S1+c AND abs(x2)<=S2+c AND abs(x1-x2)<=S1+S2+min(delta,2c)',
 'arithmetic':'Python Fraction: exact rational; finite deterministic regression, not proof of universal statement',
 'counts':counts,
 'example':{'q_outside':'3/5','delta_outside':'0',
            'all_four_unrestricted_signs':[frac_str(x) for x in unequal],
            'q_inside':'3/5','delta_inside':'1/10',
            'q_endpoint':'13/20','delta_endpoint':'0'},
 'excluded':'No native comparator observation, BRC propagation, physical time or source recurrence execution; no Task/CLAIM/result review.',
 'status':'ALL_CHECKS_PASS PREFIX783 PRIVATE_REFLECTION_SYMMETRIZATION'
}
with open('PREFIX783_R6_UNRESTRICTED_PRIVATE_REFLECTION_RESULTS.json','w',encoding='utf-8') as f:
    json.dump(out,f,indent=2,ensure_ascii=False)
    f.write('\n')
print(json.dumps(out,indent=2))
