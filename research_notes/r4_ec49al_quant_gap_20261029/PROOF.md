# EC49AL — quantified information loss after BRC observation-label saturation

Date: 2026-10-29. Status: author-side analytic proof, exact rational author check, portable draft, UNREVIEWED / NOT_ADMITTED. This is the 18+18 strictly-positive-leaf AUXILIARY probabilistic BRC observer, not native signed/phase BRC, X6 or heartbeat physics.

## Exact theorem

For each real 0 <= eta < 1/2, fixed first-stage expected cost C1=43/48, and every feasible second-stage expected sensor cost 0 <= C2 <= 43/48, let Hmax(eta,C2) be the maximum of H=alpha-(177/172) beta over all lawful real causal behavioral strategies with erased first-stage history. Define Gap(eta,C2)=(27/172)C2-Hmax(eta,C2). Then:

    Gap(eta,C2) >= (8/43) * ((1-2eta)/(1+2eta)) * max(0,C2-25/32).

Consequently Gap is quantitatively and strictly positive at every feasible C2>25/32, for every fixed eta<1/2. At eta=3/10 the coefficient becomes 2/43; at C2=13/16 this certifies Gap>=1/688. At or below C2=25/32 the lawful EC49AK witness attains Gap=0 exactly. No sharpness claim is made for the new coefficient. Quantification is over all real behavioral probabilities, not a sampled grid.

## Original law and causal observation fiber

For w,z in {0,1,2}, u in {0,1}, set t_eta(w,u)=1/2+(2u-1)(1-w)eta and

    P(w,u,z)=t_eta(w,u)*(1/6 if z=w else 1/12);
    Q(w,u,z)=t_eta(w,u)/9.

All 18 leaves per source are positive and each source normalizes to 1. Both sources have common marginal (w,u)=t_eta(w,u)/3; sum_u t_eta(w,u)=1. First-stage law x[w,c] is row-stochastic on paid labels A0,A1,B0,B1 and STOP, with costs 1,1,2,2,0; the cost expectation is exactly 43/48. A paid action reveals label c and u, never w. Second-stage S uses a fresh independent local purchase coin r(c,u) in [0,1], revealing z only when purchased. The terminal acceptance decision depends only on observed (c,u,z), or the corresponding no-S fiber; no common remembered random seed.

For paid (c,u), let q_w=x[w,c]*t_eta(w,u)/3, T=sum_w q_w and M=max_w q_w. Under S, observed z has P-mass P_z=(T+q_z)/4 and Q-mass Q_z=T/3. Therefore

    P_z-(177/172)Q_z=(43q_z-16T)/172.

The optimal acceptance on this fiber is positive-part thresholding, yielding V(q)/172 where V(q)=sum_z [43q_z-16T]_+. No-S and STOP have identical P/Q observation mass, so accepting there contributes (1-177/172)*mass<0. Thus every lawful strategy satisfies

    H <= sum_(c,u) r(c,u) V(q_(c,u))/172,
    C2 = sum_(c,u) r(c,u) T_(c,u).

The inequality remains valid for arbitrary randomized acceptance policies.

## Lemma 1: sharp per-fiber mixing loss

For every nonnegative triple q with total T and largest entry M,

    27T - V(q) >= 32(T-M).

Proof. For T=0 immediate. At most two coefficients 43q_z-16T can be positive; three positives force T>48T/43. If zero are positive, V=0 and M>=T/3>5T/32, so 27T>=32(T-M). If one is positive, it belongs to M and 27T-V=43(T-M). If two are positive, order q as M>=N>=L: V=43(M+N)-32T=11T-43L and hence 27T-V=16T+43L. Since T=M+N+L<=2M+L, 16T<=32M+16L<=32M+43L, which is equivalent to the claim. Equality of the coefficient 32 occurs at q=(T/2,T/2,0), so it is best possible for this standalone lemma. QED.

## Lemma 2: soft single-history label capacity

For each paid c choose h_c maximizing x[w,c] over w (ties arbitrary). Write p=sum_c x[h_c,c], a=sum_w(x[w,A0]+x[w,A1]), b=sum_w(x[w,B0]+x[w,B1]), s=sum_w x[w,STOP]. The three row sums and first-stage cost imply a+b+s=3 and a+2b=43/16, so a+b=43/16-b.

