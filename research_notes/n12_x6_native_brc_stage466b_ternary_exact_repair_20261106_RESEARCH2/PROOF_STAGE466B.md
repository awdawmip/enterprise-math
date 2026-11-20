# Stage466-B — Exact multi-direction Q-probe repair and ternary BRC counting

Date: 2026-11-06. Researcher-ID EM-DIRECT-6E5213; Research-Activity-ID RA-1344CA69A39C65FBDFFF8FB6. Classification: AUTHOR_SIDE_THEOREM / EXACT_INTEGER_EXECUTED / UNREVIEWED, no formal CLAIM. Parent scientific checkpoint Stage465-B at 35b8bc22d2b68fed18e6362eaf66933a8ea5170d. Frozen scientific sources: GLOBAL bf84bd7c61a2444b59b1da96be57df0e9ae47e53, EM 2af3fc484eb11060b69e0afc1b562bcaf5ad1419, P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Current normative sources were read separately on 2026-11-06.

## Exact original and future observer
Original distinct ordered sources P,Q have lengths 2<=m<n and fixed first original direction P1=Q1=A; their original alphabet is any subset of the 12 signed native X6 directions. At each legal action state we retain both lengths, each source's complete signed six-axis displacement, each source's complete directed 12x12 adjacent-direction matrix and K=sum_{i<=min(|P|,|Q|)}[P_i=Q_i]. Future labeled operations POP_P, POP_Q and APPEND_P(u), APPEND_Q(u) use all 12 possible native signed directions and finite budgets (hP,hQ,r,s). POP may remove a letter appended earlier. Future equivalence means equality of *every* legal labeled intermediate-observation tree. T0 is the complete tree with s=0; Ts is the tree with s>=1.

## Theorem 466.1 — minimal distinguishing relative Q-APPEND key
Within a fixed initial full-observer fiber, for any finite hP,hQ,r>=0 and s>=1, two histories H and H' have the same Ts if and only if they have the same T0 *and* P_j=P'_j for all

W = {j integer: max(2,n-hQ+1) <= j <= min(m-1,m-hP-1)}.

If W is empty, Q APPEND induces no additional distinction. The key is *relative* to T0 and is not an assertion that the W coordinates are independent within each initial fiber.

Necessity: Ts contains every T0 action tree. For each j in W, perform n-j+1 <= hQ POP_Q operations, leaving the original Q prefix of length j-1, with P unchanged. Then APPEND_Q(u) once, separately for all 12 native directions u. Its observed K increase equals [P_j=u]. The vector of 12 tests identifies P_j. Thus two histories differing at any W direction are Ts-distinct.

Recoverability outside W: from T0, for each j>=max(1,m-hP), perform m-j POP_P operations to obtain original P prefix through j. Its first letter remains A. For every native direction x, the observed directed edges satisfy outdeg(x)-indeg(x)=[x=A]-[x=P_j]. These equalities recover the last letter P_j (including j=1). P1=A is fixed; P_m is also available at the no-action state.

Sufficiency: consider any extended action prefix. Erase each APPEND_Q and each POP_Q that merely removes a known Q-appended letter. The remaining original-Q-POP operations and all P operations form a legal T0 action prefix using no more than the base budgets. Thus T0 determines the exact P-side observation, the original Q-prefix observation and the match count between P and that original Q prefix. The Q-appended suffix and all its native directions, signed displacement and internal adjacency edges are action-known; the connecting adjacency uses the last direction of the remaining Q prefix, recovered from its directed edge matrix and original first A (or the prefix is empty). An appended Q direction at index j can compare with an original P_j only if j>=n-hQ+1: each POP_Q, even of an appended letter, costs from the same hQ budget. If original P_j exists, its direction is either the fixed P1, recoverable from T0 for j>=m-hP, or retained as a W label. If P_j was replaced by an APPEND_P action it is action-known. Therefore every incremental K term of the Q-appended suffix is equal, and so are all full future observations by induction. This proves the stated factorization for arbitrary s, hP, hQ and r.

