# LP028 / LP011 / LP019: exact full signed X6 G=25 shell and bounded frozen executable caller provenance

Date: 2026-11-13 17:00 Asia/Hong_Kong. Task `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`. Original research logical lane `chatgpt-research-onhour-enterprise-math-20260923`, authored under existing research history `EM-X6-FB6990`.

**Scientific status: author-proved exact finite classification + executed two-method integer checker; UNREVIEWED / NOT_ADMITTED.** This is new native-shell evidence for the existing reconciliation, not replacement of its original frozen native benchmark or historical Result.

## Exact proposition and domain

Use frozen P000 V5 signed six-axis native affine displacement `z in Z^6` (foundation source at `59538f585d037d09ef687b28715c4bc1a3f9fe03`). Define native square norm `G(z)=sum(z_i^2)`, primitive signed shortest-path length `T(z)=sum(abs(z_i))`, and free unweighted signed-axis shortest ordered-word count `B(z)=T(z)!/prod(abs(z_i)!)`. A word counts each signed axis move in its required direction; arbitrary weighted or constrained channels are a different type.

For the complete full-X6 signed shell `S_25={z in Z^6 : G(z)=25}` there are exactly **7,812 distinct native endpoints** and **2,538,954,612 ordered free shortest signed-axis BRC words**, distributed among exactly five signed-coordinate permutation orbit types:

| Sorted nonzero absolute components | Signed native endpoints | T | B per endpoint | Total B |
| --- | ---: | ---: | ---: | ---: |
| `(5)` | 12 | 5 | 1 | 12 |
| `(4,3)` | 120 | 7 | 35 | 4,200 |
| `(4,2,2,1)` | 2,880 | 9 | 3,780 | 10,886,400 |
| `(3,2,2,2,2)` | 960 | 11 | 415,800 | 399,168,000 |
| `(3,3,2,1,1,1)` | 3,840 | 11 | 554,400 | 2,128,896,000 |
| **Total** | **7,812** | | | **2,538,954,612** |

### Proof and completeness

Since `G=25` and there are six integers, every nonzero `|z_i|` belongs to `{1,2,3,4,5}`. If a 5 occurs, all others vanish. If a 4 occurs, residual 9 is either one 3 or `2^2+2^2+1^2` within five remaining coordinates. If no coordinate reaches 4, three 3s exceed 25; two 3s leave 7, realized within four remaining coordinates only as `2^2+1+1+1`; one 3 leaves 16, realized within five remaining coordinates only as four 2s. With no 3, six coordinates of magnitude at most 2 have square sum at most 24. These exhaustive cases yield precisely the five rows.

For a row with `k` nonzero components and absolute-value multiplicities `m_a`, independent signed axis labels yield exactly
`N=6!/(6-k)!/prod_a(m_a!)*2^k`
native endpoints. Each endpoint admits exactly `T!/prod_i |z_i|!` shortest signed-axis words: the axis displacements are forced, and any permutation is shortest. Multiplying these integers gives each row and their totals.

### Executed independent integer methods

One standalone checker builds the five types by enumerating all nondecreasing nonnegative six-tuples in `{0,...,5}^6` whose squares sum to 25 and applies the orbit stabilizer and BRC multinomial formulas. A separately implemented axis-by-axis dynamic program propagates the pair `(endpoint_count,word_count)` indexed by exact `(G,T)`, and inserts a new signed magnitude `a` in `C(T+a,a)` positions. It produces the independent finite certificate:
`T=5:(12,12); T=7:(120,4200); T=9:(2880,10886400); T=11:(4800,2528064000)`.
Both routes agree and all assertions pass.

Actual original local checker file executed with Python, exit code 0, output `PASS_EXACT_FINITE_G25_SHELL`; 3,018 UTF-8 bytes; SHA256 `45e5a98c733a35247a21320872cdc607e04edb492d65d231bdd2f549da9f4dde`; Git blob `d0693361c8e343c48cf7dc9a1983d20442dc79d4`. This exact byte-matching executed source is stored in `research_checks/X6_LP028_G25_FULL_SIGNED_NATIVE_SHELL_20261113_1700.py` at immutable Git commit `e17622834fafcecbe3edd76e08423fc12d03c6a6`, and has been fetched back from GitHub.

### Precise relation to prior LP028/R061 counts

The support-at-most-two subfamily of the full shell consists of exactly 132 signed native endpoints and 4,212 free shortest words (the `(5)` and `(4,3)` rows). This independently reproduces the already established restricted two-axis result at its actual scope. Historical R061's 72 words are the four nonnegative roots `(0,5),(3,4),(4,3),(5,0)` within **one fixed positive ordered two-axis chart**: `1+35+35+1=72`. The prior selected signed three-axis figure `846` belongs to one selected native three-axis support, not the complete six-axis shell. All four totals count different declared domains, with the full `S_25` value now supplied.

