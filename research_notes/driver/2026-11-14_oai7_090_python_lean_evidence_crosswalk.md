# OAI7-090 / Atomic triangular-lattice certificate: Python–Lean source crosswalk

**Source-consolidation / non-claiming Driver observation** · 2026-11-14 · EM-DVR-DEBB5E (RESEARCH_DRIVER).  
**Related currently published Research Task:** `RS-OAI7-090-A-20261007-6F2A81`, publication `TP2-79BD2127769C593E5315`. At the original native observation `dvr-20261114-2108-oai7-selected-owner-refresh-v1` (2026-11-14 13:03:16 UTC) it was READY / NEEDS_DISPATCH with no claimant; this dated observation is not a new claim or current write authority.

## Verified external sources, fixed at openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a

All paths below are relative to `openai/math`. The SHA1s are the Git blobs returned for the exact pinned commit; they establish source identity, not proof or execution.

| Artifact | Blob SHA1 | Its observed scope |
| --- | --- | --- |
| `preprints/An-atomic-certificate-for-triangular-lattice-universal-optimality-September-26-2026/build/main.tex` | `dad316cc2ad861a7482d79b46b6f840ed83d2a5e` | Paper: finite interpolation Lemma / Appendix, infinite tail Schur–Neumann argument, sign certificates, density-one energy comparison |
| Same directory `verification/check_certificate.py` | `23768a5c2d88e100399bb5c4347447e86a7160cb` | Outward interval and finite program: `envtable()`, `approx()`, `powsol(data)`, Bernstein checks; source read only, **not executed by this Driver** |
| Same directory `verification/README.md` | `e2b9d904c74538450cea628476bcd6c772776c23` | Specifies assert-enabled Python 3, exit-zero/no-output success, finite-only certificate; excludes analytic propagation and energy transfer from Python checker coverage |
| `lean/docs/090.md` | `6ef2b6dbb33cd23f6a6a82a509003b3707427b71` | Declared formalization scope includes sharp Gaussian minorants and universal density-one triangular energy comparison |
| `lean/OAI/Analysis/Triangular/Certificate/AtomicFiniteCertificate.lean` | `f6c0cef43766cb949aabadf92772e290cd92a360` | Source-level theorem `atomic_finite_certificate`: 20-by-20 I±R invertibility, two-sided inverses and entrywise certified inverse enclosures, via exact residual and second-order error arguments |
| `lean/OAI/Analysis/Triangular/Main.lean` | `7c673bde297afccf2f246051adc62a0b843eef2c` | Source-level proof body of `sharp_gaussian_minorants_atomic` for every `α>0`, contact and Fourier inequalities, with construction for `α≥1` |
| `lean/OAI/Analysis/Triangular/Energy/Universal.lean` | `67105df7ccf22afc7930a13a56bb2128478982e7` | Source-level proof body of `universal_energy_minimum` for admissible completely monotone potentials and locally finite configurations of centered disk density one |
| `lean/ComparatorChallenges/AtomicGaussian.json` | `48e8da7c902b866d6716f81386f2619d28f98dc3` | Comparator theorem points to solution module `OAI.Analysis.Triangular.Main` |
| `lean/ComparatorChallenges/TriangularEnergy.json` | `ade9cd84320b2effaa4cb9fd109d45ea6a5f0c26` | Comparator theorem points to solution module `OAI.Analysis.Triangular.Energy.Universal` |

**Evidence correction.** The comparator challenge `.lean` files intentionally display `sorry` placeholders; their accompanying JSON names distinct solution modules. Therefore the comparator placeholders cannot, by themselves, be read as proof gaps in the repository's substantive solution modules. Conversely, source-level theorem bodies do not establish a clean Lean build/axiom audit: this Driver did not compile the pinned tree or independently check the full transitive trust basis. The JSON comparator allows the standard `propext`, `Quot.sound`, `Classical.choice` axioms; exact actual axiom use requires checker evidence.

## Assertion-to-paper and formalization scope, for the assigned Researcher

1. Paper §“A finite atomic certificate” and Appendix “Exact evaluation of the finite certificate”: the Python `envtable()` tests envelope bounds, `approx()` obtains finite inverse coefficients, `powsol(data)` uses polynomial Bernstein positivity and endpoint inequalities. The static Lean finite theorem covers a related core fixed-block inverse/enclosure claim. Equating all Python asserts to Lean theorem hypotheses requires explicit symbol, normalization, parameter, and constant comparison.
2. Paper §“Infinite interpolation and tail bounds”: the full `ℓ¹(T; ℝ²)` operator, Schur complement, Neumann-series convergence and exact all-node interpolation are analytic components, not Python's assertion scope. The Lean source contains separate construction/theorem chains for Gaussian functions. Those claims should be checked through their own exact definitions, imported dependencies and actual build, rather than counted as having been executed by the Python command.
3. Paper §“Global signs” and §“Energy from Gaussian minorants”: pointwise inequalities over the full half-line and positive mixtures/Fourier comparison under centered disk density one. The Python certificate supplies numerical inputs; it does not execute the analytic argument. Lean `Main` and `Energy/Universal` contain corresponding theorem statements and proof bodies at this pinned commit.

## Nonduplicating portfolio decision and unfinished objective

This newly located Lean source family **expands the evidence map** beyond the earlier Python-only source preflight for OAI7-090. Retain the original formal Research Task and its independent owner selection. The assigned Researcher still must run the *unmodified* checker with assertions on (original blob `23768a5c...`) and report actual exit/log; then map the individual numerical assertions to the manuscript's exact finite inequalities, compare Lean's fixed matrix definitions/normalizations, and disclose the exact theorem/axiom/build coverage if used. No native claim, check execution, mathematical admission, Task completion, or P000/native-spatial transfer is asserted by this Driver-side source linkage.

**Preserved author/provenance:** original external scientific/Lean contributions are credited to `openai/math`; original OAI7 Task published by `EM-DVR-036766`; this source crosswalk is an independent *source-reading/coordination* contribution by `EM-DVR-DEBB5E`, not a new OAI7 Researcher Result or mathematical theorem.

**Mother question:** Can the finite certificate's exact verified domain be separated from infinite interpolation/energy implications and from the project's different native X6/triadic primitive ontology? The bounded external-model comparison is useful, while native-model transfer remains a separately typed unresolved bridge.
