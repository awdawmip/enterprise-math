# Correlated conic transport: shared-context review

Status: PASS_WITH_EXPLICIT_SCOPE; shared-context mathematical/source review and saved-record I/O, not independent admission. No scientific module was imported, no typed arithmetic was replayed, and the old experiment was not rerun.

## Pins and read scope

Read the complete new `conic_transport.py`, its frozen plan, the complete inherited `native_relative_port.py`, the relevant `LazyModularColumns` setup/inverse implementation, and the new summary. Decoded the entire new raw JSON using only standard-library gzip/JSON/hash I/O. Checked all twelve saved layer histogram equalities and all four terminal histogram equalities directly against the old saved folded records; this is a record comparison, not a new modular/gcd reference computation. Checked the source, plan, guard and baseline byte bindings and the stored live-conic validation outputs. Did not claim a fresh per-digit semantic replay of the underlying native arithmetic traces.

| Artifact | SHA-256 |
|---|---|
| New source | `420ab2e9502fd45fd2dab85da09a69a129f8a63e95fee17eb9d895d6a9c18d65` |
| Frozen plan | `b8ce9ebb39124c4a2eba25ad24ad4b998bff9601aa4c79affb617e62483622e5` |
| Summary | `f1132acda6ad5eecc59c834e97d513ade2d33d3840da7bd110315641b4374424` |
| Decoded raw, 808809 bytes | `2ab5d7853310c2a1b9240c51f629b3374ee938f8a4eb75ef0d88a2711c253c75` |
| Gzip original | `fc18630a78ffbec5d89d59ac84d8ab21f884f028631e3ac0d4a4c1522c9e8b4e` |
| Saved baseline decoded raw | `6a111ca626f3330d16d513a15bfc31923a8c990723108e99c65b61fa5d229d28` |

## Mathematics and implementation

No blocking defect found in the finite comparison. The invariant `uv=1 mod N` is initialized at `(1,1)` and preserved by both correlated multiplier actions. Swapping the coordinates conjugates the equally weighted positive/negative actions and preserves the actual divisor `gcd(u-1,N)`. Therefore canonical exchange folding preserves the declared LIVE/factor/first-hit-depth histogram for the prescribed symmetric schedule. This proof is valid for general N with unit inputs; it does not assume primality or a known order.

The source retains two microscopic identity branches through `DOUBLE`, performs the proper-factor observation before folding, absorbs a factor with `ONE`, and retains first-hit depth. Each production multiplication, comparison and gcd uses inherited typed interfaces. Full residue pairs remain correlated, and separate paid invariant checks are saved. All four cases have empty standalone `inverses` and `folds` maps and zero `inverse_requests`; the runtime does not recompute a state inverse to choose a canonical representative.

The source does not call the generic T6/T7 finite enumerators or the spatial Cell codec. Its T6/T7 use is the explicit observer-relative symmetry theorem, not execution of those generic APIs. The conic is a derived internal arithmetic carrier. It is not an assertion that modular reduction is a lossless native Cell rechart, that a residue return is a spatial return, or that this positive instrument is a signed Shor simulator.

## Cost and unfavorable comparisons

The table below repeats the saved typed digit-replay ledger, including table setups; it does not estimate timings or total machine costs.

| N,a | New production | Old inversion-folded | Old one-coordinate relative | New schedule | New invariant validation |
|---|---:|---:|---:|---:|---:|
| 15,2 | 1552 | 1960 | 1504 | 92 | 210 |
| 21,2 | 2653 | 3162 | 2633 | 106 | 276 |
| 35,2 | 6458 | 8384 | 6706 | 122 | 689 |
| 15,14 | 828 | 1122 | 720 | 122 | 366 |

All twelve layer comparisons pass. All four production counts improve over the saved inversion-folded route, but only N=35,a=2 improves over the saved relative route. Extra coordinate transport can outweigh the removed state inverses. The negative conic check costs 34 digits. The single saved native catalog call is a reused primitive catalog, not the whole arithmetic workload. Histogram/library allocation costs and auxiliary projection merges are outside the reported digit metric, as the summary states.

In particular, `production.table(c).inverse_multiplier` reuses that table's certificate, while `production.mul(ci,...)` may construct a distinct inverse-multiplier table whose constructor pays another inverse certificate. “No standalone per-state inverse” is demonstrated; “exactly one Euclidean inverse computation per layer” is not. The saved setup counts include this work.

## Completion and failure boundaries

The paid `(2,2)` modulo 15 negative verifies a nonconic product and records `rejected=true`. It is a finite guard demonstration, not a reusable `PairCertificate` importer or serialized-tamper suite. The runner starts from its own certified `(1,1)` state, so it never accepts an arbitrary unverified external live pair in the successful experiment.

The exclusive STARTED record prevents silently repeating the run in the same output directory. On an unexpected exception the outer handler saves a traceback. It does **not** capture the local partially built `Route` objects from `execute`; thus the frozen plan's phrase “preserves FAILED evidence” must be read as STARTED plus traceback, not a complete interrupted-science checkpoint. This is a limitation of failure recovery, not a missing receipt in the successful raw artifact reviewed here. No change to frozen source or rerun is requested by this review.

The general interface/coordinate audit is `../GEOMETRY_CONIC_INTERFACE.md`. No universal factoring advantage, support-size bound, geometric primitive-path implementation, or formal admission follows from these four finite cases.

Global-Knowledge-Sync: main@7a63984 / GLOBAL_KNOWLEDGE_V1.
