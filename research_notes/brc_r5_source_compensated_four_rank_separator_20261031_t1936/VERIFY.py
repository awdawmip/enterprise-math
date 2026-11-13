#!/usr/bin/env python3
"""Exact positive-mass BRC source-labelled four-observer test.

This finite auxiliary stopping process follows SOURCE_SPECIFIC_EXTENSION.md.
No native X6 or mathematical-admission claim is made.
"""
from fractions import Fraction as F
from itertools import product, combinations

Z,O,H=F(0),F(1),F(1,2)
A=(F(1,4),F(1,5))
K=(F(3,4),F(1,6))
DELTA=F(1,4)
ETA=F(1,64)
ZETA=F(1,32)

def leaves(bits,lr=False):
    def action(i,key):
        if lr:return bits[{'A':0,'D':1,'Y':2,'L':3}[key[0]]]
        if key=='A':return bits[i]
        if key=='D':return bits[2+i]
        if key=='Y':return bits[4+i]
        return bits[6+3*i+{'LC':0,'LD':1,'LY':2}[key]]
    for i,(a,k) in enumerate(zip(A,K)):
        q=H
        ac=action(i,'A')
        if not ac:
            yield i,ac,'A',q,O,1
            continue
        d,c,y=q*a,q*(1-2*a),q*a
        if not action(i,'D'):yield i,ac,'D_STOP',d,F(1,2),2
        else:
            yield i,ac,'D_HIGH',d*F(2,3),F(1,4),3
            yield i,ac,'LD',d*F(1,3),O,3+action(i,'LD')
        yield i,ac,'C_STOP',c*(1-k),O,2
        yield i,ac,'LC',c*k,O,3+action(i,'LC')
        if not action(i,'Y'):yield i,ac,'Y_STOP',y,F(3,2),2
        else:
            yield i,ac,'Y_HIGH',y*H,F(2),3
            yield i,ac,'LY',y*H,O,3+action(i,'LY')

def terminal_error(i,ac,route,lam,time):
    # A/source cross response is retained as terminal history, not a new decision.
    parity=O if (i==0 and ac==1) or (i==1 and ac==0) else -O
    return H+DELTA*parity+ETA*(route=="A")+ZETA*(route=="D_STOP")

def observer(bits,lr=False):
    ep=eq=tp=tq=sp=sq=Z
    origin_q=[Z,Z];origin_p=[Z,Z]
    for i,ac,route,q,lam,t in leaves(bits,lr):
        p=q*lam
        er=terminal_error(i,ac,route,lam,t)
        assert 0<er<1
        eq+=q*er;ep+=p*er;tp+=p*t;tq+=q*t
        sq+=q;sp+=p;origin_q[i]+=q;origin_p[i]+=p
    assert sp==sq==O,(sp,sq)
    assert origin_q==origin_p==[H,H],(origin_q,origin_p)
    return (ep,eq,tp,tq)

def rank(x):
    mat=[list(row) for row in x]
    if not mat:return 0
    nr=len(mat);nc=len(mat[0]);r=0
    for j in range(nc):
        pv=next((i for i in range(r,nr) if mat[i][j]),None)
        if pv is None:continue
        mat[r],mat[pv]=mat[pv],mat[r]
        w=mat[r][j];mat[r]=[v/w for v in mat[r]]
        for i in range(nr):
            if i!=r and mat[i][j]:
                w=mat[i][j]
                mat[i]=[v-w*u for v,u in zip(mat[i],mat[r])]
        r+=1
        if r==nr:break
    return r

def det4(vectors):
    m=[list(v) for v in vectors];d=O
    for j in range(4):
        k=next((i for i in range(j,4) if m[i][j]),None)
        if k is None:return Z
        if k!=j:m[j],m[k]=m[k],m[j];d=-d
        pivot=m[j][j];d*=pivot
        for i in range(j+1,4):
            s=m[i][j]/pivot
            for t in range(j,4):m[i][t]-=s*m[j][t]
    return d

def hull2(points):
    pts=sorted(set(points))
    def cr(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    lo=[];up=[]
    for a in pts:
        while len(lo)>=2 and cr(lo[-2],lo[-1],a)<=0:lo.pop()
        lo.append(a)
    for a in reversed(pts):
        while len(up)>=2 and cr(up[-2],up[-1],a)<=0:up.pop()
        up.append(a)
    return lo[:-1]+up[:-1]

def inside2(h,x):
    def cr(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    return len(h)>=3 and all(cr(h[j],h[(j+1)%len(h)],x)>=0 for j in range(len(h)))

def main():
    LR=[observer(b,True) for b in product((0,1),repeat=4)]
    FU=[observer(b,False) for b in product((0,1),repeat=12)]
    assert len(LR)==16 and len(FU)==4096
    th=[(1+k*(1-2*a))/a for a,k in zip(A,K)]
    assert th==[F(11,2),F(11,2)]
    assert min(terminal_error(i,ac,r,lam,t) for i in range(2) for ac in range(2) for r in ['A','D','Y'] for lam in (F(1,4),O,F(2)) for t in (1,2,3,4))>0
    assert max(terminal_error(i,ac,r,lam,t) for i in range(2) for ac in range(2) for r in ['A','D','Y'] for lam in (F(1,4),O,F(2)) for t in (1,2,3,4))<1
    rb=rank([tuple(x[i]-LR[0][i] for i in range(4)) for x in LR[1:]])
    time_hull=hull2([(x[2],x[3]) for x in LR])
    assert all(inside2(time_hull,(x[2],x[3])) for x in FU)
    print('theta',th,'rank(LR affine)',rb,'unique LR',len(set(LR)),'unique FULL',len(set(FU)))
    print('time hull LR vertices',time_hull,'FULL_outside=0')
    for j,n in enumerate(('eP','eQ','TP','TQ')):
        fmax=max(x[j] for x in FU);lmax=max(x[j] for x in LR)
        fmin=min(x[j] for x in FU);lmin=min(x[j] for x in LR)
        print(n,'max FULL LR gap',fmax,lmax,fmax-lmax,'min FULL LR diff',fmin,lmin,lmin-fmin)
    best=None
    for ids in combinations(range(1,len(LR)),4):
        vs=[tuple(LR[k][i]-LR[0][i] for i in range(4)) for k in ids]
        d=det4(vs)
        if d:
            best=(ids,d)
            break
    print('rank_certificate',best)
    if best:
        print('rank_certificate_points',[(k,LR[k]) for k in (0,*best[0])])
    print('max eQ FULL witness',next((bits,observer(bits,False)) for bits in product((0,1),repeat=12) if observer(bits,False)[1]==max(x[1] for x in FU)))
    assert max(x[1] for x in FU)-max(x[1] for x in LR)==F(63,256)
    assert max(x[1] for x in LR)==F(33,64)
    assert min(x[1] for x in FU)==F(33,128)
    assert min(x[1] for x in LR)==F(1,2)
    assert rb==4 and max(x[1] for x in FU)>max(x[1] for x in LR)
    print('PASS_EXACT_R5_COMPENSATED_FOUR_ERROR_SOURCE_ACTION_SEPARATOR')
if __name__=='__main__':main()
