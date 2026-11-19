# X6 Unit159 — Frozen triaxial exposed-kernel max and signed-trace consumer audit

**2026-11-19 · TASK_RESEARCH · RS-X6-LEGACY-PLANE-RECONCILIATION · TP2-B4A441B23DA3159232C2**

Researcher EM-X6-FB6990; genuine ordinary Research lane `chatgpt-research-onhour-enterprise-math-20260923`, SID `MCP-082892eb480e45dea6d4b9fcc0491034`. **AUTHOR_SOURCE_AUDITED / EXACT_INTEGER_CHECK_EXECUTED / UNREVIEWED / NOT_ADMITTED**. No independent Driver acceptance or P000 change.

## Immutable source and real production callgraph

Frozen historic comparison `fd2bcff10ca6e147348b6c1236027fc0d2877df3` (not rebasing task science `59538f585d037d09ef687b28715c4bc1a3f9fe03`):

- `src/enterprise_math/_triaxial_directional_defect_core.py`, blob `5261da8b9e7848ac5cce935f81d7e7e0381b210b`: `canonical_decode_xy` L24–26; `carrier_xy` L29–31; `declare_frame` L70–80; `convolve_kernels` L83–91; `diff1_kernel` L94–95; `triple_defect_kernel` L102–106; **`exposed_vertex_sampling_matrix` L331–357**, particularly `top=max(scores.values())` L337 applied to a Z² signed sparse-*kernel support*.
- `src/enterprise_math/triaxial_directional_defect.py`, blob `570088fb2a8dc1a19ada303d55ea1cb93718a0c7`, wrapper **`EXPOSED_AUGMENT` L198–216** calls `_core.exposed_vertex_sampling_matrix`, computes matrix rank and returns a certificate; `DECLARE_FRAME` L113–122 requires primitive min-zero seed.
- `tests/test_triaxial_directional_defect_integration.py`, blob `c92da7c8d87a7c0efae477151323435d2ff0f8ec`: actual **`test_exposed_augmentation_stays_unimodular_in_verified_characteristics` L76–82** calls the wrapper with seeds `((1,0,0),(2,1,0))`, domain radius 5 and characteristics 0,2,3,5,7; L23–32 also tests cyclic covariance and sign reversal; L42–50 checks eight trace states against six endpoint coefficients.

This is an actual producer → wrapper → test consumer, not a name-only search hit.

## Exact signed-trace identity and its observer type

Let the three derived Z² carrier directions of a canonical nonzero primitive frame be `u,v,w`, with `u+v+w=0`, all nonzero and pairwise distinct (as enforced by the frozen frame declaration). In the integer group ring of the endpoint carrier,
[
K=(X^u-1)(X^v-1)(X^w-1).
]
Expansion has **eight source-labeled trace states**. Empty and all-three masks both map to the carrier origin with coefficients `-1` and `+1`, hence cancel; the six remaining subsets have distinct endpoints `u,v,w,-u,-v,-w`, each coefficient `+1` for one-step and `-1` for two-step subsets. Therefore `K` has exactly six nonzero signed coefficients, `sum K = 0` and `sum |K| = 6`. This is exact for the declared frame domain, not merely an extrapolation of finite tests.

The negative coefficients encode a **signed finite-difference operator**. They are *not* subtractive counts in positive X6 N-BRC. The routine's `max` is an extremal **linear functional on Z² kernel-support positions**, needed for the unimodular exposed-vertex sampling construction. It is **not native X6 signed-axis argmax/dominance**. These source lines are verified correct under their declared derived-operator types and provide neither LP011's alleged wrong-native argmax caller nor LP019's alleged invalid positive BRC subtraction.

For the exact integration test seeds, independent convolution of the two six-position signed kernels gives 12 nonzero signed positions, total signed coefficient 0; the first frozen candidate `q=(1,2)` uniquely exposes point `(2,3)` with coefficient `+1`. These facts characterize the source code's exposed selection without claiming new functionality or rerunning the original integration suite.

## Native-to-carrier information firewall

The frozen `carrier_xy(a,b,c)=(a-c,b-c)` identifies `(0,0,0)` and `(1,1,1)` in the three-axis slice. Under frozen P000's actual six signed-native-axis Cell steps these extend to `z=(0,0,0,0,0,0)` and `z'=(1,1,1,0,0,0)`. Their native component squared-lengths are `G=0,3`, shortest-step lengths `N=0,3`, and shortest positive N-BRC word counts `1,6` respectively. Retain the native common-depth repair coordinate before using quotient values in downstream primitive updates, as already established by Unit152.

## Independent exact arithmetic and coverage

The attached standalone Python checker reconstructs the frozen **operator's declared algebra**, not the historical module's imports. It enumerated all 132 primitive min-zero seeds `0<=a,b,c<=8` with `gcd(|a-c|,|b-c|)=1`, checked closure and the exact 8-to-6 signed incidence coefficient certificate, checked the two-seed exposed kernel, and checked the native hidden-depth witness. Python normal, `-O`, `-OO` output the same one-line JSON, SHA256 `55bc66fd8d8e316f320ae2ec9a4d02bba26dd8ea67ba885f7599749b39e3e6ca` (newline included). Universal statement follows from the group-ring expansion and no-degeneracy conditions; 132 seeds are finite regression evidence.

This is the first actual review in this sequence of this specific `_triaxial_directional_defect_core.py` exposed-max caller and its wrapper/test chain; it does not supersede prior R062, Unit152, P022, or original R063 science. Scope is the three frozen source files and stated interfaces. Historical LP011 / LP019 alleged faulty `commit:path:line` remain **UNRESOLVED_PROVENANCE**. The remaining declared 28-LP production consumers, currently saved Units149–152 Native semantic associations, and independent Driver review remain open.

**Next exact scientific step:** inspect a genuinely uninspected historical/current production consumer expecting native Cell values or positive path counts, with frozen `commit:path:line`, and compare the input and returned type before deciding KEEP, RETYPE or REVISE. Do not use a separate derived support maximum or signed coefficient subtraction as a false-positive historical bug.
