# R762IY — Star-leaf parity repair closes the (10,7,3,0) 47→45 Port–Euler class

Date: 2026-11-22 (Asia/Shanghai). Original frozen scientific input: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389` (unchanged). Based on R762IX (PR #2956, `82ded772793edd001f0c68e7d393b7a75e68bb6f`) and R762IU (PR #2950). Status: **AUTHOR_PROVED / EXACT_CONSTRUCTIVE_FINITE_CHECK / NOT_REVIEWED**.

## Model and question

Let the 15 Ports be two-element subsets of `A={0,1,2,3,4,5}`, and the 20 supports be three-element subsets. An event assigned to support `S` joins two of the three Ports within `S`; parallel edges are allowed. A legal closed history is a connected multigraph of positive even degrees on its prescribed active-Port set `V`, with an arbitrary chosen Euler-circuit start `p∈V`. Changing any one support count from 3 to 1 removes two events and preserves its parity and positivity.

The previously open terminal multiplicity class `(t,d,s,z)=(10,7,3,0)` has ten supports of multiplicity 3, seven of multiplicity 2, three of multiplicity 1 and none absent, totaling 47.

**Theorem.** For any legal realization of that class on any specified active set `V` and start `p`, there exists a legal **45-event** realization on the same `V` and with the same positive supports and per-support count parities. The new support-count vector is obtained by replacing a *single* triple count 3 with 1. This theorem is internal to the **composite Port–Euler observer**, not a native signed P000 dynamics theorem.

## New analytic star-leaf lemma (no integer-program solver)

Fix an axis `c`; suppose each of the ten star supports `{c,a,b}` has count exactly 3 and all fifteen Ports are required active. Choose a star triangle `J={c,a,b}` and its peripheral Port `v={a,b}`. If at least **one** nonstar support `Q={a,b,d}` (`d≠c,a,b`) has a positive count, while all other nonstar counts are arbitrary nonnegative integers, then there exists a legal Eulerian realization with the original nonstar counts and all star counts 3 except `n_J=1`. Its active set is all fifteen Ports.

**Construction and proof.** Relabel `(c,a,b,d)=(0,1,2,3)`. The Port `v=12` is the unique Port omitted by all nine star supports other than `J=012`. The full triangle-edge union of those nine star supports connects the other fourteen Ports `U=P\\{12}`: its central Ports `0i` form `K_5` with only edge `01–02` removed, and each other peripheral Port `ij` is attached to `0i` and `0j`. Thus the retained-star graph on `U` is connected.

Give `J=012` its one remaining edge `01–12`. For the nonstar auxiliary `Q=123`, choose one edge `12–13` and place its remaining `n_Q-1` events on the edge `13–23`. Every other nonstar support containing Port `12` sends all its events along its edge between the other two Ports, avoiding `12`. For other nonstar supports, choose any permitted edge and place all their events there. This yields `deg(12)=2`, and `12` is connected to the rest via both `01` and `13`.

For each of the other nine star supports, initially select its three distinct triangle edges, which form a connected cycle and give degree parity zero at each of its Ports. Let `q` be the degree-parity defect produced by the one-edge `J` and all nonstar edges. We already have `q_{12}=0`; since every edge contributes two endpoints, `sum_{x∈U} q_x=0` in `F₂`. Because the retained-star edge union on `U` is connected, its edge-boundary vectors `e_x+e_y` span every even-parity vector on `U`. Select a path decomposition of `q` in that graph, and group the selected path edges by supporting star triangle. Each group's boundary is an even vector on its three Ports, hence either zero or a pair `e_x+e_y`.

A triple-support triangle `(x,y,z)` realizes boundary zero while staying connected by its three distinct edges; it realizes boundary `e_x+e_y` while staying connected by **one** `xy` edge and **two** `xz` edges. Reassign each retained star's three events to realize its grouped boundary. All degrees become even. All fourteen Ports in `U` remain connected by the locally connected nine retained triangles, and Port `12` remains attached. Every required Port has positive degree, event counts are exact, and the 45-event graph has an Euler tour from any selected `p`. The proof applies without a solver and allows arbitrary positive `n_Q`.

## Discharge the full (10,7,3,0) class

Let `T` be the ten triple supports. If a `j∈T` has exactly two active Ports, all its three events are parallel on the one allowed edge. Remove two copies; this preserves a surviving edge, degrees' parity, connectivity and positive support.

Otherwise every `j∈T` is fully active. If some support triangle is not connectivity-essential in the triangle-union graph `G(T)`, apply the explicit GF(2) parity-routing reduction lemma proved in R762IX, which replaces one 3-count with 1, adjusts retained 3-count triangles and preserves the exact active set.

If all ten triangles are essential, the exact complete `C(20,10)=184,756` ten-support classification from R762IX_TEN_TRIANGLE_CLASSIFY.py identifies exactly the six full axis stars. Every Port belongs to at least one fully active star triangle, so `V` is necessarily all fifteen Ports. All ten nonstar supports are present (seven double, three single), hence every candidate star leaf `v` has three positive nonstar supports containing it. The new star-leaf lemma applies directly.

These three cases are exhaustive, proving the claimed 47→45 compression. This result reuses the exact ten-triangle classification and general nonessential-support reduction; those dependencies have author-side exact checking but not independent mathematical review.

## Stronger consequence for already solved predecessor class

For the earlier `(10,8,1,1)` 47-event class, an all-essential star still has **at least two** positive nonstar supports through every leaf, since only one of the ten nonstar supports is missing. Therefore the same analytic lemma replaces the separate 540-case star-witness enumeration in R762IX's last branch. This is a shorter proof of the *same* 45-event conclusion; it is not a second new theorem about that class.

## Exact check, scope and next question

The accompanying `R762IY_STAR_LEAF_VERIFY.py` implements the construction with `c=0,J=012,Q=123`, and covers every one of the `C(10,3)=120` choices of three singleton nonstar supports in the newly resolved class. Exact integer assertions check all 20 support counts, full 15-Port positive even degrees, and connectivity. It returned `PASS` on 2026-11-22; distinct used edge counts ranged **31–38**, maximum vertex degree **10**. By `S_6` axis relabelling, `c=0` covers all six possible star centers. The handwritten proof covers all allowed chosen star triangles, so the finite check is a supplementary cross-check rather than a logical substitute.

The earlier global `k=0 ≤47` author-side conclusion is unchanged. The remaining terminal `47→45` classes include `(8,11,1,0)` and `(9,9,2,0)`, while `(7,13,0,0)` and `(9,10,0,1)` have separate prior evidence. Determine whether every 47-event terminal class has a 45-event witness; then a uniform `k=0≤46` bound would follow using the prior reduction.

Provenance: independent portable research using the task's existing scientific input pin; no current task CLAIM/PROGRESS or mathematical Review is implied. Research identity, Activity and live ownership are tracked separately.
