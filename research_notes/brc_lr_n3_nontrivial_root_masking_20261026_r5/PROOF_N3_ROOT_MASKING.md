# N=3 nontrivial informative-step counterexample: universal four-scalar LR compression without strong lumpability

2026-10-26. **AUTHOR-LEVEL EXACT ALGEBRAIC THEOREM**, locally checked with rational arithmetic. External finite two-measure tree only; independent Research Driver review, source-native frozen Result, P000/X6/Heartbeat transfer and external literature priority are NOT claimed.

## Immutable input and real authority

Account canonical GLOBAL_KNOWLEDGE_V1: awdawmip/chatgpt-global-knowledge main@3c2f14ffb124902dc0fe1050a8bc11811842ed48. At that snapshot read 00_BOOTSTRAP.md, OPERATING_MANUAL.md, Enterprise Math router, P000_STARTUP.json, ACTIVE worldview and mathematical/BRC rules. P000 original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc agrees with the projection. Enterprise Math project research input: awdawmip/enterprise-math main@bbd71dbafe72fe012e3a79dd32e55adabf3b5b7e; portable research protocol blob ca5de2d680d2439ff4b67c2c55fbd4159813cd5c. Exact predecessor: research_notes/brc_lr_mixed_fiber_n2_20261026_r5/PROOF_MIXED_LR_N2.md, blob cc64440323fa0f2880e00e2600e959ef16a0973d; also N=2 all-unit masking note blob ab5c2ea1d6f5529dafb237646f710c908077f5f4. This work tackles their N>=3 open question without repeating the N=2 result.

Connected GitHub identity awdawmip had repository push permission. Native task listing returned CONTROL_QUOTA; attempting own em_session_start returned STATIC_READONLY_SCOPE_DENIED with operation_sent=false. Thus original active owner, native CLAIM, service session, formal Result and independent review are UNVERIFIED; GitHub author evidence is not a canonical TASK result.

## Exact model

Two strictly positive laws P,Q on a finite ordered tree, horizon N=3. Stopping and declaring P/Q is allowed at depths 0,1,2, while sampling also is allowed until depth 3; final declaration at depth 3 is mandatory. Randomized actions must be independent of which of P,Q is true. The observer is

O(policy)=(P[declare Q], Q[declare P], E_P tau, E_Q tau).

Full policy may depend on ordered raw history. Compressed behavioral policy sees time t and ONLY exact global likelihood ratio L_t=P(history)/Q(history), with no additional persistent hidden memory.

At depth 1 raw histories a,b each have P=Q=1/2, hence L1=1. At depth 2 the global likelihood ratio R=L2 has support (1/2,1,3/2). Its conditional Q probability rows are

| h | Q(R=1/2|h) | Q(R=1|h) | Q(R=3/2|h) |
|---|---:|---:|---:|
| a | 1/4 | 1/2 | 1/4 |
| b | 1/3 | 1/3 | 1/3 |

Conditional P row is r times its Q row, which is positive and normalized because the row's Q mean of R is 1. At depth 3 sample a genuinely informative signal S with Q(S=1/2)=Q(S=3/2)=1/2, P(S=1/2)=1/4, P(S=3/2)=3/4, independent of raw history and R under either law. Final LR L3=R*S. All 12 raw depth-3 leaves have strictly positive P,Q probabilities. Strong LR-lumpability FAILS at time 1 because the Q conditional distributions of R from a,b differ. At time 2 the LR-relative S kernel is common.

**Theorem.** Despite time-1 strong lumpability failure and despite the nontrivial informative third observation, every full-history randomized policy has a time/exact-LR-only behavioral policy with the same entire four-vector O.

## Proof: Bellman supports for arbitrary REAL coefficients

For any A,B,C,D in the real numbers minimize J=A eP+B eQ+C tP+D tQ. At LR r the Q-mass cost of immediate optimal classification is H(r)=min(A*r,B). This is a concave function of positive r. Put gamma=C+D. At t=2 the optimal remaining cost per incoming unit Q mass is

phi(r)=min{H(r), C*r+D+[H(r/2)+H(3r/2)]/2}.

This formula is exact even for signed sampling costs. Both options inside min are concave in r, hence phi is concave: nonnegative sums and affine addition preserve concavity, and the pointwise minimum of concave functions is concave by hypograph intersection. Moreover phi(r)<=H(r).

Write m=H(1), f_h=E_Q[phi(R)|h] and d_h=m-f_h. By direct Bellman recursion including ROOT stop, the minimum full-history objective equals

V_full=min{m, gamma+(1/2)min(m,gamma+f_a)+(1/2)min(m,gamma+f_b)}
      =m+min{0, gamma-[(d_a-gamma)_+ +(d_b-gamma)_+]/2}.

At time 1 the LR-only controller cannot distinguish a,b and must choose one common action, while its time-2 Q row if sampling is the pooled mu_bar=(7/24,5/12,7/24). Since the downstream S experiment is shared, phi(r) is available to that controller. With dbar=(d_a+d_b)/2 its exact optimum is

V_LR=m+min{0, gamma-(dbar-gamma)_+}.

