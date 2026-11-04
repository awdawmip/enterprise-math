# Hodge H0P: rank-one torsion-free changes retain the support obstruction

Date: 2026-11-04. Author: `/root/research_nt_1104`.
Status: `LOCAL_AUTHOR_PROOF / FROZEN_FOR_INDEPENDENT_REVIEW / NOT_ADMITTED`.
This is unclaimed local support for the existing mother objective
`HODGE_SPECIAL_OPEN_FRONTIER_ALGEBRAICITY_MECHANISM`. It neither executes nor
closes a formal Task, borrows a historical researcher identity, or supplies a
positive H0P premise to conditional H0R transport.

## 1. Recovered frontier and precise increment

The September 19 H0P Taskbook is not the highest mathematical source. Current
Source contains canonical Result `RR-D0D2E8489B7EC4AE9AB4`, frozen October 15,
whose main paper has SHA-256
`b53e0972c7f27bc094c2ae51130cf50d85c29309fa7628066038ee4c9eb9463d`.
Its eight actual artifact files agree byte for byte with the earlier frozen
author-copy bundle. `SOURCE_BINDING.json` records these checks at Source
`39556bf5207aa5ba559a27ec591c1bc1bf43b457`. A separate October 15 preliminary
review found no mathematical must-fix within its restricted family. Source
recovery and hashing do not provide a new formal review vote.

The old result concerns the fixed special abelian sixfold (A_0), diagonal
(j:Z=E^3\hookrightarrow A_0=E^3\times E^3), and every finite
zero-dimensional subscheme (D\subset Z). The sheaf (j_*I_D) retains a
nonzero exceptional (\operatorname{ch}_3); its complete first-order
Atiyah–Kodaira–Spencer obstruction on the nine-dimensional Weil tangent space
has rank six with an explicitly known three-dimensional kernel.

The new question: can an arbitrary **rank-one torsion-free coherent sheaf on
the same smooth support** remove that support obstruction? No. The argument
needs only injectivity of cohomology restriction across codimension at least
two, instead of the old finite-support isomorphism. It therefore includes
curve modifications on the threefold and all line-bundle twists. The enlarged
family has a proved kernel inclusion and rank lower bound, not an asserted
exact kernel.

All varieties, cohomology and tangent spaces are external mathematical
carriers. Native P000/X6 and separate time types are unchanged. This unit makes
no heartbeat, BRC–Shor, or native-residual attribution and runs no scientific
program. Programmatic work was limited to Source reading, byte comparisons,
and hashing. Standard deformation theory/local cohomology are reused, not
presented as new global tool families.

## 2. General necessary support condition

Let (X) be a smooth projective complex variety and
(i:Z\hookrightarrow X) a smooth integral closed subvariety. Let
(\mathcal E) be a coherent rank-one torsion-free sheaf on (Z), and set
(F=i_*\mathcal E). Let (R=\mathbb C[\epsilon]/(\epsilon^2)), and let
(X_R/R) be a projective first-order deformation of (X), with class
(\kappa\in H^1(X,T_X)). Define

\[
 \delta_Z(\kappa)\in H^1(Z,N_{Z/X})
\]

by restriction and the normal projection (T_X|_Z\twoheadrightarrow N_{Z/X}).

**Theorem 1.** If a perfect complex (F_R\in\operatorname{Perf}(X_R)) has
derived special fibre isomorphic to (F), then

\[
                         \delta_Z(\kappa)=0.             \tag{1}
\]

Under the standard complete Atiyah–Kodaira–Spencer perfect-lift criterion,
the obstruction map (\Omega_F) therefore satisfies

\[
 \ker\Omega_F\subseteq\ker\delta_Z.                    \tag{2}
\]

On every declared finite-dimensional tangent subspace (T\),

\[
 \operatorname{rank}(\Omega_F|_T)
       \geq\operatorname{rank}(\delta_Z|_T).             \tag{3}
\]

