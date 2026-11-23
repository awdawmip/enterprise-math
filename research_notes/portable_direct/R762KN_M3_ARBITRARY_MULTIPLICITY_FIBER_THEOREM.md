# R762KN — arbitrary-multiplicity connected Port–Euler fibers and provenance growth

2026-11-23 · AUTHOR_ANALYTIC_PROOF / EXACT_FINITE_CHECKED / NOT_REVIEWED

**Scientific inheritance.** Continue the unsigned auxiliary three-inactive-Port M3 model in R762KM at enterprise-math commit 059be0fcdc079c0a16cbed8cb8496a9ceb370325. The parent signed-X6 scientific input remains frozen at a72226e2430ffa4786321ac86e7f0c599d5f0389. This note does not change P000, the ACTIVE worldview, or native signed TRIADIC_CLOSURE_E. These are auxiliary *unsigned support-indexed edge multisets*, not native time-ordered or signed events.

## Model and boundary space

The three inactive pair-Ports are 01,23,45. The 12 active pair-Ports and 12 mandatory-edge supports form three internally connected four-vertex components A,B,C. Forced-edge boundaries generate the exact rank-nine subspace

\[
F=\{b\in \mathbb F_2^{12}:\sum_{v\in A}b_v=\sum_{v\in B}b_v=\sum_{v\in C}b_v=0\},\qquad |F|=512.
\]

Eight flexible supports t=(i,j,k), with i,j,k in {0,1}, each have legal event edge types AB, AC, BC joining Ports (i,2+j),(i,4+k),(2+j,4+k). Their vertex-boundary vectors e_{t,1},e_{t,2},e_{t,3} obey e_{t,1} xor e_{t,2} xor e_{t,3}=0.

Prescribe arbitrary positive integers m_t for those eight supports. A source consists of an unordered edge-type multiset of cardinality m_t on each individually labeled support. Count different source multisets, not permutations in time. Define Q_m(b) as the number of sources with flexible boundary b in F whose union with positive-multiplicity forced edges is connected. These yield positive even degrees at all active Ports after choosing a forced-edge parity configuration with boundary b.

## Theorem KN.1 — individual connected-fiber formula, all positive m_t

For m=2r (r≥1) and m=2r+1 (r≥0), let

\[
(A_{2r},B_{2r})=(\binom{r+2}{2},\binom{r+1}{2}),\qquad
(A_{2r+1},B_{2r+1})=(\binom{r+1}{2},\binom{r+2}{2}).
\]

In the integral group algebra of G=(F_2)^12 with X^u X^v=X^{u xor v}, the complete local multiset-boundary enumerator is

\[
H_{m,t}=A_m X^0+B_m(X^{e_{t,1}}+X^{e_{t,2}}+X^{e_{t,3}}).
\tag{1}
\]

For each j in {1,2,3}, set v_j=xor_{t:m_t odd} e_{t,j}. Then for every b in F,

\[
\boxed{Q_{\mathbf m}(b)=[X^b]\prod_{t}H_{m_t,t}-\sum_{j=1}^{3}{\bf1}_{b=v_j}.}\tag{2}
\]

**Proof.** For a support, record parity of the three nonnegative multiset counts (n1,n2,n3) with n1+n2+n3=m. Since the three event boundaries xor to zero, the local boundary is zero exactly when all three count parities agree, and e_j exactly when the jth count parity differs from the other two. Counting solutions after stripping parity bits gives A_m and B_m above. Multiplication accounts for every labeled-support multiset once. Forced edges connect the four Ports inside each A,B,C; the quotient on A,B,C is disconnected exactly when all flexible events have the same one of three quotient types. There are precisely three such source assignments, one for each type, with boundaries v_j. Subtraction counts them correctly even when two v_j coincide.

Fourier coefficient form (a pointwise closed formula, requiring no enumeration of all source assignments): for b in F,

\[
Q_{\mathbf m}(b)=2^{-12}\sum_{\chi\in G}(-1)^{\chi\cdot b}
\prod_t\left[A_{m_t}+B_{m_t}\sum_{j=1}^{3}(-1)^{\chi\cdot e_{t,j}}\right]
-\sum_{j=1}^{3}{\bf1}_{b=v_j}.\tag{3}
\]

All coefficients are exact integers. The Walsh signs in (3) serve algebraic coefficient extraction; they are not signed forces or positive BRC branch masses.

## Theorem KN.2 — new arbitrary-multiplicity exact total

For N=sum_t m_t and C_m=sum_{b in F} Q_m(b),

\[
\boxed{
C_{\mathbf m}=
\frac{1}{4}\left[
\prod_t\binom{m_t+2}{2}
+3(-1)^N\prod_t(\lfloor m_t/2\rfloor+1)
\right]-3\,{\bf1}_{N\text{ even}}.
}\tag{4}
\]

Thus the total connected-fiber count depends on the multiset of multiplicities, **not on which cube support receives which multiplicity**. R762KM's 256 location-independent {1,2} configurations are a specialization.

