# S23/AV auxiliary observer: exact capacity plateaux 21–24 by a universal low-block witness

Date: 2026-11-08 (Asia/Shanghai).
Status: AUTHOR_SIDE_ANALYTIC_PROOF_WITH_EXACT_RATIONAL_CERTIFICATE; independent review/formal Result admission pending.
Frozen science: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.

## Theorem

For the frozen iid two-point S23/AV auxiliary likelihood-sign observer, using joint counts (k,l) of labels 1,4, neutral label-3 padding, and score E(k,l)=k-r*l with r=ln(7)/ln(10/7), let N(h) be the least common padded prefix length hitting every open cell (including both exterior cells) of

    T_h={r*v-j: v,j>=0, v+j<=h}.

For every integer h in the respective inclusive interval, the exact values are

| h range | N(h) |
|---|---:|
| 7,607,280 .. 7,987,653 | 43,955,799 |
| 7,987,654 .. 8,367,948 | 46,030,494 |
| 8,367,949 .. 8,748,322 | 48,105,778 |
| 8,748,323 .. 9,128,696 | 50,180,983 |

Together with the immediately preceding twentieth plateau, this extends certified author-side capacity through h=9,128,696. These auxiliary-observer results retain the precise statistical carrier; transfer to the lawful mother model is a separate research question.

## Exact classification at the common upper horizon

Set Hmax=9,128,696, eps=79r-431, eta=11r-60, d=2074774-380295r, gamma=eta-eps. VERIFY_21_24.py certifies the 45-term rational atanh enclosure

    LO/10^26<r<(LO+1)/10^26,
    LO=545569623581288298975349314,

with positive strict tails. It certifies 0<d<eps, eta>4800eps, gamma>6eps, eps*(Hmax+79)<25.

The unimodular basis U=(79,431), W=(11,60) has det(U,W)=-1. For every integer threshold displacement (dv,dj)=aU+bW, x=r*dv-dj=a*eps+b*eta and the exact integer identity b=79*x-eps*dv hold. When 0<x<eps and |dv|<=Hmax, -25<b<25, with b!=0. Exactly 48 candidate integers b require consideration. Each gives at most one candidate integer a. The executable exact-rational classifier proves exactly SIX geometrically embeddable types:

| b | a | (dv,dj) | minimal triangle H |
|---:|---:|---|---:|
| -3 | 14444 | (1141043,6225184) | 7366227 |
| -2 | 9630 | (760748,4150410) | 4911158 |
| -1 | 4815 | (380374,2075205) | 2455579 |
| +1 | -4814 | (-380295,-2074774) | 2455069 |
| +2 | -9629 | (-760669,-4149979) | 4910648 |
| +3 | -14443 | (-1140964,-6224753) | 7365717 |

Every possible sub-eps threshold gap in all four endpoint triangles has one of those types; the enumeration is finite and exhaustive from the exact b-bound.

## Common cover for four endpoints

Define a_i=floor(i*d/eps), V_i=380295i+79a_i, K_i=2074774i+431a_i, delta_i=K_i-rV_i. The exact checker proves the first 24 a_i values and 0<delta_i<eps. In particular, V7=2662381, V12=4564093, V19=7226474, and

| i | V_i | H_i=V_i+510 | M_i=K_i+V_i-(V_(i-1)+1) |
|---:|---:|---:|---:|
| 21 | 7987143 | 7987653 | 43955799 |
| 22 | 8367438 | 8367948 | 46030494 |
| 23 | 8747812 | 8748322 | 48105778 |
| 24 | 9128186 | 9128696 | 50180983 |

For left threshold (v,j), witness (K_i,V_i) gives an attainable prefix (k,l)=(K_i-j,V_i-v) of length K_i+V_i-(v+j) and score t(v,j)+delta_i, whenever K_i>=j and V_i>=v. It hits the next open cell if no narrower positive threshold difference can originate at (v,j).

At each endpoint H_i for i=21..24, partition the left endpoints into:

1. 0<=v<=V7: use witness 7.
2. V7<v<=V12: use witness 12.
3. V12<v<=V19: use witness 19.
4. For each s=20,...,i, V_(s-1)<v<=V_s: use witness s.

The checker proves that delta7, delta12 and delta19 are below the width of ALL six narrow displacement types, making the first three blocks valid for every j. The third block is a particularly effective construction: the worst prefix length is

    K19+V19-(V12+1)=42087827 < M21.

Thus witness 19 covers the entire region from v=4564094 through v=7226474 even after the b=+2 narrow gap becomes geometrically possible at higher h. This removes the need for a fine polygon partition.

For v>V19, all six sub-eps directions are impossible at the largest horizon Hmax. Positive-coordinate directions require v+j<=Hmax-cost<=6673117<V19+1. Negative-coordinate directions require j>=2074774, whereas j<=Hmax-(V19+1)=1902221. Hence every outgoing gap in the high blocks is >=eps>delta_s. The checker verifies K_s>H_i, V_s covers its assigned v, and K_s+V_s-(V_(s-1)+1)<=M_i for every high strip and all four endpoints.

## Top rows, exteriors, lower bound, full intervals

For any endpoint H_i=V_i+510, left endpoints v>V_i have j<=509. The existing top-row gamma-spacing argument applies uniformly: if x=a*eps+b*eta in (0,gamma), b=0 would require a positive coordinate sum of at least 510; b=1 requires dj<=-802; b>=2 requires dj<-509; b<=-1 requires dv>510. Each contradicts admissibility. Thus every positive outgoing gap there has width >=gamma. For each such v take the least m in {1,...,6} with L=V_i+68+79m>=v and K=K_i+371+431m. The checker proves 0<K-rL<gamma, K>j and K+L-(V_i+1)<=M_i and L(m=6)>=H_i. These witnesses cover every top-row cell.

The two exterior cells are entered by (k,l)=(0,floor(H_i/r)+1) and (floor(rH_i)+1,0); their exact lengths are bounded by M_i in each case, as checked. Label-3 padding achieves the common length M_i. Therefore N(H_i)<=M_i.

The inherited exact scaled-gap first-entry theorem (research_notes/brc_s23_av_scaled_gap_sturmian_jumps_20261108_research1/PROOF.md, Theorem A) establishes N(V_(i-1)+511)>=M_i. Monotonicity of N(h) therefore proves exact equality on each stated integer interval.

## Evidence and scope

VERIFY_21_24.py is the actually executed Python standard-library Fraction and integer certificate; RUN_21_24.txt is exact run stdout. The finite classification covers all 48 lattice candidates in the declared domain; the infinite collection of threshold cells is covered analytically by the source-coordinate strips. No quadratic threshold enumeration is performed. The lower-bound input is an existing explicitly identified author-side theorem. Independent mathematical review remains pending; the protected P000/Heartbeat X6 premises and frozen science are unchanged.
