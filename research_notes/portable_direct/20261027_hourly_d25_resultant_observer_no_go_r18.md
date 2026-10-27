# D25/LIFT R18 — Geometric finite-face resultant and prime-specific precision obstruction

Date: 2026-10-27. Logical Research conversation: chatgpt-research-hourly-enterprise-math-20260923 (distinct from CONTROL_PLANE_MAINTENANCE). Formal Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. **Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged.**

**AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.** This is original-parameter *auxiliary finite ordered carrier mathematics*, not a native original-class CM/Frobenius experiment, formal Source checkpoint, original Clausen scalar, independent Driver review or proof of all six Hasse source cancellation.

## Prior work and exact problem

Consume without recrediting the R13/R15 original-parameter bivariate Hasse finite-source identity and the R17 geometric/rank-jet factorization. Let p=6m+1 be prime, L=1-2m, N=2m-1, theta=-p/6 and

\[
f_r=\frac{(1/6)_r(1/3)_r}{(r!)^2},\qquad
\beta_r=f_r/p^2\in\mathbb Z_{(p)}^\times\quad(2m<r<p).
\]

Define the real *ordered* low/high cells, for 1<=j,ell<=2m and n=ell-j,

\[
Z_n=\sum_{\ell-j=n}(j+\ell-p)f_j\beta_{p-\ell},
\qquad E_n=(p-n)Z_n-(p-n-\tfrac12)Z_{n+1},\quad Z_{N+1}=0.
\]

The E_n are the four distinct **real finite truncation face sources** (two at each rank orientation), not invented free-vector Ward data. The oriented positive infinity, high/high ordered corner, and six separately labeled signed Hasse channels remain separate. For a p-adic unit geometric weight z, set

\[
O_p(z)=\sum_{n=L}^{N}z^nZ_n,\quad
J_p(z)=zO'_p(z),\quad
G_p(z)=\sum_{n=L}^{N}z^nE_n.
\]

R17 proved the *exact* finite identity

\[
G_p(z)=\bigl(p-(p+\tfrac12)/z\bigr)O_p(z)
-(1-z^{-1})J_p(z)+(p-L+\tfrac12)z^{L-1}Z_L.
\]

Because p divides Z_L, modulo p

\[
\boxed{G_p(z)\equiv-O_p(z)/(2z)-(1-z^{-1})J_p(z)\pmod p.}\tag{1}
\]

R17 proved O_733(2)=0, J_733(2)=38, G_733(2)=714 modulo 733 and constructed a local Hensel zero of O alone. The **new question** is whether changing *any* unit weight can make the two authentic observer ports O and G vanish together, and what happens to double/triple roots at higher p-adic digits.

## Theorem A — genuine two-sided twisted-Wronskian polynomial

For j<=m set a_j=f_j mod p (for m<j<=2m, f_j=0 mod p). For 1<=ell<=2m set b_ell=beta_(p-ell) mod p. Define separately sourced finite-field polynomials

\[
U_p(z)=\sum_{j=1}^{m}a_jz^{m-j},\qquad
V_p(z)=\sum_{\ell=1}^{2m}b_\ell z^{\ell-1}.
\]

Then

\[
\boxed{P_p(z):=z^{m-1}O_p(z)\bmod p
=(m+1)U_p(z)V_p(z)+z\bigl(U_p(z)V_p'(z)-U_p'(z)V_p(z)\bigr).}\tag{2}
\]

**Proof:** R17 independently established the genuine original-pair reduction O=A1 B0+A0 B1 where A0=z^(-m)U, A1=z^(-m)(mU-zU'), B0=zV and B1=z(V+zV'). Multiplying by z^(m-1) yields (2). Alternatively, directly summing (j+ell)a_j b_ell z^(ell-j+m-1) across authentic ordered pairs proves the same polynomial coefficient-by-coefficient. Its constant and leading coefficients are (m+1)a_m b_1 and (2m+1)a_1 b_(2m), both nonzero; deg P=3m-2 and P(0) != 0. QED.

At any unit root P(z)=0, J=z^(2-m)P'(z). Inserting in (1) yields

