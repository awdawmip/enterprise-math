# R5 addendum: k=7 single-control inert source controllers need exactly 24 states

Date: 2026-11-16. Frozen scientific pin: `435e77af0d180eac32bd1f9c4c464bc4010b7551`. Evidence: **AUTHOR_PROVED / EXACT_FINITE_EXHAUSTIVE / NOT_REVIEWED**.

For the same genuine source-labelled cycle-of-seven-triangles observer, with raw mask u, `q(u)=sum u_i*u_(i+1)`, additive slack s=2 and only commands `Set_0(0/1)`, suppose both commands must act as identity on every controller state (an *inert* controller). Then the exact minimum number of internal states is **24**.

A self-loop state must be invariant under either reset. It therefore contains complete raw pairs `{2t,2t+1}` whenever it contains either member. For each odd source centre r define `P(r)={t in 0..63: both 2t and 2t+1 lie in C(r)}`, where `C(r)={u<=r:q(r)-q(u)<=2}`. The inherited real common-source-library theorem permits replacing any arbitrary old-source library by a canonical labelled `L(r)` for its OR centre. Thus an inert controller with m states exists exactly when <=m of the 64 sets P(r) (odd r=1..127) cover the 64 raw pairs.

**Upper certificate.** The following 24 genuine source centres cover all 64 raw pairs:

`43,47,55,59,63,75,79,83,85,87,91,93,95,101,103,107,109,111,115,117,119,123,125,127`.

For each listed centre r the controller outputs `L(r)` and stores all pairs in P(r). Each named Set operation is a self-loop, preserving membership and resource bound. The verifier checks 108 pair memberships and the complete 64-pair cover.

**Exact lower certificate.** Eliminate any P(r) contained in another P(s), retaining one representative of ties; exactly 38 candidates remain. The attached standard-library Python program exhausts the full 23-set-cover decision tree via `possible(R,m)`: select an uncovered pair, branch on every source centre containing it, delete covered pairs, and decrement m. The only other pruning is the exact bound `|R| > m*max|P(s)∩R|`. This is a complete finite proof by integer recursion. It returns `possible(all_64_pairs,23)=False` after 22 visited memoized states (zero cache hits). No inert controller has fewer than 24 states, matching the upper witness.

Together with the separately [proved 17-state dynamic theorem](R5_K7_SINGLE_CONTROL_EXACT_SEVENTEEN_THEOREM.md), this establishes the exact **seven-state inert penalty**:

`N_dyn(7,{0},2)=17 < N_inert(7,{0},2)=24`.

This strengthens the earlier `r5_partial_single_control_20261116/R5_K7_SCOPED_MILP_AND_UPPER_WITNESSES.md`, where 24 was a numerical MILP optimality report with an exactly verified upper witness. Here the lower bound is independently integer-checked. The result is scoped to the auxiliary source-labelled observer; P000/Heartbeat X6 and Task/CLAIM/Review authority remain unchanged.

**Next:** investigate inert-vs-dynamic growth in k and find a parametric nonmaximal-belief construction matching the static lower bound.
