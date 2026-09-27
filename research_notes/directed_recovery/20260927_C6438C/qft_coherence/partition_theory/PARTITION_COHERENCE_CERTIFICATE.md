# Work partitions certify direct fair replacement

Status: AUTHOR_SYMBOLIC_DERIVATION / SHARED_CONTEXT / NOT_ADMITTED.
Activity `RA-CAAAC604CB513AEA8BBC1DFC`; current EM intake `e8c5726a22d78c8d3623611afd33f4fe76b46321`; parent verified the actual startup guard and GK lease `f44ed5959c92e6e088c61c102951d1ab2c5e98d4`. The current BRC-only Markdown and JSON constraints were read. This unit performs symbolic derivation and specifies a statistical certificate; it claims no new numerical propagation or executed partition sampler. Root implements a separate bounded two-bin instance.

The input is the actual complete native instrument. Every signed residual coordinate and the time order of every feedback word remain in the state. A positive probability observer will be used only to bound an explicitly identified signed coherence expression; it is not substituted for that expression.

## 1. Raw history weights and the local joint kernel

At depth i and measured history h let v_h(z) be the full real D-coordinate raw row, and let

    M_h = sum_z ||v_h(z)||^2,
    x_hz = v_h(z),             y_hz = T_h v_h(P_i^-1 z),
    a_hz = ||x_hz||^2,         b_hz = ||y_hz||^2,
    c_hz = <x_hz,y_hz>,        L_h = sum_z |c_hz|.

P_i is the actual typed work permutation; T_h is its actual ordered complete orthogonal feedback. No commutation, ideal phase, or two-mode projection is assumed. The raw branch recurrence is

    v_(h,sigma)(z) = (x_hz + sigma y_hz)/2.

Completeness gives sum_h M_h=1 at each depth. In the exact single-walker representation, W conditional on h has mass a_hw/M_h. Independently choose a fair proposal arm and set Z=W or P_i W. Conditional on h, the proposal law is (a_hz+b_hz)/(2M_h). The exact plus-bit probability given z is

    1/2 + c_hz/(a_hz+b_hz).

Replacing that score by a fair bit, while retaining the proposal and the new latent label Z, changes its joint bit/label kernel by exactly L_h/(2M_h). Averaging the conditional transition TV over the exact joint parent law (h,W) yields

    layer joint error = (1/2) sum_h L_h.                    (1)

Equivalently write lambda_h=L_h/M_h and (1/2) sum_h M_h lambda_h. In particular one must neither drop the history weights from normalized quantities nor multiply raw L_h by M_h a second time. Histories of zero exact mass contribute zero.

Define the approximate algorithm's transitions on every possible history and label. At an unreplaced step, query x,y even if v_h(W)=0; if a+b>0 use the exact score, and if both rows are zero use a declared fair fallback. At a replaced step use the fair score without row queries. After an earlier replacement the approximate process need not have the exact conditional norm law and can reach such off-reference states. Its implementation must not call an exact-only interface that rejects them.

With these total kernels, telescoping or coupling until the first disagreement gives final joint-history/latent TV at most the sum of the reference-weighted layer errors. The exact norm law is used only under the reference distribution. No analogous invariant of the approximate process is assumed. Readout-only TV is no larger; in intermediate steps a signed cancellation bound on sum_z c_hz cannot replace sum_z |c_hz|.

## 2. A history-free partition certificate

The exact unconditional work marginal

    mu_i(z) = sum_(|h|=i) a_hz

satisfies mu_(i+1)=(mu_i+P_i mu_i)/2, by summing the two signs before discarding history. It is therefore the law of a classical fair preparation walk using actual P_0,...,P_(i-1), starting at label 1. It can be sampled without a row oracle or hidden order/factors. This is an exact positive-mass observer of the full instrument, not an assertion that every conditional work distribution is classical.

Freeze a finite work-label partition B_i={B_1,...,B_J}, including any catch-all remainder, before the validation and sampling randomness. Put

    p_j = mu_i(B_j),          q_j = mu_i(P_i^-1 B_j),
    F_i(B_i) = sum_j sqrt(p_j q_j).

