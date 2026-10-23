# Four-label auxiliary BRC: all-round, all-parameter single-pulse growth and global threshold uniqueness

**Status:** unreviewed author-side derivation, not an accepted theorem or formal Task Result. **Scope:** nonadaptive four-label positive-mass occupancy observer; not native X6 dynamics. **Date:** 2026-10-23.

**Provenance and pins:** GLOBAL_KNOWLEDGE_V1 `main@c0063368858bfea93f5bda62c8f43039d03a1f0e`; Enterprise Math `main@af1ac6a8dc1f960a84449366b5ae9cafbae6b7d8`. Continuation of the N30 author-side proof in the same ChatGPT research conversation. Native control dispatch and inventory returned `CONTROL_QUOTA`; session_start returned `STATIC_READONLY_SCOPE_DENIED` with `operation_sent=false`. No native owner, Researcher, CLAIM, Review or admission is asserted. Full manuscript, exact rational checker and output log are retained in the research conversation's N31 local evidence bundle.

## Definition

Let U={0,1,2,3}, z in [0,1]. Each independent hidden label X_t has distribution q_(p_t)/3, where

`q_0=(0,1+z,1-z,1), q_1=(1,0,1,1), q_2=(1,1,0,1), q_3=(1,1,1,0)`.

Let D_t be the set of observed labels by time t, G={{0,1},{1,2},{1,3},{2,3}}, δ_t=P(D_t in G), δ_0=0. Define Δ_t=δ_t−δ_(t−1), M_t=max_{0≤s≤t}δ_s and R_t=sum_{s=2..t}[Δ_s]_+−M_t. Fix a nonadaptive single-pulse word p^(n,k)=0^(k−1) 2 0^(n−k), with integers n≥k≥4.

## Theorem A: exact occupancy probability for all n,k,z

Put a=(1+z)/3, b=(1−z)/3, c=1/3. For 1≤t<k,

`δ_t=(a+b)^t+(a+c)^t+(b+c)^t−2(a^t+b^t+c^t)`.

For k≤t≤n,

`δ_t=((a+b)^(t−1)+2(a+c)^(t−1)+(b+c)^(t−1)−a^(t−1)−2c^(t−1))/3`.

**Proof.** Before the pulse, only labels 1,2,3 are possible, so inclusion–exclusion over the three allowed two-element sets gives the first formula. After the pulse, the t−1 action-0 outputs are independent with masses (a,b,c). The pulse output is one of 0,1,3 with probability 1/3 each. For output 0, success requires all others to be 1, probability a^(t−1). For output 1, success probability is (a+b)^(t−1)+(a+c)^(t−1)−2a^(t−1). For output 3, success probability is (a+c)^(t−1)+(b+c)^(t−1)−2c^(t−1). Averaging gives the second expression. Therefore post-pulse δ_t is independent of the pulse location k.

## Theorem B: peak freezing throughout the entire parameter interval

For all k≥4 and t≥k,

`δ_3=2/3; δ_t≤2/3−3^(−t)<2/3; M_t=M_(k−1)`.

**Proof.** Formula A with t=3 gives δ_3=3(ab+ac+bc−3abc). Since a+b=2/3, c=1/3, it simplifies to 2/3. For t≥k, condition on *any* realized set of the t−1 action-0 outputs (a nonempty subset of {1,2,3}). Of the three equiprobable pulse outcomes {0,1,3}, at most two can produce one of the four good two-label sets. On the positive-probability event that all action-0 outputs equal 3 (probability 3^(−(t−1))), only pulse outcome 1 succeeds, so the conditional success probability there is 1/3 rather than the generic bound 2/3. Therefore δ_t≤2/3−(1/3)3^(−(t−1))=2/3−3^(−t). Since M_(k−1)≥δ_3=2/3, post-pulse values never update the historical maximum.

## Theorem C: exact residual growth for ALL n>k≥4, ALL z in [0,1]