\[
\boxed{G_p(z)=-(z-1)z^{1-m}P_p'(z)\pmod p.}\tag{3}
\]

Hence **simultaneous O(z)=G(z)=0 over any residue-field extension occurs precisely when P(z)=0 and either z=1 or P'(z)=0**. The z=1 exception must not be suppressed by a squarefreeness argument. This is an observer-specific statement about the true finite ordered low/high source, not an assertion on the full Clausen scalar.

## Theorem B — 733 global no-go for all unit geometric weights

Independently compute a_j by the original finite-field ratio

\[
a_j=a_{j-1}(6j-5)(3j-2)/(18j^2),
\]

and b_ell from the independent R15 factorial expression

\[
b_\ell=(-1)^m m!(2m)!(p-\ell-m-1)!(p-\ell-2m-1)!/[18((p-\ell)!)^2]\pmod p.
\]

The executable companion builds P both by the genuine ordered pair sum and formula (2), with exact agreement for every tested prime.

For p=733, m=122, it obtains degree 364 and the **exact polynomial certificates**

\[
\boxed{\operatorname{Res}_{\mathbb F_{733}}(P_{733},P'_{733})=254\ne0,\quad P_{733}(1)=204\ne0.}\tag{4}
\]

The resultant was actually evaluated by 362 nontrivial finite-field Euclidean remainder steps, without float approximations. Therefore gcd(P,P')=1 over the algebraic closure. Exhaustive independent testing of **all 732 unit weights modulo 733** finds the unique root of P to be z=2. At this root P'(2)=357, 2^(1-m)=731=-2 mod733, so (3) gives G_733(2)=714.

Since P has no repeated roots even after residue-field extension and P(1) != 0, for **every** unit z in the full ring \(\mathbb Z_{733}^{\times}\),

\[
\boxed{(O_{733}(z),G_{733}(z))\not\equiv(0,0)\pmod{733}.}\tag{5}
\]

This also holds for unit residue weights in every finite extension: the resultant argument is algebraic, not based only on 732 enumerated base-field values. In particular, the genuine O-only Hensel deformation in R17 cannot erase the authentic finite E-source G. This is a global no-go **for the stated two ports**, not a six-channel WZ impossibility theorem and not a native CM statement.

## Theorem C — the genuine p=19 triple cancellation does not lift integrally

At p=19, m=3 the exact first-digit polynomial is

\[
P_{19}(z)=8+9z+16z^2+15z^3+3z^4+8z^5+12z^6+6z^7
\]

and

\[
\boxed{P_{19}(z)=(z+6)^3(12+17z+5z^2+18z^3+6z^4)\pmod{19}.}\tag{6}
\]

The quartic has value 7 at z=13=-6 mod19; the root z=13 has *exact multiplicity 3*, and O_19(13)=J_19(13)=G_19(13)=0 mod19. Therefore the 733 no-go does **not** hold uniformly for every target prime: this is a real prime-specific observation, not a free-vector artifact.

A new, independent exact Fraction computation of the *original* rational coefficients, beta normalization and all four finite E cutoff terms gives

\[
\boxed{O_{19}(13)\equiv G_{19}(13)\equiv 95=19\cdot 5\pmod{361},\quad
J_{19}(13)\equiv323\pmod{361}.}\tag{7}
\]

Because mod19 both first derivatives vanish at the triple root, **for every integer t**

\[
\boxed{O_{19}(13+19t)\equiv G_{19}(13+19t)\equiv95\ne0\pmod{19^2}.}\tag{8}
\]

All 19 candidate lifts mod361 were individually checked, preserving genuine ordered sources. Thus the first-digit cancellation has a nonremovable second-digit residual in the declared integral residue class.

A sharper Newton-polygon certificate uses the exact p-local polynomial \(T_{19}(z)=z^5O_{19}(z)\). Its Taylor coefficients at z=13 are, modulo361,

\[
\boxed{(c_0,c_1,c_2,c_3)=(247,304,342,122),\quad
c_k=[x^k]T_{19}(13+x).}\tag{9}
\]

Here v19(c0)=1, v19(c1),v19(c2)>=1 and c3 is a unit (c3 mod19=8). All remaining higher coefficients are p-integral. Balancing valuations of the constant term and x^3 shows that every algebraic zero near the class 13 has **v19(x)=1/3**. No integral 19-adic lift has such a fractional valuation. This is an exact precision defect rather than mere failure of a guessed Hensel correction.

## Author verification, BRC scope and continuation

**Executed PASS** of the companion Python standard-library checker on all 80 primes p=1 mod6, 7<=p<=997. Each P was constructed in two independent ways, direct genuine ordered pairs versus formula (2). Within this finite list only, p=19 was the sole non-squarefree P (gcd=(z+6)^2). The code additionally checked p733 resultant=254 with 362 Euclidean steps, its 732 unit values and p19 triple factorization; it used Fraction to audit original four cutoff sources and evaluated all 19 second-digit lifts and the four Taylor residues. All arithmetic is exact integer or Fraction with valid p-unit divisions. General claims are proved algebraically; finite checks are author verification, not independent Driver review. There is no universal prime-classification assertion.

**BRC COMPOSE_APPLIED:** preserve real (j,ell) pair origins, four finite-face source labels, separate rank derivative J, observer weight and p-adic digits; safe compression only for the declared modp O/J/G observer. Do not erase the positive-infinity port, the independent ordered high-high corner, six Hasse source labels or native CM original-class data.

**Control/status:** formal parent D25/LIFT/JT2 OPEN. Native research permission is *not* established by Git publication. Current canonical continuation was verified SUCCEEDED via research ordinary Chat Issues #6572, #6573 and #6574, retaining Source persisted_checkpoint.state=SOURCE_BYTES_AND_RECORDED_CLAIM_VERIFIED with earlier Hesse/Hilbert90 completed frontier, protected contributions and staging. Current R18 recovery #6571 shows no current own winning CLAIM/open run/unpublished upload, execution_authorized=false. Previous session-to-predecessor CAS mismatch remains tracked by enterprise-math Issue #1558. This portable theorem shall **not** be inserted as completed native Source units without an actual authorized claim/open and durable checkpoint readback.

**Next smallest science:** apply criterion (3) to the **fixed original z=2** six signed Hasse channels via the bivariate master, retaining the positive-infinity and independent high-high ports. Either prove a real cross-tag WZ cancellation or exhibit an exact source-labeled nonzero residual; do not extrapolate (5) to the larger system. Formal Source scientific priority remains original-class H0/B0 divided-power, [X]U modp², semilinear Frobenius orientation/normalization eta, native kappa, Delta_p-R_p, native experiment and independent review. Frozen source pin and historical completed work unchanged.
