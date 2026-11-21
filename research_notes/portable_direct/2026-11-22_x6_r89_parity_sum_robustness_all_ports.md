# X6 R89 — Parity-Sum Separation and Unbounded-Anisotropy Robustness

Date: 2026-11-22 (Asia/Shanghai).  
Scientific status: SYMBOLIC_AUTHOR_PROOF / EXACT_FRACTION_AUTHOR_CHECK_PASS / NOT_INDEPENDENTLY_REVIEWED.  
Mode: independent portable research; no formal CLAIM, PROGRESS, Result, or native P000 transfer is asserted.

## Model, lineage, and frozen source

Direct predecessor: R88 (` all-lattice 11-fold conditioning) and R87 (paired precision rays and full-lattice tie counts). Frozen scientific source remains `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json`. Current behavioral rules do not rebase that science pin.

The following theorem is **only** about the conditional positive-count degree-four BRC star-histogram observer with one unknown common additive offset and four positive real weights `w=(A,B,C,D)`. It does not assert an operation-faithful representation of signed native P000 named Port, Cell/Link, whole-triadic events, or ordered heartbeat-time histories.

For nonzero `a=(x,y,z)∈ℤ³`, identify `a` and `-a`, and set

```text
q(a) = max(x⁺+y⁺+z⁺,(-x)⁺+(-y)⁺+(-z)⁺)
Z(a) = (0,2x+6y+12z,6x+24y+60z,14x+78y+252z)
g_ij(a) = |Z_i-Z_j|/2
F(a;w) = max_{1≤i<j≤4} g_ij(a)/(w_i+w_j)
η*(p,w) = min_{a≠0, q(a)≤p} F(a;w)
```

Let `s=(10,-5,1)`, `d=min(A,C)+min(B,D)`, `K=max(A+C,B+D)`. Direct substitution gives `q(s)=11`, `g(s)=(1,0,1,1,0,1)` in pair order 12,13,14,23,24,34, and `F(s;w)=1/d`.

## Theorem R89: an all-integer-lattice separation inequality

For every positive `w` and integer `p≥11` define

```text
B_p(w) = min { F(a;w)/F(s;w) : a∈ℤ³, a≠0, ±s, q(a)≤p }.
```

Then

```text
B_p(w) ≥ 6d/K                 for 11≤p≤21,
B_p(w) ≥ min(2,6d/K)          for p≥22.                     (R89.1)
```

In particular,

```text
max(A+C,B+D) < 6[min(A,C)+min(B,D)]                        (R89.2)
```

is a sufficient open-chamber criterion for **unique optimality of s** among *all* unoriented nonzero feasible integer directions, for **every p≥11**. It can hold with `κ=max(w)/min(w)` arbitrarily large.

### Proof

Write `u=x+3y+6z`, `v=3x+12y+30z`, `h=7x+39y+126z`. The within-parity gaps are

```text
g_13(a)=|v|=3|x+4y+10z|,
g_24(a)=|h-u|=6|x+6y+20z|.
```

If `g_24(a)>0`, it is an integer multiple of 6 and at least 6. If `g_24(a)=0`, then `x=-6y-20z`, so `g_13(a)=6|y+5z|`; this is at least 6 unless `y=-5z`, which forces `a=z(10,-5,1)=zs`. Hence every integer direction outside `ℤs` has at least one of `g_13,g_24` at least 6. For every such direction,

```text
F(a;w) ≥ min(6/(A+C),6/(B+D)) = 6/K,
F(a;w)/F(s;w) ≥ 6d/K.                                    (R89.3)
```

For integral `a=ks` with `|k|≥2`, linearity gives `F(ks;w)/F(s;w)=|k|≥2`, while `q(ks)=11|k|` excludes such multiples when `p≤21`. This proves (R89.1). Under (R89.2) every competitor has ratio greater than 1, proving uniqueness. The argument covers the unbounded integer lattice directly; no finite atlas or candidate-cover certificate is invoked. ∎

## Corollary: all alternating-pair weights, all Port budgets

If `A=C=α>0` and `B=D=β>0`, with no bound on `α/β`, then `d=α+β` and `K=2max(α,β)`, giving

```text
6d/K=3(α+β)/max(α,β)>3.
```

Thus `s` uniquely minimizes `F` for **every `p≥11`**. When `11≤p≤21` all other feasible directions have objective ratio strictly exceeding 3. For **every `p≥22`**, the **unique unoriented runner-up** is `2s=(20,-10,2)` with exact ratio 2: nonmultiples have ratio >3, larger multiples have ratio at least 3, and `2s` is feasible. Example: `w=(10^6,1,10^6,1)` has `κ=10^6` yet retains the same unique optimum for all `p≥11`.

This strengthens the alternating-pair case of R87 from `p≥125` to `p≥11` without R86's finite cover. The strict inequality in (R89.2) is material: at `w=(1,1,11,11)`, `K=6d` and `(9,-5,1)` ties `s` (R88). The criterion is **sufficient**, not asserted necessary.

## Calculation and evidence

Reproduce with `python3 research_notes/portable_direct/x6_r89_parity_sum_separation_verify.py`. The companion `fractions.Fraction` checker enumerates all 47,305 nonzero unoriented integer differences with `q≤30` under 12 weight tuples (567,660 direction-weight pairs), checks (R89.1) for `p=11,21,22,30`, the open-chamber uniqueness assertion, and the exact alternating-class runner-up. All assertions passed on the author-side local run. This finite check is corroboration; the universally quantified claim rests on the symbolic divisibility proof above.

Next questions: classify the *necessary-and-sufficient* strict-optimality chamber and true/noncore tie walls outside (R89.2); sharpen the runner-up ratio for general asymmetric weights; independently test whole-triadic, named-Port and heartbeat-ordered operation-fidelity before lifting a histogram result to native P000.

Source status: frozen P000 V5, ACTIVE worldview and project methods read; mathematical result not independently reviewed.