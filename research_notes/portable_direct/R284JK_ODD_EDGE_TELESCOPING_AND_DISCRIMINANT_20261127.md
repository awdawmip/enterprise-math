# R284JK — Odd-edge exact endpoint carrier and endpoint-independent discriminant certificates
2026-11-27. Author proof and exact rational replay; NOT_REVIEWED. Auxiliary binary-tag arithmetic observer, not a native spatial/dynamical transfer. Existing own activity RA-B82240E8488EF5A1DA5186C4, EM-DIRECT-0C386E / TASK_RESEARCH. Own session recovery r1-20261127-1304-recovery confirms original registered unclosed researcher session, no runs; owner inventory r1-20261127-1304-owner was RUNNING at the last check before publication; no shared Task/CLAIM or owner mutation. P000 V5, ACTIVE worldview, joint/residual and portable contracts consulted. Frozen science: JJ fe21b1a48ffccb3c00640e7d3e2afe6b6b2ba9e1:research_notes/portable_direct/R284JJ_SECOND_BRANCH_EDGE_MOMENT_COMPRESSION_20261127.md (blob 92c42055a68b97821a60c173c9c1824a68146a76), and JI 6fb5c31543931e0ffe548c53feedad30b1b0926b:research_notes/portable_direct/R284JI_FULL_SECOND_BRANCH_WINDOW_POSITIVITY_20261127.md. Use their exact joint observer and pole/regular edge reductions without changing primal inputs.

## 1. A diagonal finite-difference transform with a retained endpoint
Let r,d be integers, 3<=r<=d, j=d-r, w=(r-2)/2, b=2j+2, and assume 2j+4<r. Put t_k=(-1)^k R_w(k), R_w(k)=prod_{i<k}(w-i)/(w+i+3); thus t_0=1 and t_(k+1)=t_k(k-w)/(k+w+3). Define the rising factorial P_h(k)=(k-w)^(overline h), P_0=1. Direct multiplication gives the exact telescoping identity
 (k+w+3)t_(k+1)P_h(k+1)-(k+w+2)t_k P_h(k)
 = (h-2w-2)t_k P_h(k).
This follows from (k-w)P_h(k+1)=(k-w+h)P_h(k), and holds even where t_k is zero. Since 2w+2=r, for 0<=h<r one obtains
 sum_{k=0}^r t_k P_h(k)
 = [(r+w+3)t_(r+1)P_h(r+1)-(w+2)P_h(0)]/(h-r).
No infinite limit or tail deletion is involved. The resonance h=r is deliberately excluded.

For any polynomial W(k) of degree m<r, define a_h=(-1)^h Delta^h[W(w-i)]_(i=0)/h!, the forward difference in integer i. Newton interpolation gives W(k)=sum a_h P_h(k) (evaluate at k=w-i, where P_h=(-1)^h i falling h). Consequently the complete weighted sum is L(W)+B(W) T, where T=t_(r+1) and
 L(W)=-(w+2) sum_{h=0}^m a_h(-w)^(overline h)/(h-r),
 B(W)=(r+w+3) sum_{h=0}^m a_h(r+1-w)^(overline h)/(h-r).
Both coefficients are exact. This is a scope-typed joint carrier; the endpoint is retained rather than replaced with zero.

## 2. Simultaneous exact compression of V,Q,A and the cross residual
Use JJ/JI notation q0=w-d, sign s=(-1)^r, Z=q0 A+Q+V, E*=0 at this layer, G=3q0(4q0+3d+1)^2 A Q-32(3q0+d+1) Z^2. For integer a>=2 let
 W_(n,a)(k)=(k+1)[binom(n-k+a-1,a-1)+binom(n-k+a-2,a-1)],
 where binom(z,h) means its polynomial in z (h>=0).
The coefficient kernel K(w,a,n) from JI is sum_{k=0}^n t_k W_(n,a)(k). For n=r-1,a=b+1 the extra k=r term is zero, so all sums may run through r. The exact B_k=v_k R_w(k) identity from JH gives
 W_A(k)=W_(r,b)(k)(w-k)(w+k+2)/(2w(2w+1)).
Indeed B_k=B0 R_(w-1)(k), and the rational recurrence yields the stated v factor (valid at this w>0); for integer w the product zeros remain valid. Thus the three observer pairs are
 (V0,V1)=s(j+1)(L(W_(r,b+1)),B(W_(r,b+1))),
 (Q0,Q1)=-s(j+1)(L(W_(r-1,b+1)),B(W_(r-1,b+1))),
 (A0,A1)=s(j+1)(L(W_A),B(W_A)).
