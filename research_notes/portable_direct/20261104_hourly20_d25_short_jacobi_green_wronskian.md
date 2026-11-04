# D25 — Short Jacobi Green–Wronskian source certificate

Date: 2026-11-04. Classification: AUTHOR-DERIVED / EXACT FINITE-FIELD ALGEBRAIC PROOF / FINITE-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.

Parent task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`, frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. This is a portable subunit, separate from original-class native H0/B0 experiments and Source checkpoint.

## Theorem: harmonic-free Green reconstruction of the short Jacobi Wronskian

Let p=8q+5 be prime, q>=1, and work in F_p. Set

\[
J(z)=\sum_{j=0}^q J_jz^j,\quad J_j=\binom qj\binom{3q+1}j9^{-j}.
\]

Let K be the harmonic deformation already defined in the preceding short-Jacobi note; its established inhomogeneous equation reads
\[
L_0K=-\frac z{72}(4\theta-6q-1)J+\frac{J_q}{288}z^{q+1},\quad
L_0=\theta^2-\frac z9(\theta-q)(\theta-3q-1),\quad L_0J=0.
\]

**New source cancellation:** the highest coefficient on the right is
\[
\left(\frac{2q+1}{72}+\frac1{288}\right)J_q
=\frac{8q+5}{288}J_q=0\quad\text{in }\mathbb F_p.
\]
Hence this right side is **exactly** `z H(z)` where
\[
\boxed{H(z)=-\frac1{72}\sum_{j=0}^{q-1}(4j-6q-1)J_j z^j.}\tag{1}
\]
It requires no harmonic inputs or independent terminal coefficient.

Define the Wronskian `W(z)=J(z)K'(z)-K(z)J'(z)` (ordinary derivatives). Then
\[
\boxed{z(1-z/9)W'(z)+(1+4qz/9)W(z)=J(z)H(z).}\tag{2}
\]
Writing W(z)=sum_{t=0}^{2q-1} w_t z^t, `w_{-1}=0`, and `f_t=[z^t]JH`, obtain the **source-only constructive recursion**
\[
\boxed{w_t=(f_t-(4q-t+1)w_{t-1}/9)/(t+1)\pmod p,\qquad0\le t\le2q-1.}\tag{3}
\]
Every denominator is a unit since `2q<p`. The source terms are only original J coefficients and their indexed derivatives. The polynomial W is uniquely determined by (2) with degree <=2q-1; (3) constructs it without knowing K.

More precisely, its highest degree drops by one and has explicit **nonzero** coefficient:
\[
\boxed{w_{2q-1}=0,\qquad w_{2q-2}=\frac{2q+5}{16(q+1)}J_qJ_{q-1}\ne0\pmod p.}\tag{4}
\]
Therefore `deg W=2q-2` for q>=1. For p=5, q=0, J=1, K=H=W=0 and (2) holds.

**Proof.** Starting from the exact prior identity for `L0 K`, cancellation of its terminal coefficient gives (1). Expanding `L0` as
`(1-z/9) z^2 d^2/dz^2 + z(1+4qz/9)d/dz -(q(3q+1)z/9)` shows
`J L0K-K L0J=z^2(1-z/9)W'+z(1+4qz/9)W`. Divide the polynomial equality by z to obtain (2). Coefficient extraction yields (3); all `t+1` are units, proving uniqueness. For the top coefficient, `K_j=J_j h_j` with the established harmonic correction and
`h_q-h_{q-1}=1/8+3/[8(2q+2)]=(2q+5)/[16(q+1)]`. The coefficient at degree `2q-2` in `JK'-KJ'` is `J_{q-1}K_q-J_qK_{q-1}`, which gives (4). The degree `2q-1` coefficient cancels since each product has leading coefficient `q J_qK_q`. Each displayed factor of (4) is a unit for q>=1: `J_q,J_{q-1}` are nonzero binomial products, and `0<2q+5<p`.

## New source-only branch substitutions for the open second digit

Put `W_1=W(1)`. At any prime in the stated domain for which `J(1)=0`, `J'(1)!=0`, the identity gives `K(1)=-W_1/J'(1)` modulo p. At any prime with `J'(1)=0`, `J(1)!=0`, it gives `K'(1)=W_1/J(1)` modulo p. These identities are general conditional statements; the conjectural assignment of residue classes to the zero factor is a separate proof obligation.

Using the earlier Euler-defect notation `F_p`, `E_p`, `N=(p+1)/2`, `u=(8/9)^N` and `e_0=E_p(1)`, `e_1=(theta E_p)(1)`, the formerly harmonic-dependent second-digit criteria now become:
\[
\boxed{u\left(J(1)/p+W_1/J'(1)\right)+e_0=0\pmod p}\tag{5}
\]
under the `p mod24=13` first-digit selector, and
\[
\boxed{u\left(16J'(1)/p-J(1)-16W_1/J(1)\right)+e_0+16e_1=0\pmod p}\tag{6}
\]
under the `p mod24=5` selector. Here J and J' in the divided-by-p terms must be computed modulo p^2, while unscaled factors may be reduced modulo p. Equations (5)/(6) are **proved equivalences** conditional on the stated first-digit zeros, not general proofs of their vanishing.

An independent *linear-coefficient-pass* check of the Euler scalars (without constructing the full defect polynomial) is
\[
e_0=\frac{S-uC(1)}p,\qquad e_1=\frac{D-u[C'(1)-NC(1)/8]}p\pmod p,
\]
where `S=sum_{k<p}v_k`, `D=sum_{k<p}k v_k` are the original Gauss coefficient sums modulo p^2. This is compatible with the earlier proof that the numerator polynomials have p-integral coefficients.

### Exact evidence and BRC observer

The independently executed standard-library checker verifies (2)/(3) via a harmonic-free source recursion; separately builds the harmonic K to check the scalar W and coefficientwise W for 24 representative primes; and checks the original Gauss series/euler ports modulo p^2 for **all 168 primes p<=5000 with p mod8=5**. It executes **95,290** source recurrence positions. All checks passed. This is finite computational evidence in addition to the general algebraic proof above.

Representative source-port values modulo p:

|p|q|J(1)|J'(1)|W(1)|e0|e1|selected second-digit residual|
|--:|--:|--:|--:|--:|--:|--:|--:|
|13|1|0|12|1|9|6|0|
|29|3|7|0|26|5|24|0|
|37|4|0|30|15|12|31|0|
|373|46|0|41|189|119|71|0|

For p=373, `W(1)/J'(1)=41 (mod 373)` and `J(1)/373=326 (mod 373)`; with `u=82`, equation (5) has source-resolved terms `u*(326+41)=254`, `e0=119`, giving `254+119=373=0 (mod 373)`. This is a portable arithmetic certificate, not a native p373 H0/B0 execution. Preserve separately (i) indexed J source, (ii) terminal coefficient cancellation, (iii) Wronskian reconstruction, (iv) Euler defect, and (v) signed 216–2304 Green comparison.

### Continuation

Smallest open mathematical question: prove the residue-class Jacobi selector and source-resolved vanishing of (5)/(6), potentially by finite-field character sums, CM symmetry or a finite telescoping certificate. This author subunit provides a harmonic-free operator to analyze those conditions. Original frozen parent still requires same-prime native divided-power H0/B0, `[X]U mod p^2`, normalized semilinear Frobenius and Delta_p-R_p second digit. The latest verified Source continuation carries `SOURCE_BYTES_AND_RECORDED_CLAIM_VERIFIED` and `REGISTER_NEW_SESSION_AND_CLAIM_CURRENT_PUBLICATION`, execution not authorized. Do not overwrite that Source frontier with author evidence.
