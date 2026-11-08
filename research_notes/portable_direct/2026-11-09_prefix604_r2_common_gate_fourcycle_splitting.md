# PREFIX-604-R2: Common 12+4 gate four-cycle split of the native X6-BRC zero-axis tail

Date: 2026-11-09 (Asia/Shanghai). Status: AUTHOR-SIDE EXACT PROOF + EXECUTED VERIFICATION; INDEPENDENT DRIVER REVIEW PENDING. Scientific inputs remain frozen at \`f42f2906d77f24085c123f3ccfe9667d41caa96d\`; current behavioral rules are separate. Dependency: PREFIX-596 (original typed 96-port → positive 48-phase bridge), PREFIX-599, and PREFIX-602/603 (exact common 16D tail + rank-two order defect), preserved in [PR #1826](https://github.com/awdawmip/enterprise-math/pull/1826). P000/worldview unchanged.

## Exact scientific scope

Use the *original* 48 STAR phases from triads \`(1,3,6),(1,4,5),(2,3,5),(2,4,6)\`, 96 original bit ports and 576 individually tagged actions. Fix six source-axis weights \`(1,1,1,1,0,0)\`. In the PREFIX-596 original-to-phase exact observation bridge, the 48×48 native-derived transition \`Q(z)\` has rows on axes 5,6 equal to zero; on an active phase row \`i\` the three original successors \`j∈N(i)\` have coefficient 1 if \`i=g\`, coefficient \`3+z\` if \`j=g\`, otherwise 2, with original gate target \`g=4\` (zero-based). This is an exact *phase observer* of the pinned BRC source; it does not claim to reconstruct all tagged path histories.

As in PREFIX-602, let \`A=Q(1)\`, \`G=Q(2)-Q(1)\`, \`V=im(A²)\` of dimension 16. Using the deterministic 16 pivot columns of \`A²\`, define \`E:Q^16→Q^48\`, and its left inverse \`K:Q^48→Q^16\` from the pivot rows. Then \`KE=I\`, \`Q(z)E=ET(z)\`, \`T(z)=T+(z-1)H\` where \`T=KAE\`, \`H=KGE\`. The original 48 phase observations after two steps are recovered exactly by \`y=Ev\`.

## Theorem 604.1: one fixed common gate-independent projector

For **all real gate parameters** (the admissible native BRC range is \`z≥0\`), the 16D tail has a fixed direct sum

\[
\boxed{\mathbb Q^{16}=U_4\oplus Z_{12}}
\]

such that every \`T(z)\` preserves both spaces; \`T(z)|Z\` is independent of z and has fourth power \`16 I_{12}\`. On \`U\`, in one fixed basis, the transfer is

\[
\boxed{B(z)=
\begin{pmatrix}
0&0&0&4(z+3)\\
1&0&0&0\\
0&1&0&0\\
0&0&1&0
\end{pmatrix}.}
\]

In particular this four-dimensional gate-dependent *transfer* has nonnegative entries at all admissible gates, although the complete input and output coordinate projectors are rational and may contain signs.

**Constructive proof.** \`H\` has rank one. Pick the lexicographically first nonzero entry \`H[i0,j0]\`; write \`u=H[:,j0]\`, \`h=H[i0,:]/H[i0,j0]\`. Then \`H=uh\`. Define

\[
W=[u,Tu,T^2u,T^3u],\qquad
O=\begin{pmatrix}h\\hT\\hT^2\\hT^3\end{pmatrix},\qquad M=OW.
\]

The exact rational checker obtains the **entire** matrix identity

\[
\boxed{
M=\begin{pmatrix}
0&0&0&4\\0&0&4&0\\0&4&0&0\\4&0&0&0
\end{pmatrix},\quad\det M=256\ne0.}
\]

Set \`L=M^{-1}O\`, \`P=WL\`, \`U=im(W)\`, \`Z=ker(O)\`. Complete exact 16×16 matrix verification gives

\[
LW=I_4,\quad P^2=P,\quad (I-P)TP=PT(I-P)=0,
\]
\[
(I-P)H=H(I-P)=0,\quad T^4=16I_{16},\quad
L[T+(z-1)H]W=B(z).
\]

Hence \`dim(U)=4\`, \`dim(Z)=12\`, \`U∩Z={0}\`, and the two parts are simultaneously invariant. Since \`H=PHP\`, the 12D part is **fully gate-insensitive** for arbitrary gate changes, not merely fixed z.

**Exact reconstruction.** For any nonnegative original phase input \`y_0\`, first compute two original typed-BRC-derived updates \`y_2=Q(z_2)Q(z_1)y_0\` and put \`v_2=Ky_2\`, \`c_2=Lv_2\`, \`f_2=(I-P)v_2\`. For any subsequent **ordered** gate inputs \`q_1,...,q_n\`:

\[
\boxed{y_{2+n}=E\left(
W B(q_n)\cdots B(q_1)c_2+
16^{\lfloor n/4\rfloor} T^{\,n\bmod4}f_2
\right).}
\]

All 48 phase coordinates are restored exactly at every horizon, including nonstationary sequences. The first two transitions can use arbitrary admissible gate weights because the common 16D image is independent of the gate inputs.

**Four-cycle equation.** The 4D gate coordinates have the update
\[
(c_0,c_1,c_2,c_3)\longmapsto
(4(q+3)c_3,c_0,c_1,c_2),
\]
and the fully symbolic identity
\[
\boxed{B(q_4)B(q_3)B(q_2)B(q_1)
=4\,\operatorname{diag}(q_4+3,q_3+3,q_2+3,q_1+3).}
\]

For a supplied length-n gate sequence, the gate-dependent computation therefore requires O(n) scalar moves/products and a four-coordinate state. The gate-free part needs only one of \`I,T,T²,T³\` plus an exact power of 16. For batch endpoint queries sharing a gate sequence, the four-coordinate monomial product can be reused. This is arithmetic-operation accounting on the exact observer; variable-size integer bit costs, original two-step conversion, 48-phase reconstruction and any 96-port observation bridge still belong in endpoint benchmarks.

## Theorem 604.2: exact maximal order-blind quotient

Let \`J=HT-TH\`, the PREFIX-603 rank-two immediate gate-swap defect. Complete rational rank checks establish

\[
\begin{aligned}
&\operatorname{rank}H=1,\ 
\operatorname{rank}[H,TH]=2,\ 
\operatorname{rank}[H,TH,T^2H]=3,\ 
\operatorname{rank}[H,TH,T^2H,T^3H]=4,\\
&\operatorname{rank}J=2,\ 
\operatorname{rank}[J,TJ]=3,\ 
\operatorname{rank}[J,TJ,T^2J]=4.
\end{aligned}
\]

Both generated spans equal \`U=im(W)\`; it is the **smallest (T,H)-invariant subspace containing im(H)** and also the smallest such subspace containing \`im(J)\`. For any linear quotient through which all varying-gate actions descend, gate independence forces \`im(H)\` into its kernel, so invariance forces \`U\` into that kernel. Thus **12 is the maximum dimension of a common gate-independent quotient**; \`V/U\` attains it. For all gate weights a,b the commutator is \`[T(a),T(b)]=(a-b)J\`. If the descended actions commute for every a,b, \`im(J)\` must similarly be killed; closure again forces U. Thus **12 is also the maximum dimension of the all-sequences order-blind quotient**.

This result strengthens PREFIX-603: a single adjacent swap has a **rank-two immediate defect** but its smallest future-operation-closed residual space has **dimension four**. The original full phase observer remains order-sensitive; reconstruction retains the 4D component instead of discarding it.

## Exact checker / evidence / limits

\`PREFIX604_R2_gate_fourcycle_12plus4_stacked_checker.py\` imports the predecessor's exact STAR/phase source reconstruction and full 48→16 intertwiner. It verifies the full 16×16 projector relations, rank-one H, rank-two J, rank-growth certificates, the symbolic four-gate identity and **1,683 exact equality comparisons** of complete 48-phase outputs from 51 nonnegative sources and seven different gate sequences after their two-step transient. All executable assertions passed with SymPy exact integer/rational arithmetic; the universal result is established by matrix identities, while finite tests check implementation. Data: \`PREFIX604_R2_gate_fourcycle_12plus4_results.json\`.

No classical π/trigonometry, matrix-exponential fallback, approximate native residual or physical heartbeat calibration is used. Sequence indices encode typed operation order, not assumed physical duration. Observer-safe reduction applies to the complete *48-phase linear readout and all future gate sequences* of this fixed-axis family; the original 96 ports, tagged path source, branch provenance and historical joint relations stay in the pinned typed BRC carrier. Individual raw path labels are not reconstructed by 12+4 phase coordinates.

**Next discriminator:** benchmark the complete input-to-original-96-port-output pipeline and multiquery workloads against optimized 96/48 and generic 16D propagation, including conversion, bigint costs and gate-length; separately test existence of a positive 12+4 *input/output* realization for the original nonnegative phase cone (the positive 4×4 B block alone does not settle that factorization).

**Control scope:** independent author-side portable research artifact; no shared Task CLAIM, Native Result, independent review or Foundation promotion is asserted.
