#!/usr/bin/env python3
"""Independent grouped complete-homogeneous exact audit of primitive17 Laurent
next coefficient. This groups price counts by x,y,u,v rather than retaining
all selected-event load-state DP states; integer arithmetic, no rounding.
"""
import json
D=17
ZERO=(0,)*D
ONE=(1,)+(0,)*(D-1)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
def scale(a,k):return tuple(k*x for x in a)
def shift(a,k):
    k%=D
    return tuple(a[(i-k)%D] for i in range(D))
def mul(a,b):
    v=[0]*D
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y:v[(i+j)%D]+=x*y
    return tuple(v)
def pairmul(a,b):
    return mul(a[0],b[0]),add(mul(a[1],b[0]),mul(a[0],b[1]))
def factor(p):
    return add(ONE,neg(shift(ONE,p))),scale(shift(ONE,p),-p)
def product_factor(prices):
    out=(ONE,ZERO)
    for p in prices:out=pairmul(out,factor(p))
    return out
def complete_homogeneous_group(prices,maxn):
    h=[(ZERO,ZERO) for _ in range(maxn+1)];h[0]=(ONE,ZERO)
    for p in prices:
        for n in range(1,maxn+1):
            old=h[n];prev=h[n-1]
            h[n]=(add(old[0],shift(prev[0],p)),add(old[1],add(shift(prev[1],p),scale(shift(prev[0],p),p))))
    return h
def masks_for(m):
    hU=complete_homogeneous_group([216,217,218],m-1)
    hV=complete_homogeneous_group([219,220,221],m-1)
    hv={(u,v):pairmul(hU[u],hV[v]) for u in range(m) for v in range(m)}
    hU0={(u,0):hU[u] for u in range(m)}
    masks={}
    sets={1:set(range(214,219)),2:{214,216,217,218,219,220,221},4:set(range(215,222))}
    for mask in range(1,8):
        selected=[bit for bit in (1,2,4) if mask&bit]
        union=set().union(*(sets[b] for b in selected))
        useX=214 in union;useY=215 in union;useV=219 in union
        s0=[0]*D;s1=[0]*D
        for u in range(m):
            for v in (range(m) if useV else (0,)):
                pv=hv[(u,v)] if useV else hU0[(u,0)]
                if not any(pv[0]):continue
                for x in (range(m) if useX else (0,)):
                    for y in (range(m) if useY else (0,)):
                        L0=x+y+u;L1=x+u+v;L2=y+u+v
                        if (mask&1 and L0>=m) or (mask&2 and L1>=m) or (mask&4 and L2>=m):continue
                        k=214*x+215*y
                        ix=k%D
                        for j in range(D):
                            v0=pv[0][j]
                            if v0:
                                s0[(j+ix)%D]+=v0
                                s1[(j+ix)%D]+=pv[1][j]+k*v0
                            elif pv[1][j]:s1[(j+ix)%D]+=pv[1][j]
        P=(tuple(s0),tuple(s1))
        W=product_factor(sorted(union))
        masks[mask]=pairmul(P,W)
    return masks
def reduce_phi(a):return tuple(a[i]-a[16] for i in range(16))
def compute(m):
    assert 13<=m<=17
    masks=masks_for(m)
    RA=(ZERO,ZERO)
    for mask,R in masks.items():
        sgn=1 if mask.bit_count()%2 else -1
        RA=(add(RA[0],scale(R[0],sgn)),add(RA[1],scale(R[1],sgn)))
    assert reduce_phi(RA[0])==(0,)*16
    W4=product_factor(range(296,313))
    assert reduce_phi(W4[1])==(-5202,)+(0,)*15
    DR_total=add(RA[1],W4[1])
    assert reduce_phi(DR_total)!=(0,)*16
    return {'m':m,'DR_A':list(reduce_phi(RA[1])),'DR_total':list(reduce_phi(DR_total))}
if __name__=='__main__':
    print(json.dumps({'status':'PASS','rows':[compute(m) for m in range(13,18)],'review':'NOT_REVIEWED'},indent=2))
