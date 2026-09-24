# D25 LIFT — theorem-level prior-art audit for the exact weighted d=3, lambda=1/2 carrier

Status: SOURCE_JUDGMENT_UNIT / PROVED_CLASSIFICATION_OF_RETRIEVED_SOURCES / LIFT_NOT_CLOSED / NOT_A_RESULT / UNREVIEWED
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT
Publication: TP2-B6F4FC938FF94941C1B7
Date: 2026-09-24

## 1. Exact target and normalization

The current direct target is

W_p = sum_{k=0}^{p-1} (6k+1) (1/2)_k (1/3)_k (2/3)_k /(k!)^3 * 2^{-k}

for p congruent 13 or 19 modulo 24, with the desired second-digit statement

W_p congruent p (mod p^3).

Equivalently, termwise,

(1/2)_k/k! = binom(2k,k)/4^k,
(1/3)_k(2/3)_k/(k!)^2 = binom(3k,k)binom(2k,k)/27^k,

so

W_p = sum_{k=0}^{p-1} (6k+1) binom(2k,k)^2 binom(3k,k)/216^k.

This audit only accepts a theorem whose parameters, weight, truncation, modulus and residue-class/supersingular hypotheses match this exact carrier. Analogous van-Hamme or q-supercongruences are not substitutes.

## 2. The 2013 Chisholm–Deines–Long–Nebe–Swisher theorem stops at p^2

Source: Sarah Chisholm, Alyson Deines, Ling Long, Gabriele Nebe, Holly Swisher, `p-Adic Analogues of Ramanujan Type Formulas for 1/pi`, Mathematics 1 (2013), 9–30, DOI 10.3390/math1010009.

The paper treats Ramanujan-type carriers

  sum (1/2)_k (1/d)_k ((d-1)/d)_k /(k!)^3 * (a k+1) lambda_d^k

at CM singular values. Its introduction explicitly states that the general result proved in that paper is modulo p^2. Thus it supplies the accepted first-digit mechanism but does not by itself imply W_p congruent p modulo p^3.

Resolution for D25: REUSE_APPLIED for the already-consumed first digit; INSUFFICIENT_STRENGTH for the new p^3 target.

## 3. The 2025 Babei–Roy–Swisher–Tobin–Tu paper contains the exact target and still does not prove it modulo p^3

Source: Angelica Babei, Manami Roy, Holly Swisher, Bella Tobin, Fang-Ting Tu, `Supercongruences arising from Ramanujan-Sato Series`, Results in Mathematics 80 (2025), paper 184, DOI 10.1007/s00025-025-02497-0; arXiv:2408.08844.

This is the strongest exact-match source found. In its Section 7 it writes the exact congruence

  [f_{6,(1/2,1/3,2/3)}]_{p-1}(1/2)
    congruent sgn * ((1-lambda)/p) * p (mod p^3),   lambda=1/2,

as equation (7.7). Under the already-consumed D24 supersingular/sign classification for p congruent 13 or 19 modulo 24, this is precisely the present W_p congruent p modulo p^3 target.

Crucially, the paper does **not** present (7.7) as an all-prime theorem. Immediately before (7.6)–(7.8), the authors state that these congruences were numerically verified modulo p^3 for applicable primes p<150. Proposition 7.8 says that Conjecture 7.7 would follow **if** their Theorem 2.1 held modulo p^3. Remark 7.9 further records that the relevant auxiliary congruence only seems to extend to p^3 for ordinary primes, while for supersingular primes the checked strength remains p^2.

Therefore the most current exact-match paper found is positive prior art for the *shape* of the desired statement, but it is not theorem-level closure of the D25 supersingular p^3 LIFT. Treating (7.7) as already proved would overstate the source.

Resolution for D25: EXACT_TARGET_FOUND / CONJECTURAL_OR_CONDITIONAL_AT_P3 / NO_THEOREM_PROMOTION.

## 4. Same arithmetic motive at p^3 exists in the literature, but the closest exact binomial carrier is unweighted and conjectural

Source: Zhi-Hong Sun, `Supercongruences involving Apéry-like numbers and binomial coefficients`, AIMS Mathematics 7 (2022), 2729–2781, DOI 10.3934/math.2022153.

Conjecture 5.28 concerns the unweighted sum

  sum_{k=0}^{p-1} binom(2k,k)^2 binom(3k,k)/216^k

modulo p^3 in the inert classes, including explicit p^2 terms for p congruent 13 and 19 modulo 24. This is the same unweighted coefficient sequence as W_p, so it is useful arithmetic provenance showing that the second digit is nontrivial and residue-class sensitive. But it is both (a) unweighted and (b) explicitly a conjecture, so it cannot replace the weighted D25 theorem.

Resolution: PROVENANCE_ONLY / DO_NOT_SUBSTITUTE_FOR_WEIGHTED_TARGET.

## 5. Nearby proved p^3/q-supercongruences are different carriers

The search also recovered proved p^3/q-supercongruences for nearby Ramanujan/van-Hamme carriers, including pure (1/3)_k^3 families and (1/2)_k^3 families. Their parameters, weights, arguments or truncations differ from

  (1/2)_k (1/3)_k (2/3)_k (6k+1) 2^{-k}.

No parameter transformation with theorem-level preservation of the full p-truncation and modulus p^3 was found that converts those statements into the exact present carrier. They are therefore classified as analogues, not closure evidence.

## 6. Search judgment and falsifiable boundary

Queries were run against the exact Pochhammer form, the exact binomial form with denominator 216^k, the weight 6k+1, and p^3 terminology, together with searches around Chisholm et al. (2013), Babei et al. (2025), van-Hamme/Ramanujan-type supercongruences, q-supercongruences, and recent Beukers-method work.

Result: among the retrieved sources, no proved all-target theorem was found for this exact weighted full truncation modulo p^3 in the supersingular classes p congruent 13 or 19 modulo 24. This is a bounded literature judgment, not a claim that no such theorem can exist anywhere. It should be falsified immediately if a future source supplies the exact parameters, full truncation and p^3 strength.

The particularly strong evidence is Babei et al. (2025): the exact formula itself appears as (7.7), but is explicitly left at numerical/conditional status modulo p^3.

## 7. Consequence for the live proof route

The literature route does not close LIFT. Do not cite an analogous p^3 theorem as if it proved the exact target. The current canonical next proof step remains internal and source-level:

1. preserve the already-proved universal factor chain R -> U -> V;
2. construct a legitimate adjacent-cutoff p-adic extension Q_s from (G_p h-1)/p or an equivalent p-adic deformation;
3. compute U^Q and V^Q before quotienting;
4. prove V^Q_{s+1}=mu_s V^Q_s together with the required initial data, or retain the exact defect if this transport fails.

This audit therefore removes the tempting but invalid shortcut `cite a known p^3 Ramanujan theorem`, while preserving the exact 2025 conjectural statement as a useful external consistency witness.

BRC observer: exact weighted full-truncation carrier and p^3 theorem status. Preserved coordinates: (d,lambda,a)=(3,1/2,6), full p-1 truncation, supersingular residue classes, modulus, source status (proved / conditional / conjectural), and weighted versus unweighted provenance. Compression to a generic `Ramanujan-type supercongruence exists` is forbidden because it erases precisely the parameters that decide applicability.

BRC_REUSE_RESOLUTION=REUSE_APPLIED_AND_BOUNDARY_PROVED.
