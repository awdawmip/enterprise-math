# R284IX — Budget-prime common certificate and exact diagonal joint moments
2026-11-27. Author analytic proof and executed exact/modular evidence; NOT_REVIEWED. Independent continuation of the auxiliary binary-tag joint-count observer, not a native spatial/dynamics assertion. Frozen definitions IV@3cb056d13cccd7a9ba6e8d5b003b4a40bacaaae6:research_notes/portable_direct/R284IV_DUAL_ENDPOINT_VALUATION_20261126.md (blob 0dd5f2af7610b131f580772d331ba34d6de2d383), IW@de4232a1ffd071cd698ef902dd5bbb75a0b33e21:research_notes/portable_direct/R284IW_SECOND_ENDPOINT_CLOSED_RESIDUE_AND_LIFT_20261126.md (blob 110ff2edf347b418dcfdef2174907071fb7f4258). No scientific repinning. P000 V5, ACTIVE worldview, joint observer and heartbeat companion consulted; account entry blobs match immutable main@70cb0ecfc9994d7b04f7f91a230a723223da0e36. Existing own registration EM-DIRECT-0C386E / RA-B82240E8488EF5A1DA5186C4 recovered via original SUCCEEDED receipt; owner inventory r1-20261127-0004-owner-inventory last observed RUNNING before publication. No formal Task/claim/owner mutation assumed.

## 1. New certificate on the budget itself
For integers q>=64, 1<=d, d^2<=4q retain IV definitions u=q+d, m=u+q, l=d-k, R_n(j)=product_{i=0}^{j-1}(n-i)/(n+i+3),
w0=(k+1)(l+1)R_u(k)R_m(l), w1=(k+1)l R_u(k)R_m(l-1) for l>=1 and zero otherwise,
v(k)=(u-k)(u+k+2)/(2u(2u+1)), V=sum w0, Q=sum w1, A=sum v(k)(w0+w1),
E=R_u(d)(u-d)[(d+1)(u+d+2)+(d+2)(u-1-d)](m+2)/[2u(2u+1)(4m+2)].
Y=qK=q(3u+q+1)^2(A+E)Q/[(u+2q+1)(qA+Q+V)^2].
If prime p divides q and p>4d+3, t=vp(q), then
    vp(Y)=t+vp(A+E)>=t, vp(Y-32/3)=0.
Moreover with P_d=2d^2+4d+3=2(d+1)^2+1,
    vp(Y)>t iff p divides P_d.
This is the third distinct certificate coordinate (budget q itself, versus IV endpoints q+2d+2 and q+d+1). In contrast to IV, the excess is controlled by A+E rather than Q.

## 2. Exact joint binomial moments at the formal diagonal q=0
The rational extension to q=0 is used only for residues at positive q; it is not a new physical budget. For d>=1 put
c=(d+1)/binom(2d+2,d), B=c^2 binom(4d+2,d).
At q=0, u=m=d, and the exact formulas are
 V0=B*4(d^2+3d+3)/[3(d+1)(3d+4)],
 Q0=B*4d/[3(d+1)],
 A0=B*(2d^2+4d+3)/[3(d+1)(2d+1)],
 E0=0,
 V0+Q0=B*4(4d+3)/[3(3d+4)].
Proof. Extend b(k)=binom(2d+1,d-k) by zero outside its ordinary support. Let f(k)=b(k)-b(k+1). For 0<=k<=d, (k+1)R_d(k)=c f(k), by factorial ratios. The extension has f(-1)=0 and f(k)=0 for k>d. For D=d or d-1, the bilateral convolution sum f(k)f(D-k) is exactly the physical finite sum: any k<=-2 makes D-k>d; k=-1 contributes zero; and the same holds with k and D-k exchanged. Thus no auxiliary negative-index terms remain. Write L=2d+1, n=2L, S=2d-D and H_s=binom(n,s), zero outside range. Expansion of the two differences and Vandermonde gives the convolution H_S-2H_(S-1)+H_(S-2). For D=d,d-1 respectively S=d,d+1, yielding the stated V0,Q0 after multiplying by c^2 and dividing by H_d to simplify. Their sum gives the displayed V0+Q0.

