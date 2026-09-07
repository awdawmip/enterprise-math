# Nonlinear channel quotient: frozen local validation

Date: 2026-09-07. Status: `FINITE_WITNESSES_VERIFIED`; universal mathematics is
the separate pure-algebra proof, not a conclusion inferred from this test label.
Internal `ANCHOR_EXPOSED` helper; no official V2 review or allocated identity.

Worktree: `D:/em/owner-20260907`.
Runtime: Python 3.12.14 from
`C:/Users/Administrator/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe`.
Only standard-library exact integer/Fraction arithmetic and existing local
geometry/BRC/T6 code are used. No external package installation, solver, float,
remote mutation, commit, or production-source edit occurred.

## Executed tests

```text
python -B -X utf8 -m unittest discover -s experiments/owner_nonlinear_channel_20260907 -p test_channel_quotient.py -v

test_actual_t6_finite_closed_domain_nonlinear_observer ... ok
test_all_small_cone_pairs ... ok
test_brc_histograms_remain_distinct_after_common_gate ... ok
test_changed_endpoint_and_malformed_certificate ... ok
test_equal_and_zero_mass ... ok
test_five_step_boundary_witness ... ok
test_gate_formula_and_idempotence_on_rationals ... ok
test_strict_positive_rationals_and_coordinate_bounds ... ok
test_tampered_steps_and_deleted_suffix ... ok
test_witness_is_frozen_from_mutable_inputs ... ok
test_wrong_mass_and_invalid_inputs ... ok

Ran 11 tests in 1.710s
OK
```

The small-cone test exhausts 2978 ordered equal-total pairs: coordinates in
{0,1,2}, total at most 3. It does not purport to sample every rational vector or
an arbitrary observation q. Strict-positive rational witnesses remain inside
their endpoint coordinate intervals. Forged amounts/gates, omitted/reordered
steps, changed endpoints, malformed certificates, booleans, floats and numeric
subclasses are rejected. Construction freezes mutable input lists into tuples.

`run_certificate.py` was executed separately, exit 0, with empty stderr. Its
actual JSON output is preserved as `certificate.json`, with exact source hashes.
The run executes all six original matrix idempotence checks and records the
five-step boundary witness and each common matrix image, six actual T6 finite
closed-domain checks, and the BRC histogram boundary `5[1/5] != 10[1/10]`
despite equal output masses.

No arbitrary q is supplied to or accepted by the finite witness verifier. Its
VALID result binds only the two supplied endpoints and the exact gate chain.
The injective-descendant hypothesis and resulting arbitrary-set factorization
are handled by the proof. No external certificate status can replace these
checks or enlarge the carrier to microbranch histories.

## Frozen SHA256

Paths below are relative to the worktree.

| Artifact | SHA256 |
|---|---|
| `research_notes/OWNER_NONLINEAR_CHANNEL_QUOTIENT_20260907.md` | `edcc5694bd2a85cebc0836110d03142ad3637cd953e96b2c98c08fbbe8e77ffc` |
| `research_notes/OWNER_GEOMETRY_FRONTIER_20260907.md` | `9c7d54b65cc65c3723076186675cb3ec3f744709da2b73c1d82c5d1105bd450e` |
| `research_notes/OWNER_GEOMETRY_INDEPENDENT_AUDIT_20260907.md` | `baca119a64e0f0c8c37c50db5a1d57e9a1a6b56af8628920e322657bf95bfa98` |
| `channel_quotient.py` | `c90d67e9d56bc14e2d2adea36b8f69ba2e1afc21c794c22aee73e69de34bd844` |
| `test_channel_quotient.py` | `a4afeb65ed303b6ed6788102b0117818453729f1822a05a96705268347443d28` |
| `run_certificate.py` | `a518fc682110e02bfbc0fd052599b2fc0f59d1cd91d9555655eca0caf55a9b6b` |
| `certificate.json` | `0932188c88af0739d77ff0d4121438e1fc75dc5526c2e860cffc52029208afbb` |
| `tool_coverage.json` | `9c098ba9ff5f05cc869d3463d092f7fdf36fa003e57c7d48b5d1059b75fca96f` |
| `README.md` | `24c807b39ef85d2dd9293dd6b519af758473edb652770d1718a307468cb9b10f` |

The last six paths refer to this experiment directory. Reused geometry and
production-module SHA256 values are also embedded in `certificate.json`;
the geometry consumer is checked before import against
`d92a45acb9c455b88a3786ce99ae919cbfbd5a0b09b55ce3dfeb6b39b633c4a7`.
This validation file is excluded from its own hash table.

Global-Knowledge-Sync: main@4fa7d7d / GLOBAL_KNOWLEDGE_V1