Their degrees are <=b+1,b+1,b+2 respectively; by the hypothesis all are <r. EXACTLY V=V0+V1 T, Q=Q0+Q1 T, A=A0+A1 T, with Z similarly affine. In particular G=g0+g1 T+g2 T^2, obtained by ordinary multiplication of these three pairs, retaining all cross terms. The same identity holds for integer and half-integer w; for even r the endpoint is exactly zero, recovering JJ's type of endpoint-free observer. For odd r=2s0+3, w=s0+1/2, T is nonzero and has exact double-factorial expression
 T=(-1)^(s0+1) (2s0+1)!! [(2s0+5)!!]^2/(6s0+13)!!.
This is obtained by separating the negative odd factors in numerator prod_{k=0}^r(2k-2w) and cancelling the odd denominator prefix; it can be evaluated as the original ratio product. Here !! denotes the product of positive odd integers through its argument.

Constructing all six affine coefficients by difference rows takes O((j+1)^2) rational or field arithmetic operations, including evaluating the consecutive-product binomial polynomials at O(j+1) nodes (direct O(j+1) products each). For fixed j their bit lengths are O_j(log d); uniformly an O((j+1)log d) upper bound follows from common denominators: factorials up to m!, powers of 2 with exponent O(m), the v denominator, and prod_{h=0}^m(r-h), plus numerator magnitudes d^O(m+1). In this estimate one may use m!^2 to clear the binomial and Newton factorials simultaneously. All these denominator prime factors are <=4d+6. T itself can have O(d)-scale bit length; the direct product uses O(r) field operations, not O(j^2). Thus this is a low-height coefficient carrier with one retained endpoint, NOT a claim of full odd-edge rational-height compression or a sublinear general exact evaluation.