These are full real-coefficient support formulas, not numerical approximations.

Put alpha_a=1/4, alpha_b=1/3. Both Q rows have form (alpha_h,1-2alpha_h,alpha_h). Write

G=2phi(1)-phi(1/2)-phi(3/2) >=0,
d0=m-phi(1)>=0.

The first inequality is midpoint concavity, the second is phi<=H. Therefore f_h=phi(1)-alpha_h*G, so d_h=d0+alpha_h*G>=0. Hence

dmin=d0+G/4; dbar=d0+7G/24 <=2(d0+G/4)=2dmin.

**Root masking lemma.** For nonnegative d_h with weighted mean dbar<=2dmin and any REAL gamma,

min{0,gamma-E[(d_h-gamma)_+]}=min{0,gamma-(dbar-gamma)_+}.

Proof: if gamma<=dmin, every positive part is d_h-gamma and both sides coincide. If gamma>dmin, gamma>0 and E[(d_h-gamma)_+] <= E[(d_h-dmin)_+]=dbar-dmin<=dmin<gamma; the compressed positive part is no larger by convexity. Both outer minima therefore are zero. QED.

It follows that V_full=V_LR for EVERY real (A,B,C,D), not only for nonnegative sampling costs or an enumerated grid.

## Proof: support equality yields policy-by-policy replication

Here the compressed observer image is a genuine compact convex occupancy-flow polytope, including root action. Define root Q-masses x0P,x0Q,s>=0 with sum 1; first-LR=1 action masses x1P,x1Q,c>=0 with sum s. For r in {1/2,1,3/2} let y_rP,y_rQ,y_rC>=0 split the depth-2 incoming Q mass c*mu_bar(r). For each final u in {r*s_j}, incoming Q mass m_u=sum_{r,j:r*s_j=u} Q(S=s_j)*y_rC; split it into z_uP,z_uQ>=0 with sum m_u. These are bounded LINEAR constraints. Each feasible flow is realized by legal time/exact-LR action probabilities (arbitrary on unreachable states), including collisions of several parent r values at the same terminal u.

Its observer coordinates are LINEAR in flows:

eP=x0Q+x1Q+sum_r r*y_rQ+sum_u u*z_uQ;
eQ=x0P+x1P+sum_r y_rP+sum_u z_uP;
tP=s+c+sum_r r*y_rC;
tQ=s+c+sum_r y_rC.

These identities use P/Q flow transport by LR and L1=1; they do NOT assert preservation of hidden state flows. Thus K_LR (the set of compressed four-vectors) is a compact convex polytope contained in the full-history four-vector set K_full. If any full-history four-vector were outside K_LR, strict convex separation would yield a real linear cost J with V_full<V_LR, contrary to the proved equality of ALL real support minima. Therefore K_full=K_LR. QED.

## Explicit genuinely depth-three witness

Full: sample at root; at t=1 sample from a, stop/declare P from b; at t=2 continue iff h=a and R=3/2, else declare P; at t=3 declare Q on S=1/2 and P on S=3/2.

Compressed: sample at root; at t=1 (L=1) stop/declare P with probability 1/2, sample with probability 1/2; at t=2 (R=3/2) continue with probability 6/7 and otherwise declare P, and declare P for the other R; at t=3 declare Q for final LR 3/4, P for final LR 9/4.

Both have EXACT

O=(3/64,15/16,27/16,13/8).

In particular the shared time-2 Q mass reaching the informative third experiment is (1/2)*(7/24)*(6/7)=1/8, and its P mass is 3/16, exactly matching the full-history a/R=3/2 branch. The two expected sampling times differ, so matching all four coordinates is a nontrivial check.

## Validation, method scope and next problem

The accompanying standard-library Fraction checker was locally executed. It verifies all row normalizations, positivity, the failed strong lumpability, both exact witness observer vectors, the Bellman support identity at 2401 signed integer coefficient tuples in {-3,-2,-1,0,1,2,3}^4, and the concavity/root-mask inequalities on those tuples. This finite grid is NOT the real-coefficient theorem proof, which is the algebra above. No float approximation or Monte Carlo supports the claim.

BRC: REUSE_APPLIED (ordered positive rational P/Q branch carriers, exact likelihood-ratio mass transport, typed observer compression and explicit hidden-branch preservation until proof). No source-native BRC executable was run. Signed differences of nonnegative flows are not signed BRC amplitudes. Four-scalar equivalence does NOT entail native X6/time dynamics, port/future-intervention equivalence, full fine-flow equivalence, or arbitrary horizon equivalence.

**Scientific status:** AUTHOR_PROVED_N3_EXAMPLE / EXACT_FRACTION_WITNESS_PASS / 2401_SUPPORT_CROSSCHECK_PASS / DRIVER_UNREVIEWED / NATIVE_OWNER_AND_CLAIM_UNVERIFIED.

**Next:** Test LR-dependent terminal signal kernels and the exact conditions preserving phi concavity and occupancy convexity. Investigate the nonunit-L1, later-time hidden-fiber necessity problem separately. Maintain raw branch identity, future-operation scope, precise signed cost quantifiers and original N=2 predecessor strength.
