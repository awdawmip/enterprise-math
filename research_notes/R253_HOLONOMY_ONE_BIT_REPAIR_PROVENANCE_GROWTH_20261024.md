# R253 — One-bit affine holonomy repair versus unbounded ordered-path provenance

**2026-10-24 · EM-DIRECT-R253K4 · author-side exact derivation, finite positive BRC checks · NOT a reviewed, officially CLAIMed, native-heartbeat-dynamics, or Foundation result.**

## Fixed source and intended semantics

Account rules: GLOBAL_KNOWLEDGE_V1 `main@420ddde0f088d90160ac4fdd5cf12ec873d82fc1`, locked P000 startup projection checked against canonical original blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`. Enterprise Math Source frozen `main@5404753a7a923c4ca9a3654256c057db878a7f35`: `src/enterprise_math/brc_transport.py`, `brc_control_port.py`, `docs/PORTABLE_RESEARCH_PROTOCOL.md`, and current BRC-only arithmetic and observer contracts. Predecessor R252: `research_notes/R252_INVERSE_ANCHOR_ALL_HORIZON_FIBER_20261024.md` at `1434cb61ee4166d14c16452cddfeacb36be4e30d`. R252's all-horizon inverse-anchor binomial identity is reused, not recounted as a new result.

Three finite *non-spatial* control states (Q={0,1,2}), with two distinct unit-weight, positive-multiplicity BRC alternatives from every state; six signed native chart-relative X6 axes remain six. The local chosen Cell chart anchor (o=0) is **not** a privileged global origin; neither an independent native plane nor a genuine heartbeat update law is claimed. Set (e_1=(1,0,0,0,0,0)), (S=mathrm{diag}(-1,-1,1,1,1,1)), (T_k(z)=z+ke_1), (R_k(z)=Sz+ke_1).

| Source control | Edge selector 0 | Edge selector 1 |
|---|---|---|
| 0 | target 2; (R_{-1}) | target 2; (T_{-1}) |
| 1 | target 0; (R_{-1}) | target 0; (T_{-1}) |
| 2 | target 1; (T_{+1}) | target 2; (T_{-1}) |

Each edge carries weight 1 and multiplicity 1; the selector word records the *ordered source provenance*, unlike the final weighted effect histogram. The source `Affine.then(later)` is `later ∘ self`. `ControlPacket.start` denotes a **time port**, distinct from initial control state. Its `blocks` preserve terminal control and affine-effect histogram; they do not preserve individual words.

## Theorem A — exact effect repair using inverse anchor plus linear holonomy

For any invertible six-axis affine map (F(z)=Lz+b), with a chosen target anchor (o), put (p=F^{-1}(o)). The pair ((p,L)) determines (F) uniquely via
[
oxed{F(z)=L(z-p)+o,qquad b=o-Lp.}
]
Proof: (F(p)=oRightarrow Lp+b=o); conversely any invertible (F) computes (p=L^{-1}(o-b)). Thus ((p,L)) and complete affine effect (F) are in bijection. Reindex each exact positive atom ((q,w,F,	ext{multiplicity})) as ((q,w,p,L,	ext{multiplicity})). Equality, serial effects, and aggregation of identical positive atoms are retained at **all finite horizons**. This is a faithful *effect-histogram* compression, not a claim of recovering discarded individual path words.

In the R252 finite effect subgroup (Lin{I_6,S}), write (arepsilonin{+1,-1}) for the first two diagonal signs. Then (p=-arepsilon ke_1), so
[
oxed{(,p,arepsilon,)longleftrightarrow
 F=(mathrm{diag}(arepsilon,arepsilon,1,1,1,1),-arepsilon p_1e_1)}
]
shows *one holonomy bit* suffices. Necessity is witnessed at depth 3: the same inverse anchor (p=-e_1) has both (R_{-1}) and (T_{+1}), different (L) values. The anchor alone cannot reconstruct both. For a general finite admissible linear group (H), if all (Lin H) occur at the same anchor, at least (lceillog_2|H|ceil) fixed-width repair bits are necessary *for that family*.

### Exact depth-three repaired counts

The two R252 initial controls 0 and 1 have equal *untagged inverse-anchor* distributions at **every finite depth**, but depth 3 separates their ((p,L)) observations (after suppressing terminal control):

| First anchor coordinate (p_1) | Linear effect | Start 0 count | Start 1 count |
|---:|---|---:|---:|
| -3 | S | 1 | 1 |
| -1 | S | 3 | 2 |
| -1 | I | 0 | 1 |
| +1 | I | 3 | 2 |
| +1 | S | 0 | 1 |
| +3 | I | 1 | 1 |

At depths 0, 1 and 2 their ((p,L)) histograms agree, making depth 3 the **first** repaired-observer witness. All entries count positive paths: the negative signs in *external differences of counts* do not represent signed BRC branches.

## Theorem B — fixed-width path-provenance repair is impossible for unbounded horizon

Fix initial control 0. At depth (m), every binary edge word (win W_m={0,1}^m) is a valid path, so (|W_m|=2^m). Observe only its terminal control (q), its full six-dimensional composite affine effect (F=(L,k e_1)), and its unit weight. Let (O_m(w)=(q,L,k)).

Here (q) has three possible values and (Lin{I_6,S}). The translation obeys (k_0=0, k_{j+1}=eta_{j+1}k_jpm1) with (eta_jin{pm1}); induction gives (|k_m|le m, k_mequiv mmod 2), hence at most (m+1) distinct translations. Therefore
[
oxed{|mathrm{im},O_m|le 6(m+1),quad
M_m:=max_y|O_m^{-1}(y)|ge leftlceil {2^mover 6(m+1)}ightceil.}
]

At a fixed horizon, if one adds a per-history tag and requires exact word recovery from ((O_m(w),mathrm{tag}(w))), the exact **minimum worst-case tag width** is
[
oxed{b_m=lceillog_2 M_mceil.}
]
Necessity: tags must be distinct within each (O_m)-fiber; sufficiency: enumerate each fiber using tags (0,ldots,M_m-1) and reuse tags between different fibers. Since the whole ordered word needs at most (m) bits,
[
oxed{m-log_2(6(m+1))le b_mle m,quad b_m=m-O(log m)=Theta(m).}
]
Consequently **no fixed finite tag alphabet can losslessly record every ordered R252 path at every horizon**, even when the receiving observation retains full affine effect, terminal control, weight and multiplicity. At (m=3), first collisions are binary words `000` and `101` with (O_3=(0,I_6,-1)), and `001` and `100` with (O_3=(0,S,-1)); direct enumeration proves no collisions at (mle2). The exact positive effect histogram reports count 2 at the merged atom but not which two source words produced it.

**Interpretation:** One extra holonomy bit completely repairs the weaker *affine effect* observer. Full ordered R193-style source history requires asymptotically linear additional per-path information unless its actual declared observer is weaker or its horizon bounded. A shared history DAG can compress common representation storage, but this counting bound remains about information sufficient to distinguish the (2^m) individual histories given their final ((q,F)) values. It does not assert a lower bound on the length of a separately shared DAG description.

## Independent evidence, verification and exact limits

Actual local author-side positive-integer BRC-effect calculations (no classical trigonometric/π, signed amplitudes, ordinary propagators or floating errors) were done with `R253_verify.py` to depth 48 (both initial controls), independent `R253_verify_independent.cpp` compiled with C++17 and run to depth 48, and full ordered word enumeration to depth 13 in Python (depth 3 in C++). The all-horizon theorem is proved by the counting argument, not extrapolated from test bounds.

| depth m | total paths | distinct terminal/full-effect atoms | largest provenance fiber | exact minimum fiber tag bits |
|---:|---:|---:|---:|---:|
| 3 | 8 | 6 | 2 | 1 |
| 12 | 4096 | 62 | 250 | 8 |
| 24 | 16777216 | 134 | 705854 | 20 |
| 40 | 1099511627776 | 230 | 35345337418 | 36 |
| 48 | 281474976710656 | 278 | 8233429852978 | 43 |

Source tool family `T0_BRC_AFFINE_EFFECT_TRANSPORT` and method `brc.affine_effect_transport`: **REUSE_APPLIED** at the exact `Affine.then/.inverse`, `EffectHistogram`, and control-port contracts. **NOT REUSE_EXECUTED** against the installed original `enterprise_math` modules; native `ControlPacket.from_edges/.then` was not executed in the available environment. `R253_NATIVE_INTEGRATION_PENDING.py` has passed syntax compilation only. Hence native integration = `NATIVE_SOURCE_INTEGRATION_PENDING`. The formal invertible effects have **not** been proved admissible under actual P000 heartbeat evolution/triadic dynamics, verified real Cell-address codec, or R193 source observer, and the result is not a formal claimed task, accepted Result, independent review, or physical assertion.

Local exact evidence SHA-256 (identifies local package member bytes, not GitHub note):
- `PROOF_R253.md` `c732907c36dc969cbe7fba236166f6cb673698484162eda628cdd98a5ef08c74`
- `R253_verify.py` `03097668b691527223fc0debcbf21afe17bb184eecada8a9d64a4eedb6e5c857`
- `R253_verify_independent.cpp` `9149246ae33c01b2946662644a81ed791308248a83130ca20f243683e3355dde`
- `R253_AUTHOR_EXACT_REPORT.json` `a7009649a1c2759dd6eeb3672bd69f1a9003d7964a1bd945f84aaa22c4e5a2cf`

## R254 precise next executable unit

Run `R253_NATIVE_INTEGRATION_PENDING.py` under an actually matching current Source Python package and record `ControlPacket.blocks`, aligned `start/end` time ports and positive inverse-anchor/holonomy counts through depth 3. Then read the actual R193 ordered source-path observer and permitted native X6 update family; determine whether its minimal sufficient carrier needs only (p,L) (full effect) or source-word/DAG augmentation (full provenance). A native heartbeat correspondence proof, live owner/CLAIM verification (MCP current control query yielded `CONTROL_QUOTA`), formal source Result publication and independent Driver review remain OPEN. No other owner's live task was taken.

Research activity `RA-EMR4-20261024-1330-PAIRBIT`; authentic GitHub account `awdawmip`. Project author-side note publication is a durable frontier only and does not promote mathematical status.
