# R284JJ — Second-branch edge certificate and two-ended moment height compression
2026-11-27. Author proof and exact rational replay; NOT_REVIEWED. Auxiliary binary-tag joint observer, not a native spatial transfer. Existing independent activity RA-B82240E8488EF5A1DA5186C4; own EM-DIRECT-0C386E / TASK_RESEARCH session recovered, registered, unclosed, no runs; no shared CLAIM. Owner inventory r1-20261127-1200-owner SUCCEEDED, as-of 2026-11-27T04:00:21.594245Z, no LEASED entries; source f967687c43633b462331ac72623622dffbccaa61 unchanged through completion. P000 V5, ACTIVE worldview, portable and joint/residual contracts consulted. Frozen scientific inputs: JI 6fb5c31543931e0ffe548c53feedad30b1b0926b:research_notes/portable_direct/R284JI_FULL_SECOND_BRANCH_WINDOW_POSITIVITY_20261127.md (blob bfa2394c440c20adba2aaa2334171bc647ec2f9e); JG c7853ca73cbf8d3c4e85fd3810293d63a485c000:research_notes/portable_direct/R284JG_SECOND_BRANCH_GROWING_OFFSET_CERTIFICATES_20261127.md (blob dcea8958112dba93dbebe4486896cdea090b5905). Both read in full. Previous positivity is reused at its exact scope.

## 1. Regular edge r=d, previously outside the pole theorem
Retain JG's primal q>=64, d>=2, d^2<=4q, u=q+d, m=2q+d, R_w(k)=prod_{i<k}(w-i)/(w+i+3). With l=d-k, a=(k+1)(l+1)R_u(k)R_m(l), b=(k+1)l R_u(k)R_m(l-1) (zero when l=0), v=(u-k)(u+k+2)/(2u(2u+1)), V=sum a,Q=sum b,A=sum v(a+b). The endpoint residual simplifies exactly to E=R_u(d)(u-d)(2d+3)(m+2)/(2(2u+1)(4m+2)). Z=qA+Q+V; C=3q(4q+3d+1)^2(A+E)Q-32(3q+d+1)Z^2; Y=qK, Y=32/3 implies C=0.
At r=d>=3 let N=2q+d+2, q0=-(d+2)/2, u0=(d-2)/2, m0=-2. For p|N,p>4d+6 every denominator of the full observer is a unit at q0 (clear factors of 2 first; all resulting factors have magnitude <=4d+6); u0>0. Here no internal pole is present, T=1. R_{-2}(h)=(-1)^h(h+1) by the consecutive-product identity. E(q0)=0 from m0+2, not a claim about the primal residual. All six full observations reduce mod p to the same formulas as JI with j=0, c_h=(-1)^h(h+1), b=2, and hence C mod p equals G2_d(d). No pole normalization is necessary. The full source is retained for higher jets.
JI's exact generating identities extend to j=0 algebraically (the same coefficient weighting of (1-x)^(-2)). Its positivity lemma applies to both indices of each K: w=u0 or u0-1>=-1/2; a>=2; r-2>u0. Therefore (-1)^r V, (-1)^(r-1) Q, (-1)^r A and (-1)^r(V+Q) are positive. Since q0<0, 3q0+d+1<0 and 4q0+3d+1=d-3, G>0 for d>=4. At d=3, direct exact sums give V=-1018/77,Q=164/21,A=-523/84,Z=6255/616,G=39125025/3388>0. Thus every edge d>=3 has a nonzero rational certificate. If G mod p is nonzero, Y!=32/3. This extends JI by one regular boundary, not a new pole.

