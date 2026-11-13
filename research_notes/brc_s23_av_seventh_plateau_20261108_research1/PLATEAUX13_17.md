# S23/AV exact plateaux 13–17: a second localized witness epoch

Date: 2026-11-08 Asia/Shanghai. Status: **AUTHOR_SIDE_ANALYTIC_THEOREM**, certified exact-rational computation; independent review pending.
Frozen scientific input: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Prior exact results: `research_notes/brc_s23_av_six_plateaux_20261108_research1/PROOF.md` at immutable `68e2442c77dbff0dea61970641c05d86a51e32a7`; this directory's `PROOF.md` and `PLATEAUX8_12.md`; and `research_notes/brc_s23_av_scaled_gap_sturmian_jumps_20261108_research1/PROOF.md` at immutable `85b53d06d6ba775e516c566c1d79828b6ca9bb1f`.

## Theorem

In the iid two-point S23/AV likelihood-sign observer, let the ordered one-step label probabilities (1,3,4) be

P0=(1/2,1/4,1/4), P1=(5/7,1/4,1/28).

A prefix with label-1 and label-4 counts (k,ell) has likelihood ratio 7^(k+ell)/10^k; label 3 has neutral likelihood ratio and can pad to a common prefix length. Put T_h={10^i/7^s : integers 0<=i<=s<=h}, and define N(h) as the least common padded prefix length meeting every open likelihood-ratio threshold cell (including both exterior cells).

For **every integer h** in the ranges below, the exact minimum is:

| h inclusive | N(h) |
| --- | ---: |
| 4,564,604 .. 4,944,898 | 27,355,373 |
| 4,944,899 .. 5,325,272 | 29,430,657 |
| 5,325,273 .. 5,705,567 | 31,505,352 |
| 5,705,568 .. 6,085,941 | 33,580,636 |
| 6,085,942 .. 6,466,236 | 35,655,331 |

This extends the exact staircase from twelve to **seventeen plateaux**, covering an additional 1,901,633 integer horizons, without enumerating T_h, whose size grows quadratically.

## Coordinates and exact evidence

Set r=ln7/ln(10/7), epsilon=79r-431, eta=11r-60, gamma=eta-epsilon, d=2074774-380295r. Convert threshold pairs into the integer triangle

D_H={(v,j) in Z^2: v,j>=0, v+j<=H}

with reflected-log coordinate t(v,j)=rv-j. An attainable prefix is E(k,ell)=k-r ell. A prefix is in the cell immediately following a left threshold p=(v,j) when its translated offset is strictly inside the next gap.

The unimodular integer basis U=(79,431), W=(11,60) has determinant -1. Every integer displacement between thresholds is uniquely (dv,dj)=aU+bW and its reflected-log width is x=a epsilon+b eta. The coefficient b is the **integer**

b=79*x-epsilon*dv.

The exact-rational verifier `VERIFY13_17.py` establishes LO/Q<r<HI/Q with Q=10^26, LO=545569623581288298975349314 and HI=LO+1, using 45-term rational atanh expansions and strict tail bounds. All subsequent comparisons use adverse interval endpoints. It checks epsilon>0, eta>4800epsilon, gamma>6epsilon, and epsilon*(Hmax+79)<18, with Hmax=6466236.

### Lemma 1: global narrow-spacing classification

Suppose distinct threshold points p,q belong to D_Hmax and 0<x=t(q)-t(p)<epsilon. Since |dv|<=Hmax, the integer b=79*x-epsilon*dv satisfies -18<b<18 and belongs to {-17,...,-1,1,...,17}. If b=0 then x=a epsilon with integer a>=1, contradicting x<epsilon.

For each nonzero b, at most one integer a gives 0<a epsilon+b eta<epsilon, because this interval has width exactly one unit when divided by epsilon. The rational-enclosure checker exhausts all 34 candidates, then enforces the necessary triangle embedding cost

C(dv,dj)=max(max(dv,0)+max(dj,0), max(-dv,0)+max(-dj,0)) <= Hmax.

**Precisely four** of the 34 candidates satisfy that bound:

| b | a | (dv,dj) | required minimum H | width |
| ---: | ---: | --- | ---: | --- |
| -2 | 9630 | (760748,4150410) | 4,911,158 | 2(epsilon-d) |
| -1 | 4815 | (380374,2075205) | 2,455,579 | epsilon-d |
| 1 | -4814 | (-380295,-2074774) | 2,455,069 | d |
| 2 | -9629 | (-760669,-4149979) | 4,910,648 | 2d-epsilon |

The new narrowest width is 2d-epsilon=delta2=K2-rV2. The checker certifies that **all four widths exceed delta7=K7-rV7**, where

(V7,K7)=(2662381,14525142).

Every other positive threshold difference is at least epsilon. Therefore every bounded threshold gap in D_Hmax is strictly **larger than delta7**. This claim transfers to every H<=Hmax by subset inclusion.

### Lemma 2: high-v gaps have width >=epsilon

