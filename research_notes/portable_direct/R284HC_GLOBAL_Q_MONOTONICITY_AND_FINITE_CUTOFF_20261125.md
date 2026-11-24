# R284HC — Global one-edge monotonicity and a finite symmetric-dominance cutoff

2026-11-25. Independent auxiliary four-phase binary-tag model. Author proof, NOT_REVIEWED. Frozen science: HA at 82c1bbab0211958259cb233833a8b2d2ea9d0675 (blob 256e77c033ef0c975173c818cdfdeb18ea3bc983), HB at 7106ba15d520daf9d773f5de2ccc51385ac4226f (blob 95f19730b5806b4b0e1be710391ef6076528de05), with their original GY/GX/GV/GL pins. Global canonical entries read at a32307aba5f3e3dff721408e1a56177d694e9a05; EM main control at 0fc72cdda05ca8d3d2d3da048b65476d4d16da6f, P000 V5 and ACTIVE worldview, portable and continuation protocols, BRC and residual rules. Gateway em_status succeeded; owner query r284hc-20261125-0200-owner-read-v1 last RUNNING/error=null; own current research identity not established. Historical EM-DIRECT-0C386E is provenance only. Independent nonoverwriting scientific note, no shared CLAIM or protected mutation.

## 1. Definitions and exact observer

Use d=u-q>=1, m=u+q, H=u+2q+1, J=3u+q. M_n(k)=(k+1)/(n+1) binom(2n+2,n-k) for 0<=k<=n, zero otherwise. Set A_g=B_(u,m)(g), C_g=B_(u-1,m-1)(g), with B_(n,l)(g)=sum_k M_n(k)M_l(g-k), zero for g<0. HA gives
Q=A_(d-1);
S=A_d+A_(d-1)+q[B_(u-1,m)(d)+B_(u-1,m)(d-1)];
P=C_(d+1)+3C_d+3C_(d-1)+C_(d-2).
K=PQ(J+1)^2/(S^2 H). All arguments below are on this exact positive binomial-moment observer; they do not substitute independent port probabilities for the original joint paths.

## 2. Theorem: Q/S strictly decreases at every adjacent q

For integer u>=2, 0<=q<u-1,
Q(q+1,u)/S(q+1,u) < Q(q,u)/S(q,u).
Also (Q/S)(J+1)^2/H strictly decreases. No finite upper bound on u or d is needed.

Proof. The adjacent ratio
M_n(k+1)/M_n(k)=(k+2)(n-k)/[(k+1)(n+k+3)]
strictly decreases in k and increases in n on its positive range (both factors decrease in k; the second increases in n). Hence M_n is log-concave with interval support, and M_(n+1)(k)/M_n(k) increases in k on common support.

Let pi_(g,m)(k) be the probability proportional to M_u(k)M_m(g-k), for 0<=k<=g<=u<=m. Increasing g by one shifts this probability toward larger k in monotone likelihood ratio order: the ratio of new to old weights is the adjacent ratio of M_m at g-k, increasing in k, with an extra right endpoint. Increasing m by one instead shifts it toward smaller k, because M_(m+1)(g-k)/M_m(g-k) decreases in k. These orderings imply the corresponding expectation inequalities for any monotone function; for example the sign of covariance of two increasing functions follows by summing pairwise differences against two independent copies of the same probability.

Define
r(k)=M_(u-1)(k)/M_u(k)=[u(u+2)-k(k+2)]/[2u(2u+1)].
This is nonnegative and decreases in k, vanishing at k=u. Write e_(g,m)=E_pi r(k). Thus e increases when g decreases or m increases; it is strictly positive since k=0 has positive weight.

Write R_(g,m)=A_(g+1)/A_g. At fixed m, R is nonincreasing in g because convolution of two nonnegative log-concave interval-support sequences is log-concave. For completeness, their Toeplitz matrices T(i,j)=M(j-i), extending M by zero, have nonnegative ordered 2x2 minors by the adjacent ratio test. Their product is the Toeplitz matrix of the convolution. The 2x2 Cauchy-Binet identity, with finite intermediate sums, gives the same minors nonnegative for the product, including the adjacent log-concavity inequality. At fixed g, R is nondecreasing in m: A_(g,m+1)/A_(g,m) is the expectation of M_(m+1)(j)/M_m(j) under the right-port index law proportional to M_u(g-j)M_m(j). This increasing function of j has larger expectation when g increases, by the same likelihood ratio argument. Dividing the two inequalities at g+1 and g proves R_(g,m+1)>=R_(g,m). All common-support weights used here are positive because g+1<=u<=m.

