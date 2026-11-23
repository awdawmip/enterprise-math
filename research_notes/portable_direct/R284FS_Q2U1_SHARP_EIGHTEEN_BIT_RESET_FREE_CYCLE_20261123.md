# R284FS — 跨代漏写四代循环 (q,u)=(2,1) 的十八位全局锐容量

Date: 2026-11-23 (Asia/Shanghai)
Status: EXACT_FINITE_PROOF / AUTHOR_RECALCULATED / NOT_REVIEWED
Mode: informed TASK_RESEARCH, portable independent science. No shared CLAIM; no formal Result/independent Review; P000 and original R284CO frozen science pins unchanged.

## Main theorem

Use the fixed four-code binary cyclic observer model of R284FM/R284FQ/R284FR: c0→c1→c2→c3→c0; each update writes each nominally changing coordinate once, with no more than q=2 omissions; old omitted writes can remain across arbitrarily many generations; each stateless read has at most u=1 independent bit flip. Stable phases must be decoded correctly, no third phase may succeed during a non-atomic publication, and a reader must never observe new-phase success then old-phase success on a paused physical prefix.

**Theorem R284FS-1 (exact global capacity).**

    n_min(q=2,u=1) = 18.

R284FQ and R284FR jointly exclude all tag widths <=16. The new finite obstruction excludes **all 17-bit encodings and all their per-edge bit-write orders**. R284FE's two independent nine-bit repeated Gray groups give an 18-bit legal upper construction (two groups, each K=2q+4u+1=9). Equality follows. The optimization is global over arbitrary four fixed binary tags under the stated model, not limited to Gray/separable encodings.

## Complete reduction for width 17

Complement individual columns to normalize c0=0. Delete constant columns, which preserve no observer distinction; a minimal-width counterexample cannot need one. Each of the 17 columns has one of seven patterns p in 1..7, specifying (c1,c2,c3) with c1 least-significant. Permutations within a pattern do not alter reachability or existence of a legal bit order. Thus the complete code space up to coordinate permutation is the nonnegative seven-vector x=(x1,...,x7) summing to 17, with

    binomial(23,6) = 100947

histograms. Four adjacent distances must each be >=2q+4u+1=9 and the two opposite distances must each be >=2(q+u)+1=7; exactly 3955 histograms pass these six necessary inequalities.

Apply R284FM's exact residual-flow cut separately to each phase pair i,j: an eight-vertex bipartite multigraph G_ij built from the last nominal updating edge of each differing bit has separated radius-one stable observations iff some vertex set V has internal multiedge count

    E(V) > q*|V|+2u = 2*|V|+2.

Checking all 255 nonempty vertex subsets of each graph leaves exactly **208** histograms. These are still candidates, not certified protocols.

## Exhaustion of publication prefixes

For each remaining histogram, construct all four exact stable state sets S_i as bit-masks differing from codeword c_i on at most two coordinates in **each** last-change group. The R284FM all-history reachability lemma proves this product equals the entire stable state set after arbitrarily many cycles; no finite-history cutoff is used.

For physical prefix word w define the exact **forced success phases**

    F(w)={j: d_H(w,S_j)<=2}.

A phase j in F(w) has an observation within one bit of w also within one bit of some stable S_j, so stable-read correctness forces success j. If any prefix on edge i→i+1 has a forced third phase, correctness fails. If F(w) contains both i and i+1, independent noisy reads while the writer is paused can return new success followed by old success, violating anti-rollback. Hence any correct prefix w necessarily satisfies

    F(w) subset {i,i+1}, and |F(w)|<=1.

For each proposed attempted-bit subset A in the current edge, every source physical word s in S_i and every current omission set M subset A with |M|<=2 produce

    w = (s & ~(A\M)) | (c_(i+1) & (A\M)).

Because columns with the same pattern are exchangeable, only the attempted counts t_p matter. Each possible bit-write order maps to a path of unit increments through a finite product lattice of these counts, and every path node must satisfy the above necessary condition for **all** its physical prefixes and omissions. The R284FR program uses exact bitmask Hamming radius-two dilation to compute F(w), then a BFS to decide if there is *any* path through the locally safe count vectors. Passing this necessary test does not assert existence of a complete protocol; failure rigorously excludes it.

Of the 208 stable-separated histogram candidates, **197** have no locally safe prefix path on edge 0→1. Exactly eleven have a possible safe path on that edge, enumerated as:

    (0,0,0,0,9,7,1)
    (0,0,0,0,9,8,0)
    (0,0,0,0,10,7,0)
    (0,0,0,1,8,7,1)
    (0,0,0,1,9,7,0)
    (0,0,1,0,8,7,1)
    (0,0,1,0,9,7,0)
    (0,0,5,0,6,6,0)
    (0,1,0,0,8,7,1)
    (0,1,0,0,9,7,0)
    (1,0,0,0,9,7,0).

**All eleven fail on the next edge 1→2:** its attempted-prefix lattice has no fully safe path for any of them. Therefore none of the 100947 width-17 histogram classes can yield a correct protocol. Combining the earlier lower bound n>=17 with the 18-bit explicit upper construction proves n_min(2,1)=18. QED.

## Reproduction and status

The standard-library integer checker R284FS_q2u1_17bit_sharp_checker.py, in this directory, loads the sibling pinned exact helper R284FR_q2u1_16bit_obstruction_checker.py (published commit 47d7f7fa53fda4174ad72941960064f2f1061328; blob a2c9aec04d01814587ae9c664769b93d0fa817fd). It computes the full 17-bit histogram orbit, exact six-pair graph cuts, all-history stable states and all required prefix-lattice safety conditions. Actual local execution completed with output:

    n=17 histograms: 100947; distance-pass: 3955
    all six stable read cuts pass: 208
    edge 0->1 safe-prefix-path survives: 11
    edge 1->2 safe-prefix-path survives: 0
    No correct 17-bit q=2,u=1 protocol.
    Using R284FR (n>=17) and R284FE 18-bit construction: n_min(2,1)=18

This is an exact finite proof that relies on previously documented R284FM reachability and flow-cut lemmas, R284FQ/FR smaller-width exclusions and R284FE's legal construction. It is **AUTHOR_PROVED / EXACT_LOCAL_CHECK_PASSED / NOT_REVIEWED**; no independent reviewer has yet validated the finite certificate or upstream dependency proofs.

Frozen source chain:
- R284FR proof@3b69b297b1da4d6b201e190f1a5e369b1db7a6df; checker@47d7f7fa53fda4174ad72941960064f2f1061328.
- R284FQ@5ee9ad22baf8ac68e942743960859abda863cb02.
- R284FM@1d1c5dd412719c7aaf016187b6493b77253cd9f9.
- R284FE@9974b3b5a1031bb5c841ab5a4950a9c55baed9e0.

## Continuation questions

1. Seek an analytic (non-enumerative) obstruction explaining 18-bit sharpness at q=2,u=1 and potentially a general all-(q,u) capacity theorem.
2. Independently audit R284FM's residual reachability, the forced-phase radius-two observer argument and the R284FR/R284FS count-lattice symmetry/exhaustion. Distinguish independent Review from author computation.
3. Pursue bank-data omissions and stale-reader lag H as separate typed extensions, preserving the original frozen code model.

No change to P000, the six native X6 spatial axes, BRC primitives, shared owner rights, or formal task Result is implied.