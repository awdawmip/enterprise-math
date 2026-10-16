# Existing Magma mixed pairing: exact input bridge and remaining evidence

Author: EM-DVR-F73673. Status: FROZEN_UNREVIEWED derived reuse/input note; no historical novelty, new shared Tool, Native vote, task publication or scientific invocation. External models below are rational elliptic curves, finite étale algebras and their classical cohomology. They do not alter the native affine-Z6 torsor/Cell substrate; time occurs only in execution provenance.

## 1. What was actually read

The official current Handbook, marked V2.29 / 3 August 2026, was reached through its chapter contents and read at the exact API sections, not inferred from an index alone:
https://magma.maths.usyd.edu.au/magma/handbook/text/1570
Sections: DescentMaps/TwoCover, Cassels–Tate, Four-Descent, Higher 2-power Isogeny Descents. Actual web responses are retained locally as MAGMA_EXACT_THREE_CURRENT_SECTIONS_ACTUAL.json and MAGMA_CURRENT_DESCENT_MAP_AND_BOUND_SECTION_ACTUAL.json. Official release 2.15 independently records the pre-existing mixed implementation:
https://magma.maths.usyd.edu.au/magma/releasenotes/2/15/

Compact API transcription (paraphrased; not an execution transcript): CasselsTatePairing(C,D), types Crv/CrvHyp, accepts everywhere locally soluble four-/two-coverings of the same rational elliptic curve, with C a quadric intersection. It returns an integer representing F2, hence a bit, not a Hilbert sign. FourDescent accepts a quartic or its hyperelliptic curve and returns four-coverings. AssociatedEllipticCurve can target a supplied isomorphic elliptic curve. TwoCover accepts a cubic étale algebra element. TwoPowerIsogenyDescentRankBound needs a specified rational two-torsion point when the choice is nonunique. Its ReturnFourCoverings option overrides Cutoff/MaxSteps and forces the requisite descent levels. Verbose names are CasselsTate, FourDescent and cbrank. The handbook does not promise a portable local-certificate export.

This identifies an existing mixed evaluator. It does not establish its presence, version, result or certificate coverage in this workspace.

## 2. Exact étale-algebra input, with root labels preserved

Let P>Q>0 be rational and let
E: y²=f(x)=x(x−P²)(x−Q²),
A=Q[t]/(f(t)).
The polynomial has three distinct roots, so evaluation in the fixed order
(0,P²,Q²) identifies A with Q³. For b∈Q*, define
L0(t)=(t−P²)(t−Q²)/(P²Q²),
d_b(t)=b+(1−b)L0(t).

Lemma. The element d_b is a unit, with ordered evaluations (1,b,b) and étale norm b². Its square class is therefore exactly the vertical class U_b in the usual kernel-of-norm description of H¹(Q,E[2]).

Proof. L0 is 1 at 0 and 0 at the other two roots. Hence evaluation gives the displayed triple; all entries are nonzero. The norm in the split algebra is their product b². Equality of the ordered triple establishes the desired cohomology class, rather than merely an isomorphic unlabelled Jacobian. Replacing b by bc² multiplies d_b componentwise by (1,c,c)², so this class depends only on b modulo rational squares. This is elementary CRT encoding of the existing descent representation, not a new descent algorithm. □

For the fixed new core (9,8), P=161, Q=127. The two intended elements are explicitly
d_2=2−L0 and d_3=3−2L0
in the SAME algebra with roots labelled (0,25921,16129). These formulae require no Selmer-group recomputation. The existing full all-place proof, not the norm condition alone, establishes that U2 and U3 belong to Sel²(E).

This encoding provides a prospective path through the documented TwoCover/DescentMaps machinery. No claim is made that a literal call has been tested, that an arbitrary quartic object carries the necessary internal attributes, or that an automatically chosen Jacobian isomorphism preserves our two-torsion labels.

## 3. Compatibility with the already frozen quartic

The separate 6482-byte note gives an explicit smooth genus-one model
Q3: R²=3Z⁴+84100Z²W²+31961088W⁴
and a labelled two-cover map to this exact E, identifying its Sel² class with U3. Its coefficients are strictly positive, so the quartic has no real, hence no rational, root; this avoids the rational-root exception in the documented FourDescent input description.

