# R762JA — Complete eight-triple 47→45 compression and k=0 upper bound 46

Date: 2026-11-22 (Asia/Shanghai).
Frozen scientific input: \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`.
Scope: **composite Port–Euler observer** of the six-axis model; not a signed native P000 Cell/time/force/rotation lifting.
Status: **AUTHOR_PROVED / EXACT_FINITE_CERTIFICATES_VERIFIED / NOT_REVIEWED**.
Predecessors: R762IR, R762IU, R762IV, R762IW, R762IX, R762IY, R762IZ.

## Model and new theorem

Let \(A=\{0,1,2,3,4,5\}\), with 15 Ports \(P=\binom{A}{2}\) and 20 supports \(\mathcal S=\binom{A}{3}\).
Each event of support \(S=\{a,b,c\}\) chooses one edge between two of the three Ports \(ab,ac,bc\), allowing parallel edges.
A legal closed history has a connected even-degree multigraph on precisely its positive-degree Port set \(V\), with prescribed start \(p\in V\).
Write \(N_{p,V}(n)>0\) for existence at support multiplicity vector \(n\).

**Theorem (complete eight-triple terminal class).** For every legal history whose 20 support multiplicities have histogram \((t,d,s,z)=(8,11,1,0)\) (47 events), some triple support can be reduced from count 3 to count 1, preserving the active set, designated start, all positive support types, parity of each support count and existence of an Euler circuit:

\[
N_{p,V}(n)>0
\quad\Longrightarrow\quad
\exists j:\ n_j=3,\ N_{p,V}(n-2e_j)>0 .
\]

This is a computer-assisted finite proof; its 300 explicit integer certificates are published with a standard-library-only independent checker.

## Exhaustive proof

**Case 1: A triple support contains an inactive Port.**
Because all 20 supports have positive count, two inactive Ports cannot share an axis: the support containing their three axes would have fewer than two active Port vertices and hence no allowed event edge. Thus the inactive Port set \(M=P\setminus V\) is a matching in \(K_6\).
If one of the eight triple supports contains an inactive Port, precisely two Ports of its triangle remain active. All three events must lie on the unique allowed edge. Removing two parallel copies preserves an edge of that support, active Port degrees modulo 2, connectivity and the exact active set.

**Case 2: Every triple is fully active and a triple is nonessential in the triangle-union graph.**
Let \(T\) be the set of eight triple supports and \(G(T)\) the union of *all three possible edges* of each support triangle on the 15 Ports. If deletion of \(j\in T\) does not increase the number of connected components, the three Port vertices of \(j\) remain mutually connected through \(G(T\setminus\{j\})\).
Replace its three events by one edge \(uv\) of \(j\). The degree parity change is an even GF(2) boundary supported in the three Port vertices of \(j\), either zero or two odd vertices. Route any two odd vertices along a path in \(G(T\setminus\{j\})\), grouping the traversed edges by supporting triangle. Each retained triangle receives an even local boundary, either zero or a pair of Port endpoints.
Any even local boundary of a triangle is realizable using **exactly three edges that connect all its three Port vertices**: the triangle's 3-cycle realizes zero boundary; one edge between the odd pair plus two parallel edges connecting one of that pair to the third vertex realizes the prescribed pair. Reassign the three events of each retained triple accordingly. All degrees are even again. Each retained triangle preserves (and can extend) the original within-support connectivity. The three vertices of the reduced support remain connected through the retained triangle graph; all other support allocations are fixed. Consequently the overall active Port graph stays connected, has the same active set and is Eulerian.

**Case 3: All eight fully active triple supports are essential.**
Enumerate \(\binom{20}{8}=125,970\) possible eight-support families \(T\) with an integer union-find component counter on the 15 Port vertices. Exactly **4,920** are all-essential (deleting any triple increases the component count); under the six-axis permutation group \(S_6\), they form **16 orbits**. Their triangle unions cover 13, 14 or 15 distinct Ports.

For each of the 16 orbit representatives, enumerate every inactive matching \(M\) disjoint from that union (necessary because every triple is fully active), and each of 12 choices of the singleton support outside \(T\). Reduce the lexicographically first triple support \(j\) from 3 to 1, keeping seven other triples at 3, one singleton at 1 and eleven doubles at 2.

The complete representative verification domain consists of **300 cases**: grouped by the count of Port vertices outside the triple union, \(120,96,84\) for \(0,1,2\); grouped by \(|M|\), \(192,96,12\) for \(0,1,2\). For every case the certificate provides all 60 nonnegative integer allocations to the three allowed event edges of each support; the independent checker confirms:

- Exactly 45 total events and each specified support multiplicity.
- No event touches an inactive Port; every active Port has strictly positive even degree.
- The active Port graph is connected.
- The compressed vector differs from the 47-event vector only in the one prescribed \(3\to1\) reduction.

The action of \(S_6\) transports each representative certificate to every axis-labelled case in its orbit. Euler's multigraph theorem permits any start \(p\in V\). These three cases exhaust the full \((8,11,1,0)\) histogram.

### Exact certificate material and reproducibility

Files alongside this note:
\`R762JA_CERTS.b64\` contains 300 edge-allocation certificates, each 60 integers in \(\{0,1,2,3\}\); four 2-bit values are packed per byte, giving exactly **4,500 raw bytes**, then zlib-compressed and base64-encoded.
\`R762JA_VERIFY_CERTS.py\` reproduces the union-find classification, 16 orbits, the exact representative parameter domain, and all degree/support/connectivity checks using only Python's standard library.

Raw certificate stream SHA-256: \`6b30b9be0cea2a021f894c2e5b3d82fec736b910faf52a0409a6145aa6b21980\`.
Compressed stream SHA-256: \`808000aeed1e01de0d9ff3c0336be6c22b80f92b6a467b8d204f79aacff741f5\`.
Local execution on 2026-11-22: **PASS**, 4,920 essential sets, 16 orbits, 300/300 explicit Euler witnesses. A SciPy/HiGHS integer optimizer with connectivity cuts generated the witnesses; independent mathematical verification relies on the emitted integers and the standard-library verifier, not on solver status or floating-point tolerance.

## Consequence: k=0 uniform 46-event bound

The prior R762IU author-side theorem gives a witness of length at most 47 for every legal multiplicity vector \(n\in\{0,1,2,3\}^{20}\), preserving active set, support presence, support-count parity and chosen start.
If a witness has exactly 47 events and at most 10 triple supports, its histogram is exactly one of the following six cases; each has an author-proved 47→45 reduction:

| \((t,d,s,z)\) | Proof |
|---|---|
| \((7,13,0,0)\) | R762IV |
| \((8,11,1,0)\) | **R762JA, new** |
| \((9,9,2,0)\) | R762IY, R762IZ, plus the explicit nonessential-triangle reduction |
| \((9,10,0,1)\) | R762IW, plus the explicit nonessential-triangle reduction |
| \((10,7,3,0)\) | R762IY |
| \((10,8,1,1)\) | R762IX |

With at least eleven triple supports, R762IR's author-side triangle-redundancy lemma supplies a nonessential triple, unless a triple has only two active Ports, which is the immediate parallel-pair case. Therefore every 47-event witness compresses to 45 while all witnesses already at 46 or less stay as they are. Combining with R762IU gives the following **derived author-side theorem, conditional on the stated previous author-proved dependencies**:

\[
\boxed{N_{p,V}(n)>0,\ n\in\{0,1,2,3\}^{20}
\ \Longrightarrow\
\exists h\le n:\ N_{p,V}(h)>0,\quad
\operatorname{supp}(h)=\operatorname{supp}(n),\quad
h\equiv n\pmod 2,\quad \sum_S h_S\le46.}
\]

This improves the preceding k=0 upper bound 47 to **46** within the exact composite Port–Euler observer. It does not alter the previously stated **54** for the separate fourfold-support model. All dependencies retain **NOT_REVIEWED** status: GitHub publication is source preservation, not independent proof acceptance.

The observation preserved is Port activity, support presence, support parity, closed Euler realizability and chosen start. Full event ordering, branching, native signed X6 path/residual, force/phase and time are outside this observer map; a native P000 lifting requires its own proof.

Next: independently audit R762IR and the orbit predicates; investigate 46-event terminal histograms for a 44-event witness or an exact lower bound; extend to fourfold critical supports and native signed P000 dynamics without changing the frozen input pin.