No converse is asserted: a deformation of (Z) need not deform an arbitrary
line bundle, curve ideal, or torsion-free sheaf on it.

**Proof.** Let (S\subset Z) be the closed locus where (\mathcal E) is not
locally free of rank one. At a codimension-one point, the local ring of smooth
(Z) is a discrete valuation ring, and every finite torsion-free rank-one
module there is free. Thus (S) has codimension at least two. On
(U=Z\setminus S), the sheaf (\mathcal E|_U) is a line bundle.

First, any alleged derived lift is an (R)-flat sheaf. Since (X_R) is
(R)-flat, its derived reduction (F_R\otimes_R^{\mathbf L}\mathbb C) is
the degree-zero sheaf (F). Tensoring
(0\to\mathbb C\xrightarrow{\epsilon}R\to\mathbb C\to0) with (F_R)
gives a triangle (F\to F_R\to F\to F[1]). The cohomology exact sequence
places (F_R) in degree zero and gives

\[
             0\longrightarrow F\longrightarrow F_R
                         \longrightarrow F\longrightarrow0.
\]

Multiplication by (\epsilon) is quotient followed by inclusion, so its
kernel equals its image, the flatness criterion over the dual numbers.

Next work on (X\setminus S) and its corresponding open in (X_R). On a
sufficiently small open meeting (U), trivialize the line bundle
(\mathcal E|_U). Its local generator lifts to (F_R). Nakayama's lemma for
the nilpotent ideal ((\epsilon)) makes the resulting map from the ambient
structure sheaf onto (F_R) surjective. Because this sheaf is cyclic locally,
the kernel is its annihilator. The annihilator is intrinsic, so these local
ideals glue even though the line bundle has transition functions.

The quotient by that ideal is locally the (R)-flat sheaf (F_R), with
special fibre the structure sheaf of (U). Flatness makes reduction of this
presentation exact. Thus it defines an actual flat embedded deformation
(U_R\subset(X\setminus S)_R). The usual first-order normal obstruction
must vanish after restriction:

\[
          \delta_Z(\kappa)|_U=0\quad\text{in }H^1(U,N_{Z/X}|_U). \tag{4}
\]

This uses the actual sheaf's embedded support, not a Chern trace or virtual
class. The normal-obstruction assertion follows equally from the local
regular-sequence liftings: their differences on overlaps give the Cech
cocycle obtained by restricting the ambient Kodaira–Spencer cocycle and
projecting to (N_{Z/X}).

Finally, smooth (Z) is regular and Cohen–Macaulay, and (N=N_{Z/X}) is
locally free. Depth along the codimension-at-least-two subset (S) is at least
two. Hence the local cohomology sheaves (\mathcal H^q_S(N)) vanish for
(q=0,1), and the local-to-global spectral sequence gives
(H^1_S(Z,N)=0). The localization sequence

\[
 H^1_S(Z,N)\longrightarrow H^1(Z,N)\longrightarrow H^1(U,N|_U)
\]

makes the second arrow **injective**. Surjectivity is unnecessary and has not
been asserted; (H^2_S(Z,N)) may be nonzero. Equation (4) proves (1). If (S)
is empty this restriction is simply the identity.

For (2), use the same standard perfect-lift obstruction theorem as in the
recovered paper: Huybrechts–Thomas, arXiv:0805.3527v2, Corollary 3.4. Its
square-zero/smooth-ambient hypotheses apply: (F) is perfect on smooth (X),
and projective (X_R) embeds in some
(\mathbb P^m_R\subset\mathbb P^m_{\mathbb C}\times\mathbb A^1_{\mathbb C}),
a smooth complex ambient. Vanishing of the complete Atiyah–KS product implies
a perfect lift, so (1) implies (2). Linearity and rank-nullity give (3). ∎

**Image interpretation.** The kernel inclusion gives a well-defined
surjection

\[
 \rho_F:\operatorname{im}(\Omega_F|_T)\twoheadrightarrow
               \operatorname{im}(\delta_Z|_T),\qquad
 \rho_F(\Omega_F(t))=\delta_Z(t).                       \tag{5}
\]

