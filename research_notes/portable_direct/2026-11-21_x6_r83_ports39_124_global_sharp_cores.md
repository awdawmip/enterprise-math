# X6 R83 — 四阶正权 BRC 在 39–124 Port 的全域最小充分核心（6→7→8）

Date: 2026-11-21 (Asia/Shanghai).
Scientific status: EXACT FINITE INTEGER ENUMERATION + SYMBOLIC EXCEPTION LEMMAS / AUTHOR-CHECKED / NOT INDEPENDENTLY REVIEWED.
Frozen source: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json`.
Predecessors: R82 (23–38), R79 (high-Port nine-core). This proof exhausts the stated integer domains independently of the R72 28-candidate atlas.

## 1. Exact observation problem

Use the conditional positive-count degree-4 BRC star histogram with a single unknown common additive offset, and arbitrary positive real precision weights `w=(A,B,C,D)>0`. For `a=(x,y,z) in Z^3\{0}`, set

```text
q(a) = max(sum_d max(a_d,0), sum_d max(-a_d,0))
v(a) = (0, 2x+6y+12z, 6x+24y+60z, 14x+78y+252z)
g_ij(a)=|v_i-v_j|/2  (six pairs: 12,13,14,23,24,34)
F(a;w)=max_{i<j} g_ij(a)/(w_i+w_j)
eta*(p,w)=min_{0<q(a)<=p} F(a;w).
```

Differences `a,-a` give the same objective; select the representative whose first nonzero coordinate is positive.

Define the following eight labeled difference vectors:

| label | q | a=(a2,a3,a4) | six integer pair gaps |
|---|---:|---|---|
| s7 | 7 | (6,-4,1) | (0,0,12,0,12,12) |
| s10 | 10 | (9,-5,1) | (0,3,6,3,6,3) |
| s11 | 11 | (10,-5,1) | (1,0,1,1,0,1) |
| s16 | 16 | (15,-6,1) | (3,3,3,0,6,6) |
| s27 | 27 | (24,-14,3) | (0,6,0,6,0,6) |
| s39 | 39 | (36,-16,3) | (6,6,6,0,0,0) |
| s43 | 43 | (39,-20,4) | (3,3,3,6,6,0) |
| s49 | 49 | (45,-21,4) | (6,3,0,3,6,3) |

## 2. Theorem — exact minimum size, not merely a subatlas minimum

For **every** positive real `w` and integer `p` in the respective range,

```text
39 <= p <= 42: eta*(p,w) = min_{s in S39} F(s;w),
S39 = {s7,s10,s11,s16,s27,s39};                     |S39|=6.

43 <= p <= 48: eta*(p,w) = min_{s in S43} F(s;w),
S43 = S39 union {s43};                               |S43|=7.

