# D25/W216 — a class-explicit CM binomial prediction for the third signed inverse-moment digit

Date 2026-11-10 Asia/Hong_Kong. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3; Research lane chatgpt-research-onhour-enterprise-math-20260923. **AUTHOR_SIDE / EXACT CONDITIONAL CONSEQUENCE / 13 FINITE WITNESSES / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0_B0**.

## Source and new discriminating prediction

Consume this round's **proved all-prime terminal-Fermat signed bridge**, source file 20261110_onhour_d25_W216_Sun529_Fermat_terminal_lift_bridge.md. Its exact target-class consequence is

~~~text
epsilon_p = q_p(216)-3*alpha_p - (3/2)*lambda_p mod p,
alpha_p=F0/p², epsilon_p=(F2-13F1/2+5p/2)/p²,
lambda_p=(W_p-p)/p², p≡13,19 (mod24),
~~~

under the explicitly stated first-digit/F0 integrality H. (This is merely the rearrangement of the universal proven identity.) In particular, for LIFT lambda_p=0, epsilon_p=q_p(216)-3alpha_p.

Now consume the *published CONJECTURE*, not a theorem, by Zhi-Hong Sun, AIMS Mathematics 7(2) (2022), p.2758, Conjecture 5.28; DOI 10.3934/math.2022153; PDF https://www.aimspress.com/aimspress-data/math/2022/2/PDF/math-07-02-153.pdf . Set

~~~text
R24(p) = binom((p-1)/2, floor(p/24))
        *binom((p-1)/2, floor(5p/24)) mod p.
~~~

This is a p-unit: both lower indices are between 0 and (p-1)/2<p, hence both binomials are nonzero modulo p. Conjecture 5.28 specifies alpha_p as a class-dependent CM binomial reciprocal. COMPOSING THAT CONJECTURE WITH THE PROVED BRIDGE AND THE LIFT HYPOTHESIS yields the following precisely **conditional**, separately falsifiable third-digit predictions:

~~~text
p ≡ 13 (mod24):  epsilon_p ≡ q_p(216)+21/(5*R24(p))   (mod p),
p ≡ 19 (mod24):  epsilon_p ≡ q_p(216)− 3/(11*R24(p))  (mod p).
~~~

Both formulas are direct algebraic consequences, NOT an all-prime proof of Sun's conjecture or the original LIFT. Their research value is an **explicit arithmetic target** for the first unproved divided p-adic digit of the original signed Sun-5.29 defect, requiring only a Fermat quotient and two ordinary binomial coefficients. The frozen original Δ_p−R_p and native odd source ports remain the acceptance object.

## Exact finite regression, original coefficient path

The companion executable d25_w216_sun528_R24_refined_lift_test_20261110.py reuses the preceding source's exact integer-binomial F0, F1, F2 and original W sum, independently constructs R24 via binomials, and verifies both class formulas for all 13 target primes below, without floating-point arithmetic. Observed table (entries modulo p):

| p | class | R24 | F0/p² | epsilon | q_p(216) |
|---:|---:|---:|---:|---:|---:|
| 13 | 13 | 2 | 11 | 0 | 7 |
| 19 | 19 | 8 | 8 | 1 | 6 |
| 37 | 13 | 35 | 34 | 29 | 20 |
| 43 | 19 | 36 | 24 | 9 | 38 |
| 61 | 13 | 47 | 55 | 43 | 25 |
| 67 | 19 | 8 | 16 | 27 | 8 |
| 109 | 13 | 97 | 31 | 84 | 68 |
| 139 | 19 | 103 | 53 | 66 | 86 |
| 157 | 13 | 24 | 119 | 14 | 57 |
| 163 | 19 | 72 | 85 | 141 | 70 |
| 181 | 13 | 70 | 76 | 1 | 48 |
| 229 | 13 | 213 | 106 | 218 | 78 |
| 373 | 13 | 104 | 71 | 183 | 23 |

Each example has original W lift digit λ=0. The test is a finite witness of simultaneous conjectures; only the conditional algebraic implications are theorem claims. No numerical sample establishes independent scientific acceptance.

## Next uncompleted unit and provenance

Highest mother objective: prove/refute original signed Δ_p−R_p=0 mod p in both target classes, with the frozen scalar source interface. A useful future certificate would establish independently either the CM alpha value (Sun-5.28) plus refined epsilon formula, or a direct source-preserving finite WZ/Clausen identity for their combined defect. Retain the exceptional k=p−1 denominator in F1/F2 and the exact q_p(216) terminal correction. Reusing this report must NOT reclassify Conj 5.28 as proved, nor replace the native fixed p373 H0/B0 [X]U mod139129/rank/eta/Frobenius/signed kappa/Δ−R replication tracked by the already-open Issue #1559 (NOT_RUN/PENDING_OWNER). Native session capability is absent this round; no winning CLAIM/open run/Source checkpoint. Researcher and maintenance lanes remain isolated; scheduler unchanged.
