#!/usr/bin/env python3
"""Exact-rational regression for a source-sensitive LR diamond (Python >=3.10).

Universal real-domain claims are proved in RESEARCH.md, not by finite sampling.
"""
from fractions import Fraction as F
from itertools import product
from random import Random

S = (F(1,2), F(1), F(3,2), F(5,2))
R = F(3,2)
SRC = ('A','B')
a = {'A':F(1,4),'B':F(1,4)}
mu = {'A':(F(7,50),F(11,75),F(1,2),F(16,75)),
      'B':(F(17,200),F(23,150),F(3,5),F(97,600))}
nu = {('A','L'):(F(1,2),F(1,6),F(1,4),F(1,12)),
      ('B','L'):(F(5,12),F(1,3),F(1,6),F(1,12)),
      ('A','R'):(F(17,100),F(23,75),F(1,5),F(97,300)),
      ('B','R'):(F(31,120),F(5,18),F(1,15),F(143,360))}
eta = {'A':(F(1,8),F(1,4),F(3,8),F(1,4)),
       'B':(F(5,32),F(3,16),F(13,32),F(1,4))}
V = {i:a[i]*mu[i][1]*nu[i,'L'][2] for i in SRC}
W = {i:a[i]*mu[i][2]*nu[i,'R'][2] for i in SRC}
CL=sum(V.values()); CR=sum(W.values())
A_tail=tuple(sum(V[i]*eta[i][k] for i in SRC) for k in range(4))
B_tail=tuple(sum(W[i]*eta[i][k] for i in SRC) for k in range(4))
CSTAR=(F(2),F(2),F(0),F(9,64))

def check_kernels():
    for i in SRC:
        for d, parent in ((mu[i],R),(eta[i],R),(nu[i,'L'],S[1]),(nu[i,'R'],S[2])):
            assert all(x>0 for x in d)
            assert sum(d)==1
            assert sum(s*x for s,x in zip(S,d))==parent
    assert V=={'A':F(11,1200),'B':F(23,3600)}
    assert W=={'A':F(1,40),'B':F(1,100)}
    assert CL==F(7,450) and CR==F(7,200)
    assert V['A']*W['B']-V['B']*W['A']==-F(49,720000)
    assert A_tail==(F(247,115200),F(67,19200),F(139,23040),F(7,1800))
    assert B_tail==(F(3,640),F(13,1600),F(43,3200),F(7,800))
    print('KERNELS_NORMALIZED',len(S)*2*4,'CL',CL,'CR',CR)
    print('MERGED_TAIL_COEFFICIENTS_A',A_tail)
    print('MERGED_TAIL_COEFFICIENTS_B',B_tail)

def terminal_weights_lr(U,L,H,gamma):
    """Here H is the right-path flow; gamma is common merged continuation."""
    assert 0<=U<=1 and 0<=L<=U and 0<=H<=U and 0<=gamma<=1
    out={}
    def add(t,s,z):out[t,s]=out.get((t,s),F(0))+z
    add(1,S[0],F(1,2));add(1,R,(1-U)/2)
    for k,s in enumerate(S):
        q=sum(a[i]*mu[i][k] for i in SRC)
        add(2,s, (U if k in (0,3) else U-L if k==1 else U-H)*q)
    h=CL*L+CR*H
    for k,s in enumerate(S):
        if k==2:add(3,s,(1-gamma)*h)
        else:
            zL=sum(a[i]*mu[i][1]*nu[i,'L'][k] for i in SRC)
            zR=sum(a[i]*mu[i][2]*nu[i,'R'][k] for i in SRC)
            add(3,s,L*zL+H*zR)
        add(4,s,gamma*(A_tail[k]*L+B_tail[k]*H))
    return out

def times(weights):
    tq=sum(t*z for (t,s),z in weights.items())
    tp=sum(t*s*z for (t,s),z in weights.items())
    return tp,tq

