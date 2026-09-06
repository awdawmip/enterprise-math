# Viète/X6 triadic rotation law selection: Q-equivariance reduces 64 shortest branch words to two, faithful C12 refinement uniquely selects all-OUTER

Status: `FREE_RESEARCH / EXACT ROOT-REFINING LAW-SELECTION THEOREM / NOT_FOUNDATION`
Date: `2026-09-06`
Researcher: `EM-FREE-7D3C9A / FREE_AXIOM_DISCOVERY`
Parent issue: `#1255`
Parent line: `#1158`
Consumes:
- `research_notes/X6_TRIADIC_ROTATION_GENERATORS_V1_20260906.md`
- `research_notes/X6_ROTATION_PATH_GROUPOID_V2_20260906.md`
- `research_notes/VIETE_X6_ALL20_TRIADIC_ROOT_C24_BRIDGE_20260906.md`
Checker: `experiments/viete_x6_outer_law_selection_20260906/check_viete_x6_outer_law_selection.py`
Checker source commit: `e6f018e0f4648b35fe60ae187357d79fdf778cb5`
Current source frontier consumed: `main@e6f018e0f4648b35fe60ae187357d79fdf778cb5`

## 1. Exact problem

For one oriented native triad `S`, the intrinsic generator `Q_S` has six macro phase edges.  Every macro edge has exactly two shortest native two-step realizations:

- `INNER`: `a_r -> 0 -> a_(r+1)`;
- `OUTER`: `a_r -> a_r+a_(r+1) -> a_(r+1)`.

A complete shortest lift of the six-edge frame cycle is therefore a branch word

`beta=(beta_0,...,beta_5) in {I,O}^6`,

and there are exactly

`2^6=64`

such shortest words.

The rotation-path groupoid deliberately retains all 64 because endpoint/frame data alone do not select one.

The present question is narrower:

> among deterministic shortest-path laws intended to support the Viète `C6 -> C12` root-refinement observer, which branch sections are compatible with the triadic frame symmetry and which remain faithful as a twelve-phase Cell readout?

## 2. BRC observer and future-operation horizon

Population:

`64 shortest branch words over one full Q_S frame cycle`.

Retained future operations/observations:

1. cyclic transport by `Q_S` around the six macro phase edges;
2. the twelve microtime phase slots of the chosen shortest lift;
3. Cell equality/nonzero tests at those microtime slots;
4. the oriented half-turn quarter-root readout at odd microtime;
5. downstream C24/principal-root readouts that require a defined nonzero C12 root state.

The reduction is therefore **not** allowed to identify two branch laws if one collapses microphases that the other keeps distinct.

Positive Weighted-BRC is not the relevant layer here; the active tool is the observer/provenance-loss gate on a deterministic finite population.

## 3. Q_S acts transitively on the six macro edges and preserves branch type

The generator sends

`a_r -> a_(r+1)`

and therefore transports macro edge `r` to macro edge `r+1`.

It sends the pivot Cell `0` to itself, so an INNER branch transports to an INNER branch.

It also sends

`a_r+a_(r+1)`

to

`a_(r+1)+a_(r+2)`,

so an OUTER branch transports to an OUTER branch.

Hence on branch words the `Q_S` action is exactly one cyclic shift:

`(beta_0,beta_1,...,beta_5) -> (beta_1,...,beta_5,beta_0)`.

## 4. Theorem: Q-equivariant deterministic shortest sections are exactly two

A deterministic branch section is `Q_S`-equivariant iff its branch word is fixed by one cyclic shift.

Because the six macro edges form one transitive orbit, a shift-fixed binary word must be constant.

Therefore

\[
\boxed{
\mathrm{Fix}(Q_S;\{I,O\}^6)
=\{IIIIII,OOOOOO\}.
}
\]

Thus the symmetry requirement alone produces the exact reduction

\[
\boxed{64\longrightarrow2.}
\]

The two survivors have distinct semantics:

- `I^6`: pivot-returning equivariant shortest law;
- `O^6`: outer-shell equivariant shortest law.

No appeal to standard pi, continuous rotation, FCC planarity, or force balance is used.

## 5. The all-INNER law collapses the C12 microphase observer

Under `I^6`, every odd microtime state is the same pivot Cell `0`.

Over the twelve phase positions before the terminal repeat, the state sequence contains:

- the six distinct signed unit macro phases;
- the pivot Cell `0` repeated six times.

Hence the number of distinct microphase Cells is exactly

\[
\boxed{7}.
\]

Moreover the six would-be intermediate root slots all hit the zero Cell.

At the half-turn antipode this is exactly the branch-singular state for the normalized root/bisector construction: it does not provide a nonzero oriented quarter-root Cell.

Therefore `I^6` is a perfectly valid Q-equivariant shortest **path law** for weak endpoint/frame observers, but it is not a faithful twelve-state C12 root-refinement law.

Freeze:

`ALL_INNER_VALID_SHORTEST_ROTATION_PATH_LAW = TRUE`.

