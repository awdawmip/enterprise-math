# D25 — exact tail/moment equivalence and 157-prime source-factor separation (2026-11-04 +08)

Status: TASK_RESEARCH author-side follow-up; EXACT CONDITIONAL REDUCTION / FINITE TESTED FACTOR ALLOCATION / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. Same Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7 and frozen source pin c47e13e4aba0e006366f989d6334d443f6333ae3. Research lane chatgpt-research-hourly-enterprise-math-20260923.

## Proven conditional equivalence

Reuse the just-published exact Clausen identity, without replaying that proof. Let p>3 and

v_i=(1/8)_i(3/8)_i/[i!² 9^i],
F_p=sum_(i=0)^(p-1)v_i,
D_p=sum_(i=0)^(p-1)i v_i.

The exact ordered-high-degree tail identity is

T2304(p)=F_p(F_p+16D_p)-S2304(p-1).

The published Guo–Zudilin theorem proves, for every prime p>3,

S2304(p-1) ≡ chi_p*p (mod p³), chi_p=(-3/p).

Source: Guo and Zudilin, A q-microscope for supercongruences, Advances in Mathematics 346 (2019), 329–358, https://arxiv.org/abs/1803.01830 (abstract states the exact original 2304 factorial kernel and full p−1 truncation).

Consequently, for every prime p>3, the following is an exact two-way equivalence:

T2304(p) ≡ -chi_p*p (mod p²)
IF AND ONLY IF
F_p(F_p+16D_p) ≡ 0 (mod p²).

This is a conversion of the still-open late-root tail-sum candidate into a finite Gauss moment divisibility question. Either of the factors being divisible by p² suffices; the factorization and conditional equivalence are proved independently of the numerical observations below.

## New finite source-factor allocation observation

An independent Python standard-library modular recurrence computed F_p and D_p modulo p² for all **157 primes 5<=p<=2000 with p≡5 or7 (mod8)**. Every tested prime met the stronger division into two classes:

| p (mod24) | tested primes | candidate factor vanishing modulo p² |
| --- | ---: | --- |
| 13 | 40 | F_p≡0 |
| 23 | 37 | F_p≡0 |
| 5 | 39 | F_p+16D_p≡0 |
| 7 | 41 | F_p+16D_p≡0 |

Example p=13: F=0, F+16D=137 (mod169). Example p=29: F=287, F+16D=0 (mod841). Example p=373: F=0, F+16D=110861 (mod139129). Distinct source-factors can carry the whole observed p² divisibility. All 157 exact checks passed; **no universal proof of these four residue-class factor vanishing statements was obtained**.

For the frozen p≡13 (mod24) class, a proof of F_p≡0 modp² would yield the late-root 2304 tail correction using the already-published 2304 theorem. For p≡19 (mod24), the earlier termwise tail theorem directly gives T2304≡0 modp². This creates two different concrete proof routes for the two frozen classes.

## Status and precise continuation

Mathematical progress: a proved exact equivalence and a discriminating, 157-prime tested candidate factor map. The combined 216–2304 p³ comparison, original signed low/middle/high F4-glued certificate, p373 native H0/B0 and independent mathematical review remain to be completed. This evidence is author-only, not an officially claimed run.

BRC carriers: source label 2304, original finite coefficient v_i, derivative index i, factor F or F+16D, residue class p mod24 and modulus p²; observer multiplication F(F+16D) and future tail reconstruction. Do not merge the two factors before selecting proof technique.

**Next exact action:** seek a parameter-paired terminating 2F1, Jacobi or p-adic reflection transformation proving F_p≡0 (modp²) for p≡13,23 (mod24); in parallel analyze the weighted companion F_p+16D_p for p≡5,7 (mod24). Preserve actual p-adic units and original full p−1 truncation. For mother-objective comparison, prioritize p≡13 then 19, test 373, and retain frozen science pin unchanged.

Control status as read on 2026-11-04 +08 via current Sites service: v0.6.11 / UPSTREAM_CODE_REVIEW_REQUIRED / research_authority_granted=false / executor_binding_configured=false / 5 active of 5. Previous native recovery #6637, failed continuation #6638, and support #1558 remain historical exact handles; no new native CLAIM, OPEN, checkpoint or Result.