It need not be injective. This direction is different from the old injective
image identification available when both kernels are equal. No full Ext
basis, exact rank, or sufficiency follows from the enlarged theorem.

## 3. Application to the exact H0P carrier

Keep the recovered special member, including its nonprincipal weight:

\[
 E=\mathbb C/(\mathbb Z+i\mathbb Z),\quad A_0=E_z^3\times E_w^3,
 \quad j(t)=(t,t),\quad D_0=\operatorname{diag}(1,1,3).
\]

The underlying Hermitian carrier is (K=\mathbb Q(i)), lattice
(\mathbb Z[i]^6), (h=\operatorname{diag}(1,1,1,-1,-1,-3)). The polarization
weights are (\operatorname{diag}(I_3,D_0)), and the (K)-action is
((a+bi)(z,w)=((a+bi)z,(a-bi)w)).

The old source supplies all nine polarized (K)-linear tangent directions:

\[
 C(B)=\begin{pmatrix}0&B\\D_0^{-1}B^{\mathsf T}&0\end{pmatrix},
 \qquad\delta_Z(B)=D_0^{-1}B^{\mathsf T}-B,
 \qquad B\in M_3(\mathbb C).                            \tag{6}
\]

Its previously proved kernel and rank are

\[
 \mathcal K=\left\{
 \begin{pmatrix}a&c&0\\c&b&0\\0&0&0\end{pmatrix}:a,b,c\in\mathbb C
 \right\},\quad\dim\mathcal K=3,\quad\operatorname{rank}\delta_Z=6. \tag{7}
\]

They are consumed, not counted as a new matrix result. In particular,
(B=E_{33}) has normal image (-\tfrac23E_{33}\ne0).

**Corollary 2.** For every rank-one torsion-free coherent sheaf (\mathcal E)
on this fixed diagonal, the actual perfect sheaf (j_*\mathcal E) satisfies

\[
 \ker(\Omega_{j_*\mathcal E}|_{T_{\rm Weil}})\subseteq\mathcal K,
 \qquad\operatorname{rank}(\Omega_{j_*\mathcal E}|_{T_{\rm Weil}})\geq6. \tag{8}
\]

It cannot deform in all nine directions; (E_{33}) obstructs every member.
Nevertheless

\[
 \operatorname{ch}_3(j_*\mathcal E)=[Z],\qquad
 \Pi_W\operatorname{ch}_3(j_*\mathcal E)=\Pi_W[Z]\ne0.   \tag{9}
\]

**Proof.** Equation (8) is Theorem 1 applied to (6). For (9), standard
Grothendieck–Riemann–Roch for the regular embedding gives

\[
 \operatorname{ch}(j_*\mathcal E)
   =j_*\bigl(\operatorname{ch}(\mathcal E)\operatorname{td}(N_{Z/A_0})^{-1}\bigr).
\]

The embedding has codimension three, and the degree-zero term inside the
pushforward is the rank (1). Every other term has higher codimension.
Therefore the codimension-three term is ([Z]). The nonzero exceptional
projection of the same actual diagonal is the recovered source result. ∎

Strictly new members include (\mathcal E=L\otimes I_{C/Z}), with any line
bundle (L) and any subscheme (C\subset Z) of dimension at most one, including
nonreduced curves and embedded points. Its ideal is rank one and torsion-free
as a subsheaf of the structure sheaf of integral (Z). Varying curve degree,
genus, nonreduced structure, or line-bundle twist cannot repair this normal
obstruction. For finite (C) and (L=\mathcal O_Z), the old exact-rank-six
theorem remains stronger. For other members additional sheaf obstructions may
shrink the kernel further; this unit does not decide them.

## 4. Source, duplicate boundary, and extracted interface

