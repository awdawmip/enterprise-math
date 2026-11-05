# PREFIX-502 — Quartic-word exact index for dense BRC–KMP–source ranks

Date: 2026-11-05 (Asia/Shanghai). Researcher-ID: `EM-DIRECT-736D5C`; native research activity: `RA-FD11DD0C3EDBC881854C942F`. Independent author-side continuation. Formal CLAIM/Result/Review/Admission: not established.
Status: AUTHOR_PROVED / EXACT_INTEGER_CHECKED(n=0..9) / UNREVIEWED / NOT_ADMITTED.
Scientific input remains pinned to `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`. Current behavior rules were read separately from global `main@e44164377b61cc0a95dd87399db22e2f3d9cf653` and project `main@6cf6201460518e9d72500edd818441cb475e57ad`; this note uses the PREFIX-500 exact support theorem and PREFIX-501 quotient symmetry as proved author-side dependencies.

## Observer, alphabet and aim

Work in a declared five-axis path subfamily embedded in native signed X6 by fixing sixth-axis occupation to zero. Its ten letters are `a,A,b,B,c,C,d,D,e,E`, each a primitive signed native direction. For length n retain the signed five-axis displacement y, the exact BRC cancellation readings V=p_b+2p_d+p_e and W=p_c+p_e (p_i=min(positive occupation_i,negative occupation_i)), the terminal KMP state q for g in {aab,aba}, and the first B/C provenance label t in {N,B,C}. Future operations are native signed-letter appends. This exact observer is the target of compression, with its full KMP/provenance support preserved.

PREFIX-501 showed that the full (q,t)-support at a base fiber depends only on (u,v,c,s,W,V), where u=y_a, v=y_b, c=|y_c| and s=|y_d|+|y_e|. Let K_g(n,u,v,c,s,W,V) be that support set and k_g its cardinality (zero for infeasible data). PREFIX-500 supplies a constant-number-of-integer-operations exact membership oracle for K_g.

## Theorem — O(n^4)-word exact dense lex rank/unrank index

For every integer n>=0 and either fixed gate g in {aab,aba}, assuming the two predecessor exact support/symmetry lemmas, an explicit index of O((n+1)^4) integers can represent the dense lexicographic rank on all reachable (y,V,W,q,t) at length n. The lex order is (y_a,y_b,y_c,y_d,y_e,W,V,q,t). With this shared index and on-demand K_g membership:

* rank and inverse rank each use O((n+1)^2) support-oracle evaluations and O(log(n+2)) row comparisons plus O(1) other indexed integer operations per level;
* index precomputation uses O((n+1)^6) support-oracle evaluations and O((n+1)^6) word arithmetic operations;
* the individual state's exact minimum fixed-length representation is still ceil(log2 S_g(n)) bits, where S_g(n) counts its reachable joint observations;
* append of a signed primitive direction, followed by re-ranking at n+1, uses two such rank/inverse queries and the exact BRC/KMP/tag update, given the indices for n and n+1.

All bounds count exact integer word operations; operands have O(log(n+2)) bits. A bit-cost implementation additionally pays for these operands and for the exact kernel operations. The shared index is distinct from the per-state payload and from any validation-only explicit state set.

### Proof: the absolute-value convolution

Define, for L=n-|u|-|v|-c>=0,

    A(u,v,c,s) = sum_{W,V} k_g(n,u,v,c,s,W,V),  0<=s<=L,

with A=0 for parity-incompatible and other impossible s. Define its cumulative sum

    B(u,v,c,h) = sum_{s=0}^h A(u,v,c,s),  B(-1)=0.

Fix a signed d=y_d with h=|d| and e=y_e. The remaining signed e-domain is [-R,R] where R=L-h. Because the controller support is independent of the separate signed d,e decomposition and depends only on s=h+|e|, the total number of joint observations under this signed-d prefix is

    E(h)=sum_{e=-R}^R A(u,v,c,h+|e|)
        =A(u,v,c,h)+2[B(u,v,c,L)-B(u,v,c,h)].

Thus E(h) is an O(1) lookup/expression from the length-L B row, and the signed-d row (d=-L,...,L) is stored with exact prefix weights. For ranking the last signed coordinate e, the number of joint observations before e in its own row is

    P_e(e)=
        B(L)-B(h+|e|)                         if -R<=e<0,
        B(L)-B(h)                              if e=0,
        B(L)+A(h)+B(h+e-1)-2B(h)               if 0<e<=R+1,

where all B/A symbols share the fixed (u,v,c) prefix. The formulas count signed negative e first, then zero, then positive e in lex order. Each is exact even when some A values are zero. The row total is E(h). Inverse e selection uses binary search on nondecreasing row-ending prefixes P_e(e+1), taking the first e whose interval contains the remaining rank.

