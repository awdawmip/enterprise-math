# EC49FBK — Native signed-X6 terminal-prefix lift and BRC key dominance

Date: 2026-11-05. Directed TASK_RESEARCH author-side theorem with exact finite checks. Frozen scientific input fc0f038e7bfd12c886b4d37f900bfb770c0f61ab; EC49FBJ parent commit 74aff4c6debe08da27ddc16b72a3075c2fdc367c. Protected P000/ACTIVE unchanged.

## Mother problem and local result

The nine-window H2–H9 mother problem minimizes distinct ordered signed-native X6 primitive-prefix edges, with rank-nine observation coverage per horizon and at most five complete positive BRC cache keys. Earlier author-side global bounds are 80 <= E*(H9) <= 94. EC49FBJ computed 161 for fixed early key L=(4,3,1), late key M=(8,2,1), versus 136 for L=(5,2,1), the same M. This unit proves an exact structural reason that complete terminal-prefix reuse is available only in the second of these two schedules, and gives a direct rank-preserving lifting construction.

## Definitions

Native ordered signed primitive expansions: a=(-1,-1), c=(1,2,-1,-2), d=(2,1,-2,-1), e=(3,1,1,-3), f=(1,-1), g=(2,-2). Let N(w) concatenate these signed primitive steps; D(w) is signed X6 displacement, and K(w) the *six* positive-axis counts. For a legal horizon-h terminal with D=(2,0,0,0,0,0), K=(x,y,z,0,0,0), exact operation counts satisfy

#a=z-1, #e=z, #c+#d=x+y-h-1, #f=h+1-y-2z, #g=h+1-x.

The frozen 9-state DFA's accepted nonzero signatures 1,2,4,8,16,32 reside in states 2..7; both f and g act as self-loops on each of these six states.

## Theorem 1: primitive terminal prefix iff operation-word prefix

For all operation words u,v, N(u) is a primitive-step prefix of N(v) iff u is an operation-letter prefix of v.

Proof. The first *two* signed native steps of a,c,d,e,f,g are, respectively, (-1,-1),(1,2),(2,1),(3,1),(1,-1),(2,-2). These pairs are all distinct, hence operation expansions form a prefix-free, uniquely decodable code. A complete encoded word that prefixes a second complete encoded word ends on an operation boundary. The converse follows by concatenation. QED.

Corollary (positive BRC-key dominance): if N(u) prefixes N(v), then K_i(u) <= K_i(v) for all six native axes, because a prefix cannot contain more positive steps than its extension. In particular (4,3,1,0,0,0) is incomparable with (8,2,1,0,0,0) at E2; no complete early terminal can be a native primitive prefix of any late terminal. Shorter interior prefix sharing may still occur.

## Theorem 2: exact f/g observer-stable lift

Let w be any legal horizon-h word with D(w)=(2,0,0,0,0,0), K(w)=(x,y,z,0,0,0) and nonzero accepted signature s. For all p,q>=0 and every operation suffix t consisting of p copies of f and q copies of g in any order, wt has horizon h+p+q, the same endpoint and signature s, full key (x+p,y+q,z,0,0,0), and N(w) as a primitive prefix.

Proof. f=(+E1,-E1) and g=(+E2,-E2) have exactly zero signed displacement and increase their indicated positive-key coordinate by one; both transitions fix each accepted observer state 2..7. Ordered native concatenation retains N(w). QED.

Converse for this exact paired horizon/key shift: if K(v)=(x+p,y+q,z,0,0,0), |v|=h+p+q and N(w) prefixes N(v), then v=wt for exactly p f and q g. Theorem 1 gives the letter-prefix relation. Subtracting the exact word-count formulas shows unchanged a,e,c+d and only p extra f and q extra g. No a,e,c,d can occur in t. QED.

## Full-rank coverage transfer and constructive witness

Take L=(5,2,1), M=(8,2,1). H4 and H7 have the same four needed signatures {1,2,4,8}; similarly H5,H8, while H6,H9 need {16,32}. Append fff to each L-word chosen at H4,H5,H6: they become legal, identical-signature M-words at H7,H8,H9. The original H2={fe,ge}, H3={feg,gef} use three complete BRC keys; adding L and M uses five.

An executed Python standard-library enumeration covers all legal ordered words in the stated L/M domains. H4/H5/H6 have 24/120/50 eligible words for each of L=(4,3,1) and L=(5,2,1). H7/H8/H9 under M=(8,2,1) have 210/672/224. Across all nine early-late horizon pairs, L=(4,3,1) has zero native complete-terminal prefix pairs. L=(5,2,1) has exactly 24 (H4→H7), 120 (H5→H8), 50 (H6→H9), and zero for the other six pairs; all 194 actual matches are u→ufff with unchanged signature. A further 6,208 lift checks (194 words x 16 (p,q) pairs x 2 suffix orders) passed.

The explicit ten early words appear in the saved JSON/standard-library program. Their original H2/H3 plus H4/H5/H6 prefix union has **82** distinct signed-native edges. Appending fff to all ten gives a legal complete H2–H9 witness with **142** edges and exactly five keys. Each L terminal has the same native depth 14, with distinct primitive strings. Thus the ten six-step fff tails are disjoint and account exactly for 60 new edges.

The separate actually-executed SciPy 1.17.0/HiGHS early H4–H6 MILP returned status=0, objective=66 above 16 prepaid H2/H3 edges, dual bound=66, MIP gap=0, and 1,236 trie edges; its executable source is included. Standard-library verification independently checks the 82/142 witnesses. The 142-edge lift construction is a useful solver-independent *completion route*; EC49FBJ's 136-edge optimum remains a stronger upper bound for this particular fixed-key schedule.

## Reproduction, scope and next unit

Run python VERIFY_EC49FBK_MIN.py to reproduce all 6,208 checks, all primitive-prefix pair counts, native displacement/key audits and exact 82/142 prefix unions; the JSON file stores the executed values. Run python OPT_EARLY_LOCAL.py (NumPy/SciPy) to reproduce the early 0-1 MILP. Theorems 1 and 2 are algebraic statements for every legal word in the declared six-letter signed-native model. The enumerated terminal pairs cover precisely the two stated early L values, the stated M, and horizons H4–H9.

Next EC49FBL: use positive-key coordinate dominance and exact f/g horizon shifts to prune/price all 124 EC49FBH feasible pairs, including mixed-key H4–H9 schedules; quantify interior prefix sharing, compare alternative H2/H3 roots, and seek a <=93-edge complete witness for the mother target. Research status: AUTHOR_PROOF / EXACT_FINITE_AUDIT_PASS / LOCAL_MILP_RESULT; formal native CLAIM/Result and independent Driver review depend on actual current authorization.
