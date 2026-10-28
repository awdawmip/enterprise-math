"""Exact finite-field check for GH-31 elliptic square-fiber lift (author-only)."""
from math import comb

def primes():
    for p in range(19,2001):
        if p%8==3 and all(p%d for d in range(2,int(p**.5)+1)):
            yield p

def chi(a,p):
    v=pow(a%p,(p-1)//2,p)
    return 0 if v==0 else (1 if v==1 else -1)

def check(p):
    m=(p-3)//8
    hG=lambda x:chi(x,p)*pow(x*(x+1),3*m+1,p)*pow(1+9*x,m-1,p)*(5-9*x)%p
    old_B=0
    square_x=[]
    for x in range(p):
        Q=x*(x+1)*(9*x+1)%p
        if chi(Q,p)==1:
            square_x.append(x)
            old_B=(old_B+hG(x))%p
        elif Q==0:
            assert hG(x)==0
    E_sum=0; C_sum=0; Epoints=set(); Cpoints=set()
    for x in range(p):
        Q=x*(x+1)*(9*x+1)%p
        for y in range(p):
            if y*y%p!=Q:continue
            Epoints.add((x,y))
            E_sum=(E_sum+hG(x))%p
            if x not in (0,p-1,(-pow(9,-1,p))%p):
                assert y !=0
                z=y*pow(3*x*(x+1),-1,p)%p
                delta=((6*x+3)*z*z-3)%p
                assert delta*delta%p==(9*z**4-14*z*z+9)%p
                t=(3*(z*z+1)+delta)*pow(6*z*z,-1,p)%p
                assert t==(x+1)%p
                Cpoints.add((z,delta))
    for z in range(1,p):
        v=z*z%p
        D=(9*v*v-14*v+9)%p
        for delta in range(p):
            if delta*delta%p!=D:continue
            assert (z,delta) in Cpoints, (p,z,delta)
            x=((delta+3)*pow(6*v,-1,p)-pow(2,-1,p))%p
            assert x not in (0,p-1,(-pow(9,-1,p))%p)
            y=3*x*(x+1)*z%p
            assert (x,y) in Epoints
            t=(3*(v+1)+delta)*pow(6*v,-1,p)%p
            assert t==(x+1)%p
            C_sum+=pow(z,2*m-2,p)*chi(t,p)*delta
    C_sum=C_sum*pow(9,m+1,p)*pow(16,-1,p)%p
    B_E=E_sum*pow(2,-1,p)%p
    assert old_B==B_E==C_sum,(p,old_B,B_E,C_sum)
    assert len(Cpoints)==len(Epoints)-3, (p,len(Cpoints),len(Epoints))  # Check E excludes 3 rational branch points.
    return p,old_B,len(Epoints),len(Cpoints)

if __name__=='__main__':
    out=[check(p) for p in primes()]
    print('PASS_GH31_ELLP_CURVE_POINT_MOMENT_AND_QUARTIC_BIRATIONAL',len(out))
    for p in (19,43,67,83):
        print('example',next(v for v in out if v[0]==p))
