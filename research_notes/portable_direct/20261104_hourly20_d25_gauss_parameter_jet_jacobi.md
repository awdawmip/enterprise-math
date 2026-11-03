# D25 — finite Gauss parameter jet and Jacobi boundary certificate (2026-11-04 +08)

**Evidence class:** TASK_RESEARCH author-side independent symbolic derivation; finite exact checked (157 primes); UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. This is not a native Source checkpoint, a CLAIM, a Result or a mathematical acceptance.

**Task:** RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. Publication TP2-B6F4FC938FF94941C1B7. Frozen scientific input pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Research logical lane `chatgpt-research-hourly-enterprise-math-20260923` (distinct from maintenance `chatgpt-hourly-enterprise-math-20260921`).

## Motivating frontier

Previous authored portable result proved the exact Clausen-square truncation-tail identity
`T2304 = F_p (F_p+16 D_p) - S2304(p-1)`, where
`v_i=(1/8)_i(3/8)_i/[i!^2 9^i]`,
`F_p=Σ_{0≤i<p}v_i`, `D_p=Σ_{0≤i<p}i v_i`.
An exact factor vanishing modulo p² was observed for 157 primes in residue classes 5,7,13,23 (mod 24), but requires a general proof. This note gives an **exact general p² reduction** of both factors to a finite Jacobi polynomial value, its first parameter jet, and the one-root interval. It preserves the finite p-1 truncation.

## Theorem — two-root p² decomposition (proved)

Fix a prime `p≥5` with `p≡5 or 7 (mod 8)`. Define the *integer first-root indices*
`a≡−8^{-1} (mod p)`, `b≡−3·8^{-1} (mod p)`, each in `{0,…,p−1}`,
and the exact integers `m=(8a+1)/p`, `n=(8b+3)/p`.
Set `L=min(a,b)`, `R=max(a,b)`, and `κ=m` if `L=a` or `κ=n` if `L=b`.
In these classes, `0<L<R<p`. All rational expressions below have p-unit denominators.

For `0≤i≤L`, put
`A_i=binom(a,i)binom(b,i)/9^i` (read modulo p²), and
`E_i=−[m(H_a−H_{a−i})+n(H_b−H_{b−i})]/8` (read modulo p).
For `L<i≤R` put the one-root coefficient
`C_i=(κ/8)(−1)^{L+i} L! (i−L−1)! R! / [(R−i)! (i!)² 9^i]` (mod p).

Then
```
F_p ≡ Σ(i=0..L) A_i
    + p [ Σ(i=0..L) A_i E_i + Σ(i=L+1..R) C_i ]  (mod p²).
```
In addition, for the *weighted* Gauss factor `G_p=F_p+16D_p`,
```
G_p ≡ Σ(i=0..L) (1+16i) A_i
    + p [ Σ(i=0..L) (1+16i) A_i E_i
          + Σ(i=L+1..R) (1+16i) C_i ]           (mod p²).
```
The same coefficientwise result holds with any prescribed p-integral polynomial weight `W(i)` in place of `1+16i`.

**Proof.** In the p-adic integers the equalities
`1/8=−a+mp/8` and `3/8=−b+np/8` are exact. For `i≤L`, neither `(−a)_i` nor `(−b)_i` vanishes. Expanding each rising factorial to first order in p gives
`(1/8)_i (3/8)_i / (i!)² 9^i ≡ A_i[1+p E_i]`, since `Σ_{j<i}(j−a)^{-1}=−(H_a−H_{a−i})` and likewise for b. If `L<i≤R`, the smaller-root rising factorial has exactly one p-factor; expanding that one factor and evaluating all other factors modulo p gives `p C_i`. If `R<i<p`, both rising factorials contain a p-factor, and the coefficient vanishes modulo p². Multiplying the coefficientwise identity by `W(i)` and summing proves all claimed formulas. QED.

## Jacobi-polynomial and parameter-jet interpretation (proved)

Put `P_{a,b}(z)=Σ_{i=0}^L binom(a,i)binom(b,i)z^i`. The classical finite binomial/Jacobi identity gives
```
P_{a,b}(z) = (1−z)^L · P_L^{(0,R−L)}((1+z)/(1−z)).
P_{a,b}(1/9) = (8/9)^L · P_L^{(0,R−L)}(5/4).
```
Here the right-hand `P_L^{(α,β)}` is a Jacobi polynomial, not the project P000 premise.

