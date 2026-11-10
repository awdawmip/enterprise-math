# Reproduce the cost-aware vacancy evidence results

Use Python 3.12 and its standard library. Run from this extracted package root;
the original BRC runtime dependencies are included at their required relative
paths. No earlier archive needs to be overlaid.

## Focused original-kernel checks

```bash
python optimization/check_cost_aware_kernel.py minimax --output replay_minimax.json
python optimization/check_cost_aware_kernel.py family --output replay_family.json
python optimization/check_cost_aware_kernel.py future_plan --output replay_future_plan.json
```

`minimax` executes all 96 stated initial residue preparations in the original
kernel plus one actually acquired high-half continuation, for 97 runs. It
compares each physical cost with the knowledge-state planner and checks the
complete original model at every business boundary. This mode was run once in
a fresh isolated directory; its JSON exactly matched `optimization/kernel_minimax.json`.
`CLEAN_REPLAY.json` records that completed check.

`family` executes the seven stated strategies for six and fourteen slots and
four horizons, including the high-bit probe both before and after the required
conflict check. `future_plan` executes the two-target case where the known next
target changes the useful first safe key.

The additional original-kernel modes are `word_lengths`, `regressions`,
`protected`, and `omissions`. The saved results retain their declared scopes;
repeating every earlier verification is not required to run a focused example.

## Exact slot-symmetry planning

```bash
python optimization/symmetry_checks.py --output replay_symmetry.json
```

This solves the same observation-only Bellman model using histograms of
interchangeable observed patterns. Slot zero remains distinguished before the
last round, because every round binds that physical slot. A histogram query
still reads exactly one physical slot through the existing kernel adapter.

The check compares all 1,280 nonterminal labelled states in the four inherited
small domains, replays 116 compatible static input tables including the observed
high-bit seed, and solves the exact one-round target-zero values for four, five,
and six slots. Their variable costs are 60, 70, and 86. One attaining static
witness for each case is executed by the original kernel, giving complete costs
130, 142, and 158. The six-slot result is an exact quotient solution; the package
does not claim an original-kernel enumeration of all 262,144 six-slot tables.

The final-round lower-bound cuts are compared with the unpruned recurrence on
every visited four-slot state. `optimization/symmetry_results.json` records the
state counts, complete worst-witness paths, original-kernel boundaries, and the
explicit counterexample to merging slot zero before the final round. Timings
and the generation timestamp are expected to vary across reruns.

## Read the evidence

- `optimization/kernel_notes.md`: physical execution path, original word
  lengths, cost formulas, fallback behavior and executed finite domains.
- `optimization/kernel_summary.json`: seven completed original-kernel result
  files and their scopes.
- `optimization/strategy_proofs.md`: mathematical cost and information arguments.
- `optimization/selector_proofs.md`: weighted fixed-mask selection and slot updates.
- `optimization/bellman_planner.py`: finite-horizon knowledge-state recurrence.
- `optimization/symmetry_planner.py`: exact slot-symmetry quotient and physical
  slot compilation; `optimization/symmetry_checks.py` runs its stated checks.
- `optimization/selector_results.json` and `optimization/strategy_checks.json`:
  separately labeled control-model and compiler-length checks.

Control-only reruns use the corresponding `selector_checks.py`,
`strategy_checks.py`, and any included `planner_checks.py` entry points.

`RUNTIME_DEPENDENCIES.json` lists the 51 unchanged files copied from the prior
standalone runtime closure and the new optimization files present at staging.
The scientific parent is Enterprise Math commit
`9bb764203fcb2f1ec6ec5c82b76219f951c033f4`; its unchanged dependency lineage
is retained in that file. Earlier ZIPs and unrelated historical result archives
are not embedded here.

The main family uses a sparse weighted region, with its selection and update
work counted separately. General mixed-mask fallback includes the explicitly
counted candidate-reference search described in the kernel notes. The reported
mathematical status is author arguments and the specifically declared executions.
