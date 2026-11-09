# PREFIX-638-R6 — Exposed, strictly convex mean–variance arc for the signed BRC first-passage observer

Date: 2026-11-09 (Asia/Shanghai). Status: AUTHOR_DERIVED / EXACT_RATIONAL_IMPLICATION_CHECKED / UNREVIEWED / NOT_ADMITTED.
Frozen scientific input: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Role: independent TASK_RESEARCH, without a formal shared-task CLAIM.

## Model and the exact inherited premises

Continue the signed, two-information-direction BRC first-passage statistical observer of PREFIX-621/622. Let Y denote the informative unit-rate Poisson stopping time, mu(p,z)=E[Y] and W(p,z)=Var(Y). The native action-thinned variance for the two actual slots obeys Var(T_q)=q² W-q mu at q=12 and q=24. The variable t=1/q below is an analytic interpolation, not an extra physically executed sampler.

Set I=[4/25,161/1000], z*=19/128, J=[z*-2^-33,z*+2^-33], K=[1/24,1/12].
Let G(p,t,z)=W(p,z)-t mu(p,z), and c(t,z)=argmin_{p in I} G(p,t,z).
The verified predecessor statements PREFIX-635 (ec03483204af911eef75785bcdaf610d24519ab2) and PREFIX-636 (c70457fde1d39265b126976bd92126731c31c23e) supply analytic mu,W, a unique minimizer c(t,z) in the interior of I, and, for every (p,t,z) in I×K×J,

    299 < mu_p(p,z) < 311,
    22000 < G_pp(p,t,z) < 51000.

On the central slice z=z* the bounds strengthen to 300<mu_p<310 and 23000<G_pp<50000. These are explicitly inherited mathematical premises, not re-certified by the new 21-assertion rational script. The original 96-port BRC graph is not rerun.

Define m=299²/51000=89401/51000, M=311²/22000=96721/22000 and centre-slice m*=9/5, M*=961/230.

## Theorem 638.1 — Exposed strictly convex arc

For each fixed z in J, define A(t,z)=mu(c(t,z),z) and B(t,z)=W(c(t,z),z). Then A and B increase strictly in t and satisfy

    m < A_t(t,z) < M,
    t*m < B_t(t,z) < t*M.

The map A(.,z) is invertible on K. With its inverse t_z(a), write b_z(a)=B(t_z(a),z) on the interval D_z=A(K,z). It satisfies

    b_z'(a)=t_z(a),
    22000/96721 < b_z''(a) < 51000/89401.

On z=z*, 230/961 < b_z''(a) < 5/9.

For every p in I, t in K and z in J, the following supporting-line inequality holds:

    W(p,z) >= B(t,z) + t*(mu(p,z)-A(t,z)),

with equality exactly when p=c(t,z). Thus the mean–variance curve is a strictly convex exposed arc of this BRC statistical observer's feasible mean–variance locus, without changing its signed branch/provenance representation.

Proof. The first-order condition W_p(c,z)=t mu_p(c,z), coupled to G_pp>0, gives by implicit differentiation c_t=mu_p/G_pp>0. Consequently A_t=mu_p²/G_pp, so m<A_t<M. Also B_t=W_p c_t=t mu_p c_t=t A_t>0. Invert A: b_z'(a)=B_t/A_t=t_z(a) and b_z''(a)=1/A_t(t_z(a),z). Reciprocal bounds yield the asserted rational curvature inequalities; the centre-slice bounds follow similarly. Finally the optimality inequality G(p,t,z)>=G(c,t,z), strictly if p≠c by strict convexity of G on I, rearranges to the supporting-line statement. Endpoint formulas extend one-sided continuously because of uniform strict margins. QED.

## Theorem 638.2 — Uniform positive variance gap between the two actual optimal slots

Write B_12(z)=B(1/12,z) and B_24(z)=B(1/24,z), where the subscript identifies the slot at whose optimum the informative variance is measured. For all z in J,

    89401/19584000 < B_12(z)-B_24(z) < 96721/8448000.

At z=z*, a stronger pair holds:

    3/640 < B_12(z*)-B_24(z*) < 961/88320.

Proof. Since B_t=t A_t, integrate from t0=1/24 to t1=1/12 and use the strict bounds on A_t. The exact multiplier is integral_{t0}^{t1} t dt=(t1²-t0²)/2=1/384. Hence m/384 < B_12-B_24 < M/384, and the central version uses m*/384 and M*/384. QED.

The strip-wide gap is strictly between approximately 0.0045650020 and 0.0114489820, and is an informative-Poisson variance gap, distinct from the native-thinned variance q² W-q mu. The earlier PREFIX-637 (b3b03b72e33a0c51d92b160ba4e7c3f49e2c3e34) bounded the optimized mean gap, while this result supplies its variance counterpart and the exposed-arc geometry.

## Corollary — Exact quadratic tangent-gap enclosure

For a,a0 in D_z with a≠a0,

    (11000/96721)*(a-a0)²
      < b_z(a)-b_z(a0)-t_z(a0)*(a-a0)
      < (25500/89401)*(a-a0)².

At z=z* replace the two coefficients with 115/961 and 5/18. At a=a0, all three terms in the tangent gap cancel to zero. Proof: integrate the second-derivative bounds in Theorem 638.1 twice. QED.

## Provenance, verification, and next question

The companion Python standard-library Fraction certificate checks 21 exact rational equalities and strict comparisons and produces a JSON digest; its actual local execution returned ALL_CHECKS_PASS 21. It checks arithmetic implications of the exact inherited envelopes, not the prior 189-layer recurrence, and does not revalidate the frozen native 96-port graph. This work is author-derived, awaits independent mathematical review, and makes no claim of Result/Review admission.

Next test: adaptive two-variable Bernstein cells for mu_p>0, G_pp>0 and opposite signs of endpoint G_p on p in [3/20,1/6] and z in [37/256,39/256]. Each certified cell extends the exposed arc; unresolved cells guide sharper subdivision or exact rational counterexample attempts. The complete two-dimensional global maximum of native sampling variance remains the mother objective.
