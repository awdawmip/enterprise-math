"""One finite triangular inventory slab; all readouts and comparisons exact."""
from fractions import Fraction as Q
from itertools import combinations_with_replacement
from functools import cache
import json


@cache
def edge(n,s,k):
    rho=Q(4)
    for j in range(s,n+1):
        rho *= Q(4*j+k,4*(j+k))
    inv_a=Q(28*(k-1+4*s),k-1+s)
    for j in range(3*k):
        inv_a *= Q(s+k+j,n+k+1+j)
    return rho, rho*inv_a


def read_two(c, v, w):
    z = []
    x = Q(840, (w+2)*(w+3)*(w+4))
    y = Q(1)
    for j in range(3,w+1):
        y *= Q(4*j+1, 4*j+4)
    for a,b in ((Q(3,32),Q(15,32)),(Q(3,2),Q(15,8)),(Q(6),Q(3))):
        z.append(y*(x*a+b)/(1+x*y*a))
    for n,s,k in ((v,w,3),(c,v,5)):
        rho,tau = edge(n,s,k)
        z = [(rho+tau*t)/(1+tau*t) for t in z]
    return max(z)/min(z)


def main():
    reports = []
    for c, t in ((4096,4),(4096,8),(8192,8)):
        vals=[read_two(c,v,w) for w,v in combinations_with_replacement(range(t,2*t+1),2)]
        assert len(vals)==(t+1)*(t+2)//2 and len(set(vals))==len(vals)
        width=max(vals)-1
        assert width>0
        # Largest b for which every slab value lies in [1, 1+2^-b).
        b=width.denominator.bit_length()-width.numerator.bit_length()
        if width*(1<<b)>=1: b-=1
        assert width*(1<<b)<1<=width*(1<<(b+1))
        reports.append(dict(c=c,T=t,distinct_exact_words=len(vals),
                            max_single_bin_bits=b,all_offsets_at_most_bins=2,
                            minimum_ambiguous_words_for_any_offset=len(vals)-2))
    print(json.dumps(reports,indent=2))


if __name__=='__main__':
    main()
