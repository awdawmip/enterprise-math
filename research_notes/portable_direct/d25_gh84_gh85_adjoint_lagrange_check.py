#!/usr/bin/env python3
"""GH-84/85: exact characteristic-p adjoint/concomitant and root-separation checks.

Author-side, portable.  No native research session/run/checkpoint or H0/B0.
Pure Python standard library; all field operations are integer mod p.
"""

def primes_under(bound):
    sieve = bytearray(b'\x01') * bound
    sieve[:2] = b'\x00\x00'
    for d in range(2, int(bound ** 0.5) + 1):
        if sieve[d]:
            sieve[d * d:bound:d] = b'\x00' * len(range(d * d, bound, d))
    return (p for p in range(7, bound) if sieve[p] and p % 4 == 3)


def uv_coeffs(p):
    d = (p - 3) // 4
    c, h = [1], [1]
    for r in range(d):
        c.append(c[-1] * (4*r+1)**3 * pow((4*r+2)*(4*r+3)*(4*r+4), -1, p) % p)
        h.append(h[-1] * (4*r+3)**3 * pow((4*r+4)*(4*r+5)*(4*r+6), -1, p) % p)
    return c, h


def conv(a, b, p):
    out = [0] * (len(a)+len(b)-1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                out[i+j] += x*y
    return [x % p for x in out]


def exact_bilinear(c, h, p):
    # theta acts as i on the z^i coefficient.  All products retain full degrees.
    cs = [[pow(i, k, p) * x % p for i, x in enumerate(c)] for k in (0, 1, 2)]
    hs = [[pow(i, k, p) * x % p for i, x in enumerate(h)] for k in (0, 1, 2)]
    u_s2 = conv(hs[0], cs[2], p)
    u1_s1 = conv(hs[1], cs[1], p)
    u2_s = conv(hs[2], cs[0], p)
    u_s1 = conv(hs[0], cs[1], p)
    u1_s = conv(hs[1], cs[0], p)
    u_s = conv(hs[0], cs[0], p)
    b = [0] * (len(c)+len(h))  # degree <= 2d+1
    inv4, inv16 = pow(4, -1, p), pow(16, -1, p)
    for i in range(len(u_s)):
        base = u_s2[i] - u1_s1[i] + u2_s[i]
        b[i] += base - 3*inv4*u_s1[i] + 3*inv4*u1_s[i] + 2*inv16*u_s[i]
        b[i+1] += -base + inv4*u_s1[i] - 5*inv4*u1_s[i] - 7*inv16*u_s[i]
    return [a % p for a in b]


def at(poly, z, p):
    value = 0
    for coeff in reversed(poly):
        value = (value*z + coeff) % p
    return value


def verify_one(p):
    d = (p - 3) // 4
    c, h = uv_coeffs(p)
    inv = lambda q: pow(q % p, -1, p)
    # Test the entire differential operator coefficient sets, including the
    # terminal defect.  Scale fractions to integers to avoid float operations.
    for n in range(d+2):
        # theta(theta-1/2)(theta-1/4) = n(2n-1)(4n-1)/8;
        # numerator (theta+1/4)^3=(4n+1)^3/64.
        # Use scale 64 for both channels instead.
        original = (8*n*(2*n-1)*(4*n-1)*(c[n] if n<=d else 0)
                    -(4*n-3)**3*(c[n-1] if n>0 else 0))%p
        reflected = (8*n*(4*n+1)*(2*n+1)*(h[n] if n<=d else 0)
                     -(4*n-1)**3*(h[n-1] if n>0 else 0))%p
        # The left product coefficient must be scaled by 8, but the second by 1.
        # For original, (n-3/4)^3=(4n-3)^3/64.
        assert original == (8*c[-1] if n==d+1 else 0) % p, (p,n,'original',original)
        assert reflected == 0, (p,n,'reflected',reflected)
    # Full polynomial bilinear concomitant B and its independent integrated RHS.
    bpoly = exact_bilinear(c,h,p)
    want = [0]*len(bpoly)
    want[0] = inv(8)
    for j, value in enumerate(h):
        want[d+1+j] = c[-1]*inv(8)*value*inv(d+1+j) % p
    assert bpoly == want, (p,'bilinear',bpoly,want)
    # Field derivative check is distinct from the integrated coefficient check.
    assert [(i*bpoly[i])%p for i in range(1,len(bpoly))] == [0]*d + [(c[-1]*h[j]*inv(8))%p for j in range(d+1)]
    return (p,d,c[-1],at(bpoly,9,p))


def main():
    checked=[]
    for p in primes_under(2000):
        checked.append(verify_one(p))
    assert len(checked)==154, len(checked)
    # Special-fiber reduction, checked independently at every rational
    # H-zero for primes p<500.  It retains S, theta S and theta^2 S.
    fiber_count = 0
    double_count = 0
    separation_count = 0
    for p in checked:
        p = p[0]
        if p >= 500:
            continue
        c, h = uv_coeffs(p)
        U = h
        Hd = [(8*i+5)*v % p for i,v in enumerate(h)]
        T = [(8*i+1)*v % p for i,v in enumerate(c)]
        B = exact_bilinear(c,h,p)
        sc = lambda k: [(i**k)*v%p for i,v in enumerate(c)]
        thetaHd = [i*v%p for i,v in enumerate(Hd)]
        for a in range(2, p):
            if at(Hd,a,p)!=0:
                continue
            fiber_count+=1
            u=at(U,a,p)
            ss=at(c,a,p)
            s1=at(sc(1),a,p)
            s2=at(sc(2),a,p)
            hh1=at(thetaHd,a,p)
            rhs=((1-a)*u*s2 - (1+3*a)*pow(8,-1,p)*u*s1
                 + (1-a)*(hh1*pow(8,-1,p)+3*u*pow(64,-1,p))*ss)%p
            assert at(B,a,p)==rhs, (p,a,'fiber')
            if not u:
                double_count+=1
                assert at(B,a,p)==(1-a)*pow(8,-1,p)*hh1*ss%p
            if at(T,a,p):
                separation_count+=1
    assert fiber_count > 0 and double_count > 0 and separation_count > 0
    # The control counterexample is deliberately *not* z=9.
    p=11
    c,h=uv_coeffs(p)
    t=[(8*i+1)*v%p for i,v in enumerate(c)]
    H=[(8*i+5)*v%p for i,v in enumerate(h)]
    assert c==[1,6,4] and h==[1,6,9]
    assert t==[1,10,2] and H==[5,1,2]
    assert at(H,7,p)==0 and at(t,7,p)==4
    assert at(H,9,p)==0 and at(t,9,p)==0
    # Distinct roots at z=7 and z=9 are not implied to have the same
    # behavior for the source-finite truncation.
    print('PASS_GH84_ADJOINT_LAGRANGE 154 primes p<2000; exact polynomials through 2d+1')
    print('PASS_GH85_ROOT_SEPARATION p=11 z=7: H=0,T=4; z=9: H=0,T=0')
    print('PASS_GH85_SPECIAL_FIBERS',fiber_count,'H-roots',double_count,'simultaneous U-roots',separation_count,'H-root/T-nonzero controls')
    print('EXAMPLES (p,d,c_d,B(9)):', checked[:6])

if __name__=='__main__':
    main()
