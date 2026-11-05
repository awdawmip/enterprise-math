# Stage444-B — Polynomial exact support for the zero-mismatch two-source native-X6 family

Date: 2026-11-05. Parent: Stage443-B at adc82e1518c2cfe4cdb13e6522e42601f3db419e. Frozen scientific source pins (unchanged): GLOBAL bf84bd7c61a2444b59b1da96be57df0e9ae47e53; EM 2af3fc484eb11060b69e0afc1b562bcaf5ad1419; P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Mathematical status: author proof; independent review pending.

## Exact family and observer
Use A=+E1 and B=-E1, two of the twelve native signed X6 directions. Initial ordered P,Q paths of lengths m,n>=3 have A endpoints, kP,kQ internal nonadjacent B letters. The full observed O=(m,n,V_P,V_Q,J_P,J_Q,K) retains both six-component endpoints, both complete directed neighbor-pair histograms, and the number K of absolute-position letter matches over the first t=min(m,n) coordinates. Future legal operations are up to pP,pQ POP and rP,rQ APPEND per source, in any order, with any of the twelve native APPEND letters; compare O at every prefix.

Assume K=t, 0<=pP<m, 0<=pQ<n and all r budgets nonnegative. Define q_F as the exact number of present-fiber equivalence classes under every permitted future observation sequence, with q_F=0 if the original fiber is empty. BRC counts are exact positive unit-weight branch populations: Boolean support, integer population M and original-history provenance are distinct.

## Theorem 444.1 (exact shared-prefix factorization)
For K=t, future equivalence is precisely equality of the longer original path at a computable set U of observable indices, and the feasible visible strings split into independent prefix and tail sections.

Proof: assume m>=n, exchanging source names otherwise. K=n forces Q_i=P_i for all i<=n. Q's final A forces P_n=A. Therefore P is a concatenation of an n-letter prefix with kQ defects and a tail indexed n..m (the n-th A shared as a boundary) with kP-kQ defects; no cross-boundary B adjacency remains. At m=n the tail has one zero boundary and no defects. Stage439-B's exact future-repair key R=(S_P,S_Q,A_P,A_Q,E) has (i) equality observations E_i=1 identically and (ii) every variable raw-letter slot equal to the longer path's original bit at its index. Repeated slots and forced endpoint values are determined by the unique longer-path bits on U. Equality of these bits is thus equivalent to equality of R, which is, by the Stage439-B theorem, necessary and sufficient for equality of all future full O observations. Splitting U across the forced A at position n yields the independent sections. This theorem inherits the currently author-reviewed (not independently admitted) Stage439-B exact-key premise.

## Lemma 444.2 (nonadjacent hidden gap capacities and masses)
In a single section of length L>=2 with A endpoints, choose visible interior sites 1<a1<...<as<L, adding boundary anchors a0=1 and a(s+1)=L with v0=v(s+1)=0. Let g=a_j-a_(j-1)-1 hidden cells between neighboring anchor bits l,r∈{0,1}. If g=0 and l=r=1, that visible word is forbidden (consecutive B). Otherwise put h=max(0,g-l-r). The maximum number of B letters placeable in this gap is ceil(h/2), and *every* number from zero up to that capacity occurs. For a fixed number z the exact number of gap completions is binomial(h-z+1,z), 0<=z<=ceil(h/2).

Proof: any boundary B blocks only its adjacent hidden cell. For g>=1 the remaining unblocked sites form a consecutive run of length max(0,g-l-r), with the special case g=1,l=r=1 having zero free cells. The number of z-subsets with no adjacent elements in a run of h sites is binomial(h-z+1,z), by replacing increasing positions i_j with i_j-(j-1). Every z in the indicated interval is realizable. Distinct gaps have disjoint free cells, so their integer capacities add and all totals between zero and the sum are realizable.

## Theorem 444.3 (polynomial exact future-class support)
For one section of length L with k internal B letters, and visible set U, define F(L,k,U) to be the number of *distinct visible bit words* admitting at least one nonadjacent k-defect completion. For a chosen visible word, set c=number of visible Bs and C=sum of Lemma444.2 gap capacities. Feasibility is exactly: no forbidden zero-length gap, and c<=k<=c+C.

Count all feasible visible words without enumerating them using D_j(c,C,v): number of distinct visible-word prefixes through anchor j, with visible-B count c, aggregate hidden-gap capacity C, and last anchor bit v. Initialize D_0(0,0,0)=1. At the next anchor, choose w=0 or 1 (w=0 only for the final forced endpoint), calculate gap capacity G(g,v,w), reject forbidden adjacency, and update

 D_(j+1)(c+w,C+G,w) += D_j(c,C,v).

