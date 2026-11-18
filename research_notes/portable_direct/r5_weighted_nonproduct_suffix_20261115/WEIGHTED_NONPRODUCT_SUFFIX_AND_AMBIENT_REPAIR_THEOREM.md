# R5: exact weighted non-product suffix coupling and ambient repair residual

Date: 2026-11-15
Scientific parent (frozen): 435e77af0d180eac32bd1f9c4c464bc4010b7551
Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED

## Model and source dependencies

This is an explicitly NEW weighted auxiliary observer, not a mutation of the parent 954-event input or native Heartbeat-X6/P000 axioms. Reuse the proven R5 all-m product theorem in PR #2427, commit 669c96f388bb2d84ef297e9a2ee09a5751c97353 (COUPLED_21_UNBOUNDED_SWITCH_THEOREM.md), and the exact seven-event core / radius-two repair certificate in commit 689a40d460ee119db003fd9f5b57414303b239f8 (GRAPH_COUPLED_SUFFIX_EXACT_REPAIR_THEOREM.md).

For each integer m>=2, take the one-dimensional integer event gap sequence (3,2,2,3,(2,1)^m). There are n=5+2m events. Choose K=m+3 distinct event-index centers; every event must lie within integer positional distance 2 of a chosen center. For mask t=0,a,b,ab, closure a shortens gap 0 by 1 and closure b shortens gap 3 by 1. The original integral total nearest-center distance is J_t(S). The already proved global optimum is B=m+4 in all four masks. Its complete optimizer families are G_t x {0,1}^ell, ell=m-1, with seven-event core G_t and one chosen index from each suffix pair (7,8),(9,10),... . The suffix bit h_j is 1 when the RIGHT index of that pair is chosen.

The four seven-event core sizes are 5,12,9,17. Their common old family is
G_0 = {0125,0135,0235,0245,0246},
where each digit string denotes a zero-based event-index subset. Every core in G_0 and G_b contains index 0. The cores omitting index 0 are:
A_a = {1235,1245,1246,1345,1346},
A_ab = {1235,1236,1245,1246,1345,1346}.
These complete exact enumerations follow by checking the 35 four-center subsets of seven events in each mask; the attached independent code reconstructs them.

## Integral-gap perturbation lemma

Let J be integer-valued on a finite nonempty feasible population, with minimum B, and let g map that population to {0,1}. For 0<epsilon<1 every optimizer of J+epsilon*g is an optimizer of J. If some old optimizer has g=0, the new minimum is B and the new optimizer family consists exactly of the zero-penalty old optimizers. If none has g=0, the new minimum is B+epsilon and the complete original optimizer family is retained.

Proof: each nonoptimal J-value is at least B+1, while all old minimizers have perturbed value at most B+epsilon < B+1. Restrict to old optimizers and compare g=0 and g=1. QED.

All weighted calculations below use epsilon=1/2; multiplying the objective by 2 gives exact integer arithmetic.

## Theorem A: exact phase change and a halfcube optimizer restriction

Define g_half(S)=1 if (0 in S) OR (8 not in S); otherwise g_half(S)=0, on ALL feasible center sets, and J_t^half(S)=J_t(S)+g_half(S)/2. This is nonseparable in the core-presence and suffix-selection Boolean variables; its mixed second difference is nonzero.

For EVERY integer m>=2 the exact weighted minima and full optimizing families are:
t=0: B+1/2; G_0 x {0,1}^ell; count 5*2^ell.
t=b: B+1/2; G_b x {0,1}^ell; count 9*2^ell.
t=a: B; A_a x {h:h_1=1}; count 5*2^(ell-1).
t=ab: B; A_ab x {h:h_1=1}; count 6*2^(ell-1).

Proof: on the inherited optimizer skeleton g_half is zero precisely when index 0 is absent from the core and h_1=1. The exact G_t core lists determine all possibilities. The integral-gap lemma excludes every nonoptimal original center set regardless of its penalty and proves all four statements. QED.

For equal-cardinality center sets define replacement distance d(S,T)=|S\T|. A precommitted radius-r old repair library is a subset L of the complete OLD weighted optimum family such that every NEW weighted optimizer lies within r replacements of at least one member of L. Denote its minimum size by kappa_t^half(m,r).

## Theorem B: exact all-m precommitted repair complexity

For every integer m>=2,
kappa_a^half(m,2)=kappa_ab^half(m,2)=max(2,2^(m-2)).
The worst nearest-old repair distance in either state is exactly 2. The unchanged state-b optimizer family has the previously proved kappa_b^half(m,1)=2^m.

Proof: set D_L=0135, D_R=0246, C_*=1346, C_L=1235, C_R=1246. All three new cores belong to both A_a and A_ab. Exact core distances from C_* to the five old cores in displayed G_0 order are (3,2,3,3,2). Thus, for every allowed first-bit-one suffix h, C_*+h can only be repaired in <=2 swaps by D_L+h or D_R+h, with the suffix IDENTICAL. Each of the 2^(ell-1) suffixes therefore forces its own library element. For ell=1, one old element cannot cover both C_L+h and C_R+h because their respective distances to (D_L,D_R) are (1,3) and (3,1). This gives lower bound max(2,2^(ell-1)).

