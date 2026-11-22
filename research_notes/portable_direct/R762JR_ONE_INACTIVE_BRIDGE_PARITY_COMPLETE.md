# R762JR — One inactive Port: all forty rainbow-tree exceptions admit uniform 44→42 compression

Date: 2026-11-23 (Asia/Shanghai). Role: independent portable TASK research, no current protected execution right asserted. Status: AUTHOR_PROVED / EXACT_FINITE_CROSSCHECKED / NOT_REVIEWED.

Predecessors (immutable scientific source): R762JP/JQ in Enterprise Math Draft PR #2983, head 44bd1c27ea903d643964a92bc5e811684fb76680, with existing R762JQ 1100/1140-color result. Do not re-freeze or rebase this scientific pin. All statements are in the six-axis *composite Port–Euler observer*; signed P000 Cell/path/branch/time/BRC lift remains separate.

## Exact statement and quantifiers

Let A={0,1,2,3,4,5}, Ports P=C(A,2), support labels S=C(A,3). An event with support s joins two distinct Ports belonging to C(s,2); parallel events are allowed. Let m∈P be the sole inactive Port and V=P\{m}. Suppose the 20 support multiplicities are in the histogram (6,12,2,0): six triples, twelve doubles, two singles, with total 44 events. Fix ANY such configuration and ANY legal starting Port p∈V. Then for EACH triple support j for which the set D consisting of j plus the original two singletons lies entirely in one of the six-support wings determined by m, there is a valid 42-event Euler witness with multiplicities n−2e_j, exact V, support labels, multiplicity parity, and start p.

Equivalently: in the one-inactive-Port setting, the 40 sets D missed by R762JQ's support-rainbow spanning-tree criterion are all soluble, uniformly for every choice of the other five triple supports. Together with the R762JQ theorem for the other 1100 D, this proves:

**ONE-INACTIVE COMPLETE THEOREM.** For any such n with one inactive Port, any original triple j and any p∈V, N_(p,V)(n−2e_j)>0. In fact the compressed 42-event construction exists for each choice of three distinct singleton labels D and five triple labels outside D, subject only to the initial 44-event histogram. If an original 44-event Euler witness existed, it can be compressed; existence is stronger and does not depend on which witness is supplied.

## The bridge–forest–parity argument

By axis-permutation symmetry fix m={0,1}. The only supports containing m are four "bridges" {0,1,c}, c=2,3,4,5, each involving exactly two active Ports {0,c} and {1,c}. Their required event count is 2 or 3 in every exceptional D, so every such support FORCES a positive connection {0,c}—{1,c}. Parity at these endpoints is forced by its multiplicity mod 2.

The 16 supports not containing m divide into A-wing W0={0,c,d} (6 labels), B-wing W1={1,c,d} (6 labels), and core K={c,d,e} (4 labels), for 2≤c<d<e≤5. By exchanging axis names 0 and 1, assume D⊂W0 has exactly three colors, all of multiplicity one in the compressed target. Thus all six W1 labels and all four K labels are flexible, having count either two or three; the remaining three W0 labels are also flexible.

Select these NINE pairwise differently colored edges, each designated within the indicated flexible support:

- {1,2,3}: 12—13; {1,2,4}: 12—14; {1,2,5}: 12—15;
- {1,3,4}: 13—34; {1,3,5}: 13—35; {1,4,5}: 14—45;
- {2,3,4}: 23—24; {2,3,5}: 23—25; {2,4,5}: 24—45.

Here 12 denotes Port {1,2}, etc. Direct inspection: these nine edges form a tree on all ten Ports of the form {1,c}, c=2..5, and {c,d}, 2≤c<d≤5. Together with the four compulsory bridge links {0,c}—{1,c}, they form a spanning tree on all 14 active Ports, independent of multiplicity assignment.

There are exactly FOUR other flexible full supports: the remaining core support {3,4,5} and the three W0 colors outside D. For these four supports, allow all three possible local edge endpoint boundaries as GF(2) parity generators. For each of the nine designated tree supports, restrict to its designated edge boundary alone. Let H be the graph on 14 active Ports with the nine designated edges and the three edges of each of the four remaining flexible support triangles. Its 9-edge subgraph already connects the ten W1+core Ports. The three remaining W0 supports correspond to three edges of K4 on leaf Ports 02,03,04,05. A three-edge subgraph of K4 is either a spanning tree or a triangle plus one isolated vertex:

