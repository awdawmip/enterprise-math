# Strict finite joint-energy certificate

This directory contains a new finite calculation on the existing rational matched family. The prior certificate files are immutable inputs. No previous suite is rerun, and no old source file is modified.

## Deliverable files

| File | Purpose |
|---|---|
| `JOINT_ENERGY_CERTIFICATE.md` | Definitions, numerical conclusions, limits and interpretation |
| `certify_joint_energy.py` | Rebuild complete roads, q, P256, Q and signed coarse-source inputs |
| `joint_energy_certificate.json` | Strict integer intervals, all coarse nodes/charges, costs and input hashes |
| `check_cutoff_sensitivity.py` | Reuse complete-road arrays to check neighboring H128/H512 cutoffs |
| `cutoff_sensitivity.json` | Strict neighboring-cutoff results |
| `ANCHOR_LEMMA1_CROSS_CHECK.md` | Same-author analytic check of the sibling anchored lemma; not independent review |
| `README.md` | Read-only inputs, reproduction order and cache interface |

## Required read-only dependencies

Keep these paths relative to the package root (the parent of this directory):

| Relative path | SHA-256 |
|---|---|
| `rh_correlation_rational/certify_matched_nodes.py` | `34b09defda6f67c5b70fd64da1f99b868dcc0a0ecab7afc15036a8711ed189d3` |
| `rh_correlation_rational/rational_window_certificate.json` | `d2c00df289bbac268fa54ed77c187edcc741c1fbc4d052069eef389c93f5815f` |
| `rh_correlation_phase/phase_homogenization_checks.json` | `4a456be8b2ae97961d264e05f5ec8d9592beefbb3b8367e66315dcbb72184ef1` |

Only the elementary integer/Fraction interval oracle, linear sieve and rendering helpers are imported from the old Python file. Import does not invoke its `main()` or rerun the old certificate suite.

The rational JSON supplies exact nodes/weights, a rigorous Euler-gamma enclosure, and previous endpoint values for cross-route checks. The phase JSON supplies rigorous P256 boundary values and the old general infinite-tail bound for a clearly labeled comparison. All new energies come from the complete new arrays.

Both scripts require Python 3 and its standard library only.

## Reproduction order

From the package root:

```bash
python rh_joint_certificate/certify_joint_energy.py
python rh_joint_certificate/check_cutoff_sensitivity.py
```

The first script creates the two complete-road readouts and a regenerable `_scratch_arrays.pkl` cache. The second reuses that cache; if absent, it first calls the first script's `main()`. It does not recompute roads when the cache is available.

The main script took about 28.83 seconds here, and cutoff sensitivity about 3.35 seconds. Machine timings are diagnostic, never part of a proof. Inputs, exact arithmetic, formulas and asserted cross-route compatibility determine the certificate.

All intervals use integer endpoints divided by 10**60. The JSON's `integer_bounds` are the full reproducible certificate; decimal `lower` and `upper` fields are outward displays. `width_upper` describes the underlying interval width, so the displayed decimal span may be wider.

## Cache interface for collaborating calculations

The pickle dictionary has integer constants `A=1024`, `B=32768`, `H=256`, `SCALE=10**60` and `DIGITS=60`. Each interval is a `(lower_integer, upper_integer)` tuple.

| Key | Valid indices and meaning |
|---|---|
| `D` | Complete matched-road coefficient, indices 1..B; D1=0 |
| `q` | Full-prefix original readout, indices 0..B; q0=0 |
| `P`, `Q` | P256 and q+P256, valid on A..B only |
| `f` | Original source (kappa-D)/n, indices 1..B |
| `correction_source` | Sum of small-divisor c(d)rho_d(n)/n, indices 1..B |
| `corrected_source` | f+correction_source, indices 1..B |
| `c` | Möbius-inverted complete coefficient, indices 1..H |
| `kappa` | Complete elementary background, indices 1..B |
| `nodes`, `weights` | Exact Fraction objects for the fixed rational family |

The main JSON includes three partitions, beta=1/2, 3/4, 4/5, with nodes, node values, signed coarse charges and norm budgets for both q and Q. These ports are sufficient for subsequent coarse-only work; using them does not require loading the full cache.

## Packaging and scope

Deliver the seven files listed above with the three required read-only inputs. Exclude `_scratch_arrays.pkl` (about 14.4 MB), `__pycache__`, and run logs. The cache is an intermediate shared computation, not a new independent input or a necessary part of the portable package.

These are author-side strict finite certificates, not a proof of RH, an all-scale correlation bound, or an independent project review. Algebra establishes the source/Green/square identities; interval-overlap checks are implementation compatibility checks and are not claimed as independent mathematical proofs of those identities.
