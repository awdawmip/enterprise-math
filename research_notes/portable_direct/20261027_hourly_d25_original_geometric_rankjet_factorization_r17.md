# D25/LIFT R17 — Original geometric rank-jet source, genuine 733 obstruction and a different Hensel root

Date: 2026-10-27. Research lane: chatgpt-research-hourly-enterprise-math-20260923 (never maintenance). Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; immutable publication: TP2-B6F4FC938FF94941C1B7. **Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged.**

**AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.** This source is a proven and exact-checked auxiliary finite rank relation, not the original-class CM/Frobenius experiment, Source-native checkpoint, Result, independent Driver review, native six-axis physics statement or task completion.

## Consumed results and new problem

Use without recrediting prior genuine original-coefficient finite-face identity and four actual cutoff sources (20261026_hourly_d25_original_parameter_diagonal_source_bridge_r15.md), positive complement (20261026_hourly_d25_original_positive_complement_r15.md), and the R16 true Green-weighted rank-sign flux (20261027_hourly_d25_original_full_rank_flux_r16.md). The Green port first-digit cancellation is **observer-specific** and does not by itself imply cancellation at fixed geometric weight 2^n. The previous p=733 free-Ward seam root 534359 mod 733² is from yet another operator.

**New question:** at the actual original parameter theta=-p/6, what precise constraint links fixed-geometric finite-face sources, the geometric rank moment and its first rank jet? Does a p=733 geometric cancellation erase authentic E sources, and does the original carrier's own p-adic Hensel root coincide with the free Ward seam?

## Typed ordered carrier

For prime p=6m+1 >=7, work over R=Z_(p); L=1-2m, N=2m-1. Set theta=-p/6 and

$$
f_r=f_r(\theta)=\frac{(1/6)_r(1/3)_r}{(r!)^2},\quad
\beta_r=f_r/p^2\in R^\times\quad(2m<r<p).
$$

For actual ordered pairs (j,ell) with 1<=j,ell<=2m and rank n=ell-j, define

$$
V_n^h=\sum_{\ell-j=n}j^h f_j\beta_{p-\ell},\quad
Z_n=2V_n^1-(p-n)V_n^0,\quad Z_{N+1}=0.
$$

The real four finite cutoff origin sources (two for each rank direction) are

$$
E_n=\begin{cases}
2(m+\theta)^2\beta_{p-n-1}
 -(6m^2-8m\theta+2\theta^2)f_{2m-n}\beta_{4m},&n\ge0,\\
(20m^2-14m\theta+2\theta^2)f_{-n}\beta_{p-1}
 +(2m\theta-2\theta^2)f_{2m}\beta_{p-(2m+n+1)},&n<0.
\end{cases}
$$

The original-parameter identity already proved from the bivariate Hasse master is

$$
E_n=(p-n)Z_n-(p-n-\tfrac12)Z_{n+1}.\tag{1}
$$

For any p-adic unit z define **distinct** finite Laurent observables

$$
O_p(z)=\sum_{n=L}^{N}z^n Z_n,\quad
J_p(z)=zO_p'(z)=\sum_{n=L}^{N}n z^n Z_n,\quad
G_p(z)=\sum_{n=L}^{N}z^n E_n.
$$

Neither G nor O is the original Clausen Q_p or the R16 Green-weighted flux. Positive/infinity and the independent ordered high-high corner remain separate sources.

## Theorem A — exact geometric source-to-rank-jet operator

**For every target prime and unit z**, the following rational R-identity holds:

$$
\boxed{
G_p(z)=\left(p-\frac{p+\frac12}{z}\right)O_p(z)
-\left(1-\frac1z\right)J_p(z)
+\left(p-L+\frac12\right)z^{L-1}Z_L.
}\tag{2}
$$

**Proof.** Multiply (1) by z^n and sum over the *actual finite carrier*, not an infinite formal one. After shifting the Z_(n+1) terms, the right endpoint disappears solely by the established real cutoff Z_(N+1)=0. The leftmost coefficient is (p-L)z^L Z_L. For interior L<n<=N, the Z_n coefficient is

