# Empty-prefix evidence and live regional recycling

This delivery contains the complete research report, proofs, new controllers,
finite verification results, and the unchanged Python runtime dependency closure.
Extract `region_vacancy_evidence.zip`; no earlier ZIP needs to be overlaid.

## Read first

- `RESULT.md`: complete Chinese research report and measured cost comparisons.
- `future_geometry.md`: the nine stated theorems and complete author arguments.
- `future_bounds/control_results.md`: observation/control separations and exact
  constructive families, including successful and adverse comparisons.
- `future/horizon_costs.md`: original-command cost crossover for the declared
  two-cluster preparation and fixed target sequence.
- `future/summary.json`: completed original-kernel results and execution scope.
- `PROVENANCE.json`: exact source lineage and the delivery's mathematical status.

## Reproduce a focused physical run

Python 3.12 and its standard library suffice. Run from the extracted root:

```bash
python future/check_region_certificate.py regional_gain --output replay_gain.json
python future/check_region_certificate.py regressions --output replay_regressions.json
python future/check_region_certificate.py protected --output replay_protected.json
python future/check_horizon_costs.py --output replay_horizon.json
```

The first command executes the original BRC words for the four declared size and
horizon combinations, using all three controllers. The second exercises aliases,
last-reference restoration, empty and nonempty zero-residue keys, source execution,
new-region acquisition, and physical Boolean output. The third exercises both
actual gate phases and the declared complete-contender boundary schedule.
The fourth checks the exact cost crossover at every cumulative prefix through
18 rounds for six slots and 50 rounds for fourteen slots.

For control-only verification:

```bash
python regional/check_successor.py
python regional/check_region_control.py
python future_geometry_check.py
python future_bounds/check_prefix_controls.py
python future_bounds/check_region_gain.py
```

The already completed broad enumerations retain their exact domains in the result
files; they are not prerequisites for reading or using the proved results.
`future_bounds/check_prefix_controls.py --exhaustive` repeats its 1,098,900-case
finite mixed domain. Original-kernel `audit1`, `audit2`, and `omissions` modes are
listed in the corresponding modules.

## Representation and units

`future/check_prefix_certificate.py` retains a whole proved-empty low-bit class.
`future/check_region_certificate.py` maintains the available part of a certified
class through controlled slot writes and last-reference reclamation, using
`regional/region.py`. Both wrap the inherited `directed.Controller.step`; all real
request reads, source effects, complete identity writes, and physical answer
handling remain there and in its unchanged BRC parents.

Production decisions consume actual Boolean observations and business outputs.
Full request vectors occur only in the declared verification sections or control
feedback oracles. Counters distinguish extra vacancy reads, business identity
reads, original primitive attempts, inherited tree visits, and regional updates.

The new fixed-domain reference counter replaces the initial dictionary counter
with deterministic indexed operations. The same exhaustive regional control
domain, the two-slot 3,800-batch core audit, focused original-kernel regressions,
the gain family and the horizon checks were executed after that change. Other
core results retain their actual execution scope in `future/summary.json`.

## Dependency layout and provenance

The reproduction package includes `directed/check_directed_vacancy.py`,
`incremental/check_incremental_vacancy.py`, all unchanged Python files under
`parent_bundle/`, and the original `SOURCE_PINS.json` used by their loader. Only
runtime dependencies and relevant inherited proof documents are copied; earlier
raw experiment archives remain at their original source locations.

The new project source directory stores this research's new files. Existing
dependency sources remain pinned to the previous direct research delivery:

- Enterprise Math commit `dde96c5e03fad45672656d504cd7f755d3e6a726`,
  `research_notes/chatgpt_direct/20261107_directed_vacancy_66978b96/`.
- Earlier dynamic base commit `fda5f43aca54cc1f3c56b3628ce972c2266589f2`,
  `research_notes/chatgpt_direct/20261107_dynamic_vacancy_66978b96/`.

`MANIFEST.sha256` identifies the delivered files. Its purpose is ordinary archive
integrity. Mathematical status is author derivation with the explicitly scoped
executions, as stated in the report. The decision state belongs to the typed
triadic control model; the native Cell/field/support correspondence remains a
separate unit of the parent research.
