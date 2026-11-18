# S23/AV: five more exact plateaux, through h=4,564,603

Date: 2026-11-08 (Asia/Shanghai). Frozen scientific input: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. Status: **author-side analytic theorem with exact rational certificate, independent review pending**.

Predecessors: the six-plateau result (research_notes/brc_s23_av_six_plateaux_20261108_research1/PROOF.md at immutable commit 68e2442c77dbff0dea61970641c05d86a51e32a7), the adjacent seventh-plateau PROOF.md, and the scaled-gap first-entry theorem (research_notes/brc_s23_av_scaled_gap_sturmian_jumps_20261108_research1/PROOF.md at 85b53d06d6ba775e516c566c1d79828b6ca9bb1f).

## Exact theorem

For the two-point iid S23/AV likelihood-sign observer with one-step laws P0=(1/2,1/4,1/4), P1=(5/7,1/4,1/28) on ordered labels (1,3,4), let T_h={10^i/7^s : integers 0<=i<=s<=h}, and let N(h) be the least common padded prefix length hitting every open likelihood-ratio threshold cell, including exterior cells. Neutral label 3 permits padding. **For all integers** in each horizon interval:

| Horizon h | Exact N(h) |
| --- | ---: |
| 2,662,892 to 3,043,186 | 16,980,210 |
| 3,043,187 to 3,423,560 | 19,055,494 |
| 3,423,561 to 3,803,855 | 21,130,189 |
| 3,803,856 to 4,184,229 | 23,205,473 |
| 4,184,230 to 4,564,603 | 25,280,678 |

These are exact plateaux 8–12: five further strict jumps and 1,901,712 horizon integers beyond the seventh result.

## Unimodular setup and exact gap exhaustion

Let r=ln7/ln(10/7), epsilon=79r-431, eta=11r-60, gamma=eta-epsilon and d=2074774-380295r. Represent thresholds in reflected-log coordinates t(v,j)=rv-j, with D_H={(v,j):v,j>=0,v+j<=H}; prefix count (k,ell) has E(k,ell)=k-r ell. The unimodular basis U=(79,431), W=(11,60) has determinant -1. Every integer difference (dv,dj)=aU+bW has width x=a epsilon+b eta and the **integer identity** b=79x-epsilon dv.

The verified rational enclosure LO/Q<r<HI/Q, with Q=10^26, LO=545569623581288298975349314 and HI=LO+1, comes from 45-term exact Fraction logarithm series with explicit strict remainder bounds. It certifies epsilon>0, eta>4800epsilon, gamma>6epsilon and epsilon*(H+79)<13 for H=4,564,603.

If 0<x<epsilon between points of D_H, then |dv|<=H gives -13<b<13. The b=0 case is impossible since a>=1 then x>=epsilon. For each b in {-12,...,-1,1,...,12}, the interval 0<a epsilon+b eta<epsilon contains at most one integer a, found by exact rational floor bounds. Exhausting all 24 possibilities and checking necessary triangle size

C(dv,dj)=max(max(dv,0)+max(dj,0),max(-dv,0)+max(-dj,0))<=H

leaves exactly two candidates:

| b,a | (dv,dj) | C | width |
| --- | --- | ---: | --- |
| -1, 4815 | (380374,2075205) | 2,455,579 | epsilon-d |
| 1, -4814 | (-380295,-2074774) | 2,455,069 | d |

Both widths strictly exceed delta4=K4-rV4, where (K4,V4)=(8299958,1521338); the exact verifier checks both adverse inequalities. Every bounded threshold gap is therefore **strictly larger than delta4**.

For left v>V7=2,662,381, the b=1 displacement demands j>=2074774, but j<=H-(V7+1)<=1902221, impossible. For b=-1, the displacement increases v+j by 2455579, requiring left v+j<=H-2455579<=2109024<V7+1, impossible. Thus **all bounded gaps whose left v>V7 have width at least epsilon**, for all H<=H12.

## Uniform translated-witness covering

The prior scaled-gap construction defines

a_i=floor(i*d/epsilon), V_i=380295*i+79*a_i, K_i=2074774*i+431*a_i, delta_i=K_i-r V_i.

