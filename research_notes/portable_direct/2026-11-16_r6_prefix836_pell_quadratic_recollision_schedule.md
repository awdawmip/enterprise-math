# PREFIX-836 — Pell-parametrized quadratic-time / square-root-weight Q-recollision subsequence

**Date:** 2026-11-16. **Research status:** AUTHOR_PROVED / EXACT_PELL_IDENTITY / EXACT_NAMED_STATE_REGRESSION / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.

**Frozen science:** `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`. **Previous precise interfaces:** PREFIX-832 full-time positive Q histogram, PREFIX-833 unique recollision criterion, PREFIX-834 all-parity three-source classification, PREFIX-835 exact M(T) for even T=4..40 and universal lower bound. Current account normative overlay/P000/ACTIVE worldview were read separately, without repinning the scientific model.

## 1. Mathematical problem and model

Fix capacity p=q=3, three named unmarked sources initially present, marked source absent, positive integer unmarked removal weights, marked insertion weight a=1 and marked removal weight b=2. The sole future operation is Q=R+A, the sum of all legal positive-weight transitions. Its output Y(t) is the full **unnormalized** integer occupancy histogram (bins 0,1,2,3) at integer step t. For each even T≥4, M(T) is the least possible maximum source weight over two distinct three-source multisets with a positive-time separation followed by full histogram re-aliasing at T.

Theorem 835.2 establishes M(T)≥ceil(sqrt((T+2)/4)), while PREFIX-834 gives the universal upper M(T)≤3T−1. We resolve the optimal **growth exponent on an infinite, explicitly generated even-time subsequence**.

## 2. Exact construction

Start with integers (x_0,y_0)=(3,3) and define for k≥0
```
x_(k+1) = 3*x_k + 2*y_k,
y_(k+1) = 4*x_k + 3*y_k.
```
For k≥1 set c_k=(y_k−1)/2, and two *named* source-weight triples
```
A_k=(1, x_k+1, x_k+1)
B_k=(2, x_k+c_k+1, x_k−c_k).
```
Let
```
T_k=2 + (x_k−3)(x_k+1)/6 = ((x_k−1)^2+8)/6,
W_k=x_k+(y_k+1)/2.
```

**Theorem PREFIX-836.1 (all k≥1):** These are legal positive-integer source profiles, T_k is an even integer ≥34, the complete BRC Q histograms coincide precisely at t∈{0,1,T_k} and are different at every other nonnegative integer t; the maximum source weight across the pair is W_k.

**Proof.** The recurrence preserves 2x²−y², because
2(3x+2y)²−(4x+3y)²=2x²−y²; the starting value is 9. Inductively x≡3 (mod 12), y≡3 or 9 (mod 12), alternating, so y is odd, (x−3) is divisible by 12 and T−2=(x−3)(x+1)/6 is a positive even integer for k≥1. Positivity follows from y²=2x²−9<4x² for positive x: 0≤c<x, so x−c≥1.

Write e_j for the elementary symmetric coefficients of the three source weights. For the two triples,
```
Delta e1=0,
Delta e2=c(c+1)−x+1=(x−3)(x+1)/2>0,
Delta e3=1−x^2+2c(c+1)=(1−2x^2+y^2)/2=−4.
```
Thus the first different coefficient is n=2. By the exact positive Q p=3 full-histogram criterion of PREFIX-834.2, a full re-alias at even T≥4 occurs iff
```
4*Delta e2 + 3*(T−2)*Delta e3 = 0.
```
The defined T makes this expression exactly zero. PREFIX-833.1 supplies uniqueness of the exceptional positive-time re-alias and separates all other t≥2, while t=0,1 agree from initial occupancy and equal e1. The largest entry is x+c+1 = W. QED.

**Theorem PREFIX-836.2 (sharp subsequence exponent):** The sequence T_k grows strictly and without bound, and
```
M(T_k) = Theta(sqrt(T_k))  as k -> infinity.
```
More precisely,
```
(1/2)*sqrt(T_k+2) ≤ M(T_k) ≤ W_k,
lim_(k->infinity) W_k/sqrt(T_k) = sqrt(6)*(1+1/sqrt(2)).
```

