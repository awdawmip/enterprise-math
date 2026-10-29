#!/usr/bin/env python3
"""Original weighted K(K+16 theta K) tail-transfer certificate.

Requires same-directory p^3 full-original companion checker, preserving
all coefficient and theta observers. External arithmetic; not native H0/B0.
"""
from d25_legendre_p3_frobenius_fullcompanion_guard_20261029 import companion_ports, primes_below

samples=[p for p in primes_below(200) if p>=11 and p%8 in (5,7)]+[229,373]
for p in samples:
    a=companion_ports(p)
    M=p**3
    K=a['cutoff']; T=a['tail']
    D=(a['theta']-a['tail_theta'])%M
    E=a['tail_theta']
    assert T%(p*p)==0 and E%(p*p)==0, (p,T,E)
    wc=K*(K+16*D)%M
    wf=(K+T)*(K+T+16*(D+E))%M
    predicted=(2*K*T+16*(T*D+K*E))%M
    assert (wf-wc)%M==predicted,(p,wf,wc,predicted)
    if p in (13,23,37,373):
        print('WEIGHTED_CUTOFF_CERT',p,'p3',M,
              'Kcut',K,'tail',T,'theta_cut',D,'theta_tail',E,
              'weighted_cut',wc,'weighted_full',wf,'shift',(wf-wc)%M,
              'theta_cut_modp',D%p)
print('PASS_WEIGHTED_CUTOFF_TRANSPORT',len(samples),'p=5,7 mod8 >=11')