Now put g=d-1:
S/Q=1+R_(g,m)+q[e_(g,m)+R_(g,m)e_(g+1,m)].
Under q -> q+1, g decreases and m increases. Every nonnegative factor on the right is nondecreasing, the bracket is positive and the coefficient q increases strictly. This proves strict increase of S/Q. The physical multiplier (3u+q+1)^2/(u+2q+1) decreases strictly for 0<=q<u (differentiate the positive rational function: derivative sign equals sign(q-2u)<0), proving the second assertion.

## 3. Counterexample to separate P/S monotonicity

P/S is not globally decreasing. The first counterexample in the exact scan u<=128, ordered by u then q, is u=8, q=6 -> 7. At q=6, (S,P,Q)=(1092191963070,121642878630,146198262600); at q=7, (S,P,Q)=(2147789878260,240905872740,171908991540). The cross-product P(7)S(6)-P(6)S(7)=1852114579068544128000>0. Thus a proof by separate monotonicity of both edges is impossible. In this finite scan all 378 P/S increases began at gaps d<=6; no equality. The narrower conjecture that P/S decreases for initial d>=7, or even d>=49, would combine with HB's certified strips to prove global K monotonicity. This is a conjecture, not a theorem.

## 4. Theorem: explicit all-parameter upper envelope

For u>=2 and 0<=q<u, let r=(u+2)/(2(2u+1)), t=(m+2)/(2(2m+1)),
rho=[6u(u+2)-d(2d+7)]/[12u(2u+1)]>0, b=t(1+3r).
Then
K <= b (J+1)^2/[H(1+q rho)^2].
For u>=40 this implies the simpler strict upper bound
K < 144u/(q+5)^2.
In particular, on this whole domain, q+5>=12 sqrt(u) guarantees symmetric physical-order dominance. For any valid u>=1, q^2>=144u also guarantees K<1, since it forces u>144. These are finite sufficient cutoffs, not the exact transition.

Proof of lower bound for S. For fixed g<=d, compare pi_(g,m) with pi_(g,u). The latter is symmetric and unimodal around g/2: its weights M_u(k)M_u(g-k) have decreasing adjacent ratios and are symmetric. Increasing m shifts the law left as in section 2. Thus E_pi k(k+2) <= E_(g,u) k(k+2). For the symmetric law the latter expectation equals g^2/4+g+E(k-g/2)^2. The weight is nonincreasing with distance from center, so its weighted squared distance is no greater than the uniform mean squared distance on {0,...,g}; this follows from the nonpositive covariance of the weight and squared distance under uniform measure. Consequently E_pi k(k+2) <= g(2g+7)/6. Substitution in r(k) gives e_(g,m)>=rho for g=d,d-1. Hence S >= (1+q rho)(A_d+A_(d-1)).

Proof of upper bound for P. Pointwise M_(u-1)(k)<=r M_u(k), M_(m-1)(k)<=t M_m(k), so C_g<=rt A_g. For any nonnegative moment convolution B_g, the adjacent recurrence implies (g+1)B_(g+1)<= (g+4)B_g: differentiate the finite series coefficient, or sum (k+1)M_n(k+1)M_l(g-k)+(g-k+1)M_n(k)M_l(g-k+1) and use (k+1)M_n(k+1)<=(k+2)M_n(k), including endpoints. Thus C_(d+1)<=((d+4)/(d+1))C_d. For d>=2, each k<=d-2<=u-2 satisfies
M_(u-1)(k)/M_u(k+1)=(k+1)(u+k+2)(u+k+3)/[(k+2)2u(2u+1)]<=1.
Shift the left index by one injectively to get C_(d-2)<=t A_(d-1); for d=1 its left side is zero. Hence P <= rt[4+3/(d+1)] A_d + t(1+3r) A_(d-1) <= b(A_d+A_(d-1)), since r<=2/5 for u>=2 and 1+3/(d+1)<=5/2. With Q<=A_d+A_(d-1) this proves the stated envelope.

For the simpler bound, rho>=c=(4u+5)/(12(2u+1)) (d<=u), and t<=r. Also (J+1)^2/H<=9u by its decreasing dependence on q and (3u+1)^2<=9u(u+1). Therefore K<=9u [r(1+3r)/c^2]/(q+1/c)^2. The bracket is exactly 36(u+2)(7u+8)/(4u+5)^2, strictly less than 16 for u>=40 (difference numerator from 16 is -4(u^2-38u-44)). At u>=40, 1/c>5. This proves the strict simplified bound.

