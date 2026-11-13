# PREFIX-625 addendum — native X6-BRC rank-16 image persists at every finite horizon

Date: 2026-11-09 (Asia/Shanghai). Scope: original frozen positive typed X6-BRC action algebra, science pin f42f2906d77f24085c123f3ccfe9667d41caa96d. Status: author-side exact proof, independent mathematical review pending. This addendum extends the PREFIX-625 two-generation theorem and PREFIX-624.

## Theorem A — universal endpoint rank 16

Let A(z) be the original 96x96 port transition obtained by summing all 576 native source-labelled BRC actions, with nonnegative gate z. For every finite n>=2 and every nonnegative sequence g_1,...,g_n, write F_n=A(g_n)...A(g_1). Then

\[
\boxed{\operatorname{rank} F_n = 16 \quad(n\ge2,\ g_i\ge0).}
\]

For n=1, the original rank is 32 at z=1 and 33 otherwise (PREFIX-624).

Use zero-based index sets

    R=[0,2,4,6,8,10,12,14,32,34,36,38,48,50,52,54]
    C=[0,4,8,12,16,18,20,22,24,28,42,46,56,60,64,68]

Set A_0=A(0), E=A(1)-A(0), T=A_0^2, U=A_0E, V=EA_0, K=T[R,C]. Exact native action enumeration gives E^2=0 and det K=-65536. Define

\[
G(z)=T[:,C]+zV[:,C],\qquad H(z)=T[R,:]+zU[R,:].
\]

PREFIX-625 proved the exact two-step factorization A(b)A(a)=G(b)K^{-1}H(a). Define constant 16x16 matrices:

\[
N_0=K^{-1}(A_0G(0))[R,:],\qquad
N_1=K^{-1}(A_0V[:,C])[R,:],\qquad
N(z)=N_0+zN_1.
\]

The accompanying exact checker exhaustively verifies four 96x16 native coefficient identities:

\[
A_0G(0)=G(0)N_0,\quad
A_0V[:,C]=G(0)N_1,\quad
EG(0)=V[:,C]N_0,\quad
EV[:,C]=V[:,C]N_1=0.
\]

Multiplication of these identities proves the polynomial identity

\[
\boxed{A(c)G(b)=G(c)N(b)}
\]

for all real b,c, because the bc coefficient vanishes. The checker finds N_1 has precisely one nonzero entry, zero-based (row 2,column 7)=1/2, det N_0=49152 and det(N_0+N_1)=65536. Consequently its determinant is affine and

\[
\boxed{\det N(z)=16384(z+3)=2^{14}(z+3).}
\]

This is strictly positive for every z>=0. By induction,

\[
\boxed{
F_n=G(g_n) N(g_{n-1})\cdots N(g_2)K^{-1}H(g_1).
}
\]

For n=2 the middle product is the identity. Since G(z)[R,:]=K and H(z)[:,C]=K, the *same* 16x16 endpoint minor satisfies

\[
\boxed{
\det F_n[R,C]
= -65536\,16384^{n-2}\prod_{j=2}^{n-1}(g_j+3)\ne0
\quad(g_j\ge0).
}
\]

The factorization establishes rank <=16 and this minor rank >=16 for arbitrary finite length and arbitrary nonnegative gates.

## Theorem B — all-horizon tagged history rank and fixed 48-read repair

Let J_n(g_1,...,g_n)r record the complete nonaggregated weight of each ordered length-n native-action path including its action labels and original source port. There are 96*6^n labelled structural path coordinates (including zero-weight paths). Then

\[
\boxed{\operatorname{rank} J_n =64,\qquad n\ge1,\quad g_j\ge0.}
\]

Proof: precisely 64 original input ports have a positive outgoing typed action. At zero gate the original 576-action graph has, from each of these 64 live ports, at least one positive edge to another live port, as exhaustively checked by the checker. Inductively every live input has at least one positive labelled path for every finite length. These paths persist under all nonnegative gates. Different initial ports occur in disjoint complete label-coordinate families, so their 64 columns are independent; the other 32 columns vanish.

For known full gate sequence and full endpoint state F_n r, reconstructing all labelled n-step path weights for any nonnegative predecessor r requires exactly

\[
\boxed{48\ \text{extra linear scalar predecessor observations, for every }n\ge2.}
\]

Necessity follows from the rank difference 64-16 and a positive-cone interior perturbation of each missing kernel direction. For sufficiency, choose the same **fixed** 48 original source port coordinates D=live\C for *every* horizon and gate sequence. Read r_D and recover the remaining live precursor coordinates by

\[
\boxed{r_C=(F_n[R,C])^{-1}((F_n r)_R-F_n[R,D]r_D).}
\]

The determinant above guarantees invertibility. With all 64 live precursor ports recovered, evaluate each typed ordered path weight from the original action labels. The earlier n=1 minimum is 32 extra scalar reads at z=1 and 31 otherwise.

This theorem covers **arbitrary nonnegative original precursor 96-port states, known gates, linear extra precursor observations, and complete source/action-labelled paths**. The restricted four-point reachable family with supplied ancestral phases has a different, earlier one-scalar repair result.

## Exact native certificate

Companion executable PREFIX625_any_horizon_rank_checker.py imports the exact original BRC 48-phase/96-port/576-action enumerator from PREFIX625_native_two_generation_path_checker.py at the same PR commit; computes the four 96x16 symbolic coefficients, checks N_1's unique entry, determinant coefficients, and positive live-successor property. It verifies complete exact 96x96 factorization, fixed minor and exact original source-port recovery for horizons 2,3,4,5,6 at integer, zero and rational gates. All assertions pass.

The universal claim is established by the complete coefficient identities and graph induction; finite tested horizons corroborate the implementation. Only the original native positive BRC action operator is used; no classical evolution substitute or phase cancellation is introduced.

## Next research

Determine the minimal number of additional path-history readouts within the **actual restricted four-point BRC reachable family**, conditional on which ancestral phase vectors and intermediate gates are already known. Compare explicit labelled-output cost 96*6^n with compressed exact path representation and its decoding cost.

This is author-side research evidence; no formal CLAIM, Result, independent Driver review or Foundation admission is asserted.
