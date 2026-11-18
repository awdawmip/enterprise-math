# R5 — exact bridge counterexample: Hamming target separation 2 destroys additivity

Date: 2026-11-15. Scientific pin 435e77af0d180eac32bd1f9c4c464bc4010b7551.
Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.
Scope: the auxiliary R5 mixed-weighted indexed-center observer with radius-two replacement, using the exact old and a-closure core-distance table in SEPARATED_STAR_RESIDUAL_KERNEL_AND_AB_RIGIDITY_THEOREM.md.

## Exact counterexample

Work in the binary 4-cube. Let two translated unit stars be

- h0=0000, Y0={1,2,4} (integer bitmask notation).
- h1=1111, Y1={14,13,11}.
- Y=Y0 union Y1={1,2,4,11,13,14}.
- Old suffix language X=Y union {5,10}.

Both star centers 0 and 15 are absent from X. All target suffixes are pairwise Hamming-separated by at least 2; the minimum cross-star distance is **exactly 2**. By the earlier arbitrary-old-language single-star theorem, the two stars considered separately each require 2*3=6 old resources. Their separate optimum sum is 12.

Yet their joint a-closure minimum is exactly

**kappa_a(X,Y;2) = 10.**

This is an explicit sharpness witness for the cross-target separation at least 3 condition in the preceding exact tensorization theorem: at separation 2, the additivity conclusion can fail.

## Ten-entry upper witness

Take the six baselines (O1,0,y) for every y in Y, plus the four resources

(O0,1,5), (O4,1,5), (O0,1,10), (O4,1,10).

The old cores are O0=0125, O1=0135, O4=0246. The two bridge suffixes partition the six target suffixes into two disjoint sets of three at Hamming distance exactly one:

- Hamming-neighbors in Y of 5 are {1,4,13}.
- Hamming-neighbors in Y of 10 are {2,11,14}.

For every y, its O1 baseline repairs 1235, 1345, 1346 in the a-target family: respective replacement distances 2,1,2. Its assigned O0 bridge repairs 1245 with distance 1+1=2, and its assigned O4 bridge repairs 1246 with distance 1+1=2. Thus all five a-target cores at every y are covered, proving kappa_a<=10.

## Matching lower bound (no optimizer black box)

For each of the six suffixes y, the target E_y=(1346,0,y) requires an old resource exactly (O1,0,y) or (O4,0,y). These are six distinct compulsory *baseline slots*. No other old resource repairs E_y, by the exact seven-event core-distance matrix and radius-two budget.

Consider the 24 critical targets
B_y=(1245,1,y), C_y=(1246,1,y), D_y=(1345,0,y), E_y=(1346,0,y), for y in Y.

A compulsory baseline configuration covers at most two of the 24 critical targets: it repairs only critical targets with its exact suffix y, because all distinct target suffixes have Hamming distance at least 2 and every core distance is at least 1. The core matrix then limits an O1 or O4 first-bit-zero baseline to at most two critical types at that suffix.

Every other old configuration covers at most three critical targets. When its suffix is in Y, it can act only at that one target suffix, and covers at most two critical types. The only other old suffixes in X are 5 and 10. Each is adjacent to exactly three target suffixes. At suffix distance one, each fixed old (core,first-bit) can repair at most one of B,C,D,E for each adjacent y, so its critical-target coverage is at most three.

Therefore any library with at most nine entries could cover at most

6*(2) + 3*(3) = 21 < 24

of the critical targets. It cannot repair them all. Hence kappa_a>=10. Combined with the explicit ten-entry construction, the equality is exact.

## Interpretation and remaining boundary

The bridge suffixes 5 and 10 are neither old star center; a single core-labeled old helper now serves targets from **both** previously separate groups. This is precisely the interaction information that is lost by applying a one-star cardinality formula independently after the cross-group Hamming separation fails.

The universal double-closure rigidity still gives kappa_ab(X,Y;2)=2|Y|=12, for the same X,Y; only single-a cardinality drops from the separate-star value 12 to 10.

The companion Python certificate recomputes all replacement distances, exhaustively checks the six compulsory E witnesses and per-resource 24-critical-target coverage bounds across all 80 old configurations, and verifies every target with the ten-entry witness using exact integers. It returned PASS_R5_OVERLAPPING_STAR_BRIDGE_SHARPNESS. This is a complete finite proof of the exact example; it is not evidence of a general formula when target clusters overlap.

Next: characterize a weighted overlap/incidence graph that predicts when bridge suffixes reduce the advice-library minimum, and extend the exact observer to future repair compositions without discarding old-helper provenance.