**Proof.** The recurrence has positive entries and x_(k+1)>x_k, so x_k→∞ and T_k=((x_k−1)²+8)/6→∞. The Pell identity gives y_k/x_k→sqrt(2). Therefore W_k/x_k→1+1/sqrt(2) and sqrt(T_k)/x_k→1/sqrt(6), proving the limit. The first inequality is the all-T lower bound proved in PREFIX-835.2, and the constructed pair gives M(T_k)≤W_k. Both sides bound M(T_k) above and below by positive constant multiples of sqrt(T_k). QED.

This produces infinitely many even collision times with maximum source weights growing on the **square-root scale**, improving the former linear constructive bound at these times and proving the general square-root lower law has the correct exponent on an infinite subsequence. It does not determine M(T) at arbitrary even times, or claim that W_k itself is an exact minimizer at k≥2.

## 3. Reproducible exact instances

| k | (x,y) | T | A | B | maximum W |
|---:|---|---:|---|---|---:|
| 1 | (15,21) | 34 | (1,16,16) | (2,26,5) | 26 |
| 2 | (87,123) | 1234 | (1,88,88) | (2,149,26) | 149 |
| 3 | (507,717) | 42674 | (1,508,508) | (2,866,149) | 866 |
| 4 | (2955,4179) | 1454354 | (1,2956,2956) | (2,5045,866) | 5045 |
| 5 | (17223,24357) | 49432882 | (1,17224,17224) | (2,29402,5045) | 29402 |

The first k=1 profile is the already-established PREFIX-835 *exact optimum* M(34)=26; the k≥2 profiles are new large-time constructive certificates. At k=2, Δe2=3696 and Δe3=−4; the full observer agrees at t=1234.

## 4. Exact verification and limitation

`PREFIX836_R6_PELL_RECOLLISION_CHECK.js` is a dependency-free BigInt checker. It checks five Pell instances, both triples' e1/e2/e3, the collision criterion and operator parameters, and **independently** iterates all named subsets and marked-presence flags with the actual Q transition weights for k=1 and 2 through t=T+2. It compares all four histogram bins at each frame: 5,096 scalar comparisons. The only equality times observed are {0,1,34} and {0,1,1234}. `PREFIX836_R6_PELL_RECOLLISION_RESULTS.json` contains these exact computations. The unbounded-k statement rests on the displayed algebraic proof, not finite testing.

All arithmetic in the checker is BigInt with no floating-point approximation. Its per-frame observer is a sum over the named state-space, not the closed-form elementary-symmetric observer. The two evaluations therefore check different representations of the same stipulated Q model.

## 5. Provenance and next scientific questions

This extends the specific PREFIX-835 weight-resource problem; Pell recurrences are a standard Diophantine construction, and the new conclusion is their exact transfer to the fixed three-source BRC recollision interface with a square-root resource law. Its lower bound and collision criterion reuse existing PREFIX theorems rather than constituting new foundational project admissions.

Open: establish bounds at *every* even T; find further Pell or near-Pell families with smaller constant W/sqrt(T) or denser time coverage; decide whether M(T) has large gaps above sqrt(T); independently resolve the q≥5,b>0 minimal positive integer Q-carrier. Keep this positive named-source count model separate from signed-amplitude cancellation and native X6 event time.

**Scientific provenance:** PREFIX-835 immutable paper blob `88cc76530e9a480b696d28ab9982decf1a5f3a15`; PREFIX-834 immutable paper blob `51e86b03470741d24c9a8052ae3f51cb5199f4c0`; current normative continuity `docs/RESEARCH_CONTINUATION_PROTOCOL.md` blob `08e674246c20f768b6288bbc0df42324bd07fb75`. Scientific input remains pinned to `f42f2906d77f24085c123f3ccfe9667d41caa96d`.
