# R1/N14 — Likelihood-ratio necessity with a coarse terminal observer

Status: **AUTHOR HAND PROOF + EXACT FINITE RATIONAL CHECK**. Not an independent Research Driver review, Lean formalization, native Task/CLAIM/Result, P000 native theorem or claim of external historical novelty.

## Frozen source and actual authority
- GLOBAL_KNOWLEDGE_V1 at immutable main@4893bfa3f6633d309b6f2beb3757e648044f9154: 00_BOOTSTRAP, OPERATING_MANUAL, project TASK router, P000 V4, ACTIVE worldview, applicable mathematics/code/BRC rules.
- Enterprise Math research source at immutable main@00cd15ac5b52d1e43357d92f9c7cb2855aba6d10: docs/PORTABLE_RESEARCH_PROTOCOL.md; current P000 X6/time and joint-observer constraints; predecessor research_notes/r1_n14_brc_coarse_observer_strict_separation_20261027_r1t11/{PROOF.md,NEXT_TASK.md}.
- Authenticated GitHub actor awdawmip has write permission. Native task read failed CONTROL_QUOTA; native researcher session request failed STATIC_READONLY_SCOPE_DENIED with operation_sent=false. Active native Owner/CLAIM unverified. This artifact is a nonclaiming author continuation. Source research activity RA-R1T11-20261027-LRNEC0157 is local-only identity bookkeeping, not a native session.
- The predecessor proved that refined-state strong lumpability is not necessary for a coarse terminal observer; its next question was whether likelihood-ratio constancy within x-fibers remains necessary. The result below answers **yes**, in the declared generality.

## Exact finite-path model

Let H_t be the complete finite set of ordered histories at time t of a finite horizon N, under strictly positive probability laws P and Q. Write p_h=P(H_t=h)>0 and q_h=Q(H_t=h)>0. A single law-independent full-history policy chooses stop/decide 0, stop/decide 1, or continue at each ordered prefix (forced stop at N). A proposed compressed policy may condition its fresh action randomization only on a deterministic time-respecting, symbol-updatable state x(h); it has no additional hidden register encoding past symbols. The desired terminal distribution, to be preserved simultaneously under P,Q, is (T,o(x(H_T)),D), where o is an arbitrary, possibly constant, readout.

"Universal preservation" quantifies: FOR EVERY common full-history policy there EXISTS ONE common x-policy giving exactly the same joint terminal distribution under both laws.

## Theorem (LR necessity independent of observer coarseness)

For any 0<=t<=N and any two histories h,h' in H_t with x(h)=x(h'), universal preservation implies:

    q_h / p_h = q_h' / p_h'.

This remains necessary if o(x) is identically constant, so the observer sees only (T,D).

### Proof: exact separating support function

Fix time t and positive rational threshold r. Let d_h=q_h-r p_h, and [v]_+=max(v,0). Define

    S_full(r) = sum_{h in H_t} [d_h]_+,
    S_x(r) = sum_{s in x(H_t)} [sum_{h:x(h)=s} d_h]_+.

Positive-part subadditivity shows S_full>=S_x. If one x-fiber contains two unequal LR values, choose a rational r strictly between them. That fiber contains both d_h>0 and d_h'<0, so positive and negative parts inside it give STRICT inequality

    Delta(r) := S_full(r)-S_x(r) > 0.

Construct the full-history policy which continues everyone before t, stops everyone at t, and chooses D=1 exactly on histories d_h>0. It has T=t almost surely and observed contrast

    J_r = Q(T=t,D=1)-r P(T=t,D=1) = S_full(r).

Any x-policy preserving (T,o,D) must preserve the observable marginal T=t almost surely. Strict positivity of P and Q on all ordered prefixes forces zero earlier stopping on every reachable compressed state (otherwise P(T<t)>0). Therefore everyone reaches t under that x-policy. If a_s in [0,1] is the compressed probability of choosing D=1 at s=x(h), then

    J_r = sum_s a_s sum_{h:x(h)=s}(q_h-r p_h)
        <= sum_s [sum_{h:x(h)=s}(q_h-r p_h)]_+
        = S_x(r) < S_full(r).

Contradiction. The optimization includes ALL x-states, even multiple states with identical o(x), so compensation between such states has not been silently excluded. QED.

The signed d_h is a **linear separating functional of two positive measures**, not signed/complex BRC branch amplitude or a claim of physical phase cancellation.

### Quantitative certification

A mixed-LR fiber yields a rational r and a positive exact gap Delta(r), measured on the terminal (T,D) observable alone. The gap is a closed-form obstruction to universal two-law preservation. This uses no enumeration of all randomized policies.

## Exact four-symbol example, with compensation candidates present

Use horizon N=1, alphabet {a,b,c,d}, positive laws

    P = (1/4,1/4,1/4,1/4)
    Q = (1/8,3/8,1/4,1/4).

Compress a,b to x=A and c,d to x=B; the readout is constant, o(A)=o(B)=*. Under both laws each compressed x-state has total mass 1/2. With r=1, the ordered-branch differences are

    (d_a,d_b,d_c,d_d)=(-1/8,+1/8,0,0).

Thus S_full(1)=1/8, S_x(1)=0 and Delta(1)=1/8.

The history policy D=1 iff h=b gives P(D=1)=1/4 and Q(D=1)=3/8. Any x-policy with decision probabilities u_A,u_B has P(D=1)=Q(D=1)=(u_A+u_B)/2, so matching is impossible. In particular, the other x-state B, which shares the same observer readout, cannot compensate. This is exact and strictly positive with P unequal to Q.

Local VERIFY.py checks normalization/positivity using fractions.Fraction, all 16 deterministic history-classifiers, all 4 deterministic x-classifiers, the separating support values, and the particular pair of decision masses. Randomized classifiers are handled by the analytical linear support maximum; finite enumeration itself is not claimed to establish the universal theorem.

## Sharp N=1 corollary

At horizon N=1 (with a single root x-state), LR constancy within each depth-one x-fiber is also SUFFICIENT for universal two-law preservation for any terminal observer o. Copy the original law-independent root stop hazards. For any depth-one x-state s, set its terminal D=d probability to the P-weighted average of the original D=d probabilities over histories in that fiber conditional on survival from the root. Constant q_h/p_h within s makes this same weighted average correct under Q. Hence the entire (T,x,D) distribution, and therefore (T,o,D), is preserved. Empty-survivor fibers are arbitrary. This proves the one-step equivalence; no assertion is made that the same condition is sufficient for arbitrary N>1 without additional transition/occupancy hypotheses.

## BRC reuse, admissibility and next question

BRC population: every ordered positive-rational P/Q prefix; preserve branch identity, stopping flow, decision, declared horizon and future observable before taking a quotient. REUSE_APPLIED: the existing ordered-path occupancy method and observer-safe Markovization principle; no new general tool family. Dropping x-fiber LR residual is unsafe exactly when Delta(r)>0. This is an EXTERNAL FINITE PROBABILITY AUXILIARY MODEL. It neither changes P000 (six native spatial dimensions, one separate time, triadic balance and native three-dimensional slice) nor supplies a native X6 Cell mapping.

Next unit: for N>=2 find a necessary-and-sufficient finite certificate for the inclusion of full-history two-law terminal law sets in the x-policy terminal law sets under (T,o(x_T),D). Preserve the SAME-policy quantifier across P/Q, distinguish convex occupancy relaxations from implementable Markov randomized policies, and reuse the earlier counterexample showing refined SL need not be necessary under coarse observation.
