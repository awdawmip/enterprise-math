# R5 — Fixed-budget source-faithful observer: semilinear and periodic safety spectrum

Date: 2026-11-19. Mathematical status: **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**.

## Provenance and scope

Continues the verified **BCPT1–3** result at
`awdawmip/enterprise-math@78ef1422e6d661ace839b0c2ad916b7f50e40518:research_notes/portable_direct/r5_budgeted_prefix_observer_20261119/RESEARCH.md`.
The original frozen scientific pin remains `435e77af0d180eac32bd1f9c4c464bc4010b7551`, with prior 256-state center-table SHA-256 `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`.
This is a finite deterministic **auxiliary response observer**, NOT an asserted native transfer to the R5 256-state Bellman/Port/source model. P000, ACTIVE worldview, six-dimensional discrete spatial space and independent time retain their original scopes. No heartbeat/BRC-Shor numerical operation is executed.

Let `Ω` be finite, `A` a finite action alphabet, `T_a:Ω→Ω` deterministic, `L:Ω→2^[n]` a named positive-support label, and `c_a:Ω→N` a nonnegative integer cost. Fix `x∈Ω` and nonempty finite `Y⊆Ω\{x}`. Define `C_z(w)` as the cumulative cost for a word `w` from `z`, and `D_y(w)` as the condition that every prefix `w_j` (including the empty prefix) satisfies `L(T_{w_j}x)⊆L(T_{w_j}y)`. The common-source prefix observer admits deletion of `x` at integer budget `B≥0` exactly when

```text
SAFE(B) := ∀w∈A*: C_x(w)≤B ⇒ ∃y∈Y:
           D_y(w) AND C_y(w)≤B.
```

The alternative may depend on the *whole fixed word*, but must be the **same** initial response for every prefix of that word. No negative-feedback, adaptive Bellman strategy or unproven provenance quotient is included.

## BS1: Effectively semilinear budget spectrum

**Theorem.** `GOOD={B∈N:SAFE(B)}` and its complement `BAD` are effectively semilinear sets of nonnegative integers. Hence they are ultimately periodic, although they need not stabilize to a constant verdict.

**Proof.** Enumerate `Y={y_1,...,y_m}`. Take a finite deterministic synchronous product carrying the current images of `x,y_1,...,y_m`. For each `i`, maintain a Boolean flag `f_i` which starts with `L(x)⊆L(y_i)` and is conjoined after every action with containment of the new labels. Thus `f_i` records *all prefixes*, not just the last one. Each transition carries a fixed vector of `m+1` nonnegative integer costs, one for each initial response.

For each fixed final flag vector, valid action/transition sequences form a regular language over an alphabet of product edges. Its effective Parikh image is semilinear; apply the integer-linear transition-count-to-cost map. This produces an effective Presburger definition for the possible joint cumulative cost vectors `(d_0,d_1,...,d_m)` and the chosen final flags. A budget is bad exactly when such a vector/flag state exists with
`d_0≤B AND ∧_{i=1}^m (¬f_i OR d_i>B)`.
The condition is Presburger. Finite unions and existential projections of Presburger-definable sets remain Presburger-definable. The resulting one-dimensional set BAD is effectively semilinear; so is its complement GOOD. One-dimensional semilinear sets are ultimately periodic. QED.

The standard **effective Parikh-image theorem** is an external mathematical dependency, not claimed as a new proof:
Esparza–Ganty–Kiefer–Luttenberger (2011), *Parikh's theorem: A simple and direct automaton construction*, Information Processing Letters 111, 614–619, DOI 10.1016/j.ipl.2011.03.019; and A. W. To (2010), *Parikh Images of Regular Languages: Complexity and Applications*, arXiv:1002.1464.

## BS2: Explicit infinite alternating-budget family

For any `q≥2` and `1≤d<q`, let `Ω={x,y,z}`, `A={a}`, `Y={y}`, all labels equal to the *same nonempty named support*, transitions `x→x, y→z, z→z`, and action costs `c_a(x)=q, c_a(y)=q+d, c_a(z)=q`.

**Theorem (exact for all budgets).**

```text
SAFE(B) ⇔ (B<q) OR (B mod q ≥ d).
```

**Proof.** For the empty word, both costs are zero. For every `t≥1`, the word `a^t` costs `qt` from `x` and `qt+d` from `y`; all prefix labels match. If `B<q`, only the empty source word is feasible, hence safe. Otherwise the longest source-feasible word has `t=floor(B/q)≥1`; this is the most expensive alternative. Thus all feasible words have a surviving alternative exactly when `q floor(B/q)+d≤B`, equivalently `B mod q≥d`. QED.

In particular `q=2,d=1` gives `GOOD={0,1,3,5,...}` and `BAD={2,4,6,...}`. Both are infinite. Fixed-budget safety is **not eventually constant** for unbounded words, even in a three-state, one-action, all-labels-equal system with positive integer costs. BS1 and BS2 are compatible: eventual periodicity is strictly weaker than eventual constancy.

## BS3: All-budget criterion

`∀B≥0 SAFE(B)` **if and only if**
`∀w∈A* ∃y∈Y: D_y(w) AND C_y(w)≤C_x(w)`.

For necessity, apply SAFE at `B=C_x(w)`. For sufficiency, the very same representative is feasible at every `B≥C_x(w)`. Note the quantifier order: a different representative may be chosen for each completed word.

## BS4: Bounded-horizon stabilization

If only words with `|w|≤H` are observed and `c_max=max_{a,z}c_a(z)`, then for all `B≥H c_max` the safety verdict equals the **unbudgeted** common-source prefix verdict, because every response can execute every word in the horizon at cost at most `H c_max`. The infinite alternation of BS2 needs an **unbounded word horizon**, and by itself says nothing about oscillation in fixed-depth Bellman trees.

## Exact checks and evidence scope

`VERIFY_BUDGET_SPECTRUM.py` implements independent full-prefix BFS, retaining each candidate response separately (no same-image min-cost pruning). For `q=2,...,9`, every `d=1,...,q-1`, and `B=0,...,6q+2`, the BFS verdict agrees with the symbolic formula in all **36 families and 1548 budget checks**. It also tests the source BCPT3 0/1-cost three-state witness at budgets 0,1,2,3, obtaining safe/unsafe/safe/safe. Exact integer/Boolean operations only. The finite checks **do not prove** BS1 or the infinite parameter quantifier in BS2; those claims rely on the separate proofs above.

Local independently executed result: `PASS_R5_BUDGET_SPECTRUM 36 1548 [True,True,False,True,False,True,False,True,False,True,False]`. Full local JSON and hash-verified reproducibility ZIP: `EnterpriseMath_R5_BudgetSpectrum_20261119.zip` (conversation artifact).

## Next unresolved obligations

1. Derive and verify the **actual** frozen 256-state Bellman action/branch cost, negative feedback, named Port and same-source semantics before any native application.
2. Decide whether the eight-error Bellman problem's exact observer is fixed-word positive-prefix, online/adaptive, or full positive/negative response; the quantifier order changes.
3. Implement effective semilinear/Presburger certificate extraction, including actual period/preperiod, for the auxiliary model; BS1 proves computability, not a computed period for every input.
4. Previous 256-state bound remains `8335≤C8*≤8343`; this note establishes no stronger lower bound.

**Review:** NOT_REVIEWED. No formal CLAIM/RUN, Result, Working Truth, Foundation or native BRC theorem promotion is asserted by this research note.
