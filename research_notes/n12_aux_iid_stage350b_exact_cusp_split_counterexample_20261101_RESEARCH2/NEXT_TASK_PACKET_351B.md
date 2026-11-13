# Stage351-B — isolate the first non-endpoint allocation transition

**Predecessor:** Stage350-B exact rational counterexample at `E=11/5000` (PR #1736, dated 2026-11-01). This portable author proof reconstructs the full 16-tagged Bernoulli/BRC model and certifies two strict inequalities with rational root boxes. It supersedes only attempts to extrapolate the Stage349 endpoint formula unchanged to E=0.0022; the existing Stage349 proof on E≤0.0020 remains intact and carries its stated upstream proof obligations.

**Scientific input pins at predecessor read:** GLOBAL_KNOWLEDGE_V1 `main@7d7a66283e85dfad85849dd29e6b42cd9f0408c4`, Enterprise Math canonical `main@85f90349600ef59f4cf9fcda5201d50be257772e`; parent PR Stage349 head `e6e88125099f1b829cc09733b17b1e4a9f0c9290`. Reverify current pins, owner/claim and authentic session before formal native actions. Preserve original research contributor context; author and reviewer are not independent merely because sessions differ.

**First exact question:** In the one-source right `r1=0` arc, find the first budget `E_switch` where the two-source minimization of `φ(s)+φ(E-s)` no longer chooses `(0,E)` or `(E,0)`. Derive left/right derivatives at the algebraic tag cusp, compare `φ(0)+φ(E)` with `φ(E-s†)+φ(s†)`, and isolate equality by rational interval/real algebraic certificates. Determine whether another sourcewise Pareto region or zero stratum wins earlier than this split. Avoid assuming `E_switch = E_dagger` or that the cusp split is always globally minimizing.

**Reusable exact witness:**

```
E = 11/5000
Q1 = (231139116642/10^12, 555684475793/10^12)
Q2 = (237806870832/10^12, 575693818922/10^12)
b(Q1)+b(Q2) < 2*beta_*+E - 9/10^9
c(q*)+c(qE) - c(Q1)-c(Q2) > 1/(2*10^6)
```

Proof source, exact-checker source, executed stdout and origin/source pins are in `research_notes/n12_aux_iid_stage350b_exact_cusp_split_counterexample_20261101_RESEARCH2/` on the research PR. Reuse, do not rerun as new science. A new advance is a certified narrower switching bracket, exact global split proof, or earlier competing rational witness.

**Further obligations:** independent review of Stage336/342 sign-stratum domination and Stage347/348 chamber completeness; contrast the labeled auxiliary BRC observer with real P000-native X6/triadic/third-coordinate/time/future-operation/Cell-readout preservation. Native activity/CLAIM/Result/Driver promotion remain subject to source authority and current owner, distinct from PR evidence storage.
