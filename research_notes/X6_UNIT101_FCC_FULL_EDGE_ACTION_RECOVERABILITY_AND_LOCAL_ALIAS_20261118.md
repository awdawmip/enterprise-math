# X6 Unit101 — Full FCC six-edge actions recover orientation; single-edge readouts do not

**Date:** 2026-11-18 (Asia/Hong_Kong). **Mother task:** `RS-X6-LEGACY-PLANE-RECONCILIATION` / `TP2-B4A441B23DA3159232C2`. **Historical input pin:** `fd2bcff10ca6e147348b6c1236027fc0d2877df3`. **P000 scientific premise:** frozen V5 `59538f585d037d09ef687b28715c4bc1a3f9fe03`.

**Status:** AUTHOR-PROVED / EXACT-INTEGER-EXECUTED / UNREVIEWED / NOT_ADMITTED. This theorem concerns only the derived three-dimensional FCC carrier representation, with six named carrier lines; it makes no transfer to P000's six primitive axes.

## A genuine correction to Unit100's data-loss interpretation

The preceding Unit100 proved that forgetting a *single signed carrier image* down to its unoriented line target loses a sign: `M=diag(-1,-1,1)` fixes the AB line but sends the vector `+AB` to `-AB`. The correct recoverability boundary is finer: the **entire six-edge permutation** `eact(M)` is faithful on the frozen 24-element rotation group. Accordingly, a receiver retaining that entire valid group action can reconstruct all six signs, even though a receiver retaining only one edge's image cannot. Treat this as a type refinement of Unit100, preserving its local witness and original proof.

Let `E=(AB,AC,AD,BC,BD,CD)` carry the frozen FCC vectors `((1,1,0),(1,0,1),(0,1,-1),(0,1,1),(1,0,-1),(1,-1,0))`. Let `G` consist of the 24 determinant-positive signed coordinate permutation matrices in dimension three. Define `u(M)` as the permutation of the six unoriented lines, and `s(M)=(target_index, orientation_sign)` as the full signed carrier action. Define `U=u(G)`, **a 24-element subgroup of** `Sym(6)`, rather than arbitrary six-coordinate permutations.

### Exact theorem — full-action recoverability and projection ambiguity

**(A)** There is a unique map `L:U -> SignedCarrierActions(E)` with `L(u(M))=s(M)` for all `M in G`. It respects multiplication: `L(uv)=L(u)L(v)` for `u,v in U`, with the usual right-first convention. The signed information is recoverable *from the complete six-edge action, the fixed FCC vector catalog and membership in this 24-element group*.

**(B)** For each source carrier `i` and target unoriented line `j`, precisely four elements of `G` satisfy `u(M)(i)=j`; two send the oriented source vector to `+v_j` and two send it to `-v_j`. Thus the **single-edge readout** `(i,j)` carries an exact two-versus-two sign ambiguity. No deterministic sign recovery exists from that readout alone.

**Proof.** The pinned historical `P000_6D_AXIS_MIXING_ROTATION_ALGEBRA_CHECK_20260829.py` lines 56–71 identifies all 24 source rotations with 24 distinct full six-edge permutations, so `u` is a bijection between `G` and `U`. Its inverse exists and `L=s\circ u^{-1}` is unique. Both `u` and `s` preserve matrix multiplication, hence so does `L`. For (B), the action on six unoriented lines is transitive; a source-to-target fiber has size `24/6=4`. The finite exact checker establishes for all 36 ordered source/target pairs that the sign split is `(2 positive, 2 negative)`. Equivalently, each line stabilizer contains the reversal `diag(-1,-1,1)` conjugated to the selected carrier, pairing opposite signs. This completes the finite-domain certificate; the source's determinant and signed-vector formulas specify that domain exactly.

**Minimal local witness:** `I` and `diag(-1,-1,1)` both send the unoriented AB line to AB, while sending `+AB` to `+AB` and `-AB`, respectively. Their *complete* six-edge permutations are distinct, as required by (A).

## Actual independent execution

The standalone standard-library Python checker was executed in normal Python, `-O`, and `-OO`; stdout bytes were identical. The exact results are:

| Defined finite object/check | Result |
|---|---:|
| Matrices of G | 24 |
| Full six-edge permutations | 24 |
| Full signed carrier actions | 24 |
| Complete-action lookup collisions | 0 |
| Ordered single-edge source/target pairs | 36 |
| Sign counts per such pair | 2 positive, 2 negative |
| Group composition pairs | 576 |
| Signed basis-image equalities | 3,456 |

Checker SHA256: `c3c41c218da54745fffcbdfbdc7756480bd94fb2f054b6ab3adeea072d3e9875`. Result JSON SHA256: `6b5a5b6fb1630859d6d575df740843ef7ba159999716a36e57e94fcb3acee5b7`. The checker and certificate have Git blobs `9599e2d0ca4d1faf43eaa8c6e92539927c836775` and `4bf2fe437ec234f69dbcf5704db21968331fa428`, respectively.

## Consumer-level source audit

Seventeen exact frozen `research_checks/P000_*.py` files were read from `fd2bcff1` in this turn, with functions, line numbers and content inspected. In the source `P000_6D_AXIS_MIXING_ROTATION_ALGEBRA_CHECK_20260829.py`, `eact` is defined at lines 16–17, the full 24-element action is checked at lines 56–71, and the later consumers at lines 75–117 use this complete six-index permutation. The source makes no native six-axis rotation claim.

Two independently defined derived-carrier consumers also retain a complete six-edge permutation: `P000_S4_LIFT_UNIVERSALITY_EXTENSION_V13_CHECK_20260830.py` lines 74–93 (`edge_action`, `AXIS_GROUP`, kernel check), and `P000_LOCAL_TO_GLOBAL_BACKGROUND_EQUIVARIANCE_V18_CHECK_20260831.py` lines 15–20, 42–43, 66–82 (`eperm`, `EA`). These are *reconstructed* edge actions in separate source modules rather than imports from the original `eact` implementation. No checked consumer was found to feed only one unoriented edge target into a signed-carrier operation.

**Typed integration rule:** A complete `u in U` together with the exact catalog/rotation-domain pin is sufficient for the derived FCC signed reconstruction. A partial edge target, an arbitrary permutation in `Sym(6)\setminus U`, or a native X6 axis operator requires a separate typed bridge or explicit sign data. A failure of this predicate is evidence of a potential interface bug only when a concrete live caller relies on unsupported sign reconstruction.

## Task follow-up

The positive result refines the source audit criterion for remaining 28-LP graph work: before claiming lost sign, verify whether a theorem-facing consumer retains the *entire* faithful group element or projects to a single edge. Continue exact historical LP011/LP019 provenance search at the actual frozen source lines; existing allegations remain `UNRESOLVED_PROVENANCE`. Do not rerun the original R063/Helly native benchmark. Existing independent Driver `REQUEST_REVISION` remains with the Driver.

The original session `MCP-082892eb480e45dea6d4b9fcc0491034` was recovered read-only; continuation request `onhour-20261118-0106-x6-exact-current-cont-v1` reached `SUCCEEDED/TYPED_FRONTIER_REQUIRED`, but projection reported `execution_authorized=false`. This research artifact and its Activity reference do not claim a new native winning CLAIM or semantic checkpoint.
