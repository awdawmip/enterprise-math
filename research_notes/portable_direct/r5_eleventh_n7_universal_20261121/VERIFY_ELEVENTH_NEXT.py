#!/usr/bin/env python3
"""Frozen R5: exact primitive-11 second-pole coefficient certificate.
No float, third-party dependency, or formal theorem admission.
"""
from fractions import Fraction as Q
import json
p=11; dim=10
zero=(Q(0),)*dim
one=(Q(1),)+(Q(0),)*(dim-1)
def add(x,y): return tuple(a+b for a,b in zip(x,y))
def neg(x): return tuple(-a for a in x)
def sub(x,y): return add(x,neg(y))
def scale(x,s): return tuple(s*a for a in x)
def mult(x,y):
    v=[Q(0)]*p
    for i,a in enumerate(x):
        if a:
            for j,b in enumerate(y):
                if b: v[(i+j)%p]+=a*b
    return tuple(v[i]-v[-1] for i in range(dim))
def zpow(r):
    r%=p
    return (-Q(1),)*dim if r==10 else tuple(Q(i==r) for i in range(dim))
def inv1(r):
    v=zero
    for j in range(1,p):v=add(v,scale(zpow(j*r),-Q(j,p)))
    assert mult(sub(one,zpow(r)),v)==one
    return v
def ssum(xs):
    v=zero
    for x in xs:v=add(v,x)
    return v
def geometries(residues,n):
    coeff=[one]+[zero]*(n-1)
    for r in residues:
        out=[one]+[zero]*(n-1)
        for i in range(1,n):out[i]=add(coeff[i],mult(zpow(r),out[i-1]))
        coeff=out
    return coeff
def prefix(vals):
    s=zero;out=[]
    for v in vals:s=add(s,v);out.append(s)
    return out
