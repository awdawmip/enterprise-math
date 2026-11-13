# Stage393-B — Native signed-X6 BRC: exact future-memory theorem and reversibility counterexample

Date: 2026-11-03 (Asia/Shanghai). Research line: Research2, after Stage392-B. Scope: mathematical author-side result, exact typed BRC / Path-formal combinatorics. Status: PROVED within the declared model, FINITE_EXACTLY_CHECKED within recorded ranges, UNREVIEWED, NOT_ADMITTED. This note does not update P000 or claim any native Result, Driver acceptance or physical heartbeat propagation.

## Scientific inputs and source

Frozen scientific inputs remain Enterprise Math commit 2af3fc484eb11060b69e0afc1b562bcaf5ad1419, global science commit bf84bd7c61a2444b59b1da96be57df0e9ae47e53, and P000 V5 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Current normative rules were separately read from canonical main. The native algebra comes from definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md §§2–6,10–12 and research_notes/X6_SIGNED_PATH_BRC_AND_PRIMITIVE_LINE_V17_20260905.md §§3–6,9, both at the frozen scientific input commit. The latter supplies the exact all-length N-BRC kernel.

Choose one Cell anchor in the native affine torsor over Z^6. The native alphabet is the twelve signed primitive labels A={+E_i,-E_i | 1<=i<=6}; each letter d has displacement delta(d)=+e_i or -e_i. A path-formal branch witness is an ordered finite word w=d_1...d_m in A*, with endpoint z(w)=sum delta(d_j). Its source label sigma in {P,Q} and operation-order index m are retained separately; m is not a physical heartbeat time.

For each three-element subset S={i,j,k} of {1,...,6}, define R_S(z)=(z_i-b,z_j-b,z_k-b), b=min(z_i,z_j,z_k). Keep all 20 complete three-component readouts, third component included. Together with the common depth h(z)=min_i z_i these exactly reconstruct all six signed coordinates. These are observer readings inside full native X6, not an independent native plane, automatically-realized FCC slice, or a final public Cell address.

For endpoint z and length m the frozen all-length signed endpoint BRC kernel is

  N_m(z) = m! * SUM_{k_1+...+k_6=K} PRODUCT_{i=1}^6 1/[(a_i+k_i)!(b_i+k_i)!],

where a_i=max(z_i,0), b_i=max(-z_i,0), K=(m-sum |z_i|)/2. The result is zero unless K is a nonnegative integer. It counts ordered signed-X6 paths, including backtracking. Its rational positive-weight version multiplies each summand by PRODUCT_i [omega(+E_i)^(a_i+k_i) omega(-E_i)^(b_i+k_i)]. These are nonnegative counts and weights, not signed-amplitude interference.

**Declared derived path observer:** tau(w)=sum_{j=2}^m 1[d_j != d_(j-1)]; tau(empty)=0. Signed reversal on the same axis counts as a label change. This is a selected Path-formal statistic for a mathematical observer, not a P000 force, physical jitter or source-defined field observable. Define O(w,sigma)=(sigma,R(z(w)),h(z(w)),m,N_m(z(w)),tau(w)). Allowed futures initially are right-appends A_d:w->wd, for d in a declared subset L of A. A future readout is the same O after any finite allowed sequence.

## Theorem A — Exact last-label repair for every appended word

For the full alphabet L=A, augment O by last(w), with an empty sentinel inferred from m=0. This is deterministic future-sufficient for all finite append sequences.

