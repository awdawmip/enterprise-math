# R004: embedded target defect under sequential constraints

Date: 2026-11-04. Local support draft by `/root/research_nt_1104`.

**Evidence status:** `AUTHOR_PROOF_AND_EXTERNAL_MODEL_EXACT_CHECK / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED`.
This is an unclaimed, local contribution to the existing Task
`RS-R004-PADIC-TARGET-DEFECT-RESIDUAL-PROFILE-20260930`, publication
`TP2-2F73D1BB1AAA29EF4FCD`. It neither creates a Task nor changes that Task's
ownership, state, truth status, or completion. Classification: an application of
standard finite-module algebra with explicit R004 counterexamples and a scoped
behavioral-information boundary; not a new general algebra or tool family.

## 1. Question, inputs, and declared observations

The 2026-09-30 R004 checkpoint proves that the full layer profile determines the
abstract missing-target module, but leaves its sufficiency for future operations
open. Here we resolve that question for **adding known linear constraints,
recombining such additions, and surjective coordinate cuts while keeping the
original target**. In this language the full profile is insufficient; the
embedded defect in a marked ambient quotient is sufficient. With the ambient
quotient fixed, different embeddings of a fixed profile really are observable.

Let (p) be prime, (K\geq1), (R=\mathbb Z/p^K\mathbb Z), and (V) a finite
(R)-module. In the matrix application (V=R^n), (A=\operatorname{Row}(A_H))
is the known-constraint submodule and (B=\operatorname{Row}(B_H)) is the
original target submodule. Put

\[
 W=A+B,\qquad D=W/A,\qquad
 c_j(D)=\dim_{\mathbb F_p}(p^{j-1}D/p^jD),\quad 1\leq j\leq K.
\]

The previous scalar is (\Delta=\log_p|D|=\sum_jc_j(D)). Target preservation is
(D=0) by the historical row/kernel criterion. We use this existing criterion,
not a new native-space identification.

Allowed operations and observations are explicitly:

1. Add a labeled known-constraint submodule (C\leq V): replace (A) by
   (A+C), keeping (B). The updated defect is
   (D_C=(A+B+C)/(A+C)).