## 3. A genuinely endpoint-independent non-equality certificate
At any valid primal q>=64,d^2<=4q, and p>4d+6 dividing N=2q+2d-r+2, the JG/JI normalized C/T_pole^2 residue (or JJ's regular edge C for r=d) equals G mod p; T_pole is the original normalization, distinct from the endpoint T here. All new coefficient denominators and T's factors are p-units: 2, m!, r-h, the factors from w and 2w+1, and the endpoint denominator factors after clearing 2 (maximum 3r+4) are less than p. Thus the equality Y=32/3 implies
 g2 T^2+g1 T+g0=0 in F_p.
If g2 !=0 in F_p and Delta=g1^2-4g2*g0 is a quadratic nonresidue, the equation has no root in F_p; hence Y!=32/3 without evaluating the endpoint. If g2=g1=0 and g0!=0, the same conclusion holds. This uses the full joint cross residual, including Z^2, and works even if its denominator-leading observation vanishes. The quadratic nonresidue check costs O(log p) field multiplications by Euler's criterion. Given p, total certificate check is O((j+1)^2+log p) field operations, excluding prime discovery and bit costs. No claim that every p passes this sufficient test. If it fails, retain T and evaluate or use other certificates. For fixed j, g_i are rational functions of d (r=d-j), so this is a bounded-degree polynomial character criterion independent of the potentially long odd endpoint product.

For j=0, direct finite-difference evaluation gives the following unsigned (L,B) pairs (multiply by s for V,A and -s for Q):
 V: ((w+2)(8w^3+28w^2+15w-17)/(2(2w-1)(2w+1)), -(w+3)(3w+5)(8w^2+31w+32)/(2w(2w-1)(2w+1))).
 Q: ((w+2)(8w^3+20w^2+5w-10)/(2(2w-1)(2w+1)), -(3w+4)(3w+5)(8w^2+23w+18)/(2w(2w-1)(2w+1))).
 A: ((w+1)(w+2)(4w+7)/(4(2w-1)(2w+1)), -(w+3)(3w+4)(3w+5)(8w^2+27w+25)/(4w(w-1)(2w-1)(2w+1))).
For r=d>=5, formal substitution into the residual gives
 Delta=3 (w+2)^6 (2w+3)^2 (3w+5)^2 J(w)/(16 w^2 (w-1)^2 (2w+1)^4),
 J(w)=6912w^10+85824w^9+360780w^8-211540w^7-7999145w^6-35199250w^5-81683197w^4-115108448w^3-99980896w^2-50149632w-11369472.
This identity can be checked by expanding the three pairs and computing g1^2-4g0g2, as in the general formula. Since all displayed square factors are units for p>4d+6, a nonresidue 3J(w) alone suffices on this edge (it forces Delta!=0; if g2=0 then Delta=g1^2, contradiction). This gives a fixed-degree sufficient test for the odd far edge, without computing any long product.

## 4. Exact replay and limits
Executed Python Fraction: 551 eligible (d,r) cases 5<=d<=60 with 2(d-r)+4<r, 280 odd and 271 even, all three affine observations matched original signed sums and G>0. Endpoint zero iff even r in this domain. Separately, for 5<=d<=100, odd r>=5, j<=8 and 2j+4<r, tested every prime 4d+6<p<1000: 44,652 formal modular pairs, 22,104 endpoint-independent nonzero certificates, 105 actual zero residues; for j=0, 5,854 pairs and 2,894 endpoint-independent certificates. The discriminant tests all implied actual nonzero residue. These are formal residue checks at (d,r,p), not 44,652 distinct primal budgets; a primal certificate still needs p|N. SymPy exact symbolic calculation of edge pairs and discriminant used finite differences, evaluation of G at 0,+1,-1 to obtain coefficients, then rational factorization. No density or independence extrapolation. Full budget non-equality, real inverse-polynomial separation and stronger joint exceptional-prime counting remain open. Next: combine the discriminant filter with the third window and assess joint exception compatibility; explore the resonant degree h=r and whether the remaining endpoint square class supplies another sufficient test.

## Replay code
```python
from fractions import Fraction as F
from math import comb,factorial
from sympy import primerange
def rise(x,h):
    v=F(1)
    for i in range(h):v*=x+i
    return v
def bc(x,h):return rise(x-h+1,h)/factorial(h)
def split(w,r,P,m):
    assert m<2*w+2
    row=[P(w-i) for i in range(m+1)]
    A=B=F(0);a=b=F(1)
    for h in range(m+1):
        c=(-1)**h*row[0]/factorial(h)
        A-=c*(w+2)*a/(h-2*w-2)
        B+=c*(r+w+3)*b/(h-2*w-2)
        row=[y-x for x,y in zip(row,row[1:])]
        a*=h-w;b*=r+1-w+h
    return A,B
def carrier(d,r):
    assert 3<=r<=d and 2*(d-r)+4<r
    j=d-r;w=F(r-2,2);b=2*j+2;s=(-1)**r
    def W(n,a,k):return (k+1)*(bc(n-k+a-1,a-1)+bc(n-k+a-2,a-1))
    ps=[(lambda k:W(r,b+1,k),b+1),(lambda k:W(r-1,b+1,k),b+1),(lambda k:W(r,b,k)*(w-k)*(w+k+2)/(2*w*(2*w+1)),b+2)]
    return [(sgn*(j+1)*a,sgn*(j+1)*b0) for (P,m),sgn in zip(ps,[s,-s,s]) for a,b0 in [split(w,r,P,m)]]
def end(w,r):
    t=F(1)
    for k in range(r+1):t*=(k-w)/(k+w+3)
    return t
def direct(d,r):
    u=F(r-2,2);j=d-r;U=F(1);B=(u+2)/(2*(2*u+1));V=Q=A=F(0)
    for k in range(r+1):
        h=r-k;l=d-k;c=(-1)**h*comb(2*j+h+1,h)
        a=(k+1)*(l+1)*c
        b=(k+1)*l*(-1)**(h-1)*comb(2*j+h,h-1) if h else 0
        V+=U*a;Q+=U*b;A+=B*(a+b)
        U*=(u-k)/(u+k+3);B*=(u-k-1)/(u+k+2)
    return V,Q,A
def G(d,r,V,Q,A):
    q=F(r-2,2)-d;Z=q*A+Q+V
    return 3*q*(4*q+3*d+1)**2*A*Q-32*(3*q+d+1)*Z**2
def quadratic(d,r,pairs):
    z,p,m=[G(d,r,*(a+b*t for a,b in pairs)) for t in (0,1,-1)]
    return z,(p-m)/2,(p+m)/2-z
def mod(x,p):return x.numerator*pow(x.denominator,-1,p)%p
cnt=odd=even=0
for d in range(5,61):
    for r in range(5,d+1):
        if 2*(d-r)+4>=r:continue
        pairs=carrier(d,r);t=end(F(r-2,2),r);obs=tuple(a+b*t for a,b in pairs)
        assert obs==direct(d,r) and G(d,r,*obs)>0
        cnt+=1;odd+=r%2;even+=1-r%2
        assert (t==0)==(r%2==0)
print(cnt,odd,even)
tests=certs=zero=edge_tests=edge_certs=0
for d in range(5,101):
    for r in range(5,d+1,2):
        if 2*(d-r)+4>=r or d-r>8:continue
        pairs=carrier(d,r);t=end(F(r-2,2),r);c,b,a=quadratic(d,r,pairs);disc=b*b-4*a*c
        assert G(d,r,*direct(d,r))==c+b*t+a*t*t
        for p0 in primerange(4*d+7,1000):
            p0=int(p0);am,bm,cm,dm=map(lambda x:mod(x,p0),(a,b,c,disc))
            y=mod(t,p0);val=(am*y*y+bm*y+cm)%p0
            assert val==mod(G(d,r,*(a0+b0*t for a0,b0 in pairs)),p0)
            cert=(am!=0 and pow(dm,(p0-1)//2,p0)==p0-1) or (am==bm==0 and cm!=0)
            if cert:assert val!=0
            tests+=1;certs+=cert;zero+=val==0
            if d==r:edge_tests+=1;edge_certs+=cert
print(tests,certs,zero,edge_tests,edge_certs)
```