def observer(weights, decl):
    """decl is cell-indexed probability of declaring P."""
    q=sum(weights[t,s]*decl[t,s] for t,s in weights)
    ps=sum(s*weights[t,s]*decl[t,s] for t,s in weights)
    tp,tq=times(weights)
    return (1-ps,q,tp,tq)

def greedy(H,q,reverse=False):
    result={s:F(0) for s in S}
    rem=q
    for s in reversed(S) if reverse else S:
        z=min(H[s],rem)
        result[s]=z
        rem-=z
    assert rem==0
    return result

def fixed_q_range(H,q):
    assert F(0)<=q<=sum(H.values())
    low=greedy(H,q)
    high=greedy(H,q,True)
    return sum(s*low[s] for s in S),sum(s*high[s] for s in S)

def fcost(t,s,c):
    c1,c2,c3,c4=c
    return t*(c3*s+c4)+min(F(0),c2-c1*s)

def exact_bellman(c,tail=eta):
    f={(t,s):fcost(t,s,c) for t in (1,2,3,4) for s in S}
    forced=F(1,2)*f[1,S[0]]
    full=forced
    source_diagnostics={}
    for i in SRC:
        stop3=f[3,R]
        tail3=sum(tail[i][k]*f[4,s] for k,s in enumerate(S))
        prior={}
        continue_root=F(0)
        for k,s in enumerate(S):
            if k not in (1,2):
                node=f[2,s]
            else:
                path='L' if k==1 else 'R'
                cost=sum(nu[i,path][j]*(min(stop3,tail3) if j==2 else f[3,ss]) for j,ss in enumerate(S))
                prior[path]=(f[2,s],cost)
                node=min(f[2,s],cost)
            continue_root+=mu[i][k]*node
        full+=a[i]*min(f[1,R],continue_root)
        source_diagnostics[i]=(stop3,tail3,prior,f[1,R],continue_root)
    values={}
    for alpha0,alphaL,alphaR,gamma in product((0,1),repeat=4):
        U=F(alpha0);L=U*alphaL;H=U*alphaR
        weights=terminal_weights_lr(U,L,H,F(gamma)) if tail is eta else terminal_weights_custom_tail(U,L,H,F(gamma),tail)
        value=sum(z*f[t,s] for (t,s),z in weights.items())
        values[alpha0,alphaL,alphaR,gamma]=value
    bestval=min(values.values());best=tuple(k for k,z in values.items() if z==bestval)
    assert full<=bestval
    return c[0]+full,c[0]+bestval,best,source_diagnostics,values

def terminal_weights_custom_tail(U,L,H,gamma,tail):
    original=terminal_weights_lr(U,L,H,F(0))
    h=CL*L+CR*H
    original[3,R]-=gamma*h
    for k,s in enumerate(S):
        original[4,s]+=gamma*sum((V[i]*L+W[i]*H)*tail[i][k] for i in SRC)
    return original

def full_opt_weights():
    """Verified policy: root/left/right continue; source A stops at merge, B continues."""
    out={}
    def add(t,s,z):out[t,s]=out.get((t,s),F(0))+z
    add(1,S[0],F(1,2))
    for i in SRC:
        for k,s in enumerate(S):
            if k not in (1,2):add(2,s,a[i]*mu[i][k])
            else:
                path='L' if k==1 else 'R'
                for j,ss in enumerate(S):
                    z=a[i]*mu[i][k]*nu[i,path][j]
                    if j!=2 or i=='A':add(3,ss,z)
                    else:
                        for kk,ss4 in enumerate(S):add(4,ss4,z*eta[i][kk])
    return out

