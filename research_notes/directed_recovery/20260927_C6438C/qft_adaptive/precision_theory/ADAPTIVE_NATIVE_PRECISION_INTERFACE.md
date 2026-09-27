# Adaptive native precision with a local Gram certificate

Status: AUTHOR_SYMBOLIC_DERIVATION / SHARED_CONTEXT / NOT_ADMITTED.
Activity: RA-CAAAC604CB513AEA8BBC1DFC. No new scientific execution is reported here.
Global-Knowledge-Sync: main@06788df / GLOBAL_KNOWLEDGE_V1.

## 1. Exact question and source scope

RP1 was actually read through the GitHub connector at EM commit `3d2e729c4cce0f8df228795599266e4582be3505`, file `research_notes/HEARTBEAT_RP1_LOW_PRECISION_RIDGE_20260927.md`, blob `ce983db7cf6610c9400450f649ce189c6b2398ec`. The complete response is retained in `RP1_SOURCE_READBACK.json`.

That note reports useful bounded b8/b12 executions, while its general actual64 comparison is vacuous at b8. It keeps the 32-bit target brackets, exact evolving dyadic state, complete 61 modes and output width fixed. This note neither repeats that experiment nor upgrades it to uniform fixed-precision sufficiency. Its comparator is the **actual admitted b64 instrument with the same target brackets**, not an ideal QFT. Bank construction/admission must establish all complete native columns and inverses before use.

The earlier `MASS_WEIGHTED_APPROXIMATION_BOUND.md` at EM `951cc16cb09635fae9f93230d96030fdaa2035b3` bounds consistent approximate row oracles using exact-reference prefix weights. Here each chosen low-precision word is itself complete and exactly orthogonal. We compare two actual adaptive instruments instead. The new sufficient certificate is a local action defect on the **low-policy prefix state**; it does not require a high-precision prefix row or a complete output law. This is a state-dependent channel hybrid argument, with no literature-wide novelty claim.

All identities below are symbolic. Numerical use must bind actual typed BRC word actions, signed observers and table sources. Ordinary exact arithmetic alone is not an execution certificate. No trigonometric/reference propagation is introduced.

## 2. A path-consistent precision policy

Let h be the measured bit prefix, i=|h|, and let P_i be the same admitted work permutation in both processes. Reference feedback T_h and selected feedback S_h act on the complete real internal carrier and are orthogonal. They are applied in their recorded temporal order, without interchanging noncommuting roots. Write U_h=P_i tensor T_h and V_h=P_i tensor S_h; the two-arm Kraus maps are

    K_h,sigma = (I + sigma U_h)/2,
    L_h,sigma = (I + sigma V_h)/2,       sigma in {+1,-1}.

The identity sum_sigma K^T K = sum_sigma L^T L = I follows from orthogonality. This is the existing complete native two-H4 instrument at its boundaries, not an ideal replacement.

A precision choice may depend on N, a, i, the entire measured h, public fixed input/certificate data and a previously frozen independent policy seed. It must determine one S_h before the next measurement. Repeated queries at the same prefix must see the same words. Conditioning on a policy seed first makes this deterministic; averaging over such independent seeds is allowed.

In particular, the choice must not secretly depend on the single walker's private latent W, on a prospective next output bit, or on which work label is queried. An expensive prefix calculation may guide the choice if it is a function of h and the committed past words. Its cost is charged. Later refinement changes only future gates: replacing all past gates by a newly selected bank would define a different prefix state and invalidates a certificate for the old one.

For the low policy define the raw complete prefix rows u_h(w), their mass M_h= sum_w ||u_h(w)||^2, and covariance

    C_h = sum_w u_h(w) u_h(w)^T = Gamma_low,h(1),
    trace C_h = M_h,                  sum_(|h|=i) M_h = 1.

There is no division by history probability in C_h. Zero-mass histories have no contribution to the bound, though the implementation still needs a total action on all syntactically legal histories.

## 3. Local action certificate and global theorem

