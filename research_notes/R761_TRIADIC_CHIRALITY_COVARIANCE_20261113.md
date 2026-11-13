# R761 — S6-covariant triadic port dynamics: a chirality obstruction, exact repair, and A6 reachability

Date: 2026-11-13 (Asia/Shanghai). Research mode: author-side mathematical candidate in RS-X6-TRIADIC-CLOSURE-DYNAMICS, task publication TP2-8B7E13C5904A2D6F1142. Immutable science pin: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Builds on R758P–R760 (most recently Draft PR #2225, ef6229435addf0cf99142f66f424ca56c6856056). No change to protected P000, the ACTIVE worldview, or task scientific inputs.

## 1. Explicit candidate: primitive three-token event on six native port names

Fix an affine X6 Cell c, six positive native-axis port names I={0,1,2,3,4,5}, and equal positive quantum q. Distinct axes satisfy P000's native PERP_E relation, whose native angle is 120 degrees; no Euclidean vector-sum-zero condition is used.

A typed token comprises (Cell c, port i, q, immutable provenance label lambda, event time t). Distinct provenance labels are assumed for the distinguishing and exact recovery statements. An oriented triadic input comprises three tokens at one Cell on distinct positive ports a,b,d, equal quantum q, and one explicit cyclic orientation [a,b,d] (up to cyclic rotation). Thus the two orientations of an unordered triple are distinct event inputs, not silently merged. We provisionally name its candidate local event C_E^+; whether the source's true native force incidence/admission accepts it remains a separate scientific question.

Define the local relational port operation on token labels:

  T_[a,b,d](lambda_a,lambda_b,lambda_d)=(lambda_d,lambda_a,lambda_b).

All other port slots remain unchanged; token identity, common Cell and q are preserved, and event time advances once. The reversed orientation defines the inverse three-cycle. The six-token network and sequences involving multiple triadic events are explicitly nonprimitive composites, represented by a provenance-preserving ordered event history. Each individual candidate event contains exactly three nonzero quantum tokens; no fourth primitive balanced force is inferred.

The S6 action here is an action by renaming the six native-axis port identifiers together with their attached labels. This is a test of the declared six-axis permutation/rotation skeleton's indexing covariance. It is not a claim that all 720 relabelings have been shown to be admissible physical native rotations.

## 2. Exact obstruction to constructing an orientation-free local event

Let U be the 20 unordered 3-element supports drawn from I; let O be the 40 cyclically oriented triples, two per support. Write p:O -> U for forgetting chirality.

**Theorem A (equivariant-section obstruction).** No S6-equivariant section s:U -> O exists. Furthermore, any S6-equivariant map F:U -> S6 for which F(S) changes only slots inside S must satisfy F(S)=identity for every support S.

**Proof.** Fix S={a,b,d}. The stabilizer Stab(S)=S3(S) x S3(I\S) acts on S with its full symmetric group. A transposition of a,b fixes the unordered S but exchanges its two cyclic orientations. If s were equivariant, s(S) would have to remain fixed under this transposition, which neither orientation does. Hence no section. For the stronger assertion F(S) must commute with all permutations of S and simultaneously belong to the subgroup S3(S) of permutations supported on S. The center Z(S3) is trivial, hence F(S)=e. S6 acts transitively on U, giving the same result for every support. QED.

**Sharp source repair.** If the current coarse observer retains only (Cell, q, unordered support, unordered token provenance labels) and future readouts can ask which label occupies an individual port after this event, the two orientations are distinguishable whenever the three labels differ. One bit of chirality beyond that particular unordered-support observer is both necessary (two distinct outcomes in one observer fiber) and sufficient (one binary orientation choice). It is an internal source coordinate. Existing typed provenance may already supply that bit, so no new spatial direction or duplicate state is required. This result is scoped to this observer and future port-label readout.

## 3. Constructive source-preserving covariance

**Theorem B (exact covariance and reversibility).** For every permutation sigma in S6 of port names,

  T_(sigma*[a,b,d]) = sigma T_[a,b,d] sigma^{-1}.

Also T_[a,b,d]^3=e, and swapping the cyclic orientation reverses the event permutation.

**Proof.** The event's positional assignments are a<-d, b<-a, d<-b. Under any renaming sigma, exactly these three substitutions are carried to sigma(a)<-sigma(d), sigma(b)<-sigma(a), sigma(d)<-sigma(b), which is conjugation by sigma. Rotating labels three times returns the input; reversing the cyclic order swaps the direction, giving the inverse three-cycle. Each event is a bijection on full immutable token records. Retaining its support, orientation, event time and ordered source log makes its state transition exactly replayable and reversible. QED.

The S6 action on O is transitive. Each oriented triple's stabilizer comprises C3 rotations of its cyclic order, times arbitrary S3 permutations of the unused three ports. Its order is 3*6=18; orbit-stabilizer gives 6!/18=40 oriented triples. The unordered-support stabilizer has order 3!*3!=36 and 6!/36=20 supports.

## 4. Finite composite dynamics: A6 and a three-event upper bound

**Theorem C (port-permutation reachability).** In a fixed six-token composite configuration with all six distinct provenance labels and a legal alphabet *stipulated* to allow each of the 40 oriented local triadic operations, the subgroup of reachable port permutations is exactly A6, cardinality 360. Every reachable permutation can be expressed using at most three triadic updates, and some require three; the bound is relative to this complete oriented-event alphabet.

**Proof of group equality.** Each generator is a three-cycle, hence an even permutation, so the subgroup lies in A6. For every 3-element support, both orientations are available; these are exactly all 40 three-cycles on six symbols. The three-cycles generate A6, so the subgroup equals A6. The stated maximal minimal word length 3 is an exhaustive finite assertion verified by breadth-first search over all 360 group elements in the companion exact checker. It records the shortest length on first encounter and reaches a depth-3 state. QED.

For two overlapping supports {0,1,2} and {0,1,3}, their two oriented three-cycles generate A4 on four slots, of size 12, fixing slots 4,5. The checker proves this finite subgroup identity by enumerating its 12 members.

**Precise two-visible-port lift fiber.** For an observer that sees only unordered positive ports {a,b}, equal q and the same Cell, there are four candidate hidden third native positive-axis ports (the other four axes), yielding four unordered or eight oriented local triadic lifts. The additional source distinguishes both which hidden port was used and the orientation; branch and provenance multiplicity are kept. This is an explicit example of the P000-required type of triadic lifting within the declared candidate, and does not promote a two-force native equilibrium.

## 5. Exact verification scope and reusable tool

The file R761_VERIFY.py uses only Python standard library and integer permutation operations. It checks all 20 supports, 40 oriented triples, 720 S6 port-name relabelings times 40 candidate operations (28,800 exact covariance equalities), 20 full support stabilizers (36 elements each) and the identity-only local centralizer; it checks eight oriented lifts of each of the 15 unordered visible pairs. It checks inverse orientation, event order three, opposite-orientation outputs, the A4 group of order 12, the entire A6 group of order 360, and the maximum minimum generator depth of 3. Output R761_EVIDENCE.json is the actual script's exact result. These finite tests are exhaustive over the explicitly declared port-permutation candidate; the general obstruction and group identity also have direct algebraic proofs.

There is an important structural comparison with R759–R760: those researches defined an auxiliary seven-label star-transposition representation of **ordered signed spatial words**. The present candidate instead uses six **native-axis port slots** and provenance-preserving three-token incidence updates. A6 here is a port permutation group, not the earlier auxiliary A7 frame group. The distinction prevents substituting this construction for a native V29 PASS/TRANSFER or V39 frame transport without proving a source-preserving interface.

## 6. Current task frontier and a discriminating next experiment

First, read the frozen source definitions of PRIMITIVE_FORCE_QUANTUM, TRIADIC_CLOSURE_E, native Cell/Link/Port event admissibility, V29 PASS/TRANSFER and V39 based-loop transport, including actual rotation permissions. Define a typed source-to-candidate map only if each mapped triadic event is legal under the source's own predicates. Check preservation of (Cell, port, branch, signed incidence if applicable, quantum, event order and future observation), plus correct covariance for the *actual* native rotation subgroup. If an admissibility condition fails, retain an exact failure witness and revise the candidate interface without modifying P000.

A candidate-to-native simulation should test at least the two opposite orientations of one triple with distinct provenance labels and two overlapping triads. These distinguish source orientation, noncommuting composition, and third-force observability. A successful candidate calculation alone is not a native physical transport proof. Existing task owner/CLAIM, author Activity, formal Source Result and independent Driver review retain their actual independent control requirements.

**Result classification:** Proof of Theorems A/B and general generation claim C in the stated candidate algebra; exhaustive finite certificate for the A6 diameter and incidence counts; original native P000 force-event admission and V29/V39 mapping pending.
