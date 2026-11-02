# PREFIX-435 — Exact four-phase probe repair and path-semiring observer certificate

2026-11-02 · Research line 6 · AUTHOR-DERIVED / EXACT ALGEBRAIC PROOF / FINITE EXACT CHECKED / PORTABLE_DIRECT / UNREVIEWED / NOT_ADMITTED / NATIVE_CLAIM_ABSENT.

## Source and scope

Continues PREFIX-434 (main commit 210c2ed723c8c592fc93f1586a028c9cb3f04ca2) and its exact phase-branch collision. Scientific source stays **frozen** at enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d. This note is an **external static complex-observer extension**, not a claimed native Heartbeat World dynamics, new P000 axiom, accepted Foundation theorem, or formal Task Result. Current P000 is X6 signed discrete Cell space with time separately typed; auxiliary C³ and Hermitian matrices are not native spatial coordinates.

Let X=(1,u,v)ᵀ for u,v∈C. Define
z₄=(5+9i)/2+(3+7i)u/2+4iv,
z₅=A(1+u)+Bv, A=(22+15i)/8, B=(5+9i)/4,
κ(u,v)=||z₄|²−41|.

The original five retained intensity observers from PREFIX-434 are the complex rows
q₁=(0,1,0), q₂=(1,1,0), q₃=(0,0,1),
q₄=(1,0,1), q₅=(A,A,B).
Their outputs are |q_j X|², i.e. (|u|²,|1+u|²,|v|²,|1+v|²,|z₅|²).
These are not the original Port labels 1–5 in order: q₄ is the auxiliary first-source joint intensity |1+v|², whereas z₄ remains the omitted optimization port.

## Theorem A: four explicitly extra phase-controlled probes suffice for all Hermitian readouts

Define four **new auxiliary** rows indexed by (a,b)∈{(0,1),(1,0),(1,1),(1,2)}:
q_(a,b)=(A, A i^a, B i^b).
They are specified observer capabilities **added beyond** the original fixed five measurements; no native phase actuator or transport is assumed.

Put G=XX* and real coordinates
g=(G₀₀,G₁₁,G₂₂, Re G₀₁, Im G₀₁, Re G₀₂, Im G₀₂, Re G₁₂, Im G₁₂)∈R⁹.
For q=(q₀,q₁,q₂) the intensity y_q=qGq* is the exact real-linear form with coefficients
(|q₀|²,|q₁|²,|q₂|²,
 2Re(q₀ conjugate(q₁)),−2Im(q₀ conjugate(q₁)),
 2Re(q₀ conjugate(q₂)),−2Im(q₀ conjugate(q₂)),
 2Re(q₁ conjugate(q₂)),−2Im(q₁ conjugate(q₂))).

Let M be the 9×9 matrix formed from the original five rows followed by these four phase rows, in the displayed order. Exact rational Gaussian elimination gives

**rank(M_first5)=5, rank(M)=9, det(M)=1001129928661/65536=53²·709³/2¹⁶ ≠0.**

Therefore the nine measured real intensities uniquely recover any Hermitian G (including arbitrary Hermitian matrices not known to be rank one), by g=M⁻¹y. For the declared source X=(1,u,v)ᵀ, G₀₁=conjugate(u), G₀₂=conjugate(v); hence the observer recovers (u,v), every complex-linear output intensity, |z₄|², and κ **exactly**.

Proof: expansion of qGq* yields each coefficient above. Each component of M is rational because A,B and all phase exponents are Gaussian rationals. The checked rational determinant is nonzero; thus the linear map is invertible on the full 9-dimensional real Hermitian space. On the fixed X₀=1 source submanifold, read the first two off-diagonal entries of G. Substituting u,v into the original z₄ finishes the reconstruction. No numeric approximation or extrapolation from finitely sampled u,v is used.

**Scoped linear minimality:** the original five independent real-linear forms span dimension 5 on Herm(3); no fewer than four further *scalar real-linear Hermitian intensity measurements* can produce an injective map on all Herm(3), by rank-nullity. Our four meet this bound. This is **not** a four-extra-probe lower bound on the nonlinear fixed-reference rank-one family, on the feasible subset, or on arbitrary non-linear encodings. The new probes are not asserted physically or natively available.

## Theorem B: the original counterexample is distinguished by exact new observations

Reuse PREFIX-434's sources u₊=+i, u₋=−i,
v=1/2000−123i/490000.
Their five original intensities coincide exactly and their κ differ by 172762577/3751562500>0 (inherited proved witness).
For the four phase-tagged rows in the order above, the differences
|q_(a,b)X₊|²−|q_(a,b)X₋|² are, exactly,

**(37577/1960000, −86890077/1960000, −709/16, −86814923/1960000).**

All four are nonzero. The augmented nine-channel observer thus separates this precise formerly colliding feasible fiber. This is an exact certificate that the proposed repair carries information missing from the original q₁,…,q₅ data.

## Theorem C: phase-labeled finite path semiring and a typed BRC observer lease

