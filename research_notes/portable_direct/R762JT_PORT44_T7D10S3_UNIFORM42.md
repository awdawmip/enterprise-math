# R762JT — full-support (7,10,3,0) Port–Euler 44→42 theorem

**Date:** 2026-11-23 Asia/Shanghai. **Status:** AUTHOR_PROVED_BY_EXHAUSTIVE_FINITE_LEMMA / NOT_REVIEWED. Scientific predecessor: R762JS, Draft PR #2988 @ 2cb122e7d63a148efe40515d514f242181eb870c. Task science retains the frozen X6 publication pins. This result is about the composite Port–Euler observer; it does not establish a native signed P000 Cell/path/time/branch or BRC lift.

## Definitions and theorem

Let A={0,...,5}, P=C(A,2) (15 Ports), S=C(A,3) (20 support colors). A color-s event joins two distinct Ports in C(s,2), allowing parallel edges. Write N_(p,V)(n)>0 when an undirected connected multigraph has exactly n_s color-s events, positive even degrees exactly on V⊆P, degree zero off V, and an Euler circuit beginning at any designated p∈V.

**Theorem (new terminal class).** If n∈{1,2,3}^20 has histogram (3s,2s,1s,0s)=(7,10,3,0), then

\[
N_{p,V}(n)>0\Longrightarrow
\left|\{j:n_j=3,\ N_{p,V}(n-2e_j)>0\}\right|\ge6.
\]

Each successful construction has 42 events, preserves every positive support label, multiplicity parity of each label, the exact active Port set V, and the designated circuit origin p. This resolves the entire (7,10,3,0) 44-event class at the author level. The overall k=0 author-side bound remains 44 while other terminal histograms are unresolved.

## Forced components and parity

Since every support has positive multiplicity, two inactive Ports ab and ac cannot share an axis: the support abc would have only one active endpoint, so none of its positive events could be represented. Hence the inactive Port set M=P\V is a matching of m=0,1,2,3 edges. Under all six-axis permutations choose representative M_m=first m of (01,23,45).

A *forced* support contains a missing Port and has exactly two active Ports, so each of its events has a unique legal edge. The forced supports induce respectively 15,10,6,3 connected components for m=0,1,2,3. A *flexible* support has three active Ports, giving a triangle on which each event can use any of three sides. The flexible support counts are respectively 20,16,12,8.

Use degree boundaries ∂(uv)=e_u+e_v in GF(2)^V. For a flexible support occurring once, its local parity set is its three nonzero side boundaries. For a flexible support occurring twice or thrice, the local parity set is {0,∂(uv),∂(uw),∂(vw)}. Moreover, for either multiplicity two or three, **every** local parity can be realized while preserving connectivity between endpoints of any predesignated triangle side: double the designated side at multiplicity-two/zero parity, take the two-side path at multiplicity-two/nonzero parity, use all three edges at multiplicity-three/zero, and use the odd side plus a doubled different side at multiplicity-three/nonzero.

Let F be the flexible colors and D⊆F the singleton flexible colors, |D|≤4. Let U_D be the GF(2) span of all possible side boundaries from flexible colors outside D. The exact finite parity lemma is

\[
\{\textstyle\sum_{s\in D}\partial(e_s)+u:
e_s\text{ a side of color }s,\ u\in U_D\}
=\{b\in{\bf F}_2^V:\sum_{v\in V}b_v=0\}.
\]

The attached Python standard-library verifier enumerates every D for every m, constructs a binary row-echelon basis for U_D, reduces all choices for the singleton sides into the quotient, and verifies the number of attainable cosets is exactly 2^(|V|-1-rank(U_D)). All **9670/9670** patterns pass. Forced-color edges have an even global degree boundary and can therefore always be cancelled by the flexible-color assignments.

## Certified rainbow forest

For every m and D with |D|≤4 except one specifically described *pencil pattern*, there exists a tree joining all forced-edge components, using one edge from each of distinct flexible colors in F\D.

The pencil pattern is D equal to the four supports containing a single active Port ab which is disjoint in its axes from every missing Port of M. Such a Port is isolated in the forced-edge graph and does not appear in any flexible color outside D. This is a failure of the **strong flexible-only rainbow tree method**, not a proven obstruction to other Euler realizations.

For all non-pencil D, a deterministic seeded search produces a finite tree certificate. The generator independently checks the chosen colors and edges; the separately written archive verifier rebuilds forced components and checks color distinctness, acyclicity and connectivity for every certificate. An unsuccessful stochastic attempt cannot be used to claim a valid tree. Exact enumeration:

| m | flexible F | all D, |D|≤4 | parity PASS | rainbow tree PASS | pencil exceptions |
|---:|---:|---:|---:|---:|---:|
| 0 | 20 | 6196 | 6196 | 6181 | 15 |
| 1 | 16 | 2517 | 2517 | 2511 | 6 |
| 2 | 12 | 794 | 794 | 793 | 1 |
| 3 | 8 | 163 | 163 | 163 | 0 |
| total | | **9670** | **9670** | **9648** | **22** |

Given nonexceptional D, solve flexible parities to cancel the forced boundary, independently select the rainbow component tree, and realize each non-singleton flexible color with its chosen parity *and* connectivity across its designated tree side. All forced components are joined, each vertex is active and positive, and all degrees are even. Euler's circuit theorem gives a loop from each p∈V.

## Proof of the ≥6 reductions

Let S0 be the three originally singleton supports. For any of the seven triple colors j, the target inventory n−2e_j has exactly four singleton colors S0∪{j}. Any method exception would require S0∪{j} to be a four-color pencil. Distinct Port pencils intersect in at most one support color: a three-axis support contains two distinct Port pairs only when those pairs span its three axes, making the common support unique. Thus a fixed three-color S0 lies in at most one pencil, and at most one choice of j completes an exceptional pencil. At least six j meet both lemmas and yield a connected 42-event even-degree graph with exact support labels and parities, active V and origin p. **QED.**

## Reproduction, limitations, next

- Generator and exact parity checking: R762JT_PORT44_T7D10S3_UNIFORM42_VERIFY.py (Python 3 stdlib), producing R762JT_EVIDENCE.json and R762JT_RAINBOW_CERTS.b64.
- Independent exact archive verification: R762JT_VERIFY_ARCHIVE.py, checking the full case domain, GF(2) quotients, unique tree colors and explicit forest connectivity without invoking the generator's search.
- Evidence: 9670 exact parity cases PASS, 9648 explicit rainbow forests PASS, and 22 precisely classified pencil exclusions. Both local programs completed and independently matched those totals. The full 9648-certificate archive is available in the conversation's complete research ZIP; the GitHub generator reconstructs the same archive deterministically. If the binary archive itself is not present in a checkout, run the generator first before the independent verifier.

**Scope:** finite, mathematically exact proof for the *composite Port–Euler* model, pending independent review. It does not imply a native P000 signed update, future-observer/residual preservation, BRC dynamics, or formal Result/Review admission. No current shared CLAIM/PROGRESS was made.

**Next research:** examine whether the four-singleton pencil pattern admits direct Euler realizations, attack the remaining 44-event histograms, independently review R762IR and the earlier uniform-44 dependencies, and separately develop a typed P000/BRC-faithful correspondence.
