# R5: exact future residual for multiple named Set controls

Date: 2026-11-16 (Asia/Shanghai). Frozen scientific pin: 435e77af0d180eac32bd1f9c4c464bc4010b7551. Evidence: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_INDEPENDENTLY_REVIEWED.

**Model boundary.** This is the inherited auxiliary radius-two indexed-center graph/cycle repair model, not an assertion about native X6 Cell geometry. The P000 foundation and ACTIVE worldview remain unchanged. The binary mask marks old-helper unavailability. Names and branch provenance are retained prior to the observer quotient.

**Prior exact interfaces.** Theorem sources at immutable Enterprise Math commit 258555f482c0d480b0d95a3d1c004dbb9c5c688a: research_notes/portable_direct/r5_branching_cactus_horizon_20261115/BRANCHING_CACTUS_AND_TWO_STEP_RESIDUAL_THEOREMS.md and SINGLE_VERTEX_COMMAND_MINIMAL_FUTURE_QUOTIENT.md. In the cyclic necklace of k>=3 triangles, with named unavailable-spine mask u,

\[
\kappa_a(k,u;2)=5k+q(u),\quad q(u)=\sum_{i\bmod k}u_i u_{i+1},\quad \kappa_{ab}=6k.
\]

Fix a named subset J of control vertices. Each permitted command Set_i(b), i in J, b in {0,1}, overwrites that named bit only. Observation includes q at the empty word and after every finite command word; it does not admit other operations. Equivalence is equality of all these indexed observations.

## Theorem A. Arbitrary nonnegative-weight graphs and control subsets

Let G=(V,E) be a fixed finite named simple graph with known nonnegative weights w_{ij}. Define Q(u)=sum_{ij in E} w_{ij}u_i u_j on binary masks. For J subset V and K=V\J set

\[
C(u)=\sum_{ij\in E[K]}w_{ij}u_i u_j,\qquad
b_i(u)=\sum_{j\in K:ij\in E}w_{ij}u_j\quad(i\in J),
\]
\[
d_i=\sum_{j\in J:ij\in E}w_{ij},\qquad
A(u)=\{i\in J:b_i(u)+d_i>0\}.
\]

Then the exact minimal future-observation equivalence relation is

\[
\boxed{u\equiv_J v\iff
 C(u)=C(v),\quad b_i(u)=b_i(v)\ \forall i\in J,\quad
 u_i=v_i\ \forall i\in A(u).}
\]

When the C and b values agree, the active set A is common to the states. Consequently the tuple (C,b,(u_i)_{i in A}) is a sufficient residual and describes precisely the minimal quotient classes. Any two distinct classes can be separated by an allowed command word of length at most |J|.

**Proof.** Every command word has the same final state as some partial assignment of J; repeated writes are resolved by their last write. Fully setting J to x reveals

\[
P_u(x)=C(u)+\sum_{i\in J} b_i(u)x_i+
\sum_{ij\in E[J]} w_{ij}x_ix_j.
\]

If all future observations are equal for u and v, P_u=P_v on the Boolean cube. Evaluation at x=0 and x=e_i proves equality of C and all b_i, since the last sum has degree two and the fixed graph is common.

If i in A, set every other vertex of J to 1 and leave i unchanged. The final two observations differ by (u_i-v_i)(b_i+d_i). Since b_i+d_i>0, future equality forces u_i=v_i. Conversely, identical tuples yield identical P, and P is independent of each inactive variable: nonnegativity forces b_i=d_i=0 to imply every incident controlled coefficient vanishes. For any partial assignment, values on active unset bits agree and inactive bits cannot matter, so every output agrees. These partial assignments represent all finite words; any inequality is witnessed either by a full assignment (at most |J| commands) or by setting J\{i} to 1 (|J|-1 commands). QED.

For the cycle with unit edge weights C counts 11 edges internal to the frozen complement K; b_i counts unavailable neighbors outside J. This is an exact nonnegative branch-sum observer; the named edge identities are retained through the proof of quotient sufficiency. No native BRC execution or X6 transport is asserted.

