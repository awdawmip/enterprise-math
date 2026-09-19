# Heartbeat World BRC residue-port toolkit extraction

Status: `RESEARCH_RESULT_EXTRACT / EXECUTABLE_CANDIDATE / NOT_FOUNDATION`
Date: `2026-09-20`
World: `HEARTBEAT_WORLD` = native X6 discrete space + separately typed time.

This checkpoint extracts three reusable T0 BRC subtools from the Heartbeat World experiments without changing P000 or production Nollm: residue/time-ported affine branch transport, exact observer-scoped residue quotients, and finite-horizon native-X6 contact observation.

The residue carrier keeps a finite congruence fiber as a typed port. For an integer affine map `x -> A x + b`, a declared source fiber `D Z^6 + r` maps to target `D Z^6 + s` exactly when `D^-1 A D` is integral and `A r + b = s (mod D)`. Positive BRC branches then compose only across matching residue and time ports.

For degree-two boundary observations, each retained fiber carries the homogeneous moment matrix. Exact propagation is `M'_s = sum c_e w_e H_e M_r H_e^T`. A quotient may merge source fibers only when their exact effect or moment operators into every retained target class agree for every declared future packet. The certificate is therefore observer- and future-operation-scoped.

The mod-4 misaligned macrocycle supplies the key safety witness: the whole cycle merges `{0,3}` and `{1,2}`, but a within-cycle primitive block swap distinguishes the members and invalidates that two-class quotient. In the separable six-axis macrocycle, 4^6 = 4096 residue ports collapse to 2^6 = 64 exact effect classes only at the declared macro boundary.

A separate contact adapter studies two tagged native-X6 positions through relative displacement. With all twelve signed primitive unit moves and remaining horizon `h`, the coarsest exact future-contact quotient keeps every `d` with `||d||_1 <= h` and merges all farther states into `FAR`. The exact class count is `2 + sum_{s=1..min(6,h)} 2^s C(6,s) C(h,s)`. `FAR` is not zero and cannot recover an exact far position; increasing the horizon requires re-encoding from richer state.

Local validation before publication: the full extracted bundle suite passed 12/12, the native toolbox-index excerpt found 3 methods, 8 theorem candidates and 16 public API exports, and a compact publication regression suite passed 5/5. Existing `brc_transport.py`, `brc_histogram.py` and `predictive_quotient.py` stayed on their pinned blobs. No full repository suite, independent referee, Lean proof, Foundation admission, Nollm production modification or semantic-memory benchmark is claimed.

Machine theorem ledger: `research_notes/heartbeat_brc_library_20260920_AD0416/THEOREM_LEDGER.json`.
Tool docs: `docs/toolbox/BRC_HEARTBEAT_RESIDUE_TOOLKIT.md`.
