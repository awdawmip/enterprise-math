"""Three independent positive parameters in a two-coordinate fractional-linear chain."""
from fractions import Fraction as Q
import json


def derivative_check():
    def row(p):
        tail=1/(1+2*p)
        middle=1/(1+2*tail)
        initial=1/(1+2*middle)
        return middle*initial, -2*initial**2*tail*middle
    u,v=row(Q(1)); w,z=row(Q(2))
    return u*z-v*w


def outputs(t1,t2,t3,mod):
    def row(p):
        tail=(1+t3*p)*pow(1+2*p,-1,mod)%mod
        mid=(1+t2*tail)*pow(1+2*tail,-1,mod)%mod
        outer_inv=pow(1+2*mid,-1,mod)
        val=(1+t1*mid)*outer_inv%mod
        d1=mid*outer_inv%mod
        d2=(t1-2)*outer_inv**2*tail*pow(1+2*tail,-1,mod)%mod
        return val,d1,d2
    return row(1),row(2)


def solve(bits,v3):
    mod=1<<bits
    left,right,t3=1<<12,1<<30,1<<v3
    work=4*mod
    T=outputs(left,right,0,work)
    vals=[t[0] for t in T]
    steps=0
    while True:
        (a,aa,ab),(b,ba,bb)=outputs(left,right,t3,work)
        e=(vals[0]-a)%work; f=(vals[1]-b)%work
        if e%mod==f%mod==0: break
        det=(aa*bb-ab*ba)%work
        assert det%8==4
        reduced=mod
        def ratio(z):
            assert z%4==0
            return (z//4)*pow(det//4,-1,reduced)%reduced
        left=(left+ratio(bb*e-ab*f))%mod
        right=(right+ratio(aa*f-ba*e))%mod
        steps+=1
        assert steps<15
    assert (left&-left)==1<<12 and (right&-right)==1<<30
    return dict(bits=bits,third_order=v3,steps=steps,matching_endpoints=2)


if __name__=='__main__':
    det=derivative_check()
    assert det==Q(388,34969)
    print(json.dumps(dict(determinant=str(det),controls=[solve(n,v) for n in (128,256,512,1024)
                                                         for v in (60,99)]),indent=2))
