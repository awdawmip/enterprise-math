# X6 LP026 / R061-V12 — corrected native directed-gauge consumer and exact diagonal-kernel certificate

Date: 2026-11-13 (Asia/Hong_Kong, on-hour TASK_RESEARCH lane).
Task: `RS-X6-LEGACY-PLANE-RECONCILIATION`; publication `TP2-B4A441B23DA3159232C2`; parent `PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905`.
Author-side status: **EXACT MATHEMATICAL COUNTEREXAMPLE AND CURRENT SOURCE REPAIR / LOCAL INTEGER CHECK EXECUTED / UNREVIEWED / NOT_ADMITTED**.
Researcher: `EM-X6-FB6990`; own Sources session `MCP-082892eb480e45dea6d4b9fcc0491034`.
Historical research conversation: `chatgpt-research-onhour-enterprise-math-20260923`, not the maintenance conversation.

## Exact source and frozen scientific setting

- Frozen mathematical baseline: `awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03:p000_reality_foundation.json` (P000 V5) and `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md`; mandatory `definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json`.
- Historical comparison: `fd2bcff10ca6e147348b6c1236027fc0d2877df3`.
- Actual CURRENT-MAIN consumer located: `research_notes/X6_DIRECTED_GAUGE_AND_PROJECTION_CONTRACTION_V12_20260905.md`, old current blob `7f15fdf12839f08fde90729dc5abf2cd59f0d5b5`, Section 7. It asserted that the directed gauge pulled back from `G6_D` becomes definite on an affine native Cell torsor if full coordinates are promoted.
- Corrected current consumer Source commit `9497bcd7bda2ccfa5187523e6ab4ac496e5d20ac` (new blob `b36b926b4ea337d842fbf7b33cf5aab2480d0da7`), read back at that immutable commit. Original theorem's quotient-side algebra, reversal and contraction calculations remain intact.
- Exact checker: `research_checks/X6_LP026_V12_NATIVE_GAUGE_COUNTEREXAMPLE_20261113_0057.py`, immutable commit `19a27cf91ffa9822a22f365afa4c8d1ef4a512b2`, Git blob `a88c421cd56b44ad2b1ac781fef38c8ada1bcfbf`, SHA256 `8b7ea03cade50b32d52d25f9b6f5271723f7d18206f32408c660edd73390bb74`. The exact locally executed bytes match the remote blob.

## New exact kernel theorem

In native signed six-axis coordinates, let `D=(1,1,1,1,1,1)`, `G(d)=sum_i d_i^2`,
`can6(d)=d-min_i(d_i)*D` and `g(d)=sqrt(sum_i can6(d)_i^2)`.
For any native Cells `P,Q` with full signed displacement `d=q-p`:

1. `g(d)=0` if and only if `d=tD` for some `t in Z`: `can6(d)=0` iff every component equals `min(d)`.
2. For every `t in Z`, `can6(d+tD)=can6(d)`; hence `g` factors exactly through the quotient `Z^6/ZD`. On this quotient it has positivity, definiteness and the directed triangle inequality already established in original V12 §2.
3. On native Cells, the pullback `d_rel(P,Q)=g(q-p)` satisfies the triangle inequality but has zero-distance fibers `Q-P in ZD`; it is therefore a **directed pseudometric** at native scope. This is an exact classification for every native pair, not a finite inference.

**Counterexample to V12 §7 native definiteness.** Take `P=0` and `Q=D`. Then `P!=Q`, `G(Q-P)=6`, and `can6(Q-P)=0`. Native signed shortest words from `P` to `Q` consist of all permutations of the six positive distinct primitive axis steps: `6!=720` exact witnesses, whereas the observer directed gauge is zero. For `Q-P=tD` the native squared norm is `6t²`; for nonzero integer `t`, shortest signed BRC multiplicity is `(6|t|)!/(|t|!)^6`, while `g(tD)=0`.

**Reversal-type witness.** For `e_1`, native `G(e_1)=G(-e_1)=1`; the relative directed gauge's squared values are `g(e_1)^2=1`, `g(-e_1)^2=5`. The old `{1,5}` is a useful asymmetric *observer* spectrum, not an asymmetric native metric.

### Proof scope and downstream action

The properties follow directly from integer min-shift, uniqueness of a zero min-zero section, and the previously proved triangle inequality on the quotient; the signed shortest multiplicity uses the multinomial formula on P000 native axis steps. Native Cells, relative observer classes and Path-formal/BRC remain separately typed. Correct current consumers must take raw signed `q-p` for Cell identity/native component norm and retain the common-depth register and BRC provenance before a future-operation-dependent quotient. This repairs an **actual** current theorem-facing source use (LP004/006/007/008/022/026), not the still-unlocated LP011/LP019 historical native caller.

## Exact executed finite diagnostic

The identical checker bytes were run locally with CPython; actual stdout:

```text
PASS X6_LP026_V12_GAUGE_TYPED_CORRECTION
exact shift-invariance checks=78125 native-observer collision witnesses=62500
native diagonal witness: delta=(1,1,1,1,1,1), G=6, shortest signed BRC=720, observer squared gauge=0
native reverse-axis squared norm=(1,1), relative directed squared gauge=(1,5)
```

Declared finite coverage: all `5^6=15,625` raw integer tuples in `[-2,2]^6`, each with five diagonal shifts `t in [-2,2]`; additional exact diagonal depths `t=±1,±2,±3`. The all-integer kernel and quotient theorem above are proved independently of finite coverage. This is neither the native benchmark nor a live module-import test, and does not replace prior completed 50,771-assertion original coordinate regression.

## Continuation for parent objective

Already complete and reused: historical fixed-positive 72; full signed three-axis N25 30/846; native-vs-carrier return; LP026 norm/depth and faster interval certificates; original coordinate v7 regression; LP028 chart/collision source import; verified current-router patches.

Current Source read `onhour-20261113-0057-own-x6-continuation-read-v1` observed `NO_LIVE_CLAIM`, typed continuation required from predecessor `MCP-fd3ed9c33e98f45420aedd51`, Issue #240 comment `6826074733`; original resume `onhour-20261113-0057-x6-own-run-resume-v1` failed for expired live claim. Preserve original RUN `RUN-0881a7a2c2f958314cc0b5f5`, last historical generation 3 revision 7 as historical checkpoint; do not treat that binding as current mutation authority. No independent Reviewer verdict, Result or Native semantic PROGRESS is claimed.

**Next scientific action:** further bounded current-theorem and executable caller search, especially live uses of `can6` and `Coord6.norm_squared` as signed-native Cell metric, with actual call path and immutable source pin; complete old LP011/LP019 attributed native bad-call loci if they exist, otherwise record `UNRESOLVED_PROVENANCE` with finite inspected corpus. Resolve current-authority typed continuation from same session before formal native semantic checkpoint. Existing Activity schema issue #2187 remains an independent Source validation repair, never a reason to fabricate readback or reassign Researcher identity.