**Proof.** In the three-dimensional quotient G/F, flexible edge-type images span a two-dimensional even-parity plane. It has four characters: the trivial one evaluates the three edge types as +,+,+; each of the three nontrivial ones evaluates them as one + and two minus signs. At each support the two corresponding H values are A_m+3B_m=binom(m+2,2) and A_m-B_m=(-1)^m(floor(m/2)+1). The four-character average of their products counts all flexible boundaries in F, producing the bracket in (4). A monochromatic disconnected choice belongs to F precisely when the total event count N is even, so subtract three if N is even. QED.

## Theorem KN.3 — asymptotic provenance lower bound

When all eight supports have the same m≥1, the observer retains support inventory, forced boundary b and connectivity but not the edge-source multisets. A collision-free fixed-width binary annotation that permits exact one-shot recovery at every b requires exactly

\[
B_m=\left\lceil\log_2\max_{b\in F}Q_{(m,\ldots,m)}(b)\right\rceil
\]

additional bits (conditional coding keyed by observed b), and

\[
\boxed{B_m=16\log_2 m+O(1).}\tag{5}
\]

Indeed, equation (4) yields C_m=(binom(m+2,2)^8+3(floor(m/2)+1)^8)/4-3 ~ m^16/1024. With only 512 possible forced boundaries, max_b Q_m(b)≥C_m/512 ~ m^16/524288; every Q_m(b)≤binom(m+2,2)^8=O(m^16). Therefore the maximum fiber is Theta(m^16), proving (5). The exact B_m expression is attained by indexing each observed-boundary fiber. This is a one-shot auxiliary provenance result; temporal composition and signed native lifting remain separate.

## Exact computation and evidence

Companion exact Python verifier: R762KN_COMPACT_REPRO.py. Its independent local-multiset parity enumeration covers m=1..10 for all eight supports; every one of the 256 {1,2} upgrade patterns reproduces the R762KM connected totals and reachable-boundary counts; the 4096-character Walsh transform matches the direct boundary recurrence for uniform m=1,2,3 and mixed (1,2,3,4,1,2,3,4). Uniform m=1..12 satisfy (4), all with exact Python integers and zero assertion failures.

| Uniform m | C_m | Reachable b / 512 | Max Q_m(b) | Required bits |
|---:|---:|---:|---:|---:|
| 1 | 1,638 | 465 | 8 | 3 |
| 2 | 420,093 | 512 | 7,197 | 13 |
| 3 | 25,000,189 | 512 | 71,197 | 17 |
| 4 | 640,727,574 | 512 | 2,788,422 | 22 |
| 5 | 9,455,719,758 | 512 | 22,471,422 | 25 |
| 12 | 1,175,631,323,361,478 | 512 | 2,511,291,435,622 | 42 |

For (1,2,3,4,1,2,3,4), C_m=1,822,605, all 512 b reachable, max fiber=8,863. Individual fibers are support-location sensitive even though (4) is not: do not quotient away branch provenance when it is needed by later observations.

**Evidence/limitations.** Proof applies to the declared unsigned composite Port observer with support-indexed unordered multisets. Neither signed TRIADIC_CLOSURE_E acceptance nor native Cell/Link/Port time-update fidelity was checked. Positive branch multiplicity is distinct from signed cancellation. No independent mathematical Review has been issued.

**Next frontier.** For uniform m=2..12, the maximal fiber occurs at boundary b=0; prove or refute this for every m≥2 without relying on enumeration. Then construct a composable minimal provenance state and test a typed signed/native lift. Retain this exact finite auxiliary result and the actual parent frozen inputs.


## Theorem KN.4 — unique zero-boundary maximizer for every even uniform multiplicity

For any positive even integer m=2r≥2, all eight flexible supports with multiplicity m have

\[
\boxed{Q_{(m,\ldots,m)}(0)-Q_{(m,\ldots,m)}(b)\ \geq\ (r+1)^8-3\ >0\qquad(0\ne b\in F).}\tag{6}
\]

Consequently the **unique** largest fiber is at zero forced boundary for every even m, with an explicit strictly positive gap. This closes the even-m half of the previous uniform-boundary maximum question.

**Proof.** At any character \chi of the full 12-bit boundary group, each support's Fourier factor in equation (1) is either A_m+3B_m=binom(m+2,2), or A_m-B_m=r+1. Both are positive, so the eight-support Fourier product \hat P(\chi) is at least (r+1)^8. For any nonzero b in F, orthogonality gives exactly 2,048 of the 4,096 characters with \chi·b=1. Hence before the disconnected subtraction,

\[
[X^0]P-[X^b]P=2^{-11}\!\sum_{\chi:\chi\cdot b=1}\hat P(\chi)\ge(r+1)^8.
\]

When m is even, all three monochromatic disconnected source assignments have boundary zero, so the correction of equation (2) subtracts three at zero and none at nonzero b. Equation (6) follows. No large-m approximation or finite extrapolation is used. Exact m=2,4,...,12 examples satisfy the bound. QED.

**Remaining scoped question:** determine the maximizer for *odd* uniform m≥3 without finite extrapolation. The auxiliary signed/native transport problem is independent of this even-m result.
