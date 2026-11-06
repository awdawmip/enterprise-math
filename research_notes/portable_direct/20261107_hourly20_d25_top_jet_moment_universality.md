# D25: universal top-jet stratification and finite-field source moments

Date: 2026-11-07 (Asia/Hong_Kong). Scoped author-side **portable evidence only**: UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CHECKPOINT.
Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific pin: `c47e13e4aba0e006366f989d6334d443f6333ae3` (unchanged). Configured lane label `chatgpt-research-hourly-enterprise-math-20260923` does not attest a recoverable current service session. Prior all-order single-carry result: `20261106_hourly20_d25_all_order_single_carry_jet.md`.

## 1. New all-prime theorem: degree, exact top coefficients and source separation

Fix any prime `p=6m+1 >=7`, and set `a=2m, b=3m, c=4m=(p-1)-2m`. Work in `F_p[z]` with labelled input sources

`P_m(z) = Σ_(j=0)^b (6j+1)(-1/2)^j binom(b,j) binom(a+z,j) binom(c+z,j).`

Then, writing `chi_p(2)=2^((p-1)/2) ∈ {+1,-1}`,

```
deg(P_m mod p) = p-1 = 6m,
[z^(p-1)]P_m = 2 chi_p(2),
[z^(p-2)]P_m = -chi_p(2)/2,
[z^(p-3)]P_m = (301/144) chi_p(2)         in F_p.
```

In particular the polynomial is **not identically zero** mod p. The first two displayed coefficients are nonzero in every allowed characteristic, despite previously observed cancellations of the LOW source jets. These formulas are proved, not inferred from the finite scan.

**Proof.** The degree of the summand indexed by `j` is at most `2j`; only `j=b` reaches `2b=p-1`. Its leading term equals
`L=(6b+1)(-1/2)^b/(b!)^2`.
Here `6b+1 ≡ -2 (mod p)`, Euler's criterion gives `(-1/2)^b=chi_p(-2)`, and Wilson pairing gives `(b!)^2=(-1)^(b+1)`. Hence `L=2 chi_p(2)`. The penultimate coefficient comes only from this top summand and is `L*b(b+1)= -L/4`, since the sum of its 2b labelled linear-factor constants is `b(a+c-b+1)=b(b+1)`. For the next coefficient, the top summand's elementary symmetric sum is `e_2=13/288` mod p (since `Σ constants^2 = -1/36`), while the `j=b-1` summand contributes its leading coefficient `L` (its ratio to `L` is one). Thus `[z^(p-3)]P_m=L(1+13/288)=L*301/288`. All divisions use p-units. QED.

Each normal-index term `j<=a=2m` has degree <=4m. Consequently **every coefficient with `4m<r<=6m` comes exclusively from the carry-labelled index population `a<j<=b`**. Its highest two nonzero coefficients above demonstrate that the carry contribution cannot be eliminated by any coefficientwise cancellation with the normal population. This is a precise high-order provenance distinction; it does not contradict a possible local vanishing of `[z]P_m`.

## 2. New fixed-codimension universality theorem (all k with p>k+2)

For each fixed `k>=0` there is a rational number `C_k`, independent of p, such that for every prime `p=6m+1` with `p>k+2`,

`[z^(p-1-k)]P_m(z) ≡ 2 chi_p(2) C_k (mod p).`

The constants are explicit rather than merely existential. Let `E_d(n;A,C)` be the polynomial in rational `n,A,C` obtained by Newton identities from the Faulhaber extensions of the finite power sums
`S_r(n;A,C)=Σ_(h=0)^(n-1) ((A-h)^r+(C-h)^r)`;
`E_0=1`, `d E_d = Σ_(r=1)^d (-1)^(r-1)E_(d-r)S_r`.
Define `(1/2)^{overline{ell}}=Π_(h=0)^(ell-1)(h+1/2)`. Then

```
C_k = Σ_(ell=0)^floor(k/2)
       ((1+3ell) 2^ell ((1/2)^{overline{ell}})^3 / ell!)
       E_(k-2ell)(-1/2-ell; -1/3, -2/3).
```