For ell=1, store D_L+h and D_R+h at the sole allowed suffix. For ell>=2, at every first-bit-one suffix h store exactly one old optimum: D_L+h when h_2=0 and D_R+h when h_2=1. The resulting 2^(ell-1) entries cover all new centers: for each new core C, the core certificate gives d(C,D_L)<=1, or d(C,D_R)<=1, or both core distances equal to 2. Each allowed h has both colors within Hamming radius 1 inside the first-bit-one subcube, while a same-suffix entry handles the dual-distance-2 class. By d(C+h,D+j)=d(C,D)+Hamming(h,j), total distance is <=2. The C_* witness proves worst nearest-old distance is >=2. QED.

## Theorem C: the old ambient suffix space changes the repair answer

Set m=4 and ell=3, Y={000,011}. Define on all feasible sets:
g_Y(S)=1 if [0 in S OR (h(S) not in Y)], otherwise 0,
where h(S) records presence of the right indexes 8,10,12. Minimize J_t+g_Y/2. The integral-gap lemma gives weighted optimum values (8.5,8,8.5,8), in scenario order (0,a,b,ab), and complete family sizes (40,10,72,12). The old suffixes range over the ENTIRE cube {0,1}^3; new a/ab suffixes are only Y.

Claim: kappa_a^amb(m=4,Y,2)=kappa_ab^amb(m=4,Y,2)=3.

Proof, lower bound: C_*+000 and C_*+011 each force a distinct same-suffix old configuration of type D_L or D_R. Therefore at least two entries are needed. These suffixes differ in two bits. If precisely two entries are stored, one forced D_L/D_R color must occur at each suffix. At either suffix, the other entry is too far in suffix distance to repair C_L or C_R with core distance >=1 and total budget 2. Whichever forced color was selected, one of C_L or C_R has core distance 3 from it. Hence two entries cannot suffice.

Proof, upper bound: the THREE-entry old library {D_L+000, D_L+011, D_R+001} covers all A_a x Y and A_ab x Y. For a D_L-near core use its same-suffix entry. For a D_R-near core use D_R+001, whose suffix is Hamming distance 1 from BOTH 000 and 011. For a core at distance 2 from each, use same-suffix D_L. This exhausts the core certificate. QED.

The old helper suffix 001 is absent from the NEW optimum language but belongs to the OLD optimum family. If old suffixes were artificially restricted to Y too, the earlier common-language result would give |Y|+i(Y)=2+2=4. Thus 3<4 is an exact observer-information-loss witness: restricting old repair possibilities to new optimum states changes the answer.

## Theorem D: genuinely NON-CARTESIAN optimizer sets

To make the core/suffix interaction irreducible even at the optimizer-set level, define a second binary penalty on every feasible S:
g_mix(S)=1 if [0 in S OR (1_{2 in S} != 1_{8 in S})], else 0.
Again use J_t^mix=J_t+g_mix/2. Let A_t^1 be those C in A_t containing index 2, and A_t^0 those omitting 2. The counts are (|A_a^1|,|A_a^0|)=(3,2) and (|A_ab^1|,|A_ab^0|)=(4,2).

For every m>=2, the mixed weighted optimum values are (B+1/2,B,B+1/2,B), and the OLD and b families are unchanged full-cube products. For t=a or ab the COMPLETE optimum family is
(A_t^1 x {h:h_1=1}) UNION (A_t^0 x {h:h_1=0}).
Its size is |A_t|*2^(ell-1), as in the halfcube case, but it is NOT a Cartesian product between core and suffix projections.

Proof: old and b cores all contain 0 and thus receive penalty 1. On the a/ab core families the penalty is zero precisely when the core omits 0 and h_1=1_{2 in C}; the gap lemma proves the exact family and cost. C_1=1235 (index 2 present) and C_0=1345 (index 2 absent) are each valid in both states. At fixed remaining suffix bits, (C_1,h_1=1) and (C_0,h_1=0) are both optimal; the two cross-products are not. Therefore no Cartesian product of the core and suffix projections can equal the optimizer family. QED.

Exact finite radius-two set-cover computation for the MIXED variant, using all old weighted optima, gives (kappa_a,kappa_ab)=(2,2) at m=2 and (3,4) at m=3. The all-m mixed repair-library classification remains open; these finite counts are not extrapolated.

## Executed verification and scope

The companion Python verifier enumerates all feasible distinct K-center subsets in each closure mask for m=2,3,4,5,6, uses exact doubled integer objectives, reconstructs the seven-event core, checks all four complete family identities for BOTH penalties and the nonproduct crossed-pair witness, and verifies halfcube radius-two library witnesses. It exhaustively minimizes library sizes at m=2,3 and, for Y={000,011}, at m=4 proves no 1- or 2-entry library works and checks the 3-entry witness.

Actual local verifier output: PASS_R5_WEIGHTED_NONPRODUCT_AMBIENT. Full finite report: EXACT_R5_WEIGHTED_SUFFIX_EVIDENCE.json. Universal theorems use the inherited product theorem, integral-gap argument and exact seven-event certificate, rather than finite tests as universal justification.

Structural residual interpretation: the source (OLD) optimizer language and target (NEW) optimizer language are different observers; collapsing the source to the target erases valid old helper states. The auxiliary model retains individual center-index, suffix-bit and path provenance. This does not assert a native X6 embedding or execution of a BRC-only physics operation.

Next science: determine the all-m exact minimax repair/library kernel for g_mix; for general regular target language Y with full-cube old states, compute the ambient helper correction and its smallest observer-preserving automaton. Keep the frozen parent input pin and P000 unchanged.