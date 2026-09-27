# Structural shortcuts for the aligned two-bit scalar observer

The declared unique native run and complete author/peer saved-evidence readbacks
are PASS. The result is a bounded scalar-observer improvement, under shared
author context; it is not formal independent admission or full Shor closure.

The target is the exact signed pair count on length L=2^g with signs
w(x)=(-1)^(bit_ell(x)+bit_k(x)), where 0<=ell<k<g. The new version retains the
predecessor's admission 2^ell | R and supplied canonical residue 0<=r<R. Raw
normalization remains 4^-g. It supplies scalar coefficients, not an order
oracle, chronological matrix compression or a complete Shor sampler.

`shortcut_two_bit.py` defines `ShortcutTwoBitObserver.two_negative`. Its
structural routing first validates alignment by typed division, then tests
whether R divides 2^k, which certifies zero through signed residue cancellation.
Otherwise it retains both displacement orientations, omits a shifted sum only
after an observed zero coefficient, and uses an affine progression when k=g-1.
Other required progressions use the frozen direct floor-moment helper. These
choices use public indices and actual typed observations, not saved answers.
All new routing, positive replays and paid rejected replays must be charged.

The bounded checker matched all 36 scalar answers from the predecessor's six
tuples. It read the complete aligned payload and its 720-pair comparator
evidence rather than repeating that experiment. Production required 37,503
adder digit replays, compared with the predecessor's 77,763. Four fixtures used
fewer digits than their historical typed pair comparators, but the production
total remains above that comparator's 35,531. This is an operation-count
improvement over the old observer, not a matched wall-time speedup.

| g, ell, k, R | New production digits | Old observer | Historical pair comparator |
|---|---:|---:|---:|
| 2, 0, 1, 1 | 16 | 4,664 | 387 |
| 3, 0, 1, 3 | 11,894 | 16,088 | 2,268 |
| 3, 1, 2, 2 | 78 | 6,800 | 2,186 |
| 3, 1, 2, 4 | 204 | 7,273 | 2,530 |
| 4, 1, 3, 6 | 8,065 | 18,074 | 12,547 |
| 4, 2, 3, 20 | 17,246 | 24,864 | 15,613 |

The 36 requests took seven cancellation, 26 affine and three moment-fallback
routes. Actual work includes 158 requested private progressions (146 affine,
12 moment), 38 omitted shifted progressions and 24 top-level moment tables.
Positive replay cost 37,503 digits, paid input rejection 43, and rejected
certificate replays 111,661: total current work is 186,710 digits. The one
global native core-column execution is counted once; reuse of those columns
does not erase typed digit work. The 28.76671770005487-second run interval
ends before final serialization and is not a matched timing comparison.

All six positive replays, 12 input rejections, two incomplete-observer reuse
rejections and 16 tamper controls passed. Four tamper rejections were early;
eleven completed fresh replays and one partial replay retained paid evidence.
The even-step propagation branch after failed cancellation was not re-exercised
by this grid; the corresponding fixture cancels first in this dispatcher.

Read `DESIGN.md` for the predeclared inputs, failure retention, schema and
negative controls. Its historical CODE_ONLY header records the pre-run design,
not the later actual execution state. `STRUCTURAL_SHORTCUTS.md` and its
source-specific symbolic review remain byte-frozen. `EXECUTION_NOTE.md`,
`SHORTCUT_COST_READBACK.json` and `guard_review/SHORTCUT_RESULT_REVIEW.md` record
the full raw-payload, signed/typed operation-link and native-cell checks for
all 26 charged streams. These readbacks do not repeat scientific execution.

`next_design/TOP_BIT_GENERAL_MODULUS.md` and its review are unchanged symbolic
copies. They derive at most eight degree-three floor tables for k=g-1 and
arbitrary positive supplied R, without requiring 2^ell | R. That extension
is not implemented or admitted by the current shortcut API. Its complexity
statement uses explicit scale length O(g+log(R+1)), not log(g).

`DEPENDENCIES.md` gives source-first restoration; `PRIOR_EVIDENCE_REUSE.md`
separates historical evidence from new work; `CONTINUE.md` gives the next
concrete steps. Local layout names locate immutable dependencies and do not
restrict which dialogue may continue mathematical research.

Intake: predecessor source 20b5ef9e9146039863963bc039d2a163ac99f4a5, delivery
b3a2b3bcc946cace7c83e48603f8bc1b6edd95aa. Actual startup observed own checkpoint
452ffb73180f459d4c08302aad754ac512dc1bab; the coordinator refreshed canonical
GK to 604893ec0fb958d9d86f923511255e3fbb473dc0 with unchanged policy blobs.
Final source and delivery identities belong in actual closeout receipts.

Global-Knowledge-Sync: main@604893e / GLOBAL_KNOWLEDGE_V1