**Proof.** For coefficient `[z^(2b-k)]` only indices `j=b-ell` with `0<=ell<=floor(k/2)` can contribute. Dividing their leading coefficient by `L` gives exactly
```
(6b-6ell+1)/(6b+1) * (-2)^ell * (b(b-1)...(b-ell+1))^3/ell!.
```
Substitute `b=(p-1)/2 ≡ -1/2`, `a=2b/3 ≡ -1/3`, `c=4b/3 ≡ -2/3`; the ratio becomes the constant multiplier above. The remaining near-top elementary-symmetric coefficient is a rational polynomial in the number of factors and their affine endpoints, as witnessed by Faulhaber power sums plus Newton recursion. For `p>k+2`, all denominators arising up to order k are units modulo p (including the necessary Bernoulli, factorial and Newton denominators). Hence substitution gives the exact residue. QED.

Explicit universal constants, computed with **rational arithmetic**:
```
k:   0        1          2         3          4                5
Ck:  1       -1/4      301/288   -865/384   524161/55296   -9262421/221184
k:   6                    7                       8
Ck:  11448840713/47775744  -295941110075/191102976  638943911769443/55037657088
```
These are fixed-codimension coefficients, not a claim about k comparable with or larger than p. For example, blindly applying the k=6 rational expression at p=7 (outside `p>k+2`) gives an incorrect value; the bounded characteristic hypothesis matters.

## 3. Second unit: two exact global field moments and a new first-jet observer

For the same polynomial, its degree `p-1` allows the standard finite-field power-sum pairing:
```
Σ_(z in F_p) P_m(z)      = -2 chi_p(2),
Σ_(z in F_p) z P_m(z)    =  chi_p(2)/2,
[z^r]P_m(z)              = -Σ_(z in F_p^×) z^(-r)P_m(z)
                              (1<=r<=p-2).
```
**Proof.** In `F_p`, `Σ_z z^n` is `-1` for positive `n` divisible by `p-1`, and `0` otherwise, with the n=0 sum also 0. Apply this coefficientwise to a polynomial of degree at most `p-1`. QED.

Thus the still-open exterior tangent assertion has a second, exact equivalent target:
```
T_1 + T_3 = [z]P_m(z) = A_m-B_m
          = -Σ_(z in F_p^×) P_m(z)/z.
```
This is a **change of observer**, not a proof that the final sum vanishes. A finite-field inverse-moment route may be compared with the existing head/carry harmonic WZ target. A global scalar moment does not retain individual source labels, so it does not replace the labelled head/carry decomposition. The top nonzero coefficient rules out attempting to prove the first-derivative conjecture by the much stronger false identity `P_m(z)≡0` as a whole polynomial.

## 4. Executed certificates and limitations

Actual standalone Python integer/rational checker: `d25_top_jet_universality_20261107.py`. It independently computes the rational Faulhaber/Newton constants, reconstructs top coefficients by multiplying the **original labelled linear factors in F_p**, and checks all 611 primes `7<=p<=10000, p≡1(mod6)`, up to `k=min(8,p-3)`: **611/611 PASS**. Example `p=5113`: top three field coefficients `2,2556,2097` respectively. A separate exhaustive field-value evaluator for `p=7,13,19,31,37,43,109,211` checks both global moments and independently differentiated first-jet inverse-moment equality; all eight PASS. No floating-point arithmetic, no formal Lean claim and no native experiment are implied.

## 5. Control boundary and next step

This is new **author-side proof and exact portable evidence** only. The scheduled Research lane's own current issued Researcher session, prior contribution ledger, protected staging, winning CLAIM, run and native Source checkpoint were not verified. Original reads `em-h20-20261106-1324-d25-task-r13` and `em-h20-20261106-1324-d25-cont-r13` were reconciled under their original IDs; latest transport state `QUEUED`, older `EVENT_COLLECTION_IO` remains visible. Control support: #1558. No session reset, claim, open, freeze or native publication is asserted.

**Next smallest science action:** exploit `A_m-B_m=-Σ_{z!=0}P_m(z)/z` to attempt a concrete finite-field summation/creative-telescoping identity for the single derivative coefficient, while preserving the known head/carry boundary. Compare the inverse-moment and WZ routes; do not seek a false all-coefficient vanishing. Mother objective stays `Delta_p-R_p=0 (mod p)` for `p≡13,19 (mod24)`. Original H0/B0 (p=373), Frobenius, eta/kappa and independent review remain open; other owner lanes' Pfaff/Gauss results are not republished here.
