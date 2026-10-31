# BRC N=4: sharp full-joint P/Q TV interval at fixed noise and branch distance

Date: 2026-10-30. Author-side mathematical proof; finite exact Fraction check. **UNREVIEWED / NOT_ADMITTED**. Scientific continuation of PR #1738 author commit a52545bbc2520f385eb0d698c7e3d6d0fb2af7e0, specifically its open question of exact (epsilon,D)-fixed full joint-TV bounds.

## Exact finite model

For s=AU,AV,BU,BV and j,k=0,1, Q(s,j,k)=q_s/4, P(s,j,k)=q_s r_sj/4; q=(1/6,1/3,1/4,1/4), r_AU=(9/10,11/10), r_AV=(1/4,1/4), r_BU=(1/5,9/5), r_BV=(2,2). Both are normalized with all 16 masses strictly positive. Coarse C=E,A,B has identical P/Q masses (7/12,1/6,1/4). Conditional on BU, P(J=0)=1/10 and Q(J=0)=1/2. Z=J XOR Bernoulli(epsilon), common independent sensor, epsilon in [0,1/2]. Outside BU, Z=NA and joint output is identical.

In BU branch j a lawful behavioral S2 policy continues from stage 3 to stage 4 at rate u_j (u_0=u,u_1=v), otherwise emits B3. If it continues it reads the actual fair terminal bit K, does not change K, and chooses terminal decision P with rate d_jk, Q otherwise. Future conditional kernel F_j on Y=(B3,B4P0,B4Q0,B4P1,B4Q1) is
F_j(B3)=1-u_j, F_j(B4Pk)=u_j d_jk/2, F_j(B4Qk)=u_j(1-d_jk)/2.
All six behavioral parameters lie in [0,1]; S23 further imposes d_j0=d_j1 per j. D:=TV(F0,F1) and t:=1-2epsilon.

## THEOREM — the complete sharp range, all real parameters

For every fixed epsilon∈[0,1/2], D∈[0,1], over **lawful S2**, or already the smaller **lawful S23** policies with TV(F0,F1)=D, the set of possible FULL between-law TV distances T=TV(P_(C,Z,Y),Q_(C,Z,Y)) is the entire interval

    max(D,t)/10 <= T <= [D+t(1-D)]/10,  t=1-2epsilon.       (1)

This is not a minimax decoder reconstruction error, not the marginal (C,Y) TV, and not a native P000 physical claim.

### Proof: atomwise exact positive-weight BRC readout

The signed joint differences on BU are
(P-Q)(B,Z=0,Y=y)=-[(1-epsilon)F0(y)-epsilon F1(y)]/10
and
(P-Q)(B,Z=1,Y=y)=-[epsilon F0(y)-(1-epsilon)F1(y)]/10,
because (1/4)(1/10-1/2)=-1/10. C=E,A contributions cancel. Hence
T=(1/20) sum_y (|(1-epsilon)F0-epsilon F1|+|epsilon F0-(1-epsilon)F1|).
For nonnegative a=F0(y),b=F1(y), the identity
(|b-a+t(a+b)|+|b-a-t(a+b)|)/2=max(|b-a|,t(a+b))
gives the exact formula

    T=(1/20) sum_y max( |F1(y)-F0(y)|, t[F0(y)+F1(y)] ).     (2)

Writing x_y=|F1-F0|, s_y=F0+F1, m_y=min(F0,F1), we have s_y=x_y+2m_y, sum x_y=2D, sum s_y=2, sum m_y=1-D. Therefore sum max(x_y,t s_y)>=max(2D,2t), proving the lower bound. Since 0<=t<=1, max(x_y,t(x_y+2m_y))<=x_y+2t m_y. Summing gives the upper bound 20T<=2D+2t(1-D), for every finite terminal alphabet and every real admissible parameter.

### Explicit lawful S23 lower endpoint

Set u=(1-D)/2, v=(1+D)/2, all d_jk=0 (terminal Q only). At B3 the two branch masses are (1+D)/2 and (1-D)/2; each B4Qk has masses (1-D)/4 and (1+D)/4. At every positive atom |F1-F0|=D(F0+F1). Thus TV(F0,F1)=D and (2) gives T=max(D,t)/10.

### Explicit lawful S23 upper endpoint

Set u=v=D, d00=d01=1, d10=d11=0. B3 has common F0=F1=1-D; F0's continued mass D lies in P-labeled K atoms, F1's mass D lies in disjoint Q-labeled K atoms. The common support contributes 2t(1-D) to the sum in (2), the disjoint output contributes 2D. Hence TV(F0,F1)=D and T=[D+t(1-D)]/10. These are S23 decisions (d_j0=d_j1) and change no physical K; when D=0 the unreachable decision parameters do not matter.

### All intermediate values and no gaps

For lambda∈[0,1] take F_j^lambda=(1-lambda)F_j^lower+lambda F_j^upper. It is implemented by S23 using
u_lambda=(1-lambda)(1-D)/2+lambda D,
v_lambda=(1-lambda)(1+D)/2+lambda D,
d_0k=lambda D/u_lambda if u_lambda>0, otherwise 0; d_1k=0 for k=0,1.
The difference F0^lambda-F1^lambda has positive B3 mass (1-lambda)D and positive B4P mass lambda D, balanced by negative B4Q mass D. Thus its TV is exactly D at every lambda. Formula (2) is continuous in lambda, attains both endpoints, and by the intermediate value theorem attains every intervening T. QED.

## Concrete witness and scientific meaning

At epsilon=1/4, D=1/2 the sharp interval is [1/20, 3/40]. Earlier valid u=0,v=1/2, all-Q gives T=1/16, a strict interior point. The new lawful upper construction u=v=1/2, source-dependent P vs Q terminal decisions gives 3/40. At epsilon=0 the interval collapses to 1/10 regardless of D; at epsilon=1/2 it collapses to D/10. At D=0, joint P/Q distance can remain t/10 entirely because Z still reveals different hidden-source priors. This is consistent with zero *reconstruction deficiency* at D=0, which is a distinct quantity.

## Verification and scientific limits

Executed local Python Fraction code (see VERIFY.py for the compact reproducible exact checker and accompanying RUN_EVIDENCE.txt) reconstructed 16 strictly positive normalized leaves, checked equal coarse P/Q masses, direct full-joint pushforwards and (2), 1125 S23 rational profiles, 2187 full S2 profiles, and 125 constant-D interpolation tests. Continuous claims follow from the exact derivation, not finite-grid extrapolation.

Frozen GLOBAL_KNOWLEDGE_V1 main@2a62d4bc3e5188d71a51f2b832fd0a94950a03df; Enterprise Math initial control main@902ddf2a69c5b369e19d961751af144c7d94072e; original P000 Git blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc matched its projection. Positive-weight BRC and retained branch provenance were used. Native Heartbeat X6 Cell/three-axis-slice/separately typed time observer-safe bridge remains unproved. Native Site status 2026-10-30: research_authority_granted=false and active quota 5/5, so no current native owner/CLAIM/Result/independent review is claimed.
