# Stage458-B — Uniform exact rank/unrank for P-POP=0 across c<m, c=m and c>m

Date: 2026-11-05. Status: AUTHOR_SIDE_PROOF / EXECUTED_INTEGER_AND_FINITE_FUTURE_CHECK / UNREVIEWED / NOT_ADMITTED.

## Scientific source and scope

Continue Stage456-B at `c678c1edc28ad05997bf580c35a1c979563f6d15` and Stage457-B at `36e69dde328f86108c3ca6fb24b86e3eb13fb9f0`. Preserve their frozen scientific pins: global knowledge `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`, enterprise-math `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`, P000 blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`; current behavioral rules read separately. This is a restricted native X6 *ordered-history observer* model, not native heartbeat dynamics or physical residual attribution.

Let A=+E1, B=-E1 be two of the 12 signed native spatial directions. Initial original histories P and Q have lengths 2<=m<n, start/end A, have kP,kQ internal isolated B defects and d positional mismatches within positions 1..m. Each source-distinct ordered pair is one positive integer BRC carrier. The full observer is O=(lengths, six-component signed endpoints V_P,V_Q, complete 12x12 directed adjacency histograms J_P,J_Q, positional match count K). On the specified original fibers, m,n,kP,kQ,d determine O. P may not POP; Q may POP at most b times, 0<=b<=n; P may APPEND at most r>=0 times; Q may APPEND any prescribed nonnegative finite number of times. Future APPEND letters may be any of the 12 signed native directions. Future equivalence means identical complete O after every legal *labeled* operation prefix (including arbitrary admissible interleavings).

Put c=n-b and t=min(n,m+r). Index intervals below are inclusive; a fixed terminal Q_n=A is allowed as a redundant key token.

## Theorem 458.1 (uniform exact observable quotient)

On each fixed initial observer fiber F, H~H' under all legal future operations if and only if their repair keys R458 agree:

**Case c>=m.** Let S be the sorted union of {m} if c=m, {m+1,...,t}, and {c,...,n}, intersected with {1,...,n}. Define R458=(Q_i)_{i in S}. Q_n=A is fixed, but retaining it makes the encoder's terminal boundary explicit. No P original letter is exposed by future operations in this regime.

**Case 0<=c<m.** If c>0 define R458=(Q_c,(P_i,Q_i)_{c<i<=m},(Q_i)_{m<i<=n}). If c=0 omit Q_c and start the paired interval at i=1. The last token Q_n=A is fixed.

*Necessity.* On a Q-POP-only path starting from Q_n=A, each removed original directed edge is the single nonzero signed change in J_Q. Knowing the deleted last direction determines its predecessor, so consecutive Q POPs expose Q_{n-1},...,Q_c, with Q_1=A already fixed if c=0. In the c<m regime, once the length of Q falls through i<=m, consecutive changes in K reveal [P_i=Q_i]. Since the initial alphabet is exactly {A,B} and Q_i was recovered, each bit recovers P_i. Independently, P's APPEND with a selected direction z at index m+j (1<=j<=r, m+j<=n) probes [Q_{m+j}=z] through K. Varying z across the 12 available directions identifies the original Q_{m+j}. Thus every nonfixed key coordinate is distinguishable by some labeled future. This uses the full directed edge observer, not just scalar defect counts.

*Sufficiency.* All removed original Q edges and endpoint changes can be reconstructed from the exposed Q predecessor tail; P's original edges are never removed. All appended steps and new edges are explicit future labels. For cross-source K, the initially hidden paired prefix's aggregate matches are already fixed by initial K. In c<m, subtract the exposed paired match bits to recover the hidden common-prefix contribution, which is never separated by Q POP. In c>=m, neither source loses any original position <=m, so its initial matching contribution remains fixed. Every new matched position beyond that stable prefix is between exposed original letters or labeled appended letters. Therefore every O along each legal labeled future path is reconstructed from initial O and R458.

The split at c=m is substantive: exposing Q_m by Q POP is a boundary state, while for c<m a newly exposed P_i is recovered from a Q match bit. No source labels are erased by this quotient.

## Theorem 458.2 (uniform exact BRC support, population, rank and unrank)

For c<m, invoke the Stage457-B hidden paired-prefix T transfer and indexed suffix automaton (at its immutable source pin). For c>=m use this boundary/hidden-gap transfer:

T_m(q,j) = number of length-m admissible joint P/Q prefixes with exact kP B in P, exactly j B in the Q prefix, exactly d mismatches, and Q_m=q. T_m uses states (i, B_P, B_Q, mismatches, last_P, last_Q), nonnegative integer additions and the P_m=A endpoint constraint.

When c>=m, S is the visible Q key's index set. For a candidate key w on S, let v=#B at visible positions >m; let first=Q_{m+1} if exposed; let lastL=Q_t if t>m; let right=Q_c if c>m; and let Q_m be exposed when c=m. Put g=max(0,c-t-1). Let U_g(a,z,h) count length-g binary B-isolated hidden Q gaps with left neighbor a, right neighbor z, and exactly h B steps, enforcing both adjoining edges. It is an exact integer transfer; U_0=1 only for the appropriate no-gap case.

The exact class population is

M(w) = sum_{q in {A,B}} sum_{j>=0} T_m(q,j) *
       [Q_m=q when Q_m is indexed visible] *
       [not(q=B and first=B) when Q_{m+1} is indexed visible] *
       G(j,q,w)

where G=[j+v=kQ] if g=0, and G=U_g(lastL if t>m else q, right, kQ-j-v) if g>0. The visible-key automaton itself enforces all consecutive visible B-isolation edges and Q_n=A. This factorization preserves the *hidden Q_m boundary*; naive independent prefix/gap multiplication without its predecessor state overcounts.

Process the sorted S positions with state (position, visible-B count, Q_m, Q_{m+1}, Q_t, Q_c, last visible Q). At a terminal w, return (support,population)=(1,M(w)) when M(w)>0 and (0,0) otherwise; sum these exact integer pairs backwards over available letters A,B. Memoization collapses keys with identical sufficient boundary summaries without enumerating all original histories or visible keys. It returns q_F and |F|. After precomputation, lexicographic rank and unrank descend the supported-key DP using subtree support counts (O(n) transitions), and terminal M(w) gives exact original-history population.

For fixed binary alphabet and kP,kQ,d<=n, both algorithms have polynomially many states and operations; O(N^6) arbitrary-precision integer operations is a deliberately conservative common upper bound, with N=max(m,n). Counts are at most 2^(m+n), so integer bit length remains O(N). Reporting this operation bound does not assert O(N^6) bit complexity. The implementation imports the pinned Stage457-B Counter for c<m and implements the c>=m transfer directly. It never substitutes total BRC population for Boolean support.

## Corollary 458.3 (POP refinement and population conservation)

Fix all initial-fiber and future APPEND parameters, vary only Q's POP budget b. As b increases, the permitted labeled operation set contains the previous one. Therefore the resulting equivalence partition refines: q_F(b+1)>=q_F(b). Every earlier class C is the disjoint union of its refined classes, and its positive source-distinct population is the sum of their populations. This identity is exact and holds at the boundary c=m.

For (m,n,kP,kQ,d)=(64,80,15,17,1), with r=0, the exact class counts for b=15,16,17,18 are 301,315,616,1232, respectively; in particular crossing c=m (b=16) to c=m-1 (b=17) splits many classes while keeping |F|=5,061,384,194,832,966. With r=3, b=5 gives 55 classes and b=16 gives 315. Larger b can create finer quotients without changing total source mass.

## Executed evidence and limitations

Exact integer program `STAGE458B.py` imports the previously published Stage457-B program by its repository-neighbor file path, otherwise by an explicitly local copy. Its independent original-word oracle checked 2,425 finite parameter instances (1,047 nonempty, 288 with c=m), with 4,453 per-key mass/rank/unrank comparisons. Marker: `STAGE458B_UNIFIED_ZERO_P_POP_RANK_PASS`.

Independent full-observer `STAGE458B_FUTURE_TEST.py` recurses the complete legal labeled future trees for small budgets, using all 12 signed X6 APPEND letters, full six-component endpoints, full directed adjacency histograms and K. It compared 448 pairs across 352 initial observation fibers, including c<m, c=m and c>m; 51,711 memoized tree states; marker `STAGE458B_FULL_NATIVE_FUTURE_TREE_PASS`. This is a *finite crosscheck*, not a replacement for the theorem's general symbolic proof. The program does not claim to compute true physical time evolution, mixed-phase amplitudes, formal proof-checker certificates, or fully general 12-letter initial histories.

## Next Stage459-B

1. Extend the uniform rank/unrank to pP>=1 with both original predecessor tails, retaining the exact join state between the hidden joint prefix and two indexed visible suffixes.
2. Check the minimal sufficient observable state when the *initial* alphabet has >=3 native directions, including cases where one match bit does not identify the opposite letter.
3. Prove a tighter output-sensitive/bit-complexity bound, and test exact class population refinement at the c=m transition on a nontrivial fiber by an explicit parent-key projection.

These are author-side results awaiting independent Driver review; no CLAIM, Result, accepted theorem or P000 modification is asserted.
