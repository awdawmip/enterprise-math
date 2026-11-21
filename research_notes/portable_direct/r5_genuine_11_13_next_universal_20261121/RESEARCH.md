# R5 — 真正联合约束下本原11、13次单位根的全门槛下一阶非零定理

Scientific date: 2026-11-21 (Asia/Shanghai). Status: **AUTHOR_EXACT_DERIVATION / EXACT_INTEGER_CROSSCHECKED / NOT_REVIEWED**. Mode: frozen scalar R5 cost observer; P000, ACTIVE worldview and frozen input pin unchanged. This note corrects affected downstream Laurent computations after the exact overlapping-event counterexample at [75d986aa](https://github.com/awdawmip/enterprise-math/blob/75d986aa23b68a7ecf9b29dc1006f0e322b35a15/research_notes/portable_direct/r5_true_intersection_audit_20261121/RESEARCH.md). It continues the [genuine-17 all-threshold frontier](https://github.com/awdawmip/enterprise-math/blob/caeceb3e790ad9d9ef2813bbfa6a6bf66cdbb0fd/research_notes/portable_direct/r5_true17_next_universal_20261121/RESEARCH.md), with no new formal Task CLAIM, Result or independent acceptance.

## Exact statement

Keep the original prices \(214,\ldots,314\), and failure events
\(E_i=\{\sum_{p\in S_i}a_p<m\}\), with
\(S_0=\{214,\ldots,218\}\),
\(S_1=\{214,216,217,218,219,220,221\}\),
\(S_2=\{215,216,217,218,219,220,221\}\),
\(S_3=\{223,\ldots,290\}\),
\(S_4=\{296,\ldots,312\}\).
Let \(F_m(q)=R_m(q)/\prod_{p=214}^{314}(1-q^p)\) count the union of the five failures. Here the finite inclusion-exclusion numerator \(R_m\) is formed using **all original event-specific inequalities simultaneously**, not a bound on the cardinality of their union.

For every positive integer \(m\):

1. At every primitive 11th root \(\zeta\), \(R_m(\zeta)\ne0\) for \(m\bmod11\in\{1,\ldots,6\}\); for \(m\bmod11\in\{0,7,8,9,10\}\), \(R_m(\zeta)=0\) and \(D R_m(\zeta)\ne0\), where \(D=q\,d/dq\).
2. At every primitive 13th root \(\eta\), \(R_m(\eta)\ne0\) for \(m\bmod13\in\{1,\ldots,8\}\); for \(m\bmod13\in\{0,9,10,11,12\}\), \(R_m(\eta)=0\) and \(D R_m(\eta)\ne0\).
3. Consequently the genuine cost counting function has a nonzero primitive-11 Fourier term of degree \(N^8\) or \(N^7\), and a nonzero primitive-13 term of degree \(N^7\) or \(N^6\). Thus
\[
 \boxed{11\mid M_m(O_m(N^6)),\qquad 13\mid M_m(O_m(N^5))\quad(\forall m\ge1).}
\]
Here \(M_m(O_m(N^a))\) is the least coefficient-quasipolynomial period of a representation of the cost count with error \(O_m(N^a)\).
4. Combining these **verified necessary factors** with the corrected primitive-16 all-\(m\) lower bound and genuine primitive-17 all-\(m\) lower bound yields
\[
 \boxed{\forall m\ge1,\quad \operatorname{lcm}(11,13,16,17)=38\,896\mid M_m(O_m(N^3)).}
\]
This is a uniform lower bound, **not** an assertion of the exact minimum period. Historical collapsed-intersection period tables are not imported.

## Why the five-event model reduces exactly at these roots

Write \(A=E_0\cup E_1\cup E_2\); let \(R_A,R_3,R_4\) be their numerator polynomials relative to the unrestricted Euler products. The price groups underlying \(A,E_3,E_4\) are disjoint, so in the polynomial ring
\[
 R_m=1-(1-R_A)(1-R_3)(1-R_4).
\]
For both \(d=11\) and \(d=13\), the set \(S_3\) includes at least five multiples of \(d\), and \(S_4\) contains exactly two multiples of \(d\): \((297,308)\) for 11 and \((299,312)\) for 13. Hence at every primitive \(d\)-th root, \(R_3=R_4=DR_3=DR_4=0\). Therefore
\[
 R_m(\zeta)=R_A(\zeta),\qquad DR_m(\zeta)=DR_A(\zeta).
\]
This derivative reduction is exact at the designated root and does not erase the overlap of \(E_0,E_1,E_2\).

Let \(r=220\) for \(d=11\) and \(r=221\) for \(d=13\). Only \(E_1,E_2\) contain \(r\), and no price of \(S_0\) is divisible by \(d\). Put
\(W_0(q)=\prod_{p\in S_0}(1-q^p)\),
\(W_1=\prod_{p\in S_1\setminus\{r\}}(1-\zeta^p)\),
\(W_2=\prod_{p\in S_2\setminus\{r\}}(1-\zeta^p)\),
and \(W=\prod_{p\in (S_0\cup S_1\cup S_2)\setminus\{r\}}(1-\zeta^p)\).
For each genuine event conjunction \(I\), let \(P_{I,m}(\zeta)\) be its *separately constrained* finite multiplicity sum. Then
\[
 \boxed{DR_m(\zeta)=DR_{0,m}(\zeta)-r\,B_m(\zeta)}
\]
where
\[
 B_m=W_1P_{1,m}+W_2P_{2,m}
 -W(P_{01,m}+P_{02,m}+P_{12,m})+WP_{012,m}.
\]
The sign and factor \(r\) come from the exact derivative \(D(1-q^r)|_{q=\zeta}=-r\).

## Genuine max-load kernels and global rational denominator

Use \(a=a_{214}\), \(b=a_{215}\), \(u=\sum_{p=216}^{218}a_p\), \(j=\sum_{p=219}^{221}a_p\). The three distinct original loads are
\[
 L_0=a+b+u,\quad L_1=a+u+j,\quad L_2=b+u+j.
\]
At \(\zeta\), group the complete homogeneous coefficients for \(u,j\) into their exact partial-fraction characters \(U\in\{\zeta^{216},\zeta^{217},\zeta^{218}\}\) and \(V\in\{\zeta^{219},\zeta^{220},\zeta^{221}\}\). The three characters in each group are distinct. Set \(X=\zeta^{214}\), \(Y=\zeta^{215}\), \(T\) for the threshold-series variable. Define \(P_I(T)=\sum_{m\ge1}P_{I,m}(\zeta)T^{m-1}\). Exact cone enumeration gives
\[
P_1={1\over(1-T)(1-XT)(1-UT)(1-VT)},\qquad
P_2={1\over(1-T)(1-YT)(1-UT)(1-VT)},
\]
\[
P_{01}={1-YVT^2\over(1-T)(1-XT)(1-UT)(1-YT)(1-VT)(1-YVT)},
\quad
P_{02}={1-XVT^2\over(1-T)(1-YT)(1-UT)(1-XT)(1-VT)(1-XVT)},
\]
\[
P_{12}={1-XYT^2\over(1-T)(1-UT)(1-VT)(1-XT)(1-YT)(1-XYT)},
\]
\[
 \boxed{P_{012}={1-XYVT^3\over(1-T)(1-UT)(1-XT)(1-YT)(1-VT)(1-XYVT^2)}}.
\]
These are the kernels for each *separate* maximum constraint, and are then linearly combined using the exact group partial fractions. For the triple intersection, \(\max(a+b,a+j,b+j)=a+b+j-\min(a,b,j)\); a three-cone disjoint partition, assigning ties in order \(a\), then \(b\), then \(j\), yields the last numerator exactly. In both moduli \(XY=\zeta^{429}=1\), an identity used only after retaining the separate constraints.

Each linear factor divides \(1-T^d\); each quadratic factor divides \(1-T^{2d}\). After actual numerator cancellations the maximum pole multiplicity among all the six kernel types, every character pair \(U,V\) and every \(2d\)-th root is **two**, as exhaustively checked by exact integer modular congruences (no floating point root evaluation). The potentially triple root at \(T=1,V=1\) cancels once against the numerator of \(P_{12}\) or \(P_{012}\). Thus all kernels' reduced denominators divide \((1-T^{2d})^2\). Their numerator degree after common-denominator multiplication is at most \(4d-4\).

For the single event, \(R_{0,m}\) has threshold series
\[
 \sum_{m\ge1}R_{0,m}(\zeta)T^{m-1}
 ={W_0(\zeta)\over(1-T)\prod_{p=214}^{218}(1-\zeta^pT)}.
\]
The five residues are distinct and nonzero modulo \(d\), so this denominator divides \(1-T^d\). Its numerator at that denominator has degree \(d-6\), yielding exact \(d\)-periodicity and zeros beyond \(m=d-5\) in one base cycle. Differentiating in \(q\) **before** evaluating \(q=\zeta\) gives denominator dividing \((1-T^d)^2\), with numerator degree at most \(2d-6\) after that denominator. Converting to \((1-T^{2d})^2\) raises the bound to \(4d-6\). Hence
\[
 \boxed{\sum_{m\ge1}DR_m(\zeta)T^{m-1}={H_d(T)\over(1-T^{2d})^2},\qquad \deg H_d\le4d-4.}
\]
The exact all-\(m\) recurrence is therefore
\[
 \boxed{DR_{m+4d}-2DR_{m+2d}+DR_m=0\quad(m\ge1).}
\]

## Complete finite base identities

For \(d=11\), take \(r=7,8,9,10,11\); for \(d=13\), \(r=9,10,11,12,13\) (the final residue denotes zero). In the full \((d-1)\)-coordinate basis of \(\mathbb Z[\zeta]\), two independent exact algorithms establish
\[
 DR_{r+2d}=DR_r+DR_{r+d},\qquad DR_{r+3d}=2DR_{r+d}.
\]
With \(A_r=DR_r\) and \(B_r=DR_{r+d}\), the recurrence thus yields, for **every** \(k\ge0\),
\[
 DR_{r+kd}=
 \begin{cases}A_r+\frac{k}{2}B_r&k\text{ even},\\
 \frac{k+1}{2}B_r&k\text{ odd}.\end{cases}
\]

The first cyclotomic basis coordinates of the complete exact vectors are:

| Root order | \(r\) | \([z^0]A_r\) | \([z^0]B_r\) |
|---:|---:|---:|---:|
|11|7|3091|4862|
|11|8|33|-2354|
|11|9|-3938|-12056|
|11|10|-10087|-14454|
|11|11|4433|9746|
|13|9|-2379|-8515|
|13|10|-2808|-2743|
|13|11|494|-2769|
|13|12|-4134|-5616|
|13|13|5122|5824|

Each pair is either same-sign or opposite-sign with \(|B_r|>|A_r|\). Thus the first coordinate of each displayed even/odd expression is nonzero for every \(k\ge0\). The complete vector is nonzero in \(\mathbb Q[z]/\Phi_d(z)\). Since \(\Phi_{11},\Phi_{13}\) are irreducible, this proves nonvanishing at **all** primitive conjugates.

## Verification scope and provenance

All finite checks use exact integer cyclic-ring convolution reduced by \(\Phi_d\); no floating point arithmetic. Algorithm 1 constructs threshold-series coefficients from six max-of-load kernels. Algorithm 2 independently enumerates the actual per-event inequalities on \(a,b,u,j\). Full-vector comparisons pass at eleven selected thresholds for each prime (including all ten relevant \(A_r,B_r\) bases, plus \(m=1\)). Algorithm 1 covers every threshold \(1\le m\le44\) (11) and \(1\le m\le52\) (13), including both 4-block exact base identities. An independent modular pole-multiplicity check covers all character pairs and all \(2d\)-th roots for six kernel types. The infinite extension follows from the displayed **rational function identity and exact recurrence**, not from finite extrapolation. Source scripts, exact base vectors and summaries accompany this note.

Frozen scientific model and exact incidences: [correction @75d986aa](https://github.com/awdawmip/enterprise-math/blob/75d986aa23b68a7ecf9b29dc1006f0e322b35a15/research_notes/portable_direct/r5_true_intersection_audit_20261121/RESEARCH.md). Genuine max kernels predecessor: [primitive-17 correction @caeceb3e](https://github.com/awdawmip/enterprise-math/blob/caeceb3e790ad9d9ef2813bbfa6a6bf66cdbb0fd/research_notes/portable_direct/r5_true17_next_universal_20261121/RESEARCH.md).

This is a scalar cost observer within Enterprise Math, not a native X6/Heartbeat physical or BRC evolution claim. Residual/overlap information is preserved exactly; no unnecessary BRC detour is imposed. Author review: **NOT_REVIEWED**. No independent Driver review, native CLAIM or shared Result is asserted.

## Next discriminating unit

Re-evaluate the affected primitive roots at the precision \(O_m(N^3)\), including lower-order non-leading poles at 11/13 and all other root orders with pole order at least five, then recombine *only* separately certified root factors into a strict numerical minimal period. In parallel, bind this newly saved genuine-incidence source to the originating Research Activity using an authenticated current-session CAS/immutable readback; this metadata task is distinct from the scientific proof.
