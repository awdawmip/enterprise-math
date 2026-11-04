# Independent review: CELL U27F-02 source recovery and event boundary

Date: 2026-11-04. Reviewer: `/root/research_nt_1104`.
Verdict: **PASS within the frozen paper's source-record and explicitly
conditional bridge scope.** No mathematical correction is required.

This is a local nonauthor review, not a formal Review vote, native admission,
Task completion, or shared-state transition. I did not construct, suggest,
edit, or debug the author's two propositions. We share a parent conversation
and the same Source snapshot. My prior work this turn was R004 external
finite modules and a Hodge support lemma; neither supplies a proof premise
here. The parent's review assignment identified the claims to examine, and
the author supplied filenames, frozen hashes, and the explicit nonrecovery
of `Ledger.commit`. That shared context is disclosed; it does not make this
a blind review.

## Exact frozen object

Author directory: `../../native/cell_next` relative to this review directory, actually
`/workspace/agent_artifacts/balanced_resume_20261104/native/cell_next/`.

- `SOURCE_RECOVERY_AND_EVENT_OBSTRUCTION.md`:
  `b18d9a43d82edbd36cdd4c240fbffab891196a529ced8e851daeb912dfea4b8f`.
- `SOURCE_RECOVERY.json`:
  `0c78abf330e7a4967677c7b5ccb53d0cdfd0f92ea7e7d508590f0ed1de2b09f6`.
- `EVENT_PAIR_SOURCE_EXTRACT.json`:
  `560c9c567ef7579146d9e12e6632e9e5a5aa4fdb83dcb2987f2c3d4caa39b575`.
- `NATIVE_EVENT_SOURCE_MAP.json`:
  `45d038531bdaa5cc8df5d13cbfad32695f5f5cc8301d8becab70d8a8db38e8c6`.
- `material_field_support_successor.json`:
  `a2acafe5b8c897becbed0e91bf64163cd3f170c486949eb65afc212a093f6b01`.
- `native_incidence_checks.json`:
  `5b0408a7c2838b3f27f2f79d548412109b92af8d6b6b75df335246889508c044`.

All six files match `FREEZE.json`, frozen at 2026-11-04T09:03:56.514341+00:00.
Source is `39556bf5207aa5ba559a27ec591c1bc1bf43b457`. My independent byte/JSON
audit also matched all 17 source-input pins listed by the author and all three
copied fixture records. `SOURCE_AUDIT_RECEIPT.json` retains those checks.
Hash agreement is provenance evidence, not a proof of native mechanism.

## 1. The exact event is the second transition, not the earlier move

I read the actual current `research_inputs/U27F_20261012/fixtures/carry_Q.json`
and its `/data/1`, `/data/2`, `/data/3` values, independently of the report's
table. The author extraction copies these values exactly.

At `/data/1`, stage `RESERVE_OR_DETACH`, material index 1 is at
`(1,0,0,0,0,0)`, and held token 2 has the same Cell. At `/data/2`, stage
`LOCAL_CARRY`, both are at `(1,0,1,0,0,0)`. Thus the displayed +E3 change is
between those two records. At `/data/3`, `RELATION_COMMITTED`, every material
Cell remains as at `/data/2`; token 2 changes from `held` to `bound` while
keeping `(1,0,1,0,0,0)`.

The new bound entry is exactly edge `(0,1)`, port 5, side 1. Bound tokens
0, 1, and 3 are unchanged; free records remain empty. The plan label
`['body',1,4,true]`, modes, and reference path data agree across the selected
commit pair. The source Boolean `after_relation_commit` changes false to true.
The source dictionary named `complete` acquires its `(0,1)` entry with tokens
0 and 2. I treat this as that dictionary's exact content, not an independent
certificate that a native physical edge has become complete.

The Taskbook `RS-CELL-U27F-02-NATIVE-TRIAD-20261012.md` expressly selects
`LOCAL_CARRY -> RELATION_COMMITTED`. It would be incorrect to attribute the
earlier +E3 displacement to this later selected event. The paper makes the
distinction correctly. This verification establishes facts about published
records; it does not replay or establish the unrecovered U27 implementation.

## 2. Exact U9 code recovery and path-prefix meaning

The current Source file
`research_notes/chatgpt_direct/20261008_cell_u9_local_latent_4b7e62/local_latent.py`
has 8,248 bytes, SHA256
`fc98fd83ee409bfaedd12dae634f63416d1cd779a3f27e58a06b841fb3cb482b`, and Git
blob `67408af5b977bed7295f7225cdd3f550c41b9729`. All three independently match
the original U27 input manifest's `baseline/cell_u27/reuse/local_latent.py`
entry. This is exact dependency recovery, not a substitute implementation.
I read the complete file as text without importing it or its dependencies.

Its `material(s,a,p,grow)` first sets `new=r.advance(s.cells[a],p)`, refuses
occupied destinations, and for each incident path sets
`changed=(p^1,)+w` in the grow branch. It updates only the selected endpoint's
path side and material Cell. With the declared signed port pairs, `p^1` is
the reverse step. Therefore an old path beginning at x is replaced by a path
beginning at x+d(p), first moving back to x, and then following the original
ordered word. Its meeting Cell is unchanged. For p=4 the reverse prefix is
5, as the fixture shows. This argument is a direct reading of the function
and the native signed-step definition; no dynamic run was performed.

