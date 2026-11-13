# Stage464-B — Three-POP exact future equivalence and polynomial BRC class counting

Date 2026-11-06; author-side result, awaiting independent review. Researcher-ID EM-DIRECT-7121CD, Research-Activity-ID RA-7716487BC36F1978CEAA8DD0.

## Frozen input and observer

Continuation of Stage463-B commit 05bde8e60d66e3fefdf5549cba205f80c064a356. Science pins: global bf84bd7c61a2444b59b1da96be57df0e9ae47e53; EM 2af3fc484eb11060b69e0afc1b562bcaf5ad1419; P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Current operational rules were read separately from current main.

Two source-distinct ordered original histories P,Q use the A=+E1/B=-E1 native-X6 subalphabet; 2<=m=|P|<n=|Q|, ends A, no adjacent interior B. Full initial observer includes source identity, lengths, exact signed Z^6 endpoints, full directed 12×12 adjacency counts, and overlap match count K. Fixed observation fibers are indexed by (kP,kQ,d), where kP/kQ count B defects, d counts mismatch positions in the initial overlap. This characterizes the full initial observer since isolated B with fixed A ends gives AB=BA=k, AA=length-1-2k and endpoint length-2k along E1. Each original ordered pair retains positive unit BRC multiplicity.

Future labeled operations are at most three POPs per source, at most r APPEND_P(u) and s APPEND_Q(u), for arbitrary r,s>=0 and all twelve signed native directions u. POP may remove an earlier APPEND. Compare every intermediate observation in the complete labeled future tree, including empty prefixes.

## Theorem 464.1: exact repair key

Using one-based original positions and clipping invalid or fixed A endpoints, let

IP = {m-3,m-2,m-1} ∩ {2,...,m-1}
IQ = ({m-2,m-1,m} ∪ {n-3,n-2,n-1} ∪ {m+1,...,min(n-1,m+r)}) ∩ {2,...,n-1}.

Deduplicate and set R464=(P_i : i∈IP; Q_j : j∈IQ), in index order. In every fixed full initial observation fiber, for any finite r,s>=0, two pairs have identical complete labeled future trees if and only if R464 is identical. The partition is independent of s. The P growing probe saturates at r>=n-m-1.

Proof of sufficiency: every intermediate source word is a surviving original prefix followed by action-known appended letters. With <=3 source POPs, the last removed original letters and the predecessor needed to compute any lost directed adjacency are among the original terminal A and the three predecessors in IP/IQ. All new appended letters and their directed edges are known from the action word. K starts at its observed initial value: subtract original/original comparisons lost when the shared prefix shortens and add comparisons created by appends. P POP exposes comparisons only at original P indices m,m-1,m-2; P APPEND probes Q only at m+1,...,min(n-1,m+r). When Q POP and APPEND reach P's original positions, their indices are >=n-3>=m-2, hence are fixed terminal A or P predecessors in IP. All remaining original/original comparisons stay aggregated in initial K. The complete observer after any action word is therefore a function of its initial value, R464 and that action word. Induct over the action tree.

Proof of necessity: successive POP on either source removes a directed edge (predecessor,last-letter). Exact directed-edge count differences reveal each predecessor, recursively yielding the three source terminal predecessor letters wherever non-fixed and valid. After learning P's terminal letters, the decrement of K after one, two or three P-only POPs determines the binary Q symbol at original positions m,m-1,m-2 by equality with the known P symbol. Consecutive APPEND_P(A) reveal binary Q symbols at j=m+1,...,min(n-1,m+r) from incremental K. Thus the future tree reconstructs every coordinate of R464. Q APPEND cannot probe a further unknown original P position, because after three Q POPs the shortest possible original Q prefix has length n-3>=m-2 and the P letters at those positions are already learned by P POP. Boundary cases with empty prefixes/fixed A letters are covered by clipping. This proves the equivalence and s-invariance.

## Theorem 464.2: polynomial positive-integer BRC counting and rank

Let W be IQ (visible Q positions). W has at most two contiguous components: near-overlap/P probe and terminal Q POP window. Let sigma retain the <=3 P terminal bits, every visible Q bit in the P original overlap (<=3), and first/last bits of each contiguous visible Q component (<=4). Thus |sigma|<=10 independently of n and r. Let v count B over visible Q positions W.

Use a positive integer transfer over original slots i=1..n, with state (a,b,e,lastP,lastQ,sigma,v) where a,b count B defects in original P,Q, e counts initial overlap mismatches, and lastP,lastQ enforce isolated defects. At fiber (kP,kQ,d) its terminal mass M(sigma,v) counts all ordered original source pairs (multiplicity preserved).

A second positive integer transfer over visible Q positions computes C(sigma,v), the number of legal visible bit strings consistent with the boundary bits, nonadjacent B in each component, and defect total v. Uniform completion lemma: all visible strings in one (sigma,v) group have the same number H(sigma,v) of compatible hidden pairs. The original paired P/Q constraints meet the visible Q string only at the <=3 overlap Q coordinates already in sigma; each hidden Q interval meets visible Q at its fixed boundary bits; all remaining influence on the original kQ count is v. Replacing one legal visible string by another in the same group preserves every constraint on the hidden pair. This provides an explicit bijection on hidden completions and proves H=M/C is a positive integer on supported groups.

Therefore qF=Σ_(M>0) C(sigma,v), total |F|=Σ M(sigma,v), and the exact population of each supported repaired key w equals H(sigma(w),v(w)). Prefix-constrained visible transfers calculate supported left-subtree class counts, so exact lexicographic rank/unrank uses O(|R464|) decisions and polynomially many integer additions without enumerating keys. A conservative paired-transfer upper bound is O(2^10 n(|W|+1)(kP+1)(kQ+1)(d+1)) exact integer additions. Count bit lengths are O(m+n), hence polynomial bit complexity.

## Strict new witnesses

1. m=6,n=10,Q=A^10; P1=ABAAAA and P2=AABAAA. Both have full initial observer (kP,kQ,d)=(1,0,1), identical Stage463-B keys, and different P original position 3 (one-based). Three P POPs leave ABA versus AAB, with distinct signed endpoints and directed adjacency. The new third P predecessor coordinate is necessary.

2. m=7,n=15,P=A^7; Q1 has its sole B at position 2, Q2 at position 5. Both have initial (0,1,1), identical Stage463-B keys, but the third P POP gives different K increments from original position 5. The new Q comparison coordinate is necessary.

## Actual execution

The companion standalone Python 3 standard-library script implements the exact transfer, independent original-history enumeration, population/rank/unrank and a 12-signed-direction full-future oracle. Its actual run checked 54 small parameter configurations; 756 nonempty initial fibers; all 2898 supported classes and their population and rank/unrank; 11 separate future-tree configurations; 347 history-pair comparisons; 246573 memoized future states. All assertions passed. These finite verifications cover their declared cases; the statements for arbitrary r,s follow from the two proofs.

At (m,n,kP,kQ,d)=(64,80,15,17,1), class counts for r=2,8,16 were 153, 1258, 2450, with identical total original population 5061384194832966. At (25,38,5,7,1,r=8), qF=1089 and |F|=8407656.

## Next

Stage465-B: characterize arbitrary POP horizons (hP,hQ), especially n-hQ<m-hP where Q APPEND could probe earlier P positions. Develop an action-complete multi-direction symbol observer when original alphabet has >=3 signed X6 symbols (one equality probe against A is then insufficient), retaining BRC mass and source provenance.
