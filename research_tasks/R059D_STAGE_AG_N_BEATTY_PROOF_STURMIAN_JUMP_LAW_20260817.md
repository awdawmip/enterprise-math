# R059D Stage AG — N-Resolver Algebraic Beatty Proof and Sturmian Jump Law

Task-ID: `RS-R059D-STAGE-AG-N-BEATTY-PROOF-STURMIAN-JUMP-LAW`
Identity policy: `AUTO_RESOLVE_OR_ALLOCATE`
Identity lane: `R059D-AG`
Owner branch: `research/r059d-stage-ag-n-beatty-proof-sturmian-jump-law`
Frozen source main: `fb5b7880e469c8e16769cf55601da15bb5f96b4f`
Accepted AF owner head: `9e863cfc89cab71118959deb38187a21fe1e96e1`
Date: `2026-08-17`

## 0. Driver working truth

For this research arm, freeze the following as the theorem to prove:

> The N-resolver boundary-excess count is governed by a quadratic-algebraic Beatty/Sturmian law.

The candidate is

\[
J_N(r)=\left\lfloor \alpha r+\frac13\right\rfloor,
\]

where \(\alpha\) is the unique positive root of

\[
3\alpha^2+6\alpha-1=0.
\]

Equivalently,

\[
\alpha=-1+\frac{2}{\sqrt3},
\]

but the square-root form is only an algebraic compatibility notation. The proof must not use the classical square root as a runtime generator or import a classical circle formula as a native premise.

Internal direction confidence is maximal. Do not weaken the route merely because the law was discovered experimentally. The job of Stage AG is to prove or hard-refute it from the frozen N-resolver semantics.

A hard refutation requires an exact mathematical contradiction or counterexample to the frozen law. Finite numerical discomfort, literature mismatch, or preference for another representation is not a refutation.

## 1. What AF already proved

Stage AG must inherit, not re-derive by target leakage, the accepted AF facts:

1. For each radius \(r\), the canonical one-sector N boundary word \(W_r\) is a nonnegative Motzkin excursion under the typing
   - `1 -> +1`,
   - `2 -> 0`,
   - `3 -> -1`.
2. Exactly
   \[
   \#1=\#3=J_N(r),\qquad \#2=r-J_N(r),\qquad |W_r|=r+J_N(r).
   \]
3. The bulge correction is
   \[
   B_N(r)=\sum h,
   \]
   with the AF-prescribed height sampling convention.
4. \(J\) alone does not determine \(B\); full Motzkin word state contains strictly more information.
5. The candidate
   \[
   J_N(r)=\left\lfloor \alpha r+\frac13\right\rfloor
   \]
   had zero mismatches on discovery `r=1..256` and zero mismatches on untouched holdout `r=257..512`.
6. AF froze an equivalent integer forward recurrence for the candidate:
   - `j(0)=0`;
   - at radius `r>=1`, increment `j` iff
   \[
   3(3j+2)^2+6(3j+2)(3r)-(3r)^2\le0.
   \]
7. C is not the target of this stage. C may be used only after the N theorem is established, as a phase/tie-break comparison.

## 2. Stage AG single hard target

\[
\boxed{
\texttt{PROVE\_N\_BEATTY\_STURMIAN\_JUMP\_LAW}
}
\]

A passing AG result must establish, for every integer \(r\ge0\):

\[
\boxed{
J_N(r)=\left\lfloor \alpha r+\frac13\right\rfloor
}
\]

with \(\alpha\) the positive root of

\[
3\alpha^2+6\alpha-1=0.
\]

This must be a theorem derived from the exact N-resolver / boundary semantics, not a finite-range pattern claim.

If the exact law is false, Stage AG must produce the first exact mathematical counterexample together with the precise broken implication in the attempted proof. Do not silently replace the theorem with a nearby fit.

## 3. Required proof chain

The proof must be decomposed into explicit lemmas. At minimum attempt the following chain.

### AG-L1 — Exact N boundary event criterion

Starting from the frozen N resolver definition, derive an exact inequality deciding when the sector boundary acquires one additional up/down Motzkin pair, i.e. when

\[
\Delta J_N(r)=J_N(r)-J_N(r-1)=1.
\]

The criterion must be stated with integers or exact rational/algebraic inequalities.

No table lookup of AF `J_N` values may appear in the theorem proof.

### AG-L2 — Quadratic threshold reduction

Show that the exact N boundary event criterion is equivalent to a single quadratic threshold governed by the positive root \(\alpha\) of

\[
3x^2+6x-1=0.
\]

The preferred target form is equivalent to

\[
J_N(r)=j
\quad\Longleftrightarrow\quad
j\le \alpha r+\frac13<j+1.
\]

