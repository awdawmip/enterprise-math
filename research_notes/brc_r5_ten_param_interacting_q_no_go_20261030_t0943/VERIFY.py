#!/usr/bin/env python3
"""Exact R5 ten-parameter Q compensation audit; fractions only, no floating point.
Universal all-real conclusion is in RESEARCH.md, not inferred from these finite tests.
"""
from fractions import Fraction as F
from functools import reduce
from math import gcd
from itertools import product

lam = F(1,75)
eta = F(1,1000)
# Each tuple: label, decision time, P numerator / 360, Q numerator / 360, parent
spec = [
    ('A',1,120,240,None), ('B',1,240,120,None),
    ('A0',2,60,180,'A'), ('A1',2,60,60,'A'),
    ('B0',2,180,60,'B'), ('B1',2,60,60,'B'),
    ('A00',3,30,108,'A0'), ('A01',3,30,72,'A0'),
    ('A10',3,30,45,'A1'), ('A11',3,30,15,'A1'),
    ('B00',3,90,36,'B0'), ('B01',3,90,24,'B0'),
    ('B10',3,20,40,'B1'), ('B11',3,40,20,'B1')]
names=[a[0] for a in spec]
node={name: {'t':t,'p':F(p,360),'q':F(q,360),'parent':parent,'lr':F(p,q)} for name,t,p,q,parent in spec}
assert sum(node[n]['p'] for n in ['A','B'])==1 and sum(node[n]['q'] for n in ['A','B'])==1
for n in names[:6]:
    kids=[a for a in names if node[a]['parent']==n]
    if kids:
        assert sum(node[k]['p'] for k in kids)==node[n]['p']
        assert sum(node[k]['q'] for k in kids)==node[n]['q']
for n in names: assert node[n]['p']>0 and node[n]['q']>0
keys=[]
for n in names:
    k=(node[n]['t'],node[n]['lr'])
    if k not in keys: keys.append(k)
assert len(keys)==12
assert keys.count((2,F(1)))==1 and keys.count((3,F(2)))==1
assert node['A1']['lr']==node['B1']['lr']==1
assert node['A11']['lr']==node['B11']['lr']==2
key_ix={n:keys.index((node[n]['t'],node[n]['lr'])) for n in names}
idx={n:i for i,n in enumerate(names)}
leaves=[n for n in names if node[n]['t']==3]

# Each mask encodes 14 FULL or 12 LR stop/continue decisions.
def stopped(mask,name,lr):
    return bool((mask >> (key_ix[name] if lr else idx[name])) & 1)

def score(mask,lr,rewards):
    total=F(0)
    continued={}
    for n in names:
        parent=node[n]['parent']
        reachable=parent is None or continued[parent]
        st=stopped(mask,n,lr) if reachable else False
        continued[n]=reachable and not st
        if st: total+=rewards[n]
    return total

def observation(mask,lr,coef):
    E_P=E_Q=T_P=T_Q=F(0)
    for leaf in leaves:
        chain=[leaf,node[leaf]['parent'],node[node[leaf]['parent']]['parent']][::-1]
        stopping=next((n for n in chain if stopped(mask,n,lr)),None)
        if stopping is None:
            t=4; r=node[leaf]['lr']; corr=F(0)
        else:
            t=node[stopping]['t'];r=node[stopping]['lr'];corr=coef.get(stopping,F(0))
        p=F(1,5)+F(t,20)+F(t+1,100)/r
        q=F(2,5)-F(t,30)+F(t+2,200)*r+eta*corr
        assert 0<p<1 and 0<q<1
        P=node[leaf]['p'];Q=node[leaf]['q']
        E_P+=P*p;E_Q+=Q*q;T_P+=P*t;T_Q+=Q*t
    return E_P,E_Q,T_P,T_Q

def setup(u,v,zA,zB,priv):
    c={'A1':F(u),'B1':F(v),'A11':F(1),'B11':F(-1),'A10':F(zA),'B10':F(zB)}
    c.update(dict(zip(['A0','A00','A01','B0','B00','B01'],map(F,priv))))
    for n in names:
        x=node[n];q0=F(2,5)-F(x['t'],30)+F(x['t']+2,200)*x['lr']
        p0=F(1,5)+F(x['t'],20)+F(x['t']+1,100)/x['lr']
        assert 0<q0+eta*c.get(n,F(0))<1 and 0<p0<1
    return c