49 <= p <= 124: eta*(p,w) = min_{s in S49} F(s;w),
S49 = S43 union {s49};                               |S49|=8.
```

Each cardinality **6, 7, 8 is the global minimum** among arbitrary fixed families of feasible nonzero integer differences giving the exact optimum for every positive real weight at that Port value. This is stronger than minimality within a prescribed atlas.

At the three exchange thresholds the corresponding weight exhibits an exact strict transition:

| transition | weight w | eta*(p-1,w) | eta*(p,w) |
|---|---|---|---|
| 38 → 39 | (15,1,1,1) | 1/2 | 3/8 |
| 42 → 43 | (7,15,1,1) | 1/2 | 3/8 |
| 48 → 49 | (1,15,7,1) | 1/2 | 3/8 |

Within each stated Port interval no further new integer competitor improves the optimum at **any** positive weight.

## 3. Exhaustive finite integer coverage (new independent computation)

The integer constraint `q(a)<=p` implies each coordinate is in `[-p,p]`, so the nested three-loop enumeration with the first-nonzero-positive sign convention is exact and complete. The executable `x6_r83_ports39_124_verify.js` checks **every** such integer difference at the upper endpoint of each interval, including all intermediate Port values.

At `p=42`, among **127,967** unoriented differences every six-gap vector is componentwise no smaller than one of
`{s3=(3,-4,1),s7,s10,s11,s16,s27,s39}`, except `b21=(21,-7,1)`.
First-witness allocation in that order: `[123628,3873,119,322,3,20,1]`.

At `p=48`, among **190,168** differences every six-gap vector is dominated by one of `S43`, except `b21=(21,-7,1)` and `b47=(42,-24,5)`. First-witness allocation in S43 order: `[188518,1036,553,4,24,29,2]`.

At `p=124`, among **3,216,374** differences every six-gap vector is dominated by one of `S49`, except `b47=(42,-24,5)`, `b71=(66,-28,5)`, and `2b47=(84,-48,10)`. First-witness allocation in S49 order: `[3204645,7690,3631,12,163,219,6,5]`.

Each domination certificate has the exact consequence `g(s)<=g(a) => F(s;w)<=F(a;w)` for **all** positive real `w`. For the exceptions the following independent symbolic inequalities finish the proof.

## 4. Exact symbolic treatment of all undominated exceptions

**Lemma A (remove the extra s3 at p>=39).** Let `s3=(3,-4,1)` with gaps `(3,9,9,6,6,0)`. Then

`min(F(s39;w),F(s11;w)) <= F(s3;w)` for all positive weights.

Proof. `F(s39)=max(6/(A+B),6/(A+C),6/(A+D))`. Since `F(s3)>=9/(A+C),9/(A+D)`, the only way `F(s39)>F(s3)` is `6/(A+B)>F(s3)`. Comparing with `F(s3)>=6/(B+C),6/(B+D)` forces `C>A,D>A`. Then all four nonzero terms of `F(s11)=max(1/(A+B),1/(A+D),1/(B+C),1/(C+D))` are below `F(s3)`: the first three by its gaps 3,9,6; the last because `C+D>A+C` and `F(s3)>=9/(A+C)`. Thus `F(s11)<F(s3)` in the remaining case. QED.

**Lemma B (b21).** With gaps `b21=(6,9,0,3,6,9)`, `s27=(0,6,0,6,0,6)`, `s11=(1,0,1,1,0,1)`,

`min(F(s11),F(s27))<=F(b21)`.

Proof: if `F(s27)>F(b21)`, its only possible exceeding term is `6/(B+C)`; comparison with `6/(A+B)` in `F(b21)` gives `C<A`. If `F(s11)>F(b21)`, its only possible exceeding term is `1/(A+D)`; comparison with `9/(A+C)` gives `C>8A+9D>A`, contradiction. This repeats the exact R82 lemma to preserve continuity.

**Lemma C (b47 and b71).** Their gap vectors are `(0,12,12,12,12,0)` and `(12,12,0,0,12,12)`; exactly as in R79,

```text
F(b47)=12/[min(A,B)+min(C,D)]
F(b71)=12/[min(A,D)+min(B,C)]
F(s27)=6/[C+min(A,B,D)]
F(s39)=6/[A+min(B,C,D)]
min(F(s27),F(s39)) <= 6/max(A,C)
                       <= 12/(A+C)
                       <= min(F(b47),F(b71)).
```

The last comparison follows because each denominator in `F(b47),F(b71)` is at most `A+C`. Therefore the same pair beats **each** exception. Finally `F(2b47)=2F(b47)`, so no third exception remains.

All s-vectors used in these inequalities fit at the start of the corresponding Port interval. Combining the complete finite enumeration with Lemmas A–C proves the theorem for all positive real weights and the full Port range.

## 5. Absolute minimality among all integer competitors

The following **eight** simple positive integer weight profiles force their indicated integer difference to be the **unique unoriented global minimizer** of `F` among *all* feasible integer differences at the relevant interval's largest Port. Every comparison is an exact integer cross-product; the verifier explicitly checks that the number of ties is one and no better vector occurs.

| label | w=(A,B,C,D) | unique optimal F |
|---|---|---|
| s7 | (1,1,1,33) | 6/17 |
| s10 | (1,1,7,15) | 3/8 |
| s11 | (1,1,1,1) | 1/2 |
| s16 | (7,1,1,15) | 3/8 |
| s27 | (1,1,15,1) | 3/8 |
| s39 | (15,1,1,1) | 3/8 |
| s43 | (7,15,1,1) | 3/8 |
| s49 | (1,15,7,1) | 3/8 |

The first six weights and vectors are tested through `p=42`, the first seven through `p=48`, and all eight through `p=124`. Unique global minimizing directions are indispensable in any weight-uniform fixed candidate family: each of these mutually different required directions must appear. This gives lower bounds of 6,7,8, matching the sufficient constructions. QED.

## 6. Reproduction, scope and next frontier

Recompute with `node research_notes/portable_direct/x6_r83_ports39_124_verify.js > results.json`. The checked JSON is saved at `research_notes/portable_direct/x6_r83_ports39_124_results.json`. The program has no packages, floating point, heuristic weights, or R72 dependency. All tested numerator/denominator cross-products are small exact JavaScript integers. An additional local C++ full enumeration independently reproduced the three domain counts and exception vectors, and Python `fractions.Fraction` checked the three boundary jumps.

P000 is held frozen. The theorem concerns a **conditional positive-count BRC observer** with a common bias. It does not assume a proven information-preserving factor map from native X6 Cell/Link/Port, whole triadic events, named branch provenance and time-update trajectories to this observer. This boundary is a separate live research obligation, not a reason to discard the observer theorem.

Next: combine R80–R83 with the R72/R79 high-Port portion into an exact piecewise all-`p` minimal-cardinality profile, independently audit the large-Port `p>=125` cone certificate and determine native source-faithful observer/fiber conditions. Retain historical contributors and do not claim a formal Task Result or peer review without corresponding authority/evidence.
