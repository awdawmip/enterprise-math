"""Integer completion test for the 7-layer of the divisor dictionary of 5040."""
from fractions import Fraction
from math import factorial,prod
from itertools import combinations
import json

D=[d for d in range(2,2333) if 5040%d==0]
LOW=[d for d in D if d%7]
HIGH=[d for d in D if not d%7]
MOD=[7**j for j in (1,2,3,4,5,7)]
WIT={7:-29,14:19,21:7,28:-1,35:-1,42:-7,56:-4,63:1,70:-1,84:1,105:-3,
     112:2,126:1,168:1,210:-1,252:1}
YS=(1,2,3,4,5,6,8)


def solve(values, nodes):
    a=[[Fraction(x**j) for x in nodes]+[Fraction(values[j])] for j in range(7)]
    for j in range(7):
        pivot=next(i for i in range(j,7) if a[i][j])
        a[j],a[pivot]=a[pivot],a[j]
        q=a[j][j]
        a[j]=[x/q for x in a[j]]
        for i in range(7):
            if i!=j:
                q=a[i][j]
                a[i]=[u-q*v for u,v in zip(a[i],a[j])]
    return [a[i][-1] for i in range(7)]


def signature(word):
    row=[sum(c*(5040//d)**j for d,c in word.items()) for j in range(7)]
    return [row[j]%MOD[j-1] for j in range(1,6)]+[(row[6]-7**6*row[0])%MOD[5]]


def main():
    F=prod(factorial(j) for j in range(7))
    det=lambda nodes: prod(b-a for a,b in combinations(nodes,2))
    assert set(range(3,10))<={5040//d for d in D}
    assert set(YS)<={720//d for d in LOW}
    assert det(YS)==7*F and det(range(3,10))==F
    assert {5040//d%7 for d in HIGH}==set(range(1,7))
    assert all((720//d)%7 for d in LOW)
    # A rational solution using just the seven displayed low columns is integral.
    assert not any(signature(WIT))
    targets=[-sum(Fraction(c*(5040//d)**j,7**j) for d,c in WIT.items()) for j in range(7)]
    fills=solve(targets,YS)
    assert all(x.denominator==1 for x in fills)
    full=dict(WIT)
    for y,c in zip(YS,fills):
        full[720//y]=int(c)
    assert all(sum(c*(5040//d)**j for d,c in full.items())==0 for j in range(7))
    costs=[sum(max(s*c,0)*(d-1) for d,c in WIT.items()) for s in (1,-1)]
    n=-sum(WIT.values())
    target=-sum(Fraction(c,d) for d,c in WIT.items())
    assert costs==[1297,1332] and n==14 and target==Fraction(493,180)
    lower=Fraction(n*n,n+max(costs)-costs[0])
    assert lower==4 and lower>target
    # The ordinary six congruences alone accept a simple vector the upgraded map rejects.
    control={7:7**6}
    assert not any(signature(control)[:5]) and signature(control)[5]!=0
    assert all(sum(c*(5040//d)**j for d,c in control.items())%(7**j)==0 for j in range(1,7))
    print(json.dumps({"dictionary_counts":[len(D),len(LOW),len(HIGH)],"unscaled_vandermonde_product":F,
           "quotient_index":prod(MOD),"channel_moduli":MOD,
           "old_only_control_and_signature":[control,signature(control)],
           "witness_high":WIT,"high_side_charges":costs,"unrestricted_low_completion":{720//y:int(c) for y,c in zip(YS,fills)},
           "finite_budget_obstruction":{"budget":1332,"required_atoms":n,
             "required_first_moment":str(target),"minimum_by_cauchy":str(lower)}},indent=2,sort_keys=True))


if __name__=="__main__":
    main()