def compact_formula(sign,coef):
    r={n:sign*node[n]['q']*coef.get(n,F(0))-lam*(4-node[n]['t'])*(node[n]['p']+node[n]['q']) for n in names}
    CA=max(F(0),r['A0'],max(F(0),r['A00'])+max(F(0),r['A01']))
    CB=max(F(0),r['B0'],max(F(0),r['B00'])+max(F(0),r['B01']))
    a2,b2,a3,b3=map(r.__getitem__,('A1','B1','A11','B11'))
    alpha,beta=max(F(0),r['A10']),max(F(0),r['B10'])
    full=CA+CB+max(F(0),a2,alpha+max(F(0),a3))+max(F(0),b2,beta+max(F(0),b3))
    lr=max(-3*lam*(2-x-y)+x*CA+y*CB+max(F(0),x*a2+y*b2,x*alpha+y*beta+max(F(0),x*a3+y*b3)) for x,y in product((0,1),repeat=2))
    return full,lr,CA,CB,alpha,beta

def check(case,coef):
    print('CASE',case)
    gaps=[]
    for s in (1,-1):
        r={n:s*node[n]['q']*coef.get(n,F(0))-lam*(4-node[n]['t'])*(node[n]['p']+node[n]['q']) for n in names}
        f=max((score(m,False,r),m) for m in range(1<<14))
        l=max((score(m,True,r),m) for m in range(1<<12))
        f0,l0,CA,CB,alpha,beta=compact_formula(s,coef)
        assert (f[0],l[0])==(f0,l0)
        assert f0-l0>=0
        gaps.append(f0-l0)
        print(' sign=%+d FULL=%s LR=%s GAP=%s best_FULL_mask=%s best_LR_mask=%s CA=%s CB=%s alpha=%s beta=%s'%(
            s,f0,l0,f0-l0,f[1],l[1],CA,CB,alpha,beta))
    assert max(gaps)>=F(1,25)
    s=(1,-1)[gaps[1]>gaps[0]]
    r={n:s*node[n]['q']*coef.get(n,F(0))-lam*(4-node[n]['t'])*(node[n]['p']+node[n]['q']) for n in names}
    f=max((score(m,False,r),m) for m in range(1<<14))
    l=max(score(m,True,r) for m in range(1<<12))
    O=observation(f[1],False,coef)
    E_P,E_Q,T_P,T_Q=O
    S=E_Q-F(41,100)-T_P/200+T_Q/30
    D=8-T_P-T_Q
    assert s*S/eta-lam*D==f[0]
    print(' WIN_SIGN=%+d FULL_O=%s S=%s D=%s SEPARATION=%s'%(s,O,S,D,eta*(f[0]-l)))
    return gaps

if __name__=='__main__':
    cases=[
        ('all-zero',setup(0,0,0,0,[0]*6)),
        ('signed-mixed',setup(F(1,2),F(1,10),1,-1,[1,-1,1,-1,1,-1])),
        ('large-interacting',setup(F(-1,5),F(2,5),F(5,2),F(7,3),[-1,2,-1,2,-1,1])),
        ('opposite',setup(F(-1,3),F(-1,6),F(-9,4),F(5,3),[1,1,-1,-1,-1,1])),
    ]
    for title,c in cases: check(title,c)
    # The all-real proof is a three-region exact inequality on a,b,alpha,beta,A,B (RESEARCH.md).
    # Here, an independent rational parameter lattice regression checks the formula for 2,401 cases.
    one=F(1,25)
    count=0
    grid=[F(-2),F(-1),F(-1,2),F(0),F(1,2),F(1),F(2)]
    for a,b,zA,zB in product(grid,repeat=4):
        u=6*(a+F(2,225));v=6*(b+F(2,225))
        c=setup(u,v,zA,zB,[0]*6)
        gp=compact_formula(1,c)[0]-compact_formula(1,c)[1]
        gm=compact_formula(-1,c)[0]-compact_formula(-1,c)[1]
        assert max(gp,gm)>=one
        count+=1
    print('LATTICE_VALIDATED',count)
    print('PASS_EXACT_R5_TEN_PARAMETER_INTERACTING_Q_NO_GO')