Define
`Z_n(z)=4−2^(n−2)−2(1−z)(2+z)^(n−2)−(1+z)(2−z)^(n−2)+(2−z)(1+z)^(n−2)`.

Then

`Δ_n=Z_n(z)/3^n`, and **`R_n−R_(n−1)=[Z_n(z)]_+/3^n`**.

**Proof.** Theorem A yields δ_t=P_t/3^t for t≥k, with
`P_t=2^(t−1)+2(2+z)^(t−1)+(2−z)^(t−1)−(1+z)^(t−1)−2`.
For n>k, 3^nΔ_n=P_n−3P_(n−1)=Z_n. By definition, R_n−R_(n−1)=[Δ_n]_+−(M_n−M_(n−1)); Theorem B kills the last term. This identity applies to post-pulse rounds only, not necessarily the pulse round t=k, and makes no assertion about arbitrary non-single-pulse words.

## Theorem D: unique positive root of Z_n for every n≥4

For every integer n≥4, the polynomial Z_n has exactly one positive real root θ_n. It is simple and belongs to (0,1); hence Z_n(z)>0 precisely when z>θ_n within [0,1].

**Proof.** Write m=n−2≥2 and Z_(m+2)=sum_{j=0..m+1} A_(m,j) z^j. Direct binomial expansion gives A_(m,0)=6−4·2^m<0, A_(m,m+1)=1+(−1)^(m+1) in {0,2}, and, for 1≤j≤m,

`A_(m,j)=(2+(−1)^j)2^(m−j)(2·C(m,j−1)−C(m,j))+2·C(m,j)−C(m,j−1)`.

For m≥4 let r=C(m,j−1)/C(m,j)=j/(m+1−j), and H=(2+(−1)^j)2^(m−j)≥1. Then
`A_(m,j)/C(m,j)=H(2r−1)+2−r`.
When 3j≥m+1, r≥1/2, so this is ≥(2r−1)+(2−r)=r+1>0. Otherwise put d=m+1−3j≥1. Then (2−r)/(1−2r)=1+(m+1)/d≤m+2, whereas H≥2^(m−j)≥2^ceil(2m/3)>m+2. The last strict bound holds for m=4,5,6 (8>6,16>7,16>8), and increasing m by three multiplies the left side by four while increasing the right side by only three. Thus A_(m,j)<0 when 3j<m+1 and A_(m,j)>0 when 3j≥m+1, 1≤j≤m. With the nonnegative highest coefficient and negative constant, the coefficients in descending order have exactly one sign change. For m=2,3 check Z_4=9z²+3z−10 and Z_5=2z⁴+4z³+21z²+z−26; likewise one sign change. Descartes' rule bounds the positive-root count by one including multiplicity. Since Z_n(0)=6−4·2^(n−2)<0 and Z_n(1)=2>0, a positive root exists in (0,1). Therefore it is unique and simple.

## New exact N31 threshold and verification

By exact rational bisection on a 45-decimal-place grid:

`0.999999999999985429962090489914281751655992293 < θ_31 < 0.999999999999985429962090489914281751655992294`.

A Python-stdlib-only author checker recomputed 4,272 polynomial coefficients for m=2..90 and their asserted signs, 960 independent 16-state rational dynamic-programming trials across z={0,1/7,1/3,1/2,7/10,9/10,999/1000,1} and n=4..18,k=4..n, including 12,800 occupancy prefix equations, 5,440 peak freezes, 4,480 exact residual increments and twelve 45-digit rational root brackets. All finite checks passed; they do not replace the written all-n proof nor constitute independent review.

## Scope and next research unit

No full n=31 classification was performed and no L_min≥32 follows here. The live open unit is a **uniform negative-last-increment criterion for non-single-pulse count classes across all n**, with explicit handling of historical order. A second unit is monotonicity of θ_n and one-sided lifespan of post-pulse gains. The bridge from this auxiliary positive-mass observer to native P000 X6 remains unproved.

**Receipt classification:** unreviewed research note on a separate branch; not a canonical result or research-task claim.