Define a finite *parameter jet*
```
J_p(z) = d/dt [Σ_{i=0}^R
       (−a+mt/8)_i (−b+nt/8)_i z^i /(i!)²] at t=0.
```
The explicitly given `E_i` and `C_i` are precisely its coefficient strata (for i≤L and L<i≤R). Hence
`F_p ≡ P_{a,b}(1/9)+pJ_p(1/9) (mod p²)`.
Writing `θ=z(d/dz)`,
`G_p ≡ (1+16θ)P_{a,b}(1/9)+p(1+16θ)J_p(1/9) (mod p²)`.
When the relevant base Jacobi observer is divisible by p, p²-vanishing is **equivalent** to cancellation between its quotient by p and the source-sensitive parameter jet mod p. This is an exact iff, not a conjectural final congruence.

## Executed integer evidence

The accompanying UTF-8 JavaScript uses BigInt throughout, reconstructs the original v_i independently from its exact rational recurrence, computes both Jacobi/base and two jet strata, and asserts equality modulo p² for *both* F and G. Coverage: **all 157 primes** 5≤p≤2000 with p≡5 or7 (mod8). Residue-class counts: p mod24=5:39, 7:41, 13:40, 23:37. All 314 decomposition checks passed; the prior four-class factor split was independently reproduced on all 157 primes.

Values are residues at the indicated modulus; P is modulo p², J_low/J_mid modulo p:

| p | a,b | P | J_low | J_mid | F mod p² | G mod p² |
|---:|---|---:|---:|---:|---:|---:|
| 13 | 8,11 | 104 | 6 | 12 | 0 | 137 |
| 23 | 20,14 | 368 | 15 | 15 | 0 | 243 |
| 29 | 18,25 | 403 | 8 | 17 | 287 | 0 |
| 373 | 233,326 | 27975 | 66 | 232 | 0 | 110861 |

In the F-vanishing branch the separate second digits cancel:
`p=13: P/p=8, J_low+J_mid=18≡5, 8+5≡0 (mod13)`;
`p=23: P/p=16, J_low+J_mid=30≡7, 16+7≡0 (mod23)`;
`p=373: P/p=75, J_low+J_mid=298, 75+298≡0 (mod373)`.
For `p=29` the weighted branch gives `Q=(1+16θ)P=493=17p`, weighted jet `2+10=12`, and `17+12=0 (mod29)`.

**Open hypotheses:** establish the indicated Jacobi base root modulo p and its parameter-jet cancellation for all primes p≡13,23 (mod24), with the complementary weighted observer for p≡5,7 (mod24). The 157-prime window is evidence, not a universal proof.

## BRC interface, mother objective and next action

**Carrier:** original 2304 source, finite indices i=0..p−1, the two first-root indices (a,b), their ordering and slopes (m,n), original p-valuation strata 0/1/2, binomial observer, one-root tail and first jet. **Observers:** F and G=F+16D modulo p²; operations parameter perturbation, Jacobi transformation, index-weighting, prime-residue split. Erasing the one-root stratum loses a necessary p-adic digit; e.g. p=13 has J_mid=12, and p=373 has J_mid=232.

**Next exact science unit:** prove or find a counterexample to the Jacobi-root identity `P_L^{(0,R−L)}(5/4)≡0 (modp)` for p≡13,23 (mod24), then build a finite Jacobi/parameter-derivative telescoper for `P_{a,b}(1/9)/p+J_p(1/9)≡0 (modp)`. Test first at 13,23,373 and retain full p−1 source. In parallel test weighted (1+16θ) route for p≡5,7. Once established, combine with the already-published 2304 theorem and original 216 tail/Green comparison to advance the frozen mother objective `W216(p−1)≡p (modp³)` for p≡13,19 (mod24).

No current native authorized claim/open/Source checkpoint/admission was obtained in this author-side work. Native support issue #1558 retains original recovery provenance; no session close, native write, or role-bound operation was attempted. This note and companion script are author evidence, not formal task progress.
