# S23/AV: six exact plateaux and five capacity jumps, h <= 2282517

Date: 2026-11-08 Asia/Shanghai. Status: AUTHOR_SIDE_ANALYTIC_THEOREM, exact-rational verification; independent review pending.
Frozen science: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Predecessors: scaled-gap first-entry law, research_notes/brc_s23_av_scaled_gap_sturmian_jumps_20261108_research1/PROOF.md, and exact N(510), research_notes/brc_s23_av_unimodular_first_entry_20261108_r1/FULL_SATURATION.md, both at immutable commit 85b53d06d6ba775e516c566c1d79828b6ca9bb1f.

## Exact theorem

For the two-point iid S23/AV likelihood-sign observer with labels (1,3,4) having P0=(1/2,1/4,1/4), P1=(5/7,1/4,1/28), the prefix ratio with joint label-1/label-4 counts (k,ell) is 7^(k+ell)/10^k; label 3 allows padding. Let T_h={10^i/7^s:0<=i<=s<=h}, and N(h) be the least common padded prefix length hitting every open likelihood-ratio threshold cell. Then the following six equalities are exact for ALL integers in each indicated range.

| Horizon h | N(h) |
| --- | ---: |
| 510 to 380805 | 2455069 |
| 380806 to 761179 | 4530352 |
| 761180 to 1141474 | 6605047 |
| 1141475 to 1521848 | 8680331 |
| 1521849 to 1902143 | 10755026 |
| 1902144 to 2282517 | 12830310 |

This proves the first five strict change points and adds >2.26 million horizons to the original exact h=510 base theorem. It replaces O(h^2) threshold enumeration with one unimodular spacing certificate comprising twelve integer cases, plus seven translated witnesses per plateau.

## Reflected-log coordinates, previous lower theorem

Set r=ln7/ln(10/7), eps=79r-431, eta=11r-60, gamma=eta-eps=371-68r, d=2074774-380295r, and alpha=d/eps. For (v,j)>=0, v+j<=h, define t(v,j)=rv-j. An attainable prefix value is E(k,ell)=k-r ell. One full threshold cell is an interval between consecutive t values.

Let U=(79,431), W=(11,60). They form a unimodular basis with determinant -1, and any displacement (dv,dj)=aU+bW has reflected size x=a eps+b eta. In particular, b=79x-eps dv is an integer.

For i=1,..,6 set a_i=floor(i alpha), V_i=380295i+79a_i, K_i=2074774i+431a_i, and delta_i=K_i-rV_i=i d-a_i eps. The exact verifier establishes 0<delta_i<eps and the rows:

 i | a_i | V_i | K_i | M_i | H_i=V_i+510
 1 | 0 | 380295 | 2074774 | 2455069 | 380805
 2 | 1 | 760669 | 4149979 | 4530352 | 761179
 3 | 1 | 1140964 | 6224753 | 6605047 | 1141474
 4 | 2 | 1521338 | 8299958 | 8680331 | 1521848
 5 | 2 | 1901633 | 10374732 | 10755026 | 1902143
 6 | 3 | 2282007 | 12449937 | 12830310 | 2282517

Here M_1=K_1+V_1 and M_i=K_i+V_i-(V_(i-1)+1) for i>=2. The earlier determinant-one scaled-gap first-entry theorem says the particular adjacent cell J_t=(10^431/7^(510+t),1/7^t) is first occupied at length K_i+V_i-t when V_(i-1)<t<=V_i. At the left boundary h=V_(i-1)+511, t=V_(i-1)+1, it gives N(h)>=M_i. The base exact result N(510)=M_1 is already proved. Threshold inclusion T_h subset T_(h+1) makes N monotone, carrying each lower bound throughout its proposed plateau. We prove matching endpoint upper bounds below.

## Lemma 1: global exact spacing >=eps through H*=2282517

The 45-term rational atanh expansions for ln2, ln(5/4), ln(8/7) with strict explicit tails give

 Q=10^26; LO=545569623581288298975349314; HI=LO+1,
 LO/Q<r<HI/Q.

The attached Fraction verifier checks epsilon*H*<7, epsilon*(H*+79)<7, eta>4800epsilon and gamma>6epsilon.

Suppose p,q in the integer triangle D_H for H<=H* have 0<x=t(q)-t(p)<epsilon. Then b=79x-epsilon dv is an integer in (-7,7), i.e. b in {-6,...,6}. If b=0, then x=a epsilon with integer a>=1, contradiction.

For each nonzero b in that set the strip 0<a epsilon+b eta<epsilon forces precisely one integer a, namely -floor(b eta/epsilon) for b>0 or floor((-b) eta/epsilon)+1 for b<0. The rational verifier checks all these floors and all strict inequalities. A displacement (dv,dj) is embeddable in D_H iff H>=C(dv,dj), where

 C=max(max(dv,0)+max(dj,0), max(-dv,0)+max(-dj,0)).

