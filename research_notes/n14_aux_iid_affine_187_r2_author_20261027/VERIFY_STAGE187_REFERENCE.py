#!/usr/bin/env python3
"""Stage187 external ternary IID exact reference checker; Python standard library only.
This is the source-level portable companion to the separately executed full verifier.
No native X6 theorem, formal admission or independent Driver review is asserted.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product

N = 14
P = (F(1, 8), F(1, 24), F(5, 6))
Q = (F(1, 12), F(1, 12), F(5, 6))
R, T = (5, 2, 0), (13, 6, 4)
K = F(30912926277555, 175004717024)
L = F(948381852216, 5468897407)
H = F(20011003723884904564897099291, 149794525046841680093773824)
A186 = F(880819177025099228444495, 2513951372772311530733568)
V186 = F(15842003227930467204041319427, 1448035990716851441702535168)
A187 = F(47564236941933996508186187, 135753377754634620902572032)
V187 = F(47526009692613945133124984819, 4344108088148307868882305024)
states = [(n,a,b) for n in range(15) for a in range(n+1) for b in range(n-a+1)]

def child(s,i):
    n,a,b=s
    return (n+1,a+(i==0),b+(i==1))

def bellman(k,l):
    @lru_cache(None)
    def visit(s):
        n,a,b=s
        ell=F(2**(a+b),3**a)
        opts={'P':k*ell,'Q':l}
        if n<N:opts['C']=1+sum(P[i]*visit(child(s,i))[0] for i in range(3))
        v=min(opts.values())
        return (v,tuple(act for act,cost in opts.items() if cost==v),
                tuple(cost-v for cost in opts.values() if cost>v))
    return visit

h=bellman(K,L)
assert len(states)==680 and h((0,0,0))[0]==H
ties={s:h(s)[1] for s in states if len(h(s)[1])>1}
gaps=[v for s in states for v in h(s)[2]]
assert ties=={R:('P','C'), T:('Q','C')}
assert len(gaps)==1238 and min(gaps)==F(464592386670727,29031182497677312)
policy={s:h(s)[1][0] for s in states}

def suffix(r,t):
    @lru_cache(None)
    def go(s):
        act=policy[s]
        def cont():
            vals=[go(child(s,i)) for i in range(3)]
            return (sum(P[i]*vals[i][0] for i in range(3)),
                    sum(Q[i]*vals[i][1] for i in range(3)),
                    1+sum(P[i]*vals[i][2] for i in range(3)),
                    1+sum(Q[i]*vals[i][3] for i in range(3)))
        if s==R:
            c=cont()
            return tuple(r*p+(1-r)*v for p,v in zip((F(0),F(1),F(0),F(0)),c))
        if s==T:
            c=cont()
            return tuple(t*p+(1-t)*v for p,v in zip((F(1),F(0),F(0),F(0)),c))
        if act=='P':return (F(0),F(1),F(0),F(0))
        if act=='Q':return (F(1),F(0),F(0),F(0))
        return cont()
    return go((0,0,0))

def ordered_dfs(rc,tc):
    """Independent unmerged integer-weight history traversal, denominator 24**14."""
    denom=24**N
    sums=[0,0,0,0]
    visits=0; first_R=first_T=rt_paths=0
    def walk(n,a,b,pwt,qwt,through_R):
        nonlocal visits,first_R,first_T,rt_paths
        visits+=1
        s=(n,a,b)
        if s==R:first_R+=1;through_R=True
        if s==T:
            first_T+=1
            if through_R:rt_paths+=1
        act=policy[s]
        if s==R:act='P' if rc else 'C'
        if s==T:act='Q' if tc else 'C'
        if act!='C':
            f=24**(N-n)
            if act=='Q':sums[0]+=pwt*f
            if act=='P':sums[1]+=qwt*f
            sums[2]+=n*pwt*f
            sums[3]+=n*qwt*f
        else:
            assert n<N
            walk(n+1,a+1,b,pwt*3,qwt*2,through_R)
            walk(n+1,a,b+1,pwt,qwt*2,through_R)
            walk(n+1,a,b,pwt*20,qwt*20,through_R)
    walk(0,0,0,1,1,False)
    return tuple(F(v,denom) for v in sums),visits,(first_R,first_T,rt_paths)

corners={p:suffix(F(p[0]),F(p[1])) for p in product((0,1),repeat=2)}
counts=[]
for key,expected in corners.items():
    v,n,hits=ordered_dfs(*key)
    assert v==expected,('ordered DFS mismatch',key)
    counts.append(n)
    print('CORNER',key,'NODES',n,'FIRST_HITS',hits,'OBSERVABLES',tuple(map(str,v)))
assert counts==[207250,196954,196750,186574]
B=corners[0,0]
Dr=tuple(corners[1,0][i]-B[i] for i in range(4))
Dt=tuple(corners[0,1][i]-B[i] for i in range(4))
C=tuple(corners[1,1][i]-B[i]-Dr[i]-Dt[i] for i in range(4))
assert C==(-F(625,18786186952704),F(625,20061226008576),
           F(625,2348273369088),F(625,1671768834048))

def rr(t):
    return F(29069040000)*t+F(1085119418920651),F(80000)*(F(4235)*t+F(158600461647))
def r_of(t):
    a,b=rr(t)
    return a/b
def alpha_closed(t):
    return (F(1382578638172183457)*t+F(47564235559355358336002730))/(
        F(855945643032576)*(F(4235)*t+F(158600461647)))
def time_gap_closed(t):
    return (F(1150048844006343543963931657)-F(464927064418088234390)*t)/(
        F(27390260577042432)*(F(4235)*t+F(158600461647)))
def param(t):
    r=r_of(t)
    return tuple(B[i]+r*Dr[i]+t*Dt[i]+r*t*C[i] for i in range(4))

# All expressions are rational of degree <=2 over the same positive linear
# denominator. Agreement after clearing denominators at three distinct points
# proves their polynomial identities, rather than relying on grid fitting.
for t in [F(0),F(1),F(1,2)]:
    eP,eQ,tP,tQ=param(t)
    assert eP==eQ==alpha_closed(t)
    assert tP-tQ==time_gap_closed(t)
    assert tP+K*eQ+L*eP==H
assert r_of(F(0))==F(1085119418920651,12688036931760000)
assert F(0)<r_of(F(0))<r_of(F(1))<F(1)
assert param(F(0))[0]==A186 and param(F(0))[2]==V186
assert param(F(1))[0]==A187 and param(F(1))[2]==V187
assert A187-A186==F(5947690894506310000401604043,7176849460674877056318920028290285568)
assert K+L==F(61261145548467,175004717024)
# Closed-form derivative of alpha(t) has a positive numerator
# 5947690894506310000401604043 and positive square denominator
# 285315214344192*(4235*t+158600461647)**2 for t in [0,1].
assert time_gap_closed(F(1))>0

K188=F(39993714743501421,226849611128761)
L188=F(39205434834768424,226849611128761)
H188=F(552023450050793309312530706424493,4142313307078339047903008391168)
h188=bellman(K188,L188)
ties188={s:h188(s)[1] for s in states if len(h188(s)[1])>1}
gaps188=[v for s in states for v in h188(s)[2]]
assert ties188=={R:('P','C'),(8,0,1):('Q','C')}
assert len(gaps188)==1238 and min(gaps188)==F(1858369546682908,55124455504288923)
assert h188((0,0,0))[0]==H188
o=param(F(1))
assert o[2]+K188*o[1]+L188*o[0]==H188
print('STAGE187_REFERENCE_EXACT_PASS; Stage188 dual only')
