# R749SUT — Certified zero-gap maximizers on a broad near-square family

Date: 2026-11-18 (Asia/Shanghai). Evidence: AUTHOR_EXACT_NOT_REVIEWED. Domain: frozen positive-rational WBRC-T30–T32 **auxiliary named two-Port integer observer**, not an asserted native X6 Cell/Link/Port event.

## Frozen provenance and dependency

- Immutable scientific input: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:definitions/ENTERPRISE_BRC_RECURRENT_PORT_FOUNDATION_20260903.md.
- R749SUO@161123938bc7836d62d130a755b3d6601a743182 supplies the **author-level, unreviewed** classification: for M>=116 every nonstandard optimum has Q=+1. This is an explicitly load-bearing dependency for the *full* nonstandard optimum, not for the following theorem within Q=+1.
- R749SUS@bad2cc04a18b8d3cededb4735eb3cf9302f2851a supplies the closest-factor/quotient-plateau exact optimizer. The new result constructs infinitely many inputs where no plateau search is necessary. The global P000 worldview, SOURCE pins and Foundation status are unchanged.

## Model and coordinates

Consider named integer tuples (a,u,v,d) with 1<=a,u,v,d<=M, ad-uv=1, Q=u+v-a-d!=0, tau=max(u,v)ad. Orient u=max(u,v). Within Q=+1 use the already established positive-factor representation

\[
x=u-a,\quad y=u-d,\quad 2\le x\le y,\quad n=xy=u+1\le B=M+1,
\]

with reconstruction

\[
(a,u,v,d)=(n-x-1,n-1,n-x-y,n-y-1)
\]

when all entries are positive. Write s=x+y. Then

\[
T(n,s)=(n-1)((n-1)^2-(n-1)s+n)=\tau.
\]

Every such candidate has n<=B, s<=n and n<=s^2/4. T decreases strictly in s at fixed n>1 and increases strictly in n for n>=s>=4 because

\[
\partial_n T=3(n-1)^2-2s(n-1)+2n-1\ge n^2-2n+2>0.
\]

## Theorem 1 — exact strict zero-gap certificate

Suppose B>=6 and integers 2<=x<=y satisfy xy=B, B-x-y>=1. Set

\[
s_0=x+y,\quad A=B-1,\quad D=B-\frac{(s_0-1)^2}{4}.
\]

If D>0 and

\[
\boxed{\mathcal G(B,s_0)=A^2(3D-s_0)+A(B-3D^2)+D^3>0,}
\]

then (x,y) is the unique unordered maximizer over all admissible Q=+1 factor pairs subject to xy<=B, and its optimal product is n*=B (zero gap). It yields two named maximizers if x=y, and four if x<y.

**Proof.** For any competing pair (x',y'), put n'=x'y'<=B and s'=x'+y'. If s'>=s0, monotonicity gives T(n',s')<=T(B,s0); equality requires n'=B and s'=s0, hence the identical unordered pair. If s'<=s0-1, AM-GM gives n'<= (s0-1)^2/4=B-D. Its three positive score factors are each at most n'-1, so T(n',s')<= (n'-1)^3 <= (A-D)^3. Exact expansion gives

\[
T(B,s_0)-(A-D)^3=A^2(3D-s_0)+A(B-3D^2)+D^3=\mathcal G>0.
\]

This excludes every distinct competitor. The two independent labeled swaps account for the named multiplicity. QED.

The certificate is a constant number of exact integer operations. Put d4=4B-(s0-1)^2=4D. The fractional comparison is equivalent to d4>0 and

\[
\boxed{64\mathcal G=16A^2(3d4-4s_0)+4A(16B-3d4^2)+d4^3>0.}
\]

Arbitrary-precision bit costs remain separate.

## Theorem 2 — constructive infinite near-square family

Let t,h be integers satisfying

\[
\boxed{t\ge11,\quad h\ge0,\quad 4t\ge 4h+3(h-1)^2+12.}
\]

Put B=t(t+h) and M=B-1. The unique unordered Q=+1 optimum is exactly (x,y)=(t,t+h). Its score and one oriented named tuple are

\[
\boxed{T^*(M)=M(B-t-1)(B-t-h-1),}
\]

\[
\boxed{(a,u,v,d)=(B-t-1,\ B-1,\ B-2t-h,\ B-t-h-1).}
\]

The full optimizer has two named configurations for h=0 and four for h>0. By the earlier R749SUO Q=+1 global classification for M>=116, these constitute all **nonstandard global** maximizers; the present proof of the Q=+1 part is independent of that classification.

**Proof.** s0=2t+h and

\[
D=t-\frac{(h-1)^2}{4},\qquad
3D-s_0=t-h-\frac{3(h-1)^2}{4}\ge3.
\]

Thus D>0. Since B=t^2+th>=t^2, D<=t and A=B-1>=t^2-1,

\[
\mathcal G
\ge 3A^2+A(B-3t^2)+D^3
\ge A(3A-2t^2)+D^3>0
\]

because 3A-2t²>=t²-3>0 for t>=11. Also B-2t-h>0 and the reconstructed entries all lie in [1,M]; direct calculation gives ad-uv=1 and Q=1. Invoke Theorem 1. QED.

### Quantitative family size

For every integer t>=16 and 0<=h<=floor(sqrt(t)/2), the inequality above holds: 4h+3(h-1)^2+12=3h²-2h+15<=3t/4+15<=4t. This gives at least floor(sqrt(t)/2)+1 exactly solved inputs per t. Different certified pairs (t,h) generate different M: otherwise two different unordered pairs would each be the unique Q=+1 optimum at the same M, contradicting Theorem 1. Therefore the number of such M<=X is Omega(X^(3/4)); for sufficiently large X take t in [ceil(sqrt(X)/4), floor(sqrt(X)/2)] and the displayed h range, where M<2t²<=X. This is an explicit sparse-but-growing family, not an asserted density-one set.

## Exact verification

Companion source R749SUT_NEAR_SQUARE_ZERO_GAP_CERT.py (Python standard library, exact integers only) tested all 11,713 qualifying (t,h) with 11<=t<=600 against a complete, independent Q=+1 factor-pair oracle; it also checked Theorem 1 on B=6..2000 with 241 certified candidate pairs. Local execution returned PASS; the smallest scaled strict-comparison value 64G was 6,125,248. An additional sample t=10^6,h=500 was checked arithmetically, but not by full oracle. The results JSON records the exact scope. The infinite result is the preceding proof, not an extrapolation of the finite checks.

The associated WBRC two-Port integer matrix remains an auxiliary observer. Transferring it to native X6 requires an admitted P000-consistent triadic Cell/Link/Port event and a source-preserving observer mapping with resource and causal-time permission; that event has not been supplied by these computations.

## Unfinished scientific units

1. Characterize exactly which general integers B admit zero-gap global Q=+1 optimizers and characterize any near-competitive factor pairs outside the sufficient criterion.
2. Add the constant-operation certificate as a fast path to the existing R749SUS quotient-plateau algorithm without changing its exact fallback; account separately for finding a factor pair from arbitrary B.
3. Obtain independent review of the upstream R749SUO all-M sign classification and establish a properly typed native-X6 mapping if that application is pursued.

Research identity from original registration receipt: EM-DIRECT-2CD81E, SID MCP-c40e95eadedb4b95ad8159a93e814986, RA-8D8EB5C636553ADAB3BD87AE. Independent portable research; no shared X6 CLAIM and no formal Result.
