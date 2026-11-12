# R93 — Persistent certified-OUT interval index under exact rational edits

Date: 2026-11-12. **Status: author-side mathematical derivation and independently reproducible prototype; not a Task Result or review.** Scope: R90–R92 finite rational circular-source model, frozen science pin `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Previous exact frontier: [R92](https://github.com/awdawmip/enterprise-math/blob/c62ff06a7dae3d53b0bf1e6f1abbfb1be27b8716/research_notes/brc_s23_av_indexed_cross_interval_20261112_r92/PROOF.md).

## Exact question and BRC observer

R92 indexed an immutable collection of verified OUT rectangles, but dynamic versions rebuilt the interval index. Can we insert or remove a *certified* rectangle while retaining exact historical indexes, and recover exactly the same relevant rectangles for R90/R91 coverage pruning?

Keep the R92 source model, full source identities `(time,branch)`, exact signature `sigma=(j,x,a,b)`, parameter closed rational interval `I=[L,U]`, residue class `r mod 16`. Let each verified OUT box `C=(id,sigma,r,[u,v],[p,q])` state that every corresponding source time in `[p,q]` is OUT for every real parameter in `[u,v]`. Boxes are already mathematically certified: the index never manufactures certification. Membership has typed Boolean BRC support. Branch identity remains in the winner observer; an OUT index alone does not quotient winner identities.

## R93.1 — Persistent augmented AVL theorem

Fix a complete `(sigma,r)` key. Order boxes by the exact pair `(u,id)`. Each immutable AVL node stores its exact box, two child pointers, height, size, and

`min_lo(v) = min{u(C): C occurs in the subtree of v}`,
`max_hi(v) = max{v(C): C occurs in the subtree of v}`.

Both extrema are recomputed from the new node and its actual children after each path-copying insertion, deletion or rotation. Retain every old root. To retrieve candidates for `I=[L,U]`, skip a subtree only if `max_hi<L` or `min_lo>U`; otherwise visit descendants and emit a box iff `u<=U && v>=L`.

**Theorem.** For any finite history of exact key-unique insertions/deletions, every retained root retrieves precisely the boxes of that historical version whose closed parameter intervals intersect `I`. In particular, the resulting R89/R92 joint time-cover decision, whole-subtree OUT pruning and pointwise OUT pruning are identical to a full scan of that historical version.

*Proof.* An empty node is correct. For a leaf, its metadata equal its interval. Assuming exact child summaries, the min and max formulas are exactly the extrema over the parent subtree. Ordinary AVL rotations preserve the in-order box multiset; rebuilding every rotated node by the same formulas preserves exact summaries. Path copying changes only the new root's reachable graph and never mutates prior nodes. Thus by induction each root has the correct multiset and metadata. If `max_hi<L`, all boxes end before `L`; if `min_lo>U`, all begin after `U`. No eligible rectangle is pruned. Every visited rectangle is emitted exactly when its closed interval intersects `I`. Every discarded rectangle contributes no point in `I` to the R89 joint time-cover union. Therefore the exact closed-endpoint and open-cell midpoint cover test is unchanged. R90/R91 consume this identical OUT coverage, so their certified pruning and result recovery preserve their original semantics. QED.

**Important structural counterexample:** testing only a node's *own* parameter interval is insufficient to reject its whole subtree. A parent interval `[1/10,1/5]` can be disjoint from `I=[3/4,4/5]` while its left descendant has `[0,1]` and intersects `I`. The subtree `max_hi` prevents this false negative.

**Resource bounds.** At B boxes, AVL height and single edit path length are `O(log(B+1))` (exact-key comparisons). A single insertion/deletion allocates `O(log(B+1))` new nodes and retains all old roots. For B0 initial boxes and U edits, the retained node-count bound is `O(B0 log(B0+1)+U log(Bmax+1))` when the initial tree is formed by repeated inserts; live index node count remains B. A balanced bulk initial build can reduce initial allocation to O(B0). Query has cost `O(visited nodes + emitted boxes)`, with *worst case* O(B), not a universal O(log B+k) bound from the two coarse extrema. Exact rational comparison bit costs and box-certification costs are separate. No false claim about time over all parameter precision levels follows.

The index is separated by `(sigma,r)`: an OUT certificate may only serve its own signature and residue. The certified box is an immutable record; deleting it from a version changes the index's active set, not the historical fact of its mathematical validity. An archived root safely retains it.

## R93.2 — An explicit nondegenerate certified input family

Take `j=0, x=1/4, a=0, b=1`, with the directed half-open target arc `[0,{theta})`, and choose every real `theta in [0,1/1024]` and every real source time `t in [0,200]` (in particular, all integer times with `t = 0 mod 16`). The unwrapped source coordinate is `1/4+t theta`. It lies in `[1/4,1/4+200/1024]`, strictly inside `(0,1)` and strictly above `theta`. Thus the source never belongs to the target arc; at `theta=0` the arc is empty. **Every subrectangle of this rational Cartesian domain is a certified OUT box by elementary inequalities.** This is a nondegenerate, parameter-dependent arc for positive theta, so the validation does not rely on the everywhere-empty-arc shortcut.

For the prototype, generate 512 distinct certified narrow rectangles from this family. Perform 180 path-copied insert/delete edits, retaining 181 roots; compare 4 exact rational-interval queries per historical root against its independent version's full list. Each comparison checks exact returned box IDs, exact continuous time-range joint-cover semantics, and all rational interval endpoints/midpoints. Additionally check 13 residue-0 source times at 1025 rational grid parameters, with the analytic inequality supplying the all-real certification.

## Actual executable verification

Complete unchanged prototype: `check_r93.py.gz.b64` (decode base64 and decompress gzip). JSON data: `verification_r93.json`. Run:

```bash
python -c 'import base64,gzip;open("check_r93.py","wb").write(gzip.decompress(base64.b64decode(open("check_r93.py.gz.b64","rb").read())))'
python check_r93.py
```

Deterministic Python random seed 93012026. Observed: 181 historical versions, 724 full-scan vs indexed exact retrieval/cover comparisons; 512 initial boxes, 572 final; 1,935 path-copy node allocations across 180 edits (maximum 17 in one edit). The initial 512 insertions allocated 5,324 nodes; one complete rebuild of the last version allocated 6,011 nodes. On the measured process, 100 narrow interval queries took 26.548 ms for scanning and 1.832 ms for index retrieval. This is a single-process illustrative measurement, not an independently controlled full-stack speedup; all exact assertions passed. Raw numeric records and test scope are in JSON.

The programme validates the index's *certificate-preserving substitution*. R82's three-index production representation, R86's full winner-function implementation, bigint bit-cost instrumentation and memory-in-bytes accounting remain the concrete R94 end-to-end integration unit.

## Control and next

Current exact S23 publication/owner was not affirmatively established by this research; no shared CLAIM or Result is asserted. On this run, an attempted new native researcher session received `SESSION_ISSUANCE_QUOTA`, despite a preceding status reporting available job capacity; those are different mechanisms. The bounded inventory read gave a snapshot of NEEDS_DISPATCH tasks but did not grant ownership. Scientific work here is an author-side branch only. Preserve pinned science and existing author provenance. Next unit: integrate the exact persistent box tree into R91/R92's point/whole-interval pruning and compare cold/warm cost against R82/R86 with counting rational bit sizes and retained-node memory.
