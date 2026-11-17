# R762DA — Sparse-time named-Port observation and exact BRC seed cost

Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS. Publication: TP2-8B7E13C5904A2D6F1142. Researcher: EM-X6-3050F6. Date: 2026-11-17.
Frozen science: P000 V5 and signed X6 at a72226e2430ffa4786321ac86e7f0c599d5f0389; taskbook at e3f42efac29a2da2d95be391f3231a664e2fade0.
Prior exact candidate results: R762CX (weighted C3 endpoint gcd), R762CY (every sliding Port window), R762CZ (named microbranch ID windows), GitHub Draft PR #2632 @ ad4d56476fe1eb4eb6bb173350ac3c481e86570a.
Status: new self-contained conditional finite-group positive N-BRC theorem; finite exact author verification; independent review NOT_REVIEWED. This is not native TRIADIC_CLOSURE_E event admission.

## Typed model and observer

Let G be an arbitrary finite group with identity e. Let A be a nonempty finite family of *individually named* right-multiplication branches, each with a group increment a in G and a positive integer multiplicity w_a. Set D=sum_a w_a. The initial state is e. A length-n source-branch word has weight equal to the product of its step multiplicities; after normalization, each of the D individual microbranches at each step has equal probability 1/D.

For z in G let C_n(z) be the nonnegative integer weight of source words of length n whose ordered group product is z. Then C_0(e)=1, C_0(z!=e)=0, sum_z C_n(z)=D^n, and

  C_{m+n}(z)=sum_{y in G} C_m(y) C_n(y^{-1}z).

Set g_n=gcd_{z in G} C_n(z)>0, including zero entries in the gcd.

Fix a horizon h>=1 and ONE prescribed sparse sampling schedule 1<=t_1<...<t_k<=h. The observer jointly reads (X_{t_1},...,X_{t_k}), not all sliding windows and not all later adapted queries. A deterministic realization assigns one completely legal h-step microbranch trajectory to each of M equally likely initial seeds, with no future random input. M is the least number of seeds reproducing this entire one-shot named-state joint law exactly.

This abstract finite group is a combinatorial path carrier, not a replacement for signed-X6 Cells, six native axes, or a physical force law. Named Port group labels are internal states, not an added spatial dimension.

## Theorem A: exact joint-sampling information budget

Put t_0=0, d_j=t_j-t_{j-1}>0 and s=t_k. For every finite G, every weighted branch family and every prescribed schedule above,

\[
\boxed{M_{\min}(t_1,\ldots,t_k)=
\frac{D^s}{\prod_{j=1}^{k} g_{d_j}}.}
\]

The formula is independent of the unobserved tail h-s. All factors and the quotient are integers. The minimal initial information in fixed-length bits is ceil(log_2 M_min); M_min counts equiprobable seeds rather than a uniform bit-string encoder.

**Proof (joint-law factorization).** A particular observed tuple (x_1,...,x_k), x_0=e, has integer path count through time s

  N(x_1,...,x_k)=prod_j C_{d_j}(x_{j-1}^{-1}x_j).

Its exact probability equals N/D^s. The change of variables (x_1,...,x_k) <-> (x_0^{-1}x_1,...,x_{k-1}^{-1}x_k) is a bijection of G^k, including the noncommutative case. Thus all possible increment variables range independently over G; prime-by-prime minima of the valuation of their product give

  gcd_{x_1,...,x_k} N(x_1,...,x_k)=prod_j g_{d_j}.

This product divides D^s because each g_d divides sum_z C_d(z)=D^d. Therefore the exact common reduced denominator of the joint event probabilities is M_0=D^s/prod_j g_{d_j}. An M-equiprobable-seed realization forces M_0|M.

Conversely, for each tuple with N>0, choose one genuine legal path realizing that tuple and extend it arbitrarily to the remaining h-s steps. Allocate exactly M_0 N /D^s seeds to that path. These allocations are nonnegative integers and sum to M_0. This constructs a valid deterministic full-path realization using exactly M_0 seeds. Lower and upper bounds agree. QED.

Unlike a sliding-window hierarchy, Theorem A does not demand consistency with additional unrequested joint laws; the selected schedule is the complete declared observer.

## Theorem B: exact cost of inserting one extra probe

