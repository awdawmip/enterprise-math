# X6 Unit177 — R061 min-zero relative observer cannot recover signed native BRC even with L and Q

- Task: `RS-X6-LEGACY-PLANE-RECONCILIATION`; publication `TP2-B4A441B23DA3159232C2`; parent `PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905`.
- Scientific Source pin: `59538f585d037d09ef687b28715c4bc1a3f9fe03`; immutable historical comparison pin: `fd2bcff10ca6e147348b6c1236027fc0d2877df3`.
- Research lane: `chatgpt-research-onhour-enterprise-math-20260923`; historical Researcher `EM-X6-FB6990` / SID `MCP-082892eb480e45dea6d4b9fcc0491034`. The Research/maintenance logical lanes are distinct.
- Scientific status: **AUTHOR_PROVED / EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED**; this is a signed-native-vs-relative-observer *comparison theorem*, not a new physical law, P000 revision, formal acceptance, or Native checkpoint.

## Frozen provenance and direct downstream semantic boundary

1. Historical `definitions/ENTERPRISE_DERIVED_DIAGONAL_DISPLACEMENT_QUOTIENT_20260826.md` at `fd2bcff10ca6e147348b6c1236027fc0d2877df3`, blob `11f47f9d2d70439fdada6d59242790fdcf46929e`: lines 64–88 specify `can(z)=z-min(z)(1,1,1)`; lines 103–124 identify R061 Stage-2 decoder with this **derived** section; lines 119–124 do not assert native X6 point identity.
2. Frozen `src/enterprise_math/diagonal_quotient.py`, blob `3ac387c0103665943f13ba9e306a6167080c701d`: lines 44–48 implement that min-zero canonicalization, and its module docstring lines 1–15 explicitly forbids using the derived quotient to identify primitive native points without a separate theorem. This is an inspected implementation, **not** evidence of an unverified production-module consumer.
3. Current native P000 carrier `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md` at `59538f585d037d09ef687b28715c4bc1a3f9fe03`, blob `b4d49a1bbcccad0521618c6d20f6dcfa242b420a`, retains signed `Z^6` Cell coordinates, including any selected signed `Z^3` slice. Native signed kernel `experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py`, blob `300a96e3dc24bf6fff73743037a0347a8bc83176`, supplies `L(z)=sum |z_i|`, `Q(z)=sum z_i^2`, and `B(z)=L(z)!/prod |z_i|!` for a signed Cell displacement. Embedding a three-coordinate displacement with three zero entries preserves these three values.
4. The **current main** `definitions/ENTERPRISE_ARBITRARY_POINT_DIRECTED_LINE_GAUGE_20260821.md` (blob `875e3b274e5be03c5872f782872065a0b96d14eb`) and `definitions/ENTERPRISE_UNORIENTED_BIDIRECTIONAL_SEGMENT_SPECTRUM_20260821.md` (blob `358a4997157d7546d88e63ae8d32e95feebf9c08`) are already explicitly retyped as relative/observer-only and superseded as native metric. **Do not re-edit these as if still presenting obsolete native doctrine.** No bad LP011/LP019 historical production `commit:path:line` is inferred from them.

## Exact all-integer theorem

Let `d=(1,1,1)`, `can3(z)=z-min(z)d` on signed `Z^3`, and let `L,Q,B` be the native shortest-event, squared-component-length and shortest signed-word multiplicity just defined. For every integer `m>=1`, put

```
A_m=(-3m,-3m,0),       B_m=(m,m,4m).
```

The different native Cell displacements have **identical augmented relative observations**:

\[
\boxed{\operatorname{can3}(A_m)=\operatorname{can3}(B_m)=(0,0,3m),\quad
 L(A_m)=L(B_m)=6m,\quad Q(A_m)=Q(B_m)=18m^2.}
\]

They are in one diagonal class because `B_m-A_m=4md`; no quotient is being asserted on native Cell identity. Their native signed BRC counts are

\[
B(A_m)=\frac{(6m)!}{((3m)!)^2},\q\quad
B(B_m)=\frac{(6m)!}{(m!)^2(4m)!}.
\]

Consequently the exact ratio is

\[
\boxed{R_m=\frac{B(B_m)}{B(A_m)}
=\frac{((3m)!)^2}{(m!)^2(4m)!}
=\frac{\binom{3m}{m}^2}{\binom{4m}{2m}}
\ge \left(\frac32\right)^m.}
\]

