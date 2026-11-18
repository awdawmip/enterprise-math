# X6 R12 — three mobile triads expose an exact blocker-source alias; pairwise future memory is sufficient but not minimal

Date: 2026-11-19, Asia/Shanghai. Researcher line EM-X6-214D9C / MCP-d467c19ce42d4d7fa65a3901db1cf6b2 / Activity RA-545183ADD4EF71C3E4698AEE. Task RS-X6-NATIVE-TIME-DYNAMICS, publication TP2-91D4A7C2F63805BE21A3, original scientific pin awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Exact **conditional** mathematics; independent review NOT_REVIEWED.

## R11 predecessor and new question

R11 proved that with **two mobile source-labelled triads** and fixed positive native-axis Port masks, the exact horizon-h language class of their relative displacement d is the singleton d if a collision is reachable within h moves, and otherwise a pooled FAR state. See [R11](2026-11-19_x6_two_mobile_port_relative_future_cone_r11.md). This R12 treats n>=3 simultaneously moving source-labelled triads with the same vacancy-only guarded moves, and asks whether a product of pairwise R11 signatures remains exact and minimal for the *joint* labelled future language.

Let X6 be the signed relative Z^6 affine Cell torsor about a chosen Cell anchor. Every source s has an occupied Cell a_s, an individual fixed positive native-axis Port mask I_s (nonempty), source/triad identity and its own ordered event labels (s,i). All source Cells are distinct. A permitted (s,i) step translates source s by the single native axis e_i precisely if no other source occupies the target. The step vacates its old Cell. The full typed Boolean-BRC carrier remembers the joint occupied-cell relation and all labelled ordered branches. L_h(S) is the entire prefix-closed language of successful source/Port words up to event depth h. A blocked event is observed only by **absence of that labelled successor**, not by revealing which source occupied the target. There are no additional guards or time calibration. Force closure TRIADIC_CLOSURE_E remains a separately open native admission condition.

## Theorem A: pairwise finite-future quotient is always sufficient

For every ordered pair of distinct sources, take the R11 horizon signature sigma_h(a_j-a_i;I_i,I_j). The tuple of all pair signatures (together with the fixed identities, masks, and remaining horizon h) determines the exact joint legal future language L_h(S). Its update after a legal event is Markov with horizon decremented to h-1.

Proof. A proposed source event (s,i) is legal exactly when *none* of the n-1 pairwise relative states (s,t) makes the target equal the occupied Cell of t. By the R11 two-source theorem, the pairwise sigma_h records whether the very next labelled event would collide with that other source; a FAR pair never collides at any step within the current horizon. Thus all immediate legal source events can be determined from the tuple. After an event, every pair changes by either +e_i, -e_i, or no change. R11's horizon-countdown theorem gives its updated sigma_(h-1) from its prior signature and the known event, including the FAR case; source labels preserve which pair was changed. All these updates have the same actual joint target and legal vacancy condition. Induction on h proves the product signature preserves every full legal source-labelled word. QED.

This is a sufficient joint observer descent certificate over exactly the declared guards; it is not assumed minimal.

## Theorem B: exact three-source counterexample to pairwise minimality

Give all three sources the same only available Port +e_0. Choose two distinct native axes e_0,e_1 within the full X6 chart, with all remaining components **explicitly zero for this constructed configuration**; this is a local selected-axis embedding, not a native two-dimensional plane.

Consider two legal simultaneous configurations, with A and B fixed:

    A = (0,0,0,0,0,0), B=(0,1,0,0,0,0).

    Case U: C=(-1,0,0,0,0,0)  (one step behind A).
    Case V: C=(-1,1,0,0,0,0)  (one step behind B).

In BOTH cases the A0 and B0 steps are legal, and C0 is blocked: in U it would hit A; in V it would hit B. Consequently

    L_1(U) = L_1(V) = {epsilon, A0, B0}.

Yet the pairwise horizon-1 signatures differ. In U the A-C pair is visible with displacement -e_0 while B-C is FAR (its e_1 offset cannot change); in V the A-C pair is FAR and B-C has displacement -e_0. Thus an independent product of the R11 pair signatures distinguishes two configurations whose **whole joint one-step successful-event languages are identical**.

