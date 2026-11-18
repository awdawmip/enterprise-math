# S23/AV: exact eighteenth and nineteenth capacity plateaux by a third localized witness block

Date: 2026-11-08 (Asia/Shanghai).
Status: AUTHOR_SIDE_ANALYTIC_PROOF_WITH_EXACT_RATIONAL_CERTIFICATE; independent mathematical review pending.
Frozen science: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.

## Exact theorem

In the frozen two-point iid S23/AV auxiliary likelihood-sign observer, the one-step laws on labels (1,3,4) are P0=(1/2,1/4,1/4), P1=(5/7,1/4,1/28). Joint counts (k,ell) of labels 1 and 4 yield prefix score E(k,ell)=k-r*ell, with r=ln(7)/ln(10/7); label 3 gives neutral padding. Thresholds have reflected-log coordinates t(v,j)=r*v-j for v,j nonnegative and v+j<=h. N(h) is the smallest common padded length for which all bounded open threshold cells and both exterior cells contain an attainable prefix score.

Then for EVERY integer h in the following intervals:

| h, inclusive | Exact N(h) |
| --- | ---: |
| 6,466,237 .. 6,846,610 | 37,730,615 |
| 6,846,611 .. 7,226,984 | 39,805,820 |

This extends the preceding exact plateaux 1–17 through h=7,226,984. It is a theorem within the declared auxiliary observer and inherits the separately proved scaled-cell first-entry lower bound. No new physical, X6, or six-source mother-model transfer is asserted.

## Exact irrational and lattice certificate

Set epsilon=79r-431, eta=11r-60, gamma=eta-epsilon, d=2074774-380295r. With U=(79,431), W=(11,60), det(U,W)=-1. Every integer displacement (dv,dj)=aU+bW has threshold width x=a*epsilon+b*eta and the exact integer identity b=79x-epsilon*dv.

The 45-term atanh rational series and its geometric remainder give the strict enclosure LO/Q<r<HI/Q, with Q=10^26, LO=545569623581288298975349314, HI=LO+1. The executable checker establishes 0<d<epsilon, eta>4800epsilon, gamma>6epsilon and epsilon*(Hmax+79)<20 for Hmax=7,226,984. All subsequent inequalities are certified by adverse rational endpoints, not floating-point comparisons.

If p,q lie in D_Hmax and 0<x=t(q)-t(p)<epsilon, then |dv|<=Hmax and hence -20<b<20. If b=0 then x=a*epsilon with integer a>=1, contrary to x<epsilon. For every b in {-19,...,-1,1,...,19}, the interval 0<a*epsilon+b*eta<epsilon has exactly one possible integer a, because eta/epsilon is irrational and this interval has width one in units of epsilon. The checker certifies the integer a for each of these 38 cases and tests the minimal triangle embedding cost C=max(dv_++dj_+,(-dv)_++(-dj)_+). Exactly four have C<=Hmax:

| b | a | (dv,dj) | Minimum H | Width |
| ---: | ---: | --- | ---: | --- |
| -2 | 9630 | (760748,4150410) | 4,911,158 | 2(epsilon-d) |
| -1 | 4815 | (380374,2075205) | 2,455,579 | epsilon-d |
| 1 | -4814 | (-380295,-2074774) | 2,455,069 | d |
| 2 | -9629 | (-760669,-4149979) | 4,910,648 | 2d-epsilon |

All positive differences outside these four types have width >=epsilon. The latter statement applies in particular to consecutive thresholds.

## Localized gap lemma and translated witnesses

For i>=1 define a_i=floor(i*d/epsilon), V_i=380295*i+79*a_i, K_i=2074774*i+431*a_i, delta_i=K_i-r*V_i. The strict rational checks establish the first 19 values of a_i as (0,1,1,2,2,3,4,4,5,5,6,7,7,8,8,9,9,10,11) and all 0<delta_i<epsilon.

For a bounded threshold cell following p=(v,j), a shift (K,L) translates to the admissible prefix (k,ell)=(K-j,L-v). Its score differs from t(p) by K-rL, and its length is K+L-(v+j). If K>=j, L>=v and the positive shift is smaller than every possible outgoing gap, this prefix enters the cell.

Use Hmax throughout the following gap checks, so the bounds cover BOTH endpoints H18=6,846,610 and H19=7,226,984.