2. Apply a specified surjective (R)-linear coordinate map (f:V\to V'):
   replace (A,B) by (fA,fB). Coordinate deletion is a special case.
3. Repeat finitely many of these operations; controls retain their actual
   ambient meanings under the intervening maps. Observe the resulting module,
   its profile, its size, or just whether it is zero.

All submodules, including zero and the whole ambient module, are admissible.
Repeated constraints are allowed. No new target rows, inverse coordinate lifts,
arbitrary refinement, nonlinear observation, or approximate states are being
silently admitted. Those remain parts of the broader mother question.

The vector rank (n) is an **external algebraic carrier rank**, never the number
of native spatial axes. P000 and the native signed six-axis Cell torsor remain
the project premises, with time separately typed. This paper makes no claim
about spatial geometry, motion, physical storage, or Heartbeat/BRC arithmetic.
All computations below are exact finite external module calculations. Signed
module cancellation is not positive-branch recoalescence. No Cell address or
native operator is exported.

## 2. Exact one-step and sequential transport

**Proposition 1 (marked ambient quotient).** Let (q:V\to Q=V/A), let
(\bar B=q(B)\leq Q), and let (U=q(C)\leq Q). Then

\[
 D_C\cong(\bar B+U)/U
       \cong\bar B/(\bar B\cap U).                         \tag{1}
\]

The new ambient state is

\[
 (Q,q,\bar B)\longmapsto(Q/U,\pi\circ q,\pi(\bar B)),    \tag{2}
\]

where (\pi:Q\to Q/U) is the quotient map. The tuple includes the actual
embedding of (\bar B) and the transport of input/control labels; its abstract
isomorphism types alone are not the asserted sufficient state.

**Proof.** The image of (A+B+C) under (q) is (\bar B+U), and that of
(A+C) is (U), so the first isomorphism follows from the quotient theorem.
The map (\bar B\to(\bar B+U)/U), (b\mapsto b+U), is onto with kernel
(\bar B\cap U). This proves (1) and identifies the actual embedded image
retained in (2). In the original presentation that kernel has preimage

\[
 K_C=((A+B)\cap(A+C))/A\leq D.                          \tag{3}
\]

For a sequence of additions (C_1,\ldots,C_t) in the original (V), put
(U_i=q(C_i)). At stage (i) use the image of (U_i) under all earlier
quotient maps. The quotient theorem and induction give

\[
 Q_t=Q/(U_1+\cdots+U_t),\qquad
 D_t\cong\bar B/(\bar B\cap(U_1+\cdots+U_t)).           \tag{4}
\]

This agrees with simultaneous addition. It preserves the intermediate queries
as well, since (2) holds at every prefix. Reordering additions preserves the
final state but can change the sequence of intermediate answers. ∎

**Proposition 2 (surjective coordinate cuts).** If (f:V\to V') is onto and
(N=\ker f), then

\[
 V'/fA\cong V/(A+N)\cong Q/q(N),\qquad
 (fA+fB)/fA\cong\bar B/(\bar B\cap q(N)).               \tag{5}
\]

**Proof.** The onto map (V\to V'/fA), (v\mapsto f(v)+fA), has kernel
(A+N). Its image of (B) is the new target defect. Applying Proposition 1
with (C=N) proves (5). The resulting quotient must retain its identification
with (V'/fA) so later constraints given in (V') can be transported. Induction
therefore handles arbitrary finite mixed sequences of the two declared
operations. ∎

These are standard isomorphism-theorem consequences. Their project use is an
explicit sufficient interface for the previously unclosed R004 future language.

## 3. Three exact failures of weaker carriers

### 3.1 Same complete profile, same next input, different result

For any prime (p), take (R=\mathbb Z/p^2\mathbb Z), (V=R), and compare

| State | (A) | (B) | Initial (D) | After the same (C=pR) |
|---|---|---|---|---|
| X | (pR) | (R) | (R/pR\cong\mathbb F_p) | (\mathbb F_p) |
| Y | (0) | (pR) | (pR\cong\mathbb F_p) | (0) |

Both initial full profiles are ((1,0)), so even the entire invariant-factor
spectrum loses a future-relevant distinction. The smallest prime gives explicit
one-column matrices over (\mathbb Z/4\mathbb Z):

\[
 (A_X,B_X)=([2],[1]),\qquad (A_Y,B_Y)=([0],[2]),
 \qquad C=[2].                                         \tag{6}
\]

Here the ambient quotients differ. This example is first at exponent (K=2)
**among rank-one free ambient modules for this constraint-addition language**:
over a field, (V=\mathbb F_p) has only (0,V) as submodules. Defect zero
stays zero under all additions; nonzero defect forces (A=0,B=V), so its
response is fixed. Rank zero is trivial and (p=2) is the smallest prime.
This does not assert minimality across unrelated languages or all matrix sizes.

### 3.2 Even a fixed ambient quotient does not replace the embedding

Let (Q=V=\mathbb F_p^2), (A=0), (B_1=\langle e_1\rangle), and
(B_2=\langle e_2\rangle). The known ambient module and both abstract defects
are identical in type and profile. The same addition (C=\langle e_1\rangle)
kills the first defect and leaves the second one-dimensional. Thus retaining
(Q)'s type alongside (D)'s type does not repair the loss of embedding.
For fixed (A=0) over a field, rank one has only one subspace of each profile,
so rank two is the first possible instance of this particular collision.

### 3.3 Individual update kernels do not compose

Let (Q=\mathbb F_p^2), (D=\langle e_1\rangle). Compare two tables of
labeled controls, with labels (1,2):

\[
\begin{array}{c|cc}
 &U_1&U_2\\ \hline
 S&\langle e_2\rangle&\langle e_1+e_2\rangle\\
 T&\langle e_2\rangle&\langle e_2\rangle.
\end{array}                                             \tag{7}
\]

For either table, each individual control has dimension one and
(D\cap U_1=D\cap U_2=0). Thus a compressed control table retaining only
each label's kernel inside (D), and even each control's abstract type and
individual post-update defect, is identical. But

\[
 D\cap(U_1+U_2)=D\quad\text{in }S,
 \qquad D\cap(U_1+U_2)=0\quad\text{in }T.               \tag{8}
\]

The combined defect is respectively zero and (D). In (S), the missing
relation is (e_1=(e_1+e_2)-e_2). Hence

\[
 D\cap(U_1+U_2)\ne(D\cap U_1)+(D\cap U_2)              \tag{9}
\]

in general. This is a failure of an **erased joint-control representation**;
the uncompressed ambient inputs in the two tables are different. We are not
claiming that a consumer supplied those full inputs cannot distinguish them.
Equation (2) retains precisely the joint ambient positioning needed here.

## 4. What must be retained when the ambient module is known

**Theorem 3 (exact behavioral classes at fixed ambient module and profile).**
Fix a finite labeled (R)-module (Q) and one realizable layer profile (c).
Let possible states be embedded submodules (D\leq Q) of profile (c).
All labeled cyclic constraints (Rv\leq Q) are allowed, with controls
transported through the quotient after each step.

(a) If one-step output includes defect size, any two distinct states are
distinguishable by a single cyclic constraint.

(b) Even if the only output is whether the defect is zero, any two distinct
states are distinguishable by a finite sequence of cyclic constraints.

Consequently, an exact sufficient residual for either language must distinguish
every such embedded submodule. Conversely, the embedded submodule in the fixed
marked ambient quotient is sufficient by Proposition 1. This is a behavioral
classification conditional on this ambient module and this control language,
not a claim of a universally minimal datatype for every R004 extension.

**Proof.** Distinct (D,D') of the same profile have the same finite size.
Choose (v\in D\setminus D') and (C=Rv). Then (C\subseteq D), whereas
(D'\cap C\) is a proper submodule of (C). Therefore

\[
 |D/(D\cap C)|=|D|/|C|
       < |D'|/|D'\cap C|.                              \tag{10}
\]

This proves (a). For (b), choose a finite generating tuple (v_1,\ldots,v_s)
for (D), and successively add the images of (Rv_i). Their sum in the
original (Q) is (D). Equation (4) makes the final defect of state (D)
zero. The final defect of (D') is (D'/(D'\cap D)), which is nonzero:
otherwise (D'\subseteq D), and equal finite size would force equality.
The same labeled sequence is applied to both states, proving (b). ∎

**Corollary 4 (exact conditional capacity in the field case).** If
(Q=\mathbb F_p^n) and the known profile is dimension (d), the number of
behavioral classes is

\[
 N_{p,n,d}={n\brack d}_p
 =\prod_{i=0}^{d-1}\frac{p^n-p^i}{p^d-p^i}.             \tag{11}
\]

Conditional on (p,n,d), a fixed labeled ambient basis, and the common control
interpreter, an exact fixed-length residual code needs and can attain

\[
 b_{p,n,d}=\left\lceil\log_2 {n\brack d}_p\right\rceil  \tag{12}
\]

additional bits. Here (b=0) for (d=0,n).

**Proof.** The number of ordered independent (d)-tuples in
(\mathbb F_p^n) is \(\prod_{i<d}(p^n-p^i)\). Each (d)-subspace has
\(\prod_{i<d}(p^d-p^i)\) ordered bases, giving the standard Gaussian-binomial
count. Theorem 3 requires distinct codes for all these subspaces; a binary
fixed-length code has at most (2^b) values. Conversely enumerate the unique
reduced-row-echelon presentations of the subspaces and store their index.
Decode the actual subspace and use Proposition 1. This attains the information
bound without asserting an efficient encoder or decoder. ∎

For (n=2,d=1), the (p+1) states are
(\langle(1,t)\rangle), (t\in\mathbb F_p), and
(\langle(0,1)\rangle); exactly (\lceil\log_2(p+1)\rceil) conditional bits
are required. Both the Gaussian count and finite-class coding bound are
standard. Their use here quantifies the precise information omitted by the
R004 layer profile for the declared future language.

## 5. Reusable interface, costs, and finite checks

The proposed interface is recorded in `interface.json`. It is a local tool
extraction proposal, not a registered global API. Inputs are exact finite-module
presentations, an actual target-submodule embedding, and labeled control maps.
Outputs carry the new ambient quotient, target image, and transport maps; they
must not output only an invariant-factor list and call that a sufficient state.

No algorithmic speedup is claimed. A generating matrix for a (d)-dimensional
field subspace uses at most (dn\lceil\log_2p\rceil) raw entry bits, in addition
to shape/basis metadata. A raw pair of matrices for (A,B\leq R^n) with
(a,b) rows uses ((a+b)n\lceil\log_2(p^K)\rceil) entry bits, plus dimensions
and the ring/ambient/control interpretation. Merely storing the (K) profile
entries costs at most (K\lceil\log_2(n+1)\rceil) bits for a defect generated
inside (R^n), but the collisions prohibit treating that as a sufficient
replacement. Equation (12) is conditional on fixed shared context; it does not
absorb that context's storage cost. Explicit quotient coordinates or reduction
maps, control input reading, submodule sums/intersections, normal-form
construction, profile calculation, decoding, and verification all cost work.
They are retained operations, not hidden free oracles. No improved total-cost
bound is established. In the enumerative upper bound even the preprocessing
and lookup table or enumeration time must be paid.

**Execution provenance and scope boundary.** The actual command was
`python verify_r004_embedding.py > verification.json`, run in this artifact
directory. It used ordinary Python, **not actual typed BRC**. The author initially
classifies these computations as external finite-module algebra, consistently
with the Task's explicit distinction between module cancellation and BRC.
This classification was checked against
`docs/HEARTBEAT_BRC_ONLY_ARITHMETIC.md`,
`research_constraints/heartbeat_brc_only.json`, and
`docs/PORTABLE_RESEARCH_PROTOCOL.md` at the source pin below. The first states
“本项目心跳世界、BRC–Shor 及原生残差研究；不扩张为其它专业工作的通用数学禁令”; the
machine scope is `enterprise-math/heartbeat`, `enterprise-math/BRC-Shor`,
and `native-residual-attribution`. The present inputs and outputs are finite
module sets, submodule embeddings, cosets and their profiles. They neither
generate a native state nor compare a native physical residual, and do not
model Shor, heartbeat timing, phase propagation, or a native operator. Thus
the actual computation is outside that scoped `ACTUAL_TYPED_BRC_ONLY`
requirement. No exemption or new pending gate is needed or asserted. Its
evidence is confined to the stated external finite algebra model; ordinary
arithmetic is not being renamed BRC. The general results and displayed
counterexamples also have the written proofs independently of this program.
Independent mathematical review and any formal admission remain separate.

The script `verify_r004_embedding.py` uses integer arithmetic and complete finite
sets, independently of Smith-normal-form code. Its closure search starts at
zero and adjoins every vector until no new submodule arises. This exhausts the
submodule lattice, since every submodule has a finite generating list. Cosets
are explicit sets; each layer is computed from

\[
 |p^j(W/A)|=|p^jW+A|/|A|.                              \tag{13}
\]

The script checks the three collisions and recorded minimal field controls,
then checks all 15 submodules of ((\mathbb Z/4\mathbb Z)^2): 3,375 triples
((A,B,C)) for the quotient law, 50,625 quadruples ((A,B,C_1,C_2)) for actual
coset transport versus direct addition, and 225 pairs for deletion of one
coordinate. For ((p,n)=(2,2),(2,3),(3,2),(3,3),(5,2)), it enumerates every
subspace and verifies that cyclic-control size signatures and all-subspace
zero-query signatures distinguish every state in each dimension, and match
(11). The zero-query enumeration represents all finite cyclic schedules by
their generated submodule, using the already proved composition law. The
captured `verification.json` reports PASS. These finite checks supplement,
not replace, the written proofs and do not confer formal result admission.
The checks do not exhaust the broader Task's requested
(p,K\in\{2,3,5\}\times\{2,3,4\}) matrix campaign or close its other targets.

Reproduce with the command above; wall-clock timing may differ. The script
does not access the network, write shared task state, or call BRC operations.

## 6. Sources, duplicate boundary, and remaining frontier

Scientific source pin: `awdawmip/enterprise-math@39556bf5207aa5ba559a27ec591c1bc1bf43b457`.

Read and compared:

- `research_notes/early_bottleneck_revisit/20260930_EM_DIRECT_B74C91.md`:
  layer-profile theorem and explicit unsolved future sufficiency question.
- `research_tasks/RS-R004-PADIC-TARGET-DEFECT-RESIDUAL-PROFILE-20260930.md`:
  frozen mother question, standard-algebra boundary, and remaining Task outputs.
- Historical original at
  `awdawmip/chatgpt-global-knowledge@8c863c7ec308cfc74dc325af21e41da24d0f10a7:journal/enterprise-math/2026-08-10/20260810T233000+0800-r004-padic-structural-target-defect.md`,
  preserved locally by inventory as `inventory/R004_original_20260810.md`:
  target criterion, scalar monotonicity, residue-field-rank failure, and
  nonmatroid/non-submodular boundaries.
- `src/enterprise_math/r004_causal_identifiability_completion.py`:
  distinct counterfactual-master compiler; not this embedded p-primary module.
- `research_notes/OWNER_A3_A4_QUOTIENT_IMAGE_CORRECTION_20260908.md`:
  related caution about actual quotient images and fine support; different
  object, input language, and claim. No claim of inventing that general caution.

Bounded search of the frozen main's notes, artifacts, records, and docs found
the September profile checkpoint and its transcriptions, but no earlier copy of
the specific same-update collisions or individual-kernel composition failure
above. Inventory independently checked these terms and read the August source.
This is project-local duplicate evidence, not a global literature priority
claim. General isomorphism theorems, finite-module structure, Gaussian counting,
and finite-class information capacity remain prior art.

Current behavioral context read includes `AGENTS.md`, P000, native X6/time,
`docs/PORTABLE_RESEARCH_PROTOCOL.md`, residual-faithful and joint-observer
definitions, and `research_priorities/research_method.json` effective 2026-11-01.
This is TASK-related support to an already selected cold question, not a new
FREE Phase-A discovery or a new registered execution.

**Next discriminating unit:** test inverse coordinate extension/refinement.
The present quotient remembers images of the old target but not arbitrary new
target lifts; a useful next draft must specify admissible lifts and determine
which extension/provenance data makes them compositional. A second distinct
route is efficient p-primary normal forms with full control-label transport and
honest update/reconstruction costs. Neither route should repeat the now explicit
profile-only counterexample. Layer/prefix submodularity, majorization-based
pruning, and the whole Task's completion remain undecided here.