## Frozen historical code callers: seven additional actual complete reads

The following exact files were read fully at frozen pre-rebase commit `fd2bcff10ca6e147348b6c1236027fc0d2877df3`; actual lines/functions were classified by operation, rather than raw term collision:

- `experiments/x6_signed_native_spatial_v16_20260905/check_signed_brc.py`, blob `eadc2640e190165020a60a707ac5a14c497036a0`: lines 20–52 use primitive six-axis signed endpoint recurrence and nonnegative shortest word counts, with no positive-N-BRC orientation cancellation.
- `experiments/x6_signed_native_spatial_v16_20260905/check_x6_signed.py`, blob `275f327b603a9b07f8f6c0948347e75028d3a38a`: lines 79–137 explicitly distinguish signed native diagonal `D!=0`, relative observer and positive-path length-6 720-to-D result.
- `experiments/six_axis_foundation_v2_20260905/check_closure_addenda.py`, blob `a5685eea1cba3d2a9563fc336fc5c779e5ea3e41`: gauge connection signs concern chart transport; no typed signed-native-BRC cancellation.
- `experiments/six_axis_foundation_v2_20260905/ports.py`, blob `fd9b558e007a24c1ced932da0a53b4b78b5ffef0`: `sympy.cancel` at lines 42/62/76/100 is algebraic rational-function cancellation for guarded Schur port signatures, not subtraction of positive BRC word counts.
- `experiments/six_axis_foundation_v2_20260905/check_ports.py`, blob `313a4339a139cf62e5eff506c5b3023ca2d68596`: calls test formal transfer and spectral specialization, not spatial signed dominant-axis recovery.
- `experiments/brc_holonomy_parity_thickness_check.py`, blob `d2aa874c2e0e7bda6b830c98fab6c44817f5ce44`: rational graph-edge holonomy and m-power valuation are an algebraically distinct BRC domain.
- `experiments/brc_dominant_degeneracy_quotient_check.py`, blob `33740d338fdc0459bb5ef07a9afc01892fae4752`: `lead/ladd` are dominant **weight** and tie-multiplicity operators, not LP011 signed spatial dominant-axis rules. Its nonnegative histogram multiplicity operation is not LP019 graph-orientation cancellation.

These seven selected complete-frozen-source reads establish a **bounded NO_WRONG_CALLER_FOUND** at the stated call sites. LP011/LP019 historical offending caller attribution remains `UNRESOLVED_PROVENANCE` outside this class. They are not additions to the earlier **35 current-main executable** reviews and do not assert complete active 28-LP consumer coverage.

## Continuing mother objective and control

Original Task remains to reconcile all 28 LP rows and actual current consumers against frozen source. Prior frozen 24 `definitions/` corpus and currently saved 35 distinct current executable reviews are consumed, not re-performed. New classification supplies a precise positive full-six-axis replacement reference for potentially overscoped old G=25 claims. Next action: apply its exact five-orbit test to an actual remaining LP028/PathSqrt native-shell consumer, preserving caller signatures and revising only a proven mistyped invocation; continue old `experiments/` and `scripts/` actual LP011/LP019 call provenance, then send bounded scope and uncovered callers to independent Driver `REQUEST_REVISION`.

Own Source session (historical/current subject must be reauthorized): Researcher `EM-X6-FB6990`, SID `MCP-082892eb480e45dea6d4b9fcc0491034`, CLAIM `MCP-bdd4acf9d96a8f1f0dfab4e9`, RUN `RUN-756de85b94c23b46b181f7b8`. Original resume request `onhour-20261113-1633-own-x6-resume-v1` terminal `SUCCEEDED` on 2026-11-13 16:30 Asia/Hong_Kong, with owner revalidated; this identifies the legitimate next checkpoint path, not independent review or admission. Earlier ambiguous read `onhour-20261113-1613-x6-current-task-read-v1` has also now returned `SUCCEEDED`. Preserve frozen input commit `59538f585d037d09ef687b28715c4bc1a3f9fe03` and historical comparison commit `fd2bcff10ca6e147348b6c1236027fc0d2877df3`.

Source/Review: `AUTHOR-PROVED / EXACT FINITE CHECKER PASS / INDEPENDENT DRIVER REQUEST_REVISION STILL OPEN / UNREVIEWED / NOT_ADMITTED`.
