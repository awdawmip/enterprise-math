# R284CV — 34-bit Port observer: exact minimum top-R cores through R = 20,000

**Status:** AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED. Date: 2026-11-21. Portable independent research; no shared TASK CLAIM or native X6 physical assertion.

## Frozen input and provenance

Continuation of R284CU, with the unchanged R284CO frozen checker at `awdawmip/enterprise-math@acba2d8667903434aaa2a10720f43637fcc2421b:research_notes/portable_direct/R284CO_spectral_witness_checker.py`, Git blob `b46e0f682b58e47c27094b4bea6fa4e55119a3ee`. Parameters: `P=17179869143`, `D=(1120832,6,13,1651128)`, `Z=(0,390139,394465,1497639)`, `SELECT=(0,1,2,4,5,6)`. The 65,536 distinct codeword residues have ordered SHA256 `b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4`. The exact observer consists of 64 labeled circular arcs.

For a codeword `x`, sort all 64 distances from the labeled arcs increasingly as `d_1(x),...,d_64(x)`. An **R-core**, `1 <= R <= 20000`, is a subset preserving for every `k=2,...,64` the top-R descending values of `d_k`, including multiplicities. Level `d_1=0` is automatically retained because any R-core contains at least R points.

## Exact finite theorem

Among every integer rank `1 <= R <= 20000`, **only four ranks** have nonunique minimum-cardinality R-cores:

| R | Minimum cardinality | Number of minimum cores | Unforced cutoff level |
|---:|---:|---:|---:|
| 779 | 21,944 | 2 | 64 |
| 1263 | 25,997 | 2 | 64 |
| 1563 | 27,499 | 2 | 64 |
| **7587** | **42,637** | **2** | **64** |

All remaining ranks in this exact interval have one unique minimum core. The adjacent ranks R=7586,7588 have unique minimum cores with 42,634 and 42,640 points respectively. At R=20000 the unique minimum core has 61,404 points.

Across 63 nonconstant distance levels there are **1,384 distinct tie-boundary ranks** in the interval. At **118 ranks**, at least two levels tie simultaneously (maximum: three levels). The first simultaneous event is **R=2269**, levels **4 and 38**, but their tied candidates are already forced by other levels, so the minimum core remains unique. The first nonunique minimum with simultaneous ties appears at **R=7587**.

At R=7587 the two tied levels have exact data:

| Level | Cutoff distance | Equal-cutoff residues | Forced by other levels |
|---:|---:|---|---:|
| 3 | 253,278,355 | 5,495,896,646 and 7,946,415,859 | both |
| 64 | 8,381,496,764 | 10,044,326,029 and 14,547,547,380 | neither |

Thus the mandatory union contains **42,636** points. Adding either one of the two level-64 residues yields a different minimum R-core of size **42,637**. With residues sorted ascending and encoded as unsigned 8-byte big-endian integers, their SHA256 digests are:

- `031ff9ce474211540a7244469d5784fc782e1fffd1d06d1333f7bc7f66992e4d`
- `6be92ebd1a971783c4c163a00a76b6342df17c7fb164fa292d534222e8cb2992`

The unique R=7588 minimum core has SHA256 `d9528a70300c53ff3abef51e706414c0f0ada0813d90beeb79785d9a91f3a29d`.

## General reduction and proof of finite classification

For any finite set `X` and functions `f_k:X -> R`, let `t_{k,R}` be the Rth largest value with multiplicity, `H_{k,R}={x:f_k(x)>t_{k,R}}`, `E_{k,R}={x:f_k(x)=t_{k,R}}`, and `q_{k,R}=R-|H_{k,R}|`. A subset `C` preserves the entire top-R multiset for level k **if and only if** `H_{k,R} subset C` and `|C intersect E_{k,R}| >= q_{k,R}`. Every higher value and enough equal-cutoff copies are necessary, and collecting precisely these values is sufficient. Intersecting the conditions across levels gives an exact residual hypergraph covering problem.

The mandatory basis `M_R` used by the verifier is the union of all strictly-above-cutoff sites and all **singleton-cutoff** sites of non-tied levels. At a tied level the remaining cardinality constraint is the number of required equal-cutoff members not already in `M_R`. There may be tie groups of size greater than two; the checker evaluates their full groups and quotas rather than assuming pairwise ties.

For a fixed rank R, the verifier adds one actual top-R site from each of the 63 sorted level lists to per-site prefix frequencies. For every level whose entries at positions R and R+1 are equal, it temporarily subtracts the tied portion appearing in the first R entries. The positive-frequency sites are exactly `M_R`. It tests each tied equal-cutoff group for its residual quota and restores the prefix counts before advancing the rank.

For the complete exact range R=1,...,20000, **all** tied groups have no outstanding quota except R=779,1263,1563,7587. At each exceptional rank exactly one tied level has quota one and exactly two unforced members; all other levels have zero deficit. Thus each exceptional rank has precisely two distinct minimum cores, while every other rank has exactly one. The stated core sizes and residue hashes are the resulting exact unions. Direct reconstruction of the 63 level top-R multisets additionally confirms both 7587 cores and the unique 7588 core.

This is a symbolic finite-set lemma combined with an exhaustive exact-integer certificate over the stated finite interval. No rank above 20,000 or non-Port observer is included in the classification.

## Verification and limitations

The companion standard-library Python checker imports the unchanged frozen R284CO definition, verifies the 65,536-codeword SHA256 and previous 3,712-point R284CS core digest, generates all **4,194,304 exact integer arc distances**, checks **1,260,000** adjacent rank/level positions, evaluates all **1,384** equality events and **118** simultaneous events, and reproduces the three R284CU minima and the new fourth one. It recomputes all full top-R multisets on the two new 7587 minima and unique 7588 minimum. Executed successfully locally. A separately implemented NumPy vectorized exact integer computation agreed on event counts, exception ranks and new core residues/digests; these are author-controlled checks, not independent mathematical review.

The JSON certificate records all four exception sets, the first simultaneous events, model pin, minimum-cardinality cores and hashes. Neither formal Result admission nor Working Truth/Foundational promotion has been made. Frozen 34-bit Port-observer calculations have not been reclassified as a native six-axis dynamics law.

## Next question

Determine the **first rank above 20,000** where two or more unforced cutoff groups require a genuinely coupled hypergraph minimum-cover decision, rather than a single binary choice. Explore relations between the R7587 level-64 pair and the earlier three exceptional pairs; develop an incremental event-driven algorithm to avoid full distance row reconstruction while retaining all exact input and residual provenance.
