#!/usr/bin/env python3
"""Exact finite-field checker for CM(-24) quartic Frobenius/Mobius/first-jet port.
No native crystalline Frobenius or enterprise-specific experiment is simulated.
"""
from math import isqrt
Q = [1, -140, 294, -140, 1] # ascending t^0..t^4

def primes(n):
    a=bytearray(b'\x01')*(n+1)
    a[0]=a[1]=0
    for i in range(2,isqrt(n)+1):
        if a[i]: a[i*i:n+1:i]=b'\0'*((n-i*i)//i+1)
    return [p for p in range(5,n+1) if a[p] and p%8==5]

def ring(p):
    def A(a,b): return tuple((a[i]+b[i])%p for i in range(4))
    def sub(a,b): return tuple((a[i]-b[i])%p for i in range(4))
    def scale(a,n):return tuple((n*a[i])%p for i in range(4))
    def M(a,b):
        v=[0]*7
        for i in range(4):
            for j in range(4):v[i+j]+=a[i]*b[j]
        for k in range(6,3,-1):
            h=v[k]%p
            for i in range(4):v[k-4+i]-=h*Q[i]
        return tuple(v[i]%p for i in range(4))
    def P(a,k):
        acc=(1,0,0,0)
        while k:
            if k&1:acc=M(acc,a)
            a=M(a,a);k>>=1
        return acc
    return A,sub,scale,M,P

def run(limit=20000):
    count={"all":0,"split":0,"inert":0,"split_C_zero":0,"inert_C_nonzero":0,"two_coordinate_norm_checked":0}
    samples={}
    for p in primes(limit):
        add,sub,scale,mul,powr=ring(p)
        one=(1,0,0,0); T=(0,1,0,0); zero=(0,0,0,0)
        def lin(a,b):return (a%p,b%p,0,0)
        tp=powr(T,p)
        if p%24==13:
            assert sub(mul(lin(7,-5),tp),lin(5,-7))==zero,(p,'inert_F')
            count['inert']+=1
        else:
            assert p%24==5
            assert sub(mul(lin(5,-7),tp),lin(7,-5))==zero,(p,'split_G')
            count['split']+=1
        # This computes Hasse first jet, directly from original binomial (m choose k)^2.
        m=(p-1)//2
        binoms=[1]
        for k in range(1,m+1):
            binoms.append(binoms[-1]*(m-k+1)*pow(k,-1,p)%p)
        H=zero; Hd=zero
        # Horner evaluation in F_p[t]/(Q), polynomial 0..m
        for k in range(m,-1,-1):
            ck=binoms[k]**2 %p
            H=add(mul(H,T),(ck,0,0,0))
            Hd=add(mul(Hd,T),(k*ck%p,0,0,0))
        # Hd is t*H'(t), so H' = (Hd/t)
        invT=tuple((-Q[i+1])%p for i in range(4)) # from Q(t)/t = t^3-140t^2+294t-140+1/t
        assert mul(T,invT)==one
        Hprime=mul(Hd,invT)
        # Jacobi split-derivative defect as polynomial in the quartic extension
        a=scale(sub(T,mul(powr(T,3),one)),16)  # 16t(1-t^2)
        b=add(add(one,scale(T,2)),scale(powr(T,2),-7))
        C=add(mul(a,Hprime),mul(b,H))
        # Exact reciprocal covariance for any characteristic p>3:
        # C(t^{-1}) = t^{-m-2} C(t).
        # Convert C(t) in quotient into C(t^{-1}) (the algebraic substitution).
        Cinverse=zero
        for ck in reversed(C):
            Cinverse=add(mul(Cinverse,invT),(ck,0,0,0))
        assert Cinverse==mul(powr(invT,m+2),C),(p,'reciprocity')
        # Inversion-invariant defect D=t^{-(m+2)/2} C belongs to F_p[y],
        # y=t+t^{-1}, y^2-140y+292=0, a quadratic FIELD for p=5(mod8).
        assert (m+2)%2==0
        D=mul(powr(invT,(m+2)//2),C)
        d1=(-D[3])%p
        d0=(D[0]+140*D[3])%p
        y=add(T,invT)
        assert D==add((d0,0,0,0),scale(y,d1)),(p,'2D_source',D,d0,d1)
        norm=(d0*d0+140*d0*d1+292*d1*d1)%p
        assert (norm==0)==(C==zero),(p,'field_norm',norm,C)
        count['two_coordinate_norm_checked']+=1
        if p%24==5:
            assert C==zero,(p,'split_C_finite_observation',C)
            count['split_C_zero']+=1
        else:
            assert C!=zero,(p,'inert_C_finite_observation')
            count['inert_C_nonzero']+=1
        if p in (5,13,29,37,53,373):
            samples[str(p)]={"p_mod_24":p%24,"t_to_tp":'G' if p%24==5 else 'F',"H_mod_Q":list(H),"C_mod_Q":list(C),"d0":d0,"d1":d1,"norm":norm}
        count['all']+=1
    return {"pass":True,"counts":count,"samples":samples}
if __name__=='__main__':
    import json
    print(json.dumps(run(),indent=2,sort_keys=True))
