# Stage369-B — exact nonlocal source-left exclusion at E=11/5000

Date: 2026-11-02, Research2 portable-author proof. Frozen scientific inputs: GLOBAL_KNOWLEDGE_V1 bf84bd7c61a2444b59b1da96be57df0e9ae47e53; Enterprise Math 2af3fc484eb11060b69e0afc1b562bcaf5ad1419; P000 V5 original blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Normative (independent) reads: global main ee4f4a43089f6458193229171df54ab238a8cf29; EM main e30691042083a8d24a92bce29f367885f33d364d. Scientific parent Stage368-B commit b553ffe42fce104eb2404652310ba176a8735859.

## Theorem

The external continuous-real Bernoulli/BRC auxiliary model retains all 16 labelled original source-word comparisons and its four independently weighted audit ports. Set B_k(z)=z^k(1-z)^(3-k), w=(1,3,3,1), m=(61,21,9,9), r_k(x,y)=[4 B_k(x)+B_k(y)]/5-m_k/160, b(x,y)=(5/32)sum_k w_k |r_k|, D3(a,z)=(1/2)sum_k w_k|B_k(a)-B_k(z)| and c(x,y)=[63 D3(1/4,x)+D3(3/4,x)+9 D3(1/4,y)+7 D3(3/4,y)]/256. The two-source cost is T(P,Q)=33/1024+c(P)+c(Q), and the budget is b(P)+b(Q)<=2 beta_star+11/5000, with beta_star=b(q_star) at the central r0=r1=0 root.

Let R=[219/1000,239/1000] x [51/100,16/25] and S=[219/1000,577/2500] x [51/100,16/25]. Stage368-B proves every feasible pair lies in R x R. We now prove: whenever P,Q in R obey that budget and either P in S or Q in S, the *feasible rational pair*

P0=(231138/1000000,555681/1000000), Q0=(237807/1000000,575694/1000000)

obeys the strict quantitative cost comparison

**T(P,Q)-T(P0,Q0) > 3/62500 = 0.000048.**

Consequently any global minimizer of the unrestricted four-real-parameter problem has **x_P>577/2500 and x_Q>577/2500**. This is a genuine nonlocal restriction beyond the Stage368-B global feasibility envelope x>=0.219; it requires no assumption that the post-audit-cusp algebraic candidate is globally optimal.

## Proof: reference feasibility

The exact rational rectangle x_star in (2310839,2310840)/10^7 and y_star in (5555086,5555091)/10^7 is reused and independently checked. In this rectangle, r1 increases with x and decreases with y, while r0 decreases in both variables. The checker verifies r1=0 crosses both vertical sides and r0 switches sign along that increasing implicit graph, hence the unique common root exists. There r2>0>r3, and sum_k w_k r_k=0, giving beta_star=(15/16)r2(q_star). B2 is increasing on (0,2/3); therefore beta_star>beta_L=(15/16)r2(2310839/10^7,5555086/10^7). Exact Fraction checks establish

b(P0)+b(Q0) = 156126870406900413/16000000000000000000
< 2 beta_L + 11/5000
= 19516461719181908801/2000000000000000000000
< 2 beta_star+11/5000,

c(P0)+c(Q0) = 16174439790495832521/256000000000000000000 < 6319/100000.

From the upper root bracket, 2 beta_star+11/5000 < 61/6250, checked with exact rationals.

## Proof: two exhaustive lower-bound covers of a continuous real domain

Put L(x,y)=c(x,y)+(6/5)b(x,y). The executed Fraction checker proves

L(x,y)>373/10000 for ALL REAL (x,y) in R;
L(x,y)>753/20000 for ALL REAL (x,y) in S.

For a closed rational box J, the exact extrema of each B_k on a coordinate interval occur at its endpoints or its sole interior critical point z=k/3. These bounds produce rigorous intervals for each r_k and all *separately labelled* 16 audit comparisons. If v is constant and [l,u] a certified interval, |v-z| has lower bound zero when l<=v<=u and min(|v-l|,|v-u|) otherwise. The positive-weight sums yield exact rational b_lower(J), c_lower(J) and L_lower(J). Thus L>=L_lower(J) for EVERY real point of J.

Starting with each complete R or S box, split into two closed dyadic halves through x if 5*(x1-x0)>=y1-y0, otherwise through y. Stop a leaf only when the exact lower bound exceeds its rational threshold. The full run closed R with 1190 splits, 1191 leaves, max depth 16; S with 112 splits, 113 leaves, max depth 18. No box remains unresolved. The reproducible 1304-leaf UTF-8 CSV has 189212 bytes, SHA256 c60855319b26ba0e842906aa9126489568b001eef5945fd24247e64369f884d9. Regenerate it from the published checker with: python REPRO_STAGE369B.py --emit CERTIFICATE_STAGE369B_1304_LEAVES.csv. An independent local long-form checker yielded the same byte-for-byte CSV. Two executions of the published compact checker had identical stdout.

## Proof: strict cost margin

If P in S and Q in R, then L(P)+L(Q)>753/20000+373/10000=1499/20000. Since b(P)+b(Q)<61/6250, subtracting lambda=6/5 times the budget gives

c(P)+c(Q)>1499/20000 - (6/5)(61/6250)=31619/500000=0.063238.

The rational reference has c(P0)+c(Q0)<6319/100000=0.06319. Therefore T(P,Q)-T(P0,Q0)>3/62500. The symmetric case Q in S is identical. A global minimizer exists because the feasible set is closed and compact, and the objective is continuous; Stage368-B restricts it to R x R. Its source x-coordinates must be strictly greater than 577/2500.

## Evidence and next question

The complete original-source Fraction checker, short equivalent published checker, executed logs and full generated CSV were locally checked; the published checker reproduces the same full certificate digest and exact leaf counts. This is PORTABLE_AUTHOR_THEOREM / EXACT_FRACTION_EXECUTED; native CLAIM/Result/independent Driver acceptance and P000/X6/three-dimensional-slice/independent-time/triadic/Cell-address transfer remain separate. Stage370-B should analyze the remaining R'=(577/2500,239/1000] x [51/100,16/25] on each source using joint budget/cost interval bounds or an exact rational counterexample; retain actual unclosed boxes rather than infer global optimality from a search.
