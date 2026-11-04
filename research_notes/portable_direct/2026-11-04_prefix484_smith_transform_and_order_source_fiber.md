# PREFIX-484 — Constructive Smith witnesses and three-class ordered-source defect

Date 2026-11-04 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED. Portable author-side result; no authenticated TASK Result.

## Sources / scientific scope

Continues PREFIX-483 at 4121af552f5617bde10c3aa142b825e6d7dc79c9 with frozen science pin f42f2906d77f24085c123f3ccfe9667d41caa96d. Current normative sources include P000/ACTIVE Heartbeat native X6, joint-observer preservation, docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context, research_priorities/research_method.json and docs/PORTABLE_RESEARCH_PROTOCOL.md. Letters a/A,b/B,c/C,d/D,e/E,x are a restricted, explicitly embedded *ordered-path observer* inside X6, not a reduction of X6's six native dimensions. Ordinary letters always legal. x is first or follows gate w=aab. Order, phase, source ID and time remain distinct types.

## Theorem A: explicit Smith certificate and complete integer reconstruction

For integer observation M in Z^(d×m) and additive target H in Z^(ell×m), obtain unimodular U,V so U M V=S=diag(s_1,...,s_a,0), s_i>0, s_i|s_(i+1), a=rank_Q(M). Split V=[V_A,B]; the last m-a columns B form an integral saturated kernel basis. Let L H B R=D=diag(d_1,...,d_r,0) with unimodular L,R and d_i>0, d_i|d_(i+1); r=rank_Q(HB)=rank_Q([M;H])-rank_Q(M). Define c=V^-1 p and t=(R^-1 c_K)_(1:r). Given o=Mp, reconstruct:

    c_(A,i) = (Uo)_i / s_i, i=1,...,a      (exact divisibility)
    Hp = H V_A c_A + L^-1 (d_1 t_1,...,d_r t_r,0,...,0)^T.

Proof: Uo=S c gives c_A, and H B c_K=L^-1 D R^-1 c_K gives the rest. The unimodular matrices preserve the integral lattice, so all transforms and inverse transforms are integral; Euclidean row/column moves with lower-block divisibility reduction construct the chain and their corresponding witnesses. For a signed native append, p either stays fixed or increments by a declared e_i according to the sign of the running native displacement, so the Smith t-coordinate is directly additively updateable. This realizes the PREFIX-483 rank-optimal additive integer repair with an explicit transform certificate. Its dimension minimality is limited to the declared fixed-coefficient additive class.

Nonprimitive example: M=[[2,0,0,0],[0,6,0,0]] has Smith factors (2,6). H=[[0,0,6,0],[0,0,0,10]] on ker_Z(M) has factors (2,30), rank 2, image index 60 in its saturation. A separate rank-one H=[[0,0,4,6],[0,0,8,12]] has sole factor 2. Index does not imply any universal fixed-bit saving. Reference Python code checks exact U M V=S, L H B R=D, Smith divisibility, integer inverses, rank identities and Hp recovery, including 360 deterministic randomly generated rectangular cases.

## Theorem B: three future-distinguishable source-order histories in a single BRC–KMP fiber

With ordinary positive direction weights (6,12,18,24,36), opposite letters weight 1, and BRC cancellation p_i=min(u_i,v_i), retain (n,s,y,Mp,q) with M rows:
    (1,1,1,1,1), (0,1,0,2,1), (0,0,1,0,1).
For gate aab, consider legal words
    s0=(aA)^3(dD)^2(eE)       = aAaAaAdDdDeE,
    s1=(bB)^2(aA)^2(dD)(eE)  = bBbBaAaAdDeE,
    s2=(cC)(bB)(aA)^2(dD)^2  = cCbBaAaAdDdD.
All have n=12, x-count 0, y=0, Mp=(6,5,1), q=0, and exact positive path weight 4,478,976. Their pair-count differences lie in ker_Z M.

Declare future readout F(word)=1 iff the *first occurrence* of a symbol from {b,B,c,C} is b or B. A sufficient deterministic order carrier consists of N (none), B (first is b/B), C (first is c/C); from N, b/B=>B and c/C=>C; B,C are absorbing. Output is 1 exactly in B. s0,s1,s2 yield N,B,C. Empty suffix separates B from N,C; legal suffix b separates N from C because F(s0 b)=1 and F(s2 b)=0. The original BRC–KMP observation remains identical for the three paths after the *same* suffix b. Therefore every future-correct deterministic carrier for F under arbitrary legal ordinary suffixes needs at least three labels on this single base fiber; the three-state automaton attains this, and the smallest fixed binary state width is 2 bits. This is a scoped Myhill–Nerode witness, NOT a sufficiency theorem for general ordered provenance/source ID/phase/rotation.

## Executed certificate, evidence and limits

The companion Python 3 standard-library script verifies arbitrary integer rectangular Smith transforms with exact integer arithmetic; 360 fixed-seed examples have dimensions <=5x6 and coefficients in [-9,9], with independent exact Fraction row-rank and three exact Hp reconstructions per case. It also exactly enumerates and checks the three displayed paths, their BRC, KMP, product weights, before/after source outputs and the common post-suffix observation. The saved stdout ends ALL_CHECKS_PASS. The unbounded algebraic propositions are proved above; the finite tests exercise the implementation in their stated domains. The Euclidean reference implementation is not an optimized worst-case bit-complexity algorithm.

Background sources: E. W. Weisstein, Smith Normal Form, https://mathworld.wolfram.com/SmithNormalForm.html ; M. Giesbrecht, Fast computation of the Smith normal form of an integer matrix, ISSAC 1995, DOI 10.1145/220346.220361; Cornell CS4120 DFA minimization, https://www.cs.cornell.edu/courses/cs4120/2021sp/notes/leximpl/ . These are background methods, not admission.

Next PREFIX-485: finite-horizon minimization of the product BRC–KMP–source observer, testing whether three classes persist across families of ordinary-path fibers; compare Smith transforms to selected-row additive coordinates on sparse/rank-deficient instances, recording integer coefficient growth and full encoder/decoder costs.

Authority status for this attempt: GitHub login awdawmip verified with push/admin. Native Sites gateway reports static_machine_readonly, research_authority_granted=false; em_control_tasks returned CONTROL_QUOTA and em_session_start returned STATIC_READONLY_SCOPE_DENIED (operation_sent=false). No authenticated CLAIM, independent review or admission.