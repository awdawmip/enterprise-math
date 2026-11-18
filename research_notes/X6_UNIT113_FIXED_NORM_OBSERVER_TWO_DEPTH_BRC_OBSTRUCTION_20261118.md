# X6 Unit113 — exact two-depth theorem for a fixed signed-shell observer and a sharp one-bit BRC obstruction

**2026-11-18.** Mother `PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905`; Task `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`. **Status: AUTHOR-PROVED / EXACT-FINITE-EXECUTED / UNREVIEWED / NOT_ADMITTED.** This is a direct continuation of saved Unit112 rather than a repeated N25 shell count.

## Exact theorem: at most two native depths after fixing squared norm

Let `Z³` be one **selected signed three-axis sub-torsor of frozen native X6**, with `G(z)=z_1²+z_2²+z_3²`; `rho(z)=z-min(z)(1,1,1)` is the relative/min-zero observer, not a native Cell address. Let `N >= 0` be an **exact known integer** and `q in N_0³` satisfy `min(q)=0`. All native coordinates in the joint fiber

`F_N(q)={z in Z³ : G(z)=N and rho(z)=q}`

are precisely `z=q+h(1,1,1)`, where **integer** `h` is a root of

`3h²+2 s h+G(q)-N=0`, `s=q_1+q_2+q_3`.

Define `D=s²-3(G(q)-N)`. If `D<0` or `D` is not a square, the fiber is empty. Otherwise, every allowed depth is one of

`h_±=(-s±sqrt(D))/3`, **only when the numerator is divisible by 3**.

Consequently, **for every N and q, |F_N(q)| <= 2**. The two branch labels are enough to recover a spatial signed Cell displacement once `q,N` and the fixed coordinate frame are supplied. An additional **one bit is sufficient** for this particular spatial recovery task, and one bit is **sometimes necessary**, as proved below. This is not an unrestricted result on full decorated packet state or all possible future transition histories.

**Proof.** By definition, `rho(z)=q` exactly when `z=q+h1`, `h=min(z)`, and `min(q)=0`. Expanding the three squared coordinates gives the displayed quadratic. It has at most two real, hence two integer, roots. Conversely every permitted integer root constructs a native displacement in the specified fiber, so the formula enumerates the **complete** fiber with no hidden choice.

### Universal modular injectivity subclass

For **every** `N≡1 (mod 3)`, `rho` is injective when restricted to the full fixed native shell `{z:G(z)=N}`. Indeed each component square is 0 or 1 mod 3, so exactly one of the three coordinates is nonzero mod 3. Hence `S(z)=z_1+z_2+z_3` is nonzero mod 3. If `rho(x)=rho(y)` and `G(x)=G(y)`, then `y=x+k1` and `0=k(2S(x)+3k)`. For `k≠0` the latter forces `3|S(x)`, a contradiction. This gives a general explanation for the previously saved Unit112 `N=25≡1` injection.

### Sharp N=9 obstruction: norm plus observer cannot determine native BRC

The two different native displacements

`x=(-3,0,0)`, `y=(-1,2,2)`

both obey `G(x)=G(y)=9`, and have the **same min-zero readout** `rho(x)=rho(y)=(0,3,3)`; their common readout's exact depth roots are `h=-3,-1`. Yet their native shortest signed primitive path multiplicities are

`B_min(x)=3!/(3!0!0!)=1`, `B_min(y)=5!/(1!2!2!)=30`.

Therefore **no function of just `(rho(z),G(z))` can equal the true native N-BRC shortest-word count on all signed three-axis displacements**. Unlike Unit112's norm25 example, this is a genuine *same readout AND same native norm* two-point fiber. A branch bit distinguishes the two native coordinates; equivalently retain full signed common depth `h`. This is an exact, source-preserving obstruction to LP023/LP017-style attempts to recover native path counts by a quotient-only observer.