If a gap of length a+b is split by an additional named-state observation into positive gaps a and b, then

\[
\boxed{\frac{M_{\rm new}}{M_{\rm old}}=
\frac{g_{a+b}}{g_a g_b}\in\mathbb Z_{\ge1}.}
\]

**Proof.** The convolution formula shows that every C_{a+b}(z) is divisible by g_a g_b. Hence g_a g_b divides g_{a+b}. Apply Theorem A. QED.

This is a scope-typed information certificate: inserting an observed time can strictly increase required information even when the endpoint marginal remains unchanged.

## Corollary C: complete sparse-probe parity law on the prior weighted C3 candidate

For the specifically declared three-named-Port cycle, p clockwise and q anticlockwise positive microbranches, let g=gcd(p,q), p'=p/g, q'=q/g and D'=p'+q'. Only Port states (not individual microbranch IDs) are observed. The normalized Port process has weights p',q'. Applying Theorem A with the R762CX proved formula

  g'_d=1 if 3 does not divide D';
  g'_d=3^{floor((d-1)/2)} if 3 divides D', for every d>=1,

gives for s=t_k

\[
M_{\min}=
\begin{cases}
(D')^s,& 3\nmid D',\\
(D')^s/3^{\sum_j\lfloor(d_j-1)/2\rfloor},&3\mid D'.
\end{cases}
\]

If 3|D', define E as the number of even gaps among d_1,...,d_k. Then

\[
\boxed{M_{\min}=(D')^s/3^{(s-k-E)/2}}.
\]

Inserting a probe into a gap has exact seed-cost multiplier 1 iff both resulting subgaps are odd; otherwise the multiplier is 3. If 3 does not divide D', every insertion has multiplier 1 in this one-schedule observer.

Example: p=1, q=2, last observation at time s=6. Endpoint-only costs 81 seeds. The two-time schedules {1,6},{2,6},{3,6},{4,6},{5,6} require respectively 81,243,81,243,81 seeds. Therefore sampling time placement, not merely the number of sampled instants, is an exact BRC information resource.

## Corollary D: separately inexpensive observers need not be jointly inexpensive

Even in the same fixed candidate source law, exact per-schedule compression budgets do not compose automatically. Let p=1, q=2, D=3 and end time 6. The individually queried schedules {1,6} and {3,6} each require only 81 seeds. Their *jointly observed union* {1,3,6} has gaps (1,2,3), so Theorem A requires 3^6/(g_1 g_2 g_3)=729/3=243 seeds. The two smaller joint distributions are marginals of the larger one; a purported 81-seed representation certified only for each schedule individually is not automatically certified to supply their simultaneous three-time correlations.

This is an explicit observer-composition residual, not an inference that both separately requested marginal laws could never be realized with 81 seeds. The additional factor 3 applies precisely when the user/event can jointly request all three named Port values. Whether native signed E licenses that compound observation is unresolved.

## Reproducibility and limits

R762DA_VERIFY.js independently enumerates joint increment histogram products with BigInt: all p,q=1..6, all 18,072 nonempty timestamp schedules within 1..h for 1<=h<=8, including 669,348 positive and 2,476,044 zero joint-event numerators. It also checks 1,080 schedules with 1<=p,q<=3 in a nonabelian S3 carrier (1,235,250 event numerators). For each case, actual gcd of every joint-event numerator equals the product of the gap gcds, and the exact quotient is integral. Theorem A is proved for all finite groups and all horizons; bounded enumeration is supporting evidence only. Refer to R762DA_EVIDENCE.json.

P000, the 120-degree PERP_E definition, the six signed Cell axes, triadic balance arity and the mandatory joint-relation preservation rule remain unchanged. The claims above concern an explicitly chosen conditional N-BRC group-valued path observer, not a certification that native TRIADIC_CLOSURE_E permits the probes. An actual licensed signed Cell/Link/Port update and V17/V29/V39 transport must determine which observation schedules, microbranch identities and R762CH/CK pair-area residuals are legally queried. Until that is proved, discard no other residual in native dynamics.

Next discriminating question: locate an authenticated native E event predicate, derive the actual allowed sparse read times and source/area fields, and test whether the one-schedule theorem composes under legal adaptive queries or requires a stronger automaton/observer carrier.
