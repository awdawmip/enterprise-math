# X6 Unit150 — Actual historical R061 bidirectional segment consumer, signed native reversal, and source-level type reconciliation

**Status:** AUTHOR_EXACT_PROOF / SOURCE_LINE_AUDIT / FINITE_EXACT_EXECUTED / UNREVIEWED / NOT_ADMITTED (2026-11-19).  
**Mother:** PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905; task `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`.  
**Frozen mathematical input:** `59538f585d037d09ef687b28715c4bc1a3f9fe03`; historical comparison `fd2bcff10ca6e147348b6c1236027fc0d2877df3`. No P000/Foundation alteration.

## First-hand bounded source audit — previously uninspected R061 downstream

1. Historical `definitions/ENTERPRISE_UNORIENTED_BIDIRECTIONAL_SEGMENT_SPECTRUM_20260821.md` at `fd2bcff10ca6e147348b6c1236027fc0d2877df3`, Git blob `da35c76869ff88e46e28e33ba5bc37c95374a15d`: lines **13–23** explicitly call positive/min-zero canonical directed traces and gauges *native* and disallow native negative axes; **27–48** assert that the historical canonical reverse trace differs from the inverse of the forward trace for nonzero segments; **56–86** define a bidirectional spectrum and record `{5,sqrt(17)}`, with forward/reverse path-fiber cardinalities **35** and **5**.
2. Current `main:definitions/ENTERPRISE_UNORIENTED_BIDIRECTIONAL_SEGMENT_SPECTRUM_20260821.md`, blob `358a4997157d7546d88e63ae8d32e95feebf9c08`: lines **8–30** explicitly retype the old directional asymmetry as relative/min-zero observer data and assert signed native reversal-symmetric distance; **32–49** preserve the old bidirectional spectrum only as `SPEC_rel` and retain path/provenance distinctions.
3. Frozen `experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py` at `59538f585d037d09ef687b28715c4bc1a3f9fe03`, blob `300a96e3dc24bf6fff73743037a0347a8bc83176`: `shortest_event_count(z)=sum(abs(x))`, `spatial_norm_squared(z)=sum(x*x)`, `shortest_path_multiplicity(z)=(sum |x_i|)! / prod |x_i|!`.
4. Current and historical `definitions/ENTERPRISE_SEGMENT_ALL_SHORTEST_PATHS_20260817.md` are already typed as **downstream path realization**, not as primitive line identity. Historical blob `8718391a46a5fb7f4db08480499cf7caaa2aff39`, current blob `b2eb4980e058253e22a6c40ff7fcfb1d2d3bc2f6`. Their caveat `SAME_ENDPOINT_PATH != SAME_NATIVE_LINE_PATH` remains; this unit concerns **shortest signed step-word realizations**, not primitive straight segments.

These specific historical-current source lines extend the existing claim-level ledger's R061 directed-gauge classification to its **actual bidirectional downstream consumer**. They do not establish an erroneous historical LP011 argmax caller or LP019 N-BRC subtraction caller.

## Unit150 theorem (native signed path reversal)

Let a selected native three-axis slice have relative signed displacement `d=(d_1,d_2,d_3) in Z^3` embedded in `Z^6`. The native primitive alphabet has distinct signed unit labels `+e_i,-e_i`. Write `W_min(d)` for ordered signed step words of minimal length `N(d)=sum_i |d_i|` and endpoint displacement `d`.

Define the **reversed-inverse** operation on typed step words:
`I(s_1,...,s_N)=(-s_N,...,-s_1)`.
The negative of each primitive signed label is another declared primitive label. Therefore `I` maps `W_min(d)` bijectively onto `W_min(-d)`; it is its own inverse. Thus for every `d`,

`N(d)=N(-d),   G(d)=G(-d)=sum_i d_i^2`, and
`#W_min(d)=#W_min(-d)=N(d)! / (|d_1|!|d_2|!|d_3|!)`.

