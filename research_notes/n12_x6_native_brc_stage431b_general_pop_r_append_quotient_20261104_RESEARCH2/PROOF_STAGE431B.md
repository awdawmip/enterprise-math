# Stage431-B — Exact p-POP / r-APPEND future quotient and joint information lower bound

2026-11-04 | Research2 | AUTHOR_SIDE_PROOF / EXACT_INTEGER_EXECUTED / UNREVIEWED / NOT_ADMITTED.

Frozen scientific input: global `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`, Enterprise Math `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`, P000 Git blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`. Current behavioral source read separately: global main `522a1f22156065eabb84d33a95b3c75d22e0cf42`, Enterprise Math main `ff170fce87fb7c93cd8b84279470f1af8b551647`. Parent proof: Stage430-B at `4758ad4875316189cc1b69ac9445b848b4005dfd`. Static ordered signed-X6 directions, no time-axis expansion, native Cell-address claim or physical interpretation.

## Observer and legal future

Let D={+E1,-E1,...,+E6,-E6}. Fix arbitrary integers p>=0, r>=1, n>=p+1, m>=n+r. Let P in D^m be frozen, Q in D^n be editable. The full observer is O(P,Q)=(m,n,endpoint_X6(P),endpoint_X6(Q),J_P,J_Q,K), with endpoint a six-component signed sum, J_s(u,v) the full directed adjacent-step histogram for all ordered u,v in D, and K(P,Q)=sum_{i=1}^{min(m,n)}[P_i=Q_i] at absolute 1-based positions. Future operations are POP_Q (at most p) and APPEND_Q(d) (at most r, each d arbitrary in D), with every interleaving, all intermediate observation traces and operation legality included. There are no P edits or CANCEL. This is a source-labeled, finite-operation observer quotient, not a projection of the unbounded P000 world.

## Theorem 431.1 — exact future equivalence for arbitrary p and r

Within any fiber of the current full observer O, two initial history pairs are equivalent for all budget-legal finite future operation words IF AND ONLY IF the following tuples agree:

T_{p,r}(P,Q)=(Q_{n-p},...,Q_n; P_{n-p+1},...,P_{n+r}).

Thus the exact deterministic quotient inside each O fiber consists of the distinct attained T_{p,r} values. In the requested r=2 case, it is (Q_{n-p},...,Q_n; P_{n-p+1},...,P_{n+2}). The observer is the original joint J/K/endpoint representation with all provenance needed for the stated continuation language.

Proof (sufficiency). At most p original Q labels can be removed, so Q_{n-p} survives in every allowed intermediate word because n-p>=1. The lower Q prefix is never changed. Every Q step subsequently exposed/removed or appended is determined by the retained Q suffix and the literal appended directions of the operation word. Changes in the endpoint_X6(Q) and J_Q involve only these labels, including the predecessor Q_{n-p} when the surviving prefix receives its first appended step. P is fixed, so its endpoint and J stay constant. For K, the untouched prefix's original matching contribution cancels between compared histories because initial K is equal; every newly gained/lost matching position is within absolute positions n-p+1 through n+r, where the tuple retains both the requisite original Q labels (for deletions) and the P labels (for any deletion/append). Hence each next full O and operation legality is determined by current O, T_{p,r}, and the specified operation, and induction applies to every finite budget-legal word.

Proof (necessity). For j=1,...,p, the difference of Q endpoints before and after POP_Q^j identifies Q_{n-j+1} exactly, since signed-X6 primitive steps are distinct six-vectors. After p POPs, one APPEND_Q(x) raises the directed J_Q count at (Q_{n-p},x), exposing the remaining Q_{n-p}; this same one-step probe covers p=0. To recover an arbitrary P_t with n-p+1<=t<=n+r, choose j in [0,p] and k in [1,r] with t=n-j+k: for t<=n+1 take j=n+1-t,k=1, and for t>=n+2 take j=0,k=t-n. Compare K immediately before/after the k-th APPEND in POP^j APPEND(x_1)...APPEND(x_k). Since t<=m, its increment is exactly [P_t=x_k]. Vary the final direction x_k across D: these twelve singleton indicators identify P_t uniquely. Equal complete future traces therefore force equality of every component of T_{p,r}. QED.

## Theorem 431.2 — 2^(p+r) states can be necessary in one full-O fiber

For every p>=0 and r>=1, let L=p+r, n=p+3, m=5L+9, M=3L+3, R=L+1, and choose A=+E1, B=-E1, C=+E2. For each binary word w in {A,B}^L, write b(w)=number of Bs and h_B(w)=number of maximal B-runs. Define h=R-h_B(w)>=1 and z=M-b(w)>=h, V(w)=B^(z-h+1)(AB)^(h-1), t(w)=2+b(w)+h_B(w), and

P(w)=A^3 w A V(w) A^t(w),   Q=C^n.

Every P(w) has exactly m letters, exactly M Bs and R B-runs, starts/ends in A; hence its endpoint (m-2M)E1 and directed J (J_BB=M-R, J_AB=J_BA=R, J_AA=m-1-M-R) are independent of w. Q and its full O data are fixed, and K=0 because P only uses A/B while Q only uses C. All 2^L histories lie in a single complete O fiber.

For each absolute position t in [4,3+L]=[n-p+1,n+r], pick j,k with t=n-j+k as in Theorem 431.1, then probe POP^j followed by k APPEND(A) operations. The K increment on the last APPEND is [P(w)_t=A], identifying the corresponding w letter. All p+r letters are distinguishable by legal probes; hence the 2^(p+r) histories have pairwise different future observation traces. A fixed-length binary encoding of the exact quotient on this fiber requires at least p+r bits. This is a lower bound for the declared bounded-operation observer, not a global bound for arbitrary dynamic extensions.

## Computational evidence and limits

`REPRO_STAGE431B.js` uses exact integer six-vectors, the full 12x12 directed J and indexwise K. It checks every collision pair in each listed finite initial-word domain against budget-legal future operation words, with all 12 native choices for every APPEND. Distinct tuples are verified by finding a full-trace distinguishing word; equal tuples are checked across the entire enumerated future language. Two nontrivial equal-tuple witnesses explicitly vary information outside the retained tuple, one in P and one in Q, and pass all 614 operation words for p=1,r=2. Separate families check equal current observer and decode every bit for (p,r)=(0,2),(1,2),(2,2),(3,2),(2,3),(4,2). All arithmetic is exact. Finite evidence independently checks specified domains; general quantifiers follow from the proofs above.

The new general statement resolves Stage431-B's two-APPEND question and extends it to every finite r>=1. It retains the existing frozen scientific pins and does not establish an unrestricted infinite-horizon compression theorem. Native role/CLAIM/Result and independent review are separate authorization states.

## Reuse and next unit

Reuse Stage430's typed X6 path-observer quotient and Stage428's indexed boundary-K update. Stage432-B should integrate the full retained T_{p,r} information into an executable unequal-length Euler/J/K dynamic program, compare exact counts against brute-force histories on small inputs, and account explicitly for input conversion, memo state, integer bit complexity, and output recovery. An independent question is the exact minimal binary storage of T_{p,r} conditioned on a particular current-O fiber, beyond the existence lower bound p+r.
