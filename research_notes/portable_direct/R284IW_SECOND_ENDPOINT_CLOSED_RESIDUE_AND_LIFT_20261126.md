# R284IW — Closed second-endpoint residue, Hensel lift and certificate coverage
2026-11-26. Author analytic proof plus executed exact integer/Fraction and modular tests; NOT_REVIEWED. Directed auxiliary binary-tag joint-count observer, retaining V,Q,A,E; not a native spatial/dynamics assertion. Frozen IV@3cb056d13cccd7a9ba6e8d5b003b4a40bacaaae6:research_notes/portable_direct/R284IV_DUAL_ENDPOINT_VALUATION_20261126.md (blob 0dd5f2af7610b131f580772d331ba34d6de2d383); IT@ce891978ba5d3ceca0fc041948524a50effe9e81:research_notes/portable_direct/R284IT_CRITICAL_GAP_DISTRIBUTION_AND_EQUALITY_20261126.md (blob aedc156f2775cf4e2bc5a62a943a4597d98c497f). Reuse IV hypotheses and IT critical profile, no repinning. Account entries match immutable main@acd558fcc299e323149a98e9ee3fce673cba7e45; global P000 projection matched V4 canonical blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc; Source P000 V5 foundation projection, ACTIVE worldview and joint-observer policy consulted. Own existing registration metadata and original session_start receipt recovered SUCCEEDED for EM-DIRECT-0C386E / RA-B82240E8488EF5A1DA5186C4. No shared Task or claim is assumed. Owner inventory r1-20261126-2303-owner-inventory last observed RUNNING before this publication.

## 1. Exact closed residue
For q>=64, 1<=d, d^2<=4q, take the IV notation N=q+d+1, u=N-1, m=2N-d-2, Y=qK. If prime p|N and p>4d+6, IV gives vp(Y)=vp(N)+vp(Q) and vp(Y-32/3)=0. Define Q_d(N)=sum_{k=0}^{d-1}(k+1)(d-k) R_{N-1}(k) R_{2N-d-2}(d-k-1), R_n(j)=prod_{i=0}^{j-1}(n-i)/(n+i+3). This rational function is regular on N in p Z_p. IV's residue C2(d)=Q_d(0) has the exact closed form
C2(d) = d[(2d+1)binom(2d+1,d)-(-1)^d]/[2(2d+3)].
Proof: put l=d-k. Since (k+1)R_{-1}(k)=(-1)^k and R_{-d-2}(l-1)=(d+l)!(d-l)!/[(d+1)!(d-1)!], multiply C2 by (-1)^d(d+1)!(d-1)!. The resulting sum is sum_{l=1}^d f(l), where f(l)=(-1)^l l(d+l)!(d-l)!. Put
g(l)=-(-1)^l(2l-1)(d-l+1)!(d+l)!/[2(2d+3)].
For 1<=l<=d, g(l+1)-g(l)=f(l): after division by (-1)^l(d+l)!(d-l)! the numerator is (2l+1)(d+l+1)+(2l-1)(d-l+1)=2l(2d+3). Summation gives g(d+1)-g(1), yielding the formula. All factorial arguments nonnegative including l=d+1 in g.
Consequently, defining B_d=(2d+1)binom(2d+1,d)-(-1)^d>0, under IV side 2 conditions extra valuation vp(Y)>vp(N) iff p|B_d. No summation over joint branches is required for this first digit; the binomial may be evaluated modulo p by d multiplicative steps (no assertion of poly(log d) time). Also the number of distinct eligible exceptional primes for a fixed d is at most log B_d/log(4d+6)=O(d/log(d+2)), since their product divides B_d and B_d<=(2d+1)2^(2d+1)+1.

