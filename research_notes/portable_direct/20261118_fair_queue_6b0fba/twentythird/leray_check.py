"""Exact rectangular-norm cost of the three-dimensional Leray projection."""
from fractions import Fraction
from itertools import product
import json


def power_ratio(a, b):
    """The column sum on a direction (a,b,b), homogeneous in (a,b)."""
    return Fraction(2*b*(a+b), a*a+2*b*b)


def farey_bracket(K):
    """Farey neighbors of sqrt(3)-1 of order K, via integer mediants."""
    if type(K) is not int or K < 1:
        raise ValueError('K must be a positive integer box cutoff')
    a,b,c,d = 0,1,1,1
    steps = 0
    while b+d <= K:
        m,n = a+c,b+d
        if (m+n)**2 < 3*n*n:
            a,b = m,n
        else:
            c,d = m,n
        steps += 1
    assert b*c-a*d == 1 and b <= K and d <= K < b+d
    return (a,b), (c,d), steps


def exact_column_norm(K) -> Fraction:
    """Best l1 column norm for the nonzero modes in the integer box [-K,K]^3."""
    lower,upper,_ = farey_bracket(K)
    return max(power_ratio(*lower),power_ratio(*upper))


def literal_column(k, j):
    den = sum(v*v for v in k)
    return Fraction(sum(abs((den if i==j else 0)-v*k[j]) for i,v in enumerate(k)), den)


def certificate(K):
    lower,upper,steps = farey_bracket(K)
    score = exact_column_norm(K)
    winners = [pair for pair in (lower,upper) if power_ratio(*pair)==score]
    return dict(K=K,lower=lower,upper=upper,winning_slopes=winners,mediants=steps,
                maximum=[score.numerator,score.denominator])


def main():
    # Each signed direction and every original matrix column are enumerated.
    cubemax = {}
    for k in product(range(-12,13),repeat=3):
        radius = max(map(abs,k))
        if radius:
            observed = max(literal_column(k,j) for j in range(3))
            cubemax[radius] = max(cubemax.get(radius,Fraction(0)),observed)
    prev = Fraction(0)
    for K in range(1,13):
        prev=max(prev,cubemax[K]);assert exact_column_norm(K)==prev
    # Enumerate all possible integer symmetric directions independently.
    record=Fraction(0)
    for K in range(1,401):
        record=max(record,*(power_ratio(a,K) for a in range(K+1)))
        assert record==exact_column_norm(K)
    maxK=10000
    pell=[]; y,n=2,1
    expected=set()
    while y<=maxK:
        assert y*y-3*n*n==1
        pell.append([y,y+n-1]); expected.update(range(y,min(y+n,maxK+1)))
        y,n=2*y+3*n,y+2*n
    for K in range(1,maxK+1):
        low,hi,_=farey_bracket(K)
        assert (power_ratio(*low)==power_ratio(*hi))==(K in expected)
    # Excluding the special K=2 tie, a maximal column has |k_j'|=|k_j''|.
    asymmetric=[]
    for K in range(1,13):
        best=exact_column_norm(K)
        for a,b,c in product(range(K+1),repeat=3):
            if b<c and literal_column((a,b,c),0)==best:
                asymmetric.append([K,a,b,c])
    assert asymmetric==[[2,1,1,2]]
    examples=[certificate(k) for k in (1,2,3,4,7,10,11,26,40,128,1024,10**6,10**15)]
    print(json.dumps(dict(signed_directions_checked=25**3-1,
        matrix_columns_checked=3*(25**3-1),all_literal_cube_cutoffs=[1,12],
        symmetric_direction_check_through=400,all_pell_ties_checked_through=maxK,
        pell_tie_intervals_starting_by_10000=pell,asymmetric_column_examples=asymmetric,
        cutoffs=examples),indent=2))


if __name__=='__main__':
    main()
