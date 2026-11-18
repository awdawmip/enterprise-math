# S23/AV seventh plateau: localized repair of sub-epsilon gaps

Date: 2026-11-08 (Asia/Shanghai). **Status: author-side analytic proof with exact rational certificate; independent mathematical review pending.**

Frozen scientific pin: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.

Predecessors: six-plateau result at immutable commit 68e2442c77dbff0dea61970641c05d86a51e32a7 (research_notes/brc_s23_av_six_plateaux_20261108_research1/PROOF.md), and scaled-gap first-entry theorem at 85b53d06d6ba775e516c566c1d79828b6ca9bb1f (research_notes/brc_s23_av_scaled_gap_sturmian_jumps_20261108_research1/PROOF.md).

## Exact theorem

In the two-point iid S23/AV auxiliary sign observer, the one-step laws on ordered labels (1,3,4) are P0=(1/2,1/4,1/4), P1=(5/7,1/4,1/28). Joint prefix counts of labels 1 and 4 are (k,ell); label 3 is neutral and pads to a common length. Let T_h={10^i/7^s : integers 0<=i<=s<=h}. Define N(h) as the smallest common padded prefix length that supplies an attainable likelihood ratio in every open cell of T_h, including the two outer cells.

**For all integers 2,282,518 <= h <= 2,662,891, N(h)=14,905,515.**

The first six plateaux had been established through h=2,282,517. The old global epsilon-spacing statement becomes false beyond h=2,455,068. We introduce a localized two-scale spacing certificate to establish the seventh plateau.

## Coordinates and exact enclosure

Set r=ln(7)/ln(10/7), epsilon=79r-431, eta=11r-60, gamma=eta-epsilon=371-68r and d=2074774-380295r. In the integer triangle D_h={(v,j):v>=0,j>=0,v+j<=h}, let t(v,j)=rv-j, and for a prefix define E(k,ell)=k-r*ell. A prefix lies in the cell after left endpoint p=(v,j) with next endpoint q iff 0<E(k,ell)-t(p)<t(q)-t(p).

The unimodular basis U=(79,431), W=(11,60) has determinant -1. Every difference (dv,dj)=q-p=aU+bW has reflected width x=a*epsilon+b*eta and the **integer identity** b=79x-epsilon*dv. Its minimal triangle size is

C(dv,dj)=max(max(dv,0)+max(dj,0), max(-dv,0)+max(-dj,0)).

A difference between two points of D_H requires C<=H.

The 45-term exact rational logarithm enclosures in VERIFY7.py prove LO/Q<r<HI/Q, for Q=10^26, LO=545569623581288298975349314 and HI=LO+1. They certify 0<d<epsilon, eta>4800epsilon, gamma>6epsilon, epsilon*(H+79)<8, and 79gamma+epsilon*H<9, with H=2662891. All integer comparisons use adverse interval endpoints; no floating decision is made.

## Lemma A: global narrow-gap classification

Let p,q be distinct points in D_H and 0<x=t(q)-t(p)<epsilon. Since |dv|<=H, the integer b=79x-epsilon*dv belongs to {-7,-6,...,7}. b=0 forces a>=1 and x>=epsilon, impossible. For each nonzero b, the interval 0<a epsilon+b eta<epsilon contains at most one integer a. The exact rational floors and the triangle-size checks exhaust all 14 candidates.

Exactly two positive sub-epsilon displacement types fit in D_H:

| b | a | (dv,dj) | C | width |
| ---: | ---: | --- | ---: | --- |
| -1 | 4815 | (380374,2075205) | 2455579 | epsilon-d |
| 1 | -4814 | (-380295,-2074774) | 2455069 | d |

Both widths are strictly greater than delta4=K4-r V4, with (V4,K4)=(1521338,8299958). All other distinct-point separations are >=epsilon, and delta4<epsilon. Hence **every positive gap in D_H is strictly larger than delta4**.

There is a stronger local conclusion. If the left endpoint has v>V4, its j<=H-(V4+1)<2074774, excluding the b=1 displacement (requiring j>=2074774). The b=-1 displacement would increase v+j by 2455579, requiring v+j<=H-2455579<V4+1, also impossible. Thus **every outgoing gap from left v>V4 has width at least epsilon**.

These two verified facts replace the six-plateau theorem's former global epsilon-spacing hypothesis.

## Lemma B: translated prefix witnesses for v<=V7

