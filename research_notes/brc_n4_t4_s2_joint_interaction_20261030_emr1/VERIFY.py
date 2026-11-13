"""Exact BRC N=4 BU stage-four k-dependent terminal-decision verification.

All arithmetic uses fractions.Fraction; finite grids check examples and the
explicit universal algebraic formula, but cannot prove universality themselves.
"""
from fractions import Fraction as F
from itertools import product

q = {'AU':F(1,6), 'AV':F(1,3), 'BU':F(1,4), 'BV':F(1,4)}
r = {'AU':(F(9,10),F(11,10)), 'AV':(F(1,4),)*2,
     'BU':(F(1,5),F(9,5)), 'BV':(F(2),)*2}

def add(table,key,mass):
    table[key] = table.get(key,F(0))+mass

def source(law):
    raw={(s,j,k):q[s]/4*(r[s][j] if law=='P' else 1)
         for s in q for j,k in product(range(2),repeat=2)}
    assert len(raw)==16 and min(raw.values())>0 and sum(raw.values())==1
    return raw

def laws(u,v,d00,d01,d10,d11):
    # j=0 uses u and d00,d01; j=1 uses v and d10,d11.
    params={0:(u,(d00,d01)),1:(v,(d10,d11))}
    out={}
    for law in ('P','Q'):
        obs={}
        for (s,j,k),m in source(law).items():
            if s in ('AV','BV'):
                add(obs,'E',m)
            elif s=='AU':
                add(obs,'A',m)
            else:
                t,ds=params[j]
                add(obs,'B3',m*(1-t))
                add(obs,('B4','P',k),m*t*ds[k])
                add(obs,('B4','Q',k),m*t*(1-ds[k]))
        assert sum(obs.values())==1
        out[law]=obs
    return out['P'],out['Q']

def tv(p,q):
    return sum((abs(p.get(k,F(0))-q.get(k,F(0))) for k in p.keys()|q.keys()),F(0))/2

def push_without_k(m):
    y={}
    for key,val in m.items():
        if isinstance(key,tuple) and key[0]=='B4':
            key=key[:2]
        add(y,key,val)
    return y

def formula(u,v,d00,d01,d10,d11):
    return (2*abs(u-v)+sum(abs(v*d1-u*d0)+abs(v*(1-d1)-u*(1-d0))
             for d0,d1 in ((d00,d10),(d01,d11))))/40

def check(args):
    u,v,d00,d01,d10,d11=args
    p,qq=laws(*args)
    pred=formula(*args)
    assert p['E']==qq['E']==F(7,12)
    assert p['A']==qq['A']==F(1,6)
    # Independent atom-level signed-mass check; no TV simplification used here.
    assert p['B3']-qq['B3']==(u-v)/10
    for k,dd0,dd1 in [(0,d00,d10),(1,d01,d11)]:
        assert p['B4','P',k]-qq['B4','P',k]==(v*dd1-u*dd0)/20
        assert p['B4','Q',k]-qq['B4','Q',k]==(v*(1-dd1)-u*(1-dd0))/20
    assert tv(p,qq)==pred
    assert abs(u-v)/10 <= pred <= max(u,v)/10
    if u==v:
        assert pred==u*(abs(d10-d00)+abs(d11-d01))/20
        assert tv(push_without_k(p),push_without_k(qq))==u*abs((d10-d00)+(d11-d01))/20
    # The midpoint R is actually the pushforward of a C-preserving common decoder.
    mid={k:(p.get(k,F(0))+qq.get(k,F(0)))/2 for k in p.keys()|qq.keys()}
    assert sum(mid.values())==1
    assert tv(p,mid)==tv(qq,mid)==pred/2
    # Simulate exact S=(C,j) conditional kernel via source masses.
    for law,actual in (('P',p),('Q',qq)):
        common={}
        raw=source(law)
        for (s,j,k),m in raw.items():
            # Reconstruct from S, *discarding* actual k; integrate one fresh fair k.
            if s in ('AV','BV'):
                add(common,'E',m)
            elif s=='AU':
                add(common,'A',m)
            else:
                t,ds={0:(u,(d00,d01)),1:(v,(d10,d11))}[j]
                add(common,'B3',m*(1-t))
                for drawn in range(2):
                    add(common,('B4','P',drawn),m*t*ds[drawn]/2)
                    add(common,('B4','Q',drawn),m*t*(1-ds[drawn])/2)
        assert common==actual
    return pred

zero=F(0);one=F(1)
# Distinct new joint-only interaction witness: each one-coordinate observer blind.
witness=(one,one,one,zero,zero,one)
p,qq=laws(*witness)
assert check(witness)==F(1,10)
assert tv(push_without_k(p),push_without_k(qq))==0
assert (sum(v for k,v in p.items() if isinstance(k,tuple) and k[1]=='P')
        ==sum(v for k,v in qq.items() if isinstance(k,tuple) and k[1]=='P')==F(1,8))
assert {k:p[k]-qq[k] for k in [('B4','P',0),('B4','Q',0),('B4','P',1),('B4','Q',1)]} == {
    ('B4','P',0):-F(1,20),('B4','Q',0):F(1,20),
    ('B4','P',1):F(1,20),('B4','Q',1):-F(1,20)}
# For arbitrary fixed u,v the sharp interval endpoints are achieved.
for u,v in product([zero,F(1,4),F(1,2),F(3,4),one],repeat=2):
    assert check((u,v,zero,zero,zero,zero))==abs(u-v)/10
    assert check((u,v,zero,zero,one,one))==max(u,v)/10
# Whole finite 6D rational grid, including all boundary corners.
vals=(zero,F(1,2),one)
for args in product(vals,repeat=6):
    check(args)
# Distinct non-binary denominators and asymmetric k decisions.
vals2=(F(1,7),F(2,5),F(3,4))
for args in product(vals2,repeat=6):
    check(args)
print('PASS_BRC_N4_T4_K_DEPENDENT_JOINT_INTERACTION_20261030')
print('16 positive leaves per law; 729+729 six-parameter profiles; 25 endpoint-pair families; exact Fraction arithmetic')
print('interaction witness full_joint_TV=1/10, no_k_TV=0, C_common_decoder_minimax=1/20')
print('sharp all-real bounds: |u-v|/10 <= full_joint_TV <= max(u,v)/10 (analytic proof in PROOF.md)')
