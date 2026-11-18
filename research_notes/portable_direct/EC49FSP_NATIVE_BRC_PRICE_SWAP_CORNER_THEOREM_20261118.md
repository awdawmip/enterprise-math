# EC49FSP — BRC16943 具名观察价格交换：尖锐边界后的精确四相图

Date: 2026-11-18. Independent portable research continuation of [EC49FSO PR #2708](https://github.com/awdawmip/enterprise-math/pull/2708), source commit \`b960bf6f1ed58fbc7eb7333183b38671f0330f1b\`. **Frozen scientific input:** \`fc0f038e7bfd12c886b4d37f900bfb770c0f61ab\`, unrebased. Formal task/CLAIM/Result authority is not asserted.

## Model and statement

Original native BRC16943: 310 configurations, 141 distinct **named joint-response profiles**, 228 **physically named** observations, uniform weight across the 141 profiles. All complete deterministic adaptive identification trees are allowed. For observation prices \((1-a)t,(1-b)t,(1-z)t\) on q32, q34, q140 respectively, all other observation prices \(t>0\), define \(F(a,b,z)=141V(a,b,z)/t\), where \(V\) is the unrestricted exact Bellman optimum.

Put \(A=31/64\), \(B=27/64\). Define \(D(z)=F(A,B,z)\) and \(S(z)=F(B,A,z)\). The following equalities hold for **every real** \(0\le z\le1/4\):

\[
D(z)=\begin{cases}
7053/32-4z,&0\le z\le1/6,\\
7085/32-10z,&1/6\le z\le1/4,
\end{cases}
\]

\[
S(z)=\begin{cases}
7053/32-10z,&0\le z\le51/448,\\
14157/64-17z,&51/448\le z\le1/6,\\
14285/64-29z,&1/6\le z\le11/48,\\
14329/64-32z,&11/48\le z\le1/4.
\end{cases}
\]

Consequently, the exact exchange penalty is

\[
D(z)-S(z)=
\begin{cases}
6z,&0\le z\le51/448,\\
13z-51/64,&51/448\le z\le1/6,\\
19z-115/64,&1/6\le z\le11/48,\\
22z-159/64,&11/48\le z\le1/4.
\end{cases}
\]

It is strictly increasing and positive for every \(z>0\), reaching exactly \(193/64\) at \(z=1/4\). There is a **synchronized slope change at \(z=1/6\)** for both orientations. The first boundary \(51/448\) agrees with EC49FSO; the complete classification of the subsequent native Bellman phases through \(1/4\) is this research increment.

## Complete source-native witness vectors

For a fully replayed native decision tree, let \(U\) count all internal named observation occurrences across the 141 paths and \(N_q\) count uses of q. Its cost is \(U-aN_{32}-bN_{34}-zN_{140}\). Six full lossless original-native witnesses, with ordered tuple \((U,N_{32},N_{34},N_{140})\), are:

| Orientation / z range | Native tree tuple | Canonical tree-JSON SHA256 |
|---|---|---|
| D: [0,1/6] | (306,141,41,4) | \`ad7047debd6d04d3c076eef6d593b7de4d50879a671a439760d4d436210cc767\` |
| D: [1/6,1/4] | (307,141,41,10) | \`8b5e58dba1a6ecab2d645e18745e6ddf5a1346a661c33351b7c1f0418d26f16c\` |
| S: [0,51/448] | (306,41,141,10) | \`db669e0116a1816bbf53fed6cb1bc07a4549ef9665637433e05c059936ff9742\` |
| S: [51/448,1/6] | (303,32,141,17) | \`c43c37dfca7f748b0e4acadcd69c8be5e8c5bdeb3a0515c6c7e8c796250042e2\` |
| S: [1/6,11/48] | (305,32,141,29) | \`99c8731a0e6499e70278318237d06576d3b347fb47e885b6467a2d82fd5541ec\` |
| S: [11/48,1/4] | (304,28,141,32) | \`df7cb044a0d2ac4a7bf6460b0b0311bbe352cfd1b695f1713a915b1e2e9b3ec1\` |

All six complete trees have been replayed across **141/141** original named profiles with exact original observation responses; each profile terminates at the correct singleton leaf and no observer repeats on one path. The complete JSON trees, native 94-family master, profile CSV, both original-data decoders, solver programs, execution logs and SHA256 manifest reside together in the accompanying self-contained research evidence bundle. Prior witnesses are reused byte-for-byte. This PR's machine certificate retains the coordinates, counts and hashes for independent revalidation.

## Exhaustive exact Bellman endpoints

The recurrence, for every non-singleton subset \(S\) of the 141 named profiles, is

\[
T(S)=\min_{q\in\{0,\dots,227\}\text{ splits }S}
\left(|S|(1-d_q)+\sum_r T(S\cap q^{-1}(r))\right),\qquad
T(\{s\})=0,
\]
with \(d_{32}=a\), \(d_{34}=b\), \(d_{140}=z\), other \(d_q=0\).

| Exact z | D Bellman value | S Bellman value |
|---|---|---|
| 0 | 7053/32 | 7053/32 |
| 51/448 | 49269/224 | 12279/56 |
| 1/6 | 21095/96 | 41927/192 |
| 11/48 | 21035/96 | 41579/192 |
| 1/4 | 7005/32 | 13817/64 |

**Proof of continuum coverage.** At every vertex of each **feasible-tree affine lower envelope** the exact unrestricted, original-all-228-observer Bellman optimum coincides with the envelope. Each fixed native tree remains feasible for every discount; its affine cost is an upper bound on \(F\). Conversely, \(F\) is the pointwise infimum of these affine costs, hence concave. On the interval between any adjacent verified envelope vertices, concavity gives the chord of endpoint optima as a lower bound; the appropriate exhibited complete tree gives that *same* chord as an upper bound. Equality follows at every real interior point. This proves the two formulae and their exact difference, including all phase boundaries. No float-grid inference is used.

The primary exact-bellman envelope algorithm discovered one new intermediate swapped tree at \(z=43/240\), which improves the provisional three-tree envelope by exactly \(144/960\); further vertex verification added no missing phase. Six separate **independent raw 94-family/CSV decoder** Bellman checks reproduced D at z=1/6 and 1/4, and S at z=51/448, 1/6, 11/48, 1/4. Fractions and denominators are exact throughout. The independent tests are implementation cross-checks, not an independent project review.

## Reproduction and deliverable

The actual completed self-contained package includes \`EC49FSP_EDGE_EXACT.py\` (full native 228-observer exact-envelope discovery), \`EC49FSP_VERIFY_INDEPENDENT.py\` (second source decoder), \`EC49FSP_CERTIFICATE_CHECK.py\` (fast exact checks), \`COMBINED_CERT.json\`, all six original named tree witnesses, frozen original source data, primary/secondary decoders, execution logs and SHA256 manifest. On extraction, the first two scripts run from the archive's \`EC49FSP/\` root with standard Python; the complete files are retained in the handoff package. The accompanying GitHub \`EC49FSP_NATIVE_BRC_EDGE_REPRO_20261118.py\` is a short, exact check of the published formulas.

**Scope:** AUTHOR_PROVED / EXACT_PRIMARY_FINITE_EXHAUSTIVE / INDEPENDENT_PARTIAL / NOT_REVIEWED. A finite model of named BRC observations and observer prices; no claimed physical timescale or universality beyond the quantified region. Historical Researcher \`EM-DIRECT-8454C6\`, SID \`MCP-44cfc4e6f2094f96861854ebefc77e84\`, Activity \`RA-ED136F89271FD89288F3E58D\`. Original continuation request ended \`FAILED / CANONICAL_REJECTED: unknown current immutable task publication\`; current session metadata still has \`execution_authorized=false\`, so this is independent portable scientific preservation, without a formal CLAIM, Result, Review or Activity checkpoint.

**Next:** certify a two-parameter neighborhood where \(b\) varies, starting with the candidate first crossing \(z=(9b-3)/7\), and then the three-parameter facet complex toward the q32/q34 diagonal \(a=b\). Neither geometric extension is claimed here.
