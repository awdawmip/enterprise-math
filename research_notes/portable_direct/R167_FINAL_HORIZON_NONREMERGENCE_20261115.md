# R167 — Final-horizon scalar-signature collision cannot re-merge after a split

Date: 2026-11-15 (Asia/Shanghai). Status: AUTHOR_PROVED / NOT_REVIEWED.
Scope: external finite-Sturmian binary tied-phase scalar observer; **not** a native X6/BRC transfer theorem.
Frozen science pin: 43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Direct scientific dependencies: R162 (unique swapped-prefix structure) @f451da2665923179eed166c488a1e8063222ca29; R164 (exact signature oracle) @991d99ab20b7669ecf1465eba01e87851855381e; R166 (one-step and prefixwise persistence certificate) @40de7600f89e9cf868db2593e4b4907d46086b6a. P000 and the joint-observer-preservation contract are held fixed.

## Definitions and precise statement

A binary word w of length n has prefix sums p_0=0, p_i=sum_{k<=i}w_k. For a slope theta in [0,1], its feasible intercepts are
I_w(theta) = intersection over 0<=i<=n of [p_i-i theta, p_i+1-i theta].
The **admitted open slope support** is (alpha_w,beta_w) where I_w(theta) is nonempty with a positive-length slope range. In the previous notes the exact signature is S(w)=(alpha_w,beta_w,U_w,V_w), with the endpoint extremal intercept coordinates encoded by the endpoint denominator (R164).

Let u,v be two *distinct admitted* length-m words with S(u)=S(v)=S_0=(alpha,beta,U,V). By R162 their prefix sums coincide except at one internal j, 1<=j<m. Orient so p_j(u)=q-1 and p_j(v)=q; their other prefix sums and terminal count N coincide. Write g(theta)=q-j theta.

For a common appended word z=z_1...z_s of length s>=1, write N_h=N+sum_{a=1}^h z_a and t_h=m+h-j.

**R167A (non-remergence and unchanged signature).** The following are equivalent:
1. u z and v z are both admitted and have identical *final* exact signatures.
2. For every 1<=h<=s, the intermediate words u z[:h] and v z[:h] are admitted and have identical exact signatures.
3. For all 1<=h<=s, the following exact inequalities hold:
   q+t_h beta-1 <= N_h <= q+t_h alpha.

Whenever the conditions hold, **every** intermediate and final signature is S_0 (the initial signature). In particular, a common suffix cannot restore a scalar signature collision that has been lost after a previously equal-signature prefix.

**R167B (contiguous collision lifespan).** Fix two infinite binary sequences whose prefix sums first differ by an adjacent 01/10 swap and agree at all other indices. On the lengths for which both finite words are admitted, the set of lengths at which they have the same valid signature, if nonempty, is an interval of consecutive integers. New collision births can occur after earlier *noncollision* prefixes, but a collision that has ended never reappears under the same appended symbols.

**R167C (final-horizon certificate).** The R166 interval test, formerly established for *prefixwise* preservation, is a necessary and sufficient O(s) exact-arithmetic certificate even when the user observes **only the final horizon**. It follows that any final-horizon preserving suffix has length
s <= floor(1/(beta-alpha))-(m-j),
and there is at most one such suffix of any fixed length. Its symbols, when they exist, are determined successively by N_h=floor(q+t_h alpha), with bit differences in {0,1}. This is arithmetic-operation complexity; input-bit complexity depends on numerator and denominator lengths.

## Proof

**Lemma 1: the common-chord feasibility identity.**
At every slope theta, all old prefixes other than j give identical intercept constraints for the two words. Let K(theta) be the intersection of these common closed strips, including *all* appended prefix constraints under the same suffix. The differing j-th constraints are [g(theta)-1,g(theta)] for u z and [g(theta),g(theta)+1] for v z.

For this fixed theta, both words have feasible intercepts iff K meets each of those intervals. As K is an interval, this is equivalent to g(theta) belonging to K. Therefore the intersection of their slope supports is precisely the set on which the single common chord x=g(theta) satisfies every common prefix strip. This identity uses the entire closed feasibility geometry, not a probabilistic or floating-point argument.

**Lemma 2: strict old common strips in the initial interior.**
For each common old prefix index i!=j and alpha<theta<beta,
p_i-i theta < g(theta) < p_i+1-i theta.
Indeed if an old common lower bound touched g at an interior theta_0, the two affine lines (of different slopes i and j) would cross. Immediately on one side, the common lower bound would exceed g, making u infeasible at a slope inside its admitted support; contradiction. An upper-bound contact similarly makes v infeasible on one side. Since both old supports are (alpha,beta), every such inequality is strict.

