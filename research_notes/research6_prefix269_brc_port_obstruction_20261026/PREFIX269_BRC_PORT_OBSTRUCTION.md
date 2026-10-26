# PREFIX-269 | X6 relative observation + target-forgotten positive-BRC mass is not port-context safe

**Research line:** 进取数论研究6. **Date:** 2026-10-26. **Type:** author-side mathematical note; **status:** EXACT_PROOF / LOCAL_SEMANTIC_MIRROR_PASS / SOURCE_IMPORT_CHECK_PENDING / NATIVE_PHI_PENDING / UNREVIEWED / NOT_ADMITTED. This note does not claim a live research Task, CLAIM, formal Result, Driver review, or physical heartbeat law.

## Frozen authority and exact Source

- GLOBAL_KNOWLEDGE_V1: `awdawmip/chatgpt-global-knowledge@f5d54855ddabc643c239655311517ccb33e15f31`; entry files, current Project/TASK router, ACTIVE worldview and P000 startup projection were read. The P000 projection's canonical SHA-1 `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc` matched the original P000 blob.
- Enterprise Math: `awdawmip/enterprise-math@d9d1164a14181612de02c6379821760f9b749420`; `docs/PORTABLE_RESEARCH_PROTOCOL.md`, `docs/HEARTBEAT_BRC_ONLY_ARITHMETIC.md`, `research_constraints/heartbeat_brc_only.json`, `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md`, `definitions/ENTERPRISE_BRC_RECURRENT_PORT_FOUNDATION_20260903.md` (WBRC-T30/T31), `src/enterprise_math/brc_weighted.py`, `src/enterprise_math/brc_weighted_recurrent.py`, `src/enterprise_math/brc_recurrent_ports.py`, `definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json`, and `definitions/HEARTBEAT_SELF_CONSISTENT_INSTANT_V0_1.json`.
- Actual GitHub connector actor `awdawmip`. The separate static Enterprise Math MCP execution identity returned `STATIC_READONLY_SCOPE_DENIED`, `operation_sent=false` on session registration; current tasks and dispatch returned `CONTROL_QUOTA`. Therefore current active Owner/CLAIM is **unverified**, and this author-side note is not a canonical Task Result.

## Mother question, scope and observer

PREFIX-268 established that `r(z)=z-min_i(z_i)(1,...,1)` is future-safe for the declared **pure spatial** native X6 signed unit translations and axis permutations. It did *not* show that spatial relative coordinates together with a source-erasing positive BRC summary are safe for later joint port contexts.

Work entirely within Source WBRC-T30/T31 finite **non-negative rational** port modules with a stable hidden block. Choose the same native chart-relative Cell coordinate `z=(0,0,0,0,0,0)` for both modules. Form a *mathematical product test carrier*, not a declared complete native heartbeat state. Let its intentionally coarse observer be

```
q(z, module) = (can6(z), CWM of one completed positive macro-excursion,
                 with the output-port label forgotten).
```

Future operations are precisely the WBRC-T31 allowed additions of rational non-negative edges between existing labeled boundary ports. The future observation is the stable/unstable result of Source recurrent positive total-mass analysis. CWM is the positive (count,total,dominant) branch state, not a signed amplitude or absolute global loop zeta.

## Theorem: exact minimal two-port obstruction

**There exist two baseline-stable positive-rational modules with the same `q`, but a single identical permitted future port context makes one unstable and leaves the other stable. For this exact observer, one labeled port cannot exhibit such a failure: two are minimal. The labeled effective port matrix `W_eff` is the correct minimal all-context dynamic signature under WBRC-T31; absolute full global zeta requires the separate hidden-loop constant `Z_int`.**

### Full three-state matrices and source-typed collapse

Order full states as `(p,h,q)`, where `p,q` are visible labeled ports and `h` is one hidden internal state. All unlisted edges have positive BRC mass zero. Use

```
M_A = ((0, 1/2, 0),
       (0,   0, 1/2),
       (0,   0,   0))

M_B = ((0, 1/2, 0),
       (1/2, 0, 0),
       (0,   0, 0))
```

Both hidden blocks are `A_h=(0)`, hence stable, `(I-A_h)^(-1)=(1)`, and hidden zeta `Z_int=1`. Source `recurrent_port_signature` computes `W_eff=B+Y(I-A_h)^(-1)X`, giving

```
W_A = ((0,   1/4), (0,0))
W_B = ((1/4,   0), (0,0))
```

