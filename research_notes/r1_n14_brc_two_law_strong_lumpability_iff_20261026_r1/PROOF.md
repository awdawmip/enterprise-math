# R1/N14 — exact universal two-law quotient criterion: LR + strong lumpability iff preservation

Status 2026-10-26: author-level complete hand proof; locally executed exact Fraction checker PASS; independent Research Driver review pending. External finite positive-history model only. Not a native P000 six-axis Cell theorem, formal Task/CLAIM/Result, Lean formalization, or scholarly novelty claim.

## Source and scope

Account knowledge frozen at GLOBAL_KNOWLEDGE_V1 main a307e21a64150ced71df99120a1a14f0487946e9, including bootstrap, manual, enterprise-math project router, P000 startup projection and original Git blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc (identical to projection's source SHA), ACTIVE worldview, math/code/BRC policy. Enterprise Math initial source main 71f923a1b64ba20e9fdfaa9c45a23f2cf5aa3a73; read AGENTS.md, Heartbeat native X6/time, joint-relation observer contract, portable research protocol, current authority and the previous author frontier research_notes/r1_n14_brc_noniid_two_law_ratio_lumpability_20261026_t11/PROOF.md and NEXT_TASK.md. Previous frontier already proved LR necessary and LR+SL sufficient. This note proves the outstanding necessity of SL and provides a distinct-law exact witness.

Connected GitHub actor awdawmip has push rights. Native task enumeration returned CONTROL_QUOTA. Native researcher session creation returned STATIC_READONLY_SCOPE_DENIED with operation_sent=false. Consequently no active canonical Owner was verified, no claim or native research session was obtained; author-only nonclaiming source persistence is intended. The locally assigned activity/session identifier is not a server-issued authority token.

## Theorem (full necessary-and-sufficient criterion)

Fix a finite alphabet A, finite horizon N, and two strictly positive laws P and Q on A^N, with induced prefix masses L(h)>0 and next-letter probabilities K_L(a|h)=L(ha)/L(h) for L in {P,Q}. Fix a time-respecting deterministic quotient x_t(h) of words h in A^t, equipped with deterministic updates rho_t(x_t(h),a)=x_{t+1}(ha).

A history policy chooses at each ordered prefix, possibly using independent private randomization, either terminal decision d_P, terminal decision d_Q, or continuation, and necessarily stops by depth N. A quotient policy uses only its current state x, clock and private randomness; the action rule is independent of whether P or Q is true.

Let UP mean: for EVERY full-history policy there exists ONE quotient policy preserving under BOTH P and Q the joint terminal distribution of (T,x_T(H_T),D).

Condition LR: for any fixed depth-state x, Q(h)/P(h)=r_x is constant over all h with x_t(h)=x.

Condition SL: for any L in {P,Q}, every nonterminal depth-state x, every child quotient state y, and any h with x_t(h)=x, the quantity

    M_L(h,y) = sum over a with rho_t(x,a)=y of K_L(a|h)

is independent of the representative h in the x-fiber. At depth N SL is vacuous.

**Theorem. UP is equivalent to (LR and SL).**

### Sufficiency

For the original randomized policy write u_h for its pre-action survival fraction, and a_h,b_h,c_h for the three actions stop-d_P, stop-d_Q, continue (a_h+b_h+c_h=1; c_h=0 at depth N). Define aggregate flows at x for L=P,Q:

    F_L(x) = sum_{h in x} L(h) u_h
    A_L(x) = sum_{h in x} L(h) u_h a_h
    B_L(x) = sum_{h in x} L(h) u_h b_h
    C_L(x) = sum_{h in x} L(h) u_h c_h.

By LR, the vector (F_Q,A_Q,B_Q,C_Q)(x) is r_x times its P-counterpart. At F_P(x)>0 choose the single quotient action (A_P/F_P,B_P/F_P,C_P/F_P); at zero flow choose any legal action. These fractions are therefore correct for BOTH laws. By SL, each original aggregate next-survival flow satisfies

    F_L(y at t+1) = sum_{x at t} C_L(x) M_L(x,y).

The quotient policy satisfies exactly this recurrence. Induction in t, starting at the root, proves equality of all four flows for both laws. In particular the complete joint terminal distributions (T,x,D) coincide. QED.

### Necessity of LR (recalled with complete argument)

Fix any depth-state x and any ordered prefix h* in that fiber. Construct a history policy that continues surely before depth t and at t stops everywhere, selecting d_P only on h*, d_Q elsewhere. Under each strictly positive law a matching quotient policy must also have no earlier stop. Thus at t its prefix distribution is unconditioned L(h), and its common d_P decision probability p_x must satisfy

    p_x = P(h*)/sum_{h in x}P(h) = Q(h*)/sum_{h in x}Q(h).

UP holds for every choice of h* in x, so the normalized P- and Q-fiber mass vectors are identical. Consequently Q(h)/P(h) is constant over that fiber. QED.

### NEW: necessity of SL (isolating-continuation probe)

Fix any nonterminal depth-state x and any prefix h* in x. Construct a second policy: continue surely at depths below t; at depth t stop and decide d_Q on ALL prefixes except h*, but continue exactly on h*; at depth t+1 stop and decide d_P on every descendant of h*. No other terminal time has positive probability.

Take a quotient policy whose (T,x,D) terminal distribution matches this probe. Strict positivity and no earlier terminals force it to continue surely before t, hence the depth-t pre-action law remains unconditional L(h). At every state x' different from x the observed depth-t terminal d_Q mass is all of L(x'), so continuation mass at x' is zero. At x the observable depth-t d_Q mass is L(x)-L(h*); hence under law L its continuation fraction MUST equal

    c_L(x)=L(h*)/L(x), where L(x)=sum_{h in x} L(h).

