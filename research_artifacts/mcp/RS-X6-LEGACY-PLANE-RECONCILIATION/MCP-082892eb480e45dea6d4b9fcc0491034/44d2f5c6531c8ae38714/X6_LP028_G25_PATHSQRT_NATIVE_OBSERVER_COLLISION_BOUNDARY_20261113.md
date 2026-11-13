# X6 LP028: full-G25 observer fibers versus actual R063/PathSqrt pair-chart consumers

Date: 2026-11-13. Parent Task: `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`. Research logical lane `chatgpt-research-onhour-enterprise-math-20260923`. Authorship continued from existing researcher `EM-X6-FB6990`, Source-backed session `MCP-082892eb480e45dea6d4b9fcc0491034`. **AUTHOR-PROVED / EXACT LOCAL CHECK EXECUTED / UNREVIEWED / NOT_ADMITTED.**

## Exact new consumer-boundary proposition

Under the frozen P000 V5 signed primitive-axis `Z^6` affine displacement and square norm `G(z)=Σ_i z_i²`, let `S25={z:G(z)=25}`, `rho(z)=z-min(z)*(1,1,1,1,1,1)`, and `B(z)=T!/(Π_i |z_i|!)` for `T=Σ_i|z_i|`. Denote by `U25` the **union of the signed fixed-two-axis PathSqrt/R063 native endpoint images**, with zero coordinates admitted.

**Proposition.** The map `rho:U25 -> rho(S25)` has 132 distinct values, each with a **singleton fiber even when the fiber is computed in all of S25**. Thus none of the 132 actual pair-chart native displacements is confused with an additional higher-support native G25 endpoint by the min-zero relative observer. Their de-duplicated shortest signed primitive-word BRC mass is 4,212.

**Proof.** Existing exact G25 shell decomposition gives the five absolute-coordinate types `(5)`, `(4,3)`, `(4,2,2,1)`, `(3,2,2,2,2)`, `(3,3,2,1,1,1)`. Pair-support `U25` consists of exactly the first two types: 12 signed axial endpoints and 120 signed two-axis endpoints. The R063 positive ordered roots are `(0,5),(3,4),(4,3),(5,0)`, and the native pair-chart embedding yields the same 132 endpoints with mass `12*1+120*35=4212`.

If distinct `z,w ∈ S25` have `rho(z)=rho(w)`, then after swapping them `w=z+kD` for an integer `k>0`, `D=(1,1,1,1,1,1)`. Equality of square norms gives `2k Σ_i z_i+6k²=0` and hence `Σ_i z_i=-3k`. Because `Σ_i z_i ≡ G(z)=25 (mod 2)`, `k` is odd; and Cauchy-Schwarz gives `9k²=(Σ_i z_i)² ≤ 6*25=150`. Consequently `k∈{1,3}`, forcing `Σ_i z_i∈{-3,-9}`.

For a signed axial G25 state, the component sum is `±5`. For a signed `(4,3)` state it is one of `±7,±1`. None equals `-3` or `-9`; thus a pair-chart endpoint cannot be one member of any nontrivial relative fiber in **the entire** S25. This proves the proposition without presuming that relative observers identify native cells or ordered paths.

## Executed finite certificate, including the complementary collision structure

An independently authored integer checker recursively enumerates the whole `G=25` signed six-axis shell, constructs the signed R063 two-axis chart union from the four positive ordered roots, and groups every full-shell endpoint by `rho`. Actual local execution (exit code 0) produced:

```
PASS_X6_LP028_G25_PATHSQRT_NATIVE_OBSERVER_COLLISION_BOUNDARY
full_native=7812; full_observers=6372; double_fibers=1440
collision_support=(4,6):1080,(5,6):360; depth_gaps=1:1080,3:360
current_R063_signed_pair_chart_endpoints=132; native_BRC=4212
pair_endpoints_with_global_observer_collision=0
scope=SIGNED_NATIVE_G25_ONLY; not full PathSqrt operator or Result review
```

The complete 1,440 double fibers split by support signatures as follows: exactly **1,080 with supports (4,6)** and **360 with supports (5,6)**. All 1,440 G25 pairs still have unequal positive BRC counts, as separately certified in the previously saved full-shell G25 fiber work. No positive signed-path multiplicity is cancelled on graph orientation. This test is an additional native/observer consumer boundary, not a re-run of the original X6 Cover or R2500 benchmark.