For a declared finite set of labeled path witnesses with discrete *auxiliary* phase tags in C₄={0,1,2,3}, let h=(h₀,h₁,h₂,h₃)∈N⁴ count paths of each tag. Define alternatives (h⊕k)_r=h_r+k_r, and serial independent path concatenation
(h⊗k)_r=Σ_{j=0}³ h_j k_(r−j mod 4).
Then h→E(h)=(h₀−h₂)+i(h₁−h₃)∈Z[i] is a semiring homomorphism: E(h⊕k)=E(h)+E(k), E(h⊗k)=E(h)E(k). Path count m(h)=Σ h_j is also a semiring homomorphism into N; terminal coherent intensity I(h)=|E(h)|² is an observer, **not** an additive semiring map (interference matters).

Consequently the pair (m(h),E(h)) is an **exact observer-safe quotient** for any finite future expression built from ⊕,⊗ with fixed other tagged-path inputs, when the only terminal observations are (total labeled-path count, coherent intensity). Proof is structural induction over expression trees using the two homomorphism laws. It does not preserve individual branch identity, ordered-step provenance, intermediate phase histogram, or observers on those discarded distinctions; for such futures the complete path-formal carrier must stay. The quotient is not claimed minimal for every narrower observer language.

On P000's declared signed X6 path alphabet, displacement (+1,+1,0,0,0,0) has two distinct minimal ordered native step words (+e₁,+e₂) and (+e₂,+e₁), by the existing shortest-path signed BRC multiplicity 2!/(1!1!)=2. It does **not** assign these paths a native phase. If an auxiliary coherent observer assigns the first path phase 1 and the second ζ∈{1,−1,i,−i}, positive count stays 2 while I=|1+ζ|² assumes 4,0,2,2. A second explicitly tagged reference readout J=|1+iζ|² yields exact pairs (I,J)=(4,2),(0,2),(2,0),(2,4), distinguishing all four tags. Such a conditional finite phase sidecar requires at least two binary tag bits to recover all four possibilities; again that is not a measured P000 phase rule.

The existing typed interfaces read for this audit are:
- experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py: signed X6 shortest-path multiplicity and positive endpoint weights;
- definitions/ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md: PATH_FORMAL_BRC→N_BRC→BOOLEAN_BRC with ordered-path/provenance retention;
- src/enterprise_math/brc_transport.py and src/enterprise_math/brc_control_port.py: exact positive-rational effect histogram, six-axis affine and finite control transitions with explicit quotient leases;
- src/enterprise_math/brc_weighted.py: explicitly excludes signed/amplitude cancellation.

**Reuse decision:** REUSE_APPLIED for exact signed-X6 path count, provenance hierarchy, control-port and observer-safe quotient semantics; COMPOSE_APPLIED for their laws with the newly proven auxiliary finite C₄ path semiring. No existing native signed/coherent transport was executed or shown by these sources. C₄ tagging is a **candidate auxiliary sidecar**; it is neither an approved typed BRC extension nor an automatic map ψ from physical/native X6 to complex amplitudes.

## Executed reproducible evidence and provenance

Saved beside this note:
- prefix435_exact_certificate.py — Python stdlib Fraction determinant, rank and witness check, executed: PASS_PREFIX435_EXACT_FRACTION_TOMOGRAPHY; base_rank=5, augmented_rank=9; determinant=1001129928661/65536.
- prefix435_independent_sympy.py — independent SymPy re-derivation of Hermitian rows and direct input witness, executed: PASS_PREFIX435_INDEPENDENT_SYMPY, same exact matrix rank and determinant and four exact source differences.
- prefix435_phase_path_semiring.py — Python stdlib exhaustive finite semiring cross-check for **81²=6561** ordered pairs h,k∈{0,1,2}⁴, plus native shortest-word multiplicity formula and four tagged readout pairs, executed: PASS_PREFIX435_PHASE_TAGGED_SEMIRING_6561_EXACT_PAIRS.
- PREFIX435_EXECUTION.log — captured outputs. The universally quantified Theorems A/C are established by algebraic proofs above; finite execution is author-side regression evidence, **not** native runtime execution, formal verification, or independent referee review.

## Remaining precise question PREFIX-436

Find an actual **source-versioned typed X6 path/phase interface**, including spatial start Cell, six-axis signed ordered path witnesses, the tag/amplitude update on each primitive step (if any), path and branch provenance, finite future-operation algebra, and observation port. Determine whether the four auxiliary q_(a,b) probes descend from **admissible native updates/observers** or remain external; do not simply postulate a ψ that proves its own intertwinement. A valid native transfer requires explicit ψ, allowed U with ψ(Uω)=Aψ(ω), exact port readout, and preservation of all declared future operations; compare both u=±i witness configurations wherever ψ genuinely exists. If source supplies no phase semantics, preserve this result as an exact external algebraic observer design and isolate the missing native phase-generation law. Formal CLAIM/Result/Review/Admission remain separate from this portable GitHub artifact.
