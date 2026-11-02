#!/usr/bin/env python3
"""D25: exact modular verification of the Gauss deformation/Wronskian bridge.
No external packages, no GitHub network, original 216 coefficients kept distinct.
"""
import json
from math import isqrt


def primes_upto(limit):
    sieve = bytearray(b'\x01') * (limit + 1)
    sieve[:2] = b'\x00\x00'
    for t in range(2, isqrt(limit) + 1):
        if sieve[t]:
            sieve[t*t::t] = b'\x00' * ((limit - t*t)//t + 1)
    return [p for p in range(7, limit + 1) if sieve[p] and p % 6 == 1]


def compute(p):
    r = (p - 1)//6
    m = p*p
    inv2 = pow(2, -1, m)
    lp = [1]
    for k in range(r):
        lp.append(lp[-1] * (r-k)*(2*r-k) * pow((k+1)**2, -1, m) % m)
    hp = [1]
    ap = [1]
    for k in range(p-1):
        hp.append(hp[-1]*(6*k+1)*(3*k+1)*pow(18*(k+1)**2,-1,m)%m)
        ap.append(ap[-1]*(2*k+1)*(3*k+1)*(3*k+2)*pow(18*(k+1)**3,-1,m)%m)
    q = [0]
    for k in range(1, 2*r+1):
        source = ((k-1)*pow(2,-1,p)-2*r*pow(3,-1,p)) * (lp[k-1] % p) if k-1 <= r else 0
        q.append(((k-1-r)*(k-1-2*r)*q[-1]+source)*pow(k*k,-1,p)%p)
    for k in range(p):
        lhs = (hp[k] - (lp[k] if k<=r else 0)) % m
        assert lhs % p == 0
        assert lhs//p % p == (q[k] if k<=2*r else 0), ('deformation',p,k)
    a = [x%p for x in ap[:2*r+1]]
    wr = [0]
    for n in range(3*r):
        s = ((n*pow(4,-1,p)-2*r*pow(3,-1,p))*a[n])%p if n<=2*r else 0
        wr.append(((s-(3*r-n)*wr[-1])*pow(n+1,-1,p))%p)
    # Independent power-series evaluations of the two routes.
    def ev(coeffs, mod):
        z, zpow, val, deriv = pow(2,-1,mod),1,0,0
        for k,c in enumerate(coeffs):
            val=(val+c*zpow)%mod
            deriv=(deriv+k*c*zpow)%mod
            zpow=zpow*z%mod
        return val,deriv
    L, dL=ev(lp,m)
    H,dH=ev(hp,m)
    F,dF=ev(ap,m)
    Q,dQ=ev(q,p)
    Wr,_=ev(wr,p)
    assert Wr == ((L%p)*dQ - Q*(dL%p)) % p, ('Wr',p)
    assert (H*H-F)%m == 0 and (H*H+12*H*dH-F-6*dF)%m==0, ('Clausen',p)
    assert (F-L*L)%p==0 and (dF-2*L*dL)%p==0, ('R_A',p)
    q_R = (((F-L*L)%m)//p + 6*(((dF-2*L*dL)%m)//p))%p
    assert q_R == (2*(L%p)*Q + 12*((dL%p)*Q+(L%p)*dQ))%p, ('q_R',p)
    result={'p':p,'r':r,'L_modp':L%p,'j':dL%p,'Q_half':Q,'Wr_half':Wr,
            'R_A_weighted':q_R,'F_weighted_modp2':(F+6*dF)%m}
    if p%24 in (13,19):
        assert L%p==0, ('CM0',p)
        assert q_R==(-12*Wr)%p==12*(dL%p)*Q%p, ('CM-Wronskian',p)
        g=L//p %p
        u=H//p %p
        assert H%p==0 and (u-g-Q)%p==0
        carry=12*g*(dL%p)+q_R
        assert carry%p==12*(dL%p)*u%p
        assert (F+6*dF)%m==p*(carry%p), ('original-216',p)
        result.update({'g':g,'u':u,'second_carry':carry%p,'observed_target_one':carry%p==1})
    return result


def green_kernel_check(p):
    """Independent finite Green-kernel expansion, separate from the recurrence."""
    row = compute(p)
    r = (p - 1)//6
    fac = [1]
    for n in range(1, 3*r + 1):
        fac.append(fac[-1]*n%p)
    ifac = [pow(t, -1, p) for t in fac]
    a = [1]
    for k in range(2*r):
        a.append(a[-1]*(2*k+1)*(3*k+1)*(3*k+2)*pow(18*(k+1)**3,-1,p)%p)
    source = [((9*k+4)*pow(36,-1,p)*v)%p for k,v in enumerate(a)]
    omega = [0]
    for n in range(1, 3*r+1):
        val = 0
        for k in range(min(n,2*r+1)):
            w = fac[k]*fac[3*r-k-1]*ifac[n]*ifac[3*r-n]%p
            val += (1 if (n-k-1)%2==0 else -1)*w*source[k]
        omega.append(val%p)
    v = sum(t*pow(2,-n,p) for n,t in enumerate(omega))%p
    assert v == row['Wr_half'], ('finite_green',p,v,row['Wr_half'])
    return {'p':p,'green_kernel_value':v,'passed':True}


def main():
    ps=primes_upto(10000)
    samples=[7,13,19,31,37,43,373,1171,9967]
    data=[]
    for p in ps:
        data.append(compute(p))
    cm=[row for row in data if row['p']%24 in (13,19)]
    assert len(ps)==611, len(ps)
    assert len(cm)==312, len(cm)
    print(json.dumps({
        'scope':'p<=10000, prime p=1 mod6','all_primes':len(ps),
        'all_general_identity_checks':'PASS','cm_target_primes':len(cm),
        'cm_second_carry_one_finite_check':sum(x['observed_target_one'] for x in cm),
        'sample_rows':[x for x in data if x['p'] in samples],
        'independent_finite_green_checks':[green_kernel_check(p) for p in [7,13,19,31,37,43,373,1171]],
        'note':'Only algebraic bridge identities are proven. second_carry=1 is finite-tested, not a universal proof.'
    },ensure_ascii=False,indent=2))


if __name__=='__main__':
    main()