**Proof of the uniform exponential lower bound.** Define `R_0=1` by the same factorial expression. Direct integer cancellation yields

\[
\frac{R_{m+1}}{R_m}=
\frac{9(3m+1)^2(3m+2)^2}
{8(m+1)(2m+1)(4m+1)(4m+3)}.
\]

Subtracting `3/2` leaves

\[
\frac{3m(115m^3+166m^2+71m+8)}
{8(m+1)(2m+1)(4m+1)(4m+3)}ge0
\q\quad(m\ge0).
\]

Thus `R_{m+1}>=3R_m/2` and induction proves the claimed bound, with `R_1=3/2`. All formulas are exact integer/rational identities. The leading exponential growth rate is `729/256` by Stirling, but the elementary lower bound suffices for the no-uniform-approximation theorem.

**Consequence.** Let `F(can3(z),L(z),Q(z))>0` be any estimator of native `B(z)`, using only these three readouts, and suppose `B(z)/K <= F <= K B(z)` holds on all signed triple displacements for a constant `K>=1`. Applying it to `A_m` and `B_m` gives `K^2 >= R_m >=(3/2)^m`, which is impossible for any fixed finite K. Thus the relative min-zero observer remains insufficient even after adding native path length and native squared length; the required multiplicative BRC distortion is unbounded.

For `m=1`, `A=(-3,-3,0)` and `B=(1,1,4)` both produce `can3=(0,0,3)`, `L=6`, `Q=18`, yet have native BRC counts **20** and **30**, respectively. The old R061 min-zero representation is a valid **relative** section; it simply cannot replace signed raw coordinates for an arbitrary native BRC query.

## Reproducible executed certificate

Independent Python checker `research_checks/X6_UNIT177_R061_MINZERO_NATIVE_BRC_LOSS_CHECK_20261120.py` (blob `3c96dc21f386ea3a2fd2b761a435f0fe18d11fec`, commit `8f368364f80f69f6e6c7f28d6639dc88f0602982`) implements signed integer `can3,L,Q,B` without importing a historical production module. Its exact JSON certificate `research_checks/X6_UNIT177_R061_MINZERO_NATIVE_BRC_LOSS_RESULTS_20261120.json` (blob `0cfa3647f9d00f6b2f5e0334ae01aa4c50c600d6`, commit `c69754f8856e57c6d692c4cd7a13fb3d4079ae76`) is verified against local output. Python normal, `-O`, and `-OO` modes produce the same SHA256 `dead3b168de465eebe6c22c1a3f96a0b18fa4ce92a8b6da2b4a68c2ef9371175`.

It checks every `m=1,...,64`, 729 signed triples in `[-4,4]^3` grouped by `(can3,L,Q)` (683 groups; **6 distinct groups with differing native BRC multiplicities**), plus 1,715 exact diagonal-shift invariance checks; **1,779 explicit validations**, zero failures. No `assert`-only checker gate exists; no R063 native benchmark was rerun. The general theorem is proved independently of this finite check.

## Task disposition and precise remaining work

- New claim status: `PRESERVE_OBSERVER` for the old derived R061 min-zero section; `PRESERVE_PATH_BRC` only with native signed displacement and branch multiplicity data. Augmented observer-only `(can3,L,Q)` is **not** a native BRC-sufficient statistic.
- This unit adds no false source assertion: the alleged historical LP011 invalid native argmax and LP019 subtraction of positive native N-BRC still lack verified offending `commit:path:line`. Real producer–consumer crosswalk of the entire frozen 28-LP corpus remains open.
- Units175–176 already have immutable author artifacts and Activity193. Original native resume `onhour-20261120-0812-x6-own-run-after174-resume-v1` has now returned `SUCCEEDED / RUN_READY`, generation 2 as of its own receipt; a later read does not by itself grant writer authority. The first new exact continuation read `onhour-20261120-0907-x6-exact-cont-read-v1` was last observed RUNNING and must be reconciled by **its own** request ID, not duplicated.
- Unit177 native association, Units175–176 native association, historical Units149–152, final 28-LP crosswalk, and independent Driver review/admission remain separate. Private custody lookup currently supplies a profile with another declared conversation label; that account capability is not silently borrowed for this Research lane.

**Next:** consume the pending original continuation read, verify current exact own Research claim/run and explicit lawful role capability, then publish the already-saved Unit175–177 semantic citations only if the same-lane write is independently authorized. Continue the highest-impact uninspected real frozen producer→consumer line; do not repeat existing exact checks or infer LP011/LP019 offenders without the original code.
