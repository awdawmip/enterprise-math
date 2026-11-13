# X6 local C6: exact six-step BRC branch-fiber composition and spur-free census

Date: 2026-11-13. Author-side scoped research under native Researcher-ID `EM-DIRECT-3BBAC3`, Activity-ID `RA-2591AD545920200CEECEF5D6`. This is a symbolic exact N-BRC path-fiber theorem, not a formal Task Result/Review or an authenticated claim. Frozen X6 source: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`. Reuses, without re-proving, `research_notes/VIETE_X6_FIXED_RADIUS_MICROTRACE_C12_20260905.md` at that pin.

## Domain, semantics, and inputs

Work relative to one chosen native Cell pivot in signed X6. Choose any three distinct signed-axis labels i,j,k and one local chirality. In the restricted local C6 shell, take the six ordered shell phases

```text
a_0=+e_i, a_1=+e_j, a_2=+e_k,
a_3=-e_i, a_4=-e_j, a_5=-e_k, a_6=a_0.
```

Every adjacent pair a_r,b=a_(r+1) uses **distinct axes**. The already-proved exact shortest-path N-BRC fiber for the macro-transition a_r→b contains precisely two native primitive two-step realizations:

- INNER: `a_r -> 0 -> b`, pivot intermediate;
- OUTER: `a_r -> a_r+b -> b`, outward composite Cell intermediate.

They retain distinct branch labels, intermediate native Cells, signed axis-word order and provenance. No classical π or trigonometric numerical propagation is performed. Time is only separately typed step order; this finite microtrace theorem does not identify heartbeat duration or a physical rotation law.

## Theorem 1: associative exact N-BRC path-fiber composition

For a prescribed ordered sequence of m adjacent C6 macro-transitions `a_0->a_1->...->a_m`, keep the **tagged native Cell path** of each component, and concatenate paths at matching endpoints without erasing intermediate visits or cancelling reversals. The composite N-BRC fiber is the Cartesian product of the m two-element INNER/OUTER fibers, mapped by tagged concatenation. It has exactly `2^m` distinct length-`2m` native primitive paths.

Proof. Each 2-step component is a valid signed native-axis adjacency pair. Concatenation is valid since the terminal Cell of one component equals the initial Cell of the next. The intermediate Cell of each pair, at microstep index `2r+1`, is either zero or `a_r+a_(r+1)`, which is nonzero since axes differ. Thus the full path uniquely recovers each branch bit by examining those odd-index intermediate Cells. The map from binary words of length m to full path traces is injective and surjective by construction. Path concatenation is associative because concatenating finite ordered lists of primitive Cell edges is associative, with no quotient/cancellation. QED.

For the complete six-macro C6 return `a_0->...->a_6=a_0`, the raw tagged full fiber has `2^6=64` distinct closed native primitive 12-step paths. This recovers the previously proved all-OUTER 12-Cell cycle as **one** of 64 native realizations; the other 63 are distinct and cannot be silently removed from the unrestricted path observer.

## Theorem 2: cyclic nonbacktracking iff inner branches are nonadjacent

A primitive 12-step closed path is called **cyclically nonbacktracking** when no edge is immediately followed by its inverse, including across the final-to-first junction. For the six-macro N-BRC fiber just defined, cyclic nonbacktracking holds **if and only if no two cyclically consecutive branch flags are INNER**.

Proof. Within a component, the two signed elementary steps act on distinct axes and hence are never inverse. At a junction `a_r->a_(r+1)->a_(r+2)`, write `a=a_r,b=a_(r+1),c=a_(r+2)`. These are three different unsigned axis families in the displayed phase ordering. The last step of the first macro is either `+b` (INNER) or `-a` (OUTER); the first step of the next macro is either `-b` (INNER) or `+c` (OUTER). The only inverse pair is `+b,-b`, occurring exactly for INNER followed by INNER. The same analysis applies cyclically to the macro 5→0 junction. QED.

Consequently, spur-freeness is **not componentwise closed**: two separate legal, individually nonbacktracking two-step INNER paths can concatenate to form `0->b->0` at their shared shell Cell. This is an explicit composition counterexample to a branch-erasing simplification.

## Exact count

The nonbacktracking selections are the independent sets of the six-cycle graph `C_6`, with INNER positions as chosen vertices. By cardinality of independent sets on a cycle:

| Number of INNER branches | Cyclically nonbacktracking six-macro BRC traces |
|---:|---:|
| 0 | 1 |
| 1 | 6 |
| 2 | 9 |
| 3 | 2 |
| **Total** | **18** |

Indeed the adjacent-free k-subsets of C6 have counts `1,6,9,2`; no four vertices are pairwise nonadjacent. Thus precisely **18** of 64 closed native 12-step microtraces avoid immediate edge reversal, and **46** contain at least one spur. All-OUTER is the unique trajectory of this fiber with no pivot visit. Among cyclically nonbacktracking trajectories the pivot is visited precisely k times when the branch word has k isolated INNER choices.

For a full path-observing operation that distinguishes all 64 primitive traces, at least six binary bits of branch provenance are necessary and sufficient with the macro phase sequence fixed, by injectivity and the counting lower bound. If a separate future admissible law **restricts** the domain to the 18 nonbacktracking traces, at least five binary bits are necessary for a fixed-length code of those 18 alternatives. These bounds are explicitly observer/domain-specific, not a claim that every future rotation law has to retain these bits.

## Exact computational check

A small standard-library six-integer-coordinate enumerator (attached) exhausts all 64 branch words; each produces a distinct 13-vertex representation of a closed 12-primitive-edge path, every edge changes exactly one native signed axis by one, and cyclic no-backtracking status matches the consecutive-INNER criterion for all 64. The 18 satisfying trajectories have INNER-count histogram `{0:1,1:6,2:9,3:2}`; all-OUTER visits 12 distinct native Cells before return. All arithmetic is symbolic integer native adjacency and the **existing typed two-branch N-BRC shortest-path identity**, not an alternative classical dynamics calculation.

## Preservation horizon and remaining task

- Preserves full raw native path and BRC branch provenance under arbitrary composition of the declared local C6 macrosteps.
- Endpoint-only phase readout can quotient the 64 fibers to the same macro return, but intermediate pivot visits, cyclic backtracks, individual signed microsteps and history observers cannot.
- Does **not** demonstrate that a native physical law chooses the 18 nonbacktracking subset or the unique outer trace; it classifies each *conditional* domain exactly.
- Does not identify the global generated signed permutation group anew (previous exact result `G_all=(C2)^6 ⋊ A6`, order 23040, is available in Draft PR #2216). It does not equate those abstract signed-frame symmetries with physical native rotations.

**Next:** establish an operation-safe atlas transport and a typed BRC branch-selection rule from native triadic closure or another actual project-native condition, or return a sharp obstruction. Any candidate restriction must be checked against the retained primitive path and provenance observers.

Control context: canonical dispatch selected `RS-X6-NATIVE-ROTATION-DYNAMICS`; native continuation identified an expired predecessor and no active claim. This session's typed prepare request `em-r5-20261113-1754-x6-typed-prepare-01` failed with exact `ARTIFACT_HASH_MISMATCH` and was not replayed. This note is therefore **independently preserved author-side research**, not a task-authorized Result or TASK CLAIM.
