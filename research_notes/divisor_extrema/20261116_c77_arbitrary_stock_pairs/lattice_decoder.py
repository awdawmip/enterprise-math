"""Exact inversion at n >= 72*max(c,100), using certified rank-three LLL.

Compile the included GMP utility with
  c++ -O3 -std=c++17 kernel_lll.cpp -lgmpxx -lgmp -o kernel_lll
Then pass an exact fractions.Fraction to decode(c,n,measurement).
"""
from bisect import bisect_left
from fractions import Fraction as Q
from pathlib import Path
import subprocess
from far_decoder import _first_parameters, _inner_extremes, _rising, outer_product


def decode(c, n, measurement, *, executable=None, certificate=None):
    """Decode the original unordered statistic, and check both physical endpoints."""
    if not isinstance(c,int) or not isinstance(n,int) or c<2 or n<72*max(c,100):
        raise ValueError("require integer c>=2 and n>=72*max(c,100)")
    if not isinstance(measurement,(Q,int)) or measurement<=1:
        raise ValueError("expected an exact rational readout greater than one")
    g=Q(measurement)
    P=_rising(n+6,15)
    z=P/outer_product(n)
    H=(P+1) << (104*max(c,100))
    if executable is None:
        executable=Path(__file__).resolve().parent/"kernel_lll"
    # Hexadecimal avoids interpreter limits on the number of decimal digits.
    row=" ".join(format(t,"x") for t in
                 (z.numerator,z.denominator,g.numerator,g.denominator))
    first,swaps=subprocess.check_output([executable],input=row.encode()).decode().splitlines()
    coeff=tuple(int(t,16) for t in first.split())
    if len(coeff)!=4 or max(map(abs,coeff))>4*H:
        raise ArithmeticError("LLL vector exceeds the certified height")
    u0,u1,v0,v1=coeff
    if not u1*v1 or not (u0*v1-u1*v0) or (v0+v1*z)*g!=u0+u1*z:
        raise ArithmeticError("uncertified rational-function relation")
    # g(z)=K*(z+AL)/(z+AH).
    K=Q(u1,v1)
    AL,AH=Q(u0,u1),Q(v0,v1)
    if K==1:
        raise ValueError("nonphysical constant at infinity")
    A=(AH-K*AL)/(P*(K-1))
    first_range=range(2,c+1)
    v=2+bisect_left(first_range,A,key=lambda j:_first_parameters(j)[0])
    if v>c or _first_parameters(v)[0]!=A:
        raise ValueError("no legal first landing")
    B=_first_parameters(v)[1]
    extremes=tuple(sorted((AL/(A*B),AH/(A*B))))
    def ratio(pair):
        low,high=sorted(abs(a-1) for a in pair)
        if low==0:
            raise ValueError("blind inner endpoint")
        return high/low
    w=2+bisect_left(range(2,v+1),ratio(extremes),key=lambda j:ratio(_inner_extremes(v,j)))
    if w>v or _inner_extremes(v,w)!=extremes:
        raise ValueError("no legal second landing")
    if certificate is not None:
        certificate.update(lll_swaps=int(swaps), output_max_bits=max(abs(k).bit_length() for k in coeff),
                           template=[v,w])
    return v,w