or an exact integer inequality from which this follows immediately.

### AG-L3 — Floor-law theorem

Prove by direct inequality, induction on \(r\), or exact jump-position characterization that

\[
J_N(r)=\left\lfloor \alpha r+\frac13\right\rfloor.
\]

A merely computational induction through a finite bound does not pass.

### AG-L4 — Exact jump-position formula

Let \(r_m\) be the first radius with \(J_N(r_m)=m\). Derive an exact formula such as

\[
\boxed{
r_m=\left\lceil\frac{m-1/3}{\alpha}\right\rceil
}
\]

and then simplify it using the quadratic identity. Since

\[
\alpha^{-1}=3+2\sqrt3,
\]

a classical algebraic notation may be given after the integer/algebraic derivation.

Tie/equality cases must be handled explicitly. Do not assume irrationality without proving it from the minimal polynomial.

### AG-L5 — Gap alphabet theorem

Prove the exact jump gap alphabet:

\[
g_m=r_{m+1}-r_m\in\{6,7\}.
\]

Do not infer this only from the first 512 radii.

### AG-L6 — Sturmian / mechanical-word characterization

Prove that

\[
s_r:=\Delta J_N(r)\in\{0,1\}
\]

is the mechanical/Sturmian coding determined by the same quadratic slope and phase.

State the precise convention used (lower/upper mechanical word, intercept, indexing). Avoid loose use of the word `Sturmian`.

### AG-L7 — Periodic continued-fraction structure

Derive the periodic continued fraction of the slope or its reciprocal from the quadratic equation. The expected simple structure should be proved, not imported as a fit.

At minimum determine and verify the exact periodic block. Use it to derive a hierarchy of best rational approximants / convergents for the jump schedule.

### AG-L8 — Finite substitution or morphic consequence, if exact

Investigate whether the periodic continued fraction gives an exact substitution/morphism generating the jump word. If yes, prove it and give a forward generator independent of N occupancy lookup.

If no compact substitution is established, report the strongest exact Sturmian generator instead. Do not invent an ad hoc automaton merely to satisfy this item.

## 4. Integer-only forward generator requirement

The theorem package must include at least one forward generator for \(J_N\) that uses only integer arithmetic/comparison after initialization.

AF already proposed:

```text
j(0)=0
for r >= 1:
    increment j iff
    3(3j+2)^2 + 6(3j+2)(3r) - (3r)^2 <= 0
```

AG must either prove this recurrence equivalent to the floor theorem for all \(r\), or replace it with a simpler exact integer recurrence and prove equivalence.

Runtime prohibitions:

- no `sqrt`;
- no floating point;
- no source-Q lookup;
- no AD/AE/AF occupancy query;
- no precomputed jump table;
- no radius-specific tuning.

## 5. Relation to the Motzkin boundary word

AG does **not** need to solve the full \(W_r\to W_{r+1}\) generator. That is a later stage unless it falls out naturally.

But AG must derive all exact consequences for the Motzkin word that follow from the proved \(J_N\) theorem, including:

\[
\#1=\#3=\left\lfloor \alpha r+\frac13\right\rfloor,
\]

\[
\#2=r-\left\lfloor \alpha r+\frac13\right\rfloor,
\]

\[
|W_r|=r+\left\lfloor \alpha r+\frac13\right\rfloor.
\]

Determine the asymptotic symbol densities exactly.

This is a count theorem only. Do not infer \(B\) or the internal arrangement of \(W_r\) from \(J\) alone; AF has already proved that inference false.

## 6. C-resolver comparison after the N theorem

Only after AG-L1..L6 are proved may C be revisited.

Use the proved N jump schedule to classify the AF observation that every N/C \(J\)-disagreement through `r<=512` was a one-radius delay:

\[
N\text{ jumps at }r,\qquad C\text{ jumps at }r+1.
\]

Allowed outcomes:

- `C_IS_EXACT_PHASE_TIEBREAK_OF_N_PROVED`;
- `C_PHASE_DELAY_RULE_REFINED_BUT_PROOF_OPEN`;
- `FINITE_CENSUS_ONLY`;
- exact counterexample beyond previous range.

Do not let C work block completion of the N theorem.

## 7. Validation protocol

Once the theorem is proved symbolically, generate fresh validation data from the theorem, not from a fitted table.

Mandatory validation:

- exact comparison against frozen N ledger for `r=1..512`;
- extend checker comparison to at least `r=4096` if the N source generator can be replayed at reasonable cost;
- preferred extension `r=16384`;
- verify jump gaps are only `6/7` on the extended finite census;
- verify integer recurrence = floor formula = source N ledger on the tested range.