Proof of the count: a minimal word may contain no cancellable opposite-sign pair along an axis. It therefore has precisely `|d_i|` steps of sign `sgn(d_i)` on axis `i`; all multiset permutations and only those permutations attain the endpoint at length `N`. The multinomial formula follows. Reversing and flipping signs gives a bijection of such multisets, with order/provenance retained by the word map, not collapsed by scalar distance symmetry. For nonzero `d`, the orientation-tagged disjoint union of the two native shortest word fibers has size `2 #W_min(d)`.

**Exact test witness.** For `d=(3,4,0)`, `N=7, G=25`, and both native orientations have `C(7,3)=35` typed shortest words. Their orientation-tagged native union has **70** words. The historical R061 `35+5=40` pair remains an exact assertion *about its two independently decoded positive/min-zero traces*, not about the full native forward-and-inverse signed path pair. Likewise the historical unit-segment spectrum `{1,sqrt(2)}` is an observer diagnostic, while the native scalar is `1` in either orientation. This is a type correction, not a retrospective claim that the frozen historic positive-sector arithmetic was numerically wrong.

**Scope.** A native signed shortest-path fiber equality does not imply primitive-line membership for an off-axis composite displacement; nor does it identify tagged individual path provenance after applying the relative observer. No theorem is asserted for a history-bearing time evolution or original R063 benchmark.

## Exact finite regression

A standalone independent recursive count `F(a,b,c)=sum_{i:a_i>0}F(a-e_i)`, `F(0,0,0)=1`, was compared with the pinned factorial/multinomial mathematical interface for **all 2,197 triples in [-6,6]^3**; reversal-symmetric square norm was simultaneously checked. Explicit ordered signed words and their reversal-inverse images were independently enumerated for **all 125 triples in [-2,2]^3**, plus the `(3,4,0)` 35-word witness. Each side's signed labels, endpoint displacement and order were retained. In the corrected checker, these invariant checks execute through an explicit error-raising `require` function and remain active even when CPython strips `assert` statements under `-O` and `-OO`. The initial checker revision used `assert` and is superseded by the always-on check; historical revisions remain in Git. All checks passed.

Executed under CPython normal, `-O`, and `-OO`; stdout SHA256 including final newline was `9c9a175d0589b08fd2da0f501b0ee34cd19acef42ea67178b300391ad62c26ae` in all modes. The frozen `signed_brc.py` module and historical R061 decoding program were **not** executed by this unit: the checker independently reproduces their stated mathematical relation; the original six-file R063 512-case native benchmark was **not** rerun.

## Claim-level disposition / unresolved work

- **SUPERSEDE_AS_NATIVE** for historic R061 Stage3 positive-only native-axis restriction and reversal-asymmetric *native* gauge; these statements are valid only in the historic positive/min-zero decoding context, and current `main` has already retyped this consumer.
- **PRESERVE_OBSERVER** for historical orientation-free length multiset `SPEC_rel`, exact `{5,sqrt(17)}` and asymmetric `35,5` trace fibers, with their legacy observer and two independent decoding operations explicitly retained.
- **PRESERVE_PATH_BRC** for signed native shortest-step word multiplicity and its exact inverse-word bijection, with separate path orientation/word identity.
- **NO_CURRENT_PATCH_REQUIRED** on the audited current bidirectional spectrum file: existing current lines 8–49 supply the needed type correction. Do not overwrite historic commit evidence or duplicate earlier repairs.
- **UNRESOLVED_PROVENANCE:** historical LP011 allegedly wrong signed-native argmax call and LP019 allegedly wrong natural N-BRC subtraction call still require exact frozen `commit:path:line`, if they exist. A bounded search through source documents is not proof of full-corpus absence. Additional 28-LP downstream consumers remain to be inspected. Driver review and admission are independent.

**Next precise scientific action:** inspect another actually unexamined frozen/current consumer by exact file:line; compare affected claim against signed primitive directions, Cell identity, and retained path/observer types. Do not substitute more general auxiliary theory or repeat the original R063 benchmark.