By norm preservation, b_hz=a_h,P_i^-1z. First bound |c_hz| <= sqrt(a_hz b_hz), then apply Cauchy--Schwarz to the entire (h,z) population inside each bin:

    sum_h L_h
      <= sum_j sum_h sum_(z in B_j) sqrt(a_hz b_hz)
      <= sum_j sqrt[(sum_h sum_(z in B_j) a_hz)
                    (sum_h sum_(z in B_j) b_hz)]
       = F_i(B_i).                                            (2)

Consequently replacing the full depth i by fair scores costs at most F_i/2 in joint TV. For a fixed set I of replaced depths,

    TV(final joint law) <= min(1, (1/2) sum_(i in I) F_i).       (3)

F_i lies in [0,1]. Refining a partition cannot increase it: for each old bin, sum over refined bins sqrt(p_j q_j) <= sqrt(p_old q_old). This is a one-sided information hierarchy; it is never a proof that a finer partition becomes cheap or that its bound approaches the actual coherence rather than its norm-only upper bound.

The useful combination is direct: a certified small F_i permits a whole fair layer without constructing an approximate row field at that layer. Future exact-score layers can still require expensive exact row queries, whose histories include the sampled fair bits. Avoided local queries are not automatically avoided ancestor work in a recursive oracle.

## 3. Selecting only some histories

Let H_i be a declared predicate on measured prefixes, with exact mass alpha_i=sum_(h in H_i) M_h. It may depend on independently frozen training data. Define raw submarginals

    p_j^H = sum_(h in H_i) sum_(z in B_j) a_hz,
    q_j^H = sum_(h in H_i) sum_(z in B_j) b_hz.

Both sum to alpha_i. The exact analogue of (2) is

    sum_(h in H_i) L_h <= sum_j sqrt(p_j^H q_j^H)
                         <= min(alpha_i, F_i(B_i)).            (4)

When alpha_i>0, the first upper bound equals alpha_i times the affinity of the *conditional submarginals* p^H/alpha_i and q^H/alpha_i. In general it does not equal, and is not bounded by, alpha_i F_i(B_i). The selected histories can carry all the overlap. The preparation-walk sampler supplies mu_i, not mu_i^H or alpha_i. Estimating a selected-history certificate requires separately justified joint-history access, a proved structural domination bound, or reuse of the unconditional bound in (4). Drawing preparation paths and simply attaching an independently chosen history label is invalid.

A concrete algebraic witness to the false multiplication uses six work labels and the actual modular permutation P(w)=6w mod 7. Let T=I. In one history of mass 1/2, set rows at labels 1 and 6 to e0/2. In another history of mass 1/2, set rows at labels 2 and 3 to e0/2; all other rows vanish. Select only the first history. The singleton partition has F_all=1/2, but the selected raw coherence is 1/2; alpha F_all=1/4 is false. All rows are rational full-D rows and the permutation is a valid typed modular permutation. This is a symbolic counterexample to an inference from submarginals alone, not a claim that this raw history family was executed or occurs at a specified standard Shor prefix.

If a skip decision additionally depends on the private latent label or proposal, its weighted error has that decision indicator inside the (h,W,proposal) expectation. Equations (1)--(4) cannot silently be reused as a history-only equality. A conservative all-history/all-label upper bound remains available because the indicator is at most one; a sharper latent-dependent certificate needs its own observer derivation.

## 4. Two-bin union-event specialization

For B={A,A^c}, write p=mu_i(A) and q=mu_i(P_i^-1 A). For a preparation sample W define one Boolean event

    Bad = (W not in A) OR (P_i W in A),     r=Pr(Bad).

The two events need not be independent. If r<=d<=1/2, then p>=1-d and q<=d. The two-bin affinity obeys

    sqrt(pq)+sqrt((1-p)(1-q)) <= 2 sqrt(d(1-d)),
    whole-layer joint TV <= sqrt(d(1-d)) <= sqrt(d).           (5)

For completeness, at p>=q, the affinity decreases as p increases and increases as q increases (the endpoint cases follow continuously). Its maximum on p>=1-d, q<=d is at p=1-d,q=d. The same conclusion follows by squaring the two terms and comparing their nonnegative difference. No numerical angle parameterization is needed.