Corollaries: When original P uses only two signed directions, original Q_j is recovered by its POP and [P_j=Q_j] by the K decrement, so the base tree also recovers P_W; Q APPEND is fully redundant, recovering Stage465-B. For a ternary or larger alphabet the identity of P_j, not only one equality bit, is the general repair object. In the nondegenerate hP<m-1 case, a new potentially hidden index first becomes accessible at hQ=n-m+hP+2, consistent with the Stage465-B threshold.

## Theorem 466.2 — exact positive-integer BRC population in a growing visible ternary family
Fix A=+E1, B=+E2, C=+E3 as real native signed-X6 directions. For k>=1, 0<=b<=k and n>m=2k+1, let the declared source population be
P=A X1 A X2 ... A Xk A, Xi in {B,C}, exactly b of the Xi are B, and Q=A repeated n times.
Only Q operates, with up to hQ<=n POP operations and one APPEND_Q operation in any of the 12 native directions; hP=r=0. There are binom(k,b) distinct original source histories.

All originals share the complete initial observation: P displacement has A count k+1, B count b, C count k-b; P adjacency AB=BA=b and AC=CA=k-b; Q has n-1 AA edges; initial K=k+1. All Q-POP-only full future trees agree, since every variable Xi is different from the original Q direction A.

Let v be the number of even variable positions 2i with 2i>=max(1,n-hQ+1), and h=k-v. Theorem466.1 makes the visible ordered suffix word w=(X_{k-v+1},...,X_k) the exact equivalence label. If it has a B letters, its population is M(w)=binom(h,b-a), supported iff 0<=b-a<=h. Consequently
qF = sum_{a=max(0,b-h)}^{min(v,b)} binom(v,a)
and |F| = sum_a binom(v,a)binom(h,b-a) = binom(k,b).
These are Boolean support, exact class population and conserved source-distinct mass, not a total-only quotient.

Proof: if two visible words differ, select a differing even index 2i and perform n-(2i)+1 Q POPs and APPEND_Q(B), observing different K. For identical visible words, the key theorem gives identical futures. The hidden h variables can place the remaining b-a B labels in binom(h,b-a) ways; Vandermonde yields population conservation.

Rank/unrank: lexicographically B<C, define F(0,z)=1 if 0<=z<=h else 0, and F(t,z)=F(t-1,z-1)+F(t-1,z). Then F(v,b)=qF. On a C step, rank adds the supported B-prefix branch size F(t-1,z-1); on a B step decrement z. Unrank uses the same comparison. The DP has O(v(k+1)) arbitrary-precision integer entries and a rank/unrank query takes O(v) integer operations after preprocessing; one class mass uses a binomial coefficient. No full history or full class enumeration is needed in the large case.

## Executed verification
The companion standard-library Python program checks every k=1..5, b=0..k, n=2k+4 and hQ=0..n: 20 families, 240 exact parameter cases, 496 supported rank/unrank and class population checks. In 170 original-history-pair comparisons it evaluates full native signed endpoints, directed 12x12 edge counts and K for every Q original-prefix POP state and all 12 APPEND_Q choices. Because s=1, subsequent POP of the newly appended direction returns to an already represented prefix state; this covers the remaining Q-only branches. Every assertion passed.
Large exact counts without history enumeration: (k,b,v)=(30,14,18) gives qF=261137 and |F|=145422675; (50,23,34) gives qF=16969401736 and |F|=108043253365600. The complete executed JSON and actually executed source are included here.

## Next science and admission
Stage467-B: retain the exact relative key, then count full ternary initial-observer fibers with arbitrary P/Q words and both sources' POP/APPEND budgets. Develop a directed-edge/endpoint/K constrained BRC transfer; test small complete fibers before asserting polynomial support rank/unrank. This author-side theorem is offered for independent Driver audit; no canonical result/admission is asserted.
