"""Check every directional derivative by exact dual arithmetic in fixed examples."""
from fractions import Fraction as F
from itertools import product
import json

def one_plus(p):
    return (1+p[0],p[1])

def mul(p,q):
    return p[0]*q[0], p[0]*q[1]+p[1]*q[0]

def div(p,q):
    return p[0]/q[0], (p[1]*q[0]-p[0]*q[1])/q[0]**2

def eval_log_deriv(coeffs, W, which):
    def get(j,e):
        p=(1/(1+j*W), (1/(1+j*W))*W/e if which == len(coeffs) else F(0))
        for i in reversed(range(len(coeffs))):
            t=F(0), F(i==which)
            a=coeffs[i],F(0)
            p=div(one_plus(mul(t,p)), one_plus(mul(a,p)))
        return p
    R=div(get(F(1,2),F(6)),get(F(5),F(3,32)))
    return R[1]/R[0]

def closed_two(a,b,W):
    d,D=1/(1+W/2),1/(1+5*W)
    e,E=F(6),F(3,32)
    return (
        1/(1+b*d)-1/(1+b*D),
        -a*(d/(1+a+b*d) - D/(1+a+b*D)),
        a*b*W*(d/(e*(1+b*d)*(1+a+b*d))-D/(E*(1+b*D)*(1+a+b*D))),
    )

def main():
    count=0
    for a,b,W in product((F(1,997),F(23),F(997,2)),repeat=3):
        real = [eval_log_deriv((a,b),W,i) for i in range(3)]
        assert tuple(real) == closed_two(a,b,W)
        assert max(real)<0
        count+=3
    extra = 0
    for r in range(1,11):
        coeffs = [F((i+2)**3, 11+3*i) for i in range(r)]
        for W in (F(1,9),F(5),F(997,11)):
            checks = [eval_log_deriv(coeffs,W,i) for i in range(r+1)]
            assert all(checks)
            extra+=len(checks)
    print(json.dumps(dict(exact_two_block_derivatives=count,derivatives_through_depth_ten=extra),indent=2))
if __name__=='__main__':
    main()
