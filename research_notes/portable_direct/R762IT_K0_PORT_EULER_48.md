# R762IT — Exact 48-event kernel for the six-axis k=0 Port–Euler observer

Date: 2026-11-22 (Asia/Shanghai). Scientific status: AUTHOR_PROVED / EXACT_FINITE_CERTIFICATES_REPLAYED / NOT_REVIEWED.
Frozen scientific source: `a72226e2430ffa4786321ac86e7f0c599d5f0389` (unchanged).
Predecessors: R762IR/R762IS, GitHub Draft PR #2946 @ `74e40c74cdebeab4e72cc3d814c35386ca060e44`; earlier GF(2) quotient R762IP and active-Port correction R762IO. This is independent portable source research, not a new shared TASK CLAIM.

## Precise model and theorem

Fix six labeled axes A={0,1,2,3,4,5}. The 15 Ports are unordered two-axis subsets; the 20 support types are unordered three-axis subsets. An event of support S chooses one edge between two of its three Ports. A legal closed Port history is a nonempty connected even-degree multigraph on its positive-degree Port set V; any p in V is an allowed specified Euler-circuit starting Port.

**Theorem (k=0 uniform 48).** For every support-multiplicity vector n with n_S in {0,1,2,3} and every legal realization with active Port set V and starting Port p, there is h with 0<=h_S<=n_S, exactly the same positive supports, h_S congruent to n_S modulo 2, and a legal Port realization with exactly V and p, such that **sum h_S <= 48**. The removed same-support event pairs can be reinserted along surviving legal edges.

Scope: the fixed composite six-axis Port–Euler observer. It does not assert native signed P000 Cell/Link/force/time/rotation transport or residual-fidelity lift. Full model with four-or-more event supports retains its earlier separately established bound of 54.

## Proof

R762IS proves an observer-preserving reduction to at most 49 events for all k=0 inputs. Choose one such witness. If it has at most 48 events, finish. Otherwise it has exactly 49, with at most ten supports of multiplicity 3. Since there are 20 supports and every other multiplicity is at most 2, equality 49 permits only the following two histograms:

1. Nine triple-event supports and eleven double-event supports (9*3+11*2=49).
2. Ten triple-event supports, nine double-event supports and one single-event support (10*3+9*2+1=49).

In particular every one of the 20 supports is present. Therefore the inactive Port set M must be a matching of K6: two inactive Ports sharing an axis would lie in one support S and leave S with fewer than two active Ports, contradicting the presence of an event of S. K6 has exactly 1+15+45+15=76 matchings (including empty).

**Ten-triple case.** If some triple-event support has only two active Ports, all three original events use their sole allowed edge and may be replaced by one. Otherwise every triple support is fully active. If its triangle is redundant in their union, apply the R762IR GF(2) connected-path parity correction to reduce it from three events to one. If all ten triangles are connectivity-essential, the exhaustive R762IR 10-subset theorem identifies their family as one of six complete axis stars. The R762IS star deletion proof requires only one unchanged event on a nonstar support to reconnect the omitted outer Port. Here there are nine doubled nonstar supports, so select one such edge and apply precisely the same 14-Port-core and GF(2) parity repair. The output has 47 events and exactly V.

**Nine-triple case.** Again, a triple support meeting only two active Ports reduces immediately; a connectivity-redundant full triple reduces by R762IR. It remains to consider nine distinct full, connectivity-essential support triangles. The exact `R762IT_NINE_TRIANGLE_ORBITS.cpp` checker enumerates all C(20,9)=167,960 families, identifies exactly **240** all-essential families, and partitions them into **two S6 axis-permutation orbits of sizes 180 and 60**. The representative support-index bitmasks (lexicographic triple order) are respectively `967489` and `971528`.

For each representative F, each of the 76 possible matching inactive sets M and its fixed reduction support j (index 0 for mask 967489; index 3 for mask 971528), the independent exact certificate `R762IT_47_CERT_CHECK.py` contains a 47-edge multigraph with:
- support multiplicities h_j=1, h_S=3 for the other eight S in F, and h_S=2 for all eleven S not in F;
- every edge assigned to a valid pair of active Ports of its support;
- all and only the requested active Ports of strictly positive even degree;
- connected active graph.

The checker replays **all 152 cases**, verifying each support count, incident degree, exact active set and connectivity with integer arithmetic; no mixed-integer optimizer is required to verify the certificate. Any essential nine-family is the S6-image of one of the two representatives, and any matching M becomes one of the 76 checked matchings under the same permutation. Relabeling the stored witness produces a legal 47-event witness for the actual F,M. For a chosen p in V a connected even-degree graph admits an Euler circuit beginning at p. This completes the nine-triple case, and thus proves the 48-event theorem.

This proof uses finite computer-assisted orbit and witness lemmas whose complete domains and replay sources are included. It does not claim a human-only proof of the 240-family classification or 152 certificate instances.

## Exact evidence and validation

- `R762IT_NINE_TRIANGLE_ORBITS.cpp`: exhaustively scans 167,960 nine-support subsets and every support removal, builds connected-component partitions on all 15 Ports; performs all 720 axis permutations to classify the 240 all-essential cases into 2 orbits of sizes 180 and 60. Independent of R762IR's previous ten/eleven-subset census.
- `R762IT_47_CERT_CHECK.py`: self-contained Python 3 standard-library replay, 152 stored exact witnesses for all matching inactive sets of both orbit representatives; certificate payload decompressed size 3,344 bytes; SHA-256 `30d13b776c596bc90a78fb62294c6dff070d3b48ff5edba2dbb2daceb809be5a`. Each instance has 47 events and passes positivity, even-degree, support parity, exact V and graph connectivity checks.
- Both checkers were executed locally on 2026-11-22. C++17 census: `all-essential9=240; star-subsets=60; nonstar=180; orbit_count=2`. Python replay: `PASS R762IT, 152 certificates`.
- The actual certificate construction used SciPy's integer MILP to find one witness per case; its verifier does not depend on SciPy or optimization heuristics. The proof is by the independently checkable saved finite certificates.

## Open frontier

The k=0 uniform upper bound is now **48**, not yet shown optimal. Analyze the remaining 48-event terminal histograms (10 three-event supports plus eight double and two single, 9 three-event plus ten double and one single, 8 three-event plus twelve double, and other feasible support patterns) to decide whether they reduce to 46 or yield a 48-event lower-bound certificate. For the whole Port model, independently analyze critical four-event supports (k>0), where the existing global upper bound remains 54. A native signed P000 TRIADIC_CLOSURE_E preservation lift remains a separate, typed research obligation.

Contribution: portable research of this logical conversation; prior researcher identity EM-DIRECT-CF96E0 is historical provenance, not presumed live capability. Independent mathematical review: NOT_REVIEWED. No protected PROGRESS/Result/Review has been written by this publication.
