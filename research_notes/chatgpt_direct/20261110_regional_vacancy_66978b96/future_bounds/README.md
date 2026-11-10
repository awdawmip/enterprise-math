# Empty-prefix evidence: control comparisons

Date: 2026-11-10. This directory contains exact integer control experiments and
their finite receipts. The maintained `PrefixTree` is imported from the preceding
production implementation. Request values are accessed by the test feedback
oracle and verification assertions; the controller consumes next-bit feedback.
Physical BRC command counts are supplied by the separate kernel experiment.

These residues and prefix trees describe typed request observations within the
existing X6 model. They introduce no spatial coordinates or native plane.

## Reproduction

With this directory beside `directed/`, `incremental/`, and the unchanged parent
dependencies, run:

```bash
python future_bounds/check_prefix_controls.py
python future_bounds/check_future_controls.py
python future_bounds/check_region_gain.py
```

The first command replays the short gain/tradeoff examples and four instances of
the general separation family. Its receipt is `prefix_controls_replay.json`.
The optional `--exhaustive` performs the already completed 1,098,900-case mixed
preparation enumeration. That completed enumeration is recorded separately in
`prefix_controls_checks.json`; it need not be repeated to use the general proof.

The second command reproduces the two minimal future-intersection examples and
the finite ABA repetition comparison in `future_controls_checks.json`.

## Files and completed coverage

- `control_results.md`: general separation proof, repetition lemma, and exact
  finite examples with interpretation.
- `check_prefix_controls.py`: single-point versus single-empty-prefix control.
- `prefix_controls_checks.json`: all `r=2,...,6`, every length-`r` residue
  multiset, and every triple of attainable target phases; operations are
  reserve/bind-slot-0/reserve/bind-slot-1/reserve. Exactly 1,098,900 preparations.
- `prefix_controls_replay.json`: focused short examples and separation family.
- `prefix_stable_family_checks.json`: four scale instances, `r=6,30,126,510`.
- `prefix_mixed_random_checks.json`: the 63 preparations of one reproducible
  exploration seed that yielded both directions. This is discovery evidence;
  the simplified cases are replayed directly by the first command above.
- `prefix_mixed_regressions.json`: exact simplified mixed cases with every choice.
- `check_future_controls.py`: arbitrary finite candidate-set search, including
  possible failure, plus point-retention comparisons.
- `future_controls_checks.json`: 13 preparations needed to exhibit both signs
  of the common-intersection read difference, 124,200 complete ABA comparisons,
  and the selected six-slot examples.
- `check_region_gain.py` / `region_gain_checks.json`: the two-cluster family
  comparing point, monotone prefix shrinking, and live regional recycling;
  includes replay of the existing mixed tradeoff cases with RegionEvidence.

The complete RegionEvidence slot-state/transition verifier is stored separately
as `regional/check_region_control.py`, with `regional/region_control_checks.json`.
It tests 1,390 states, 31,960 controlled transitions, 11,966 valid empty-prefix
reacquisitions, and 428,864 selector queries. Width 3 with two slots is an
additional data-structure domain beyond the model's minimal width; each row
states its actual parameters.

The candidate-set checker explicitly constructs a candidate trie. Its build
touches are recorded, not treated as zero cost. The asymptotic separation in
`control_results.md` concerns the inherited production controller's constant-time
capacity formula, whose equivalent search paths the checker verifies.

Argument status: author derivation plus exact finite control execution in shared
research context. The general claims use the written proof. No formal-checker or
independent-review admission is asserted by these receipts.