`ALL_INNER_FAITHFUL_C12_ROOT_PHASE_LIFT = FALSE`.

## 6. The all-OUTER law is a faithful nonzero C12 microphase cycle

Under `O^6`, the twelve phase positions are

`a_0,m_0,a_1,m_1,...,a_5,m_5`,

with

`m_r=a_r+a_(r+1)`.

The universal triadic theorem proves these twelve Cells are pairwise distinct.

Every state is nonzero:

- each `a_r` is a signed unit Cell;
- each `m_r` has two nonzero components.

Thus

\[
\boxed{
|\{\text{12 microphase Cells under }O^6\}|=12
}
\]

and every odd slot carries a defined nonzero balanced root state.

This is precisely the universal native C12 phase cycle used by the all-20 Viète root/C24 bridge.

## 7. Main selection theorem: 64 -> 2 -> 1

Combine the previous two sections.

Among all 64 shortest branch words:

1. `Q_S`-equivariance leaves exactly `I^6` and `O^6`;
2. faithful/noncollapsing twelve-state C12 Cell phase readout rejects `I^6`;
3. nonzero root availability at every fine phase also rejects `I^6`;
4. `O^6` satisfies both requirements.

Therefore

\[
\boxed{
\text{Q_S-EQUIVARIANT DETERMINISTIC SHORTEST LAW}
+
\text{FAITHFUL NONZERO C12 ROOT-PHASE LIFT}
\Longrightarrow
\beta=OOOOOO.
}
\]

Equivalently,

\[
\boxed{64\longrightarrow2\longrightarrow1.}
\]

The final survivor is the all-OUTER root-refining law.

This holds identically for all

\[
\binom63=20
\]

selected native triads.

## 8. Exact scope of uniqueness

This is **not** a theorem that all native rotation dynamics must use OUTER.

It proves uniqueness only in the declared class:

- deterministic;
- shortest two-step realization on every Q_S macro edge;
- Q_S-equivariant;
- intended to expose a faithful nonzero C12 Cell phase/root observer.

If the future observer asks only for macro endpoints/frame transformations, `I^6` remains admissible and the distinction may be erased under that weaker lease.

Longer paths, mixed non-shortest paths, stochastic branch laws, signed/amplitude laws, and general elements of `ROT_PATH_X6` remain outside the uniqueness theorem.

Freeze:

`OUTER_UNIQUENESS = ROOT_REFINING_OBSERVER_RELATIVE`.

`OUTER_UNIQUENESS != UNIQUE_ALL_NATIVE_ROTATION_DYNAMICS`.

## 9. Why P000 triadic force balance is not used as a branch selector

A tempting slogan is that the OUTER midpoint `m=a+b` appears in the ordinary coordinate identity

`a+b-m=0`,

whereas INNER passes through zero.

Current P000 does **not** license turning this identity into `TRIADIC_CLOSURE_E`.

The Foundation explicitly types `TRIADIC_CLOSURE_E` as a predicate on primitive force/作用 events and forbids silently replacing it by a classical or ordinary coordinate-vector sum condition.

Therefore this research does not claim

`a+b-m=0 -> PRIMITIVE_STABLE_BALANCE`.

A later force/rotation bridge could derive such a relation only by explicitly constructing the force-event typing and proving the transfer.

Freeze:

`COORDINATE_THREE_TERM_IDENTITY != TRIADIC_CLOSURE_E_WITHOUT_BRIDGE_THEOREM`.

This negative typing result prevents a false Foundation promotion while preserving the force-coupling question as a future target.

## 10. Relation to the rotation-path groupoid

The selected `O^6` law gives one distinguished shortest path over each local Q_S cycle, but the full `ROT_PATH_X6` composition problem remains.

In particular, a shortest OUTER lift of a nontrivial rotation followed by a shortest OUTER lift of its inverse generally produces a nonempty loop, while the shortest identity lift is empty.

Thus the selected shortest OUTER section is not closed under arbitrary rotation composition merely because it is locally unique for the root observer.

Consequently

\[
\boxed{
\text{LOCAL ROOT-LAW SELECTION CLOSED}
\quad\text{but}\quad
\text{GLOBAL COMPOSITION-SAFE PATH QUOTIENT STILL OPEN}.
}
\]

The next problem is to find the smallest path-history signature that:

- composes exactly;
- distinguishes root-relevant INNER/OUTER order when necessary;
- distinguishes nontrivial rotation loops from the empty identity when required by the observer;
- is strictly smaller than the full primitive step word if possible.

## 11. Current #1255 consequence

After the same-day all-20 triadic rotation rebase, the root branch is now sharper than the original issue formulation.

For every oriented selected triad:

```text
Q_S frame macrocycle
  -> 64 shortest branch words
  -> Q_S covariance: {I^6,O^6}
  -> faithful nonzero C12 root observer: O^6 only
  -> actual balanced C12 root Cell
  -> C24 balanced spinor
  -> principal +/-3 precision lineage.
```

The remaining unresolved unit is no longer existence or local branch selection of the principal root path.  It is **composition-safe native rotation history and time coupling**.