## 2. Exact higher-digit classification when the first jet is a unit
Let H_j=sum_{i=1}^j 1/i, H_0=0. Write
D_d=Q_d'(0)=sum_{k=0}^{d-1} (-1)^k(d-k) R_{-d-2}(d-k-1) L_k,
L_k=-3H_k-H_{k+1}+1+2H_{d-1}-2H_{2d-k}+2H_{d+1}.
Proof: differentiate each shifted fiber, retaining the same k. The log derivative of R_{N-1}(k) at 0 is -H_k-H_{k+1}+1; of R_{2N-d-2}(j), j=d-k-1, it is 2[H_{d-1}-H_k-H_{2d-k}+H_{d+1}]. All factors are p-units at 0 under p>4d+6, hence no singular differentiation. This yields the displayed jet. The individual signed values here are rational residues of the positive physical-parameter fibers, not signed mass.
For N in p Z_p all denominators of Q_d are units; its power series in N has coefficients in Z_p by geometric expansion of each reciprocal. In particular
Q_d(N) = C2(d)+N D_d (mod p^(2t)), t=vp(N)>=1.
If vp(C2)<t, then vp(Q)=vp(C2) (without a derivative-unit assumption). If p|B_d and p does not divide D_d in Z_p, there exists exactly one alpha in p Z_p with Q_d(alpha)=0. Indeed from a root r_e modulo p^e, the next digit is uniquely s=-[Q_d(r_e)/p^e] / Q_d'(r_e) mod p, and r_(e+1)=r_e+s p^e. Start r_1=0; Q_d'(r_e)=D_d mod p. The compatible residues converge to alpha. For N,alpha in p Z_p, the divided difference (Q_d(N)-Q_d(alpha))/(N-alpha) equals D_d modulo p by the integral series; hence is a unit. Therefore
vp(Q_d(N))=vp(N-alpha), vp(alpha)=vp(C2(d)),
and IV yields vp(Y)=vp(N)+vp(N-alpha) for actual positive parameters. If t differs from vp(C2), this equals t+min(t,vp(C2)); if equal, the lifted root gives the higher digits. The root is nonzero because C2(d)>0. Q_d at positive valid q,d is positive, so actual N is not alpha. These formulas are exact and conditional only on the stated p-unit derivative; a singular residue requires separate analysis. No real absolute separation follows from the p-adic unit test.

## 3. Asymptotic coverage of the existing non-equality certificate
This is a coverage theorem for IV, not a density assertion about actual equality events. Let d(q) be any eventually nondecreasing positive integer function with d(q)=s sqrt(q)+O(1), 0<s<2. For either endpoint i=1,2, define N_i as IV and threshold C_i(q)=12d(q)+14 or 4d(q)+6 respectively. Then
lim_{X->infty} X^(-1) #{q<=X: P^+(N_i(q))>C_i(q)} = log 2.
Here P^+ is largest prime factor. Proof: N_i(q) is strictly increasing eventually; its image up to X differs from integers up to X by O(sqrt X) points, because N_i(q)=q+O(sqrt q) and omitted points telescope. Moreover C_i(q)/sqrt(N_i(q)) tends to positive constant. For any fixed c>0 the density of n<=X with P^+(n)>c sqrt(n) is log 2. To see this first use fixed cutoff sqrt X, where at most one prime >sqrt X divides n<=X. Count equals sum_{sqrt X<p<=X} floor(X/p)= X(log 2+o(1)) by the classical prime reciprocal Mertens theorem sum_{p<=x}1/p=log log x+M+o(1) and pi(X)=o(X). On epsilon X<=n<=X the variable cutoff is between c sqrt(epsilon X) and c sqrt X; the symmetric difference from the fixed cutoff is bounded by sum_{p in [a sqrt X,b sqrt X]} floor(X/p)=o(X) for fixed positive a,b by the same reciprocal theorem. The first epsilon X integers cost at most epsilon X; send epsilon to zero. The same proof sandwiches thresholds whose ratio to sqrt n tends to a positive constant. Thus the image error is negligible and the asserted density follows.
In particular for the IT approximation T(q)=s0 sqrt(q)+C0+Z0/sqrt(q), both d0=floor(T(q)) and d1=d0+1 meet the hypotheses (T increasing eventually, 0<s0<2). Each candidate is directly certified non-equal on a density log 2 set via either endpoint separately. For the pair of candidates, using side 2 alone, the set on which BOTH are certified has lower density >=2 log 2-1=0.386294... by the union bound on complements; no independence assumed. This establishes coverage of cheap arithmetic certificates even though IT already supplies a stronger sparsity bound for actual equality, which is a different observable. Correlations between smooth neighboring endpoints, higher density and universal exclusion remain open.