UP ensures this can be implemented by one law-independent state action. In particular its total continuing mass from x equals L(h*). Because this fraction applies equally to ALL prefixes sharing x, their unconditional L-weighted average transition into child state y is

    bar M_L(x,y) = [sum_{h in x} L(h) M_L(h,y)]/L(x).

Thus the quotient's entire mass arriving at y at t+1 is L(h*) bar M_L(x,y). The original policy's mass at y at t+1 is L(h*) M_L(h*,y). Every continuing path stops at t+1 in the original. To match its terminal-time support the quotient must likewise stop at t+1 wherever positive mass arrives; it cannot conceal any discrepancy by a later continuation. Since the joint terminal distribution includes y and the d_P decision,

    L(h*) bar M_L(x,y) = L(h*) M_L(h*,y).

Strict positivity cancels L(h*). Since h* and y were arbitrary, M_L(h,y) is the same bar M_L(x,y) for EVERY representative h in x. Apply to each L=P,Q independently; that is exactly SL. No other depth-t state can compensate because its continuation mass was forced to zero. QED.

### Limitations of the theorem

The quantifier EVERY history policy and observation of the ENTIRE terminal quotient state are load-bearing. This theorem does not claim SL necessity for one fixed policy, for retaining only (e_P,e_Q,t_P,t_Q), for a strictly coarser terminal observer, for zero-mass prefixes, for policies supplied with the hidden true law, or for non-deterministic quotient updates. It is not a BRC signed/phase cancellation theorem.

## Exact witness that LR alone is not sufficient, with P != Q

Let A={0,1}, N=3, x(h)=(|h|,#0(h),#1(h)). Under P the first two letters are independent fair, while the third obeys P(0|01)=3/4, P(0|10)=1/4, P(0|00)=P(0|11)=1/2. Its terminal probabilities in lexicographic 000,001,010,011,100,101,110,111 order are

    P3 = (1/8,1/8,3/16,1/16,1/16,3/16,1/8,1/8).

Define distinct Q by tilting P's terminal counts with weights w(3 zeros)=2, w(2 zeros)=w(1 zero)=1, w(0 zeros)=1/2 and normalizing Z=17/16. The induced Q terminal probabilities are

    Q3 = (4/17,2/17,3/17,1/17,1/17,3/17,2/17,1/17).

Prefixes are computed by summing descendants. Every prefix is positive. All Q/P ratios are constant within x-fibers: at depth zero 1; at depth one 20/17 (prefix 0) and 14/17 (prefix 1), each a singleton; at depth two 24/17 (00), 16/17 (both 01 and 10), 12/17 (11); at depth three ratios depend only on count, namely 32/17 for 000, 16/17 when one or two zeros occur, 8/17 for 111. Hence LR holds globally.

But at the merged state x=(2,1,1), next-state count (2,1) has conditional mass P(0|01)=3/4 versus P(0|10)=1/4; under Q the same two transitions are 3/4 and 1/4 because both mixed-prefix children have tilt weight 1. Therefore SL fails.

Choose the isolating policy at depth 2: all words except 01 terminate in d_Q, exactly 01 continues, and its length-3 children terminate in d_P. Any matching quotient must continue with fraction 1/2 at count (1,1) under both laws; all other count states must stop at depth 2. Its fractionally thinned mixture after 01 and 10 has next-zero probability 1/2, whereas the selected ordered branch 01 has probability 3/4. At terminal (t=3,count=(2,1),d_P):

    P original = 3/16;  P forced quotient = 1/8; difference 1/16.
    Q original = 3/17;  Q forced quotient = 2/17; difference 1/17.

Both discrepancies are positive exact rationals. No other state can continue to compensate. This supplies a nondegenerate distinct-two-law LR-but-not-SL counterexample.

## Exact evidence

The Python standard-library Fraction checker enumerates all 2^0+2^1+2^2+2^3 = 15 ordered prefixes; independently constructs P and Q from their terminal masses; tests positivity, normalization, LR in every quotient fiber, P/Q transition kernels at 01 and 10, full terminal distributions for both original and forced count-policy, exact mass conservation, and the displayed deviations. Local execution returned all_assertions=PASS. This is an exact finite witness check; universal theorem proof is the preceding argument, NOT enumeration of all policies. Exact computed fractions in CERTIFICATE.json; checker in VERIFY.py. Local extended research bundle has separately executed source and raw log.

## Native boundary and next

BRC path identity, multiplicity, conditional weights and future-update operations were retained until the (LR,SL) criterion was proved; premature count compression fails in the witness. The result concerns an external binary model only. No native X6 mapping, heartbeat-time correspondence, signed/phase BRC operator semantics or observer-operation bridge was supplied. Native owner query remains blocked, so Source publication is author scoped, pending independent driver review and proper task admission.

Next: replace full terminal x by a coarser readout o(x) and determine which conditions survive; then study signed or complex BRC, where ratio constancy in positive measures is not an amplitude-cancellation certificate. See NEXT_TASK.md.
