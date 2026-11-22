# R762IN addendum — six inactive Ports despite 54 original events

Date: 2026-11-22 (Asia/Shanghai). **AUTHOR_PROVED / EXACT_FINITE_CROSSCHECKED / NOT_REVIEWED**.

Frozen model: six-axis composite Port-Euler observer, science pin `a72226e2430ffa4786321ac86e7f0c599d5f0389`. Read with [R762IN full-support theorem](R762IN_FULL_ODD_SUPPORT_SHARP_20.md) and predecessor [R762IM](https://github.com/awdawmip/enterprise-math/blob/b5e3a6073c54d1bbccd3a5d798887def7243a34c/research_notes/portable_direct/R762IM_K0_EVEN_TAIL_52.md).

## Exact correction and constructive witness

Let A = {0,1,2}, B = {3,4,5}. Among the 20 three-axis supports set `n_012=n_345=0` and all other 18 supports have multiplicity 3. Total original events are **54**.

The six pair-Ports internal to A or B, `01,02,12,34,35,45`, are declared inactive; the nine cross pair-Ports `03,04,05,13,14,15,23,24,25` are active. Each of the remaining 18 supports is of type two axes from A and one from B, or vice versa. Its three pair-Ports consist of exactly two cross pair-Ports and one internal pair-Port. Assign all three named events of that support to the unique edge connecting its two cross pair-Ports.

The resulting weighted Port multigraph is the 3-by-3 rook graph `K3 □ K3` with 18 simple edges, each of multiplicity 3. Every one of its nine active vertices has degree 12. It is connected, all degrees are even, all 54 events are used on valid support edges, and exactly **six Port vertices are inactive**.

Remove two parallel events from any one support. That support still has an event on the same edge, so connectivity, active vertices and even-degree parity are preserved. This supplies a **52-event** witness with the original support positivity and parity (and any chosen active start Port). Thus this is a counterexample to R762IM's *assertion that an original 54–60 event terminal histogram can omit at most one Port*, NOT to its existential 52-event statement.

## Exhaustive necessary inactive-set census with exactly two absent support types

For any proposed set M of inactive pair-Ports, every **positive** triple support S must have **at most one** of its three pair-Ports in M: any allowed event edge has two endpoints, so it cannot avoid two inactive vertices. This necessary incidence condition can be tested with 15-bit masks. Define `F(M)` as all triple supports whose triangle contains at least two inactive pair-Ports. Such a set M requires every support of F(M) to have zero multiplicity.

Enumerate all `2^15=32,768` Port-inactive masks M, and all `C(20,2)=190` choices T of exactly two zero supports; retain M only when `F(M) ⊆ T`. The accompanying **executed** standard-library Python checker verifies:

| Zero-support arrangement | Number of labeled arrangements | Maximal inactive Port count allowed by the necessary incidence condition |
|---|---:|---:|
| Two complementary, disjoint triples | 10 | 6 |
| Two intersecting triples | 180 | 4 |

Across masks with at most two forced-zero supports, the numbers by inactive Port count 0 through 6 are **1,15,105,395,330,60,10**; none has 7 or more inactive Ports. These maxima are **incidence upper bounds**; no assertion is made that every upper bound 4 case has a legal Euler realization. The 6-Port bound *is* attained by the explicit 54-event Euler construction above.

The classification is exact and finite because every potential inactive set corresponds to exactly one 15-bit mask and the condition is tested for all 20 support triangles. All arithmetic is integer; no floating point, optimizer or probability is used.

## Evidence, implication and next step

Execute `python3 research_notes/portable_direct/R762IN_OMITTED_PORT_CENSUS_CHECK.py`. The local run returned `PASS R762IN_OMITTED_PORT_CENSUS` and independently checked the above 54-event graph, connectedness, 9 active vertices, six missing, every active degree 12 and the immediate 52-event reduction.

The previous R762IM 3,165-case census is a strict subset of the possible original active-set cases, and its completeness claim is withdrawn pending a corrected count and certificates. Existing verified source artifacts remain preserved as their historical claims; the present note does not rewrite or promote them. To recover the full R762IM theorem, redo the active-set classification for each of its 14 upper-tail histogram families and construct a 52-event witness for each *realizable* active set, or isolate an actual obstruction. The global 54-event bound and its k>=1 unresolved sharpness question retain their prior research status. This is an observer-scoped mathematical correction, not a native P000 rewrite or physical assertion.
