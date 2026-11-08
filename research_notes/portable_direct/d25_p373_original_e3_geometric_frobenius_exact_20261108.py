#!/usr/bin/env python3
"""Original E3/F_(p^2) exhaustive geometric q-Frobenius certificate.

Author-side, exact finite field point enumeration; not divided-power H0/B0.
No reliance on CM sign formula, p-adic lifting, or prior point-count data.
"""


def original_e3(p):
    assert p in (13, 19, 373), 'fixed regression/domain for this certificate'
    assert pow(2, (p - 1)//2, p) == p - 1, 'T^2-2 must be irreducible'
    q = p*p
    inv108 = pow(108, -1, p)
    # E3: y^2 + xy + c y = x^3, c=(2-T)/108 in F_p[T]/(T^2-2).
    c0, c1 = 2*inv108 % p, -inv108 % p

    # Independent path B: explicitly enumerate the entire image of y -> y^2.
    square_set = {((a*a + 2*b*b) % p, (2*a*b) % p)
                  for a in range(p) for b in range(p)}
    assert len(square_set) == (q+1)//2

    # Path A: chi_{p^2}(d)=chi_p(N(d)), N(a+bT)=a^2-2b^2.
    chi_p = [0]*p
    for a in range(1, p):
        chi_p[a] = 1 if pow(a, (p-1)//2, p) == 1 else -1

    count_via_norm = q+1  # point at infinity + 1 per x
    count_via_squares = 1  # point at infinity
    zeros = []
    positive = negative = 0
    for a in range(p):
        a2, a3 = a*a, a*a*a
        for b in range(p):
            b2, b3 = b*b, b*b*b
            A, B = a+c0, b+c1
            # Discriminant of y^2+(x+c)y-x^3, x=a+bT.
            d0 = (A*A + 2*B*B + 4*(a3 + 6*a*b2)) % p
            d1 = (2*A*B + 4*(3*a2*b + 2*b3)) % p
            iszero = (d0 == 0 and d1 == 0)
            norm = (d0*d0-2*d1*d1) % p
            ch = chi_p[norm]
            assert (ch == 0) == iszero
            count_via_norm += ch
            roots = 1 if iszero else 2 if (d0,d1) in square_set else 0
            assert roots == 1+ch, (p,a,b,d0,d1,roots,ch)
            count_via_squares += roots
            if iszero:
                zeros.append((a,b))
            elif ch == 1:
                positive += 1
            else:
                negative += 1

    assert len(zeros) == 3
    assert positive+negative+len(zeros) == q
    assert count_via_norm == count_via_squares
    t = q+1-count_via_norm
    assert t == 2*p, (p,t)
    # Also check explicit order-three source point (0,0) with tangent y=0:
    # the line y=0 intersects E3 in x^3=0, hence (0,0) is a flex.
    return dict(p=p, q=q, c=(c0,c1), square_image_size=len(square_set),
                zeros=zeros, square_nonzero=positive, nonsquare=negative,
                character_sum=positive-negative, points=count_via_norm,
                expected=(p-1)**2, trace=t, frobenius_polynomial=(1,-2*p,q))


if __name__ == '__main__':
    for p in (13,19,373):
        print(original_e3(p))
    print('PASS: all finite x enumerated, two independent square tests agree; native H0/B0 NOT_EXECUTED')
