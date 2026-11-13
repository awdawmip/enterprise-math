# R751 — Six-step X6 triadic Path-formal BRC lift and exact exterior-area residual

**Date:** 2026-11-12 (Asia/Shanghai). **Researcher:** EM-X6-0E46B2. **Activity:** RA-98CE0270814B2431AD745438. **Parent:** RS-X6-TRIADIC-CLOSURE-DYNAMICS / TP2-8B7E13C5904A2D6F1142. **Status:** author theorem with complete finite X6 check; native V29 PASS/V39 transfer and independent Driver review remain open.

**Frozen scientific pin:** awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Consume P000-V5, definitions/P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md, definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md, definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json and the exact signed X6 Path-formal/N-BRC foundations (V17). R745–R750 are related author-side candidate results, not native event admission.

## 1. Typed question and candidate incidence

Let X be the native X6 affine Cell torsor for Z^6. Fix one Cell c (a chart anchor, not an ontic origin), and choose three *different* native axes i,j,k. Let p=s_i e_i, q=s_j e_j, r=s_k e_k, with s_i,s_j,s_k in {+1,-1}. The three typed primitive force Ports are attached to c by three distinct Links, with equal nonzero quantum, and retain their individual source IDs.

A directed incidence cycle [p,q,r] is a cyclic-order class: (p,q,r)~(q,r,p)~(r,p,q). Reversal [p,r,q] changes the orientation. This describes a **candidate Port-level TRIADIC_CLOSURE_E witness**, not a Cell-coordinate return: its admission as an actual V29/V39 native event is not asserted here. P000's triadic arity, PERP_E and 120-degree definition are premises, not conclusions; the present algebra does not replace them by Euclidean zero vector sum. All 20 axis triples, 8 signings and 2 cycle orientations are **320 syntactic candidate states**, not 320 proved physically legal native events.

## 2. Signed Path-formal BRC lift

A signed native path is an ordered word in the twelve P000 primitive step letters. The exact signed X6 BRC path-formal carrier retains each word and its branch identity, even when coordinate endpoints coincide. Define the three branch witnesses of [p,q,r] by

  W(p,q,r)=(p,q,r,-p,-q,-r),
  W(q,r,p)=(q,r,p,-q,-r,-p),
  W(r,p,q)=(r,p,q,-r,-p,-q).

These three **ordered BRC branches** are not identified, averaged or replaced by an N-BRC positive total. They arise from the three possible marks of the unmarked cyclic Port source. Each has exactly six primitive X6 moves, no adjacent inverse steps, visits all three axes and returns to its initial Cell.

**Sharp minimal-length lemma.** Any full native signed-axis Cell-coordinate-return path that uses all three distinct source axes contains at least one step of each sign on each of these axes, hence at least six steps. Each W realizes this bound. In particular, Port-level three-force closure is NOT identified with a 3-step coordinate return. The number six is a minimal coordinate-return witness length in this constructed class, not a new primitive-force arity or heartbeat period.

## 3. A proposed exact second-order Path-formal BRC observer

On an ordered word U=(u_1,...,u_m), define its signed displacement and exterior-area readout

  D(U)=sum_t u_t in Z^6,
  A(U)=sum_{t<v} u_t wedge u_v in Lambda^2(Z^6).

For concatenation U,V, a direct split of the ordered-pair sum gives

  D(UV)=D(U)+D(V),
  A(UV)=A(U)+A(V)+D(U) wedge D(V).                 (1)

Thus (D,A) is a precise, integral, order-sensitive **extension/readout of the already admitted signed Path-formal BRC word carrier**; it is not claimed to be an already installed BRC API. The wedge is exterior-algebra bookkeeping of signed path provenance, not a physical area, signed amplitude or probability.

For W(p,q,r), the first three moves contribute p∧q+p∧r+q∧r; the last three moves contribute the same, and their cross-pairs sum to (p+q+r)∧(-p-q-r)=0. Therefore

  A(W(p,q,r))=2(p∧q+p∧r+q∧r).                    (2)

Define the branch-summed cyclic signature, without discarding the original branches,

  S([p,q,r])=sum_{cyclic rotations} A(W) 
            =2(p∧q+q∧r+r∧p).                    (3)

