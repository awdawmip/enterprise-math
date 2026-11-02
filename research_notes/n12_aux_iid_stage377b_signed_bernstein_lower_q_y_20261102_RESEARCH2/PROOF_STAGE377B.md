# Stage377-B | Exact signed-support Bernstein exclusion of Q-y lower strip

Date: 2026-11-02 (Asia/Shanghai). Status: portable author theorem, exact Fraction execution and independent certificate replay; independent review pending.

## Model and inherited inputs

Scientific inputs remain pinned to GLOBAL_KNOWLEDGE_V1 main bf84bd7c61a2444b59b1da96be57df0e9ae47e53, Enterprise Math main 2af3fc484eb11060b69e0afc1b562bcaf5ad1419 and P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. The normative snapshots actually read for this run were GLOBAL main cfffd9c4bd4c3d67261fecc00267ccc3e9517ae9 and EM main 1fc25a040ab5f5570692fd7f081e652b22f8f728. Stage376-B commit d38ae89fb3d783aa975255802ea68d24a501ff02 is the predecessor.

Let k range over 0,1,2,3. Set B_k(z)=z^k(1-z)^(3-k), w=(1,3,3,1), m=(61,21,9,9), r_k(x,y)=[4B_k(x)+B_k(y)]/5-m_k/160, b(x,y)=(5/32) sum_k w_k |r_k(x,y)|, D(a,z)=sum_k w_k |B_k(a)-B_k(z)|/2 and c(x,y)=[63D(1/4,x)+D(3/4,x)+9D(1/4,y)+7D(3/4,y)]/256. The objective is T(P,Q)=33/1024+c(P)+c(Q), minimizing over P,Q in [0,1]^2 subject to b(P)+b(Q)<=2beta_*+11/5000; beta_*=b(q_*), with q_* the unique inherited r_0=r_1=0 root. The four residual channels and sixteen separately labelled audit comparisons are retained.

## Theorem

Every global minimizer can be ordered with P in (577/2500,469/2000) x (11/20,14/25) and Q in (473/2000,239/1000] x (1439/2500,72/125). The new strict lower bound is y_Q>0.5756, strengthening Stage376-B's y_Q>0.572. More precisely, every budget-feasible real pair in the CLOSED four-dimensional region P in [577/2500,469/2000] x [11/20,14/25], Q in [473/2000,239/1000] x [143/250,1439/2500] has a variable cost gap

 c(P)+c(Q)-C_ref >= 17461273132244294327/256000000000000000000000000 >0,

relative to the following exactly feasible rational comparator.

## Sharper exact budget and comparator

An isolating rectangle of the inherited simultaneous residual zero has x_* in (231083940,231083942)/10^9 and y_* in (555508852,555508864)/10^9. On the rectangle r_0 decreases in both coordinates, r_1 increases in x and decreases in y. Four exact strict rational face inequalities checked by REPRO_STAGE377B.py permit Poincare-Miranda; inherited uniqueness identifies the root. Since sum_k w_k r_k=0 and at the root r_2>0>r_3, beta_*=(15/16)r_2(q_*). B_2 increases on this rectangle, so corner evaluations show the actual budget 2beta_*+11/5000 is strictly below B_up=97582683/10^10.

Choose P_ref=(23113910/10^8,55568442/10^8), Q_ref=(23780690/10^8,57569391/10^8). An exact Fraction calculation verifies b(P_ref)+b(Q_ref)<2beta_lower+11/5000 and

 C_ref=c(P_ref)+c(Q_ref)=16174336378406867755705673/256000000000000000000000000.

The reference is strictly feasible and compactness gives the existence of a global optimizer.

## Signed polynomial support and exact all-real interval certificate

