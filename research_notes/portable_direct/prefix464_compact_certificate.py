#!/usr/bin/env python3
"""PREFIX-464 finite-horizon signature codec: exact stdlib certificate."""
from fractions import Fraction as F
from math import comb, factorial

def compositions(k,n,t=()):
    if k==1:
        yield t+(n,)
    else:
        for a in range(n+1): yield from compositions(k-1,n-a,t+(a,))

def primevals(x):
    z={}
    for e,n in ((1,x.numerator),(-1,x.denominator)):
        p=2
        while p*p<=n:
            while n%p==0:
                z[p]=z.get(p,0)+e;n//=p
            p+=1
        if n>1:z[n]=z.get(n,0)+e
    return {p:v for p,v in z.items() if v}

def rank(rows):
    a=[list(map(F,row)) for row in rows]
    if not a:return 0
    h=0
    for j in range(4):
        i=next((i for i in range(h,len(a)) if a[i][j]),None)
        if i is None:continue
        a[h],a[i]=a[i],a[h]
        v=a[h][j];a[h]=[x/v for x in a[h]]
        for i in range(h+1,len(a)):
            v=a[i][j];a[i]=[x-v*y for x,y in zip(a[i],a[h])]
        h+=1
        if h==len(a):break
    return h

def rows(weights):
    w0,plus,minus=weights
    rho=[a*b for a,b in zip(plus,minus)]
    factors=[primevals(x/rho[0]) for x in rho[1:]]
    B=[[d.get(p,0) for d in factors] for p in sorted(set().union(*(set(d) for d in factors)))]
    C=[]
    for row in B:
        if rank(C+[row])>len(C):C.append(row)
    assert len(C)==rank(B)
    return C

def pack(sig,p,C):
    code,base=0,1
    for v,row in zip(sig,C):
        lo=p*min(0,*row); width=p*(max(0,*row)-min(0,*row))+1
        assert 0<=v-lo<width
        code+=(v-lo)*base;base*=width
    return code,base

def unpack(code,p,C):
    out=[]
    for row in C:
        lo=p*min(0,*row);width=p*(max(0,*row)-min(0,*row))+1
        code,a=divmod(code,width);out.append(lo+a)
    assert code==0
    return tuple(out)

def native_moves(w):
    w0,plus,minus=w
    move=[((1,0,0,0,0,0),w0,0,0)]
    for i in range(5):
        for sign,weight in ((1,plus[i]),(-1,minus[i])):
            d=[0]*6;d[i+1]=sign;move.append((tuple(d),weight,i,sign))
    return move

def family(rho):return (F(5),tuple([F(1)]*5),tuple(map(F,rho)))

def verify(name,w):
    C=rows(w);r=len(C); moves=native_moves(w)
    if name.startswith('r') and name[1:].isdigit():assert r==int(name[1:])
    states={((0,)*6, (0,)*r):1}
    report=[f'FAMILY {name} rank={r} basis={C}']
    fac=[factorial(i) for i in range(8)]
    for m in range(8):
        exact={};weighted={};total=0
        for v in compositions(11,m):
            s=v[0];y=tuple(v[2*i+1]-v[2*i+2] for i in range(5));pt=(s,)+y
            u=tuple(min(v[2*i+1],v[2*i+2]) for i in range(1,5))
            sig=tuple(sum(row[j]*u[j] for j in range(4)) for row in C)
            count=fac[m]
            den=1
            for a in v:den*=fac[a]
            count=fac[m]//den
            weight=w[0]**v[0]
            for i in range(5):weight*=w[1][i]**v[2*i+1]*w[2][i]**v[2*i+2]
            key=(pt,sig)
            if key in weighted:assert weighted[key]==weight
            else:weighted[key]=weight
            exact[key]=exact.get(key,0)+count;total+=count
        assert total==11**m and exact==states
        projected={}
        for key,count in states.items():
            pt,sig=key;p=(m-pt[0]-sum(map(abs,pt[1:])))//2
            code,size=pack(sig,p,C)
            assert unpack(code,p,C)==sig and 0<=code<size
            ek=(pt,weighted[key]);projected[ek]=projected.get(ek,0)+count
        assert len(projected)==len(states)
        report.append(f'PASS m={m} states={len(states)} paths={total}')
        if m==7:break
        new={}
        for (pt,sig),count in states.items():
            for d,weight,i,sign in moves:
                pos=tuple(a+b for a,b in zip(pt,d))
                sig2=list(sig)
                if sign and i>0 and pt[i+1]*sign<0:
                    for j,row in enumerate(C):sig2[j]+=row[i-1]
                key=(pos,tuple(sig2));new[key]=new.get(key,0)+count
        states=new
    for p in (2,4,8,16):
        seen=set()
        for pi in compositions(5,p):
            u=pi[1:]
            sig=tuple(sum(row[j]*u[j] for j in range(4)) for row in C)
            key,size=pack(sig,p,C)
            assert unpack(key,p,C)==sig
            seen.add(key)
        report.append(f'FIBER p={p} distinct={len(seen)} occupations={comb(p+4,4)} bits={(size-1).bit_length()}')
    return '\n'.join(report)

if __name__=='__main__':
    cases={'r0':family((6,6,6,6,6)),'r1':family((6,12,24,48,96)),
      'r2':family((6,12,18,24,36)),'r3':family((6,12,18,30,24)),
      'r4':family((6,12,18,30,42)),
      'rational':(F(2,3),(F(1,2),F(2,3),F(5,4),F(7,3),F(11,5)),
                   (F(3,2),F(7,3),F(13,5),F(17,7),F(19,11)))}
    for name,weights in cases.items():print(verify(name,weights))
    print('ALL_CHECKS_PASS')
