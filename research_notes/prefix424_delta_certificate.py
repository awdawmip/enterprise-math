#!/usr/bin/env python3
"""PREFIX-424 delta: exact all-epsilon certificate. Requires PREFIX-423's pinned checker.
Usage: python prefix424_delta_certificate.py path/to/prefix423_exact_certificate.py
The dependency is in research_notes/PREFIX423_CODE_EVIDENCE.tar.br (GitHub commit 9a1ea3...).
"""
import runpy,sys
from pathlib import Path
from fractions import Fraction
src=Path(sys.argv[1] if len(sys.argv)>1 else Path(__file__).with_name('prefix423_exact_certificate.py'))
assert src.is_file(),f'Missing frozen predecessor: {src}'
d=runpy.run_path(str(src))  # includes predecessor's 1448 exact checks
Q=d['Q']; IV=d['IV']; model=d['model']; b=d['beta']
CHECKS=0

def check(v,op,bound,label):
    global CHECKS
    if op=='>': v.gt(Q(bound),label)
    else: v.lt(Q(bound),label)
    CHECKS+=1

def mixed(m):
    a=m['a']; w=m['invroot']
    brs=-(w/4+a*(1+a)*w*w*w/4)
    ars=12*brs; crs=28*brs; prs=123*brs/16; qrs=245*brs/16
    nrs=2*(m['Pr']*m['Ps']+m['P']*prs+m['Wr']*m['Ws']+m['W']*qrs)
    trs=(ars*m['P']+m['Ar']*m['Ps']+m['As']*m['Pr']+m['A']*prs
          +crs*m['W']+m['Br']*m['Ws']+m['Bs']*m['Wr']+m['B']*qrs)
    crs_=(ars*m['W']+m['Ar']*m['Ws']+m['As']*m['Wr']+m['A']*qrs
          -crs*m['P']-m['Br']*m['Ps']-m['Bs']*m['Pr']-m['B']*prs)
    lrs=(trs-m['Ls']*m['Nr']-m['L']*nrs-m['Lr']*m['Ns'])/m['N']
    mrs=(crs_-m['Ms']*m['Nr']-m['M']*nrs-m['Mr']*m['Ns'])/m['N']
    srs=nrs*b/(2*m['S'])-m['Rr']*m['Rs']/(4*m['S']*m['S']*m['S'])
    return (-4*brs+lrs*m['K']-m['Lr']*Q(Fraction(709,64))
            +mrs*m['S']+m['Mr']*m['Ss']+m['Ms']*m['Sr']+m['M']*srs)

eta_lo=d['eta_lo'];eta_hi=d['eta_hi'];n=d['NBOXES']
for j in range(n):
    e=IV.b(eta_lo+(eta_hi-eta_lo)*j/n,eta_lo+(eta_hi-eta_lo)*(j+1)/n)
    z=model(d['rbox'],d['sbox'],e)
    for name,v,op,k in [('Vss >7649',z['Vss'],'>',7649),('Vss <7832',z['Vss'],'<',7832),
                        ('Vse >691',z['Vse'],'>',691),('Vse <708',z['Vse'],'<',708),
                        ('Vsr >5',mixed(z),'>',5),('Vsr <6',mixed(z),'<',6)]:
        check(v,op,k,'PREFIX424 '+name)
for e,op in [(eta_lo,'<'),(eta_hi,'>')]:
    check(model(d['rbox'],d['sbox'],Q(e))['Vs'],op,0,'PREFIX424 uniform endpoint sign')
check(model(Q(1),Q(2),Q('0.01952966218269903976527'))['Vs'],'<',0,'eta0 left')
check(model(Q(1),Q(2),Q('0.01952966218269903976529'))['Vs'],'>',0,'eta0 right')
assert CHECKS==6*n+4
print('PREFIX424_EXTRA_INTEGER_CHECKS',CHECKS)
print('PREFIX424_TOTAL_INTEGER_CHECKS',d['CHECKS']+CHECKS)
print('PREFIX424_PHASE_BOUNDS', 'Vss:(7649,7832)', 'Vs_eta:(691,708)', 'Vs_r:(5,6)')
print('PREFIX424_ETA0_INTERVAL','0.01952966218269903976527','0.01952966218269903976529')
print('PREFIX424_DERIVATIVE_A', '-7838/691 < A_prime < -7654/708')
print('PREFIX424_DERIVATIVE_B', '7643/708 < B_prime < 7827/691')
print('PREFIX424_WIDTH', '(15298/708)*epsilon < W < (15664/691)*epsilon')
print('PASS_PREFIX424_TWO_PARAMETER_DELTA_EXACT_CERTIFICATE')
