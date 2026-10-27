# D25: signed original-E3 period norm / unweighted-216 cross-port diagnostic

**Date:** 2026-10-27. **Logical Research lane:** `chatgpt-research-onhour-enterprise-math-20260923` (TASK_RESEARCH), distinct from maintenance `chatgpt-hourly-enterprise-math-20260921` and other Research conversations. **Mother task:** `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; mother objective `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`. **Immutable SCIENTIFIC Source pin:** `c47e13e4aba0e006366f989d6334d443f6333ae3` (unchanged). Initial research input and accepted UR/JT0 are not replaced.

**Evidence type:** ORIGINAL-CLASS EXACT FINITE COMPUTATION / SIGNED PROPOSED CONGRUENCE / NEW NEGATIVE CONTROL; **UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / NOT_SOURCE_NATIVE_CHECKPOINT / NATIVE_H0B0_NOT_EXECUTED / NOT_UNIFORM_PROOF / NOT_LIFT_COMPLETION**. Only the declared finite prime set is exhaustively certified by the executed checker. No previously accepted D24 result or another lane's contribution is recredited.

## 1. Actual science: original d=3 form coefficient versus original unweighted hypergeometric branch

Let `p>3` be prime, `p mod 24 in {13,17,19,23}`, `M=p^3`, `R_M=(Z/MZ)[T]/(T^2-2)`, `t=(2-T)/4`, and `c=t/27=(2-T)/108`.

Use the **original E3 formal invariant-differential coefficient** (Chisholm–Deines–Long–Nebe–Swisher, Lemma 12; also independently derived in the prior original-model ODE and binomial certificate):
\[
H_p(T):=a(p-1;t)=
\sum_{j=0}^{\lfloor(p-1)/3\rfloor}
\binom{2j}{j}\binom{p-1-j}{2j}c^j\ \in R_M.
\]
The involution \(\iota(T)=-T\) is retained. Its **quadratic-algebra norm** is
\[
N_p=H_p(T)\,\iota(H_p(T))=H_{p,0}^2-2H_{p,1}^2\bmod p^3.
\]
This is a finite-field norm only when \(T^2-2\) is irreducible modulo \(p\); in the split branches \(p\equiv17,23\pmod{24}\) it is the corresponding *quadratic étale algebra* norm, **not** an extension-field norm. Preserve these distinct provenance ports.

Define the original *unweighted* finite hypergeometric sum (not the original LIFT weighted sum):
\[
U_p:=\sum_{n=0}^{p-1}
\frac{\binom{2n}{n}^{2}\binom{3n}{n}}{216^n}\pmod{p^3}.
\]
The exact factorial identity
\[
\frac{(1/2)_n(1/3)_n(2/3)_n}{2^n(n!)^3}
=\frac{\binom{2n}{n}^{2}\binom{3n}{n}}{216^n}
\]
follows by writing \((1/2)_n=(2n)!/(4^nn!)\) and \((1/3)_n(2/3)_n=(3n)!/(27^nn!)\). All displayed denominators are p-units in the declared range.

**Finite verified signed observation, not yet a theorem for all primes:**
\[
\boxed{U_p\equiv-\Big(\frac2p\Big)N_p\pmod{p^3}.}\tag{O}
\]
Here \((2/p)\) is the usual Legendre symbol: in the *target* p≡13,19 branches it equals −1, so (O) has **positive** sign; p≡17,23 gives the **negative** sign. The observed valuation \(p\mid H_p(T)\), \(p^2\mid U_p,N_p\) is independently checked for every tested prime.

## 2. Executed exact finite certificate (stronger branch discrimination than the existing weighted scan)

The reproducible STD-LIB Python verifier is [the exact source code](d25_original_E3_signed_norm_216_finite_check_20261027.py), Git blob `0c61d0df3b8bfdf18e4cfc5402c96349d4dde653`. The author actually executed the same recurrence algorithm locally; a second independent `math.comb` coefficient path checks 10 specified primes. It does **not** execute or imitate native H0/B0.

Exhaustive declared finite domain: **all 186 primes \(p<2500\)** in these four residue classes; class counts 13→48, 17→46, 19→46, 23→46. All 186 satisfy (O) exactly modulo \(p^3\), with p-integrality asserts checked; for the 94 target-class primes the existing weighted \(W_p\equiv p\pmod{p^3}\) is also rechecked only as a consistency test (not counted as a new proof or new 815-prime scan).

Full deterministic per-prime row ledger (lines `p,U_mod_p3,NormH_mod_p3,W_mod_p3,H0_mod_p3,H1_mod_p3,sign`, ascending p) has SHA256
`2e4a31655302eeba1560c8cd21300d5ae5c3c621ebe072b96f1e18c52f9b0687`.

| p | class | \(U_p/p^2\bmod p\) | \(N_p/p^2\bmod p\) | signed result |
|---:|---:|---:|---:|---|
| 13 | 13 | 11 | 11 | + |
| **17** | **17** | **3** | **14 = -3** | **−** |
| 19 | 19 | 8 | 8 | + |
| 23 | 23 | 6 | 17 = −6 | − |
| 37 | 13 | 34 | 34 | + |
| 41 | 17 | 29 | 12 = −29 | − |
| 43 | 19 | 24 | 24 | + |
| 47 | 23 | 13 | 34 = −13 | − |
| 211 | 19 | 53 | 53 | + |
| **373** | **13** | **71** | **71** | **+** |

**Exact negative control:** The unqualified unsigned proposal \(U_p=N_p\bmod p^3\) is **false already for p=17**, since \(U_{17}=3\cdot17^2=867\) while \(N_{17}=14\cdot17^2=4046\) modulo \(17^3=4913\). The signed version (O) passes there; this is *not* a counterexample to LIFT, whose target primes are 13 and 19 classes only.

At p=373, the previously verified actual **original** differential coefficient is
\(H_{373}=46042747+33130606T\mod 373^3\),
so \(H_{373}/373=349+48T\bmod373\), \(N(H_{373}/373)=71\bmod373\), and independently \(U_{373}=9,878,159=71\cdot373^2\pmod{373^3}\). Thus the p373 match is between the original **d=3 differential coefficient** and the actual unweighted 3F2 sum, **not** between an ordinary Hesse surrogate and a claimed native [X]U.

Arithmetic and reproducibility: \(A_0=1\), \(A_{n+1}/A_n=(2n+1)(3n+1)(3n+2)/(36(n+1)^3)\); for \(f_j=\binom{2j}{j}\binom{p-1-j}{2j}\), \(f_0=1\) and \(f_{j+1}/f_j=(p-1-3j)(p-2-3j)(p-3-3j)/((p-1-j)(j+1)^2)\). Both are exact ratios with invertible denominators at every used transition. Quadratic ring multiplication retains both integer-coordinate residues; no floating point, WZ unproved identity, quadratic-character averaging or renamed axiom is used.

## 3. External prior-art interface, not theorem promotion

Zhi-Hong Sun, *Supercongruences involving Apéry-like numbers and binomial coefficients*, AIMS Mathematics **7(2)** (published Nov 18 2021), DOI `10.3934/math.2022153`, **Conjecture 5.28** (printed p.2758, PDF page 30), explicitly concerns this same *unweighted* \(U_p\) and proposes a \(p^2\)-coefficient using \(R_{24}(p)\). It treats all four inert classes with different signs. **Its status in that source is CONJECTURE**, not a published proof of (O) or LIFT. PDF: https://www.aimspress.com/aimspress-data/math/2022/2/PDF/math-07-02-153.pdf . The original E3 coefficient itself comes from the 2013 Chisholm et al. source and from the earlier exact original-model checker, not from Sun's proposed \(R_{24}\) formula.

Under the unproved Conjecture 5.28, (O) would supply a testable original E3-norm formula; without a uniform proof of (O), **neither statement may be exported as an unconditional all-prime theorem**. A bounded title/content search of recent author notes found no previous same signed-cross-port certificate; global novelty is NOT asserted.

## 4. BRC audit, conditional relevance, and genuine unfilled native gap

**BRC: COMPOSE_APPLIED.** Population: four separately labeled inert-CM congruence classes; carrier: \(U_p\), ordered original \(H_p(T),H_p(-T)\), exact ring involution, signs, valuations and the still separate signed weighted observer \(W_p=\sum(6n+1)A_n\). Later observer: original LIFT \(\Delta_p-R_p=(W_p-p)/p^2\bmod p\). The quotient \(H\mapsto N(H)\) loses the individual branch/gauge information, so it is permitted **only** for the declared unweighted norm comparison, not as a native Frobenius or \([X]U\) replacement. The sign switch at p17 is a concrete witness that dropping the residue branch is unsafe. This quadratic ring is an **external algebraic computation**; no bridge to the complete native six-axis X6 coordinates, dynamics, or spatial claim is made.

For the live target classes p≡13,19, (O) suggests a prospective **signed original-class scalar input**: verify \(U_p\) against the actual \(H_p(T)\iota H_p(T)\). Since the original LIFT is \(W_p=U_p+6\sum nA_n\equiv p\bmod p^3\), the additional weighted/derivative digit remains live, even **assuming** (O). Do not misstate an unweighted norm as solving the weighted supercongruence.

**Unchanged benchmark:** #1559 is `PENDING_OWNER / NATIVE_H0B0_NOT_EXECUTED`. Still missing the fixed genuine H0/B0 divided-power representative, native module rank and basis, true \([X]U\bmod 373^2\), Frobenius direction/twist/two-digit normalization, signed odd Green/Hesse, and same-definition \(\kappa,\Delta-R\). The present \(U_p\) and \(H_p\) are *not* any of these measurements. An authorized owner must still obtain the actual fixed original representative and run the exact benchmark with independently reproducible raw receipt. This author-side regression is an optional **post-authentication** comparator only, and does not change #1559 acceptance.

**Source control recovery:** old own recovery receipt is `research-onhour-20261026-1403-recovery-r12` (#6556) with `source_authority_verified=false`, zero own claim/open/run; prior dispatch `research-onhour-20261026-1355-dispatch-r11` (#6529) is `FAILED/TimeoutExpired`, not `NO_DISPATCH`; read-only exact continuation `onhour-20261027-0300-d25-exact-cont-read-01` returned `CONTROL_QUOTA` (not a successful packet). No fresh claim/prepare/open/dispatch, maintenance identity, Source checkpoint/Result/review or role registration is asserted. Three old neutral staging files remain separate. No scheduler or notification mutations.

**Next exact science action:** an independently licensed native implementer locates the Source-typed H0/B0 representative and executes the missing p373 [X]U / Frobenius / signed-κ observation; if the Source permits a portable mathematical follow-up, proving or finding a counterexample to the precisely stated **signed all-prime bridge (O)** would connect original d3 coefficient and unweighted 3F2 without altering or replacing the mandatory native experiment. Do not repeat the already finished weighted 815-prime scan, prior E3 isogeny, UR/JT0 or earlier ordinary-Hesse norm gates. Until Source accepts a real claim, this remains a **separate unpublished-to-control / UNREVIEWED author artifact**, not the canonical task frontier.