For the moment A0, v(k)=[(d+1)^2-(k+1)^2]/[2d(2d+1)]. The same bilateral extension is exact even with this weight. For a,b in {0,1}, put h=S-a-b, C=d+1-a, x=d-k-a. Expand f(k)f(D-k) with coefficient (-1)^(a+b) multiplying binom(L,x)binom(L,h-x). The factor (k+1)^2=(C-x)^2. The three factorial moment sums are H_h, L binom(n-1,h-1), L(L-1)binom(n-2,h-2), respectively for weights 1,x,x(x-1), obtained directly by x binom(L,x)=L binom(L-1,x-1) and its two-factor version followed by Vandermonde. Thus the exact contribution for the square is
 C^2 H_h+(1-2C)L binom(n-1,h-1)+L(L-1)binom(n-2,h-2).
Substitute S=d,d+1 and sum the four signs for each S. For an explicit algebra check, define r_j=H_(d+j)/H_d, j=-2,-1,0,1, with r_-2=d(d-1)/[(3d+3)(3d+4)], r_-1=d/(3d+3), r_0=1, r_1=(3d+2)/(d+1). The normalized expression A0/B equals
 sum_{j=0,1; a,b=0,1} (-1)^(a+b) r_(j-a-b)
 *[(d+1)^2-C^2+(2C-1)h/2-L(L-1)h(h-1)/(n(n-1))]/[2d(2d+1)],
 where h=d+j-a-b. Expanding this rational expression gives (2d^2+4d+3)/[3(d+1)(2d+1)] (valid also d=1, where r_-2=0). Finally u-d=0 implies E0=0; this retains its exact contribution at the residue, not a deletion away from q=0.

## 3. Exact valuation and classification
At positive q divisible by p>4d+3 all rational denominators in R, v, E and the exterior factor are p-units: at q=0 they are among d+i+3 (i<=d-1), 2d,2d+1,4d+2,d+1, with factors at most 4d+3. Thus V,Q,A,E reduce to V0,Q0,A0,0. The binomial normalization B is a p-unit because every factorial argument is <=4d+2. V0+Q0 and Q0 are units by the closed formulas, and 3d+1 is a unit. Consequently qA+Q+V is a unit and all factors of Y/q other than A+E are units. This proves the exact valuation and its first-digit classification. Equivalently
 Y/q = d(3d+1)^2(3d+4)^2 P_d / [4(d+1)^3(2d+1)(4d+3)^2] (mod p).
Since p>3 and vp(Y)>=1, Y-32/3 is a unit and nonzero. For fixed d there is at most one eligible exceptional prime: P_d<(4d+3)^2, and the product of two such primes would exceed P_d. Any such prime is 1 or 3 mod 8, since 2(d+1)^2=-1 mod p implies (-2/p)=1. This is a necessary condition, not a claim of existence or higher-digit classification.

## 4. Simultaneous certificate density, without smooth-number independence
Take any fixed finite family of integer candidate functions d_j(q)=s sqrt(q)+O(1), 0<s<2. For all sufficiently large q they meet the IV domain. Set D(q)=max_j d_j(q). On the common event P^+(q)>4D(q)+3, the SAME prime certifies Y(q,d_j(q)) !=32/3 for every j. This event has asymptotic density log 2: the IW Mertens argument applies directly to q and a threshold asymptotic to 4s sqrt(q). Briefly count q<=X with prime factor >sqrt X by sum_{sqrt X<p<=X} floor(X/p)=X(log 2+o(1)); on epsilon X<=q<=X, changing a cutoff by fixed positive factors of sqrt X costs o(X) by prime reciprocal Mertens; send epsilon to zero. No correlation assumption. Thus for the two critical candidates floor(T(q)), floor(T(q))+1, simultaneous certification has lower density >=log 2 rather than the previous 2 log 2-1. The particular common-prime event has exactly density log 2; the union of all certificate routes may be larger.
Furthermore the number q<=X on that event at which ANY of the fixed candidates has vp(Y)>vp(q) is O(sqrt X). For each d in O(sqrt X), there is at most one eligible exceptional prime p|P_d. The condition d_j(q)=d implies |d-s sqrt(q)|<=C_j for a constant C_j, so q belongs to an interval of length O(d+1). Since p>4d+3, that interval contains O(1) multiples of p. Sum over d and finitely many j. Outside O(sqrt X) exceptional q, the same prime gives exact vp(Y(q,d_j(q)))=vp(q) for all candidates. This is an unconditional count for the specified certificate event, not a real absolute separation bound or a claim of efficient general factoring. An already supplied prime can be checked and used directly; obtaining it is a separate computational cost.

