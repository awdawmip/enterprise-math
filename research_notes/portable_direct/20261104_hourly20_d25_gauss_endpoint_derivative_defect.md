# D25 — Universal p³ endpoint defect for truncated Gauss derivative transport

Date: 2026-11-04 (+08). **Evidence:** author-derived exact algebra + 157-prime exact integer check; UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. No native CLAIM, OPEN, Source checkpoint or formal Result.

Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`, frozen science pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Logical Research lane: `chatgpt-research-hourly-enterprise-math-20260923` (distinct from the maintenance and onhour lanes). Previous author proof: `research_notes/portable_direct/20261104_hourly20_d25_gauss_parameter_jet_jacobi.md`. This note extends that first-root/parameter-jet work, preserving its finite-truncation provenance.

## Original objects

Let `alpha=1/8`, `beta=3/8`, `c_k=(alpha)_k(beta)_k/(k!)²`, and
\[
F_p(z)=\sum_{k=0}^{p-1}c_kz^k,\qquad G_p(z)=F_p(z)+16zF'_p(z).
\]
At `z0=1/9`, these are exactly the original 2304 Gauss factors `V`, `V+16V_1` in the prior Clausen-tail result; the derivative `G'_p(z0)` is an additional, explicitly typed observer.

## Theorem 1: exact truncated ODE boundary (proved over Q)

For every positive integer `n`, put `F_n=Σ_{k=0}^{n-1}c_kz^k` and `G_n=F_n+16zF'_n`. With
\[
\mathcal H=z(1-z)\frac{d^2}{dz^2}+(1-\tfrac32z)\frac d{dz}-\tfrac3{64},
\]
one has
\[
\boxed{\mathcal HF_n(z)=-n^2c_nz^{n-1}.}\tag{1}
\]
Consequently,
\[
\boxed{G'_n(1/9)-\tfrac98G_n(1/9)+\tfrac9{32}F_n(1/9)
=-18n^2c_n9^{1-n}.}\tag{2}
\]
**Proof.** The hypergeometric recurrence
`(k+1)²c_(k+1)=(k+1/8)(k+3/8)c_k` cancels every coefficient of `H F_n` below degree `n-1`. The remaining coefficient is `-(n-1+1/8)(n-1+3/8)c_(n-1)=-n²c_n`. Then `G'_n=17F'_n+16zF''_n`; substitute (1) and `z=1/9` to obtain `G'_n=2F'_n+27F_n/32-18n²c_n9^{1-n}`, and eliminate `F'_n=(9/16)(G_n-F_n)`. QED.

## Theorem 2: universal third-digit defect and sharp valuation (proved)

Fix a prime `p>=5` with `p mod8∈{5,7}`. Let `a,b∈[0,p-1]` be the first-root indices `8a+1=mp`, `8b+3=np`. For `p mod8=5`, `(m,n)=(5,7)`; for `p mod8=7`, `(m,n)=(7,5)`. Thus `mn=35`.

