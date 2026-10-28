#!/usr/bin/env python3
"""Exact symbolic interface checks, not an Euler/BRC-world re-execution."""
from fractions import Fraction as Q
import hashlib
import json
from math import comb
from pathlib import Path
import sympy as S

u=S.Symbol('u')
C=lambda z:(18-9*z-11*z*z-8*z**3)/(18-2*z*z+2*z**4)
R0=lambda z:3*z*z/(9-4*z*z)
R1=lambda z:2*z**3/(9-4*z*z)

def rat_coeffs(expr, length):
    expr=S.cancel(expr)
    num,den=S.fraction(expr)
    pn=S.Poly(num,u);pd=S.Poly(den,u)
    nums=[Q(pn.nth(i)) for i in range(length)]
    dens=[Q(pd.nth(i)) for i in range(pd.degree()+1)]
    out=[]
    for i in range(length):
        out.append((nums[i]-sum(dens[j]*out[i-j] for j in range(1,min(i,len(dens)-1)+1)))/dens[0])
    return out

def renewal_occupancy(wait_pmf, horizon):
    # T_0=0; convolution tracks the complete positive waiting distribution.
    arrival=[Q(0)]*(horizon+1);arrival[0]=Q(1)
    distributions=[]
    survival=[sum(p for w,p in wait_pmf.items() if w>t) for t in range(horizon+1)]
    for n in range(horizon+1):
        occupancy=[sum(arrival[j]*survival[t-j] for j in range(t+1)) for t in range(horizon+1)]
        distributions.append(occupancy)
        nxt=[Q(0)]*(horizon+1)
        for t,p in enumerate(arrival):
            for w,pw in wait_pmf.items():
                if t+w<=horizon:nxt[t+w]+=p*pw
        arrival=nxt
    assert all(sum(distributions[n][t] for n in range(horizon+1))==1 for t in range(horizon+1))
    return distributions

def main():
    horizon=32
    edge=rat_coeffs(C(u),horizon+1)
    assert edge[:9]==[Q(1),Q(-1,2),Q(-1,2),Q(-1,2),Q(-1,6),Q(0),Q(1,27),Q(1,18),Q(11,486)]
    det=rat_coeffs((1+u)*C(u*u),horizon+1)
    geo=rat_coeffs(2/(2-u)*C(u/(2-u)),horizon+1)
    assert det==[edge[t//2] for t in range(horizon+1)]
    assert geo==[sum(Q(comb(t,n),2**t)*edge[n] for n in range(t+1)) for t in range(horizon+1)]
    assert det[:3]==[Q(1),Q(1),Q(-1,2)]
    assert geo[:3]==[Q(1),Q(1,4),Q(-1,8)]
    wait={1:Q(1,3),3:Q(2,3)}
    F=u/3+2*u**3/3
    occ=renewal_occupancy(wait,horizon)
    direct=[sum(occ[n][t]*edge[n] for n in range(horizon+1)) for t in range(horizon+1)]
    transformed=rat_coeffs((1-F)/(1-u)*C(F),horizon+1)
    assert direct==transformed
    clock_summaries=[]
    for name,f in [('deterministic_2',u*u),('geometric_half',u/(2-u))]:
        even=S.cancel(R0(f));odd=S.cancel(R1(f))
        assert even.subs(u,1)==S.Rational(3,5)
        assert odd.subs(u,1)==S.Rational(2,5)
        assert S.diff(even+odd,u).subs(u,1)==8
        assert S.diff(even,u).subs(u,1)/even.subs(u,1)==S.Rational(36,5)
        assert S.diff(odd,u).subs(u,1)/odd.subs(u,1)==S.Rational(46,5)
        clock_summaries.append({'clock':name,'transport_mark_one_probability':'2/5',
                               'mean_return_clock_duration':'8','even_mark_mean':'36/5','odd_mark_mean':'46/5'})
    det_odd_mark=rat_coeffs(R1(u*u),horizon+1)
    assert all(det_odd_mark[t]==0 for t in range(1,horizon+1,2))
    out={'status':'EXACT_CLOCK_INTERFACE_PASS','horizon':horizon,
         'source_edge_prefix':[str(x) for x in edge[:9]],
         'deterministic_response':[str(x) for x in det[:9]],
         'geometric_response':[str(x) for x in geo[:9]],
         'third_clock_independent_renewal_convolution_matches':True,
         'clock_summaries':clock_summaries,
         'deterministic_clock_has_only_even_durations_but_odd_transport_mark_mass':'2/5',
         'native_clock_selection':'UNKNOWN','BRC_world_reexecution':False,
         'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    Path(__file__).with_name('euler_clock_validation.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
