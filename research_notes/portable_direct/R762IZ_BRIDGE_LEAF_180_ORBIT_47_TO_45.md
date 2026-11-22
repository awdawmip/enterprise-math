# R762IZ — Bridge-leaf parity repair closes the 180-orbit all-essential nine-triple Port class

Date: 2026-11-22 (Asia/Shanghai).
Status: AUTHOR_PROVED / EXACT_FINITE_CROSSCHECKED / NOT_REVIEWED.
Scientific inputs remain frozen at \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`; no P000 revision or native signed lift is asserted.
Predecessors: R762IT (Draft PR #2947), R762IW (Draft PR #2954), R762IY (Draft PR #2958).

## Mathematical setting

Let \(A=\{0,1,2,3,4,5\}\), with 15 Ports \(P=\binom A2\) and 20 three-axis support types \(H=\binom A3\). A support \(S=\{a,b,c\}\) admits one event-edge between any two of its three Ports \(ab,ac,bc\). Parallel event-edges are allowed. A legal closed history is a connected undirected multigraph of strictly positive even degrees on its specified active set \(V\subseteq P\), with any prescribed Euler starting Port \(p\in V\). Each positive support has at least one event.

Write \(T\subset H\) for the nine support types with multiplicity 3. The remaining eleven support types have multiplicity 1 or 2, with exactly two singletons. Thus \((t,d,s,z)=(9,9,2,0)\) and \(\sum n_S=47\). A triangle family \(T\) is **all-essential** when removing any triangle strictly increases the component count of the full triangle-edge union graph on all 15 Ports.

## New theorem: the entire 180-member all-essential orbit compresses from 47 to 45

Suppose \(T\), up to a relabeling of the six axes, has the form

\[
T=\big(\{\{c,i,j\}:i,j\in A\setminus\{c\},i<j\}
\setminus\{\{c,a,b\},\{c,b,d\}\}\big)\cup\{\{a,b,d\}\},
\]

where \(a,b,d,c\) are distinct. Assume all eleven nontriple support counts are positive, as in the 47-event histogram. For every legal original realization with precisely active Ports \(V\) and specified Euler start \(p\), there exists a legal 45-event realization with the **same** \(V\), \(p\), positive support types and componentwise support-count parities, obtained by reducing exactly one triple support from 3 to 1.

The family is the 180-member \(S_6\)-orbit represented by the support index bitmask \(967489\) in lexicographic order, with canonical representative \(c=5\), \((a,b,d)=(0,1,2)\):
\[
T=\{012,025,035,045,135,145,235,245,345\}.
\]
The other all-essential nine-triangle orbit has 60 members and is the star-minus-one class resolved by R762IY.

### Proof

**Case 1: a triple support meets only two active Ports.** All three of its events must use the one edge joining those two Ports. Delete two of those parallel edges. One remains, preserving connectivity, positive degrees, even parity, the support presence and the Euler start. This gives 45 events.

**Case 2: all nine triple supports have all three Ports active.** Their union covers all 15 Ports (the eight retained star triangles cover 13 Ports and the bridge triangle supplies the two missing leaves), so the required active set is necessarily \(V=P\).

Relabel to \(c=5,a=0,b=1,d=2\), and set \(J=012\). Reduce the three \(J\)-events to the one edge \(01\!-\!12\). The remaining eight star triangles form a connected graph on
\[
W=P\setminus\{01,12\}.
\]
Indeed the central Ports \(05,15,25,35,45\) induce \(K_5\) minus edges \(05\!-\!15\) and \(15\!-\!25\), hence remain connected. Each remaining peripheral Port belongs to its retained star triangle and attaches to the central core.

To maintain both missing-star leaf Ports, use positive private nontriple supports \(Q_{01}=013\) and \(Q_{12}=123\). Place one \(013\)-event on \(01\!-\!03\) and one \(123\)-event on \(12\!-\!23\); place any remaining copies of those supports on their opposite edges \(03\!-\!13\) and \(13\!-\!23\), respectively. For every other positive support not among the retained eight star triangles or \(J\), put all its events on an edge avoiding \(01,12\). Such an edge always exists: the only support containing both leaf Ports is \(J\). The single \(J\)-edge and the two private nontriple edges give degree exactly 2 at each leaf, and connect each leaf to \(W\).

The initial multigraph formed by \(J\) and these eleven other supports has an even-cardinality parity defect \(q\in\mathbb F_2^W\) on \(W\). The eight retained star triangles span a connected edge graph on \(W\), so their edge-boundary vectors generate the entire even-parity subspace of \(\mathbb F_2^W\). Choose a path-routing of \(q\) through this graph and group the selected edge boundaries by their supporting triangles. Each grouped triangle boundary has either zero or two nonzero coordinates.

For each retained star triangle with Ports \(x,y,z\), exactly **three** event-edges can realize either boundary while keeping its three vertices connected: use the 3-cycle \(xy,yz,zx\) for zero boundary; for boundary \(e_x+e_y\), use the edge \(xy\) once and \(xz\) twice. Hence the eight full star triangles can be reassigned to cancel \(q\), preserving their support counts, positive Port degrees, and connectivity of the core.

Both leaves have degree 2 and attach to this connected core, so the resulting 15-Port graph is connected with positive even degrees. Its support counts equal the original ones except \(n_J=3\mapsto1\). Their sum is \(45\), and an Euler circuit starts at every requested \(p\in V\). All deletions are a same-support event pair; the opposite expansion restores the original 47-event count if needed. QED.

## Exhaustive verification and orbit coverage

The attached standard-library-only \`R762IZ_BRIDGE_LEAF_VERIFY.py\` performs:

1. A complete enumeration of \(\binom{20}{9}=167{,}960\) nine-support families using a 15-Port component test. Exactly **240** are all-essential.
2. An independent \(S_6\) orbit generation: the above bridge-leaf orbit has **180** families; the star-minus-one orbit has **60**; their disjoint union exhausts the 240 all-essential families.
3. The explicit construction for all \(\binom{11}{2}=55\) placements of singleton counts among the eleven nontriple supports in the full-active canonical case. It checks every support count, the precise 15-Port active set, positive even degrees, connectivity, and total 45 events. Axis-equivariance covers **180×55=9,900** labeled \((T,\text{singleton set})\) full-active cases. Case 1 handles every legally realizable proper active subset without any additional computational assumption.

Execution on 2026-11-22: **PASS** for all 55 construction instances and the complete 240-family census. Reproducible SHA-256 of the deterministic canonical JSON certificate list:

\`eff09ac6cf6b412385bb7ade59eae7e37a98680894f5e941e2f19acc82fc23ed\`.

No external optimization solver, floating point arithmetic or numerical tolerance is used. The author-side finite check is not an independent mathematical review.

## Consequences and remaining obligations

Combining this new 180-orbit construction with R762IY's 60-orbit star-minus-one proof resolves the **entire all-essential \((9,9,2,0)\) terminal class** at 45 events for any legally realizable active Port set. For non-essential nine-triangle families the previous R762IR connected-triangle parity-repair reduction remains the relevant author-side dependency. The broader \(k=0\le47\) upper bound is not strengthened by this class result alone. The \((8,11,1,0)\) terminal class, any remaining dependency checks for general non-essential triangles, and the separately typed four-or-more multiplicity and signed native P000 lifts remain open.

This is a composite Port–Euler observer theorem. It does not establish a native signed six-dimensional Cell/force/time/rotation representation preserving all residual provenance. Review status: NOT_REVIEWED. Formal Task CLAIM/PROGRESS and Activity association are separate from this scientific publication.