The file calls itself candidate auxiliary-path dynamics, and `slide` explicitly
states that relation-record reassignment is not a certified three-force
event. The author correctly preserves this distinction. The -E3 prefix is a
path-maintenance datum; treating it as a mechanical reaction needs a further
source-qualified action/readout relation.

Crucially, recovering this dependency does not recover U27 `finite_inventory`,
`work_exposure`, or `Ledger.commit`. The frozen paper explicitly says so.
The manifest itself states that the complete original code archive is not
installed by the published fixtures. Its file list provides hashes for
`finite_inventory.py` and `code_entrypoints.json`, while the Task-required
`authority_pins.json` and `baseline/cell_u27/NOTE.md` are not individually
listed there. The report correctly treats their bytes/archive membership as
unrecovered. I do not independently certify the author's historical failed
remote Git request, and did not repeat it: that attempt is not load-bearing
for either proposition or for the narrower verified recovery statement.

## 3. The observer collision and U2 corollary are valid

The declared Q retains identity-labelled material Cells, identity-labelled
token Cells regardless of their storage class, and the common plan/modes/
reference paths. It intentionally omits stage labels, storage class, bound
relation, and the commit flag. For the selected C and R records every retained
value agrees. The predicate b checks token 2's specified bound-map membership:
it is false for C and true for R. Thus no function h can have b=h(Q) on even
this two-record domain. Appending b distinguishes this pair, but supplies no
general minimal-memory or whole-future-state theorem. The author's one-bit
qualification is correspondingly limited and correct.

I inspected the actual `field_prefix` signature and body in
`research_notes/balanced_resume_20261028/native/u2_incidence_prefix.py`.
It takes the pinned kernel object, labelled Cells, material incidence
families, depth, attenuation, and leaf bound. It seeds and propagates its
own source/path/packet grammar from those inputs. It has no U27 free/held/
bound ledger argument. Under the paper's explicitly equal complete input
assignment, deterministic output is equal, including full retained leaves.
Appending that equal output to Q cannot separate C and R. The same statement
holds componentwise for any collection of completed finite depths; it is not
an infinite-depth execution or convergence assertion. Resource-bound failures
are not counted as completed field outputs.

This does not say all possible U2-based models fail. A sourced map from the
U27 binding relation to incidence, gates, injection or internal response can
supply different inputs. The paper correctly treats that map as the missing
additional mechanism instead of presupposing it. The result applies the
existing fiber-constancy principle to a newly identified concrete source
pair and does not repeat the older I1/I2 adapter repair as new mathematics.

## 4. The displacement-only bridge is excluded only under its own premises

The candidate B_disp is deliberately restrictive: it generates each nonzero
primitive action from a nonzero change in listed material/token positions,
adds no action when all those positions are unchanged, and nevertheless calls
this commit a primitive stable nonzero triadic event. For this pair it produces
no nonzero action. Current P000 `typed_semantics.primitive_force_balance`
has `force_count_0=QUIESCENT_NOT_BALANCE_EVENT` and primitive stable balance
requires exactly three nonzero force quanta with `TRIADIC_CLOSURE_E`.
The candidate cannot meet its claimed event type. The implication is valid.

The paper does not infer that all actions require displacement, that a
nonmoving commit is physically impossible, or that this bookkeeping stage
must be a primitive stable event. It permits internal/non-displacement
actions or an explicitly enlarged composite event window, with their own
source and readout obligations. Counting the four tokens, three bound entries,
or three response legs as primitive action occurrences would not repair the
missing certificate. The distinctions and retained X6/timing types are sound.

## 5. Remaining obligations and disposition

I read the old `INTERFACE_CERTIFICATE.md` and U2 incidence adapter alongside
the new paper. Their G1/G2 obligations concern actual signed action incidence,
`Adm_E`/`TRIADIC_CLOSURE_E`, indivisible-event realization, and third-action
provenance. They may be jointly specified by `Lift_E`; neither the old nor
new paper proves that these obligations are independently separable.
The U27 source-record collision identifies information a proposed bridge
must carry. It supplies none of those native realization inputs.

G3 reaction/storage and release, G4 physical time and boundary update, and G5
occupancy law remain unknown. The successor JSON correctly records the
conditional ledger state and explicitly leaves physical material, field,
support and timing fields UNKNOWN. It does not offer two supposedly legal
native completions, a general native impossibility theorem, or empirical
compatibility. The related empirical task additionally needs an effective
force/readout and intervention behavior; a ledger bit is insufficient.

Both conditional propositions, the exact recovered dependency, and the
source-position/stage distinction pass. The package can be preserved as
independently reviewed local evidence at precisely that scope. The original
archive, implementation and authority-byte debts remain, as does the need
for an actual native event lift. The mother objective remains open.

Scientific program executions in this review: **zero**. I did not import
`local_latent`, call a propagator, reconstruct a trajectory, or run ordinary
arithmetic as a substitute for typed BRC. Administrative checks read files,
verified hashes, and compared copied JSON values. Hand source/relational
proof review is distinct from an execution certificate; no BRC operation is
claimed as executed.

EM-Source-Status: Read=Verified snapshot reused and frozen author files.
Write=Not required for shared Source in this local review role; local review
saved for owner publication. Actual reviewer identity: `/root/research_nt_1104`;
no formal Researcher-ID, Driver identity or review authority is assumed.
