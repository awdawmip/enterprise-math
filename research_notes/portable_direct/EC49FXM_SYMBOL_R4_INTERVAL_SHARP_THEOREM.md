# EC49FXM — Sharp symbol distance-4 observer optimum for all consecutive relative-phase sets

**Date:** 2026-11-23 (Asia/Shanghai). **Frozen scientific pin:** BRC16943. **Scientific status:** AUTHOR_PROVED / EXACT_INTEGER_CROSSCHECK / PARENT_DEPENDENT / NOT_REVIEWED.

**Predecessors:** EC49FXK (whole-activation symbol distance 2), EC49FXL (symbol distance 3 in the same Draft PR #2986). Both concern the same pinned auxiliary Farey–CRT two-channel Boolean observer. No world-model, frozen input or meaning-of-error change is introduced.

## Exact theorem

Let D_k={0,...,k-1} subset of Z/110 for 1<=k<=55. Each physical activation t in S subset of Z/110 yields the ordered two-channel Boolean pair, treated as **one symbol**. As in EC49FXL,

\[
G_S(d,i,j)=\sum_{t\in S}\mathbf1\big[
(t\bmod5=i\ \&\ t\bmod11\ne j)
\ \lor\
((d-t)\bmod5=i\ \&\ (d-t)\bmod11\ne j)
\big].
\]

Require G_S(d,i,j)>=4 for every d in D_k, i in Z/5 and j in Z/11. This minimum symbol distance supports one arbitrary unknown whole-activation error **plus one known whole-activation erasure** (2*1+1<4).

**Sharp result for all 55 k values:**

\[
\boxed{
N_{\mathrm{symbol}}(D_k;4)=
\begin{cases}
14,&1\le k\le2,\\
17,&3\le k\le4,\\
20,&5\le k\le45,\\
k-25,&46\le k\le49,\\
25,&50\le k\le55.
\end{cases}}
\]

As in EC49FXL, the long constant-cost regime persists through k=45. Adding phases k=46,...,50 raises the optimal cost by exactly one each time.

## Lower bound

Put m_i=|{t∈S:t mod5=i}|.

**For k<=2:** phase d=0 is allowed. Its self-color row i=0 requires m_0>=4 because all its support lies in color 0. A distinct-color row has support exactly in two different colors i,h with d≡i+h (mod5), and some missing-column j deletes at least one of their symbols; thus it is necessary that m_i+m_h>=5. For d=0 the pairs {1,4},{2,3} are disjoint, giving |S|>=4+5+5=14.

**For k=3,4:** the self-color phases d=0,1,2 respectively require m_0,m_3,m_1>=4; phase d=1 also involves distinct-color pair {2,4}, requiring m_2+m_4>=5. Thus |S|>=4+4+4+5=17.

**For k>=5:** d=0,...,4 include the five self-color residues; every m_i>=4, giving |S|>=20.

If m_i=4 then no selected site in that color may satisfy (2t mod55)<k: otherwise the allowed self-color phase d≡2t (mod55), missing column j=t mod11, deletes that physical symbol and leaves at most three. As there are only two physical lifts t,t+55 of one residue modulo55, a 4-site color needs at least two *different* safe residues x mod55 with x mod5=i and 2x mod55>=k.

The safe-residue counts for k=45,...,50 by color i=0,...,4 are:

| k | safe counts | number of colors able to have 4 sites |
|---|---|---:|
| 45 | 2,2,2,2,2 | 5 |
| 46 | 1,2,2,2,2 | 4 |
| 47 | 1,2,2,1,2 | 3 |
| 48 | 1,1,2,1,2 | 2 |
| 49 | 1,1,2,1,1 | 1 |
| 50 | 1,1,1,1,1 | 0 |

Beyond k=50, no count grows. With L=max(0,50-k) possible 4-site colors for 45<=k<=55, at least 5-L colors need >=5 sites, so |S|>=4L+5(5-L)=25-L. This proves all lower bounds.

## Attaining configurations

**Small k:** Exact witnesses (all sites are distinct in Z/110):

For k=1,2, use the 14-site set

\[
S_2=\{1,3,4,9,10,13,14,19,25,27,33,40,43,50\}.
\]

For k=3,4, use the 17-site set

\[
S_4=\{5,9,10,12,14,15,18,23,26,30,31,33,36,39,41,48,49\}.
\]

The standalone verifier evaluates all corresponding d,i,j rows, with exact per-row minima; both attain G>=4. The finite checks comprise 110 and 220 rows respectively.

**Uniform construction for k>=5:** For each i=0,...,4 define the safe base-residue set

\[
A_i(k)=\{x\in\{0,\ldots,54\}:x\bmod5=i,\ (2x\bmod55)\ge k\}.
\]

If |A_i(k)|>=2, pick any two distinct safe residues a,b in it and activate their **four physical lifts** {a,a+55,b,b+55}. If |A_i(k)|<2, activate the five heavy sites {i,i+5,i+10,i+15,i+20}. The verifier chooses the largest two safe residues for reproducibility. Each site's mod5 color is i and different color sets are disjoint.

The count is 4L+5(5-L), with L=5 for k=5,...,45, L=4,3,2,1 for k=46,...,49, and L=0 for k>=50, precisely the theorem's upper bound.

In a self-color row, all four sites of a light color survive every missing column, since their 2t mod55 are outside D_k. For a heavy color the five mod11 columns are distinct, so at most one activation vanishes and at least four survive.

In a distinct-color row the two channel contributions occupy disjoint mod5 color classes. A 4-site light color has exactly two different mod11 columns, each duplicated by its two physical lifts, so any missing column deletes at most two of its sites. A 5-site heavy color uses five distinct mod11 columns, so any missing column deletes at most one. Therefore two light colors retain at least 4+4-2-2=4, a light/heavy pair at least 4+5-2-1=6, and two heavy colors at least 5+5-1-1=8. All cases satisfy G>=4. The explicit upper bound equals the lower bound for every k.

## Evidence and boundaries

EC49FXM_SYMBOL_R4_INTERVAL_VERIFY.js evaluates every k=1,...,55, d=0,...,k-1, i=0,...,4 and j=0,...,10, totalling exactly 84,700 **integer** symbol-distance checks. The immutable output records all sites and their minimum observed distance (=4), plus the small-k row matrices and safe-residue counts. An independent local HiGHS integer-programming crosscheck agrees on all 55 optima; the analytic proof does not rely on solver tolerances.

This theorem is for the pinned auxiliary Farey–CRT observer only. No inference is made yet about genuine same-anchor Farey phase reachability, full signed/height/path provenance, native six-dimensional world dynamics, formal Result or independent Review.

**Next scientific direction:** Test whole-activation symbol distances r=5,6 under these same consecutive D_k, and derive the exact family of attainable relative phases from the original Farey anchor evolution. For genuine dynamics retain source provenance rather than treating D_k as a freely chosen phase set.