$$
z^n\left[(p-n)-(p-n+\tfrac12)z^{-1}\right]
=z^n\left[p-(p+\tfrac12)z^{-1}-(1-z^{-1})n\right].
$$

Restoring the left coefficient adds precisely (p-L+1/2)z^(L-1) Z_L, proving (2) with no suppressed finite-face origin. All denominators are units in R. QED.

At **fixed original geometric z=2**:

$$
\boxed{
G_p(2)=\frac{2p-1}{4}O_p(2)-\frac12J_p(2)
+\frac{2p-2L+1}{4}\,2^L Z_L.
}\tag{3}
$$

The unique left ordered pair (j,ell)=(2m,1) yields Z_L=-4m f_(2m) beta_(p-1), with valuation exactly one. Therefore

$$
\boxed{
G_p(2)\equiv-\frac14O_p(2)-\frac12J_p(2)\pmod p.
}\tag{4}
$$

In particular, if O_p(2) vanishes modulo p, the genuine finite-face geometric source G_p(2) vanishes iff the rank jet J_p(2) also vanishes. This is not the R16 Green-port cancellation theorem.

The exact separately oriented sources, retaining the n=0 interface, satisfy

$$
\begin{aligned}
G_-={}&(p-L)z^LZ_L+
\sum_{n=L+1}^{-1}z^n[(p-n)-(p-n+\tfrac12)/z]Z_n
-(p+\tfrac12)z^{-1}Z_0,\\
G_+={}&pZ_0+
\sum_{n=1}^{N}z^n[(p-n)-(p-n+\tfrac12)/z]Z_n.
\end{aligned}\tag{5}
$$

These are proved by the same shifted finite sum separately on n<0 and n>=0.

## Theorem B — exact mod-p factorization from genuine ordered original pairs

Let a_j=f_j modp for 1<=j<=m and b_ell=beta_(p-ell) modp for 1<=ell<=2m. Set, for r=0,1,2,

$$
A_r(z)=\sum_{j=1}^{m} j^r a_j z^{-j},\qquad
B_r(z)=\sum_{\ell=1}^{2m}\ell^r b_\ell z^\ell\quad \in\mathbb F_p[z,z^{-1}].
$$

**Then**, at any z !=0 modp,

$$
\boxed{O_p(z)=A_1(z)B_0(z)+A_0(z)B_1(z)\pmod p,}\tag{6}
$$

$$
\boxed{J_p(z)=A_0(z)B_2(z)-A_2(z)B_0(z)\pmod p.}\tag{7}
$$

**Proof.** The exact original ratio f_(j+1)/f_j=(6j+1)(3j+1)/(18(j+1)²) has its first p numerator factor at j=m. Thus f_j=0 modp on m<j<=2m. On any surviving actual ordered pair of rank n=ell-j, the coefficient of Z_n is 2j-(p-n)=j+ell modp. This makes O the product of the two one-variable moment families in (6). Multiplying by the rank ell-j changes the factor to (ell-j)(j+ell)=ell²-j², giving (7). This uses the **actual** constrained pair carrier rather than a free formal Ward vector. QED.

The factorial route for b_ell is independently computable by the R15 formula

$$
b_\ell\equiv
\frac{(-1)^m m!(2m)!(p-\ell-m-1)!(p-\ell-2m-1)!}
{18((p-\ell)!)^2}\pmod p.
$$

The attached program computes this using factorials **separately** from the original rational recurrence and genuine E-source side.

## Exact source-tagged finite witnesses

Residues modulo the prime at fixed original z=2:

| p | (A0,A1,A2) | (B0,B1,B2) | (O-,O+) | (G-,G+) | O | J | G |
| ---: | :--- | :--- | :--- | :--- | ---: | ---: | ---: |
| 13 | (12,7,10) | (9,12,8) | (10,2) | (5,2) | 12 | 6 | 7 |
| **733** | **(732,1,367)** | **(577,577,40)** | **(433,300)** | **(285,429)** | **0** | **38** | **714** |