def check_support():
    full,lr,best,diag,all_lr=exact_bellman(CSTAR)
    assert full==F(370793,230400)
    assert lr==F(92713,57600)
    assert lr-full==F(59,230400)
    assert best==((1,1,1,0),)
    assert diag['A'][1]-diag['A'][0]==F(1,64)
    assert diag['B'][1]-diag['B'][0]==-F(1,64)
    for i in SRC:
        assert diag[i][4]<diag[i][3]
        for stop,cont in diag[i][2].values():assert cont<stop
    assert sum(V.values())+sum(W.values())==F(91,1800)
    assert (V['A']+W['A']-(V['B']+W['B']))/F(64)==F(1,3600)
    assert (V['B']+W['B'])/F(64)==F(59,230400)
    fW=full_opt_weights()
    lW=terminal_weights_lr(F(1),F(1),F(1),F(0))
    assert sum(fW.values())==sum(lW.values())==1
    assert sum(s*z for (_,s),z in fW.items())==sum(s*z for (_,s),z in lW.items())==1
    decF={k:F(1) if k[1]>1 else F(0) for k in fW}
    decL={k:F(1) if k[1]>1 else F(0) for k in lW}
    oFull=observer(fW,decF);oLR=observer(lW,decL)
    assert oFull==(F(98731,230400),F(627,2560),F(5429,2400),F(6719,3600))
    assert oLR==(F(509,1200),F(451,1800),F(179,80),F(37,20))
    assert sum(CSTAR[k]*oFull[k] for k in range(4))==full
    assert sum(CSTAR[k]*oLR[k] for k in range(4))==lr
    norm=sum(abs(x) for x in CSTAR)
    assert (lr-full)/norm==F(59,954000)
    blind={'A':eta['A'],'B':eta['A']}
    bf,bl,_,_,_=exact_bellman(CSTAR,tail=blind)
    assert bf==bl==lr
    print('SIGNED_TARGET',CSTAR)
    print('FULL_MIN',full,'LR_MIN',lr,'GAP',lr-full,'LR_BEST',best)
    print('FULL_OBSERVER',oFull,'LR_OBSERVER',oLR)
    print('L_INFINITY_DISTANCE_LOWER_BOUND',F(59,954000))
    print('BLIND_TAIL_SAME_TARGET_GAP',bl-bf)
    print('LR_DETERMINISTIC_POLICIES',len(all_lr))
    return full,lr

def random_exact_regression(n=600):
    rng=Random(101029)
    for _ in range(n):
        ratios=[F(rng.randint(0,16),16) for _ in range(4)]
        U,al,ar,g=ratios
        L=U*al;H=U*ar
        wt=terminal_weights_lr(U,L,H,g)
        assert sum(wt.values())==1
        assert sum(s*v for (t,s),v in wt.items())==1
        tp,tq=times(wt)
        M=g*(CL*L+CR*H)
        assert tq==1+U/2+F(3,40)*L+F(11,40)*H+M
        assert tp==1+F(3,4)*U+F(3,40)*L+F(33,80)*H+R*M
        assert L==-F(80,3)*(tp-R*tq+F(1,2))
        recoveredM=tq-1-U/2-F(3,40)*L-F(11,40)*H
        assert recoveredM==M
        declaration={(t,s):F(rng.randint(0,16),16) for t,s in wt}
        p,q,_,_=observer(wt,declaration)
        totals={s:sum(wt.get((t,s),F(0)) for t in (1,2,3,4)) for s in S}
        lo,hi=fixed_q_range(totals,q)
        assert lo<=1-p<=hi
        if lo<hi:
            t=((1-p)-lo)/(hi-lo)
            low=greedy(totals,q)
            high=greedy(totals,q,reverse=True)
            m={s:(1-t)*low[s]+t*high[s] for s in S}
        else:m=greedy(totals,q)
        assert all(0<=m[s]<=totals[s] for s in S)
        assert sum(m.values())==q
        assert sum(s*m[s] for s in S)==1-p
    rng=Random(777)
    for _ in range(120):
        c=tuple(F(rng.randint(-9,9)) for j in range(4))
        if not any(c):continue
        fa,lb,*_=exact_bellman(c)
        assert fa<=lb
    print('EXACT_FLOW_AND_GREEDY_RECONSTRUCTION_CASES',n)
    print('EXACT_SIGNED_DIRECTION_REGRESSION_CASES',120)

if __name__=='__main__':
    check_kernels()
    check_support()
    random_exact_regression()
    print('PASS_EXACT_R5_SOURCE_SENSITIVE_TAIL_TWO_VARIABLE_FEASIBILITY')