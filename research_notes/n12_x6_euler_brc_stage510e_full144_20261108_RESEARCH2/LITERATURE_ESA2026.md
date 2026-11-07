# Stage510-E literature comparison — verified 2026 ESA publication

Verified on 2026-11-08 from publisher's official proceedings page:

- Ben Bals, Solon P. Pissis, Matei Tinca, "Optimal Enumeration of Eulerian Trails in Directed Graphs", 34th Annual European Symposium on Algorithms, LIPIcs 388, article 60, pages 60:1–60:16, publication date **2026-08-25**, DOI **10.4230/LIPIcs.ESA.2026.60**. Official publisher URL: https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2026.60
- The authors derive an **output-sensitive O(m+z_T)** *enumeration* algorithm where z_T denotes the number of reported Eulerian trails, and describe an extension to directed multigraphs. The publisher abstract explicitly separates polynomial counting via BEST from listing all solutions.

**Relation to this project.** Stage510-E solves **exact random-access rank/unrank** for indistinguishable parallel-edge native-X6 **direction words** under all 144 directed adjacent relation counts. Its per-prefix completion counter uses directed matrix-tree/BEST, all repeated multiplicity factorials and exact big integers, and it can return a word at a chosen 940-bit rank without listing all preceding trails. Enumeration time O(m+z_T) and per-query rank/unrank costs measure different targets; no direct algorithmic speedup is claimed without common problem/output semantics and same-input cost comparisons. If a later comparison uses the ESA algorithm, define whether parallel copies are distinguishable and whether duplicates of identical direction words are emitted. The generic theorem is a classical BEST-derived count; project-specific contribution is its typed observer-preserving exact implementation and full-144 inventory reference benchmark.

This literature note does not modify Stage510-E proof, frozen scientific inputs or physical-model claims.