def certificate_sequence(n):
    # V(t)=[(1-t)(1-z*t)(1-z^-1*t)]^-1,
    # W(t)=t*V(t)/(1-t), U(t)=prod_{r=7,8,9}(1-z^r*t)^-1.
    v=geometries((0,1,10),n)
    w=[zero]*n;running=zero
    for i in range(1,n):running=add(running,v[i-1]);w[i]=running
    u=prefix(geometries((7,8,9),n))
    u0=prefix(geometries((5,6,7,8,9),n))
    # J_c(t) = [t^2 V(t^2)/(1-t) - c^2 V(ct)/(1-c)
    #             -t W(t^2) + c W(ct)]/(t-c).
    def J(r):
        inv=inv1(r);c2inv=mult(zpow(2*r),inv)
        num=[];prefix_even=zero
        for i in range(n):
            if i>=2 and i%2==0:prefix_even=add(prefix_even,v[(i-2)//2])
            q=sub(prefix_even,mult(c2inv,mult(v[i],zpow(r*i))))
            if i%2:q=sub(q,w[(i-1)//2])
            q=add(q,mult(w[i],zpow(r*(i+1))))
            num.append(q)
        out=[]
        for i in range(n):
            out.append(mult(zpow(-r),sub((out[-1] if out else zero),num[i])))
        return out
    j5,j6=J(5),J(6)
    # E(t)=t V(t^2)/(1-t)-W(t^2).
    e=[];q=zero
    for i in range(n):
        if i>=1 and i%2:q=add(q,v[(i-1)//2])
        e.append(sub(q,(w[i//2] if i%2==0 else zero)))
    s=[sub(add(j5[i],j6[i]),e[i]) for i in range(n)]
    T=[ssum(mult(u[j],s[i-j]) for j in range(i+1)) for i in range(n)]
    # D(t)=-z*d_x [ (1-t)^-1 prod_{price=214}^218(1-x^price*t)^-1 ] at x=z.
    D=[zero]*n
    for i in range(1,n):
        D[i]=neg(ssum(scale(mult(zpow(price*j),u0[i-j]),price)
                       for price in range(214,219) for j in range(1,i+1)))
    factor=mult(sub(one,zpow(10)),sub(one,zpow(1)))
    C=[add(scale(mult(factor,T[i]),220),D[i]) for i in range(n)]
    return v,T,D,C
def independent_T(m):
    # Direct L0=a+b+s, min(L1,L2)=min(a,b)+s+w,
    # with s=c+d+e, w=f+g+h. Infinite geometric a/b tails
    # converge in x then specialize x=z: (1-z^r)^-1.
    u=geometries((7,8,9),m);v=geometries((0,1,10),m)
    val=zero
    for s in range(m):
        for w in range(m-s):
            t=m-s;k=t-w
            j=ssum(mult(zpow(5*a+6*(t-a)),inv1(6)) for a in range(k))
            j=add(j,ssum(mult(zpow(6*b+5*(t-b)),inv1(5)) for b in range(k)))
            j=sub(j,ssum(zpow(5*a+6*b) for a in range(k) for b in range(k) if a+b>=t))
            val=add(val,mult(mult(u[s],v[w]),j))
    return val
def independent_D(m):
    # Reweighted finite 5-tuple DP for -z B'_m(z).
    counts=[one]+[zero]*(m-1); moments=[zero]*m
    for price in range(214,219):
        nc=[zero]*m;nd=[zero]*m
        for s in range(m):
            for k in range(m-s):
                zz=zpow(price*k)
                nc[s+k]=add(nc[s+k],mult(counts[s],zz))
                nd[s+k]=add(nd[s+k],add(mult(moments[s],zz),scale(mult(counts[s],zz),price*k)))
        counts,moments=nc,nd
    return neg(ssum(moments))
def main():
    n=90
    _,T,D,C=certificate_sequence(n)
    cross=[1,2,3,4,5,6,7,8,9,10,11,12,13,18,19,20,21,22]
    for m in cross:
        assert independent_T(m)==T[m-1],('direct T',m)
        assert independent_D(m)==D[m-1],('direct derivative',m)
    # Rational-function proof gives denominator dividing (1-t^22)^3,
    # and numerator degree <=60. Compute its complete 61 coefficients.
    F=[]
    for i in range(61):
        v=C[i]
        if i>=22:v=sub(v,scale(C[i-22],3))
        if i>=44:v=add(v,scale(C[i-44],3))
        F.append(v)
    assert all(ssum(F[r::22])==zero for r in range(22))
    # Thus (1-t^22)^2 sum C_{m}t^(m-1) is polynomial degree<=38.
    for i in range(39,n):
        v=C[i]
        if i>=22:v=sub(v,scale(C[i-22],2))
        if i>=44:v=add(v,C[i-44])
        assert v==zero,('period22 affine',i)
    ex={}
    for r in range(7,12):
        x,y=C[r-1],C[r+10]
        assert C[r+21]==add(x,y)
        assert C[r+32]==scale(y,2)
        assert x[0]!=0 and y[0]!=0 and x[0]*y[0]>0
        for k in range(6):
            got=C[r+11*k-1]
            want=add(x,scale(y,k//2)) if k%2==0 else scale(y,(k+1)//2)
            assert got==want
        ex[str(r)]={'C_r':list(map(int,x)),'C_r_plus_11':list(map(int,y)),
                    'first_basis_coordinate':[int(x[0]),int(y[0])]}
    out={'schema':'R5_PRIMITIVE11_N7_UNIVERSAL_V1','status':'PASS',
         'basis':'Z[z]/Phi_11(z), coefficient index 0..9',
         'C_definition':'220*(1-z^10)*(1-z)*T_m - z*derivative(B_m) evaluated at z',
         'exceptional_classes_r_mod11':['7','8','9','10','0'],
         'C_class_templates':ex,'common_denominator_bound':'(1-t^22)^3',
         'numerator_degree_bound':60,'divisible_by_1_minus_t22':True,
         'residual_numerator_degree_bound':38,
         'independent_direct_thresholds':cross,'exact_arithmetic':True,
         'new_cost_period_at_O(N^6)':{'m_mod13_1_to_8':360360,'m_mod13_0_9_to_12':27720},
         'formal_independent_review':'NOT_REVIEWED'}
    print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__':main()
