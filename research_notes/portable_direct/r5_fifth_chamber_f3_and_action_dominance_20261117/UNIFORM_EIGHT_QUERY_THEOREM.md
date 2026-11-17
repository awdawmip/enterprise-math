# R5 fifth noise chamber: a minimal uniform eight-query simulation alphabet

**Frozen exact source** `435e77af0d180eac32bd1f9c4c464bc4010b7551`; exact count input SHA-256 `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`. The derived observer uses all 256 masks and 101 integer budgets 214,...,314.

Define the real fifth noise chamber by

\[
L=25845652773852463277015040000 \le \tau=2\eta <
U=58182461585441404127941754880.
\]

## Exact theorem

The eight query budgets

\[
J_8=\{214,215,216,217,223,294,295,296\}
\]

form a **uniform cost-nonincreasing, one-query normal-support domination alphabet** for all 101 original budgets throughout the entire chamber: each original k has a single replacement j(k) in J8 with j(k)<=k, valid for every real tau in [L,U).

Consequently **for every finite f** of arbitrary unmarked corrupted observations, any adaptive decision tree of the 101-budget model can be replaced by a decision tree using J8 at no greater worst-case cumulative budget, for every tau in the chamber. This statement supplies a strategy-reduction theorem; the minimum cumulative budget itself remains open for f>=4.

Further, eight is the **smallest cardinality of a set with this uniform one-step cost/info domination property**. This cardinality does not assert the smallest alphabet on which a particular optimal decision tree can happen to be represented.

## Mathematical proof

For each pair of actual masks p<q, let `d_k(p,q)=|N_p(k)-N_q(k)|` be their exact integer count gap.

At a fixed tau, budget j weakly dominates k for the declared one-query simulation if and only if

\[
\forall p<q,\quad d_j(p,q)\le\tau \implies d_k(p,q)\le\tau.
\]

When the premise holds, the normal-response support of every j reading has k-center diameter at most tau, so it is contained in a valid k normal-response support. Each normal j answer can be mapped to a normal k answer for the real state. An arbitrary corrupted j answer maps to an arbitrary simulated k answer, never increasing the number of corruptions. The reverse implication follows by choosing a j reading compatible with a pair p,q that no k reading can jointly support.

For all real tau in [L,U), the implication holds **exactly when** there is no pair p,q satisfying

\[
d_j(p,q)<d_k(p,q),\qquad d_j(p,q)<U,\qquad d_k(p,q)>L.
\]

Indeed such a pair permits a tau in
`[max(L,d_j),min(U,d_k))`, and conversely a failed implication at any tau yields the three inequalities. Therefore one finite all-integer check covers the entire continuum of noise amplitudes, with no interpolation assumption.

Exhaustively checking all 32,640 unordered mask pairs for each tested j,k finds a uniform j(k) from J8 for each of the 101 budgets. The distribution of assigned j(k) is:

| j(k) | 214 | 215 | 216 | 217 | 223 | 294 | 295 | 296 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Number of original budgets | 4 | 1 | 1 | 6 | 68 | 1 | 3 | 17 |

**Minimality for this domination property:** at tau=U-1 each of the seven budgets 214,215,216,217,223,295,296 lacks any strictly cheaper dominator among the full 101; all seven must belong to a cost-nonincreasing uniform replacement alphabet. Yet at tau=L none of those seven can dominate original query k=294: the genuine mask pair (0,48) has gap zero under each of the five eligible cheaper candidates 214,215,216,217,223, whereas query 294 has gap exactly `45392032647559604256815185920`, greater than L. Thus at least one eighth action is required, and J8 achieves eight.

## Reproduction and scope

The source program `VERIFY_R5_UNIFORM_EIGHT_ACTION_DOMINANCE.py` loads and SHA-checks the pinned 256x101 count table, evaluates the exact pairwise implication over the full chamber, checks irredundancy witnesses and writes the complete mapping/results JSON. Local execution returned

`PASS_R5_FIFTH_CHAMBER_UNIFORM_EIGHT_ACTIONS_MINIMAL_DOMINANCE`.

This improves the earlier exact-seven-action theorem at the **single threshold U-1**, where k=294 is also dominated. Full source/proof/checker/JSON/count input and SHA256 manifest are contained in the R5 reproduction bundle. The claim is a derived discrete scalar-observer result, `AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED`, independent of P000 native-space promotion and authenticated Task/CLAIM status.

**Next:** compute full-256 f=4 with only eight essential uniform budgets and test the candidate cost 4535; seek an all-f analytic recurrence.