## Theorem B. Two adjacent named controls: exact state count

For G=C_k, k>=3, J={0,1}, let N_k denote the number of full-future scalar-observation equivalence classes. Then

\[
\boxed{N_3=8,\quad N_4=16,\quad N_k=16k-52\text{ for }k\ge5.}
\]

For example, N_6=44 versus 64 raw states; N_12=140 versus 4096 raw states.

**Proof.** Each controlled vertex has the other as a controlled neighbor with weight 1. Both are active, so their original two bits give four independent possibilities. For k>=4 the complement K is a path of n=k-2 vertices. Its endpoint values determine (b_1,b_0), and C counts adjacent 11 edges within the path.

For n>=3, endpoints 00 allow C=0,...,n-3 (n-2 values); endpoints 01 and 10 each allow C=0,...,n-2 (n-1 values each); endpoints 11 allow C in {0,...,n-3} union {n-1} (n-1 values). Each range is sharp: form a contiguous 1-run of the desired length, with appropriate separated endpoint 1s in the 11 case; the all-one path supplies n-1. The number of distinct triples (C,b_0,b_1) is (n-2)+3(n-1)=4n-5. With four controlled-bit choices, N_k=4(4(k-2)-5)=16k-52 for k>=5. At k=4 the two complement endpoint bits give four path configurations, hence 16 classes. At k=3 the complement has a single bit, producing two common boundary-coefficient configurations times four controlled-bit assignments, hence 8. Apply Theorem A for minimality. QED.

## Theorem C. Source-labeled optimal repairs need a finer quotient

For k=6, J={0,1}, consider

\[
u=(0,0,0,1,0,0),\qquad v=(0,0,0,0,1,0).
\]

The sole unavailable helper is 3 in u and 4 in v. Both share (C,b_0,b_1,u_0,u_1)=(0,0,0,0,0), hence their scalar future-readout traces agree under **every** named Set word on J. The inherited cyclic repair formula gives both individual optimal old-library sizes equal to 30.

A single old-source-labeled library valid under both masks could use neither helper 3 nor helper 4. It would therefore also be feasible under the union mask u OR v, which has precisely one adjacent unavailable pair (3,4). The same exact source-aware optimization theorem gives minimum 31 for that union mask. Consequently **no common library of size 30 is source-valid for both u and v**. This proves that source-optimal witness production requires distinguishing at least some masks that the scalar future-readout quotient merges. It does not assert an exact minimum size for the general source-aware quotient.

## Executable evidence, limits and continuation

The companion standard-library checker regenerates every q trace after named partial assignments and compares the complete equivalence partitions with the theorem residual. Locally executed evidence:

- 242 exhaustive (k,J) cycle families, k=3,...,8, 1<=|J|<=3, all 2^k masks and every partial assignment;
- 160 fixed-seed nonnegative integer-weight graph instances, n=3,...,6, all binary masks and all command partial assignments for each instance;
- exact adjacent-two-control class counts k=3,...,14, plus independent partition comparisons through k=10;
- exhaustive graph-cover source-library minima 30,30,31 for the two six-spine configurations and their union.

Observed status: PASS_R5_MULTI_CONTROL_RESIDUAL_AND_SOURCE_SEPARATION. Universal scope follows from the proofs; finite checks are explicit cross-checks and independent review is pending. Source linkages and execution artifacts are on this Draft PR; no Result, Review, protected Activity checkpoint or CLAIM has been written as part of this theorem.

**Next question.** Construct the exact minimal **source-aware** finite transducer for a fixed set J of controllable vertices: it must report optimal cardinalities and recover feasible named old-library sources after every allowed command. Compare the direct full availability mask with provenance-preserving graph-factor states, using the separating pair above as a regression witness.

Historical contributor metadata: EM-DIRECT-B78E55 / RA-33C87C2B703418F0706695E9. These public identifiers are provenance, not an authenticated live execution capability.