# Stage378-B | Rigorous two-sided localization of the right-source Bernoulli/BRC audit cusp

Date 2026-11-02, Asia/Shanghai. Author-side proof, not yet independently reviewed or admitted.

## Exact model and scientific pins

Frozen inputs: GLOBAL bf84bd7c61a2444b59b1da96be57df0e9ae47e53; Enterprise Math 2af3fc484eb11060b69e0afc1b562bcaf5ad1419; protected P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Current behavioral context read separately: GLOBAL main@b05b335e29b3f7ff175dc6ae73b5bfa487a8a1c2, EM main@c5502908fbc8f3acfc8cfb4421fd71a9e747d809.

For k=0,1,2,3, B_k(z)=z^k(1-z)^(3-k), w=(1,3,3,1), m=(61,21,9,9), and r_k(x,y)=[4B_k(x)+B_k(y)]/5-m_k/160. Define b(x,y)=(5/32)sum_k w_k|r_k|; D(a,z)=sum_k w_k|B_k(a)-B_k(z)|/2; c(x,y)=[63D(1/4,x)+D(3/4,x)+9D(1/4,y)+7D(3/4,y)]/256. All four separate residual channels and all 16 anchor-audit comparisons retain their provenance. Minimize T(P,Q)=33/1024+c(P)+c(Q) over P,Q in [0,1]^2 subject to b(P)+b(Q)<=2beta_*+11/5000, with beta_*=b(q_*) at the inherited unique r0=r1=0 root.

## Theorem

Every global minimizer can be ordered so that P is in (577/2500,469/2000)x(11/20,14/25) and Q is in (473/2000,239/1000]x(11513/20000,2303/4000). Thus 0.57565<y_Q<0.57575. If alpha=(1+sqrt(13))/8 then |y_Q-alpha|<57/1000000.

## Budget bound and feasible reference

The inherited root is isolated in x in (231083940,231083942)/10^9 and y in (555508852,555508864)/10^9 by exact Poincare-Miranda opposing face signs. Because sum_k w_k r_k=0 and r2>0>r3 at q_*, beta_*=(15/16)r2(q_*). B2 is increasing in both variables on the root enclosure, so the verified rational face signs and corner bounds prove

2 beta_*+11/5000 < B_UP=97582683/10^10.

The exact rational reference P_ref=(23113910/10^8,55568442/10^8), Q_ref=(23780690/10^8,57569391/10^8) has b(P_ref)+b(Q_ref)<2 beta_lower+11/5000 and variable cost

C_ref=16174336378406867755705673/256000000000000000000000000.

The reference is feasible and the compact continuous optimization problem has a minimizer.

## All-real signed-support Bernstein certificate

Let lambda=97/80, L=c+lambda*b. In a closed source box, independently choose signs sr,sxa,sxb,sya,syb in {-1,0,1} at its midpoint for each k's residual and four anchor comparisons. The global identity |u|>=s*u, including across zero crossings, gives the exact lower polynomial

L(x,y) >= K + sum_k A_k B_k(x)+sum_k H_k B_k(y),
A_k=w_k[lambda sr/8-(63sxa+sxb)/512],
H_k=w_k[lambda sr/32-(9sya+7syb)/512],
K=sum_k w_k[((63sxa+9sya)B_k(1/4)+(sxb+7syb)B_k(3/4))/512-lambda m_k sr/1024].

For a cubic f on [a,b], the minimum of the four exact Bernstein-Bezier controls f(a), f(a)+(b-a)f'(a)/3, f(b)-(b-a)f'(b)/3, f(b) is a lower bound for every real z in [a,b]. Apply separately to x and y cubics. Recursive rational midpoint bisection of the longer box side produces full dyadic partitions certifying

P=[577/2500,469/2000]x[11/20,14/25]: L(P)>37536223/10^9, 637 leaves, max depth 31.
Q_LO=[473/2000,239/1000]x[1439/2500,11513/20000]: L(Q)>37476695/10^9, 57 leaves, max depth 20.
Q_HI=[473/2000,239/1000]x[2303/4000,72/125]: L(Q)>37476680/10^9, 100 leaves, max depth 25.

All 794 leaves close with strictly positive rational margins, and their binary paths exactly cover the three closed source rectangles. The full CSV certificate is 94,157 bytes, SHA256 1c7552cc6ae40cb133faee01b59b47329e4357691bb58e7198cabda2b5a826bc. The independently executed standalone exact checker accompanies this run as REPRO_STAGE378B.py; the in-PR REPRO_STAGE378B.py is a transparent adapter to previously published unchanged Stage377-B exact proof core (Git blob 9b54a83059ff965e4807577448c3828cc64e8f04), capable of regenerating/validating the same normalized CSV and digest from a repository checkout.

The dual upper comparison is C_ref+lambda B_UP=19203302858726867755705673/256000000000000000000000000. The lower-strip sum of thresholds exceeds it by 4149273132244294327/256000000000000000000000000; the upper-strip sum exceeds it by 309273132244294327/256000000000000000000000000. Both are strictly positive. For any feasible pair in either strip,

c(P)+c(Q)=L(P)+L(Q)-lambda[b(P)+b(Q)] > C_ref.

That pair therefore cannot globally minimize cost, since the reference is feasible. Stage377-B already confines Q_y to (0.5756,0.576), and the two closed strip exclusions give the theorem. The polynomial 16t^2-4t-3 is increasing for t>1/8, negative at t=575693/10^6 and positive at t=575694/10^6; hence alpha lies strictly between and |y_Q-alpha|<57/10^6.

## Validation, boundaries and next question

Actual local standard-library Fraction execution, plus deterministic certificate replay, both yielded STAGE378B_EXACT_TWO_SIDED_NEAR_CUSP_QY_PASS and the exact 794-leaf CSV hash. Source functions preserve all 16 audit labels and 4 residuals (BRC reuse, not a new native operator). No finite grid inference is used to extend the scope: every real point in the stated closed boxes is covered.

Still open: complete four-parameter optimum, exact improvement/counterexample to the inherited algebraic cusp candidate, and a native observer-preserving P000/X6 three-dimensional-slice/third-coordinate/update mapping. The current research service reports research_authority_granted=false; Owner inventory returned CONTROL_QUOTA. GitHub storage in this Draft PR is author evidence, not authenticated CLAIM or independent Driver acceptance.

Stage379-B: refine the residual near-cusp band by a joint 4D budget-cost certificate or a better feasible comparator, prioritizing y_Q<=0.57566 / y_Q>=0.57574, or produce an exact rational strict counterexample.