## 2. Exact joint moment transform for even r
Take even 4<=r<=d, j=d-r, w=(r-2)/2 integer>=1, b=2j+2. Define F_w(x)=sum (k+1)(-1)^k R_w(k)x^k. For integer w>=0 it is a polynomial of degree w. Define M_h(w)=(-1)^h F_w^(h)(1)/h!, 0<=h<=w, zero otherwise. From JI's Beta integral (differentiate polynomial under integral),
M_h(w)=(w+1)(w+2) binom(w,h) integral_0^1 t^(h+1)(1-t)^(2w-h) dt
=(w+1)(w+2) binom(w,h)/[(h+2) binom(2w+2,h+2)].
These are strictly positive. For a>=2, n>w and n>=1, exact Taylor expansion around x=1 gives
K(w,a,n)=[x^n](1+x)(1-x)^(-a)F_w(x)
=sum_{h=0}^{min(w,a-1)} M_h(w) [binom(n+a-h-1,a-h-1)+binom(n+a-h-2,a-h-1)].
Indeed terms h>=a are polynomials of degree <=w-a+1<n, so contribute EXACTLY zero to this observer. This is a scope-typed compression of the signed branch polynomial, not a positive-mass approximation; no deletion for other observations/higher jets. JI's identities (now also valid at j=0):
V=(j+1)K(w,b+1,r), Q=-(j+1)K(w,b+1,r-1),
A=(j+1)B0 K(w-1,b,r), B0=(w+2)/(2(2w+1)),
E*=0, Z=(w-d)A+Q+V, G=3(w-d)(4(w-d)+3d+1)^2 A Q-32(3(w-d)+d+1)Z^2.
Only O(min(r,j+1)) moments are required. M0=(w+2)/(2(2w+1)), M_(h+1)/M_h=(h+2)(w-h)/[(h+1)(2w-h)]; binomial weights can also be generated consecutively in O(min(r,j+1)) steps (initialize with a binomial computed by a short product when j is small). Given p>4d+6, all denominators are units. For j fixed the near-edge observer uses O(j+1) field steps and arithmetic bit lengths O_j(log d) in exact rational evaluation; prime discovery cost not included. General modular implementation can choose direct branch sum when a is large.

## 3. Two-ended integerization and exceptional resource bound
Let L(H)=lcm(1,...,H), H(w,a)=min(w,a-1)+2, D(w,a)=binom(2w+2,H) L(H)^2. For 2<=k<=H, binom(2w+2,k) divides binom(2w+2,H) binom(H,k) by the nested binomial identity. And binom(H,k)|L(H): the factorial valuation is a sum of at most floor(log_p H) carries, each <=1. Since also k|L(H), D(w,a) clears M_h for all relevant h. Then
D=2(2w+1) D(w,b+1) D(w-1,b)
clears V,Q,A,E*,Z,W*. All its prime factors are <=2w+2=r except for no new prime from the factor 2. Thus P=D^2 G is a strictly positive integer by JI and section 1, and p>4d+6 never divides D.
Use log L(H)=O(H) (elementary Chebyshev bound), log binom(n,H)<=H log(en/H). Since H<=2j+4 and H<=d, log D=O((j+1)log(ed/(j+1))+log d). The bound is uniform including j=0. In JI's original signed sums |U_k|<=1, |B_k|<=1, |c_h|<=|c_r|=binom(d+j+1,2j+1); the latter is <=(e(d+j+1)/(2j+1))^(2j+1). Each of V,Q,A is O(d^3 |c_r|); Z=O(d^4 |c_r|), G=O(d^9 |c_r|^2). Hence
log P=O((j+1)log(ed/(j+1))+log d).
Combined with JI/JG's r-end height, this supplies a two-ended bound for even interior r:
O(log d+min{r log(ed/r),(j+1)log(ed/(j+1))}) for an integerization with unit denominator at p>4d+6 (choose either proven carrier).
Number of exceptional large primes <= log P/log(4d+6) = O(1+(j+1)log(ed/(j+1))/log d). In particular, for every fixed distance j from the far edge and even r=d-j, only O(j+1) exceptional large primes, whereas the earlier r-end bound alone was O(d/log d). For fixed j the moment formulas are explicit rational functions of d of bounded degree O(j+1); no claim about odd-offset moment truncation. At odd r the infinite signed generating tail must be retained.

