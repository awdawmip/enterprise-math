#!/usr/bin/env python3
"""Second author-side method: ordered-history first reach, absorbing backward DP,
randomization corner interpolation, independently minimized Bellman recursion.
Only the stop-set definition is shared with the first checker; this is not an
independent external review.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import factorial
from pathlib import Path
import runpy
m=runpy.run_path(str(Path(__file__).with_name('verify_n14_fiftyfirst.py')))
P,Q,N,A,B,S,AL,V,K,G=(m[z] for z in ('P','Q','N','A','B','S','AL','V','K','G'))
act,child=(m[z] for z in ('act','child'))
H=F(3335641,20889600000000)
ETA=F(8490125,310422953206480896)

def enumerate_target(st):
    total=alive=0; pa=qa=F()
    for word in product(range(3),repeat=st[0]):
        if word.count(0)!=st[1] or word.count(1)!=st[2]:
            continue
        total+=1
        current=(0,0,0); p=q=F(1)
        for sym in word:
            if act(current)!='C':
                break
            p*=P[sym];q*=Q[sym]
            current=child(current,sym)
        else:
            assert current==st
            alive+=1;pa+=p;qa+=q
    return total,alive,pa,qa

def absorbing_backward(u,s):
    @lru_cache(None)
    def recur(st):
        if st==A:
            qstop=u;pstop=F()
        elif st==B:
            qstop=s;pstop=F()
        else:
            a=act(st)
            if a=='P':return F(),F(1),F(),F()
            if a=='Q':return F(1),F(),F(),F()
            qstop=pstop=F()
        assert st[0]<N
        desc=[recur(child(st,i)) for i in range(3)]
        c=(sum((P[i]*desc[i][0] for i in range(3)),F()),
           sum((Q[i]*desc[i][1] for i in range(3)),F()),
           F(1)+sum((P[i]*desc[i][2] for i in range(3)),F()),
           F(1)+sum((Q[i]*desc[i][3] for i in range(3)),F()))
        # Random immediate Q. Under P, error 1; under Q, error 0.
        return (qstop+(1-qstop)*c[0],
                (1-qstop)*c[1],
                (1-qstop)*c[2],
                (1-qstop)*c[3])
    return recur((0,0,0))

def independently_minimize(k):
    lp=F(72)+F(8,9)*k;lq=k
    @lru_cache(None)
    def d(st):
        n,a,b=st
        opts={'P':lq*F(2**(a+b),3**a),'Q':lp}
        if n<N:opts['C']=F(1)+sum((P[i]*d(child(st,i)) for i in range(3)),F())
        return min(opts.values())
    ties=[];strict=0
    for n in range(N+1):
        for a in range(n+1):
            for b in range(n-a+1):
                st=(n,a,b);opts={'P':lq*F(2**(a+b),3**a),'Q':lp}
                if n<N:opts['C']=F(1)+sum((P[i]*d(child(st,i)) for i in range(3)),F())
                best=min(opts.values());zeros=[mode for mode,v in opts.items() if v==best]
                if len(zeros)>1:ties.append((st,zeros))
                strict+=len(opts)-len(zeros)
    return d((0,0,0)),ties,strict,d.cache_info().currsize

def check():
    total,live,pa,qa=enumerate_target(A)
    assert (total,live,pa,qa)==(3150,1565,F(39125,48922361856),F(39125,15479341056))
    tb,lb,pb,qb=enumerate_target(B)
    assert (tb,lb,pb,qb)==(12,12,F(48828125,725594112),F(48828125,362797056))
    value,ties,strict,states=independently_minimize(K)
    assert states==680 and strict==1238
    assert len(ties)==2 and {t[0] for t in ties}=={A,B}
    assert value==V+G*AL
    corner={(u,s):absorbing_backward(F(u),F(s)) for u in (0,1) for s in (0,1)}
    assert all(corner[1,1][i]-corner[1,0][i]-corner[0,1][i]+corner[0,0][i]==0 for i in range(4))
    for u in [F(),F(1,4),F(1,2),F(3,4),F(1)]:
        s=S-H*u
        exact=absorbing_backward(u,s)
        interp=tuple(corner[0,0][j]+u*(corner[1,0][j]-corner[0,0][j])+s*(corner[0,1][j]-corner[0,0][j]) for j in range(4))
        assert exact==interp
        assert exact[0]==exact[1]==AL+ETA*u
        assert exact[2]==V-G*ETA*u and exact[2]>exact[3]
    assert absorbing_backward(F(1),S-H)[:3]==(
      F(5171825736480880397,14900301753911083008),
      F(5171825736480880397,14900301753911083008),
      F(12376505799748489069,931268859619442688))
    print('PASS: 3^10=59049 first-stop words; nominal=3150; live=1565; cut=1585;')
    print('  Bellman independent minimum 680 states; 1238 strict positives; 2 ties;')
    print('  four-corner backward interpolation and 5 mixed policies exact.')
if __name__=='__main__':check()