1. If it is a spanning tree, H is connected on all 14 Ports.
2. If it is a triangle and an isolated leaf Port 0x, H has exactly two components: the singleton {0x} and one connected 13-Port component. In this case D is the three W0 labels {0,x,y} with y ranging over the other three leaf indices. All three singleton support triangles contain 0x; each offers a local edge avoiding 0x and an edge incident with 0x.

**Local parity realization.** For any full support triangle with multiplicity c=2 or c=3, one can realize each of the four possible even endpoint-boundaries (zero or the boundary of any of its three sides), preserving exact c: for c=2, zero uses two parallel copies of an arbitrary side and a nonzero side-boundary uses the *other two* triangle sides; for c=3, zero uses the three sides once each and a nonzero side-boundary uses three parallel copies of the desired side. For the nine designated tree supports, the zero or designated-edge boundary realizations BOTH connect the endpoints of their designated tree edges. The four other flexible triangles realize every possible local even parity vector (there is no designated connectivity constraint on these four).

Initially realize the four compulsory bridge supports as their forced parallel edges and each D singleton as one local side. This produces an even-weight global boundary b∈GF(2)^V. All flexible supports have a zero-parity realization as baseline. The attainable changes to the total parity equal exactly the boundary span of H: for the nine designated colors, choose the designated edge vector; for each of the four other colors, choose any of its three edge vectors or zero. The sum of several edge vectors in a single triangle is still either zero or one triangle-edge boundary, hence realizable with one local support of count 2 or 3.

If H is connected, the incidence image is every even-weight vector on V, so choose flexible realizations canceling b. If H has the isolated leaf 0x, orient one of the D singleton events so that the total initial boundary at 0x is zero: choosing a side of this singleton triangle which avoids or meets 0x flips this bit. The total b is even, so its restriction to the 13-Port component of H is even and can be canceled by flexible supports. (The other two D singleton choices are arbitrary.) In both cases total parity becomes zero.

The designated nine tree supports always connect their designated tree endpoints, regardless of selected parity. Each compulsory bridge support connects its two active endpoints. Their 13 links constitute the above 14-Port spanning tree. The final multigraph is thus connected and has every active degree positive and even, inactive degree zero, correct positive support labels and exact multiplicities (3 singleton + 5 triple×3 + 12 double×2 = 42 events). Euler's circuit theorem provides a closed route starting at arbitrary p∈V. Relabeling covers D⊂W1 and any inactive Port m. QED.

## Exact independent integer recalculation

A deterministic Python-standard-library generator constructs explicit 42-event multigraphs and independently checks all 20 support counts, each active vertex's positive even degree, zero inactive degree, connectivity and 42-event total. The complete 40 exceptional D comprise 32 patterns with connected H and 8 star-D patterns with one isolated H vertex (both wing orientations counted).

The full run enumerates every five-triple inventory outside each three-singleton D: C(17,5)=6,188 inventories per D, 40×6,188 = 247,520 distinct labeled compressed inventories, all **PASS**. The deterministic SHA-256 of the concatenated sequence (D indices, extra triple indices, 60 per-support edge multiplicities) was:

41bfe6d509c22ef4b0559bb8549ecb26cbb8287dd7fbef1786639d87c5cfd0c8

A smaller 640-certificate check covers the 16 possible compulsory-bridge parity masks in each of 40 D; its stream SHA-256 was:

0a8016b0aef84f0c4445af37c918b405621b2ea35f7238fde520eb8e1fcf480c

The complete computation validates the precise finite domain claimed. The written construction proves the universal statement independently of finite runtime and of any floating-point solver. The complement R762JQ 1100-pattern proof is reused at its pinned scope rather than recomputed.

## Scope, next question, and control separation

This closes **exactly one inactive Port** for the (6,12,2,0) 44→42 terminal class. Cases with two or more inactive Ports remain open. The overarching k=0 author-side upper bound stays 44 pending those cases and the other histogram classes. The earlier R762IR/reduction dependency remains under independent-review requirement. No P000 signed-state lift is claimed; the Euler support observer may forget path order/branch/time and BRC structural residuals.

New next scientific question: enumerate all legal inactive Port sets M with |M|≥2 for (6,12,2,0), seek compulsory-link + flexible-triangle boundary spanning criteria, and separate exact obstructions from insufficiencies of a chosen rainbow-tree method.

Researcher / Source status: independent portable author result. Current protected Task owner, run generation and CLAIM must be verified separately. Do not infer a current authority from past researcher names or published files. Activity linkage and protected PROGRESS not asserted by this document.