For M_h>0 put D_h=T_h-S_h and

    A_h = trace(D_h C_h D_h^T),
    a_h = A_h/M_h,                    0 <= a_h <= 4,
    ell_h = sqrt(a_h/2 - a_h^2/16),    0 <= ell_h <= 1.

**Local lemma.** On the normalized low prefix state, applying the reference instrument or the selected instrument changes the complete one-step classical/quantum output by trace distance at most ell_h.

Proof: retain sigma as an orthogonal output label, so each instrument is an isometry. The inner product of its two pure outputs on u_h/sqrt(M_h) is

    (1 + <U_h u_h,V_h u_h>/M_h)/2 = 1 - A_h/(4M_h).

Here P_i cancels from the norm/inner product because it is the same bijection; no assumption about T_h and S_h commuting is used. The pure-state trace distance is exactly sqrt(1-(1-a_h/4)^2). Measuring the label sigma can only decrease it, proving the lemma. The observed one-step bit marginal can have a smaller error; ell_h controls the complete remaining state as well.

**Adaptive theorem.** Let P_low and P_ref denote the terminal joint laws of the full measured history and work label, or any common measurement/postprocessor thereof. Then

    TV(P_low,P_ref)
       <= min(1, sum_i sum_(|h|=i) M_h ell_h)
        = min(1, E_low[sum_i ell_(H_i)]).

Proof: compare hybrids with the first i layers from the low policy and all later layers from the reference instrument. Consecutive hybrids have the identical low prefix state, whose orthogonal history blocks have raw weights M_h. Sum the local trace distances with those weights and use contractivity of the common reference suffix. Finally telescope over layers. The history-controlled reference suffix is one completely positive trace-preserving map, even when it acts differently on different histories.

This is the key distinction from a conditional-history assertion. A large normalized a_h at one rare prefix costs M_h ell_h, not ell_h alone, in the ensemble bound. Conversely, looking only at a small raw A_h and ignoring M_h is invalid. Neither a sampled path's charge nor its observed absence of large charges certifies the expectation by itself. This argument also does not justify replacing E[sum ell] with E[min(1,sum ell)]; only the final total bound is capped at one.

The theorem preserves all residual modes. A smaller carrier may be used only after verifying a common invariant subspace for **both** compared word families and the initial state. The previous direct-word six-mode codec is not automatically a codec for RP1 roots.

## 4. Deterministic precision filter: no full history law

The theorem admits a useful implementable sufficient rule. Fix a rational total budget epsilon. At each visited prefix select a rational charge e_h in [0,1] and a certified candidate S_h with ell_h<=e_h. Commit the choice only if the accumulated charge along that prefix, including e_h, is at most epsilon. Any remaining step can choose S_h=T_h, whose charge is exactly zero. Apply the same rule on every possible prefix, and preserve its ledger on pause/restart.

Every completed low trajectory then has sum e_h<=epsilon, hence the theorem gives TV<=epsilon without enumerating the history tree or estimating its probabilities. This is a correctness construction, not a guarantee that a desired coarse candidate will pass cheaply. The reference-word fallback can be expensive. Certificate failure or a budget pause is not grounds to discard a draw and condition on successful completion: resume it, use a defined complete fallback, or include failure probability explicitly.

With exact raw A_h and M_h, the exact rational admission test is

    8 A_h M_h - A_h^2 <= 16 e_h^2 M_h^2,
    M_h>0,  0<=A_h<=4 M_h.

It avoids a numerical square root or normalization. The simpler sufficient test A_h <= 2 e_h^2 M_h also works. If certified intervals are used, A_upper <= 2 e_h^2 M_lower with M_lower>0 is safe. A zero or unproved lower mass must not be divided into; decline that state-specific certificate and use a valid uniform gate bound or the exact reference word.

If an exact physical-prefix certificate gives M_h=0, positivity of C_h implies C_h=0 and A_h=0. This prefix has zero probability under the low policy. Define its total action as S_h=T_h with charge zero; do not feed M_h=A_h=0 into the polynomial inequality and call that a normalized certificate. This same reference choice is a safe total fallback when a query is incomplete, provided the sampling routine completes the reference action and preserves the committed past. A bogus negative A_h or A_h>4M_h is an invalid physical/action certificate and must be rejected before the nonlinear test, whose monotonicity would otherwise not apply.