Let V12=4564093. Fix any H<=Hmax and a left threshold p=(v,j) with v>V12. If a sub-epsilon displacement were embedded, Lemma 1 shows it must have one of four signs above.

For b=1 or 2, both dv<0 and dj<0, forcing p.j>=2074774, while p.j<=Hmax-(V12+1)=1902142. Impossible.

For b=-1 or -2, both dv>0,dj>0, forcing p.v+p.j<=Hmax-C. The largest such bound is Hmax-2455579=4010657<V12+1. Impossible.

Hence **all bounded outgoing gaps with left v>V12 have width at least epsilon**, uniformly for H<=Hmax.

### Lemma 3: complete translated-witness upper bound at each endpoint

The prior exact first-entry law defines, for each positive integer i,

a_i=floor(i*d/epsilon),
V_i=380295*i+79*a_i,
K_i=2074774*i+431*a_i,
delta_i=K_i-r V_i in (0,epsilon).

A translated witness (K,L) for a left threshold (v,j) produces prefix (k,ell)=(K-j,L-v), with gap offset delta=K-rL and prefix length k+ell=K+L-(v+j).

At H=Hmax, the checker gives a_1,...,a_17 =
(0,1,1,2,2,3,4,4,5,5,6,7,7,8,8,9,9).

For every endpoint H_i=V_i+510 with i=13,...,17, the following two initial blocks work, since each K exceeds Hmax and each offset is smaller than **every** bounded gap (Lemma 1):

| left v | selected (K,L) | max prefix length |
| --- | --- | ---: |
| 0..V7=2662381 | (K7,V7), offset delta7 | 17,187,523 |
| V7+1..V12=4564093 | (K12,V12), offset delta12<delta7 | 26,802,016 |

Both maximum lengths are below the very first new capacity M13=27,355,373.

For each intermediate block V_(s-1)<v<=V_s with s=13,...,i, use (K_s,V_s). Here v>V12, so Lemma 2 gives gap width >=epsilon and 0<delta_s<epsilon guarantees entry. All K_s>H_i, so the prefix has nonnegative counts. The length is at most

M_s=K_s+V_s-(V_(s-1)+1),

and the verifier checks M_s<=M_i in every chosen block.

For top 510 rows v>V_i, the left endpoint has j<=509. The prior top-row gamma lemma applies unchanged: no next threshold can have positive width <gamma. The proof considers the arbitrary integer b=79*x-epsilon*dv. If b=0, then a>=1 and the sum increase dv+dj=510a exceeds the available <=509; if b=1, x<gamma forces a<=-2 and dj<=-802; if b>=2, eta>4800epsilon gives dj<-509; and if b<=-1, it gives dv>510. Each case contradicts threshold membership. This argument needs no bounded b enumeration.

For each such v choose the smallest m in 1..6 with L=V_i+68+79m >=v; m=6 reaches V_i+542. Let K=K_i+371+431m. The offset K-rL=delta_i+gamma-m epsilon is in (0,gamma), certified by six strict rational checks per i. The prefix (K-j,L-v) is nonnegative and length <=K_i+3498<M_i.

Both exterior cells are covered by (0,floor(H_i/r)+1) and (floor(rH_i)+1,0), with strict inequalities and lengths <M_i certified for all five endpoints. Padded prefixes give **N(H_i)<=M_i**.

### Sharp lower bound and monotonicity

The predecessor scaled-gap first-entry theorem gives, for t=V_(i-1)+1, an adjacent threshold cell J_t whose least prefix length is exactly

K_i+V_i-t=M_i.

J_t is present at h=V_(i-1)+511, so N(V_(i-1)+511)>=M_i. Since T_h increases with h and N(h) is nondecreasing, the endpoint bound N(V_i+510)<=M_i proves N(h)=M_i for every h in the indicated interval.

## Verification and next question

`VERIFY13_17.py` executes under Python 3.13.5 standard-library `Fraction` and exact integers. `RUN13_17.txt` is the actual stdout, ending `PASS_S23_AV_ANALYTIC_PLATEAUX_13_TO_17`. It verifies the log enclosure, 34 candidate narrow displacements, four embedding survivors, the global/local width inequalities, initial and intermediate witness blocks, all auxiliary inequalities, five sharp lengths, and both exterior cells. The supplied lemmas account for the universal coverage quantifiers without O(H²) enumeration.

The result is an author-side exact theorem about the two-point S23/AV auxiliary BRC joint-count likelihood-sign observer. The full lawful-parameter delta4 error and the six-source/ten-label mother-model transfer remain separate targets; P000/ACTIVE native six-dimensional spatial reality and its distinct time are unchanged.

**Next discriminating experiment:** at H18=V18+510, enumerate the possible b=±3 narrow displacements. They become embeddable around triangle cost 7.36 million; seek another pair of base translated witnesses with offset below their minimum gap. If a new candidate width is below delta12, split the low-v block at the shortest range required by the displacement's admissible source coordinates rather than reverting to full threshold enumeration.