**Proof.** Given R,h, reconstruct z exactly by the existing native descent theorem. A permitted append d determines z'=z+delta(d), m'=m+1, source unchanged, and N_(m+1)(z') from the frozen endpoint formula. The turn statistic and terminal label obey

  tau(wd)=tau(w)+1[m>0]*1[last(w)!=d]; last(wd)=d.

Thus every next augmented state is a function of the current augmented state and d. Induction over arbitrary finite appended words proves the claim. The same argument applies to any restricted future alphabet L. QED.

## Theorem B — Sharp twelve-state lower bound at one observation fiber

There exists one current O-fiber whose histories require at least 12 additional equivalence classes under the full append language. Theorem A supplies a matching 12-state code, or ceil(log2(12))=4 extra fixed-width binary bits, for the worst fiber.

**Proof.** For each d in A choose a positive letter alpha=+E_j with j distinct from the axis of d. Construct the actual signed-X6 word w_d=(alpha,-alpha,-d,d). Every w_d has z=0, m=4, tau=3, common depth h=0, all 20 triples R_S=(0,0,0), and N_4(0)=396. Give them the same source label. Their last labels are exactly the 12 distinct values d.

For d!=e, the future append d produces endpoints delta(d), lengths 5, and the same endpoint kernel N_5(delta(d))=1660, but tau(w_d d)=3 whereas tau(w_e d)=4. Every pair is distinguished. Hence a deterministic exact future-safe compression on that same fiber needs at least 12 codes. The terminal label attains 12 codes, proving sharpness at that fiber. This lower bound is intentionally observer-specific and not a universal per-fiber claim. QED.

## Theorem C — Sharp restriction to a future alphabet

For any subset L of A, the histories {w_d:d in A} in the same O-fiber have exactly

  q(L)=|L|+1[L != A]

future-observation equivalence classes. For nonempty words a sufficient code is s_L(w)=last(w) when last(w) belongs to L, and OUTSIDE otherwise. The m=0 case is already distinguished by length.

**Proof.** Two last labels outside L both contribute one additional turn on the first allowed append, after which their next last label is the common appended symbol. Their future readouts agree by Theorem A. In contrast, if one label d belongs to L and the other differs, append d: one new tau is unchanged, the other rises by one, distinguishing the pair. Every pair of distinct labels in L separates in the same way. All required representatives occur among w_d. If L=A no outside class exists; if L is empty there is one class. The same update recurrence proves that s_L is future-sufficient for all words, and the witness fiber proves the class count is sharp there. QED.

Examples: all twelve possible future steps require twelve states/four binary bits; a single allowed step requires two states/one bit; an empty operation alphabet requires one state/no extra bit. This exact law quantifies how a proven compression depends on its declared future language.

## Theorem D — Faithful turn-refined exact BRC recurrence

Define F_m(z,c,d) as the number of ordered length-m signed-X6 paths with endpoint z, turn count tau=c, and terminal signed label d. Set F_1(delta(d),0,d)=1 and all other length-one states zero. For m>=1,

  F_(m+1)(z,c,d) = SUM_{b in A} F_m(z-delta(d),c-1[b!=d],b),

with absent/negative states interpreted as zero. The empty base is F_0(0,0,EMPTY)=1.

**Proof.** Any word ending with d admits a unique decomposition into a prior word ending in b and final letter d. Deleting d decreases the endpoint by delta(d), length by one, and turn count by 1[b!=d]. The recurrence is exact and disjoint. Summing over c,d counts all ordered native signed words of endpoint z and length m. By the frozen source combinatorial law, SUM_(c,d) F_m(z,c,d)=N_m(z). If positive rational label weights omega are declared, multiply each term by omega_d; its marginal is exactly the frozen W_m(z). This is a faithful typed refinement of source BRC, not a replacement physical propagator and not destructive signed-amplitude cancellation. QED.

## Theorem E — Full Path-formal provenance can require unbounded extra information

If an allowed future operation reads the entire ordered historical branch, no uniform finite number of extra history states suffices for all word lengths, even after Theorem A's last-label repair.

**Proof.** Let B0=(+E1,+E2,-E2,-E1) and B1=(+E1,+E3,-E3,-E1). For each n>=1 concatenate an arbitrary n-letter sequence of blocks B0 or B1. There are 2^n distinct path words. All have endpoint zero, m=4n, tau=4n-1, last=-E1, identical twenty R_S, h and frozen N_(4n)(0). Hence all have identical augmented current O. Right-appending a common letter preserves distinct ordered words. A later full-history readout distinguishes each; at least 2^n states or n bits are needed on that fiber. QED.

This theorem concerns full history readout. It does not conflict with the finite turn-statistic code proved under Theorems A–C.

## Proposition F — One typed POP defeats the last-label repair

Extend the future operation set to include POP(wd)=w for nonempty ordered path words. Then the augmented observer (O,last) of Theorem A is not future-sufficient under one POP.

**Proof by exact witness.** Take
  w=(+E1,+E1,-E1,+E1),
  v=(+E1,-E1,+E1,+E1).
Both have z=2E1, m=4, tau=2, last=+E1, the same source tag, R_S and h, and frozen N_4(2E1)=64. POP(w) and POP(v) both have z=E1, m=3, last either -E1 or +E1, N_3(E1)=33, but their turn counts are 1 and 2 respectively. Hence equal repaired states have different future observations. POP here is a *typed ordered-history* operation, not a physical reversal law or heartbeat update. QED.

Finite exact enumeration of every signed path of lengths 1,2,3 (12+12^2+12^3=1884 histories) found no shorter POP contrast with equal (z,m,tau,last); this is auxiliary bounded evidence, and the length-four witness alone supplies the universal failure.

## Executed arithmetic evidence and limits

The locally executed full Python integer/Fraction checker (REPRO_STAGE393B_TURN_BRC.py) used two independent formulations of signed BRC: the frozen factorial/coefficient endpoint formula and direct signed primitive-step DP. Twice executing the same full checker yielded byte-identical stdout and the tag STAGE393B_X6_TURN_BRC_PASS. Exact test coverage: 4,043 endpoint pairs, 31,429 turn-decorated states, 1,375 positive-rational weighted endpoint comparisons, 7,021 weighted decorated states, 295,945 finite append tests, 132 pair separations, all 4,096 possible future alphabets, 126 exponential-family samples, and the finite 1,884 shorter POP paths. N_4(0)=396; N_5(E1)=1660; N_4(2E1)=64; N_3(E1)=33. The exact JSON certificate is 1,622 bytes, SHA256 5374feb44a071f47b1bc4a938b53856278458aab43fdc483a0272b4a7b3c1624. Finite tests corroborate the separately written universal combinatorial proofs; no physical heartbeat model was executed.

The declared object population is signed native-X6 ordered path words. Future APPEND, POP and full-history readout are separate operation/observer claims. Additional source provenance, joint relations and fields stay in their own types. Researcher identity and canonical Result/Review authority are not established by GitHub author-side publication.

## Next Stage394-B

Classify the exact minimum sufficient suffix/stack memory under append plus POP for an explicitly bounded POP horizon H; distinguish one-pop, repeated pops, append/pop alternation and an unbounded future horizon. Determine minimal state class counts and prove exact descent or produce separating words, with full six-axis and all-three-component observer semantics preserved. Keep frozen scientific pins unchanged and account for real bit cost versus horizon.
