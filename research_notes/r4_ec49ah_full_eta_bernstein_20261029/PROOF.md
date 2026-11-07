# EC49AH — Full positive-η sharp causal support from a quadratic Bernstein certificate

2026-10-29 · AUTHOR_ANALYTIC_PROOF / EXACT_FRACTION_AND_BIGINT_PASS / UNREVIEWED / NOT_ADMITTED.

## Exact model and new theorem

Retain the EC49AG auxiliary positive P/Q model: histories w,z∈{0,1,2}, u∈{0,1}, 0≤η<1/2; t(w,u)=1/2+(2u−1)(1−w)η; P(w,u,z)=t(w,u)*(1/6 if z=w else 1/12), Q(w,u,z)=t(w,u)/9. First-stage STOP/A0/A1/B0/B1 cost 0/1/1/2/2. The observer erases w and all first-stage random seed. On each paid (c,u), it may buy S for cost 1, then see z and independently accept. Expected source-identical costs C1=43/48, C2=7/8. Put k=177/172, H=α−kβ.

**AH1. For every real 123/430≤η<1/2, the maximum H over ALL lawful real fresh-coin causal policies is**

    h(η) = 1193/16512 + (25/192)η.

The same fixed lawful X attains it: w0→A0; w1→A1; w2→(9/16)A0+(1/16)B0+(3/8)STOP; buy S at every paid observation and accept precisely the z atoms with positive P−kQ contribution. X has both exact costs.

Combining with EC49AG (immutable proof commit 80db39bb54f7cdf3e559c378501e7d61e6010663), this closes the complete **author-side** real parameter range 0≤η<1/2:

    Hmax(η) = 249/2752
       +(499/8256)[η−13/998]_+
       +(3/43)[η−1/4]_+.

## Causal upper reduction

Write first-stage paid probabilities x_wc, total B probability b, STOP mass h_STOP. C1 implies h_STOP=5/16+b; the achievable C2 implies 0≤b≤1/16. As proved in EC49AG, the first-stage polytope K has exactly 168 distinct vertices (24 with b=0; 144 with b=1/16); complete indexed enumeration has 288 entries including b=0 duplicates. At any vertex one A label is chosen for every w; all STOP mass is at one history; B mass (if any) occupies a single history and B label. Its row capacities remain slack since 5/16+2b≤7/16<1.

For each paid observation (c,u), set y_w=x_wc t(w,u), Y=Σ_w y_w, q_cu=Y/3, and

    d_cuz = Σ_w x_wc (P(w,u,z)−kQ(w,u,z))
          = y_z/12 − (4/129)Y,
    Φ_cu = Σ_z [d_cuz]_+.

The STOP or S-skipped observation has equal P/Q mass, hence optimal support rejects it since k>1. With lawful S-buy probabilities s_cu∈[0,1] shared across erased histories, every behavioral strategy obeys

    H ≤ Σ_cu s_cu Φ_cu,
    Σ_cu s_cu q_cu = C2.

For any λ≥0, the exact valid upper dual is

    H ≤ Fλ(x,η) := λC2 + Σ_cu [Φ_cu−λq_cu]_+.

For fixed η, Fλ is convex in x; thus its maximum on K is at one of the 168 vertices. The dual is only an upper bound; X supplies an independent *lawful* sharpness witness.

## One-interval variable-multiplier certificate

On the entire closed algebraic comparison interval [a,b]=[123/430,1/2], choose

    λ(η)=η/2−4/43, λ(a)=1/20, λ(b)=27/172.

For η≥1/4, h(η)=1193/16512+25η/192 is affine. Fix one first-stage vertex v. For each of the eight paid observations (c,u), a deterministic future action is either skip S or buy S and accept any of 2³=8 z masks. For any joint action choice π, define

    G_vπ(η) = λ(η)C2−h(η)
             + Σ_cu s_cu (Σ_{z∈A_cu} d_cuz(η)−λ(η)q_cu(η)).

At fixed v, d and q are affine in η, so G_vπ is an exact rational quadratic. Maximizing over π gives precisely Fλ(v,η)−h(η).

For p(η)=Aη²+Bη+C, the degree-2 Bernstein coefficients on [a,b] are

    B0(p)=p(a);
    B1(p)=Aab+B(a+b)/2+C;
    B2(p)=p(b).

For t=(η−a)/(b−a): p(η)=B0(1−t)²+2B1 t(1−t)+B2 t².

Each B_j is linear in the polynomial. Maximizing its value over *all* 9⁸ future plans factors exactly over independent observations, producing the finite expression

    M_j(v) = B_j(λC2−h)
      + Σ_cu [Σ_z [B_j(d_cuz)]_+ − B_j(λ q_cu)]_+ ,
    j=0,1,2.

The inner maxima enumerate the eight accept masks, the outer max chooses buy or skip; no shared seed or invalid prefix mixing is introduced. This is an identity for maximum **Bernstein coefficients**, not an unjustified exchange of maxima and interpolation.

Actually executed, independent exact arithmetic checkers (Python Fraction and JavaScript BigInt) prove via exhaustive 168-vertex enumeration:

    max_v M_0(v)=0,  max_v M_1(v)=0,  max_v M_2(v)=0.

Each checks 168×3=504 inequalities; equality vertex counts (20,20,168); minima (-1357/20640,-1357/41280,0). Reproducer: `node VERIFY.js`, with output `EXACT_BIGINT_REPORT.json`. An independently executed standard-library Python Fraction verifier and its complete result are included in the author evidence pack.

Thus every quadratic G_vπ has all three Bernstein coefficients ≤0 on [a,b]; the nonnegative Bernstein basis proves G_vπ(η)≤0 **for every real η in that interval**. Taking the exact maximum over future masks and then over first-stage vertices yields H≤h for every lawful real causal policy. The lawful X achieves equality. This completes AH1.

The endpoint η=1/2 is only the polynomial comparison boundary (some P/Q leaves become zero); the stated strictly-positive model uses η<1/2.

## Reuse, status and next

P000, ACTIVE worldview, native six-dimensional X6 and heartbeat time have not been modified. This is auxiliary positive-probability BRC with an explicit erased-history provenance fiber; native signed/phase BRC cancellation, true three-dimensional layers, and physical heartbeat time still require a separate typed observer-preservation bridge.

Sources: EC49AG PR #1692 at immutable 80db39bb54f7cdf3e559c378501e7d61e6010663, EC49AF PR #1691 at 39151b8632ac4ff0fe1685b092c382b9e1dbb429. Fixed normative GLOBAL_KNOWLEDGE_V1 main@22914f0903be04abde0f1c8cca91f737a31df4a8 and scientific Enterprise Math main@ba18098a824b0306c55d6feb27415aaa801be71a.

Native service 0.6.11 read returned authority_granted=false; live owner query CONTROL_QUOTA; native session_start STATIC_READONLY_SCOPE_DENIED with operation_sent=false. This is portable, unreviewed author work, not formal CLAIM/Result/review/admission.