## 5. Executed exact verification
150 exact diagonal cases d=1..150. Physical modular verification for d=1..50, all primes p<=1000 with p>4d+3, q in {p,2p,p^2} and q>=64,d^2<=4q: 20,021 cases, 7,089 with t=2, 50 exceptional cases (not distinct prime/degree pairs). 781 physical cases independently checked by full rational Fraction computation (d<=12,p<150); all assertions passed. At each modular case computation modulo p^(t+2) verifies the leading valuation and equality exclusion. Examples (q,d,p,t): (361,2,19,2), (73,5,73,1), (5329,5,73,2), (86,7,43,1), (163,8,163,1), (67,9,67,1). No full large-budget real K rerun. Reproduction (Python standard library):
```python
from fractions import Fraction as F
from math import comb,isqrt
def vals(q,d,M=None):
    u=q+d;m=u+q
    def div(a,b):return F(a,b) if M is None else a*pow(b,-1,M)%M
    def red(a):return a if M is None else a%M
    def R(n):
        z=[1]
        for i in range(d):z.append(red(z[-1]*div(n-i,n+i+3)))
        return z
    P,S=R(u),R(m);V=Q=A=0
    for k in range(d+1):
        l=d-k;w0=(k+1)*(l+1)*P[k]*S[l];w1=(k+1)*l*P[k]*S[l-1] if l else 0
        v=div((u-k)*(u+k+2),2*u*(2*u+1))
        V=red(V+w0);Q=red(Q+w1);A=red(A+v*(w0+w1))
    E=red(P[d]*div((u-d)*((d+1)*(u+d+2)+(d+2)*(u-1-d))*(m+2),2*u*(2*u+1)*(4*m+2)))
    Y=red(div(q*(3*u+q+1)**2,u+2*q+1)*(A+E)*Q*div(1,red(q*A+Q+V)**2))
    return V,Q,A,E,Y
def expected(d):
    c=F(d+1,comb(2*d+2,d));B=c*c*comb(4*d+2,d)
    return B*F(4*(d*d+3*d+3),3*(d+1)*(3*d+4)),B*F(4*d,3*(d+1)),B*F(2*d*d+4*d+3,3*(d+1)*(2*d+1))
def mod(x,p):
    x=F(x);return x.numerator*pow(x.denominator,-1,p)%p
def vp(x,p):
    x=F(x);a,b=abs(x.numerator),x.denominator
    if not a:return float('inf')
    t=0
    while a%p==0:a//=p;t+=1
    while b%p==0:b//=p;t-=1
    return t
ps=[p for p in range(2,1001) if all(p%j for j in range(2,isqrt(p)+1))]
for d in range(1,151):
    V,Q,A,E,Y=vals(0,d);assert (V,Q,A)==expected(d) and E==Y==0
counts=ex=exact=digits2=0
for d in range(1,51):
    v0,q0,a0=expected(d);poly=2*d*d+4*d+3
    for p in ps:
        if p<=4*d+3:continue
        for q,t in [(p,1),(2*p,1),(p*p,2)]:
            if q<64 or d*d>4*q:continue
            M=p**(t+2);V,Q,A,E,Y=vals(q,d,M)
            assert (V%p,Q%p,A%p,E%p)==(mod(v0,p),mod(q0,p),mod(a0,p),0)
            assert (V+Q)%p and Q%p and Y%(p**t)==0
            assert (Y//p**t)%p==0 if poly%p==0 else (Y//p**t)%p!=0
            assert (Y-mod(F(32,3),M))%p!=0
            assert (A+E)%p==0 if poly%p==0 else (A+E)%p!=0
            assert p%8 in (1,3) if poly%p==0 else True
            counts+=1;digits2+=t==2;ex+=poly%p==0
            if d<=12 and p<150:
                V1,Q1,A1,E1,Y1=vals(q,d)
                assert tuple(mod(x,M) for x in (V1,Q1,A1,E1,Y1))==(V,Q,A,E,Y)
                assert vp(Y1,p)==t+vp(A1+E1,p) and vp(Y1-F(32,3),p)==0
                exact+=1
print(150,counts,digits2,ex,exact)
# 150 20021 7089 50 781
```
Next: use diagonal moment recurrence for first derivative of A+E in the unique exceptional budget-prime case; investigate additional certificate coordinates and correlations of smooth numbers; retain IW singular derivative and first endpoint closure as open. Real inverse-polynomial separation and worst-case fast sign determination still open. No shared Result/claim or independent review.