**Lemma 3: no proper common-support contraction.**
The slopes where the *final* common chord satisfies every constraint are the closed interval
J=[alpha,beta] intersect intersection_{h=1}^s [ (N_h-q)/t_h, (N_h+1-q)/t_h ].
All t_h>0, so each appended strip has the declared interval form.

Suppose the two final words have identical admitted supports (a,b), necessarily contained in (alpha,beta). Lemma 1 gives the interior of J as (a,b). Assume a>alpha. Then a is the largest of some new lower bounds (N_h-q)/t_h. At theta=a the associated common lower intercept equals g(a). Every common upper intercept is **strictly above** g(a): all old common upper strips are strict by Lemma 2 since a is inside (alpha,beta), and every new upper bound has its right slope endpoint at least b>a. Hence at theta=a and at slopes just below a the common intercept interval intersects [g(theta),g(theta)+1], allowing v z to remain feasible below a. This contradicts a as the left endpoint of v z's support. Therefore a=alpha.

If b<beta, the symmetric argument uses an active *new upper* bound at b. All common lower intercepts are strictly below g(b); the common interval intersects [g(theta)-1,g(theta)] for slopes just above b, so u z remains feasible beyond b. Contradiction. Consequently b=beta. Neither endpoint can shrink if both final supports coincide.

**Completion of R167A.**
Lemma 3 says the final common-chord interval must be [alpha,beta]. Therefore *every* new strip contains the old chord for all theta in [alpha,beta]; equivalently, the inequalities in (3) hold for each h. Conversely, if those inequalities hold, the chord remains feasible for both words at all original slopes after every prefix, while appending strips can never enlarge either support. Thus all intermediate and final supports remain (alpha,beta). At theta=alpha and theta=beta the old extremal intercepts are preserved: the old chord attains the equal-signature extremum for both words at each appropriate endpoint, and every added strip still contains it. Consequently U and V stay unchanged. This proves (3) => (2) => (1), and Lemma 3 proves (1) => (3).

**R167B.**
If a collision occurs at length m and again at n>m, apply R167A with the shared suffix of length n-m: every intervening length collides. Any possible set of collision lengths is therefore contiguous. No existence or location of the first collision is assumed.

**R167C.**
Apply R166C to (3), now equivalent to final-only equality. Each admissible interval [q+t_h beta-1, q+t_h alpha] has width 1-t_h(beta-alpha)<1, so it contains at most one integer N_h; if it contains an integer, that integer equals floor(q+t_h alpha). Nonempty requires t_h(beta-alpha)<=1. Iterating determines at most one binary suffix and gives the length bound. QED.

## Independently executed exact checks

Script: R167_nonremergence_check.py. Data: R167_nonremergence_verification.json.
Run marker: R167_FINAL_ALIAS_NONREMERGENCE_EXACT_PASS.

- All binary words of lengths 2..16: 131,068 candidates, 191 final two-preimage signature classes (Fraction oracle).
- 168 earlier-prefix collision stages within those final classes; no collision->split->collision witness.
- For all 21 original collision pairs at lengths 2..9, exhaustively test every common suffix of lengths 1..6: 2,646 cases, 14 final-collision suffixes; all agree exactly with the interval certificate and with stepwise equality, zero re-merges.
- Mathematical status: author proof plus independent-formula finite checks; no independent reviewer, no formal proof checker, no claim about an arbitrary BRC/native observer.

## Interpretation and remaining problems

The one-bit identity residual can be *born* at a later length even if shorter words had different signatures; R167 addresses **recovery after an existing collision breaks**, not collision birth. The R166 uniqueness/lifetime bound now applies to a terminal-only scalar observer, removing the prior limitation to observers that inspect all intermediate lengths.

Next: classify exact collision-birth lengths for a fixed adjacent swap and test whether finite observer enrichments (signed ports, BRC path/provenance carriers) admit controlled recovery after scalar collision splits. Such a transfer requires the relevant typed observation and future-operation map; do not equate scalar signature identity with BRC branch equality.

Research path: independent portable_direct artifact. The exact RS-S23-AV task publication directory was absent in Source control read as-of 2026-11-15T02:02:17.831751Z; no formal claim, Result, Review, or shared-owner mutation is asserted.