The full inventory groups were inspected: seven Hodge publication leaves and
six T6 leaves. Hodge was chosen because its later exact Result and a concrete
unclosed enlargement were recoverable. No later-order T6 residual or budget
was invented, and the accepted order-one through order-four work was not repeated.

Read H0P/Q/R Taskbooks, the October 15 main paper, finite-support lemma, Chern
lemma, and separate preliminary review. Bounded searches of current notes,
returns, result records and artifacts for rank-one torsion-free/codimension-two
modification terminology found no matching Hodge extension. This is
project-local duplicate evidence, not a literature priority claim. The old
proof quantifies over finite zero-dimensional (D); its converse uses an
affine chart containing that finite support. It does not supply a converse
for arbitrary curves or line bundles.

Exact paths at Source `39556bf5207aa5ba559a27ec591c1bc1bf43b457`:

- Task: `research_tasks/HODGE_H0P_NONSPLIT_WEIL_BILATERAL_DEFORMATION_OBJECT_20260919.md`.
- Result: `research_result_records/RS-HODGE-H0P-NONSPLIT-WEIL-BILATERAL-DEFORMATION-OBJECT/RR-D0D2E8489B7EC4AE9AB4.json`.
- Actual artifacts: `research_artifacts/mcp/RS-HODGE-H0P-NONSPLIT-WEIL-BILATERAL-DEFORMATION-OBJECT/MCP-e3eda4529333438d8ae1ae7e6983e5e5/86da7418af02a4cc365b/`.
- Author-copy bundle: `research_notes/owner_goal_20261015/HODGE_H0P_FROZEN_AUTHOR_PROOF_COPY_BUNDLE.json`.
- Independent preliminary review: `research_notes/owner_goal_20261015/HODGE_H0P_SCIENTIFIC_PRELIMINARY_REVIEWED_BUNDLE.json`, member ending `reviews/h0p_scientific_preliminary/REVIEW.md`, SHA-256 `90023e15d3e8f9740788b2ffc5f73ca2fcb340dde033ae32dcfaca51b52b5ca4`.

The standard depth/localization and complete-obstruction inputs are those
already identified in the old primary-input ledger: Stacks tags
[0AVZ](https://stacks.math.columbia.edu/tag/0AVZ),
[0G71](https://stacks.math.columbia.edu/tag/0G71),
[0A6T](https://stacks.math.columbia.edu/tag/0A6T), and
[Huybrechts–Thomas, arXiv:0805.3527v2](https://arxiv.org/abs/0805.3527),
Corollary 3.4. Their fulltexts were not newly fetched in this unit; the exact
historical statement-level use and preliminary source checks were read.
The codimension-two application is proved above. GRR and rank-one
torsion-free freeness over a DVR are standard mathematical inputs.

The local `interface.json` extracts a necessary-condition filter. Nonzero
normal obstruction yields `NO_PERFECT_LIFT`; zero returns
`NOT_DECIDED_BY_THIS_FILTER`. It must not return an unobstructed object or
exact Ext rank merely because the normal map vanishes. No complexity
improvement, new registered API, or theorem admission is asserted.

## 5. Remaining mother question

The enlarged negative boundary covers all rank-one torsion-free sheaves on
this fixed smooth diagonal support, pending independent review of the new
argument. A useful next positive candidate must change more than such a
rank-one sheaf: for example, specify a genuinely mixed derived object or a
different support with a different normal map. This is a necessary route
change, not a proof that either alternative works. Generic rank greater than
one, multiple/nonreduced support, genuinely multi-degree complexes, and
arbitrary special or very-general objects are outside this theorem.

H0R's dependency remains unpaid: this unit supplies no nonzero exceptional
object unobstructed in all nine directions, and no H0Q validation of such a
positive object. No higher-order deformation/algebraization argument is run.
The mother objective remains open.

EM-Source-Status: Read=Verified snapshot reused. Write=Not required for shared
Source in this local support role; local draft saved and owner publication
pending. Author identity: `/root/research_nt_1104`; no formal Researcher-ID or
CLAIM is assumed.
