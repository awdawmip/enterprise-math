# D25/LIFT — exact p=6m+5 rank theorem, signed third-digit falsifier and finite-class certificate

**2026-10-25 · TASK_RESEARCH · AUTHOR_SIDE_EXACT_PROOF / FINITE_CHECKS_PASSED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT.** This is a portable author contribution, **not** a Source-native checkpoint, CLAIM, run, Result, independently reviewed theorem, or native benchmark. Original frozen task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`, unchanged scientific source pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Research identity requested for this lane `chatgpt-research-onhour-enterprise-math-20260923`; maintenance `chatgpt-hourly-enterprise-math-20260921` is separate.

## Whole-prime exact valuation theorem (new p=5 mod6 case)

For any prime p>=5 and every original rank 0<=n<p, set
\[
a_n=(6n+1)\frac{(1/2)_n(1/3)_n(2/3)_n}{2^n(n!)^3}.
\]
Elementary factorial algebra gives the **exact rational identity**
\[
\boxed{a_n=(6n+1)\binom{2n}{n}^{2}\binom{3n}{n}216^{-n}
=(6n+1)\frac{(2n)!(3n)!}{216^n(n!)^5}.}
\]
Since p>3, n<p, the denominator is a p-unit and 3n<3p<p². Thus Legendre's factorial formula gives the **exact valuation including the weight**
\[
\boxed{v_p(a_n)=\left\lfloor\frac{2n}{p}\right\rfloor+
\left\lfloor\frac{3n}{p}\right\rfloor+v_p(6n+1).}
\]

In particular, for any p=6m+5, m>=0, the unweighted valuation is 0 for n<=2m+1; 1 for 2m+2<=n<=3m+2; 2 for 3m+3<=n<=4m+3; and >=3 for n>=4m+4. The sole weighted rank divisible by p is n=(5p-1)/6=5m+4, with 6n+1=5p (valuation 2 rather than 1 when p=5). This already lies above n=4m+3, so **without assuming any cancellation**:
\[
\boxed{W_p:=\sum_{n=0}^{p-1}a_n\equiv\sum_{n=0}^{4m+3}a_n\pmod{p^3}\quad (p=6m+5).}
\]
For p=6m+1 the same valuation identity specializes to the *already-proved* previous four-band result, including the weighted n=m crossing; we do not count it as newly discovered.

## Exact falsifier, conditional class prediction

The blanket extension W_p≡p (modp³) for *every* p>3 is false. The original five weighted ranks modulo 125 at p=5 are exactly (1,49,45,25,0), giving
\[
\boxed{W_5\equiv120\equiv-5\not\equiv5\pmod{125}.}
\]
This is a rigorous counterexample to an **over-generalized auxiliary claim** only; p=5 is not a target-class D25 counterexample.

**CONJECTURE, NOT PROVED:** $W_p\stackrel{?}{\equiv}p\left(\frac{-3}{p}\right)\pmod{p^3}$ for all p>3. Quadratic reciprocity makes the symbol +1 for p=1 mod3 and -1 for p=2 mod3. The frozen D25 primes p=13,19 mod24 are only a subclass of the positive branch, so this conjecture does not change the frozen original benchmark or expand its official quantifiers.

## Reproducible, exact original-sum verification

Two independently coded observers of **the unchanged original cutoff and coefficients** were executed, with integer modular arithmetic only:

1. Pochhammer rank recurrence (u_0=1, u_n=u_{n-1}(2n-1)(3n-2)(3n-1)/(36n^3)), sum ((6n+1)u_n) modulo p³. All denominators are units because 1<=n<p, p>3.
2. An independent factorial observer updates (n)!, (2n)!, (3n)! and 216^{-n} modulo p³, and computes each summand by the exact integer-factor identity above. Factorials (2n)!, (3n)! keep their entire p-adic factors; only (n)! is inverted.

Deterministic sieve **all 667 primes 5<=p<=5000**, **0 exceptions** to the stated signed p³ conjecture; residues class counts by p mod24: {1:76, 5:85, 7:88, 11:84, 13:83, 17:85, 19:83, 23:83}. **All 166 frozen-target primes in this finite domain** have W_p≡p modp³. The factorial observer independently reproduced 247 cases, including **every one of the 166 target primes**, plus large p=19963 and p=19991.

Exact independent samples: W_5=120 mod125; W_19=19 mod19³; W_211=211 mod211³; W_19963=19963 mod19963³; W_19991=7,989,204,839,280=-19991 mod19991³. All finite-computation statements describe tested coverage, not a universal all-prime proof or a formal checker. The local standalone checker is `d25_sign_class_independent_certificate_check_20261025.py`; complete run output and SHA256-preserved proof/continuation files were packaged in the companion author-side deliverable.

## Dependency and observer boundaries; exact next step

Use the already-author-side-proved CM/Hasse inert zero classification in `research_notes/portable_direct/20261025_onhour_d25_cm_hasse_inert_zero_classification.md` at EM main commit `502294bc379ecb2f5e6666c2e60bb6c7334e031e`, together with the signed Clausen joint obstruction of `20261025_onhour_d25_clausen_three_band_local_jet_joint.md` at `9713f10774d8c0a64c64fb2bd9888bec5679f40d`. **Do not repeat** the prior low/mid/high jets, reflected corner, or Legendre zero proof. The remaining **original all-prime target** is still to prove/deny
\[
\mathcal E_p=\frac{12U_0D_0-1}{p}+U_0^2+12U_0D_1+
12D_0(L_2^{low}+L_2^{mid}+V_{4m})-T_p\equiv0\pmod p.
\]
for p=13,19 mod24, conditional on the separately accepted first-digit statement allowing division by p. A direct finite-field formal-adjoint/telescoping certificate retaining the signed cutoff is the next mathematical unit. The stronger signed-character conjecture is only an additional *pressure test*, not a substitute.

The frozen original native CM/Hasse same-class `[X]U` modulo p², primitive-class comparison/semilinearity and exact leading normalization, Frobenius direction, κ and native benchmark remain **unexecuted/unverified**. A scalar finite p³ test is NOT that experiment. The BRC/residual observer retains full rank provenance, prime valuations, signed mod p³ residues and separate scalar/Hasse/native ports. Positive BRC mass is inapplicable to signed residue cancellation; the classical finite-field auxiliary model makes no claim about native X6 spatial dynamics.

## Control provenance (no role-bound mutation)

Fresh global GitHub main `63cd2246686734c910e23f92f8ebe5f7706559b5`, current EM control snapshot `502294bc379ecb2f5e6666c2e60bb6c7334e031e` at entry; later GitHub author/activity commits do not drift frozen science pin. P000 locked canonical blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc` verified. Gateway status 0.6.11 and Site `static_machine_readonly`, no Researcher write authority; one bounded canonical inventory read returned `CONTROL_QUOTA`.

Historical original continuation `awdawmip/kimi-query-bridge#6198`, target request `rsch20-successor-continuation-d25-20261023-a50`, has a verified **SUCCEEDED READ-ONLY** receipt, not a claim. Its literal conversation ID is `chatgpt-research-hourly-enterprise-math-20260923`, different from this task's explicit `chatgpt-research-onhour-enterprise-math-20260923`; it is historical evidence only, never inherited as this lane's Researcher session/ownership. No duplicate request, Source-native checkpoint, freeze, review, HANDOFF or release was issued. Existing support owner path `enterprise-math#1558` remains. Task D25/JT2 **OPEN**, original on-the-hour scheduling/notifications untouched.
