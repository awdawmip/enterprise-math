# EC49FWU — Exact two-sided Farey observer theorem: no fixed-site reduction

**Date 2026-11-22 · frozen BRC16943 · predecessor EC49FWT @136457f47094a12c087f2eb44f31a04b08409480 · AUTHOR_PROVED / EXACT_INTEGER_CERTIFICATE / PARENT_DEPENDENT / NOT_REVIEWED**

## Population, quantifiers, and theorem

Use the original frozen 44-pair P10 predicate and C11(h,n)=P10(h mod10,n mod10) AND ((9h+10n) mod11 !=0). For *each unknown reduced rational anchor* 0<a<b, construct the two signed determinant-one Farey branches, separately Euclidean/lexicographically normalized as in EC49FWT. The observed baseline is the **ordered pair of complete indexed 110-period reflection-defect spectra**. A fixed paired-probe layout reads Boolean membership at previously specified (sign, t mod110). Require minimum Hamming distance r between different *paired periodic words* having identical two spectra.

**Sharp theorem:** For every 1<=r<=10, N_joint,fixed(r)=3(r+1). Thus exact reconstruction takes **6**, resistance to one known erasure **9**, and correction of one unknown wrong bit **12** fixed physical readings. A universal optimum observes only the left branch, with modulo-10 rows 1,2,3 in r+1 distinct modulo-11 columns. CRT physical index: t=11*row+100*column mod110. Neither the extra right spectrum nor access to right-side probes reduces the worst-case fixed-site cost. Spectrum-adaptive minimum N_joint,adaptive(r)=r for 1<=r<=10.

The object identified is the pair of normalized periodic membership words; the anchor numerator, denominator, rephasing and height origin remain separate provenance.

## Genuine-anchor lower bound: three disjoint two-sided blocks

Define disjoint physical row blocks:

| Block | Left modulo-10 rows | Right modulo-10 rows |
|---|---|---|
| A | {1,4,6,9} | {1,4,6,9} |
| B | {2,7} | {3,8} |
| C | {3,8} | {2,7} |

For *every* block G and *every* j in Z/11 there are two actually reduced anchors with identical **both** full indexed defect spectra and with exact membership difference

D(G,j) = (G_left x (Z11 without {j})) union (G_right x (Z11 without {1-j mod11})).

The accompanying standalone exact-integer verifier reconstructs **33 explicit anchor pairs, all with b<=80**, checks 14,520 direct C11 evaluations against their CRT words, compares both full indexed spectra and validates the entire 220-site difference support per pair.

Let T be any fixed paired layout and m_G the number of its sites in block G. If m_G=0, its G-witness is unseparated. If 1<=m_G<=r, pick one of those observed sites: choose j to erase its left column, or j=1-(its right column) to erase its right column. The corresponding *real* G-witness has measured distance at most m_G-1<r. Hence m_G>=r+1 for each G, and because the three blocks are disjoint, |T|>=3(r+1).

## Universal upper bound from a 1,150-state exact finite carrier

Let v=(a,b-a), and p_minus/p_plus the normalized signed Farey origins. The two preliminary Euclidean origins sum to v for a>1 and to zero for a=1. Their final modulo-10 rephasings each add t*v with t in {0,...,9}; therefore p_minus+p_plus=k*v for some integer 0<=k<=19. Since C11(-p)=C11(p), the normalized right word is R(t)=L(-k-t). The congruence class of k mod10 is uniquely determined by the primitive direction (a,b-a) mod10 and the two lexicographic roots. When the left mod11 factor has excluded residue h_L, the right excluded residue obeys h_R=-k-h_L mod11; the full-factor case maps to full.

Thus every genuine anchor lies within the explicit finite superset formed from all **72 primitive modulo-10 directions**, the corresponding k in {0,...,19}, and all twelve allowed full/one-hole left factors. The standalone verifier deduplicates exactly **1,150** paired states, with **964 distinct paired spectral fibers**, of which **186 are doubletons**. Every doubleton has distinct left word, with at least **20 differing left bits** and **40 differing paired bits**.

A complete exact check of the 186 doubletons verifies that the left-only rows 1,2,3, with r+1 chosen distinct columns (take 0,...,r), give minimum observed distance r for r=1,...,10. This proves the upper bound for *all* genuine anchors irrespective of denominator. Once the spectra are known, each fiber has at most two candidate paired words and r positions among their at least 40 differing paired bits suffice, proving the adaptive upper bound; a real ambiguous pair proves its lower bound.

## Evidence, scope and next problem

Execute `node EC49FWU_JOINT_TWO_SIDED_VERIFY.js`; its accompanying JSON is the complete output including the actual 33 anchor-pair witnesses. Arithmetic is exact integer arithmetic. The proof uses the same BRC16943 predicate, CRT coupling, signed branches and origin provenance, while preserving the active P000 and X6 observer-safety limits. No Lean, CI, separate Review or formal Task/CLAIM/Result is asserted.

The fixed-site negative improvement statement is specific to the *unknown-anchor complete-paired-spectrum* observer, not a general redundancy result for the right branch. Next study known-anchor sensor drift, branch activation cost, and the typed signed height readout of EC49FVU; the left/right mirror may reduce physical resource cost in those different observation models.