In the product
\[
c_p=\frac{\prod_{j=0}^{p-1}(8j+1)(8j+3)}{8^{2p}(p!)^2},
\]
each numerator factor family contains exactly one `p`-multiple. Removing those factors gives `A/p≡-m`, `B/p≡-n` via Wilson's theorem, while `8^(2p)((p-1)!)²≡64`. Thus
\[
\boxed{c_p\equiv35/64\pmod p.}\tag{3}
\]
Equation (2), Fermat's theorem and (3) yield
\[
\boxed{G'_p(1/9)-\tfrac98G_p(1/9)+\tfrac9{32}F_p(1/9)
\equiv-\tfrac{315}{32}p^2\pmod{p^3}.}\tag{4}
\]
For every such prime `p>=11`, the defect has **exact p-adic valuation 2**, since no prime `p>=11` divides `315`. At `p=5,7` it vanishes modulo `p³`. Its first two digits satisfy the universal finite-truncation transport identity
\[
\boxed{G'_p(1/9)\equiv\tfrac98G_p(1/9)-\tfrac9{32}F_p(1/9)\pmod{p^2}.}\tag{5}
\]
The `k=p` omitted coefficient is the exact third-digit endpoint source; (5) cannot be lifted homogeneously to `p³` for the `p>=11` class without that source.

## Theorem 3: first-digit branch transversality (proved)

Modulo `p`, `F_p(z)` becomes
\[
P(z)=\sum_{k=0}^{L}\binom ak\binom bk z^k\in\mathbf F_p[z],\quad L=\min(a,b)<p.
\]
The corresponding weighted polynomial is `Q(z)=P(z)+16zP'(z)`. It is the same Jacobi base polynomial in the prior author-side parameter-jet reduction. Equation (1) gives `H P=0 modp`. At `z0=1/9`, `z0(1-z0)` is nonzero, so a repeated root of `P` with multiplicity `2<=s<=L<p` would give an impossible leading coefficient `z0(1-z0)s(s-1)` in its differential equation. Every root of `P` at `z0` is simple.

If `P(z0)=Q(z0)=0`, then `P'(z0)=0`, contradiction. Thus the two base observers cannot vanish simultaneously at `z0`. If `Q(z0)=0`, equation (5) implies
\[
\boxed{Q'(z0)=-9P(z0)/32\neq0\pmod p.}\tag{6}
\]
Thus both possible observer zeros are simple and mutually exclusive at `z0`; which residue classes select them is a **separate open arithmetic problem**.

Conditional p² slope locks follow immediately from (5): if `F_p(z0)≡0 (modp²)`, then `G'_p(z0)≡9G_p(z0)/8 (modp²)` and `G_p(z0)` is a mod-p unit; if `G_p(z0)≡0 (modp²)`, then `G'_p(z0)≡-9F_p(z0)/32 (modp²)` and `F_p(z0)` is a mod-p unit. No unproved residue-class vanishing has been upgraded to a theorem.

## Integer evidence and BRC use

The accompanying independent standard-library checker reconstructs every original `k=0,...,p-1` term using the exact recurrence `t_(k+1)=t_k(8k+1)(8k+3)/(576(k+1)²)`, then computes `F,G,G'` modulo `p³`. It passed **all 157 primes `5<=p<=2000`, `p mod8∈{5,7}`** for (4), its exact valuation classification, the base transversality check, and conditional p² slope locks in the 157-prime observed factor split. Samples `p=13,23,29,373` have normalized defect `6,11,11,165 (modp)`. This finite test is not a universal proof of the factor allocation.

**BRC carrier:** original Gauss source and index `k<=p`, first-root indices/slopes, valuation strata, finite truncation boundary, finite parameters, and derivative observer. **Allowed operations:** derivatives, p-adic lifts, original-216/2304 comparison, signed Clausen-tail compositions. The projection `(F,G,G') -> (F,G)` is certified mod p² by (5); at p³ it requires the explicit endpoint residue (4). Do not erase source or promote this finite-observer statement to a universal state reduction.

**Unfinished science:** establish the residue-class Jacobi root and first-parameter-jet cancellation uniformly; construct a source-labelled inhomogeneous parameter-jet/contiguous certificate retaining (4) and test `p=13,23,373`; combine with original 216–2304 mod-p³ signed Green/WZ ports `2r,3r,4r`. Frozen D25 mother target `W216(p-1)≡p (modp³)` at `p mod24∈{13,19}` remains open.

**Control provenance:** as read 2026-11-04 +08, gateway 0.6.11 reports `UPSTREAM_CODE_REVIEW_REQUIRED`, `research_authority_granted=false`, `executor_binding_configured=false`, active quota `5/5`. Support issue `enterprise-math#1558` remains open; distinct native benchmark `#1559` remains open. No live CLAIM/OPEN or native checkpoint is asserted in this author-side publication; no historical service session/staging was modified.