1. For 0<=v<=V7=2,662,381 choose (K7,V7); for V7<v<=V12=4,564,093 choose (K12,V12). The two deltas are smaller than all four sub-epsilon widths.
2. For V12<v<=V14=5,324,762 choose (K14,V14). Here the only sub-epsilon width smaller than delta14 is the b=2 displacement (-760669,-4149979), which would require j>=4,149,979 at its left endpoint. But j<=Hmax-(V12+1)=2,662,890, so that displacement cannot occur. The checker certifies delta14 below the remaining three narrow widths.
3. For v>V14, NONE of the four sub-epsilon displacements can originate. For the two decreasing vectors, j would need to be >=2,074,774, but j<=Hmax-(V14+1)=1,902,221. For an increasing vector with cost C, the left endpoint requires v+j<=Hmax-C; its largest such bound is Hmax-2,455,579=4,771,405<V14+1. Thus every bounded outgoing gap above V14 has width >=epsilon.

For each endpoint i=18,19, cover V14<v<=V_i by the successive shifts (K_s,V_s) on each block V_(s-1)<v<=V_s, s=15,...,i. The third item gives outgoing gap >=epsilon and each delta_s lies in (0,epsilon). K_s exceeds Hmax and hence j. The three initial blocks have maximal prefix lengths respectively 17,187,523; 26,802,016; 29,810,952, each <=M18=37,730,615. The middle-block lengths K_s+V_s-(V_(s-1)+1) are <=M_i, as the exact checker verifies.

## Top 510 rows and both exterior cells

At endpoint H_i=V_i+510, each left endpoint v>V_i has j<=509. No positive outgoing difference can have width <gamma. Indeed write x=a*epsilon+b*eta and use the integer b=79x-epsilon*dv. If b=0, then a>=1 and dv+dj=510a>=510 exceeds the available triangle slack <=509. If b=1, x<gamma forces a<=-2 and dj=431a+60<=-802<-j. If b>=2, eta>4800epsilon forces dj<-509. If b<=-1, it forces dv>510, exceeding H_i-v<=509. Hence every top-row gap has width >=gamma; this argument does not require enumeration of b.

For each top-row left v choose the least m in {1,...,6} with L=V_i+68+79m>=v, and put K=K_i+371+431m. The exact verifier checks 0<K-rL<gamma for all six m at both i=18,19. Moreover K>j and the maximum padded length is <=K_i+3498<M_i. The two exterior intervals are reached by (0,floor(H_i/r)+1) and (floor(rH_i)+1,0). Adverse-endpoint checks verify the strict inequalities and lengths <=M_i.

All bounded and exterior cells of T_(H_i) thus contain attainable joint-count prefix scores of length <=M_i. Label 3 pads to the common length M_i, proving N(H_i)<=M_i.

## Sharp lower bounds, evidence, and scope

The existing exact scaled-gap first-entry theorem states that the translated adjacent cell J_t with t=V_(i-1)+1 is first hit at length K_i+V_i-t. It occurs at h=V_(i-1)+511. Thus N(V17+511)>=M18=37,730,615 and N(V18+511)>=M19=39,805,820. Monotonicity of N(h), combined with both endpoint upper bounds, proves the table.

VERIFY.py is the executed Python standard-library Fraction/integer certificate (38 exhaustive narrow-lattice candidates, 19 exact witness offsets, all block and top-row constraints, and exterior checks). RUN_EVIDENCE.txt is its actual stdout; no threshold-triangle O(H^2) enumeration was performed. This is author-side mathematical evidence pending independent review and formal Result admission. The full joint label-1/4 carrier and the label-3 padding are retained. The frozen source and P000 Heartbeat X6 semantics are unchanged.

Source lineage: research_notes/brc_s23_av_seventh_plateau_20261108_research1/PLATEAUX13_17.md at PR #1777 head af26bbd1ecf53fa700ff5c56e755384ed0a3f783; scaled first-entry theorem research_notes/brc_s23_av_scaled_gap_sturmian_jumps_20261108_research1/PROOF.md at 85b53d06d6ba775e516c566c1d79828b6ca9bb1f.

Next: the i=20 horizon H20=7,607,279 admits new b=±3 narrow vectors. Derive a localized repair for b=2 at medium v and b=1 above V14, using short-offset shifts (notably the i=19 witness) only where each narrow displacement is geometrically possible. Verify exact capacity at plateau 20, retaining the original mother-model questions separately.