For integer i>=1 define a_i=floor(i*d/epsilon), V_i=380295*i+79*a_i, K_i=2074774*i+431*a_i, delta_i=K_i-r V_i. The exact verifier proves a_1,...,a_7=(0,1,1,2,2,3,4) and 0<delta_i<epsilon.

A witness (K,L) for left threshold (v,j) gives (k,ell)=(K-j,L-v), with offset E(k,ell)-t(v,j)=K-rL and length k+ell=K+L-v-j. Thus it suffices that K>=j, L>=v, 0<K-rL<gap-width, and k+ell<=n.

Use the following disjoint left-v blocks (all selected K exceed H, so k>=0):

| left v | witness | maximal prefix length |
| --- | --- | ---: |
| 0..760669 | (K2,V2) | 4,910,648 |
| 760670..1521338 | (K4,V4) | 9,060,626 |
| 1521339..1901633 | (K5,V5) | 10,755,026 |
| 1901634..2282007 | (K6,V6) | 12,830,310 |
| 2282008..2662381 | (K7,V7) | 14,905,515 |

The first two offsets are delta2<delta4 and delta4; every gap globally exceeds delta4. The last three offsets are <epsilon, and their v>V4 intervals have width >=epsilon. Therefore these five families supply a legal prefix in **every** bounded gap with left v<=V7, all of length <=14905515.

## Lemma C: the remaining top 510 rows

H=V7+510. For left endpoint p=(v,j) with v>V7, j<=509. No q in D_H can have 0<x=t(q)-t(p)<gamma.

Indeed integer b=79x-epsilon*dv satisfies -8<b<9, hence b is one of -7,...,8. If b=0, x>0 forces a>=1 and increases v+j by 510a>H-(v+j). If b=1, x<eta-epsilon forces a<=-2, whence dj=431a+60<=-802<-j. If b>=2, eta>4800epsilon gives a<-4800(b-1), whence dj<-509. If b<=-1, positive x yields a>4800(-b), whence dv>(79*4800-11)*(-b)>510>H-v. Each possibility contradicts q in D_H. Thus all these top-row outgoing gaps have width >=gamma.

For each such v, choose the smallest m in {1,...,6} with v<=V7+68+79m. Such an m exists because m=6 reaches V7+542>H. Set L=V7+68+79m and K=K7+371+431m. Then

K-rL=delta7+gamma-m*epsilon belongs strictly to (0,gamma).

The exact verifier checks six pairs of strict inequalities. Counts (K-j,L-v) are nonnegative and their length is <=K7+3498=14,528,640<14,905,515.

The exterior left and right cells are hit by (k,ell)=(0,floor(H/r)+1) and (floor(rH)+1,0), with exact certified lengths 488094 and 14527925, both <=14905515. Label 3 permits padding all constructed prefixes to common length M7=14905515. Therefore N(H)<=14905515.

## Sharp lower bound and resulting plateau

The predecessor scaled-gap first-entry theorem proves: for the translated adjacent cell J_t=(10^431/7^(510+t),1/7^t), the least prefix length is K_i+V_i-t when V_(i-1)<t<=V_i. At t=V6+1=2282008 this cell appears at horizon h=2282518 and requires length K7+V7-(V6+1)=**14905515**. Thus N(2282518)>=14905515.

N(h) is nondecreasing because T_h is nested. For each integer 2282518<=h<=H,

14905515<=N(h)<=N(H)<=14905515.

This completes the proof of the seventh exact plateau. The predecessor supplies the sharp lower bound; Lemmas A-C establish the new upper bound independently.

## Reproducibility, limitations and continuation

VERIFY7.py is the actually executed Python 3.13.5 standard-library Fraction/integer verification program; RUN7.txt records its exact stdout. The finite certificate checks the log enclosure, complete narrow-lattice candidate enumeration, seven witness offsets, five block bounds, six auxiliary gaps and both outer cells. The lemmas prove quantified cell coverage without enumerating the O(H^2) threshold points.

Model scope: the two-point auxiliary S23/AV likelihood-sign experiment retaining the joint label-1/label-4 counts and neutral label-3 padding. P000, ACTIVE Heartbeat X6 worldview and separate six-source/ten-label mother-model mapping are preserved. Mathematical acceptance and any formal shared TASK CLAIM require their own independent authority.

**Next:** establish N(2662892), where the scaled-gap first-entry theorem gives the eighth-step lower bound. Develop multi-witness localized spacing beyond H=2455069 rather than assuming obsolete global epsilon spacing. Keep the independent four-observation minimax error and mother-model transfer questions in the research portfolio.