Executed 3,325-byte script SHA256 `17361b7a110025c45cfc938246fcd23b40b99dbdd97867001d8bc368828fef9d`, Git blob `aec58e8e0ebfc803138c74e02cc91967272274d2`. Its GitHub byte-identical source is `research_checks/X6_LP028_G25_PATHSQRT_NATIVE_OBSERVER_COLLISION_BOUNDARY_20261113.py` at commit `071ac3d18aae7d3ab17a74af8af60b5c8b2d4e5d` (connector readback verified).

## Actual caller/source disposition

Original current `research_checks/X6_LP028_R25_ORDERED_CHART_VS_SIGNED_NATIVE_FIBERS_20261113_1100.py`, observed blob `ac4e10220a8aa41c512b6c1afbe8504da6734c64`, declares signed **two-axis** support, 132 unique endpoints and 4,212 BRC words. The original `research_checks/X6_LP028_SIGNED_PATHSQRT_TYPED_CURRENT_CONSUMER_CHECK_20261112_2300.py`, observed blob `db46dde5a962b93b65775bf2b4d8f52d5e3f83b9`, retains all labelled axes, signs and native start Cell, then removes only repeated axial endpoints. Both currently preserve the required scope; **KEEP original implementations**. This round inspected both actual current bodies, but they were already covered in prior audit history and are not counted as two new uncovered consumers.

The new global-fiber boundary shows that a *hypothetical* future G25-only consumer which projects an R063 two-axis displacement to min-zero may restore its displacement uniquely within `S25`, while a consumer that projects **arbitrary** G25 endpoints cannot assume that property. Native start Cell, ordered word history and chart labels remain distinct types regardless.

Other observed current consumers `research_checks/X6_LP028_R2500_FULL_NATIVE_SHELL_20261112_ONHOUR.py` (blob `4cedddae1cafca1004d19b849bb626712c0caa82`) and `research_checks/X6_LP028_NATIVE_NORM_PROBE_BRC_MINIMALITY_20261112_ONHOUR.py` (blob `365f1c59271be86b28a0d57b7480ccc806d8c8db`) explicitly distinguish full-shell combinatorics and native norm probes at their inspected statements. No new demonstrated mistyped native/observer call in these locations. Reading code is not a rerun of their original checker.

## Preserved mother-task frontier and next precise action

Task/source authority: `RS-X6-LEGACY-PLANE-RECONCILIATION` / `TP2-B4A441B23DA3159232C2`; frozen math `59538f585d037d09ef687b28715c4bc1a3f9fe03`; historical comparison `fd2bcff10ca6e147348b6c1236027fc0d2877df3`. Reuse old complete G25 five-orbit and 1,440-fiber certificates and original PathSqrt R063 fixed-axis proof; the new support-signature certificate adds a directly testable native/observer interface condition.

Original owned identity record: Researcher `EM-X6-FB6990`; SID `MCP-082892eb480e45dea6d4b9fcc0491034`; CLAIM `MCP-bdd4acf9d96a8f1f0dfab4e9`; RUN `RUN-756de85b94c23b46b181f7b8`. Latest prior resume request `onhour-20261113-1930-own-x6-resume-g3-progress-v1` is `SUCCEEDED`; any new Source mutation requires fresh authorization and its own receipt. Original G25 PROGRESS `onhour-20261113-1714-x6-native-g25-progress-v1` is `SUCCEEDED`.

The 28-LP current dependency ledger is not yet globally closed. The exact frozen pre-rebase LP011 alleged misselected native argmax and LP019 alleged positive BRC signed-cancellation caller locations remain `UNRESOLVED_PROVENANCE`. Next: read remaining frozen actual `experiments/` and `scripts/` call-sites against the existing 24-definition/7-executable exclusion boundary; provide precise found file/function/line or a bounded open residue to independent Driver `REQUEST_REVISION`. Preserve the author-side published G3/G25 notes and original run frontiers; do not redo completed native benchmarks. Source semantic progress/admission is separate from this GitHub report.