At horizon 2 the cases separate: the labelled word (A0,C0) is legal in U (A vacates C's target) but forbidden in V (B is still there). Equivalently (B0,C0) is legal in V but forbidden in U. Their current counts, count-derived local phase and event label alphabet may be fixed equal: the missing datum is the **identity of the blocker** of C0, which is invisible at one step but becomes future-relevant after moving one blocking source.

Therefore any claim that independent pairwise minimal signatures necessarily form a minimal *joint* source-labelled future state is refuted. The same pair-product remains sound as a sufficient state by Theorem A.

## Theorem C: an unbounded m-bit finite-horizon over-retention family

For every integer m>=1 build 3m distinct source-labelled moving triads, with labels A_j,B_j,C_j for j=0,...,m-1 and every source Port restricted to +e_0. Choose a third independent native axis e_2 and set q_j=4j e_2. For each bit beta_j in {0,1} place

    A_j=q_j,
    B_j=q_j+e_1,
    C_j=q_j-e_0+beta_j e_1.

All coordinates are signed relative six-component X6 vectors. The e_2 offsets make different triples independent in the declared vacancy model. For each of the 2^m possible beta-vectors, every A_j0 and B_j0 is legal and every C_j0 blocked. Accordingly, the entire horizon-1 language is **identical across 2^m states**. By the blocker-source mechanism of Theorem B, however, each choice of beta_j changes which pairwise sigma_1 records the blocked C_j event. The 2^m pair-product signatures are all distinct.

At horizon 2, the labelled witness (A_j0,C_j0) is legal iff beta_j=0. Thus the family yields **2^m different horizon-2 future languages**. In this fixed observer fiber, the exact minimum additional coding demand jumps from

    b_1=ceil(log2 1)=0  to  b_2=ceil(log2 2^m)=m bits,

while retaining independent pairwise horizon-1 signatures would already consume m bits with no one-step-language benefit. This proves a sharp, arbitrarily large gap in the number of independent source-history bits needed by two declared observation horizons, in a fixed six-dimensional native spatial carrier with growing source count.

The observer is precisely defined: it sees the *successful* next event alphabet and its future iterations, not the blocker ID in a rejected event. If an augmented observer reports the blocking source, the displayed one-step alias disappears; that is a different observable and requires a separate compression claim.

## Exact Boolean-BRC verification

The checker [x6_three_mobile_blocker_alias_brc_verify.py](https://github.com/awdawmip/enterprise-math/blob/66b2f8fbd1f309f77cc334723970ab35747f0d75/research_notes/portable_direct/x6_three_mobile_blocker_alias_brc_verify.py) enumerates full source/Port labelled legal word branches and occupied joint Cell states. Its [result JSON](https://github.com/awdawmip/enterprise-math/blob/c5c93cde0e55318af981e28e4446cfb377f71310/research_notes/portable_direct/x6_three_mobile_blocker_alias_brc_results.json) records PASS.

- Exhausted **182** distinct three-source states with A at the chosen origin, B and C in the selected signed coordinate grid. Their 1-step futures produce **7** different joint languages but **13** distinct pair-product signatures; **6** language classes contain more than one pair-product signature.
- Constructed every history bit word for m=1..5 (2,4,8,16,32 configurations); verified one identical L_1 per family and 2^m distinct L_2 languages and pairwise sigma_1 signatures. Each case verifies the actual source-labelled two-event witness for every j.
- All arithmetic and comparisons are exact six-component integer Cell tuples, labelled Boolean support and finite sets. The unbounded m conclusion follows from the explicit independent-axis-source construction and proof, with small finite cases as independent execution checks.

## Interpretation, boundary and next discriminating question

R11 shows that two-source relative displacement is the exact future-local collision signature. R12 proves that for 3+ mobile sources, the pairwise product remains a correct future-safe upper representation but may retain arbitrarily many horizon-invisible **blocker-source assignment** bits. The smallest sufficient joint state is observer-dependent: the precise canonical (if computationally expensive) finite-horizon solution is the guarded labelled transition-tree equivalence, recursively recording the full set of legal labelled successors and their horizon-(h-1) equivalence classes. The concrete family quantifies when pairwise factorization fails to be minimal.

Next: derive a *compact joint* frontier for moving triads that merges same-label blocked successors without losing the later distinguishing source move; compare its encoding size to the pairwise product, and then validate against genuinely legal TRIADIC_CLOSURE_E/Port force updates. The event trace remains time as order of relational change, not a seventh spatial axis. No independent mathematical acceptance is asserted.