All 12 candidate displacements have C>=2455069>H*; the unique minimum among them is b=1, a=-4814, (dv,dj)=(-380295,-2074774), with C=2455069. Therefore no distinct threshold points in D_H have positive t-distance <epsilon for H<=H*. Hence every actual bounded threshold interval is at least epsilon wide. The certificate has 12 candidate rows, rather than trillions of threshold comparisons.

## Lemma 2: narrow high-v gaps are excluded

Fix i<=6 and H<=H_i=V_i+510. If an interval's left threshold is p=(v,j) with v>V_i, then j<=H-v<=509. Suppose its next threshold q has t-distance 0<x<gamma. The integer b=79x-epsilon dv satisfies -7<b<8 by the verified bound 79gamma+epsilon H*<8. Handle b in {-6,...,7}:

b=0 implies a>=1 and q.v+q.j=(v+j)+510a>H, impossible.
b=1 implies a<=-2 since x=a epsilon+eta<gamma=eta-epsilon; then dj=431a+60<=-802, while p.j<=509, impossible.
b>=2 implies a<-(b-1)*eta/epsilon-1<-4800(b-1)-1. Thus dj=431a+60b is negative with magnitude >509, impossible since p.j<=509.
b<=-1 implies a>4800(-b), so dv+dj=510a+71b >2448439>H*, impossible since q.v+q.j<=H.

Therefore every outgoing bounded interval from high-v p is at least gamma wide.

## Lemma 3: translated witness cover of each H_i endpoint

For a bounded interval with left endpoint p=(v,j), an integer pair (K,L) with K>=j, L>=v, and 0<K-rL<the interval width produces legal counts (k,ell)=(K-j,L-v), with length K+L-(v+j). It lies strictly inside the cell.

For v<=V_i, let s be the least index <=i with v<=V_s. The primary witness (K_s,V_s) has offset delta_s in (0,epsilon), and Lemma 1 certifies it is strictly inside the interval. Its length is <=M_s<=M_i. K_s>=j because K_s>H* for s>=2; for s=1 and i<=5 we have j<=H_i<=1902143<K_1=2074774.

At the sixth endpoint H_6=2282517, the s=1 witness can have negative k when j>K_1. In that case select the SIXTH witness instead. Here v<=V_1<V_6 and K_6>H*, and

 K_6+V_6-(v+j) <=K_6+V_6-(K_1+1)
                   =12657169 <M_6=12830310.

Its delta_6 is in (0,epsilon), so the same interval is covered.

For v>V_i, choose the least m in {1,2,3,4,5,6} such that v<=V_i+68+79m; this is always possible because m=6 reaches V_i+542>H_i. Define the auxiliary witness

 L=V_i+68+79m, K=K_i+371+431m,
 K-rL=delta_i+gamma-m epsilon.

Since 0<delta_i<epsilon and gamma>6epsilon, the offset is strictly between 0 and gamma. By Lemma 2 it belongs inside the next interval. Both counts are nonnegative (j<=509<K; v<=L). Its length is bounded by

 K+L-(v+j) <=K_i+439+510m <= K_i+3499,

more sharply using v>=V_i+1:

 K+L-(v+j) <=K_i+3498 <=M_i.

The final inequality is verified for all six i.

For the exterior left interval below -H take prefix (0, floor(H/r)+1), and for the exterior right interval above rH take (floor(rH)+1,0). Exact rational inequalities verify their strict positions and lengths <=M_i at every endpoint H_i; the required length for smaller H is no greater.

Thus every open cell at H_i has an attainable prefix of length <=M_i. Pad with label 3 to the common length M_i. Together with the scaled-gap lower bound at the left endpoint and N monotonicity, this proves each exact plateau in the theorem. QED.

## Evidence and boundaries

VERIFY_STAIRCASE6.py performs exact Fraction log enclosures, all twelve admissible sub-epsilon lattice cases, six scaled witnesses, thirty-six strict auxiliary-offset inequalities, sixth-plateau large-j repair and twelve outer endpoint inequalities. RUN_STAIRCASE6.txt is actual executed stdout, ending in PASS_S23_AV_SIX_ANALYTIC_PLATEAUX_AND_FIVE_EXACT_JUMPS. The finite script certifies arithmetic bounds and the finite possible exceptions; the proof supplies quantified geometric coverage, not numerical extrapolation.

This is the joint-count BRC observer for the declared two-point statistical experiment with label-3 padding and future likelihood-sign readouts. P000 and ACTIVE Heartbeat X6 ontology remain unchanged; full-lawful delta4 and the six-source/ten-label mother-model mapping remain separate tasks. Publication is an author-side Draft PR checkpoint, independent review/native task authority pending.

Next: establish exact N(2282518) from the next scaled-gap first entry; after h=2455069 new attainable sub-epsilon displacements may demand a second basis or refined offset coverage.
