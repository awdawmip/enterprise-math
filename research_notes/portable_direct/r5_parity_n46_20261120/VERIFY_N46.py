"""R5 N^46 parity coefficient exact checker (standard-library only)."""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import comb
import json

SHORT = (
    set(range(214, 219)),
    {214, 216, 217, 218, 219, 220, 221},
    set(range(215, 222)),
)

def moment_at_minus_one(m, prices):
    """Return H(-1), H'(-1); the local total count is <m."""
    coeff = [1] + [0]*(m - 1)
    deriv = [0]*m
    for p in sorted(prices):
        c1, d1 = [0]*m, [0]*m
        for j in range(m):
            sign = (-1)**(p*j)
            for k in range(m - j):
                c1[j+k] += coeff[k]*sign
                d1[j+k] += (deriv[k]-p*j*coeff[k])*sign
        coeff, deriv = c1, d1
    return sum(coeff), sum(deriv)

def overlap_minus_one(m):
    """Signed sum of h=max(0, number of short failures-1)."""
    states = {(0,0,0):1}
    for p in range(214,222):
        memberships = tuple(int(p in s) for s in SHORT)
        after = defaultdict(int)
        for state, weight in states.items():
            for n in range(m):
                target = tuple(min(m,state[i]+n*memberships[i]) for i in range(3))
                after[target] += weight * (-1)**(p*n)
        states = after
    return sum(w*max(sum(v<m for v in key)-1,0) for key,w in states.items())

def coefficients(m):
    a,d0 = moment_at_minus_one(m,SHORT[0])
    b,d2 = moment_at_minus_one(m,SHORT[2])
    c = moment_at_minus_one(m,SHORT[1])[0]
    h = overlap_minus_one(m)
    assert a == sum((j+1)*(m-2*j) for j in range((m-1)//2+1))
    assert b == (comb((m-1)//2+3,3) if m%2 else 0)
    return dict(m=m,a=a,d0=d0,b=b,d2=d2,c=c,h=h,
        C_over_C1=str(Fraction(107*a+440*b,547)),
        K_over_C1=str(Fraction(107*(12792*a+d0)+440*(12569*b+d2)
                               +47080*c-94160*h,547)))

def brute_overlap(m):
    total=0
    for n in product(range(m),repeat=8):
        failures=sum(sum(n[p-214] for p in s)<m for s in SHORT)
        total+=max(failures-1,0)*(-1)**sum(p*n[p-214] for p in range(214,222))
    return total

def brute_moment(m,prices):
    prices=sorted(prices)
    def rec(i,remaining,cost):
        if i==len(prices):
            sign=(-1)**cost
            return sign,-cost*sign
        a=b=0
        for n in range(remaining):
            x,y=rec(i+1,remaining-n,cost+n*prices[i])
            a+=x; b+=y
        return a,b
    return rec(0,m,0)

if __name__=="__main__":
    for m in range(1,5):
        assert overlap_minus_one(m)==brute_overlap(m),m
        for s in SHORT:
            assert moment_at_minus_one(m,s)==brute_moment(m,s),m
    vals=[coefficients(m) for m in range(1,18)]
    for m,value in ((1,"6757864/547"),(2,"2810296/547"),
                    (3,"27096176/547"),(5,"66417936/547"),
                    (8,"52448800/547"),(17,"824701320/547")):
        assert vals[m-1]["K_over_C1"]==value
    print(json.dumps({"method":"exact signed DP + independent enumeration for m<=4",
        "m_range":[1,17],"samples":[vals[i-1] for i in (1,2,3,5,8,17)],
        "scope":"all fixed positive m by symbolic Laurent argument"},
        ensure_ascii=False,indent=2))
