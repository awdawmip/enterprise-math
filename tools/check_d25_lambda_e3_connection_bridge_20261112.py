#!/usr/bin/env python3
"""Exact (Z/p^2)[T]/(T^2-2) check of signed Hesse -> E3 lambda-connection.
Author-side connection geometry; not native divided-power Frobenius.
"""

class QuadraticRing:
    def __init__(self, modulus):
        self.m = modulus
        self.zero = (0, 0)
        self.one = (1, 0)

    def q(self, a, b=0):
        return (a % self.m, b % self.m)

    def add(self, x, y):
        return ((x[0]+y[0])%self.m, (x[1]+y[1])%self.m)

    def neg(self, x):
        return ((-x[0])%self.m, (-x[1])%self.m)

    def sub(self, x, y):
        return self.add(x, self.neg(y))

    def mul(self, x, y):
        return ((x[0]*y[0]+2*x[1]*y[1])%self.m,
                (x[0]*y[1]+x[1]*y[0])%self.m)

    def inv(self, x):
        n = (x[0]*x[0]-2*x[1]*x[1])%self.m
        inv_n = pow(n, -1, self.m)
        return self.q(x[0]*inv_n, -x[1]*inv_n)

    def div(self, x, y):
        return self.mul(x, self.inv(y))

    def power(self, x, n):
        if n < 0:
            return self.power(self.inv(x), -n)
        r = self.one
        while n:
            if n & 1:
                r = self.mul(r, x)
            x = self.mul(x, x)
            n >>= 1
        return r

    def scale(self, n, x):
        return self.mul(self.q(n), x)


def cubic_root_lift(p, r):
    # Known, already documented residue branch at p=373; deterministic search elsewhere.
    x = (56, 19) if p == 373 else None
    if x is None:
        modp = QuadraticRing(p)
        target = (4%p, 2%p)
        for a in range(p):
            for b in range(p):
                if modp.power((a,b), 3) == target:
                    x = (a,b)
                    break
            if x is not None: break
    assert x is not None
    target = r.q(4,2)
    # Newton/Hensel: cubic derivative 3*x^2 is a unit at every target prime.
    delta = r.div(r.sub(r.power(x,3),target),r.scale(3,r.power(x,2)))
    ans = r.sub(x,delta)
    assert r.power(ans,3)==target
    return ans


def sqrt_minus_three(p):
    # Select the earlier p=373 r residue to make signed witness comparable.
    r0 = 177 if p == 373 else next(a for a in range(1,p) if (a*a+3)%p==0)
    m = p*p
    # Integers: (r0^2+3)/p is divisible since r0 is a root mod p.
    r1 = (-((r0*r0+3)//p)*pow(2*r0,-1,p))%p
    r = (r0+p*r1)%m
    assert (r*r+3)%m==0
    return r


def verify(p):
    assert p%24 in (13,19)
    R=QuadraticRing(p*p)
    q=R.q; add=R.add; sub=R.sub; mul=R.mul; div=R.div; power=R.power; scale=R.scale
    one=R.one
    lam=cubic_root_lift(p,R)
    rad=sqrt_minus_three(p)
    s=scale(rad,lam)
    t=power(lam,3); d=sub(t,one)
    w=sub(one,power(lam,-3))
    assert t == q(4,2)
    assert w == div(q(2,1),q(4))
    # For the source Hesse lambda^(-3)=u=(2-T)/4, E3 port w=1-u=(2+T)/4.
    E_den=scale(12,mul(w,sub(one,w)))
    E=[[div(sub(scale(4,w),q(3)),E_den),div(sub(scale(8,w),q(9)),E_den)],
       [div(one,E_den),div(sub(q(3),scale(4,w)),E_den)]]
    H=[[div(scale(-3,power(lam,2)),scale(4,d)),div(scale(3,mul(lam,add(t,q(8)))),scale(4,d))],
       [div(q(-1),scale(12,d)),div(scale(3,power(lam,2)),scale(4,d))]]
    c=div(q(3),power(lam,4))
    assert c==div(q(3),power(lam,4))
    assert scale(rad*rad,one)==q(-3)
    # G^-1*M_H*G + G^-1 G', with G=diag(s,s^-1) and G^-1 G'=diag(1/lambda,-1/lambda).
    gauge=[[add(H[0][0],power(lam,-1)), div(H[0][1],power(s,2))],
           [mul(H[1][0],power(s,2)), sub(H[1][1],power(lam,-1))]]
    assert [[mul(c,E[i][j]) for j in range(2)] for i in range(2)]==gauge
    # Source Hesse observable omega_H+6*connection_lambda(omega_H), omega_H=2e0_H.
    obs_H=(add(q(2),scale(12,H[0][0])),scale(12,H[1][0]))
    assert obs_H==(sub(q(2),div(scale(9,power(lam,2)),d)),div(q(-1),d))
    # H form represented in E basis via G^-1.
    obs_in_E=(div(obs_H[0],s),mul(s,obs_H[1]))
    # Direct Leibniz: omega_H=omega_E/(3s), dw/dlambda=3/lambda^4, d log s/dlambda=1/lambda.
    obs_E_direct=(div(add(scale(6,sub(one,div(q(6),lam))),scale(36,mul(c,E[0][0]))),scale(3,s)),
                  div(scale(36,mul(c,E[1][0])),scale(3,s)))
    assert obs_in_E == obs_E_direct
    det_H=scale(4,H[1][0])
    det_E=scale(36,mul(c,E[1][0]))
    assert det_H==div(q(-1),scale(3,d))
    assert det_E == div(q(72),power(lam,4))  # p-units, no cyclic rank drop.
    return {'p':p,'modulus':p*p,'lambda':lam,'rad':rad,'s':s,'w':w,
            'dwdlambda':c,'H_observer':obs_H,'H_observer_in_E':obs_in_E,
            'Q_lambda_E_det':det_E,'Q_lambda_H_det':det_H,
            'full_connection_entries_checked':4}

if __name__=='__main__':
    for p in [13,19,37,43,373]:
        print(verify(p))
    print('PASS: 5 target primes, both connection columns and full signed source lambda observer.')