These finite checks validate the implementation of the proof; they do not replace the proof.

## 8. Target-leakage firewall

Classical geometry may not generate the theorem.

Forbidden theorem premises:

- Euclidean circle equation as a native law;
- classical circumference / pi;
- equal-distance locus definition;
- floating `sqrt(3)` fit;
- continued-fraction parameters imported because they match the observed sequence;
- lookup into AF jump positions during runtime.

Permitted:

- exact N resolver semantics already frozen upstream;
- integer triangular-grid incidence/edge relations;
- algebraic manipulation after the quadratic polynomial is derived from the N event criterion;
- classical names such as Beatty/Sturmian/continued fraction only after the native derivation establishes the same structure.

## 9. Required artifacts

Create at minimum:

- `research_results/R059D_STAGE_AG/R059D_STAGE_AG_REPORT.md`
- `research_results/R059D_STAGE_AG/R059D_STAGE_AG_PROOF.md`
- `research_results/R059D_STAGE_AG/R059D_STAGE_AG_N_EVENT_CRITERION.json`
- `research_results/R059D_STAGE_AG/R059D_STAGE_AG_BEATTY_THEOREM.json`
- `research_results/R059D_STAGE_AG/R059D_STAGE_AG_JUMP_POSITIONS.json`
- `research_results/R059D_STAGE_AG/R059D_STAGE_AG_STURMIAN_STRUCTURE.json`
- `research_results/R059D_STAGE_AG/R059D_STAGE_AG_INTEGER_GENERATOR.json`
- `research_results/R059D_STAGE_AG/R059D_STAGE_AG_EXTENDED_VALIDATION.json`
- `research_results/R059D_STAGE_AG/R059D_STAGE_AG_TARGET_LEAKAGE_AUDIT.json`
- `research_results/R059D_STAGE_AG/R059D_STAGE_AG_DETERMINISTIC_CHECKER_OUTPUT.json`
- `research_results/R059D_STAGE_AG/R059D_STAGE_AG_FROZEN_CHECKPOINT.json`

If Lean formalization is practical and local infrastructure already supports the required arithmetic, add it. Lean is valuable but is not allowed to delay the mathematical proof if the formalization path becomes a tooling bottleneck.

## 10. Deterministic checker gates

The checker must verify at least:

1. source/AF immutability;
2. exact polynomial and positive-root typing;
3. exact integer recurrence;
4. recurrence/floor equivalence on a broad deterministic range;
5. jump-position formula;
6. gap alphabet `{6,7}` over broad finite replay;
7. all frozen AF `J_N` rows reproduced;
8. extended N replay reproduced;
9. no occupancy/table lookup inside the theorem generator;
10. target-leakage audit complete;
11. theorem/census/candidate statuses separated.

## 11. Promotion statuses

Strongest allowed disposition:

`N_BEATTY_STURMIAN_JUMP_LAW_PROVED`

Second:

`N_QUADRATIC_JUMP_CRITERION_PROVED__FLOOR_EQUIVALENCE_PROOF_INCOMPLETE`

Third:

`N_BEATTY_LAW_HARD_REFUTED__EXACT_COUNTEREXAMPLE_FOUND`

Weak finite validation alone is **not** an acceptable successful completion because AF already supplied that evidence.

## 12. Next-stage gate

Only after `N_BEATTY_STURMIAN_JUMP_LAW_PROVED` should the control plane open the next hard problem:

\[
\boxed{W_r\longrightarrow W_{r+1}}
\]

with the proved jump skeleton frozen as input.

That later stage will ask whether the complete Motzkin integer-curvature word admits a finite/local/substitutional growth law, and therefore whether

\[
r\longrightarrow W_r\longrightarrow(B,J)\longrightarrow(C,V)
\]

can become a completely autonomous Enterprise-circle generator.

## 13. Completion estimate / advancement vector

Before AG:

- count semantics: `~100%` for current carrier;
- first bulge boundary: `~100%`;
- Motzkin state reduction: `~100%`;
- N jump-law empirical identification: `~90%`;
- N jump-law theorem proof: `0%`;
- complete word generator: `0%`.

Target after AG:

- N jump-law theorem proof: `+90..100%`;
- exact jump-position/gap structure: `+100%`;
- Sturmian/arithmetic structure: `+80..100%`;
- complete word generator: `+0..20%` only if it follows naturally.

Advancement vector:

`N-jump-proof +100 / jump-arithmetic +90 / Motzkin-count-structure +30 / full-word-generator +10 / resolver-selection +5`.

## 14. Stop condition

Stop for Driver review only after one of the explicit promotion statuses in §11 is supported by artifacts and deterministic replay.

Do not open Stage AH or later work on this branch.