Put lambda=97/80 and L(x,y)=c(x,y)+lambda*b(x,y). For each source rectangle choose per k five signs s_rk,s_xak,s_xbk,s_yak,s_ybk in {-1,0,1}, from the exact midpoint values of each residual or labelled anchor comparison. Because |u|>=s*u universally for every s in {-1,0,1}, including across sign changes, we obtain a valid lower polynomial for all real (x,y) in that rectangle:

 L(x,y) >= K+sum_k A_k B_k(x)+sum_k H_k B_k(y),

 A_k=w_k[lambda*s_rk/8-(63*s_xak+s_xbk)/512],
 H_k=w_k[lambda*s_rk/32-(9*s_yak+7*s_ybk)/512],
 K=sum_k w_k{[(63*s_xak+9*s_yak)B_k(1/4)+(s_xbk+7*s_ybk)B_k(3/4)]/512-lambda*m_k*s_rk/1024}.

The support splits into two univariate cubics plus a constant. For any cubic f on [a,b] its four exact Bernstein-Bezier controls are f(a), f(a)+(b-a)f'(a)/3, f(b)-(b-a)f'(b)/3 and f(b). Positivity and partition-of-unity of the Bernstein basis show f(z) is at least the minimum of these four rational values at every z in [a,b]. Applying these bounds independently to both coordinate cubics produces an exact rational lower bound for L over the WHOLE rectangle.

Starting with each of the two closed source rectangles in the theorem, bisect the longer coordinate interval at its exact rational midpoint until the bound is strictly above its target. Completed exhaustive binary covers prove

 L(P)>L_P=3753605/10^8=0.03753605,
 L(Q)>L_Q=3747692/10^8=0.03747692.

These bounds imply L(P)+L(Q)>0.07501297, which is strictly above

 C_ref+lambda*B_up=19203302858726867755705673/256000000000000000000000000.

For any feasible pair, c(P)+c(Q)=L(P)+L(Q)-lambda[b(P)+b(Q)]>=L_P+L_Q-lambda*B_up>C_ref, with the exact gap in the theorem. Stage376-B already excludes y_Q>=0.576; combining them proves the asserted narrowed necessary strip.

## Execution and reproducibility

The attached complete standard-library Fraction source REPRO_STAGE377B.py was actually executed twice for generation, with byte-identical CSV and stdout, and once separately in certificate replay mode. The result token was STAGE377B_EXACT_SIGNED_SUPPORT_BERNSTEIN_LOW_Q_STRIP_PASS. P cover: 387 leaves / 386 splits, max depth 23. Q cover: 79 leaves / 78 splits, max depth 20. Total 466 closed leaves, zero unresolved. Every leaf's exact positive lower margin is checked. Replay reconstructs each leaf from its binary path and validates exhaustive two-child branching, volume coverage and all original signed-support inequalities.

CSV SHA256: bcb2b5b8ba4f07288fc462de02ce7cb4873fce84734c1015433beac0e33338c3. Deterministically regenerate and replay:
 python REPRO_STAGE377B.py --emit CERTIFICATE_STAGE377B_SIGNED_BERNSTEIN.csv
 python REPRO_STAGE377B.py --verify CERTIFICATE_STAGE377B_SIGNED_BERNSTEIN.csv

All sixteen source-provenance labels and four residual channels are present in each lower-bound construction. The improved sign-aware cubic support permitted the new strip certificate using two 2D covers, 466 leaves, versus the preceding 4D strip's 66,246 leaves; the leaf counts pertain to different regions and are not a global complexity comparison.

## Status and continuation

The theorem concerns the frozen auxiliary Bernoulli/BRC two-source observer at the fixed budget E=11/5000. Native X6 observer-preserving correspondence and full global optimality remain open questions. GitHub actor awdawmip has repository write permission; current native Site service reports research_authority_granted=false and owner query CONTROL_QUOTA. Accordingly this is a portable author result, not an authenticated CLAIM, native Source Result or independent Driver review.

Stage378-B: isolate the algebraic audit cusp alpha=(1+sqrt(13))/8 within the now-surviving right-source y interval (0.5756,0.576), using sharper source supports or parameter-dependent lambda, and/or produce an exactly feasible rational counterexample with cost below the algebraic cusp candidate. Preserve the scientific pins and original four-channel / sixteen-label observer.