At the last anchor sum D_(s+1)(c,C,0) over c<=k<=c+C. This counts visible words, not hidden paths: each visible word has exactly one sequence of chosen anchor bits, and aggregation combines integer counts of those distinct words.

For m>=n let (L0,k0,U0)=(n,kQ,U_pre) and (L1,k1,U1)=(m-n+1,kP-kQ,U_tail). If m=n the tail factor is 1 for k1=0. Then

 q_F = F(L0,k0,U0) F(L1,k1,U1).

The symmetric case n>m follows by exchanging P and Q. There are O(L^2) (c,C,v) states per layer and O(L) visible anchors; the computation uses O(N^3) exact integer additions and O(N^2) active cells with N=max(m,n). Counts are at most 2^N and require O(N) bits; ordinary-schoolbook bit cost is conservatively O(N^4). Parsing initial P,Q, creating the full present O, constructing Stage439 slots and U and extracting a key all take O(m+n) time (a Boolean index mask removes duplicated slots).

For an individual feasible visible word, its *raw-history integer population* is the coefficient

 M_section(v)=[z^(k-c)] PRODUCT_g ( SUM_{j=0}^{ceil(h_g/2)} binomial(h_g-j+1,j) z^j ),

with h_g=max(0,g-left_g-right_g). The joint class population is M_prefix(v0)*M_tail(v1). Exact polynomial convolution, followed by gap-wise unranking with a within-class index, recovers original history and branch provenance; suffix versions of the Boolean DP rank/unrank only feasible visible words without materializing a q_F-sized codebook. A minimal fixed-width class label needs ceil(log2 q_F) bits when q_F>0.

This gives a polynomial algorithm for *arbitrarily growing* defect counts and POP/APPEND budgets in the entire K=t model family; Stage443-B's general support construction instead has O(NH 2^b) transitions. The conserved full V/J/K future observer is the declared scope of this factorization.

## Executed exact checks
The companion REPRO_STAGE444B.py uses only Python3 standard-library arbitrary-precision integers. Its marker is STAGE444B_ZERO_MISMATCH_POLYNOMIAL_SUPPORT_PASS. An exhaustive parameter sweep over m,n∈{4,5,6,7,8}, kP,kQ∈{0,1,2}, pP,pQ∈{0,1,2}, rP,rQ∈{0,1}, always K=min(m,n), compares polynomial support with direct raw-pair enumeration for all 8,100 parameter combinations: 3,312 nonempty fibers, 8,172 raw-history instances and 5,484 aggregate support classes, all equal. Result SHA256 e26da74d7db107e91b2f1ef62301d493cba38022f5981f66f0811f2d0f1beafc. Sixteen additional fixed test domains include 317 directly enumerated histories and 51 exact population-coefficient checks. Five small independent full-future tests traverse 12,168 memoized all-12-native-direction operation states and 24 unordered history pairs, agreeing with the repair-key partition. A Stage442-style subset determinizer was also executed for all fixtures with max(m,n)<=32.

Measured cases (K always min(m,n)):

| m,n,kP,kQ,pP,pQ,rP,rQ | q_F | capacity-DP transitions | subset-state visits | Stage443 candidate 2^b |
|---|---:|---:|---:|---:|
| 15,10,4,2,4,3,3,2 | 15 | 36 | 70 | 131,072 |
| 24,19,7,5,8,6,6,5 | 63 | 75 | 112 | 68,719,476,736 |
| 32,25,10,7,10,9,8,10 | 356 | 120 | 262 | 562,949,953,421,312 |
| 64,48,20,14,25,20,20,20 | 3,719,100 | 531 | not run | 5,192,296,858,534,827,628,530,496,329,220,096 |

These are measured state/transition counts of different representations, not a wall-time speedup assertion. The last line computes q_F without listing its 3,719,100 classes.

## Stage445-B open frontier
Study K=t-1 (exactly one mismatch across the initial overlapping prefix) with growing kP,kQ and operation budgets. Compare subset-state languages and test a candidate compressed carrier combining the sole mismatch marker, nonadjacent-defect capacities and boundary bits. A distinguishing accepted-output suffix proves a proposed merger unsound; a successful new carrier needs a full-future factorization proof and separate exact BRC integer-population recovery. Preserve the current P000, ACTIVE worldview, frozen scientific pins and independent-review status.
