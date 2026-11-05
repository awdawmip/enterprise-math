# PREFIX-517 — C6 BRC observer-safe indexed Cell visitation: minimal collision and history lift

Date: 2026-11-05 (Asia/Shanghai). Evidence: AUTHOR_PROVED / EXACT_FINITE_CHECKED / UNREVIEWED / NOT_ADMITTED.
Task linkage: `RS-X6-NATIVE-ROTATION-DYNAMICS`; independent author-side, no formal CLAIM asserted.
Frozen scientific pin: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`.

## Research problem and scoped carrier

Can `(Gamma^A, previous/current phase, STAR frame)` from PREFIX-516 answer, for every historical macroedge r, which native intermediate Cell its two-step microtrace visited? We work inside the frozen selected STAR `S_B={L1,L4,L5}` embedded in six signed native axes at zero-based axes (0,3,4). Relative chart positions are referenced to one **chosen Cell**, not a universal origin. The six signed phase Cells are

`a_0=+e_0,a_1=-e_4,a_2=+e_3,a_3=-e_0,a_4=+e_4,a_5=-e_3`.

For each r, frozen shortest microtraces are `I_r=(-a_r,a_{r+1})` and `O_r=(a_{r+1},-a_r)`. Their midpoint Cells are respectively the chosen pivot `0` and `a_r+a_{r+1}`. The full ordered branch string is `beta=(beta_0,...,beta_{6m-1}) in {0,1}^{6m}` for m closed cycles. Query `Q_r(beta)` returns the midpoint Cell visited at the r-th macroedge. The declared future operations are concatenation of complete native macroedge paths, exact BRC signature readouts, and these indexed visitation queries.

`Gamma_g` is PREFIX-515's `(n,y,V,W,T_g,T_g^rev,first,last)`; `Gamma_g^A=(Gamma_g,A)` adds PREFIX-516's 15 signed exterior-square area components. Both KMP gate words `aab` and `aba` use the established five-color observation. The population is labeled native branch histories; no quotient erases multiplicity or intermediate Cell provenance.

## Theorem 1 — A minimal two-flip counterexample within one complete C6 loop

Set `beta=(1,0,0,0,0,0)` and `beta'=(0,0,0,1,0,0)`; their native words are respectively

`EAedDAaeEDda` and `AEedDAeaEDda`.

For **both** `g=aab` and `g=aba`, direct exact evaluation yields the identical full observer:

`n=12, y=(0,0,0,0,0,0), V=6, W=2, T_g=(1,1,1,1), T_g^rev=(0,0,0,0), first=last=N`,

and `A_{0,4}=-2`, all other 14 wedge coordinates zero. Their initial phase, final phase and STAR frame are identical. Nevertheless at r=0 the first word visits outer midpoint `(+1,0,0,0,-1,0)` while the second visits the chosen pivot; at r=3 the roles reverse and the other outer midpoint is `(-1,0,0,0,+1,0)`. Hence the candidate joint observer does not factor the indexed historical Cell visitation readout, even within one STAR. A global four-STAR sufficiency statement containing this subfamily must therefore retain more information.

**Minimal Hamming distance within a fixed six-macroedge circuit:** for every edge, flipping exactly one `beta_r` changes total oriented area by the nonzero vector `Delta_r=2 a_r wedge a_{r+1}`. Therefore any same-area (and hence same-`Gamma^A`) distinct pair has Hamming distance at least two; the displayed two-flip pair attains it because `Delta_{r+3}=Delta_r` with opposite bit changes. This minimality concerns branch-flip distance, not earliest possible path length among arbitrary non-C6 paths.

## Theorem 2 — Exact indexed-midpoint recovery and optimal information scale

For fixed phase schedule and frame, the r-th midpoint Cell is `0` iff `beta_r=0`; if `beta_r=1` it is `a_r+a_{r+1}`, which is a nonzero signed native X6 Cell because distinct axes support the two phases. Thus `(Q_0,...,Q_{6m-1})` and the branch word `beta` are in exact bijection. The typed extension

`Gamma_g^{A,H}(w)=(Gamma_g^A(w), frame, first_phase, beta)`

therefore recovers all indexed intermediate Cells, preserves labeled BRC source multiplicity, and can be concatenated by appending the ordered bit strings while tracking the phase/frame boundary. For the stated fixed C6 phase schedule, the information lower bound for any exact encoding that answers **all** indexed visit queries is `log2(2^{6m})=6m` bits on the uniformly distributed complete branch history; the binary branch string attains the bound. This is a total-history lower bound, not an assertion that 6m *additional* bits are needed when `Gamma^A` is retained.

The same conclusion gives a useful narrower compressed observer: when only **ever-visited Cell membership** is asked, an ordered trace is unnecessary. Define `U(w)` as the set of visited intermediate Cell offsets relative to the initial native Cell of a **complete-macroedge** word w. Then for two concatenable microtrace sequences `u,v`,

`U(uv)=U(u) union (y(u)+U(v))`.

This follows because the intermediate positions in v are translated by the endpoint displacement of u; it is a semidirect, associative composition law alongside `y(uv)=y(u)+y(v)`. The set is sufficient for unordered membership but not for indexed-time queries. Where the atlas supplies a signed-axis frame transformation `F`, coordinate transport is `U -> F(U)` and `y -> F(y)` on this carrier. Actual permitted cross-STAR transitions remain to be proved from their native source, not assumed by this algebraic identity.

## Proof notes and finite certificate

PREFIX-516 proves `A(beta)=m A_0 + sum_r beta_r Delta_r` and `Delta_{r+3}=Delta_r`; this supplies Theorem 1's area equality and single-flip lower bound. The two explicit signed words can be checked directly against the full KMP transition *functions*, their reverse transition functions, BRC pair counts, and all 15 area components; the published JavaScript independently evaluates each. Theorem 2 follows from the distinct, declared inner/outer native midpoint Cells, plus the exact translated-prefix identity for concatenation.

Execute `node research_notes/portable_direct/prefix517_c6_visit_lift_certificate.js`. The exact-integer program enumerates all 64 C6 histories at m=1 and all 4096 histories at m=2 for **each** gate, verifying both `Gamma^A` fibers, indexed visit recovery, all single-flip area changes, and midpoint-set concatenation at a fixed split. Its observed counts are:

| m | labeled histories | area classes | full Gamma^A classes | Gamma^A fibers ambiguous for indexed visits |
|---|---:|---:|---:|---:|
| 1 | 64 | 27 | 36 | 20 |
| 2 | 4096 | 125 | 200 | 184 |

Counts are identical for `aab` and `aba` in this scoped C6 family. The program returns `ALL_CHECKS_PASS`. Infinite-m statements are from exact symbolic proofs, not from extrapolating this enumeration.

## Research scope and next dependency

This is a typed native-X6/C6/BRC observer result under the frozen STAR microtrace realization. It does not select or validate a unique physical path among branches. The remaining mother-objective dependency is to read the frozen four-STAR transition relations and construct or refute a frame-covariant associative `(Gamma^A,H,U)` transport across admissible STAR switches, preserving when/whether a pivot is a Cell or carrier incidence point. Compare the resulting state cost and exact BRC branch weights against the all-history representation.

Sources: frozen `research_notes/VIETE_X6_FIXED_RADIUS_MICROTRACE_C12_20260905.md`, current `research_notes/portable_direct/2026-11-05_prefix516_native_c6_exterior_area_brc_histogram.md` at `20fd31d31a54ade0f9089411527b00790dd7636a`; `p000_reality_foundation.json`; `definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json`; `docs/PORTABLE_RESEARCH_PROTOCOL.md`.
