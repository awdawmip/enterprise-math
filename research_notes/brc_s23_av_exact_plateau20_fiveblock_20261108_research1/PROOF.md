# S23/AV twentieth exact capacity plateau: a five-block integer-lattice proof

Date: 2026-11-08 Asia/Shanghai. Status: AUTHOR_SIDE_ANALYTIC_PROOF_EXACT_RATIONAL_CERTIFICATE; independent review pending.
Frozen scientific inputs: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.

## Exact theorem

For the frozen two-point iid S23/AV auxiliary likelihood-sign experiment with one-step laws on labels (1,3,4), P0=(1/2,1/4,1/4), P1=(5/7,1/4,1/28), let E(k,l)=k-r*l, where k and l jointly count labels 1 and 4 and label 3 gives neutral padding. Define r=ln(7)/ln(10/7), T_h={r*v-j: v,j>=0 integers and v+j<=h}. N(h) is the minimum *common padded prefix length* required to hit every bounded open threshold cell and both exterior cells.

Then for EVERY integer h with

    7,226,985 <= h <= 7,607,279

we have the exact equality

    N(h)=41,880,515.

This adds 380,295 integer horizons beyond the nineteenth plateau. This is a result for the stated auxiliary statistical observer; the lawful six-source/ten-label mother-model transfer is an independent question.

## Exhaustive narrow-gap classification

Put eps=79*r-431, eta=11*r-60, gamma=eta-eps and d=2074774-380295*r.
The checker VERIFY_FIVE_BLOCK.py certifies through a 45-term rational atanh enclosure (with explicit tail):

    LO/10^26 < r < (LO+1)/10^26,
    LO=545569623581288298975349314,

and consequently 0<d<eps, eta>4800*eps, gamma>6*eps, and eps*(H+79)<21 for H=7607279.

The determinant det((79,431),(11,60))=-1. Every integer displacement (dv,dj) between thresholds is uniquely a*(79,431)+b*(11,60), with integer a,b. Its positive score difference is x=dv*r-dj=a*eps+b*eta and the identity b=79*x-eps*dv is exact.

For 0<x<eps and |dv|<=H, -21<b<21. The case b=0 would force x=a*eps>=eps. Thus b belongs to exactly forty candidate values {-20,...,-1,1,...,20}. For each, the interval 0<a*eps+b*eta<eps has a unique integral a; the checker certifies its floor with adverse rational endpoints. The triangle-embedding cost is max(dv_+ + dj_+, (-dv)_+ + (-dj)_+). Only the following SIX types have cost <=H:

| b | a | (dv,dj) | required minimal H |
|---:|---:|---|---:|
| -3 | 14444 | (1141043,6225184) | 7366227 |
| -2 | 9630 | (760748,4150410) | 4911158 |
| -1 | 4815 | (380374,2075205) | 2455579 |
| +1 | -4814 | (-380295,-2074774) | 2455069 |
| +2 | -9629 | (-760669,-4149979) | 4910648 |
| +3 | -14443 | (-1140964,-6224753) | 7365717 |

Every potentially narrower-than-eps outgoing threshold gap is among these six; this is exhaustive finite lattice classification, not sampled numerical agreement.

## Five uniform translated witness blocks

For integer i>=1 let a_i=floor(i*d/eps), V_i=380295*i+79*a_i, K_i=2074774*i+431*a_i and delta_i=K_i-r*V_i. The exact checker verifies first 20 values and 0<delta_i<eps. In particular,

    V7=2662381, V12=4564093, V14=5324762,
    V19=7226474, V20=7606769,
    K19=39425447, K20=41500221.

For any left threshold p=(v,j), the shift (K_i,V_i) yields prefix (k,l)=(K_i-j,V_i-v) with E(k,l)=t(p)+delta_i and length K_i+V_i-(v+j). It enters the next open cell whenever no threshold displacement with positive width <delta_i can originate at p.

The complete five-block cover is:

| left v | witness i | maximal prefix length |
|---|---:|---:|
| 0..2662381 | 7 | 17187523 |
| 2662382..4564093 | 12 | 26802016 |
| 4564094..5324762 | 14 | 29810952 |
| 5324763..7226474 | 19 | 41327158 |
| 7226475..7606769 | 20 | 41880515 |

Widths delta7, delta12 and delta19 are strictly smaller than ALL six narrow widths, so blocks 7,12,19 work for every admissible j. Width delta14 is smaller than all except b=+2, whose negative displacement needs j>=4149979. But on block 14, j<=H-(V12+1)<4149979, excluding that type.

Above V19, negative-coordinate narrow types require j>=2074774, but j<=H-(V19+1)=380804. Positive-coordinate types require v+j<=H-cost<=5151700<V19+1. Therefore ALL six narrow types are impossible in block 20; every outgoing gap there has width >=eps>delta20.

Each witness has K_i>H, its V_i dominates its assigned v, and the exact checker verifies the five maximal lengths. Thus every bounded cell whose left endpoint v<=V20 is reached within M20=K20+V20-(V19+1)=41880515.

The new construction is the long fourth block: reuse the nineteenth very-small-offset witness uniformly across (V14,V19]. Its worst required length, 41327158, remains below M20. No per-row threshold enumeration is needed.

## Last 510 rows, exterior cells and sharp lower bound

For v>V20, j<=509. The earlier exact top-row lemma shows no outgoing gap narrower than gamma=eta-eps: writing x=a*eps+b*eta, b=0 gives positive displacement sum 510a>509; b=1 implies a<=-2 and dj<=-802; b>=2 implies dj<-509 by eta>4800eps; b<=-1 implies dv>510. Each contradicts triangle feasibility. For each such v choose the smallest m in {1,...,6} with L=V20+68+79m>=v, K=K20+371+431m. The checker proves 0<K-r*L<gamma, K>j and K+L-(V20+1)<=M20 for all six candidates, and m=6 reaches above H.

The left and right exterior cells are reached by (0,floor(H/r)+1) and (floor(r*H)+1,0), respectively. The certified prefix lengths 1394374 and 41503004 are <=M20. Label 3 pads all legal prefixes to common length M20. Hence N(H)<=M20.

Sharpness uses the previously established *scaled-gap exact first-entry theorem* (research_notes/brc_s23_av_scaled_gap_sturmian_jumps_20261108_research1/PROOF.md, Theorem A): the translated adjacent gap J_t at t=V19+1 has least entry length K20+V20-t=M20, and appears when h=t+510=7226985. So N(7226985)>=M20. Monotonicity of N(h) combined with endpoint coverage yields the stated exact constant value throughout 7226985..7607279.

## Verification, scope and provenance

VERIFY_FIVE_BLOCK.py is an executable Python-standard-library Fraction certificate; RUN_FIVE_BLOCK.txt is its actual stdout. The finite b-classification covers all relevant integer displacements, while the full-quantifier coverage is by analytic strips, not an O(H^2) point scan. The sharp lower bound is reused with its exact statement and scientific pin; independent mathematical review and formal Source Result admission remain pending.

Relevant preceding evidence: research_notes/brc_s23_av_analytic_plateaux18_19_20261108_r1/PROOF.md and the universal first-entry theorem in the same PR #1777. Protected P000 / Heartbeat X6 worldview and frozen science are unchanged.
