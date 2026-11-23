# R762JZ — All-active 42-event Euler theorem for all five-singleton inventories

Date: 2026-11-23. Author-side exact finite constructive theorem; independent review **NOT_REVIEWED**. Predecessor: R762JY, `awdawmip/enterprise-math@3d230a3d4cf5436cdf2f98aeee3670e12fb88d0c`, Draft PR #3002. Task context: RS-X6-TRIADIC-CLOSURE-DYNAMICS. Frozen P000 unchanged.

## Exact model and theorem

Let A={0,1,2,3,4,5} denote six *axis labels*. The 15 composite Port vertices are P=C(A,2); the 20 event colors are S=C(A,3). A color t={a,b,c} permits precisely the three unoriented edges between vertices ab, ac and bc. Repeated colored edges are allowed. This is an **unsigned composite Port–Euler observer**, not a primitive signed P000 force event.

Choose **any** D⊂S with |D|=5 and **any** T⊂S\D with |T|=7. Prescribe n_t=1 for t∈D, n_t=3 for t∈T, and n_t=2 otherwise. There are 5+7×3+8×2=42 events.

**Theorem JZ.1.** Every such (D,T) admits a connected multigraph on all 15 composite Ports with exactly the prescribed colored edge multiplicities, legal endpoints, and strictly positive even degree at every Port. Hence a 42-event Euler circuit exists starting at **any** Port.

**Corollary JZ.2.** For any one of the five singleton colors j∈D, add two copies of its realized legal edge. This yields a valid **44-event** multigraph with color histogram (8 triple, 8 double, 4 singleton, 0 absent); removing those two marked copies gives the original 42-event circuit. The exact labeled target count is C(20,5)×C(15,7)=**99,768,240**. Keeping the selected removable color j as a mark yields **498,841,200** distinct marked target specifications (D,T,j), without asserting that all unmarked 44-source multigraphs are different.

## Constructive finite proof

We retain the explicit R762JY GF(2) parity construction. The new assertion is its **universal success for all D and T when no Port is inactive**, established by an exhaustive symmetry-reduced finite proof.

For fixed D, build graph G_F using all three candidate sides of every non-singleton color, and contract its connected components. Exhaust all legal choices of one edge for each singleton, retaining exactly those choices that connect the G_F quotient. This uses at most 3^5=243 candidate tuples.

For fixed T, build H_T from all candidate sides of the seven triple colors. Contract H_T components to obtain quotient Q. Define ∂_Q(uv)=[Q(u)]+[Q(v)] in GF(2). For each double color, selecting two of its three triangle sides has parity boundary equal to the boundary of its *missing* side. XOR dynamic programming over the eight double colors determines the exact set of reachable quotient boundaries. Select one connected singleton choice and double-side choices that cancel the total Q-boundary.

The remaining vertex parity lies in the image of the candidate sides of the triple colors. Solve the GF(2) generator system exactly. Every per-color correction is either zero or the boundary of one side of that color's triangle. Realize correction zero with all three triangle sides; realize a nonzero correction ∂(uv) with uv once and *another* side twice. Both use three events and keep the color's triangle connected. The resulting multigraph has correct multiplicities, even degrees, full connectivity, and positive degree on every Port. An independent event checker recomputes all legal colored edges, 42 event counts, vertex degrees and DFS connectivity; it does not trust the builder's return flag.

To prove that the required choices exist in **every** case, enumerate the S6 orbits on all 15,504 five-element D subsets. Applying all 720 label permutations and repeatedly removing the orbit of the least remaining D produces **exactly 43 disjoint orbits** whose sizes sum to 15,504. Each orbit has one representative. For each of these 43 D values, enumerate **all** C(15,7)=6,435 disjoint seven-element T values. The exact constructor succeeds and the independent checker accepts **all 276,705 representative cases**. A six-axis label permutation bijectively transports each legal Port, color and edge, preserving event multiplicities, positivity, evenness and connectivity. Thus the representative construction extends to all 15,504×6,435=99,768,240 labeled targets. Euler's finite connected-even multigraph criterion completes the proof.

This is an exact **finite proof by exhaustive constructive computation**, with the full executable finite argument and each case's deterministic witness recoverable from the code. No floating-point tolerance or probabilistic sampling is involved.

## Verified computation

| Orbit indices | D representatives | Exact representative targets | Valid witnesses | Transported labeled targets |
|---|---:|---:|---:|---:|
| 0–19 | 20 | 128,700 | 128,700 | 44,401,500 |
| 20–39 | 20 | 128,700 | 128,700 | 47,258,640 |
| 40–42 | 3 | 19,305 | 19,305 | 8,108,100 |
| **Total** | **43** | **276,705** | **276,705** | **99,768,240** |

Reproduction: `python R762JZ_M0_ALL_ORBITS_VERIFY.py --start 0 --end 20`, then `--start 20 --end 40`, then `--start 40 --end 43`; Python 3.10+ standard library. The three full input/output records and their framed witness-stream SHA-256 values are preserved in `R762JZ_EVIDENCE.json`. Run without arguments to check all 43 orbits at once.

## Scope, lineage and next

This extends R762JY's four fixed (inactive Port matching, D) slice families to **every** D,T combination with **no inactive Ports**. It neither changes P000 nor identifies these unsigned graph edges with primitive signed `TRIADIC_CLOSURE_E` Cell/Link/Port updates. The order of an Euler walk and BRC branch provenance are not recovered from a terminal multigraph. Independent mathematical review: **NOT_REVIEWED**.

Next investigate one-inactive-Port (M,D) orbit classes, whether the all-T existence theorem survives, and a symbolic certificate replacing the 43×6,435 exact enumeration; separately construct a source-faithful signed native lift and preserve required ordered BRC residuals.