## 4. Even edge explicit polynomial and constant exception count
For even d>=6, j=0,w=(d-2)/2>=2. The first three moments give K(w,2,n)=(2n+3)B0 and K(w,3,n)=B0[(n+2)^2-(w+1)/(2w-1)], while K(w-1,2,n)=(2n+3)(w+1)/(2(2w-1)). In particular
V=(d+2)(2d^3+2d^2-17d-24)/(8(d-3)(d-1)),
Q=-(d+2)(2d^3-2d^2-11d-6)/(8(d-3)(d-1)),
A=d(d+2)(2d+3)/(16(d-3)(d-1)),
Z=-(d+2)(2d+3)(d^2-6d+24)/(32(d-3)(d-1)).
Substituting in C at q0 gives
G=(d+2)^2(2d+3) H7(d)/(256(d-3)^2(d-1)^2),
H7(d)=6d^7-22d^6-79d^5+432d^4+879d^3-4572d^2+11196d+27648.
G>0 implies H7>0. For d>=6, triangle bound divided by d^7 is <=6+22/6+79/6^2+432/6^3+879/6^4+4572/6^5+11196/6^6+27648/6^7<16. Thus H7<(4d+6)^7, and at most six distinct primes >4d+6 divide it. At p|2q+d+2, p>4d+6, p not dividing H7(d) suffices to certify Y!=32/3. For d=4 the special values V=17,Q=-23/2,A=9/2,Z=-8,G=34631/4 apply, not the d>=6 formula.

## 5. New complementary short window, same local exception order
For fixed large d and q in any interval I of length O(d), q comparable to d^2 and primal legal, choose even r=d-j, j of parity d, 0<=j<=2h+1 with exactly h consecutive such offsets, h=ceil(C0 d/log d) for sufficiently large fixed C0. Then N/2=q+(d+j)/2+1 gives h consecutive integers near q+d/2. This differs by order d from the earlier r-small first/second windows near q+2d and q+d. Take B=C d>4d+6 and B^2>=max N/2 throughout the q range; h<B. In each window of h consecutive integers ending at n, the exact binomial product has large prime portion prod_{P^+(a)>B} P^+(a), with one large prime per a, no repeats across a; small prime portion <=n^pi(B) by factorial carry bounds. Thus the number of large-prime witnesses is >=log binom(n,h)/log n-pi(B)>=h/2-o(h)-O(d/log d), hence Omega(h) for all these q by elementary prime-count upper bound. For fixed j the exceptional large primes are counted in section 3; each p>B gives O(1) q in I by its single congruence on N/2. Sum over the h offsets: O(h+h^2 log(ed/h)/log d) bad incidences. Dividing by a fixed positive fraction of the witness count gives at most O(1+h log(ed/h)/log d)=O(d log log d/log^2 d) q with insufficient survivors. Every other q has Omega(d/log d) surviving far-edge certificates. This is a third window of the same local exception order; no independence or smaller intersection asserted. Full equality exclusion and real inverse-polynomial separation remain open.

## 6. Exact replay
Executed Python Fraction and SymPy primerange: 118 formal edge cases d=3..120 against original observer at q0, even edge polynomial checked for d>=6; 3481 even (d,r) cases d=4..120, even r=4..d, comparing the moment transform to direct signed sums and checking integerization and positivity; 1736 legal primal modular cases d=3..34, p from 4d+7 to 349, N in {p,2p,p^2}, parity and domain filters, all six observations checked, 11 zero residues (not equality). Five large near-edge cases (d,j; D bits,P bits): (1000,0;86,228), (1000,10;454,1234), (10000,20;1066,2946), (10^30,20;8667,25576), (10^60,10;9544,28125). Large cases use only moments, not full branch enumeration. All assertions passed. Analytic proof bears unbounded conclusions.

