#!/usr/bin/env python3
"""EC49DR signed-X6 ten-step full-rank witness and actual returning-future checks."""
from itertools import product
D=(-2,0,0,0,0,0)
Z=((1,0,0,0,0,0),(0,1,0,0,0,0),(0,0,1,0,0,0),(0,0,0,1,0,0),(0,1,0,0,1,0),(0,0,1,0,0,1))
X=(2,2,1,2,3,4);Y=(3,3,2,4,6,8)
P=((3,1,0,0,0,0),(2,1,1,0,0,0),(2,1,0,0,1,0))
OPS={'a':(-1,-1),'b':(-2,-2),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3)}
def observe(w):
    loc=[0]*6;cnt=[0]*6;a=b=last=0
    for s in w:
        i=abs(s)-1
        assert 0<=i<6
        loc[i]+=1 if s>0 else -1
        if s>0:cnt[i]+=1
        a=int(a or (last==1 and s==2));b=int(b or (last==2 and s==1))
        last=s if s in (1,2) else 0
    z=(int(not a and not b),int(not a and b),int(a and not b),int(a and b),int(not a and last==1),int(not b and last==2))
    return tuple(loc),tuple(cnt),z,(a,b)
def select(pos,z):
    neg=list(pos);neg[0]+=2
    state={(pos,tuple(neg),0,0,0):()}
    for _ in range(10):
        ns={}
        for (p,q,a,b,last),hist in state.items():
            for i in range(6):
                for s in (i+1,-(i+1)):
                    pp=list(p);qq=list(q)
                    if s>0:
                        if not pp[i]:continue
                        pp[i]-=1
                    else:
                        if not qq[i]:continue
                        qq[i]-=1
                    aa=int(a or (last==1 and s==2));bb=int(b or (last==2 and s==1))
                    ll=s if s in (1,2) else 0
                    key=(tuple(pp),tuple(qq),aa,bb,ll)
                    if key not in ns:ns[key]=hist+(s,)
        state=ns
    return min((w for w in state.values() if observe(w)[2]==z),default=None)
def wt(p,weights):
    r=1
    for j,c in enumerate(p):r*=weights[j]**c
    return r
def det_exact(M):
    A=[list(row) for row in M];n=len(A);sign=1;prev=1
    for k in range(n-1):
        if not A[k][k]:
            j=next((j for j in range(k+1,n) if A[j][k]),None)
            if j is None:return 0
            A[k],A[j]=A[j],A[k];sign=-sign
        v=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                nom=A[i][j]*v-A[i][k]*A[k][j]
                assert nom%prev==0
                A[i][j]=nom//prev
            A[i][k]=0
        prev=v
    return sign*A[-1][-1]
def rank_mod(rows,p):
    basis={}
    for rr in rows:
        a=[v%p for v in rr]
        for col,r in sorted(basis.items()):
            v=a[col]
            if v:a=[(x-v*y)%p for x,y in zip(a,r)]
        j=next((j for j,v in enumerate(a) if v),None)
        if j is not None:
            fac=pow(a[j],-1,p);basis[j]=[(fac*v)%p for v in a]
    return len(basis)
def future_words(h):
    ans=[]
    for seq in product(OPS,repeat=h):
        f=tuple(s for ch in seq for s in OPS[ch]);loc=[0]*6
        for s in f:loc[abs(s)-1]+=1 if s>0 else -1
        if tuple(loc)==(2,0,0,0,0,0):ans.append(f)
    return ans
def direct_rank(paths,hs):
    fws=[f for h in hs for f in future_words(h)]
    rows=[]
    for hist in paths:
        row=[]
        for weights in (X,Y,None):
            for f in fws:
                loc,pos,z,label=observe(hist+f)
                value=wt(pos,weights) if weights is not None else 1
                row.extend(value*int(label==tag) for tag in ((0,0),(0,1),(1,0),(1,1)))
        rows.append(row)
    return (len(fws),rank_mod(rows,1000003),rank_mod(rows,1000033))
def main():
    assert all(Y[j]==2*X[j] for j in range(2,6))
    paths=[]
    for z in Z:
        for p in P:
            w=select(p,z)
            assert w is not None,(p,z)
            assert len(w)==10 and observe(w)[:3]==(D,p,z)
            paths.append(w)
    G=[(wt(p,X),wt(p,Y),1) for p in P]
    gdet=det_exact(G);assert gdet==-432
    M=[]
    for w in paths:
        _,p,z,_=observe(w)
        M.append(tuple(wt(p,X)*v for v in z)+tuple(wt(p,Y)*v for v in z)+z)
    d=det_exact(M)
    assert abs(d)==432**6 and rank_mod(M,1000003)==rank_mod(M,1000033)==18
    outcomes={k:direct_rank(paths,hs) for k,hs in (('h2',(2,)),('h3',(3,)),('h4',(4,)),('h5',(5,)),('cumulative',(1,2)))}
    assert [v[1:] for v in outcomes.values()]==[(15,15),(18,18),(15,15),(18,18),(18,18)]
    print("PASS",{"n":10,"D":D,"histories":len(paths),"detG":gdet,"detM18":d,"rank18":18,"future":outcomes})
if __name__=="__main__":main()
