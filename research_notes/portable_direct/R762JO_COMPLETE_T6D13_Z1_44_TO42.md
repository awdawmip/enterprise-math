# R762JO — Complete 44→42 compression of (6,13,0,1)

Date: 2026-11-23 (Asia/Shanghai). Status: **AUTHOR_EXACT_FINITE_CHECKED / NOT_REVIEWED**. Frozen science: predecessor R762JN, immutable task source pins unchanged. This is the six-axis **composite Port–Euler observer**, not the native signed P000 triadic Cell/path/time model.

## Theorem and quantified domain

Let (A=\{0,1,2,3,4,5\}), (P=\binom A2) (15 Port vertices) and (\mathcal S=\binom A3) (20 support labels). A support (s) has the three Port vertices (\binom s2); an event of (s) is one edge joining two distinct such vertices (parallel edges permitted). A legal (N_{p,V}(n)>0) witness is a connected multigraph with positive even degrees on exactly active (V\subseteq P), zero degrees outside, prescribed support counts (n_s), and an Euler circuit from (p\in V).

Fix an absent support (z\in\mathcal S) and a six-set (T\subseteq\mathcal S\setminus\{z\}). Put (n_z=0), (n_s=3) for (s\in T), and (n_s=2) for the 13 other labels. Then, for *every* (V,p) with (N_{p,V}(n)>0), there exists (j\in T) such that
\[
N_{p,V}(n-2e_j)>0,\qquad\sum_s(n-2e_j)_s=42.
\]
The new circuit retains *exact active Port set*, *all positive support labels*, *per-support count parity* and *any original starting Port*.

More strongly: the 42-event witness exists for every locally eligible inactive set (M=P\setminus V), meaning (|M\cap\binom s2|\le1) for all (s\ne z), regardless of whether the 44-event witness was given. This eligibility is necessary for the original graph: every present support has positive count and requires at least two active local Ports. Adding two parallel (j)-edges along a retained (j)-edge recovers a 44-event witness.

## Finite completeness proof

1. Exhaustively enumerate **all (2^{15}=32768)** possible inactive Port subsets for fixed (z). Exactly **92** obey local eligibility. They partition into **1 empty, 16 nonmatching, 75 nonempty matching** sets (the latter means all inactive pairs are mutually disjoint in the six-axis set).
2. The action (S_6) is transitive on 20 absent labels. Fix (z=\{0,1,2\}). The stabilizer (S_3\times S_3) has 36 permutations and divides the (\binom{19}{6}=27132) choices of (T) into **885 exact orbits**; their sizes sum to 27,132.
3. For *each* representative (T), verify all 92 inactive sets, avoiding any unstated restriction from the representative's residual stabilizer. The new R762JO computation supplies **885×75 = 66,375** certificates for matching sets. R762JN already supplied **885×17 = 15,045** certificates for empty and nonmatching sets. The same new standalone integer checker successfully checks **81,420** certificates.
4. The axis permutations preserve support incidence, counts, parity, exact active sets and connectivity; apply inverse transport of every representative witness. Hence coverage is **20×27,132×92 = 49,922,880 labelled instances**. This is an exact finite computer-assisted proof of the stated composite-model theorem.

## Certificate semantics and independent verification

Each certificate is 16 bytes: first byte is deleted-support index (j\in T), followed by 15 packed bytes holding four 2-bit integers each. The resulting **60** local-edge multiplicities (a_{s,e}\in\{0,1,2,3\}) must satisfy: for each (s), \(\sum_{e\in E_s}a_{s,e}=n_s-2\mathbf 1[s=j]\); grand total exactly 42; positive even degree at every active Port, zero degree at every inactive Port; and positive-edge graph connected. Euler's theorem then gives a closed trail based at **any** (p\in V).

SciPy/HiGHS was **only a proposer**, with connectivity cuts. No floating-point output was accepted as proof: every certificate was checked using exact integer arithmetic and graph traversal in the separate standard-library verifier. Independent verifier regenerates incidence, 36 stabilizer permutations, 885 orbits, and 92 eligibility patterns by itself. Sources used for prior archives: R762JN package and GitHub Draft PR #2975@e7c02b1b55f6debed1612bbf012a86e7e27700bd; the new 66,375-record raw archive is preserved with the attached full research package, *not* asserted to have been uploaded to GitHub.

| Part | Exact verified records | Raw SHA-256 |
|---|---:|---|
| New matching inactive configurations | 66,375 | `b53b09e48aa3c124a2cce3cca54c437a99e928e96f6150944a71077a325654f8` |
| Previously saved R762JN fully active | 885 | `52ccee2fab77f0b8ff343cffbebbe2833dc3fe2f10bc5fa963c0412e22a4a738` |
| Previously saved R762JN 16 nonmatching | 14,160 | `a255c9a3fc95d4d578a99243c68171d114db7bef038b3fc28b2035b037d5e512` |
| **Total** | **81,420** | separately hashed as above |

Raw lengths respectively **1,062,000; 14,160; 226,560 bytes**. New Base64 archive text SHA-256: `b7078a725ed5472d64fa2ade3fdebd9bf4ad193eb41eccfde32e705919fa886a`. Exact evidence summary is stored in `R762JO_EVIDENCE.json`; verifier source `R762JO_INDEPENDENT_VERIFY.py`; regenerating method uses the previous R762JM candidate proposer plus `R762JO_MATCHING_GENERATE.py`.

## What is solved and what remains

This completes **the whole (6,13,0,1) 44→42 terminal class**, including all 75 previously open nonempty matching patterns. The separate (6,12,2,0) class remains open. Earlier author-side global (k=0\) 44-event bound depends on unreviewed R762IR/R762JK antecedents; completion of this terminal class alone **does not** lower the global bound. Native signed P000 Cell/path/branch/time or typed BRC residue transfer needs a separate observer- and future-operation-safe lift, preserving source provenance and signed/path information.

Next research: tackle (6,12,2,0), and seek a structural parity/bridge proof replacing finite search; audit the antecedent GF(2) reduction where material. No P000, frozen-source, Task/CLAIM, Result, Review, owner or activity promotion is claimed.
