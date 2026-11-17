# R5 Fifth Chamber: sharp f=3 adaptive unmarked-error cost and seven-query dominance

Scientific input: frozen source pin `435e77af0d180eac32bd1f9c4c464bc4010b7551`; exact 101-budget/256-mask integer table `EXACT_R5_ALL_101_BUDGETS.json`, SHA-256 `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`. Derived scalar observer only; native P000/X6 and BRC provenance remain typed separately.

## Theorem 1 — exact f=3

For every real noise amplitude eta such that

\[
25845652773852463277015040000 \le 2\eta
< 58182461585441404127941754880,
\]

when the hidden state is any of 256 masks, available integer budgets are k=214..314, normal readings lie within eta of the exact N_h(k), and at most THREE readings can be arbitrarily corrupted without markers, the minimum over adaptive decoders of the worst-case cumulative queried budget is exactly

\[
\boxed{C_3=3585.}
\]

With the previously certified f=0,1,2 results this yields C_f=735+950f for f=0,1,2,3 in this fifth chamber (no universal-f claim).

**Lower certificate:** constrain the adversary to the actual five masks (18,24,82,34,17) at the left endpoint L, retaining all 101 actions. The prior exact five-state Bellman certificate `r5_fifth_chamber_five_state_minimax_20261117/RESULTS_R5_FIFTH_CHAMBER.json` returns V_3(L)=3585 with 1733 memoized states.

**Upper certificate:** at the rightmost integer gap threshold U-1 use all 256 states but permit only budgets (214,215,216,223,296). The executed exact Bellman computation returned V_3(U-1)=3585, visiting 1,704,343 memoized states. Executed program `TEST_F3_REDUCED.py`, and output:
`actions 5 [216, 223, 296, 214, 215]
F3= 3585 states 1704343 sec 52.67717920699994`
are included in the downloadable reproduction package.

The center counts are integers; all response masks at real tau<U are contained in the masks at tau=U-1. Monotonicity between the endpoint upper and lower certificates proves the exact claim for the entire half-open interval.

The Bellman state is (S_0,...,S_f), where S_i contains hidden states consistent with precisely i corrupted readings. For a possible normal-reading compatibility set A and B=complement(A), update S'_0=S_0∩A and S'_i=(S_i∩A) ∪ (S_{i-1}∩B). Stop if the union is a singleton. Compute min_k[k+max_A V(S')] over inclusion-maximal response sets A. For integer count centers these are exactly the maximal supports of sliding intervals [c,c+tau]. The full verifier, prior five-state result, frozen exact input and execution log are in the reproducible package; a redundant full-verifier replay exceeded the available synchronous execution window and was not reported as passing.

## Theorem 2 — seven-query action dominance at tau=U-1

At tau=U-1, the 101 available query budgets are cost-/information-dominated by the seven-query set

\[
J=\{214,215,216,217,223,295,296\}.
\]

For each k in 214..314, exhaustive integer compatibility-mask checking finds j in J with j<=k and for **every** inclusion-maximal allowed response support A of query j, a response support B of k with A⊆B. A true-normal j reading can therefore be simulated as a true-normal k reading; a corrupted j reading maps to a possibly corrupted k reading. The number of corruptions never increases. Replacing queries recursively proves that J suffices for the same minimax cost **for every finite f** at this fixed tau=U-1. This statement does not claim a universal closed-form cost, minimal alphabet cardinality, or identical seven-action domination map for other tau.

Selected dominating j frequencies across the 101 k: 214:5, 215:1, 216:1, 217:6, 223:68, 295:3, 296:17. Each of the seven lacks any strictly cheaper single-query dominator at the checked threshold. The exact 101-action inclusion check executed successfully.

## Evidence and frontier

Status: `AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED`. Own author output is independent portable research, **not** a formal CLAIM, Result, Review or Foundation promotion. Full reproduction input digest above. No live owner or authority inferred from historical Researcher-ID. Source PR is Draft #2427.

Next: exact full256 f=4 (five-state lower 4535, previously constructed full256 upper 4539), arbitrary-f analytic bound, or chamber-uniform action dominance verification. Work with BRC joint/provenance-aware observers as a separate typed extension.
