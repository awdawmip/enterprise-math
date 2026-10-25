"""Independently constructed N14 Stage124 literal ordered-prefix verifier.
Integer-weight P and Q measures on every reached ordered word; Fraction only for
Bellman choices and the reported exact moment fractions.
"""
from fractions import Fraction as F
from collections import defaultdict

N=14
K=F(1245231873,1658336)
L=F(36440256,51823)
A=(9,3,0)
T=(14,7,4)
P_INT=(3,1,20)
Q_INT=(1,1,10)
P24=(F(3,24),F(1,24),F(20,24))
H={}
POL={}
def child(s,j):
    n,a,b=s
    return (n+1,a+(j==0),b+(j==1))
for n in range(N,-1,-1):
    for a in range(n+1):
        for b in range(n+1-a):
            s=(n,a,b)
            opts=[K*F(2**(a+b),3**a),L]
            if n<N:
                opts.append(F(1)+sum(P24[j]*H[child(s,j)] for j in range(3)))
            H[s]=min(opts)
            POL[s]=opts.index(H[s])
assert H[(0,0,0)]==F(5878829162353591081475135,11355563791072559628288)
DEN_P=24**N
DEN_Q=12**N

def enumerate_word(y,z):
    hits=defaultdict(lambda:[0,0,0])
    total=[0,0,0,0]
    visited=0
    stop_hist=0
    def visit(state,pw,qw):
        nonlocal visited,stop_hist
        visited+=1
        n=state[0]
        if state in (A,T):
            hh=hits[state]
            hh[0]+=1
            hh[1]+=pw*24**(N-n)
            hh[2]+=qw*12**(N-n)
        if state==A:
            act=0 if y else 2
        elif state==T:
            act=0 if z else 1
        else:
            act=POL[state]
        if act!=2:
            stop_hist+=1
            mp=pw*24**(N-n)
            mq=qw*12**(N-n)
            if act==1:total[0]+=mp # P -> Q
            else:total[1]+=mq # Q -> P
            total[2]+=n*mp
            total[3]+=n*mq
            return
        for j in range(3):
            visit(child(state,j),pw*P_INT[j],qw*Q_INT[j])
    visit((0,0,0),1,1)
    obs=(F(total[0],DEN_P),F(total[1],DEN_Q),F(total[2],DEN_P),F(total[3],DEN_Q))
    return obs,hits,visited,stop_hist

expected={
    "00":(F(608919703452600011,1752976676930715648),F(55715889515225,160489808068608),F(2798007941169380921,219122084616339456),F(161747615623729,13374150672384)),
}
for y,z in ((0,0),(0,1),(1,0),(1,1)):
    obs,hits,visited,stops=enumerate_word(y,z)
    # Exact integer-weight ordered words, no count-state moment recursion.
    print('corner',y,z,'visited',visited,'stopped',stops,'obs',obs)
    print('hitsA',hits[A][0],F(hits[A][1],DEN_P),F(hits[A][2],DEN_Q))
    print('hitsT',hits[T][0],F(hits[T][1],DEN_P),F(hits[T][2],DEN_Q))
    assert hits[A][0]==84
    assert F(hits[A][1],DEN_P)==F(109375,1990656)
    assert F(hits[A][2],DEN_Q)==F(109375,6718464)
    base=expected['00']
    da=(F(-1921609375,7925422620672),F(259765625,835884417024),
        F(-20758609375,330225942528),F(-1476453125,69657034752))
    dt=(F(-165875,25048249270272),F(165875,26748301344768),F(0),F(0))
    assert obs==tuple(base[i]+y*da[i]+z*dt[i] for i in range(4))
    assert hits[T][0]==7962
    assert F(hits[T][1],DEN_P)==F(165875,25048249270272)
    assert F(hits[T][2],DEN_Q)==F(165875,26748301344768)
    assert visited==(815542 if y==0 else 810502)
    assert stops==(543695 if y==0 else 540335)
    assert sum((obs[0],F(1)-obs[0]),F(0))==1
    assert sum((obs[1],F(1)-obs[1]),F(0))==1
print('PASS literal-ordered exact integer DFS Stage124')
