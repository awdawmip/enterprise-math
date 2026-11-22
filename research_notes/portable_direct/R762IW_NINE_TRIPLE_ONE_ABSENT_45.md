# R762IW — 47→45 in the nine-triple / ten-double / one-absent Port–Euler class

Date: 2026-11-22 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FINITE_CERTIFICATE_VERIFIED / NOT_REVIEWED.

Scientific pin (unchanged): `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`. Composite observer and terminology: R762IV (Draft PR #2951, commit `f65fb8c707ddf92014a7e13362e6785755fee810`). This result is a statement about the composite Port–Euler observation, not about the signed native P000 Cell / phase / time / rotation history.

## Definitions

Let A={0,1,2,3,4,5}, P=C(A,2) (15 Ports), and H=C(A,3) (20 supports). The three Ports contained in S∈H form a triangle with three possible event-edges; one event of support S selects one such edge. An allowed closed realization has a connected multigraph on exactly its positive-degree Port set V, all degrees positive and even, and prescribed start p∈V. Let n_S be the count of support S.

For T⊂H of size 9 define the *support-triangle union graph* G(T) on all 15 Ports, with all three triangle edges for each S∈T. Call T all-essential if removing any one S∈T strictly increases the number of connected components of G(T). Take z∈H\T and the 47-event histogram

- n_S=3 for S∈T;
- n_z=0;
- n_S=2 for all remaining ten supports.

A candidate active set V⊆P is *locally eligible* if every S≠z contains at least two Ports belonging to V. This is necessary for every positive support to choose an event-edge.

## Theorem — all-essential 47→45, including inactive Ports

For every all-essential 9-support family T, every omitted z∉T, and every locally eligible V, let j=min(T) in the lexicographic order of the twenty triples. There exists a connected even-degree event allocation on **exactly V**, having n'_j=1 and n'_S=n_S for all S≠j. In particular

[
\sum_S n'_S=45,\qquad n'_S\le n_S,\quad n'_S\equiv n_S\pmod 2.
]

Every positive support remains positive. Since the allocation graph is connected and Eulerian, it has an Euler circuit from **any** requested p∈V. The deleted two copies of support j can be reinserted as a parallel edge pair using j's surviving event-edge, recovering the original 47-event histogram with the same active Port set. The theorem is stronger than the conditional statement "if an original 47-event closed realization exists" for this all-essential class: local eligibility alone is sufficient.

## Exact finite proof and coverage

Enumerate all C(20,9)=167,960 choices of T. The exact union-find component predicate produces **240 all-essential T**. For each, z can be any of the other 11 supports: 2,640 labeled (T,z) pairs. The five adjacent swaps of axes generate the full S6 action on these pairs; breadth-first orbit enumeration gives **nine** orbits with sizes

`60,60,360,180,360,360,720,360,180`.

The corresponding lexicographically minimal representative pairs (support bitmask, absent-support index) are

`(511,9),(511,10),(511,11),(511,15),(2029,1),(2029,11),(2029,13),(2029,15),(2029,19)`.

For each representative, enumerate all 2^15 possible inactive-Port masks and retain those with at least two active Ports in every support except z. **Exactly 92** masks qualify for each representative, split by numbers of inactive Ports as `[1,15,48,25,3]` for k=0,1,2,3,4. Thus **9×92=828** representative allocation checks cover **2,640×92=242,880** labeled (T,z,V) instances by axis-permutation equivariance.

The accompanying 12,420-byte certificate stream specifies a 60-entry edge multiplicity vector for each representative mask, in deterministic enumeration order. Four consecutive entries, each in {0,1,2,3}, are packed in one byte; 15 bytes represent one allocation. The stream is zlib-compressed and base64-encoded in `R762IW_CERTS.b64`. The companion `R762IW_VERIFY_CERTS.py` is **standard-library only**: it independently enumerates the exact finite domains and orbits, decodes each certificate and checks every per-support edge sum, forbidden Port degree zero, positive even degrees of exactly V, and connectivity. It returns PASS for all 828 and checks the byte SHA256

`15d611b1e80d16b45ab9ec471c233e826d60bb6f189377041c566acaa2631035`.

The certificates were constructed locally using integer MILP proposals with connectivity cuts (SciPy/HiGHS); mathematical acceptance depends only on the independent integer certificate checks, not a solver status or floating-point feasibility. Because support-edge incidence and all predicates are equivariant under permutations of A, applying an axis permutation to each certificate proves all labeled cases.

## What this advances and what remains open

This closes the **all-essential** 47-event terminal histogram (t,d,s,z)=(9,10,0,1), with all eligible active sets, improving the earlier R762IU path on this case. For **non-essential** T the R762IR parity/connectedness redundancy lemma offers a conditional 47→45 reduction; that antecedent lemma retains its author-side / not-independently-reviewed status. This note does not upgrade it by assertion.

The other 47-event terminal histograms remain to investigate: (8,11,1,0), (9,9,2,0), (10,7,3,0), and (10,8,1,1), with (7,13,0,0) treated in R762IV. The full k=0 author-side uniform bound is still 47; the k>0 four-event critical-support bound remains 54 under its separate assumptions. Neither is a new native signed P000 theorem.

Scientific proof status: finite exhaustive certificate, locally run and integer-verified; independent mathematical review pending. Control status: this portable result is not a formal CLAIM, PROGRESS, Result or Review. The gateway status/Task read attempt returned `BACKEND_IDENTITY_CHECK_UNAVAILABLE / operation_sent=false` during this turn, so current owner and authenticated write authority remain unconfirmed; no protected control mutation was attempted.
