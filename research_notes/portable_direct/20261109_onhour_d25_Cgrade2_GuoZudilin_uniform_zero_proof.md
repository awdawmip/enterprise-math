# D25 / original 2304 grade-2: uniform zero DISCHARGED by Guo--Zudilin (2019)

Date: 2026-11-09. Research lane: `chatgpt-research-onhour-enterprise-math-20260923` (never maintenance). Mother Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; immutable publication: `TP2-B6F4FC938FF94941C1B7`; frozen scientific pin: `c47e13e4aba0e006366f989d6334d443f6333ae3`.

Status: **AUTHOR-SIDE SOURCE-DEPENDENT PROOF / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE**. Source theorem is published Guo--Zudilin 2019; this note supplies a new application to the EXACT preceding grade-2 polynomial, not a claim of a new independent proof of their theorem.

## 1. Correct source match

Write `C_n=binom(4n,2n) binom(2n,n)^2 /2304^n`, `S_p(M)=sum_{n=0}^M (8n+1) C_n`. The denominator in V_p is exactly `2^(8n) 3^(2n) =2304^n`. Thus the source's series is the **same original signed 2304 model**, not a substitute or a coordinate proxy.

Victor J. W. Guo and Wadim Zudilin, *A q-microscope for supercongruences*, **Advances in Mathematics 346 (2019), 329--358**, DOI `10.1016/j.aim.2019.02.008`, arXiv `1803.01830`, Theorem 1.1 and its q->1 consequence (Introduction equations (2) and (3)), prove for every prime p>3:

`S_p(p-1) == p*(-3/p) (mod p^3)` **and** `S_p((p-1)/2) == p*(-3/p) (mod p^3)`.

Direct online source (equations (2),(3), Theorem 1.1): https://arxiv.org/abs/1803.01830

## 2. Exact all-prime theorem (derived)

**Theorem.** For EVERY prime `p>3`, with `n0=(p+1)/2` and `n1=floor((3p-1)/4)`, the original signed coefficient-grade-2 block

`V_{2,p} = sum_{n=n0}^{n1} (8n+1) C_n`

satisfies **`V_{2,p} == 0 (mod p^3)`**. Consequently, the polynomial `P_N(x)` defined in the previous note `20261109_onhour_d25_Cgrade2_polynomial_carry_scan.md` has **`P_N(1)=0` in F_p** for `N=floor((p-3)/4)`, uniformly for every prime p>3.

**Proof.** Since `n<p` and `p>=5`, Legendre's factorial formula gives `v_p(C_n)=floor(4n/p)`; `p` does not divide 2304. The exact difference of the two original signed truncations is

`S_p(p-1)-S_p((p-1)/2) = V_{2,p}+V_{3,p}`,

where `V_{3,p}=sum_{n=n1+1}^{p-1}(8n+1)C_n`. Every summand of `V_{3,p}` has p-adic valuation >=3. The two published supercongruences have exactly equal right-hand sides modulo p^3, hence their difference vanishes mod p^3. Subtract `V_{3,p}` to obtain `V_{2,p}=0 (mod p^3)`.

The preceding source-preserving algebraic reduction, proved in the prior note from the ORIGINAL rational coefficient recurrence, gives

`V_{2,p}/p^2 == K_p P_N(1) (mod p)` with `K_p=C_{n0}/p^2 (mod p)`.

By `v_p(C_{n0})=2`, `K_p` is a nonzero unit in F_p, so `P_N(1)=0`. For p=5, N=0 and P_0=5=0 in F_5, consistent with the general argument. QED.

**Strength and dependency:** the finite-field polynomial reduction is the previously author-proved lemma; this all-prime zero is now **proved conditional on the exact published 2019 theorem** (a properly cited external theorem, not an invented axiom). Its older classification as a 1,227-prime conjecture should be updated to a proven corollary of the two published truncation congruences. The 1,227 checks remain regression evidence, not the proof.

## 3. Fourth digit: retained genuine grade boundaries

Define in F_p

`Q2 = V_{2,p}/p^3 mod p`,
`Q3 = V_{3,p}/p^3 mod p`,
`D = (S_p(p-1)-S_p((p-1)/2))/p^3 mod p`.

All divisions are integral in Z_(p), by the proven theorem, hence the **exact fourth-digit identity** `D=Q2+Q3 (mod p)`. The published theorem annihilates only the THIRD p-adic digit of grade 2, not its fourth digit.

Using two independent implementations, (a) integer binomial coefficients with 2304 modular inverses and (b) the original unit-denominator recurrence
`C_(n+1)/C_n = (4n+1)(4n+3)(2n+1)/(288(n+1)^3)`,
the following p^4 data agree:

| prime p | n0..n1 | Q2 | Q3 | D=Q2+Q3 mod p |
|---:|---:|---:|---:|---:|
| 13 | 7..9 | 3 | 6 | 9 |
| 19 | 10..14 | 6 | 16 | 3 |
| 373 | 187..279 | 234 | 119 | 353 |

In particular, `Q2 != 0` for p=13,19,373: any proposed p^4 argument must retain this exact 2304 fourth-digit contribution. Additional independent checks: p=5,7,11,17,37,43,73 (10 primes in total). These samples prove only the listed finite integer congruences.

Reproduction script: `research_notes/portable_direct/d25_C_grade2_GZ_modp3_to_modp4_20261109.py`. Arithmetic: exact integers modulo p^4, no floating point.

## 4. How this advances the frozen mother objective

The signed AF4 fourth-digit carrier remains
`ell_p + b_p + p t_p == 0 (mod p^2)`, where `b_p=(W2-2V2)/p^2`. The just-proved `V2/p^2=0 (mod p)` gives **`b_0=W2/p^2 (mod p)`** for every p>3, with NO need to separately conjecture the 2304 third-digit vanishing. For fourth digits `b_1` must retain `-2 Q2` plus any actual p-adic digit carry in the normalized residues; derive from exact `b_p`, not from a carry-free simplification.

Next: use the proved b0 reduction and the existing low/high carry relation to attack the original 216 signed finite WZ/Fricke interface; retain `Q2` as a fourth-digit observed quantity. The strongest unrepaired parent dependency remains original-class p=373 native H0/B0 divided-power `[X]U mod 139129`, module rank, actual semilinear Frobenius and eta, signed kappa, Delta-R and independent verification. Existing capability support issue: https://github.com/awdawmip/enterprise-math/issues/1559 (OPEN as read on 2026-11-09; no verified assigned executor). No native operator experiment was run here.

## 5. Source and authorization

Canonical Source continuation read `onhour11-20261109-1508-current-task-continuation`, status SUCCEEDED, Source `add65897dfdf2c040a73249b5a34c100217f81de`, observed 2026-11-09T07:12:08Z. Route `REGISTER_NEW_SESSION_AND_CLAIM_CURRENT_PUBLICATION`; NO_LIVE_CLAIM, `execution_authorized=false`; own `recovery_status` returned `SITE_CONTROL_OWN_ISSUED_SESSION_REQUIRED`. Historical other-conversation session/claim is NOT acquired. Author-side document is NOT a Source checkpoint, Result, acceptance, or native benchmark. Preserve the frozen scientific pin and both Research/Maintenance identities separately.
