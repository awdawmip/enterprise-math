#!/usr/bin/env python3
"""W216 finite diagonal carry certificate: two exact p-adic arithmetic paths."""
from __future__ import annotations

def strip(n: int, p: int) -> tuple[int, int]:
    assert n > 0
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return n, v

def scalar_at_scales(p: int, rmax: int, digits: int, method: str) -> dict[int, int]:
    e = 3*rmax + digits
    modulus = p**e
    inv216 = pow(216, -1, modulus)
    scales = {p**r: r for r in range(1, rmax+1)}
    n, total = p**rmax, 0
    powers = [p**j for j in range(e)]
    out = {0:1}
    if method == "recurrence":
        unit, val = 1, 0
        inv36 = pow(36, -1, modulus)
        for k in range(n):
            if val < e:
                total = (total + (6*k+1)*unit*powers[val]) % modulus
            if k+1 in scales: out[scales[k+1]] = total
            top, vt = strip((2*k+1)*(3*k+1)*(3*k+2), p)
            bot, vb = strip(k+1, p)
            val += vt - 3*vb
            assert val >= 0
            unit = unit*top*pow(bot, -3, modulus)*inv36 % modulus
    elif method == "factorials":
        f1_inv = f2 = f3 = power216 = 1
        v1 = v2 = v3 = 0
        for k in range(n):
            val = v2+v3-5*v1
            assert val >= 0
            if val < e:
                coeff = f2*f3 % modulus
                coeff = coeff*pow(f1_inv, 5, modulus)*power216 % modulus
                coeff = coeff*powers[val] % modulus
                total = (total + (6*k+1)*coeff) % modulus
            if k+1 in scales: out[scales[k+1]] = total
            x,v = strip(k+1,p)
            f1_inv = f1_inv*pow(x,-1,modulus)%modulus
            v1 += v
            for t in (2*k+1,2*k+2):
                x,v=strip(t,p)
                f2=f2*x%modulus
                v2+=v
            for t in (3*k+1,3*k+2,3*k+3):
                x,v=strip(t,p)
                f3=f3*x%modulus
                v3+=v
            power216=power216*inv216%modulus
    else: raise ValueError(method)
    assert len(out)==rmax+1
    return out

def E_array(p: int, R: int, digits: int, method: str) -> list[int]:
    W=scalar_at_scales(p,R,digits,method)
    chi=1 if p%3==1 else -1
    E=[]
    for r in range(1,R+1):
        d=(W[r]-chi*p*W[r-1])%p**(3*r+digits)
        assert d%p**(3*r)==0
        E.append(d//p**(3*r))
    return E

def main() -> None:
    expected = {
        13: (5,5,[300777,331470,146077,335019,192214],8),
        19: (5,5,[726059,572843,2024063,2360154,1317586],11),
        37: (3,3,[45714,32357,44678],9),
        43: (3,3,[34548,8834,16230],4),
        61: (3,3,[115724,132682,32215],34),
        67: (3,3,[30875,265442,40992],17),
    }
    for p,(R,d,expected_E,delta) in expected.items():
        e=E_array(p,R,d,"recurrence")
        other=E_array(p,R,d,"factorials")
        assert e==other==expected_E
        assert (e[1]-e[0])%p==0
        for r in range(1,R):
            residual=(e[r]-e[r-1])%p**(r+1)
            assert residual==delta*p**r, (p,r,residual,delta)
        print("PASS",p,"R",R,"delta",delta,"E",e)
    print("22 finite scale points, 16 exact diagonal transitions; NOT a universal theorem")

if __name__ == "__main__":
    main()