Summing the d row yields

    G(u,v,c) = sum_{d=-L}^L E(|d|)
             = A(u,v,c,0) + sum_{s=1}^L 4s A(u,v,c,s).

The equality follows by counting all signed integer pairs (d,e) with |d|+|e|=s: one at s=0 and 4s at s>0. Store signed prefix rows for y_c with weight G(u,v,|y_c|), then for y_b with the corresponding signed-y_c totals, then y_a at the root. These hierarchical signed-coordinate rows and the d row suffice to rank and invert the complete signed displacement y while preserving exact lex ordering.

After y is decoded, the residual rank runs over the actual W,V,controller choices. Set m=(n-|u|-|v|-c-s)/2, a nonnegative integer on every feasible fiber. Scan W from 0 to m and V from 0 to 2m using k_g to obtain their lexicographic prefix offsets, then choose the sorted (q,t) ordinal within the final K_g set. Each W block needs at most (2m+1) oracle calls, so both rank and inverse require O((n+1)^2) such calls. All consecutive blocks are disjoint and have total weight S_g(n), establishing a bijection with [0,S_g(n)).

The table A and its per-(u,v,c) B sums have O(n^4) entries because their indices are four bounded integers. Signed-d prefix rows also have O(n^4) entries; the y_c, y_b and y_a rows have O(n^3), O(n^2), O(n) entries. To populate A, loop over O(n^4) quotient (u,v,c,s) candidates and O(n^2) feasible (W,V) candidates; this is O(n^6) support-oracle work and needs no persistent K table. This finishes the construction and the complexity claim. QED.

### Resource tradeoff

Compared with PREFIX-501's O(n^6)-word shared weighted (W,V)-prefix index, this exact scheme stores O(n^4) words and computes the fine W,V block on demand. The predecessor supports O(1) rank table operations and O(log n) inverse comparisons; the new scheme trades O(n^2) exact support queries per rank/unrank for a lower shared memory asymptotic. Precomputation remains O(n^6) oracle evaluations. In a practical implementation, the preferable scheme depends on the number of online operations and the cost of the support oracle.

## Exact execution evidence

Published certificate: `research_notes/portable_direct/prefix502_quartic_compact_certificate.py`.
Published execution JSON: `research_notes/portable_direct/PREFIX502_COMPACT_EXACT_EXECUTION.json`.
Command: `python3 prefix502_quartic_compact_certificate.py 9`. Python 3 standard library with unbounded integers, bisect, set/dict and integer comparisons; no floats.

The self-contained published certificate independently advances every reachable native ten-direction state, constructs K and A via actual base-fiber support, checks quotient symmetry, builds the new A/B/signed-prefix index, then compares its rank and inverse for EVERY reachable joint state to an independently sorted full state list for every n=0,...,9 and both gates.

    n   aab joint states   aba joint states   new index words
    8          60,590             60,550            5,426
    9         127,403            127,298            8,004

The published index's word count excludes the full native states and explicit K dictionary used solely for the validation oracle. At n=9 PREFIX-501 reported 28,324 row entries (excluding its K payload); the new arithmetic-prefix index records 8,004 integer entries, including its A, B and signed rows. The two reports count distinct concrete index structures and do not measure total Python-process peak memory.

A separate expanded local checker also performed exact e-row convolution identities, complete native rank/inverse comparisons for n<=9, and crosschecked PREFIX-500's actual mod-12 oracle on all reachable quotient keys for n<=4. That expanded checker is supplied as an additional local evidence package; the exact committed compact certificate is self-contained and has itself run successfully. Both executions reported `ALL_CHECKS_PASS`.

## Source semantics, remaining question

BRC reuse: exact cancellation update (REUSE_APPLIED); fixed support oracle from PREFIX-500, Parikh quotient from PREFIX-497 and symmetric ordinal from PREFIX-501 (COMPOSE_APPLIED). This is a scoped exact compression of the declared X6 path observer. The signed axis-6 parent world, full path history, time and physical rotation remain typed separately. The formal rotation task `RS-X6-NATIVE-ROTATION-DYNAMICS` was read as READY/NEEDS_DISPATCH with unassigned Owner at the native control snapshot 2026-11-04T23:59:22Z; this research has no formal CLAIM.

Next PREFIX-503: derive batched W,V prefix counts from the constant-suffix/PRESBURGER support predicates, seeking O(n) or better query time while retaining O(n^4) shared memory; alternatively test a lazy cache under realistic rank/append workloads and record actual amortized throughput and peak memory. Preserve the exact source and future-operation observer during any further quotient.