The sharp one-bit statement concerns only *coordinates and endpoint-derived shortest counts* under declared `(rho,N)`; it does not certify erasure of labeled trajectory histories, signed branch provenance, interaction data, or safe future operations. When `N` changes after a native step, current depth/readout may need to be recomputed.

## Executed finite certificate

The independent opt-in Python program `research_checks/X6_UNIT113_FIXED_NORM_OBSERVER_DEPTH_FIBER_BRC_CHECK_20261118.py` (SHA256 `af642e574c1ba1b8eefdc2034bd029e1eaccfd47222819dde713a27e280e6c3c`, Git blob `444421a2c6ecf02dc5c5847ed6deca37f9f437f3`) exhausts all 9,261 lattice triples in `[-10,10]^3`, retaining exactly all shells for `N=0,1,...,100`. It checks 3,576 observer fibers and exact quadratic depth-root reconstruction, the max-two bound, all mod-three-one shell injections, and all native BRC values. CPython ordinary, `-O` and `-OO` each executed successfully with byte-identical JSON output SHA256 `20789773cdde2b60f312dbd998f1617a01619650e4a35045a0b57b7f08ea75fd`. Every assertion is an always-on conditional.

For `N=9`: 30 signed native Cell displacements, 24 different relative observer images, 6 two-depth fibers, **6 fibers with nonconstant BRC**. For `N=25`: 30 signed displacements, 30 observer images, no depth alias, consistently reusing Unit112's recorded result. Over `0 <= N <=100` the maximum fiber size is 2. The **first N** in this fully exhaustively checked nonnegative interval with a BRC-inconsistent fiber is **9** (and the interval contains all smaller nonnegative N). The `N=9` witness above proves non-descent independently of the finite sweep.

The report's algebraic fiber theorem and the `N≡1 (mod 3)` injectivity theorem are **universal inside their declared signed-Z³ model**; the 0..100 numerical prevalence counts are finite only, not an extrapolated density or a theorem about other dimensions.

## Frozen provenance and required downstream interpretation

- P000 V5 at `awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03` fixes native `Z^6` signed Cell torsor, selected signed three-axis slice and exact component sum of squares. The relative min-zero observer and lossless common-depth reconstruction are in `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md` at that pin, blob `b4d49a1bbcccad0521618c6d20f6dcfa242b420a`.
- Joint observer preservation constraint `definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json`, blob `3923890d77a02d84b772f789e6912dd14f220d14`, requires a future-operation safe certificate before discarding joint/depth/path data.
- Original 28-claim ledger `a0bfa8eace20b061f5b228c733acdc46221388d7:research_artifacts/X6_LEGACY_PLANE_RECONCILIATION/claim_ledger.json`, blob `5881055c0801ca5bb0970756d500daa0114d36b0`, and existing 28-row action map `research_notes/X6_LP28_SOURCE_CONSUMER_ACTION_CROSSWALK_20261112_ONHOUR_1400.md` remain the claim/source ledger. This unit upgrades the **mathematical downstream decision** for LP003/LP005/LP017/LP019/LP023 without asserting that an unlocated old wrong caller was found.
- Unit112 scoped theorem: `N25` min-zero observer is injective on the shell, but naive observer path mass `3699` differs from native `846`, and the positive-section nine cells give `213`. Unit113 refines this by describing **every** fixed-norm relative fiber and producing a two-point same-norm BRC obstruction at `N9`. No earlier proof or original R063 C3/C4 test was rerun.

**Next scientific action:** inspect actual LP023 / LP017 native endpoint consumers using `(rho,N)` or a fixed norm/readout as if it determines native signed BRC. For an evidenced current consumer, give precise `commit:path:line`, preserve full signed/depth/path labels and perform targeted original-input regression. Keep LP011/LP019 asserted historical wrong-source citations `UNRESOLVED_PROVENANCE`; independent Driver `REQUEST_REVISION` and R063 same-object native replay support Issue #2416 remain distinct and pending. Author validation is **not** an independent review or native Result/admission.