## 4. Exact computation (executed)
Python standard library Fraction and modular integer arithmetic, d=1..100 and every prime p<=3000 with p>4d+6. 100 exact closed-sum comparisons; 38,518 prime/degree pairs checked against exact rational C2 and derivative D; 46 exceptional pairs, all 46 simple, zero singular in this finite domain. 138 lift steps (three per simple pair), verifying the lifted root and two neighboring digits per step. The absence of singular pairs is finite evidence, not an unbounded theorem. Examples (d,p,alpha mod p^4): (3,41,1239881), (4,103,48781315), (7,167,3522030), (10,2221,7632781058009), (11,811,340216303664), (13,127,227840032), (16,89,45762287), (16,2213,11859308199546), (17,653,149352170309), (17,673,147118051029), (18,1153,1017543016482), (20,277,5646955794). No full real K rerun claimed. Reproduction:
```python
from fractions import Fraction as F
from math import comb,isqrt

def R(n,j):
    a=F(1)
    for i in range(j): a*=F(n-i,n+i+3)
    return a

def C(d): return sum((-1)**k*(d-k)*R(-d-2,d-k-1) for k in range(d))
def closed(d): return F(d*((2*d+1)*comb(2*d+1,d)-(-1)**d),2*(2*d+3))
def mod(x,m):
    x=F(x);return x.numerator*pow(x.denominator,-1,m)%m

def jet(d,N,M):
    def seq(n,b):
        a=[(1,0)]
        for i in range(d-1):
            v,w=a[-1];r=pow(n+i+3,-1,M);z=(n-i)*r%M;dz=b*(2*i+3)*r*r%M
            a.append((v*z%M,(w*z+v*dz)%M))
        return a
    U,S=seq(N-1,1),seq(2*N-d-2,2);v=w=0
    for k in range(d):
        a,b=U[k];c,e=S[d-k-1];fac=(k+1)*(d-k);v+=fac*a*c;w+=fac*(a*e+b*c)
    return v%M,w%M

def derivative(d):
    H=[F(0)]
    for i in range(1,2*d+2):H.append(H[-1]+F(1,i))
    return sum((-1)**k*(d-k)*R(-d-2,d-k-1)*(-3*H[k]-H[k+1]+1+2*H[d-1]-2*H[2*d-k]+2*H[d+1]) for k in range(d))
ps=[p for p in range(2,3001) if all(p%j for j in range(2,isqrt(p)+1))]
count=exc=simple=singular=lifts=0; examples=[]; singular_examples=[]
for d in range(1,101):
    c=closed(d);assert c==C(d);D=derivative(d)
    for p in ps:
        if p<=4*d+6:continue
        count+=1
        z,j=jet(d,0,p);assert z==mod(c,p) and j==mod(D,p)
        if z:continue
        exc+=1
        if not j: singular+=1;singular_examples.append((d,p));continue
        simple+=1;r=0;m=p
        for e in range(1,4):
            q,j=jet(d,r,m*p);assert q%m==0
            r+=m*((-q//m)*pow(j,-1,p)%p);m*=p
            assert jet(d,r,m)[0]==0
            for k in (1,2):assert jet(d,(r+k*(m//p))%m,m)[0]!=0
            lifts+=1
        if len(examples)<12:examples.append((d,p,r))
print('pairs,exceptional,simple,singular,lifts',count,exc,simple,singular,lifts)
print('examples mod p^4',examples,'singular',singular_examples)
# pairs,exceptional,simple,singular,lifts 38518 46 46 0 138
```
Next: determine whether p>4d+6 and p|B_d can ever have D_d=0 mod p; search for a closed derivative identity or singular witness, extend to first endpoint C1, and implement shifted IS oracle. Real inverse-polynomial separation and universal equality exclusion remain open. No shared Result or independent review claimed.