For the special candidate S_h=I the same covariance gives

    A_h = 2 [M_h - trace(T_h C_h)].

More generally A_h=2[M_h-trace(T_h^T S_h C_h)]. These identities use the symmetry of the full C_h and orthogonality, not a marginal bit correlation at a displaced work label. They can be evaluated by the corresponding actual word/inverse action and signed trace observer. A direct-word-versus-identity execution would validate this interface; it would not reproduce RP1's b8/b64 comparison or inherit its empirical success results.

An entirely state-independent fallback certificate is ||T_h-S_h||<=d_h<=2, giving

    ell_h <= sqrt(d_h^2/2 - d_h^4/16) <= d_h/sqrt(2).

The monotonicity used here holds for squared defect in [0,4]. A conservative sum of per-root norm bounds may first be clipped at 2. RP1's bound 4(2^(-b/2)+2^(-32)) is a permissible per-root bound only with its actual common-target construction hypotheses; count level3 as two root4 actions. Its being valid does not make it nonvacuous at b8. Rational conservative charges suffice for an executable filter.

## 5. Native rank-two action observers

There is additional structure before a full feedback product is formed. For the certified forward root form R_u=D0(2u u^T-I), with real unit u and a common orthogonal sign matrix D0, compare the actual vectors u and v and write c=u^T v. Direct multiplication gives

    (R_u-R_v)^T(R_u-R_v)
       = 4[uu^T+vv^T-c(uv^T+vu^T)].

Thus on an arbitrary unnormalized covariance C, the exact squared action defect is

    4[u^T C u + v^T C v - 2c u^T C v].

Only three quadratic/bilinear covariance observations are required once the actual vectors and C are available. For |c|<1 the same expression is 4(1-c^2) trace(Pi_span{u,v} C); for |c|=1 the roots coincide. For inverse words, conjugate the input covariance by D0 as required by the transposed root formula; do not reuse the forward orientation silently.

This identity retains signs and all components of u,v, including residuals. It can improve a uniform operator bound if the state has little mass in the defect plane. It does **not** prove that the three scalar observations are easy. Pulling a low-rank observable backward through a sum of noncommuting instrument branches can grow its rank and number of terms.

For T=A_g ... A_1 and S=B_g ... B_1, the exact ordered telescoping identity is

    T-S = sum_j A_g ... A_(j+1) (A_j-B_j) B_(j-1) ... B_1.

By Minkowski on the complete row family,

    sqrt(A_h) <= sum_j sqrt(trace((A_j-B_j) C_(h,j) (A_j-B_j)^T)),
    C_(h,j) = (B_(j-1)...B_1) C_h (B_(j-1)...B_1)^T.

All prefix factors on the right are the selected actual words and all reference suffix factors have disappeared only by norm preservation. This provides a compositional certificate with native rank-two observations and no high-state propagation. It can be weaker than directly observing the complete D_h defect. No roots are commuted.

## 6. Statistical alternative and complete outer semantics

For a frozen complete policy, independent low-policy rollouts may record upper charges e_h>=ell_h in [0,1]. Put X=sum_i e_(H_i), so 0<=X<=t. The mean E X is an upper bound for terminal TV before the cap. A distribution-free elementary certificate uses m independent rollouts: Var(sample_mean X)<=t^2/(4m), hence

    Pr(E X > sample_mean X + d) <= t^2/(4m d^2).

This follows from the bounded-variable variance inequality and Chebyshev; all thresholds can be rational. Choosing m>=t^2/(4 zeta d^2) makes the failure event at most zeta. This deliberately conservative bound is implementable using native signed observers without a logarithm, but the m full sampling/certificate costs must be counted. Sharper valid concentration can be substituted with its own implementation and source contract.

