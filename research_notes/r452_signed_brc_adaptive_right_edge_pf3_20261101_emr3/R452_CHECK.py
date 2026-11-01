#!/usr/bin/env python3
"""R452: exact, finite-s / infinite-k coefficient certificates for signed BRC.

Requires Python standard library only. No floating-point arithmetic.
For 2<=s<=100, k0=(s+2)//2, proves both local D2 and D3
have strictly positive coefficients in u=k-k0 >=0, after positive normalization.
The original signed convolution is independently sampled as input crosscheck.
"""
from math import comb, factorial
from hashlib import sha256
from fractions import Fraction
import json

S_MIN, S_MAX = 2, 100


def add(*ps):
    z = [0] * max(map(len, ps))
    for p in ps:
        for j, c in enumerate(p):
            z[j] += c
    while len(z) > 1 and z[-1] == 0:
        z.pop()
    return z


def mul(a, b):
    z = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                z[i+j] += x*y
    return z


def prod(*ps):
    z = [1]
    for p in ps:
        z = mul(z, p)
    return z


def B_numer(s, k0, F):
    """F*B_s(k0+u) using the proved E_s O_s R_s factorization."""
    if s < 2:
        return [0]
    assert F % factorial(2*s) == 0
    E,O=prefactors(s,k0)
    R=residual_R(s,k0)
    return [v*(F//factorial(2*s)) for v in prod(E,O,R)]


def B_numer_direct(s, k0, F):
    """Independent original signed-Catalan polynomial generation (slower)."""
    if s < 2:return [0]
    terms=[]
    for q in range((s-1)//2+1):
        p=[comb(s-1,2*q)*2**q]
        omit={-(2*t+1) for t in range(q)}
        for a in range(2-s,s+2):
            if a not in omit:p=mul(p,[2*k0+a,2])
        for d in range(q):p=mul(p,[k0+1-d,1])
        terms.append(p)
    return [v*(F//factorial(2*s)) for v in add(*terms)]


def cat(k):
    assert k >= 0
    return comb(2*k, k)//(k+1)


def H_positive(k, s):
    if s < 2 or s > 2*k+1:
        return 0
    r = 2*k+1
    return comb(r+s, 2*s) * sum(comb(s-1,2*q) * 4**q * cat(k-q)
        for q in range((s-1)//2+1))


def H_signed_raw(k, s):
    if s < 2 or s > 2*k+1:
        return 0
    r = 2*k+1
    d = r-s
    def choose(n, j):
        return comb(n,j) if 0 <= j <= n else 0
    return comb(r+s,2*s) * sum(comb(d,q) *
        (choose(2*s,r-2*q)-choose(2*s,r-2*q-1)) for q in range(d+1))


def at(poly, u):
    v = 0
    for c in reversed(poly):
        v = v*u+c
    return v


def append_positive(h, value):
    assert value > 0
    b = value.to_bytes(max(1, (value.bit_length()+7)//8), "big")
    h.update(len(b).to_bytes(4, "big"))
    h.update(b)


def residual_R(s, k0):
    """Numerator residual polynomial R_s(k0+u) in structural factorization."""
    m = (s-1)//2
    terms=[]
    for q in range(m+1):
        p=[comb(s-1, 2*q) * 2**q]
        for t in range(q,m):
            p = mul(p,[2*k0-(2*t+1),2])
        for d in range(q):
            p = mul(p,[k0+1-d,1])
        terms.append(p)
    return add(*terms)


def prefactors(s,k0):
    even = prod(*[[2*(k0+1-s//2+j),2] for j in range(s)])
    odd = prod(*[[2*k0+2*j+1,2] for j in range(s//2+1)])
    return even,odd


def main():
    digest = sha256()
    total_coeff=total_minor=0
    s_reports=[]
    input_checks=raw_checks=minor_checks=structural_checks=0
    sample_s={2,3,4,13,26,27,50,75,100}
    for s in range(S_MIN,S_MAX+1):
        if s%10==0: print("s",s,flush=True)
        k0=(s+2)//2
        F=factorial(2*(s+2))
        b={t:B_numer(t,k0,F) for t in range(s-2,s+3)}
        a,v,w,d,e=[b[s+j] for j in (0,-1,1,-2,2)]
        P2=add(mul(a,a),[-z for z in mul(v,w)])
        P3=add(prod(a,a,a),[-2*z for z in prod(v,a,w)],prod(d,w,w),
            prod(v,v,e),[-z for z in prod(d,a,e)])
        assert len(P2)==4*s+1 and len(P3)==6*s+1, (s,"degree")
        assert all(z>0 for z in P2), (s,2)
        assert all(z>0 for z in P3), (s,3)
        for order,p in ((2,P2),(3,P3)):
            digest.update(bytes((s,order)))
            digest.update((len(p)-1).to_bytes(2,"big"))
            for z in p:
                append_positive(digest,z)
            total_coeff+=len(p)
            total_minor+=1
        # Independent factorization identity E_s*O_s*R_s = (2s)! B_s
        # checked symbolically for three neighboring s; m<=k0 for physical input.
        for t in ((s-1,s,s+1) if s in sample_s else ()):
            if t<2:continue
            E,O=prefactors(t,k0)
            R=residual_R(t,k0)
            lhs=prod(E,O,R)
            # Integer-safe equality: multiply both sides by F; divide by (2t)! afterwards.
            assert [x*(F//factorial(2*t)) for x in lhs]==b[t],(s,t,"factorization")
            assert b[t] == B_numer_direct(t,k0,F),(s,t,"independent original polynomial")
            assert all(x>0 for x in residual_R(t,(t-1)//2)),(s,t,"residual positivity")
            structural_checks+=1
        # Exact original signed convolution, independent from polynomial construction.
        if s in sample_s:
            for k in (k0,k0+1):
                coeff=cat(k)
                for t in range(s-2,s+3):
                    if t<2:continue
                    assert at(b[t],k-k0)*coeff==F*H_positive(k,t), (s,k,t,"B=Catalan")
                    assert H_positive(k,t)==H_signed_raw(k,t), (s,k,t,"signed")
                    input_checks+=1
                    raw_checks+=1
                x,y,z,w0,v0=[H_signed_raw(k,s+j) for j in (0,-1,1,-2,2)]
                D2=x*x-y*z
                D3=x**3-2*y*x*z+w0*z*z+y*y*v0-w0*x*v0
                assert D2>0 and D3>0, (s,k,"direct positivity")
                assert at(P2,k-k0)*coeff**2 == F**2*D2,(s,k,2,"minor")
                assert at(P3,k-k0)*coeff**3 == F**3*D3,(s,k,3,"minor")
                minor_checks+=2
        s_reports.append({"s":s,"k0":k0,"r_min":2*k0+1,"positive_coefficients":len(P2)+len(P3),"min_sign":1})
    assert total_coeff==50688 and total_minor==198
    result={"result":"R452_EXACT_PASS","s_range":[S_MIN,S_MAX],
      "r_condition":"r=2k+1, k >= (s+2)//2, j=r-s", 
      "positive_polynomials":total_minor,"positive_coefficients":total_coeff,
      "factorization_checks":structural_checks,
      "input_catalan_checks":input_checks,"independent_signed_checks":raw_checks,
      "direct_exact_minor_checks":minor_checks,
      "coefficient_stream_sha256":digest.hexdigest(),"coefficient_encoding":
      "for s increasing 2..100 and order=2,3: uint8(s),uint8(order),uint16_be(degree), each strictly positive coefficient ascending: uint32_be(byte_length),unsigned_minimal_be"}
    print(json.dumps(result,ensure_ascii=False,indent=2))
    with open('R452_EVIDENCE.json','w',encoding='utf-8') as f:
        json.dump({**result,'rows':s_reports},f,indent=2,ensure_ascii=False)
        f.write('\n')

if __name__=='__main__':main()
