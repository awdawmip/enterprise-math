#!/usr/bin/env python3
"""Exact finite-atom check for the BRC N4 G0 stopped-filtration result.

No random sampling and no floating-point arithmetic.  The universal
stopped-sigma-algebra and minimax steps are proved in PROOF.md.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product

SOURCES = ('AU', 'AV', 'BU', 'BV')
q = {'AU': F(1,6), 'AV': F(1,3), 'BU': F(1,4), 'BV': F(1,4)}
ratio = {'AU': (F(9,10),F(11,10)),
         'AV': (F(1,4),F(1,4)),
         'BU': (F(1,5),F(9,5)),
         'BV': (F(2),F(2))}


def stop_atom(s,j,k):
    return (s,j) if s in ('AU','BU') else (s,None)


def coarse_atom(s,j,k):
    return {'AU':'AU_T3_P', 'BU':'BU_T3_Q',
            'AV':'EARLY_T2_Q', 'BV':'EARLY_T2_Q'}[s]


def tv(left,right):
    keys=set(left)|set(right)
    return sum((abs(left.get(key,F(0))-right.get(key,F(0)))
                for key in keys),F(0))/2

raw={'P':{},'Q':{}}
for s,j,k in product(SOURCES,range(2),range(2)):
    raw['Q'][(s,j,k)]=q[s]/4
    raw['P'][(s,j,k)]=q[s]*ratio[s][j]/4
for L in ('P','Q'):
    assert len(raw[L])==16 and all(x>0 for x in raw[L].values())
    assert sum(raw[L].values())==1

stopped={}; coarse={}
for L in ('P','Q'):
    f=defaultdict(lambda:F(0)); g=defaultdict(lambda:F(0))
    for (s,j,k),mass in raw[L].items():
        f[stop_atom(s,j,k)]+=mass
        g[coarse_atom(s,j,k)]+=mass
    stopped[L]=dict(f); coarse[L]=dict(g)

assert len(stopped['P'])==len(stopped['Q'])==6
assert coarse['P']==coarse['Q']=={
    'AU_T3_P': F(1,6), 'BU_T3_Q': F(1,4),
    'EARLY_T2_Q': F(7,12)}
assert stopped['P']=={('AU',0):F(3,40),('AU',1):F(11,120),
    ('BU',0):F(1,40),('BU',1):F(9,40),
    ('AV',None):F(1,12),('BV',None):F(1,2)}
assert stopped['Q']=={('AU',0):F(1,12),('AU',1):F(1,12),
    ('BU',0):F(1,8),('BU',1):F(1,8),
    ('AV',None):F(1,3),('BV',None):F(1,4)}
assert tv(stopped['P'],stopped['Q'])==F(43,120)

# Equal coarse marginals make the full midpoint law a common O'-decoder.
common_mid={x:(stopped['P'][x]+stopped['Q'][x])/2
            for x in stopped['P']}
decoder={}
for x,mass in common_mid.items():
    s,j=x
    coarse_key=coarse_atom(s,j,0)
    decoder[(coarse_key,x)]=mass/coarse['P'][coarse_key]
for z,m in coarse['P'].items():
    assert sum((p for (key,x),p in decoder.items() if key==z),F(0))==1
for L in ('P','Q'):
    sim={x:coarse[L][coarse_atom(x[0],x[1],0)]*
         decoder[(coarse_atom(x[0],x[1],0),x)] for x in common_mid}
    assert sim==common_mid
    assert tv(stopped[L],sim)==F(43,240)
assert tv(coarse['P'],coarse['Q'])==0

# Stopping-time information: G0 stops at T=2 on AV/BV and T=3 on AU/BU.
# The six disjoint stop atoms are precisely F_T atoms; no BU atom splits by k.
for s in SOURCES:
    for j in range(2):
        for k in range(2):
            if s in ('AU','BU'):
                assert stop_atom(s,j,k)==stop_atom(s,j,1-k)
# All BU leaf-siblings have equal P and Q masses, hence fair k conditional on stop atom.
for L in ('P','Q'):
    for j in (0,1):
        assert raw[L][('BU',j,0)]==raw[L][('BU',j,1)]
    assert sum((mass for (s,j,k),mass in raw[L].items() if s=='BU'),F(0))==F(1,4)
    # Every F_T-deterministic predictor of k on BU has the same 1/8 error.
    for guess0,guess1 in product((0,1),repeat=2):
        wrong=sum((mass for (s,j,k),mass in raw[L].items()
                   if s=='BU' and k!=(guess0 if j==0 else guess1)),F(0))
        assert wrong==F(1,8)

print('P_STOP=',sorted(stopped['P'].items(), key=str))
print('Q_STOP=',sorted(stopped['Q'].items(), key=str))
print('COMMON_COARSE=', sorted(coarse['P'].items()))
print('TV_FULL_STOP_PQ=',tv(stopped['P'],stopped['Q']))
print('OPT_COMMON_DECODER_TV_P=OPT_COMMON_DECODER_TV_Q=',F(43,240))
print('PATHWISE_BU_K_ERROR_P=PATHWISE_BU_K_ERROR_Q=',F(1,8))
print('PASS_BRC_N4_G0_STOP_SIGMA_SIX_ATOM_SHARP_COMMON_DECODER_20261030')