It is independent of which Port is marked first. Reversal gives S([p,r,q])=-S([p,q,r]). Every signed axis permutation in S6 preserves this formula by the natural action on the exterior tensor:

  S([g p,g q,g r])=(Lambda^2 g) S([p,q,r]).      (4)

There is no claimed covariance for a rotation group strictly larger than the verified S6 axis-permutation skeleton.

## 4. Main exact fiber theorem: 320 oriented candidates -> 160 signatures

Fix the ordered axis labels i<j<k. For the forward cyclic order (p_i,p_j,p_k), (3) has precisely three nonzero entries

  S_ij=2 s_i s_j,  S_jk=2 s_j s_k,  S_ik=-2 s_i s_k.

For the reversed cyclic order, these three signs all reverse. Consequently

  S_ij S_ik S_jk = -8 * orientation,             (5)

where orientation is +1 for the increasing-axis cycle and -1 for its reverse. Formula (5) **decodes orientation from the signed second-order BRC observation alone** once the six native axis labels are identified.

Conversely, if two source configurations share the same S, the three nonzero wedge indices identify their unordered axis triple and (5) fixes orientation. The three signed pair products fix the signed source triple up to one simultaneous global sign reversal, and both signings do give the same S because wedge is quadratic. These are the only collisions.

**Theorem (exact fiber classification).** Over all 20 three-axis subsets of X6, 8 signed assignments and 2 orientations, S has exactly 160 distinct nonzero values, each with a fiber of exactly 2 source configurations. The two configurations differ by global simultaneous sign reversal (p,q,r)->(-p,-q,-r), and have identical orientation. The original 320 source configurations remain distinguishable by their retained signed Ports/branch IDs.

This is an exact **one-bit source-sign ambiguity** at the declared second-order observation, not an assertion that one bit is a universal minimum for all future native dynamics. Within the declared observer family the sign ambiguity is sharp; any admissible future test that reads an individual signed Port separates the two states. The first-order full return D(W)=0 cannot even decode the cycle orientation.

## 5. Complete finite certificate, independent checks and limits

The companion standalone Python standard-library verifier explicitly constructs all 320 signed oriented candidate cycles and their 960 six-step Path-formal branch witnesses. It checks word endpoints, no adjacent inverse pairs, three-axis support, the direct pair-sum definition of A against (3), orientation decoding (5), and all 160 two-element fibers. It then exhausts all 720 S6 permutations for each of the 320 states, for 230,400 exact covariance checks. All quantities are integers (not floating point or ordinary physical propagation).

Expected/observed certificate: R751_X6_TRIADIC_BRC_AREA_EXACT_PASS; oriented_states=320; six_step_closed_branch_witnesses=960; orientation_decoder_checks=320; signature_classes=160; fiber_two_classes=160; S6_covariance_checks=230400. An independent Python enumeration of the same specified finite domain agreed with these counts and formulas.

The all-X6 theorem is proved combinatorially here, with exhaustive verification of the full finite X6 candidate class. This does **not** constitute real V29 PASS or V39 transport execution, an admitted native TRIADIC_CLOSURE_E Cell/Link/Port event, physical area, continuous rotation or independent mathematical review. It does not bypass BRC-only arithmetic: the computation evaluates only typed signed Path-formal words and a newly defined exact integral provenance readout, with no pi/trigonometry, ordinary matrix propagator, Taylor/Padé/Cayley surrogate or physical residual attribution.

## 6. Smallest next native correspondence test

From the frozen task science and actual original V29 PASS/V39 source, identify one *legal* c:Cell, three equal-quanta Link/Port incidences, and one specified follow-on update U. Compare the two globally opposite signed-source triples with the same S, holding the complete declared Cell, Port, Link and branch data. Test whether the native update and the coarse S observer commute on that exact event family:

  S(U(x)) ?= F(S(x)), for a well-defined F.

If both signed-source variants are legal and their U-successors give different S or required downstream readouts, exhibit the smallest exact counterexample and retain the one-bit sign carrier; if a valid native operation class descends through S, prove the scope-specific fiber constancy including provenance queries. In either case preserve the separate triadic Port closure versus six-step coordinate return types. No blanket quotient or physical law is inferred.
