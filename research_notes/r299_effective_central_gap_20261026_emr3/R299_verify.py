#!/usr/bin/env python3
"""Independent exact source-word DP and algebraic-kernel crosscheck for R299."""
import json
MAXR=180
K=[1,-2,1,-8,6,-3,7,-5,1]
LL=[-1,1,-8,4,-6,11,-6,1]
def pmul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c
def padd(a,b):
    c=[0]*max(len(a),len(b))
    for i,x in enumerate(a):c[i]+=x
    for i,x in enumerate(b):c[i]+=x
    return c
def trim(a):
    while a and a[-1]==0:a.pop()
    return a
def qreduce(d):
    """Z[y,w]/(y*w*w-(1+2y²-y³)*w+1), reducing a polynomial with integral remainder."""
    d=d.copy()
    for j in range(max([e[1] for e in d] or [0]),1,-1):
        for (i,jj),v in list(d.items()):
            if jj!=j or not v:continue
            del d[i,j]
            for di,dj,c in [(-1,-1,1),(1,-1,2),(2,-1,-1),(-1,-2,-1)]:
                p=(i+di,j+dj);d[p]=d.get(p,0)+v*c
    return {k:v for k,v in d.items() if v}
def qpoly():
    def plus(*ps):
        z={}
        for p in ps:
            for k,v in p.items():z[k]=z.get(k,0)+v
        return {k:v for k,v in z.items() if v}
    def mul(x,y):
        z={}
        for (i,j),v in x.items():
            for (ii,jj),w in y.items():
                key=(i+ii,j+jj);z[key]=z.get(key,0)+v*w
        return {k:v for k,v in z.items() if v}
    def power(a,n):
        b={(0,0):1}
        for _ in range(n):b=mul(b,a)
        return b
    y={(1,0):1};w={(0,1):1};one={(0,0):1}
    U=plus(one,{(1,0):-1,(2,0):1,(1,1):-1});V=plus(one,{(1,1):-1})
    neg=lambda a:{k:-v for k,v in a.items()}
    N=mul(power(y,3),mul(power(w,2),plus(mul(power(w,2),U),neg(V))))
    r0=[0]*4+[-v for v in pmul(pmul([-2,1],[-1,1]),[-1,-1,-2,1])]
    r1=[0]*4+[-v for v in pmul([-1,1],LL)]
    expected={(i,0):v for i,v in enumerate(r0) if v}
    expected.update({(i,1):v for i,v in enumerate(r1) if v})
    assert qreduce(N)==expected
    left=padd(pmul([0,2],r0),pmul(r1,[1,0,2,-1]))
    right=[0]*4+pmul(pmul([-1,1],[1,-3,1]),K)
    assert left==right
    M=[2,0,1,-3,1]
    assert trim(padd(K,pmul([1,-1],LL)))==trim([0,0]+[2*x for x in pmul([-2,1],M)])
def kernel(N):
    h=[0]*(N+1);g=[0]*(N+1)
    for n in range(N+1):
        x=int(n==4)
        for j,c in ((1,1),(2,2),(3,1),(4,1)):
            if n>=j:x+=c*h[n-j]
        for j,c in ((1,1),(2,2),(3,1)):
            if n>=j:
                for i in range(4,n-j-3):x+=c*h[i]*h[n-j-i]
        h[n]=x
        g[n]=int(n==0)+h[n]+(h[n-1] if n>0 else 0)+(g[n-3] if n>=3 else 0)
    assert h[4]==1 and all(z>0 for z in h[4:])
    assert g[0]==1 and g[1:3]==[0,0] and all(x>0 for x in g[3:])
    M=[2,0,1,-3,1]
    correction=pmul([0,-2,1],M)
    nom=[0]*(N+1)
    for i,k in enumerate(K):
        for j,x in enumerate(g):
            if i+j<=N:nom[i+j]+=k*x
    for i,c in enumerate(correction):nom[i]-=c
    filtr=[0]*(N+1)
    for i in range(N+1):filtr[i]=nom[i]-(filtr[i-1] if i else 0)
    return [0]*4+filtr[:N-3]
def raw_dp(maxn):
    edge={0:((2,-1,-1),(2,1,-1)),1:((0,-1,-1),(0,1,-1)),2:((1,1,1),(2,1,-1))}
    states={(0,1,0,0):1}
    aa=[];bb=[];samples={}
    for n in range(maxn+1):
        counts={}
        for (q,e,k,z),v in states.items():
            if q==0:counts[e,k]=counts.get((e,k),0)+v
        get=lambda e,k:counts.get((e,k),0)
        if n%2==0:aa.append(get(1,-4)-get(-1,-4))
        else:bb.append(get(-1,-3)-get(1,-5))
        if n in (80,81,82,100,200,300,360):
            a,b=((1,-4),(-1,-4)) if n%2==0 else ((-1,-3),(1,-5))
            samples[str(n)]={"first":str(get(*a)),"second":str(get(*b)),"gap":str(get(*a)-get(*b))}
        if n==maxn:break
        nexts={}
        for (q,e,k,z),count in states.items():
            for bit,(qq,eta,step) in enumerate(edge[q]):
                if bit==0 and z:continue
                key=(qq,eta*e,eta*k+step,int(bit==0))
                nexts[key]=nexts.get(key,0)+count
        states=nexts
    return aa,bb,samples
def verify():
    qpoly()
    aa,bb,samples=raw_dp(360)
    assert aa==kernel(MAXR)
    for i in range(len(bb)):
        assert bb[i]==aa[i+2]-aa[i+1]-(2*aa[i-1] if i>=1 else 0)+(aa[i-2] if i>=2 else 0)
    assert samples["80"]["gap"]=="-727277462" and samples["82"]["gap"]=="1985689179"
    assert all(aa[i]>0 and aa[i+1]>=2*aa[i] for i in range(41,MAXR))
    return {"schema":"EM_R299_INDEPENDENT_BRC_DP_V1","status":"PASS","max_length":360,
            "even_gap_coefficients_matched":181,"cross_parity_coefficients_matched":179,
            "kernel":"h positive ordered source recurrence, g=(1+(1+y)h)/(1-y³)",
            "symbolic":"Q-reduction and two integer polynomial identities","samples":samples,
            "limitation":"Finite source checks do not independently prove R294 all-length source-to-GF mapping or native X6 correspondence"}
if __name__=="__main__":
    print(json.dumps(verify(),ensure_ascii=False,indent=2))