For i=1,...,12, exact rational checks confirm the a_i values (0,1,1,2,2,3,4,4,5,5,6,7), and 0<delta_i<epsilon. For any gap after p=(v,j) a pair (K,L) translates into legal prefix (k,ell)=(K-j,L-v) with separation K-rL and length K+L-(v+j). Whenever K>=j, L>=v, and 0<K-rL<gap-width, the cell is occupied.

The following two initial blocks work **simultaneously for all five endpoint horizons**, and both selected K exceed H12:

| left v | Witness | Largest prefix length |
| --- | --- | ---: |
| 0..1,521,338 | (K4,V4) | 9,821,296 |
| 1,521,339..2,662,381 | (K7,V7) | 15,666,184 |

The first offset equals delta4, and the second delta7<delta4; every positive gap exceeds delta4. The maximal prefix length of 15,666,184 is less than M8=16,980,210.

For endpoint H_i=V_i+510, where i=8,...,12, cover remaining medium v in successive blocks V_(s-1)<v<=V_s for s=8,...,i by (K_s,V_s). These start above V7, so their gaps have width >=epsilon. Each offset delta_s lies in (0,epsilon), and each K_s exceeds the endpoint H_i, yielding valid nonnegative counts. Their maximum lengths are

M_s=K_s+V_s-(V_(s-1)+1),

and the verifier certifies M_s<=M_i for s<=i in this range.

For the top 510 rows v>V_i and j<=509, the **top-row gamma lemma** from the seventh-plateau proof applies unchanged: no q in D_(H_i) can have 0<t(q)-t(p)<gamma. To see this, set x=t(q)-t(p), b=79x-epsilon dv (an arbitrary integer). b=0 forces triangle growth 510a>H_i-v-j; b=1 forces dj<=-802; b>=2 forces dj<-509 using eta>4800epsilon; and b<=-1 forces dv>510. Each contradicts endpoint membership. There is no finite bound on b needed for this case split.

For the top rows choose the least m=1,...,6 with L=V_i+68+79m>=v (m=6 reaches V_i+542>H_i) and K=K_i+371+431m. Then K-rL=delta_i+gamma-m epsilon lies strictly between 0 and gamma, by exact verified inequalities. The prefix is legal and has length <=K_i+3498<M_i. The exterior left/right cells have the explicit witnesses (0,floor(H_i/r)+1) and (floor(rH_i)+1,0); the exact checker certifies their lengths <M_i.

Consequently every open threshold cell of T_(H_i) is occupied by a prefix of length at most M_i, and label 3 pads each to that common length: **N(H_i)<=M_i**, for i=8,...,12.

## Sharp lower bound and interval conclusion

The previously proved scaled-gap first-entry theorem gives, for t=V_(i-1)+1, a particular adjacent cell J_t first occupied at prefix length K_i+V_i-t=M_i. That cell appears at horizon h=V_(i-1)+511, so **N(V_(i-1)+511)>=M_i**. Since T_h is nested, N(h) is nondecreasing. Therefore N(h)=M_i throughout every interval [V_(i-1)+511,V_i+510], proving the table.

## Evidence, model scope and next question

VERIFY8_12.py is the actually executed Python 3.13.5 integer/Fraction rational certificate and RUN8_12.txt is the exact stdout. It checks complete sub-epsilon candidate exhaustion, the local gap inequalities, the two universal low blocks, all medium and high-v witnesses, five endpoint lengths and all outer cells. The quantified proof uses translated witness lemmas instead of O(H^2) threshold enumeration.

The result applies to the declared two-point auxiliary S23/AV BRC joint-count sign observer with neutral label-3 padding. The separate six-source/ten-label mother-model bridge, four-observation minimax-error target and P000/ACTIVE X6 semantics retain their existing scopes.

**Next:** Analyze h=H13=4,944,898 and the newly embeddable b=+2 and b=-2 near-resonance differences (minimum triangle sizes 4,910,648 and 4,911,158). Determine whether a new low-v witness block can recover exact plateau 13 without exhaustive threshold sorting.
