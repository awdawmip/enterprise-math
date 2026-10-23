# R246 — Singular affine effects: three-step witness and strong quotient gap

Status: **AUTHOR-SIDE PROVED FINITE MODEL / NONCANONICAL DRAFT**. This is an immutable author research handoff on a non-main branch, **not** a Researcher CLAIM, native Result, accepted theorem, Working Truth, or physical heartbeat demonstration.

## Frozen authority and source

- GLOBAL_KNOWLEDGE_V1 main: c7595dc39a2a68074c2c732a0a8b5c16d3a4e60a.
- P000 original blob: 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc, ACTIVE_LOCKED; ACTIVE worldview and portable research rules read at this snapshot.
- Enterprise Math main source: 49b2545cb2cdcde3b7ac32d7821c57fdb6f2f412.
- Source interfaces: src/enterprise_math/brc_control_port.py blob 44def6b8ac787e798d3cc2c6be16f873f91b9db8; src/enterprise_math/brc_transport.py blob be1debe367263931bd5e93fd750be3ed54624fe1; docs/PORTABLE_RESEARCH_PROTOCOL.md blob ca5de2d680d2439ff4b67c2c55fbd4159813cd5c.
- Affine.__post_init__ does not require invertibility. ControlPacket.deterministic/then preserve positive exact branch weights and full affine effect.
- Status of native tool: session_start -> STATIC_READONLY_SCOPE_DENIED (operation_sent=false); control_tasks -> CONTROL_QUOTA; no active owner or CLAIM verified. Standalone checkers are **not** imports of the Enterprise Math Python package.

## Mathematical question

R245 proves a ≤2-step effect-distinguishability bound for the specific deterministic two-gate 16-state model with invertible actions. Is this still true for **singular** six-axis affine effects accepted by the algebraic type? Must the strongly future-safe quotient returned by refine_control_partition equal observational trace equivalence?

All labels in S={0,...,15} are four **nonspatial** control bits, s=8x+4a+2c+r. Define the 8-label observer π(s)=(x,a XOR c,r), complementary partner τ(s)=s XOR 6; two deterministic gates:
G3(x,a,c,r)=(x XOR a XOR c,a,c,r) and G2(x,a,c,r)=(x XOR r,a,c,r).
Both commute with τ and preserve π-class pairings. Every transition carries unit weight and multiplicity, positive BRC only. Spatial effects act on six rational/integer coordinates, separate from four control labels. For a gate word w, observe (π(final control), exact composed six-axis affine action), not only total mass or effect at one point.

## Lemma: prefix image test

For maps F,A,B:X→X, we have A∘F=B∘F **if and only if** A and B agree pointwise on im(F). Proof: equality of the two compositions at every x is precisely equality of A and B on all y=F(x). If F is surjective, A∘F=B∘F implies A=B. This is the exact role of invertibility in R245: later edge-effect differences can be permanently masked after a singular prefix; no commutativity is needed for the original two-step bound.

For an arbitrary alphabet of q distinct **invertible** six-axis affine actions, with the same 16-state/two-gate control graph and independent edge choices, the R245 bivariate counting polynomial therefore extends without a commuting assumption:
F_q(X,Y) = (q² + (q⁴−q²)X)² × (q⁴ + 2q²(q⁴−q²)XY + (q⁴−q²)²X²)³.
This follows by pairing four edge labels per π-fiber: q² choices equal within each gate versus q⁴−q² unequal, and multiplying the two one-fiber and three coupled two-fiber factors of the exact R245 control graph. F_q(1,1)=q³². The theorem requires equality of complete affine effects, not equality only at a selected initial Cell.

## Explicit singular-effect alphabet

On z=(z1,...,z6) set:
I(z)=z;
N(z)=(0,z2,z3,z4,z5,z6) (rank 5);
C(z)=(z1+1,z2,z3,z4,z5,z6);
R(z)=(-z1,z2,z3,z4,z5,z6).
Their matrices and offsets are exact integer/six-axis Affine inputs. These typed maps are **not thereby proved to be allowed physical X6 heartbeat steps**. Identities: R != I, R∘N = N, while R∘C∘N != C∘N; applied at the origin, the last two maps output first spatial coordinate −1 and +1 respectively.

All states outside {2,4,10,12} have I for both gates. For s=2,4 use N on both G3 and G2. For s=10 use I on G3; for s=12 use R on G3. In the **delayed** variant use C on G2 for both s=10 and s=12; in the **masked** variant use I for G2 at both. Other effects are I. Controls satisfy G3(2)=10, G3(4)=12, G3(10)=2, G3(12)=4 and G2 fixes these four.