This single union event certifies both inequalities with one binomial test and can be cheaper than two simultaneous coordinate intervals. It is tight as a norm-only statement: if P swaps A and its complement, mu(A^c)=d, and paired rows are parallel with proportional masses, then r=d and equality holds in (5). A rational example uses row amplitudes 4/5 and 3/5 at two exchanged labels, giving d=9/25, L=24/25 and joint error 12/25. This is a symbolic actual-instrument algebra example, not a new propagated fixture or an ideal-QFT comparison.

For history-restricted skips, the unconditional (5) still upper-bounds their contribution, but multiplying it by alpha_i without conditional mass information is again unwarranted.

## 5. Finite statistical certificates with exact positive arithmetic

Condition on all training randomness, so partitions, membership programs, tested depths, candidate bounds, budgets and maximum test work are fixed. Use an independent sample of m preparation walks. One walk can provide observations for every depth; for each i evaluate the bin of W_i and of the actual typed P_i W_i. Across bins, p/q sides and depths the indicators can be correlated. Only independence of different validation walks is required. A union bound needs no independence between tests.

For any Boolean indicator with unknown rate theta, let K be its count among m walks. For a declared upper threshold u in [0,1], the exact one-sided test is

    accept theta<=u if F_u(K) = Pr[Bin(m,u)<=K] <= eta.

Under theta>u, monotonicity of the lower-tail CDF gives Pr[false acceptance] <= eta. More precisely, the accepted k form an initial segment and its probability under theta is no larger than its probability under u. The assertion is a joint bad-and-pass bound, not a bound conditional on passing.

Two implementable general-partition variants are:

1. Freeze upper thresholds U_ij,V_ij before validation; test each p_ij and q_ij at its threshold, with allocated error budgets summing to zeta. Accept a schedule only if all tests pass and the certified affinity sum meets its declared TV budget.
2. Freeze a rational grid before validation. For each observed count k, choose U(k) as the first grid value u with F_u(k)<=eta, or use U=1 if none exists. This is a valid upper confidence rule without an extra union bound over grid points: U(K)<theta implies F_theta(K)<=eta, whose probability is at most eta. Use this separately for p and q with simultaneous per-coordinate budgets. The tested partition family must remain fixed; picking a new partition after seeing this heldout data requires simultaneous bounds for all candidates or fresh validation with an added failure budget.

On the simultaneous valid event, compute

    F_i <= min(1, sum_j sqrt(U_ij V_ij)).

A fully rational verifier need not output an irrational square root. For each product U V, certify a nonnegative rational s with s^2>=UV and sum these s. On a denominator-2^b grid, choosing the smallest such s overestimates each root by less than 2^-b, hence the layer TV overhead is less than J/2^(b+1). Actual products, differences and certificate signs must pass through the existing typed positive-path observer (or a proved extension), with source-bound receipts. Higher precision in this *statistical bound certificate* is not a replacement for any native gate, field or target precision.

The existing source `projected_rows.py:binomial_lower_tail` provides an actual positive-path DP for the binomial CDF and is a reuse candidate; no new copy or execution is claimed here. A bounded DP truncated at observed count k has O(m(k+1)) scalar recurrence entries, at worst O(m^2) per tested coordinate. A straightforward grid-search verifier multiplies this by its tested grid candidates; a monotone binary search can reduce the number of CDF evaluations, with every compared endpoint certified. Charge exact numerator/denominator bit growth, not just recurrence-entry counts. The binomial population is a declared product of Bernoulli observations, so its positive path interpretation is appropriate. It is not being used to propagate signed quantum amplitudes.

For the two-bin union-event test at fixed d, a zero-miss certificate has false-pass bound (1-d)^m. A finite plan can choose m by exact repeated multiplication until this is at most zeta; it then draws exactly that many walks once. When the desired layer TV is epsilon, taking d<=epsilon^2 gives a conservative plan. This illustrates the potentially substantial sampling cost even if the true bad rate is zero. Positive misses can also pass the exact lower-tail test; they are not a zero-miss certificate.

## 6. Outer algorithm, failure, and cost