```python
from fractions import Fraction as F
from math import comb,lcm

def rr(w,n):
    w=F(w); a=[F(1)]
    for k in range(n): a.append(a[-1]*(w-k)/(w+k+3))
    return a

def reduced(d,r):
    u=F(r-2,2); q=u-d; j=d-r
    c=[(-1)**h*comb(2*j+h+1,h) for h in range(r+1)]
    U=rr(u,r); B=[(u+2)/(2*(2*u+1))]
    for k in range(r): B.append(B[-1]*(u-k-1)/(u+k+2))
    V=Q=A=F(0)
    for k in range(r+1):
        l=d-k; h=r-k
        a=(k+1)*(l+1)*c[h]; b=(k+1)*l*c[h-1] if h else 0
        V+=U[k]*a; Q+=U[k]*b; A+=B[k]*(a+b)
    Z=q*A+Q+V; G=3*q*(4*q+3*d+1)**2*A*Q-32*(3*q+d+1)*Z**2
    return V,Q,A,Z,G

def K(w,a,n):
    assert w>=0 and n>w
    M=F(w+2,2*(2*w+1)); S=F(0)
    for h in range(min(w,a-1)+1):
        b=a-h
        S+=M*(comb(n+b-1,b-1)+comb(n+b-2,b-1))
        if h<min(w,a-1): M*=F((h+2)*(w-h),(h+1)*(2*w-h))
    return S

def L(n): return lcm(*range(1,n+1))
def DD(w,a):
    H=min(w,a-1)+2
    return comb(2*w+2,H)*L(H)**2

def fast(d,r):
    assert r%2==0 and 4<=r<=d
    u=(r-2)//2; j=d-r; b=2*j+2; q=u-d
    V=(j+1)*K(u,b+1,r); Q=-(j+1)*K(u,b+1,r-1)
    A=(j+1)*F(u+2,2*(2*u+1))*K(u-1,b,r)
    Z=q*A+Q+V; G=3*q*(4*q+3*d+1)**2*A*Q-32*(3*q+d+1)*Z**2
    D=2*(2*u+1)*DD(u,b+1)*DD(u-1,b)
    assert all((D*x).denominator==1 for x in (V,Q,A,Z))
    P=D*D*G; assert P.denominator==1 and P>0
    return (V,Q,A,Z,G),D

def full(q,d):
    q=F(q);u=q+d;m=2*q+d;U=rr(u,d);M=rr(m,d);V=Q=A=F(0)
    for k in range(d+1):
        l=d-k; a=(k+1)*(l+1)*U[k]*M[l]; b=(k+1)*l*U[k]*M[l-1] if l else F(0)
        v=(u-k)*(u+k+2)/(2*u*(2*u+1));V+=a;Q+=b;A+=v*(a+b)
    E=U[d]*(u-d)*(2*d+3)*(m+2)/(2*(2*u+1)*(4*m+2))
    Z=q*A+Q+V;G=3*q*(4*q+3*d+1)**2*(A+E)*Q-32*(3*q+d+1)*Z**2
    return V,Q,A,E,Z,G

def mod(x,p):return x.numerator*pow(x.denominator,-1,p)%p

def H(d):return 6*d**7-22*d**6-79*d**5+432*d**4+879*d**3-4572*d**2+11196*d+27648

if __name__=='__main__':
    from sympy import primerange
    print('edge d3,d4',reduced(3,3),reduced(4,4))
    for d in range(3,121):
        V,Q,A,Z,G=reduced(d,d)
        assert G>0
        v,q,a,e,z,g=full(-F(d+2,2),d)
        assert (v,q,a,z,g)==(V,Q,A,Z,G) and e==0
        if d>=6 and d%2==0:
            assert G==F((d+2)**2*(2*d+3)*H(d),256*(d-3)**2*(d-1)**2)
    print('formal edge checks',118)
    c=0
    for d in range(4,121):
        for r in range(4,d+1,2):
            a,D=fast(d,r); assert a==reduced(d,r); c+=1
    print('even triangle checks',c)
    c=exc=0
    for d in range(3,35):
        v,q,a,z,g=reduced(d,d)
        for p in primerange(4*d+7,350):
            for N in (p,2*p,p*p):
                if (N-d-2)%2:continue
                Q=(N-d-2)//2
                if Q<64 or d*d>4*Q:continue
                vals=full(Q,d)
                assert list(map(lambda x:mod(x,p),vals))==list(map(lambda x:mod(x,p),(v,q,a,F(0),z,g)))
                c+=1;exc+=mod(g,p)==0
    print('primal edge modular checks',c,'zero residues',exc)
    for d,j in [(1000,0),(1000,10),(10000,20),(10**30,20),(10**60,10)]:
        r=d-j; a,D=fast(d,r); P=D*D*a[-1]
        print('large d,j,D bits,P bits',d,j,D.bit_length(),P.numerator.bit_length())
```

Next: use disjoint coordinate windows and cross-offset arithmetic to discriminate simultaneous failures; extend the near-edge moment transform to odd r via a finite telescoping endpoint correction, preserving the signed residual. Do not repeat the JI interior positivity or the even transform above. No formal Result or independent review asserted.