## Theorem A — exact minimal witness depth 3 (delayed variant)

Initial paired sources 2 and 4 have identical full-effect observation for the empty word, both one-gate words and **all four** length-two words.

Proof by exhaustive symbolic case split: If the first gate is G2, it applies N to both sources, leaving them at {2,4}; the next gate also applies N to both. If the first gate is G3, it applies common N, moves to {10,12}; the second gate G2 applies common C, while G3 applies respectively I and R but (R∘N=N). The observer π remains matched by τ-commutation.

However word (G3,G2,G3) gives total effects
  E_323(2)=I∘C∘N=C∘N;
  E_323(4)=R∘C∘N.
They differ at every initial first coordinate, output first coordinate +1 versus −1. Hence minimum distinguishing length d(2,4)=3, **disproving extension of the universal R245 ≤2 bound when singular effects are permitted**.

## Theorem B — exact 9 trace classes versus 10 strong congruence classes (masked variant)

In the masked variant, starting from 2 or 4, the *first gate* applies N and projects the cumulative action into H0={z:z1=0}. All subsequent edge actions on this closed control component lie among N,I,R; they preserve H0, and I and R coincide when restricted to H0. Induction on arbitrary gate words proves that total affine effects from sources 2 and 4 coincide for **all finite words**, while paired final π observations coincide by τ. Thus 2 and 4 are trace-equivalent forever.

Sources 10 and 12 are immediately distinguishable by G3, which applies I vs R. Other six π fibers have only I effects and remain trace-equivalent. Because the initial observer already separates the 8 distinct π values, the **coarsest external trace equivalence** has 8+1=9 classes.

The Source control-port strong row-refinement algorithm instead checks exact full effects into current target quotient classes from every source state. Starting at π partition with 8 classes, G3 I/R mismatch first splits {10,12}, leaving 9 classes. On the second refinement step G3 targets 10 versus 12, now distinct target classes, so {2,4} must split, leaving 10 classes; third round stable. Therefore:
  |S/~trace| = 9 < 10 = |S/~strong-congruence|.

This **is not a defect in the Source function**: the Source's strong quotient must support restarting each compressed target state independently and composing new packets. Trace equivalence only compares cumulative effects from the original fixed inputs, whose prior N prefix limits subsequent reachable images. The 9 trace labels cannot be substituted for the stronger 10-state memoryless compositional quotient without preserving additional prefix-image data.

## Verification and exact scope

- Standalone Python 6×6 integer affine checker: enumerated all 16 states and two gates, 8 π fibers, words through depth 7 for both configurations; confirmed earliest delayed witness G3-G2-G3, masked 9 trace classes up to depth 7 and 10 strong classes. Infinite masked assertion is proved by H0 invariance above, not inferred from finite search.
- Independent C++17 integer affine specialization along first axis (identical other 5 spatial axes): enumerated all words through depth 8, verified delayed d=3, masked no finite witness in this depth, strong classes 10. Build used -std=c++17 -O2 -Wall -Wextra -Werror.
- Both checkers passed author-side; full local self-contained evidence bundle and hashes available with the R246 author return. Native enterprise_math Python import/true source execution, 193-series native path provenance and physical heartbeat effect admissibility remain pending. No actual negative BRC mass, classical π/trigonometry, or physical residual attribution was used.
- Actual BRC reuse: REUSE_APPLIED to named ControlPacket/EffectHistogram/Affine/partition interfaces; REUSE_IDENTIFIED_EXECUTION_UNAVAILABLE for actual installed Source Python.

## Next R247 discriminating tasks

(1) Execute native Source's ControlPacket.deterministic/then and refine_control_partition at **exact** Source commit 49b2545c; record __file__, full source SHA and native output, distinguishing local simulators from native pass.
(2) Read actual permitted X6 heartbeat effect set; decide whether linear parts must be invertible, whether singular N is permitted, or only an algebraic nonphysical operator.
(3) If singular is permitted, design a reachable-prefix-image-aware observer/certificate within existing typed BRC control family and prove finite exact limits for the allowed effects.
(4) Independently establish faithful R193 original-path/branch provenance embedding and enumeration completeness.
(5) Authenticate researcher session, formal CLAIM and independent Research Driver before claiming official Task/Result acceptance.

Do not merge this draft into canonical mathematical truth without actual owner/review/admission.
