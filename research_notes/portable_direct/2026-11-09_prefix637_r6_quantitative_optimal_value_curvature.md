# PREFIX-637-R6 — Quantitative strong concavity of the optimized BRC variance tradeoff

Date: 2026-11-09 (Asia/Shanghai). Researcher-ID: EM-DIRECT-7D7B87 / TASK_RESEARCH. Research-Activity-ID: RA-3962F65E02F24F4BF0E09394.
Frozen science: `f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Status: AUTHOR_DERIVED / EXACT_RATIONAL_IMPLICATION_CHECKED / UNREVIEWED / NOT_ADMITTED.

## Model and exact predecessor scope

The finite signed two-information-direction BRC first-passage statistical observer of PREFIX-621/622 has Poisson informative stopping time Y, mean mu(p,z)=E[Y], and variance W(p,z)=Var(Y). The native thinned action sampler satisfies Var(T_q)=q²(W-mu/q) for slots q=12 and 24. The continuous parameter t=1/q is an analytic interpolation, with t in [1/24,1/12].

Fix I=[4/25,161/1000], central second parameter p*=19/128 and transverse radius d=2^(-33). Define G(p,t,z)=W(p,z)-t mu(p,z), c(t,z)=argmin_{p in I} G(p,t,z), and Phi(t,z)=G(c(t,z),t,z).

Predecessor [PREFIX-635](https://github.com/awdawmip/enterprise-math/blob/ec03483204af911eef75785bcdaf610d24519ab2/research_notes/portable_direct/2026-11-09_prefix635_r6_central_slice_unique_valleys.md) supplies unique interior minimizers and, on z=p*, strict continuous envelopes 300<mu_p<310 and 23000<G_pp<50000 for the whole interval I and all t. [PREFIX-636](https://github.com/awdawmip/enterprise-math/blob/c70457fde1d39265b126976bd92126731c31c23e/research_notes/portable_direct/2026-11-09_prefix636_r6_transverse_unique_valley_stability.md) extends unique interior minimizers with 299<mu_p<311 and 22000<G_pp<51000 throughout I × [p*-d,p*+d] and all t. The current theorem takes these source-pinned certified bounds as explicit premises, without re-running the original 96-port native BRC graph or the 189-layer generator.

## Theorem: order-one, uniform optimized-value curvature

For every z in [19/128-2^-33,19/128+2^-33] and t in [1/24,1/12], Phi has a continuous second derivative in t satisfying the **strict** rational bounds

    89401/51000 < -Phi_tt(t,z) < 96721/22000.

In particular, 7/4 < -Phi_tt < 22/5 on the strip. On the fixed central slice z=19/128, the sharper inequalities are

    9/5 < -Phi_tt(t,19/128) < 961/230.

Consequently the optimal value Phi(t,z) is uniformly strongly concave in the inverse thinning parameter t with modulus at least 89401/51000, and at least 9/5 on the centre slice.

**Proof.** The defining critical point identity is G_p(c(t,z),t,z)=W_p(c,z)-t mu_p(c,z)=0. By the strict positivity of G_pp and the interior minimum, the implicit-function theorem gives c_t=mu_p(c,z)/G_pp(c,t,z). The envelope theorem gives Phi_t=-mu(c(t,z),z). Differentiating once more yields the exact identity

    Phi_tt(t,z)= -mu_p(c(t,z),z)^2 / G_pp(c(t,z),t,z).

Substituting the inherited strict bounds produces 299²/51000 < -Phi_tt < 311²/22000 on the strip, and 300²/50000 < -Phi_tt < 310²/23000 on its centre. The algebra is exact rational arithmetic. The endpoint values of t follow by the prior strict gradient margins, which allow local analytic extension. QED.

## New quantitative consequences for actual slots 12 and 24

Let t_24=1/24 and t_12=1/12. The difference in *optimal informative unit-rate Poisson mean stopping times* obeys, for every z in the stated strip,

    89401/1224000
      < mu(c(t_12,z),z)-mu(c(t_24,z),z)
      < 96721/528000.

On the central slice the bounds improve to 3/40 and 961/5520. Proof: integrate -Phi_tt between t_24 and t_12; use Phi_t=-mu(c,z) and t_12-t_24=1/24.

The exact midpoint t_m=(t_24+t_12)/2=1/16 satisfies

    Phi(t_m,z) - [Phi(t_24,z)+Phi(t_12,z)]/2
      > 89401/235008000.

At z=p* the lower bound improves to 1/2560. This follows by integrating the uniform second-derivative bound or applying strong concavity with the midpoint separation (1/24)^2/8.

These facts substantially strengthen the curvature constant from PREFIX-634 on this rigorously isolated two-parameter family and give a new quantitative optimal-mean cost gap.

## Reproducibility, status, and next question

`PREFIX637_R6_OPTIMAL_VALUE_CURVATURE_CERTIFICATE.py` uses Python standard-library Fraction to validate 18 exact rational identities and inequalities; its companion JSON gives all constants, inherited source pins, domains and proof scope. Local execution returned `ALL_CHECKS_PASS 18`. The certificate checks the new logical/arithmetic implication from PREFIX-635/636 and is not an independent rerun of their 189-layer exact interval proof. No independent mathematical review or formal RESULT/REVIEW admission is asserted.

Next: build direct two-variable Bernstein interval certificates for positive mu_p, G_pp and opposite-sign endpoint gradients over p in [3/20,1/6], z in [37/256,39/256], to advance the original global-in-interval valley uniqueness and strengthen optimized-value curvature on the larger BRC parameter family.