Both baselines are stable: `W_A^2=0`, while the only nonzero feedback in `W_B` has mass `1/4<1`. The sole one-hidden-state excursion for A is `p→h→q`; for B it is `p→h→p`. Actual Source CWM semantics are `cwm_propagate(cwm_edge(1/2),cwm_edge(1/2))=(1,1/4,1/4)`, so forgetting output-port label yields exactly the same macro CWM. The Cell and relative coordinate are also identical. Thus the two declared coarse states have identical `q`, even though `W_A != W_B`.

### A single future Port context distinguishes them

Add **the same** WBRC-T31-permitted non-negative rational edge `q→p` with weight `4`:

```
K   = ((0,0),(4,0))
U_A = W_A + K = ((0,1/4),(4,0))
U_B = W_B + K = ((1/4,0),(4,0))
```

A is **unstable**: the positive closed port path `p→q→p` has exactly `(1/4)*4=1` mass. Repeating it yields at least one unit of positive walk mass at every even recurrence depth, so the positive star diverges. Algebraically `det(I-U_A)=0`.

B is **stable**: the strict positive integer potential `h=(1,5)^T` satisfies `U_B h=(1/4,4)^T < h`, which is a Source `verify_recurrent_integer_stable_certificate`-type witness. Its exact non-negative star is

```
(I-U_B)^(-1) = ((4/3,0),(16/3,1)).
```

Thus the same legal future context yields different stable/unstable BRC outputs from states with the same coarse observer. This proves **non-congruence** for the precisely declared product observer, not for a physical one-heartbeat operator.

### Why two ports is sharp

With one labeled port, the unlabelled macro total mass is just the single scalar `W_eff` entry. Equal CWM entails equal total W, hence equal `W_eff`. Canonical WBRC-T31 states that two baseline-stable modules with the same labeled `W_eff` are dynamically context-equivalent for every allowed non-negative rational port context. Therefore one port cannot realize this observer failure; the exhibited two-port construction attains the lower bound. The statement is conditional on *this* macro-total CWM observer; removing more information can allow earlier failure.

An independent paper certificate consists of the positive recurrent cycle of mass exactly 1 for A and the strict integer potential `(1,5)` for B. It does not depend on a floating-point eigensolver.

## Exact executed check and separate native gap

Local author-side checker `verify_prefix269.py` performed only positive rational BRC operations and asserted the two full modules, hidden stars, effective matrices, equal target-forgotten CWM, context, unstable singular cycle, stable positive certificate, and exact inverse for B. It emitted structured `RESULTS_PREFIX269.json` with PASS. Both are carried in the conversation handoff ZIP `em_research6_prefix269_20261026_local_handoff.zip` (SHA-256 `88b388ef7e45473d8e56108ddeaf7793d81a20ac054d7b162f6e573d7d7c7390`). ZIP contents were separately extracted and re-run with byte-identical results. This **standalone semantic mirror** did not import the installed Source package, absent from this runtime. A Source-import verification script is provided separately for native execution; successful GitHub storage of that script is not its execution.

No pi, ordinary trigonometry, conventional matrix exponential, Taylor/Padé/Cayley substitution, floating errors, physical phase cancellation, or native physical time was used. These certificates prove only positive finite-rational BRC port-context behavior, not a phase-amplitude or `TRIADIC_CLOSURE_E` result.

**Full native-heartbeat barrier:** the immutable Source `HEARTBEAT_WORLD_NATIVE_X6_TIME.json` has `fixed_heartbeat_program=null`; the provisional `HEARTBEAT_SELF_CONSISTENT_INSTANT_V0_1.json` defines an instantaneous self-consistent *snapshot*, not a complete update law `Phi`. Thus no real native `Phi(Cell,Port,field,phase,time,provenance,boundary)` was identified or executed. Cell-to-port coupling, typed sign/phase transfer, boundaries, time evolution and native/BRC correspondence remain unresolved. In particular `K` is an allowed **BRC port context**, not a performed heartbeat.

## Next exact question (PREFIX-270)

Find one Source-backed coupled native `model_law_id` and full typed heartbeat update `Phi`; prove that its one-heartbeat port subaction actually implements the WBRC-T31 context contract or identify the first violated type/correspondence assumption. If it does, lift the two-port witness with complete Cell/Port/field/phase/time/source/boundary details and check native observation descent. Otherwise preserve the new minimal obstruction as a **conditional BRC theorem**, not a physics theorem. The native current Owner/CLAIM and independent Driver must be resolved by a live authorized receipt before formal publication/review.

**Admission:** `AUTHOR_SIDE_BRC_CONTEXT_EXACT / NOT_A_NATIVE_RESULT / NO_LIVE_CLAIM / NOT_REVIEWED`.