Two admissible preparation choices are therefore:
(a) carry Q3 together with its explicit labelled map, and verify compatibility of any software normalization with that map; or
(b) construct the U3 object from d_3 in the split cubic algebra, retain the returned map and exhibit the isomorphism to Q3 over E.
For the second argument, construct the U2 object from d_2 with the same labelled base E. A bare assertion that two Jacobians are isomorphic is insufficient: a nontrivial permutation of E[2] can change which U-class is being paired.

A future binding check must compare the induced Kummer classes/maps over E, preserve covering level, and record all rational change-of-variable maps. The minimal-model map and any deck/sign automorphism must be explicit or proved harmless. This is an evidence obligation, not an additional invented Native role gate.

## 4. Why only one lift and one mixed evaluation are needed

Use the already proved, separately reviewed full first Cassels form B=0 for this core, and the genuine Sel⁴→Sel² image theorem. There is an everywhere locally soluble four-cover c3 lifting U3. Any two lifts differ by i(w) for w∈W=Sel²(E). Their Cassels–Tate values against U2 differ by B(w,U2)=0. Therefore the bit
e=j(CT(q4(c3),q2(U2)))
is independent of which valid lift is selected. Alternating skew symmetry does not change a two-torsion-valued bit, so this equals the fixed beta(U2,U3) orientation of the earlier conditional paper.

Consequently one verified valid lift and one exact mixed evaluation suffice mathematically. There is no need to enumerate abstract Sel⁴ again, build a full mixed table, or evaluate all lifts merely to make this bit robust. This does not bound the internal cost of the existing FourDescent implementation or assert how many objects it will return.

If the implementation returns an empty lift set, that conflicts with the already established hypotheses/image result; it is an integrity or input-binding diagnostic. It must not be silently read as a fresh rank-zero certificate for this core. A failed computation, resource limit, missing map or incomplete local test leaves e UNKNOWN.

Conditional interpretation remains unchanged:
- e=1: rank(E/Q)=0 and Sha(E)[2∞]≅C4², by the separately proved one-bit theorem.
- e=0: this mixed test is exhausted; rank remains UNKNOWN in 0..2 and no larger descent is automatically authorized.
A certified rational nontorsion point found by any later authorized work would separately imply rank≥1 and hence force e=0; no such point is presently claimed.

## 5. Runtime, cost and portable evidence are still actual gaps

The metadata-only inventory EXISTING_RUNTIME_METADATA_ONLY_CAPABILITY_INVENTORY.json, observed 2026-10-16 04:31:03 UTC, found no magma, sage, gp, pari-gp or Singular on the current PATH. A bounded installation-name scan did not establish an alternative runtime. Docker client presence is not a Magma installation. No algebra interpreter, container, remote calculator or old fixed233 consumer was invoked. This is current limited environment evidence, not a permanent impossibility statement.

The recommended next reversible action is to bind an available licensed/existing runtime and inspect its exact version, installed help and export facilities without doing arithmetic. If unavailable, retain REUSE_IDENTIFIED_EXECUTION_UNAVAILABLE; do not rebuild a mixed-pairing tool family just because this environment lacks an executable.

Before a scientific invocation, a genuinely authorized researcher must freeze the exact runtime/binary or service identity, script/input/map digests, integer serialization/codec, total preparation and single-invocation budgets, full output/upload/storage/memory accounting, and the required independent static audit. Those are prospective obligations for a new explicitly scoped unit; they do not revive or expand the stopped fixed233 Task.

A returned bit with full command/version/log provenance is implementation evidence. A replayable arithmetic certificate additionally requires the actual four-cover equations, map to the U3 two-cover and E, all-place local-solubility evidence, correct pushout/divisor data or an independently adequate auditable implementation, complete local support/outside-support proof, and the exact local readout. The public Handbook alone does not certify that CasselsTate verbose output exports these objects. Fisher's one-T0 pushout route remains a separately reviewed way to explain/check the same value; the conditional Hilbert reduction does not manufacture its missing f, local points or support.

Decision: the mathematical method and a precise class-labelled input path now exist in prior work. The remaining delta is actual runtime binding, normalization/export verification and an admitted bounded execution/certificate. Actual c3, f, e, rank and executable readiness remain UNKNOWN.