## 5. Executed exact verification

Python arbitrary-precision integers and Fraction. Full scan 1<=u<=128, 0<=q<u: 8128 adjacent comparisons of Q/S, all strictly decreasing; 8255 envelope checks for u>=2, all pass; 378 increases of P/S, first witness above, largest initial gap 6, zero equalities. Also direct crosscheck against the previously locally preserved original GW distance DP for u<=12: 234 exact S/P/Q counts, zero discrepancies. The proof uses the frozen HA identities, not a finite scan assumption. Selected K: (u,q)=(145,144):0.03531512756; (256,192):0.08111236999; (1024,384):0.11978689104; (4096,768):0.16125377494. Decimal display only.

Reproduce with Python 3:
```python
from math import comb
from fractions import Fraction

def moments(n,g):
    a=[comb(2*n+2,n)//(n+1)]
    for k in range(g):
        a.append(a[-1]*(k+2)*(n-k)//((k+1)*(n+k+3)) if k<n else 0)
    return a

def conv(a,b,g):
    return sum(a[k]*b[g-k] for k in range(g+1)) if g>=0 else 0

def counts(u,q):
    d=u-q; m=u+q; g=d+1
    A,a,B,b=(moments(n,g) for n in (u,u-1,m,m-1))
    Q=conv(A,B,d-1); S=Q+conv(A,B,d)+q*(conv(a,B,d)+conv(a,B,d-1))
    P=sum(comb(3,j)*conv(a,b,d+1-j) for j in range(4))
    return S,P,Q

def bounds(u,q,S,P,Q):
    d=u-q; m=u+q; H=2*q+u+1; J=q+3*u
    r=Fraction(u+2,2*(2*u+1)); t=Fraction(m+2,2*(2*m+1))
    rho=Fraction(6*u*(u+2)-d*(2*d+7),12*u*(2*u+1))
    K=Fraction(P*Q*(J+1)**2,S*S*H)
    assert K<=t*(1+3*r)*Fraction((J+1)**2,H)/(1+q*rho)**2
    if u>=40: assert K<Fraction(144*u,(q+5)**2)
    if q*q>=144*u: assert K<1

def scan(limit=128):
    comparisons=checks=ties=0; increases=[]
    for u in range(1,limit+1):
        prev=None
        for q in range(u):
            S,P,Q=counts(u,q)
            if u>=2:
                bounds(u,q,S,P,Q); checks+=1
            if prev:
                s,p,r=prev
                assert r*S>Q*s
                if P*s>p*S: increases.append((u,q-1,q,u-q+1))
                if P*s==p*S: ties+=1
                comparisons+=1
            prev=S,P,Q
    print(comparisons,checks,len(increases),increases[0],max(p[-1] for p in increases),ties)
    assert (comparisons,checks,len(increases),increases[0],max(p[-1] for p in increases),ties)==(8128,8255,378,(8,6,7,2),6,0)

def dp(q,u,A,B,D):
    r=2*u+1; M=max(0,D-q); p=lambda x:max(0,x); v=[0]*(B+1)
    for a in range(A+1):
        for b in range(B+1):
            D2=p(A-a-2*q)+p(p(b-q)+M-q)
            D3=max(0,D-2*q,p(a-q)-q,B-b+p(a-q)-2*q+M)
            v[b]=0 if min(D2,D3)<r else 1 if a==b==0 else v[b]+(v[b-1] if b else 0)
    return v[B]

if __name__=='__main__':
    scan()
    n=0
    for u in range(1,13):
        for q in range(u):
            H=2*q+u+1; J=q+3*u
            configs=[(H,J,H),(H-1,J+1,H),(H,J+1,H-1)]
            assert counts(u,q)==tuple(dp(q,u,*c) for c in configs)
            n+=3
    assert n==234
    print('DP checks',n)
```

## 6. Next action

Analyze the other edge P/S in the remaining d>=49 region via joint moment-index transport, or establish a sufficiently small upper bound on its possible increase relative to the strict Q/S decrease. HB covers d<=48; a global K proof remains open. The new explicit envelope restricts where asymmetric physical dominance can occur without asymptotic approximations. Activity association remains pending actual current own identity and source authorization; no formal task completion or review.