At p=733, A0=-A1 and B0=B1 **on genuine original coefficients**, hence O_733(2)=0 mod733. Nevertheless J_733(2)=38, so

$$
\boxed{G_{733}(2)=-38/2=714\not=0\pmod{733}.}\tag{8}
$$

This is a bona fide finite-face information-loss certificate: fixed geometric first-digit state moment cancellation does not erase its rank jet or finite-face source. R16's *different Green-weighted* port residues F_+/p=129 and F_-/p=604 cancel at 733, but the present genuine *geometric-source* port residues 429 and 285 sum to 714, NOT zero. Neither port represents the separately ordered high-high or positive infinity.

## Second new unit — Hensel root of genuine original moment, not the free seam

The genuine O_733(z) is finite Laurent with p-adic coefficients. Equation (6) proves O_733(2)=0 mod733, while equation (7) gives

$$
O'_{733}(2)=J_{733}(2)/2=19\not=0\pmod{733}.
$$

By Hensel's lemma there exists exactly one z-dagger in 2+733 Z_733 for which **this genuine original moment** vanishes to all digits. The first two explicit exact lifts:

$$
\boxed{z^\dagger=38851=2+733\cdot53\pmod{733^2},}
$$

$$
\boxed{z^\dagger=257400282=38851+733^2\cdot479\pmod{733^3}.}\tag{9}
$$

Independent original-pair source computations give

$$
\begin{aligned}
O_{733}(2)&=337753939\pmod{733^3},\\
O_{733}(38851)&=229959692=733^2\cdot428\pmod{733^3},\\
O_{733}(257400282)&=0\pmod{733^3}.
\end{aligned}
$$

These lifts **do not** agree with the earlier free-Ward seam z_* =534359 mod733². Indeed, using the same genuine O

$$
\boxed{O_{733}(534359)=280739=733\cdot383\not=0\pmod{733^2}.}\tag{10}
$$

The true geometric carrier and free seam exhibit **different higher-digit defects even though each has first-digit resonance at z=2**. Changing z changes the observed function, so this result cannot substitute for original fixed-z=2 Clausen Q or prove a final cross-source WZ cancellation.

## Evidence and precise remaining actions

Companion script: **20261027_hourly_d25_original_geometric_rankjet_factorization_r17_check.py** (standard library, integers modulo p³ and independent rational Fraction audits). **Actually executed PASS:** all 80 p≡1 mod6 primes 7<=p<=997; complete original coefficient normalization, every genuine four-face Ward rank equation, (2)/(5), independent factorial (6)/(7), p13/p733 source witness, two p733 moment Hensel digits. Independent exact rational audits p=7,13,19 also passed. These are **author checks**, not a native CM/Frobenius test, Lean proof or independent Driver review. General identities are proved by finite algebra, while global Hensel existence uses the simple-root criterion and the exact p733 finite certificates.

**BRC COMPOSE_APPLIED:** carrier is actual ordered (j,ell), positive/negative rank and true four-source provenance, finite prime valuations, rank jet and forward observation. Factorization (6)/(7) is safe for declared *mod-p O,J readouts*; it cannot replace six separately labeled signed Hasse ports, higher p-adic digits, original Q, positive infinity, or independent ordered high-high sector. Auxiliary rank indices are external arithmetic, not Heartbeat Native X6 spatial axes; P000 is unchanged.

**Next smallest unit:** bring authentic O,J,G at fixed z=2 into the proved Hasse signed 3+2+1 anti-diagonal six-channel source transport. Determine whether its real separate J/E couplings cancel the 733 rank-jet obstruction while retaining p13 nonresonant finite face, independently oriented infinity, and high-high. If impossible, produce a full source-labeled counterexample, not a free-vector no-go.

Mother D25/LIFT/JT2 remains OPEN: same-original-class H0/B0, [X]U modp², Frobenius eta and kappa, Delta_p-R_p, native original-class experiment and independent review all remain pending. Current paper is **not** a canonical Source checkpoint. Historical Source frontier, own old staging, researcher contribution history, frozen scientific pin and logical Research/maintenance separation must be preserved. Control support remains awdawmip/enterprise-math#1558.