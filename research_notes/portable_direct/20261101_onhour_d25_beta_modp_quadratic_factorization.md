# D25 SECOND-DIGIT-LIFT — exact finite-field quadratic factorization and original-beta CM selector

2026-11-01 Asia/Hong_Kong. **AUTHOR-SIDE COEFFICIENTWISE PROOF / EXACT FINITE REGRESSION EXECUTED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING / NATIVE_NOT_RUN.** Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`. Frozen science pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Research lane `chatgpt-research-onhour-enterprise-math-20260923`; maintenance ID never used.

## Original objects and new **all-prime polynomial identity**

Let p>3 be a prime p≡5(mod8), n=(p−1)/4 (necessarily odd), a=(5p−1)/8, b=(7p−3)/8. In the finite field F_p define the original truncated Gauss and its quadratic transform:

\[
 F_{\beta,p}(z)=\sum_{k=0}^{p-1}\frac{(1/8)_k(3/8)_k}{(k!)^2}z^k,
 \qquad U_p(t)=\sum_{k=0}^{p-1}\frac{(1/4)_k(3/4)_k}{(k!)^2}t^k .
\]

The coefficients are p-local before reduction. **Theorem:** the following is an identity *of whole polynomials*, not merely an identity at CM points:

\[
 \boxed{F_{\beta,p}(4t(1-t))\equiv (1-2t^p)U_p(t)\pmod p}
 \quad\text{in }\mathbf F_p[t]. \tag{QF}
\]

Furthermore `U_p(t)=P_n(1−2t)` mod p. The factor `1−2t^p` is **not** a scalar constant and records the Frobenius high-degree cutoff branch.

## Elementary proof using the original high-degree cutoff (no assumption of beta CM selector)

1. Modulo p, the Gauss parameters 1/8 and 3/8 become −a and −b, and the 1/4,3/4 parameters become −n and n+1. Consequently `deg F_beta,p = a`, `deg U_p=n`. Let `G(t)=F_beta,p(4t(1−t))`: then `deg G≤2a=p+n`.

2. Use the exact formal quadratic hypergeometric identity already derived from differential operators in predecessor `20261101_onhour_d25_legendre_p2_reflection_quadratic_cutoff_antitrace.md`:
\[
{}_2F_1(1/8,3/8;1;4t(1-t))={}_2F_1(1/4,3/4;1;t).
\]
All coefficients of degree <p use only terms with k<p and have p-unit factorial denominators. Hence `G(t)−U_p(t)` has no coefficients below degree p, i.e. `G(t)=U_p(t)+t^p H(t)` for a unique `H\in F_p[t]`, `deg H≤n`.

3. The original Gauss pullback is symmetric: `G(1−t)=G(t)`. Since n odd, the finite Legendre polynomial is antisymmetric: `U_p(1−t)=−U_p(t)`. As `(1−t)^p=1−t^p` in F_p,
\[
U_p(t)+t^pH(t)=-U_p(t)+(1-t^p)H(1-t).
\]
The coefficients of degree <p therefore force `H(1−t)=2U_p(t)`. Reflecting gives `H(t)=2U_p(1−t)=−2U_p(t)`. Substitution gives (QF). **QED.**

## New corollary: independently close the original beta mod-p selector

Work over `F_(p²)=F_p[s]/(s²−2)` (because `(2/p)=−1`), and set `t_−=1/2−s/3`. Then `t_−^p=1/2+s/3`, `4t_−(1−t_−)=1/9`. Evaluating (QF) gives the *exact original Gauss arithmetic*:

\[
\boxed{F_{\beta,p}(1/9)\equiv-\frac{2s}{3}P_n(2s/3)\pmod p.}\tag{CMβ}
\]

The prefactor is a unit. Our preceding new all-prime CM(-24) Legendre theorem `20261101_onhour_d25_cm24_legendre_selector_dichotomy.md` proves `P_n(2s/3)=0\iff p\equiv13\pmod{24}` for p≡5mod8 by explicit Hasse polynomial and Deuring split/inert reduction. **Thus the original beta selector is itself now proved**, independently of an opaque imported CM claim:

\[
\boxed{F_{\beta,p}(1/9)=0\pmod p\quad\Longleftrightarrow\quad p\equiv13\pmod{24},
\qquad p>3,\ p\equiv5\pmod8.}
\]

For non-target p≡5(mod24), this Gauss factor is a p-adic unit.

## New exact first-carry interface at mod p²; no unsupported cancellation

Lift all coefficients into the original p-local quadratic ring `R₂=(Z/p²)[s]/(s²−2)`. Retain two **different original provenance ports**:

\[
 E_p(t):=\frac{F_{\beta,p}(4t(1-t))-(1-2t^p)U_p(t)}p
 \quad (\bmod p).
\]

This division is coefficientwise in p-local integral polynomials: (QF) makes its numerator divisible by p. At p≡13(mod24), the newly proved selector gives `U_p(t_−)=pV_p(t_−)` with `V_p=U_p(t_-)/p\in F_(p²)`. Thus

\[
\boxed{
\frac{F_{\beta,p}(1/9)}p\equiv
-\frac{2s}{3}\,V_p(t_-)+E_p(t_-)\pmod p. }\tag{C1}
\]

The quadratic prefactor's p-adic carry is multiplied by `U_p(t_-)\equiv0\mod p`, so its contribution at mod p² vanishes by valuation, not by discarding a source. The two remaining terms in (C1) generally are individually **nonzero**; proving their universal cancellation is precisely the still-open p13 beta second-digit target.

Fixed-prime verified ports in F_p (even scalar observer) are:

| p | Legendre first digit `U_p(t_-)/p` in (1,s) | prefactor×Legendre first digit (even) | `E_p(t_-)` (even) | original `F_beta,p(1/9)/p` |
|---:|---:|---:|---:|---:|
| 13 | (0,3) | 9 | 4 | 0 |
| 37 | (0,27) | 1 | 36 | 0 |
| 61 | (0,41) | 47 | 14 | 0 |
| 109 | (0,42) | 53 | 56 | 0 |
| 373 | (0,115) | 344 | 29 | 0 |

All are exact mod p. The full p² original beta sum is evaluated independently, not read off the identity. At p=29 the non-target full sum is `287 mod841`, and the defect `E_29(t_-)` has coordinates (20,19) mod29; consequently it must not be erased by a blanket cancellation claim.

## Executed arithmetic, original observer and limits

Companion exact source: `research_notes/portable_direct/d25_beta_modp_quadratic_factorization_20261101.py`. Standard-library execution passed **43/43 primes p≤1000, p≡5(mod8)** in the *full degree ≤p+n coefficientwise identity* (QF), with original binomial coefficients and independent Legendre coefficients. Additionally, p=5,13,29,37,53,61,109,373 passed direct original p² Gauss/Legendre recurrence against the two-coordinate first-carry equation; five target p values above independently showed nonzero canceling first digits. The finite calculation corroborates but does not confer independent review or Source admission.

BRC composition is source-faithful: original beta finite coefficient integers → quadratic transformation cutoffs → independent elliptic CM Hasse observer → original p-integral Gauss scalar, with Frobenius and ±s branches preserved. This auxiliary quadratic coordinate does not become the native X6 three-dimensional slice, divided-power H0/B0, eta or signed odd Green/Hesse. Frozen P000 and ACTIVE worldview unchanged.

## Recovery and next scientific obligation

This consumes, but never recredits, the existing exact quadratic-cutoff theorem and the just-proved CM(-24) Legendre selector. Both mod-p assumptions of the predecessor's **conditional** Frobenius-carry elimination are now proved for all p=13(mod24). The minimal missing science remains (C1)'s universal two-source cancellation, equivalent to `F_beta,p(1/9)=0 modp²` for p13; the original weighted216 goal `A_p=p modp³` for p=13,19(mod24) additionally needs its frozen `Delta_p−R_p` port.

Native same-original-class p373 H0/B0 divided-power benchmark remains GitHub issue #1559 OPEN/unassigned at 2026-11-01: [X]U mod139129, module rank, actual semilinear Frobenius and eta, signed odd Green/Hesse, kappa and independent replication. **NATIVE_NOT_RUN/PENDING_OWNER**; this external polynomial calculation does not fulfill the native benchmark.

Source Gateway 0.6.11 at 2026-11-01: Site client `research_authority_granted=false`, `executor_binding_configured=false`; own checkpoint read `ACCESS_DENIED`; prior target request `research-onhour-20261031-0205-dispatch-r15` `CONTROL_REQUEST_NOT_FOUND` in this specific client scope. No native session/claim/run, checkpoint, Result, review or Source acceptance. Retain original request for lawful reconcile; old staging retains distinct origin. Do not dispatch to maintenance or silently rebase frozen source pin; scheduled settings are untouched.