After one training/validation attempt, the outer algorithm selects a certified skip schedule if the bounds give (1/2) sum_i F_i<=epsilon; otherwise it runs the original totalized exact sampler. There is no unbudgeted resampling until a favorable certificate appears. All private sampling randomness is independent of training/validation.

On the simultaneous valid event the totalized skip sampler has TV<=epsilon; on its complement use the trivial TV<=1. Mixture convexity therefore gives unconditional output TV<=epsilon+zeta, provided both selected routes are continued to completion. Budget pauses must preserve the parent history, latent label and already consumed random choices. They must be resumed, or the probability of an unresolved/FAILURE output must be added to the error budget. Discarding failed or paused runs and conditioning on completion is not justified.

A concrete total-cost expression is

    C_train + C_validate + C_replay
      + Pr(pass) E[C_skip | pass]
      + Pr(fail) E[C_exact | fail],

including any additional per-run source/native admission and table setup. The expectations cannot generally be replaced by unconditional averages because the selected partition affects subsequent query cost. Charge preparation column requests (at most m sum_i i for separately generated prefixes, or m times the maximum sampled depth for shared walks), one P_i lookup per observed tested depth, membership evaluation, cache growth, binomial/root-bound work, RNG, stored evidence and later exact row queries. Training has the same types of costs. There is no implicit full-domain enumeration requirement, but neither a polynomial membership program nor a small useful partition is assumed free.

Cheap local skips may leave expensive global preprocessing or future exact row recursion. A failed certificate can be frequent, making exact fallback dominate. Without bounds on certificate success probability and both route costs, this is a correct approximation scheme with a conditional useful-cost criterion, not an efficient dequantization theorem.

## 7. Tightness and information-loss witnesses

- **Single-bin blindness.** With only the full carrier as a bin, F=1 always. Even exactly disjoint support and its P image receives only the generic layer error bound 1/2.
- **All partitions can remain blind to phase/internal geometry.** Two equal-norm rows on a swapped pair have the same mu whether they are parallel or orthogonal internal vectors. With T=I, parallel rows yield maximal coherence and orthogonal rows yield zero coherence. All work partitions see the same p,q. For rational normalized rows one can use equal amplitudes 1/2 and raw total mass 1/2, or add a disjoint raw-history block to normalize the total population. Full61 permits both cases. This shows a limitation of norm-marginal access, not a claim that an arbitrary such row family is a standard Shor prefix.
- **Exact support separation is stronger than sparsity.** If mu is supported on A and A is disjoint from P A, the two-bin certificate gives F=0 and an exact fair layer, irrespective of how many labels lie in A or how large each complete internal row is. This bypasses the explicit sparse-row L2 barrier at that layer without approximating any row.
- **Refinement can require the hard label information.** The singleton partition gives the best bound available from mu and P alone, sum_z sqrt(mu(z)mu(P^-1z)); computing or validating it may require exponentially many occupied bins. This unit does not assume support enumeration or a hidden period oracle.

The new useful statement is therefore the direct bridge (2)--(3) plus a finite confidence/fallback contract. It leaves a precise research gap: find an independently constructible cheap partition with small affinity on relevant nontrivial depths, or retain extra correlation information whose computation is cheaper than the skipped row oracle. No worldwide-priority, independence or admission claim is made.

## Sources and reading scope

The complete local sources read for this derivation were `sep27-qft-approx/observer_contracts/PROJECTIVE_AND_COHERENCE_BOUNDS.md` (direct local joint coherence formula and robust separation) and `sep27-qft-approx/structured_approx/WORK_MARGINAL_PRUNING_AND_BARRIER.md` (preparation marginal, independent holdout and explicit-label barrier), plus current GK BRC-only Markdown/JSON. General amplitude-query antecedents and literature readback are already archived in `sep27-qft-research/prior_art/PRIOR_ART_AND_BRIDGES.md`; this task reuses that packet and makes no new literature or metadata-as-fulltext assertion. All additional algebra needed above is displayed. Coauthor audit confirmed the partition/history-weight formula and the union-event specialization; this is shared-context author checking.

Global-Knowledge-Sync: main@f44ed595 / GLOBAL_KNOWLEDGE_V1
