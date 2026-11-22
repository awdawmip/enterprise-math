# R762JP — Complementary singleton 44→42 Port–Euler compression

Date: 2026-11-23 (Asia/Shanghai). Scope: frozen six-axis composite Port–Euler observer, not signed native P000 Cell/path/time. Status: **AUTHOR_EXACT_FINITE_CHECKED / NOT_REVIEWED**. Predecessor: R762JO (Draft PR #2978, commit f712e0bbe7ef895d94d2eb6b8b28847d653f91da). Frozen scientific pins unchanged.

## Theorem

Let A={0,1,2,3,4,5}, P=binom(A,2) (15 Port vertices), and S=binom(A,3) (20 support labels). Support {a,b,c} permits events (edges) between distinct pair-Ports ab,ac,bc, with parallel events allowed. N_{p,V}(n)>0 denotes a connected multigraph with exact positive-even-degree Port set V, support counts n_s and Euler start p∈V.

Fix two **complementary/disjoint singleton supports** U={u1,u2}, any T⊂S\U of size 6, and n_s=1 on U, 3 on T, 2 on the remaining 12 supports (total 44). Then for every p,V with N_{p,V}(n)>0 there exists j∈T such that N_{p,V}(n−2e_j)>0, with total 42. The realization preserves exact active Ports, all positive support labels, support parity and any Euler start.

Stronger finite fact: for every Port matching M and V=P\M, a connected 42-event Eulerian realization exists for some j∈T whether or not the input 44-event witness is given. Adding two parallel j-edges to the retained j-edge recovers a 44-event realization. This is observer-level reconstruction, not preservation of native event history.

## Exhaustive finite proof and transport

1. All 20 labels are present. Two inactive pair-Ports sharing an axis would leave a present support with fewer than two active endpoints. Thus every admissible inactive M is a matching on six axes. The size distribution for |M|=0,1,2,3 is 1,15,45,15; total 76.
2. S6 is transitive on the 10 unordered disjoint triple pairs U. Fix U0={012,345}; its setwise stabilizer has order 2*(3!)^2=72.
3. The C(18,6)=18,564 choices of T outside U0 form exactly 307 stabilizer orbits, verified by complete bitmask/permutation enumeration (orbit sizes sum to 18,564). For each orbit representative, **all 76** matchings are verified independently of its residual stabilizer. That is 307*76=23,332 exact integer witnesses.
4. Given any labelled (U,T,M), an axis permutation takes U to U0 and a stabilizer permutation takes T to the representative; the transported M remains one of the 76 checked matchings. Inverse transportation preserves incidence, positivity, even degrees, support parity, connectivity and Euler start. Full labelled coverage is 10*18,564*76 = **14,108,640**.

## Certificate and independent arithmetic

One record is 16 bytes: byte 0 is j∈T; following 15 bytes pack 60 two-bit local edge counts a_{s,k}∈{0,1,2,3}, ordered by lexicographic supports, Ports and local edges. Records are ordered by increasing representative bitmask, then matchings sorted first by size then lexicographically.

The separate Python-standard-library verifier reconstructs S6, all 307 orbits, all 76 matchings and checks *every* record using exact integers: support totals n_s−2*[s=j], total 42, positive even active degrees, inactive degrees zero, and full BFS connectivity. Euler's theorem gives an Euler circuit for any p∈V. SciPy/HiGHS only proposed candidate allocations, with connectivity cuts; its floating outputs are not evidence without the exact checker.

Local checker output: PASS **23,332/23,332** records, grouped by |M| as [307,4605,13815,4605]. Raw 16-byte records: 373,312 bytes, SHA-256 ec4fbf12a906d2a6179d33974645523e6ffcbd0b165742208e45a2337cc4ff0f. LZMA/base64 certificate text: 222,349 bytes, SHA-256 1c9959c35a29f3300a804eeb2f7e218e9d5e4f4e04b7b506056fb5cbb37c9ad3.

Full archive, candidate generator, independent checker, exact evidence and complete proof text are retained together in the contemporaneous downloadable R762JP_Port_Euler_ComplementarySingletons_44to42_Research.zip (ZIP-integrity PASS). The full binary certificate archive is **not included in this GitHub PR**; the published text is a reproducible author result and remote full-certificate archival remains an explicit separate state. Independent review requires access to the raw certificate archive or a genuinely independent recomputation.

## Next frontiers

This resolves all complementary singleton pairs in the (t,d,s,z)=(6,12,2,0) 44-event histogram. Singleton supports sharing 1 or 2 axes remain open. No reduction in the existing author-side global k=0 bound 44 is asserted. R762IR/R762JK independent review and the native P000 signed Cell/path/time and BRC residual-faithful lift remain separate.

Next: classify remaining singleton-intersection types under S6 and seek exact 42-event construction or valid obstruction for their actual observer. This portable scientific save neither requests nor establishes a protected shared CLAIM, Result, Review or Foundation promotion.