Freeze the policy before validation. If the certificate passes, use that fixed low policy for a fresh output draw; otherwise use a complete actual reference sampler. Outside a bad validation event of probability at most zeta, accepted policies have TV<=epsilon. The unconditional outer output therefore has TV<=epsilon+zeta. This is a one-shot training/validation scheme; it does not assert conditional-on-acceptance confidence, permit unlimited validation retries, or allow policy tuning on the same validation set without extra control. Rejected validation work and reference fallback are part of total cost. Approximate/failed certificate generation must itself be totalized and charged.

For a fixed decoder success set G, the deterministic theorem gives

    P_low(G) >= max(0,P_ref(G)-epsilon).

It only yields a numerical useful-success lower bound if P_ref(G) has a valid lower certificate. There is no assumed known order or free ridge mask. Independently held-out verified-factor indicators can instead certify the actual policy's success rate directly, without a full output law; their sample cost, selection rule and failure budget remain necessary. A high geometric peak alone supplies neither certificate, as RP1's adverse b4 fixture demonstrates.

## 7. Cost and implementation boundary

One C_h=Gamma_low,h(1) can be reused to score multiple candidate gates at the same prefix, after paying for the candidate words and their admission. Direct matrix scoring uses bounded internal dimension, but obtaining C_h can remain expensive. Paid odd-part/alias aggregation is available only with all order/address construction, fresh replay and matrix contraction costs included. A proof that a few observables determine the certificate does not imply polynomial query cost.

The existing `GramSampler._gates` and `CarryExecutor.phase_snapshot` bind a static bank. They cannot represent a policy that retrospectively changes past precision by swapping that bank. A new adapter must bind the actual committed per-step word lists and their hashes, and have every point/Gram query consume that same immutable prefix ledger. Budget/certificate/RNG/pending-step state must survive restart. This is a concrete next implementation unit, not an already delivered adaptive sampler.

`MASS_TRACE_ORDER_REDUCTION.md` strengthens the known oracle-cost warning: even a uniform exact **scalar mass** oracle for arbitrary prefixes suffices for modular order recovery. That reduction is not a lower bound on typical histories or on approximate certificates. The positive route left open here is cheap certificates on the histories actually reached, or a conservative precision filter whose certification costs less than the expensive operations it avoids.

It also does not rule out a cheap normalized defect ratio that avoids computing the raw mass: for example, if D_h^T D_h is a known scalar on a proved reachable subspace, a_h is that scalar for every state in the subspace. Such an algebraic identity must be certified for the actual word family; it cannot be inferred from a low-dimensional output alone.

## 8. Explicit counterexamples and limits

1. **Raw mass is not conditional precision.** On a prefix of mass alpha, let P=I, reference T=I and candidate S=-I on the populated direction. Then A=4 alpha can be arbitrarily small, but the next reference bit is certainly plus and the candidate bit certainly minus. The conditional TV is one; the layer's weighted cost is alpha. This is a symbolic complete orthogonal-instrument example, not a claim that a particular RP1 bank realizes it.
2. **A local action certificate is sufficient, not necessary.** Let a populated label w and P(w) be distinct, T=I and S=-I on its internal direction. The local coherent bound is ell=1, yet the immediate measured joint bit/work law is identical (each of its four atoms has probability 1/4). Future interference can distinguish the retained phase, which is why this one-step coincidence does not justify dropping full-state error in a general history.
3. **One passing path is not a distribution certificate.** A policy can have zero charge on a common prefix and charge one on an unobserved branch of positive mass. Checking only the realized common path neither establishes a pathwise filter rule for other histories nor estimates the missing expectation with zero failure probability.
4. **Private latent adaptation changes the model.** Choosing different candidate words after observing the single walker's private W need not define one linear instrument on u_h. The theorem then has no S_h or C_h to which it applies. The earlier row-oracle sign-flip counterexample likewise prevents treating independently query-dependent approximations as one coherent prefix.

No general fixed8-bit success, polynomial Gram algorithm, universal simulator speedup, independent review/admission, or new ideal reference execution is claimed. The local-isometry formula and the low-prefix hybrid weighting were cross-checked symbolically by another shared-context author.
