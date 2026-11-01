#!/usr/bin/env python3
"""GH-151: one ordinary CM trace anchor + an exact Picard--Fuchs recurrence.

Pure Python-stdlib exact arithmetic. Not the native D25 divided-power experiment.
"""
from math import comb

PRIMES = (11, 19, 43, 59, 67, 83, 107)


def lpow(a, p):
    a %= p
    if a == 0:
        return 0
    v = pow(a, (p - 1) // 2, p)
    return -1 if v == p - 1 else v


def count_trace_prime_field(p):
    """Independent integer count for E_(1/8) over F_p."""
    b = pow(8, -1, p)
    return -sum(lpow((x*x*x + x*x + b*x) % p, p) for x in range(p))


def ode_coefficients(p, normalization):
    assert p % 8 == 3 and p >= 11
    m = (p - 3) // 8
    out = [normalization % p]
    for k in range(m):
        numerator = 4 * (8*k + 1) * (8*k + 3) * out[-1]
        denominator = (k+1)*(2*k+1)
        out.append((numerator * pow(denominator, -1, p)) % p)
    return out


def eval_and_derivative(cs, w, p):
    v, d = 0, 0
    for c in reversed(cs):
        d = (w*d + v) % p
        v = (w*v + c) % p
    return v, d


def ode_residual_zero(cs, p):
    # (2W-256W²)G'' + (1-384W)G' -12G = 0
    maxdegree = len(cs)
    for k in range(maxdegree):
        c_next = cs[k+1] if k+1 < maxdegree else 0
        coefficient = ((k+1)*(2*k+1)*c_next
                       -4*(8*k+1)*(8*k+3)*cs[k]) % p
        if coefficient:
            return False, k, coefficient
    return True, None, None


def field_add(x, y, p):
    return ((x[0]+y[0])%p, (x[1]+y[1])%p)


def field_mul(x, y, p):
    return ((x[0]*y[0]+2*x[1]*y[1])%p,
            (x[0]*y[1]+x[1]*y[0])%p)


def field_inv(x, p):
    a, b = x
    den = pow((a*a-2*b*b)%p, -1, p)
    return ((a*den)%p, (-b*den)%p)


def field_char(x, p):
    a,b=x
    return lpow(a*a-2*b*b,p)


def direct_character_s1(p):
    # S_1(B) = sum_{x,g(x)!=0} chi(x)chi(g(x)) /g(x).
    b = (pow(8,-1,p),pow(12,-1,p))
    acc=(0,0)
    for a in range(p):
        for c in range(p):
            x=(a,c)
            x2=field_mul(x,x,p)
            g=field_add(field_add(x2,x,p),b,p)
            ch=field_char(x,p)*field_char(g,p)
            if ch:
                gi=field_inv(g,p)
                acc=((acc[0]+ch*gi[0])%p,(acc[1]+ch*gi[1])%p)
    return acc


def direct_hasse_at_b0(p):
    n=(p-1)//2
    B=(pow(8,-1,p),pow(12,-1,p))
    val=(0,0)
    bk=(1,0)
    for k in range(n//2+1):
        h=comb(n,2*k)*comb(2*k,k) % p
        val=field_add(val,((h*bk[0])%p,(h*bk[1])%p),p)
        bk=field_mul(bk,B,p)
    return val


def run():
    for p in PRIMES:
        a = count_trace_prime_field(p)
        cs=ode_coefficients(p,a)
        ok, k, val=ode_residual_zero(cs,p)
        assert ok,(p,k,val)
        w0=pow(144,-1,p)
        g, gd = eval_and_derivative(cs,w0,p)
        j, jd = g*g%p, 2*g*gd%p
        phi, phid = eval_and_derivative(ode_coefficients(p,1),w0,p)
        unsigned_anchor = a*a % p
        assert (j,jd)==((unsigned_anchor*phi*phi)%p,
                         (2*unsigned_anchor*phi*phid)%p)
        s1=(0, (jd*pow(12,-1,p))%p)
        s1_direct=direct_character_s1(p)
        hasse=direct_hasse_at_b0(p)
        assert (g,0)==hasse,(p,g,hasse)
        assert s1==s1_direct,(p,s1,s1_direct)
        print(f"P{p}_PASS",f"a_p={a}",f"m={(p-3)//8}",
              f"G_w0={g}",f"J_w0={j}",f"Jprime_w0={jd}",
              f"S1={s1}","DIRECT_CHARACTER_SUM_PASS","HASSE_PASS")
    p=3347
    a=count_trace_prime_field(p)
    assert a == -114, a
    cs=ode_coefficients(p,a)
    assert ode_residual_zero(cs,p)[0]
    w0=pow(144,-1,p)
    g,gd=eval_and_derivative(cs,w0,p)
    j,jd=g*g%p,2*g*gd%p
    phi,phid=eval_and_derivative(ode_coefficients(p,1),w0,p)
    unsigned_anchor=(a*a-2*p)%p
    assert (j,jd)==((unsigned_anchor*phi*phi)%p,
                    (2*unsigned_anchor*phi*phid)%p)
    s1coeff=jd*pow(12,-1,p)%p
    assert (w0,g,gd,j,jd,s1coeff)==(860,783,2824,588,997,362)
    hasse=direct_hasse_at_b0(p)
    assert hasse == (783,0),hasse
    print("P3347_PASS", f"independent_ap={a}",f"independent_a_p2={a*a-2*p}",
          f"G0={cs[0]}",f"m={(p-3)//8}",f"G_w0={g}",f"Gprime_w0={gd}",
          f"J_w0={j}",f"Jprime_w0={jd}",f"unsigned_anchor={unsigned_anchor}",f"S1=(0,{s1coeff})",f"reversed_orientation_S1=(0,{(-s1coeff)%p})",
          "DEPENDENT_HASSE_CROSSCHECK_PASS")
    print("PASS_GH151_GH152_ONE_CM_ANCHOR_AND_ORIENTED_JET_EXACT")

if __name__ == "__main__":
    run()