Each of the two A-label maxima is at most 1; the sum of the B-label maxima is at most b; and p<=total paid mass=a+b. Therefore

    p <= min(2+b,43/16-b) <=75/32,

because the two affine expressions meet at b=11/32. The inequality applies even when every c is mixed; it does NOT infer hidden history from the observed label.

## Lemma 3: purchased minority mass

Let t_min=1/2-eta>0, t_max=1/2+eta and rho=t_min/t_max=(1-2eta)/(1+2eta).

Define the purchased NON-chosen-history mass

    N=sum_(c,u) r(c,u) sum_(w != h_c) x[w,c] t_eta(w,u)/3.

The purchased chosen-history contribution is at most

    sum_c (x[h_c,c]/3) sum_u r(c,u)t_eta(h_c,u) <= p/3 <=25/32.

Consequently C2=N+(chosen mass) gives N>=max(0,C2-25/32).

For each fiber, write q_w=x[w,c]t_eta(w,u)/3, m=T-max_w q_w and n=sum_(w != h_c)q_w. We claim m>=rho*n. If h_c maximizes q, then m=n. If another j maximizes q, x[h_c,c]>=x[j,c] and t_min<=t_eta<=t_max give q_(h_c)>=rho*q_j. Thus

    m=q_(h_c)+sum_(w not in {h_c,j})q_w
     >=rho*(q_j+sum_(w not in {h_c,j})q_w)=rho*n.

After multiplication by r(c,u)>=0 and summation:

    sum_(c,u) r(c,u)(T-max_w q_w) >= rho*max(0,C2-25/32).

## End of theorem proof

Combining the optimal-fiber objective, exact C2, Lemma 1 and Lemma 3:

    (27/172)C2 - H
      >= (32/172)sum_(c,u)r(c,u)(T-max_w q_w)
      >= (8/43)*rho*max(0,C2-25/32).

This is true for each lawful real policy, hence for Hmax. The feasible-policy set is closed and bounded, with continuous H and exact cost equalities, so its maximum exists. The EC49AK explicitly lawful independent-coin pure-label strategy attains equality (zero Gap) for C2<=25/32. No complete-policy shared-seed convexification is used. QED.

## Executed exact witness and finite verification scope

VERIFY.py (Python standard-library Fraction) generated EXACT_REPORT.json. It checked 325 finite rational triple compositions for Lemma 1, its equality case, 16 exact lawful pure-label settings spanning eta=0,1/200,3/10,49/100 and C2=0,1/2,31/40,25/32, strict source positivity and normalization (18+18 leaves), and one lawful post-cutoff mixed policy. These checks are independent sanity checks; the universal real theorem is proved by the lemmas above.

At eta=3/10 and C2=13/16, choose first-stage rows:
    w0: A0 with probability 1;
    w1: A1 with probability 1;
    w2: A0 with probability 11/16, STOP with 5/16.
Buy S with a FRESH coin r(c,u)=39/43 for every paid pair; accept after S exactly on positive coefficients 43q_z-16T>0. Exact calculation gives
    C1=43/48; C2=13/16; alpha=5239/13760; beta=13/48;
    H=351/3440; (27/172)C2-H=351/13760>=1/688.
This is a feasible illustration, NOT a claimed optimizer.

Comparison only: the inherited EC49AJ eta=3/10 exact facet at epsilon=1/16 states Hmax=293/2580, hence Gap=577/41280>=1/688. We have not independently re-proved the EC49AJ facet or promoted any of these results to mathematical admission.

## Validity and next question

The exact lower bound has positive slope for each eta<1/2, but tends to zero as eta approaches 1/2; the slope can be sharpened. The next discriminating question EC49AM is a better all-real sharp coefficient on a nonzero eta/C2 rectangle, or an exact causal counterexample to an attempted improvement. Signed/phase BRC, native X6 three-dimensional slice and heartbeat transfer require separately typed observer/provenance/future-operation preservation. Neither protected P000 nor ACTIVE worldview was altered.