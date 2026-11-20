# PREFIX-972 — Parity-refined labeled gcd source fibers and provenance gap

Date: 2026-11-21 (Asia/Shanghai). Status: AUTHOR_PROOF / EXACT_INTEGER_VERIFIED / NOT_REVIEWED.
Scope: independent auxiliary adjacent-core XOR integer observer. Historical EM-DIRECT-58C410 is prior provenance, not current authenticated session possession. No X6 CLAIM, Result, Review, or P000 promotion is asserted.

Frozen scientific input pin (unchanged): f42f2906d77f24085c123f3ccfe9667d41caa96d.
Predecessor: PREFIX-971 at enterprise-math@d5d9737c0536df0ef14c205333c6507f6d792d2f, research_notes/portable_direct/2026-11-21_r6_prefix971_gcd_source_fiber_exact_count.md.

## Object and theorem 972.1: exact parity-refined numeric and labeled spectra

Let p >= 4. The signed, labeled source set is L_p = {(i,j,s): 0 <= i,j < p, s in {+1,-1}} with residual c(i,j,s) = 2^i - s*2^j, and D_p is the set of distinct numeric residual values. Define L_p(g) and D_p(g) by divisibility of c by odd g. Counts labeled by parity refer to c mod 2, not s.

For odd g > 1 put h=ord_g(2). Set eta=1 exactly when h is even and 2^(h/2)=-1 (mod g). Let
A = sum_{1 <= e < p, e=0 mod h}(p-e),
B = sum_{1 <= e < p, e=h/2 mod h}(p-e) if eta=1, else 0,
L = floor((p-1)/h),
M = #{1 <= e < p : e=h/2 mod h} if eta=1, else 0.

Then all these integer counts are exact:

- Numeric total |D_p(g)| = 1+2A+B-[g=3]*(p-2).
- Numeric odd |D_p(g) odd| = 2L+M-[g=3]; numeric even is the difference.
- Labeled slots with sign s=+1: p+2A; with s=-1: 2B.
- Labeled odd slots: 2L+2M; labeled even slots: p+2A+2B-2L-2M.

For g=1:
- |D_p|=(3p^2-5p+10)/2, numeric odd=3p-4.
- |L_p|=2p^2, labeled odd=4(p-1), labeled sign+ and sign- each p^2.

Proof. For i != j set e=|i-j|>0 and r=min(i,j). Since g is odd, 2^r is invertible mod g. If s=+1, g divides the difference exactly when 2^e=1 mod g, so e=0 mod h. If s=-1, divisibility requires 2^e=-1 mod g, equivalently eta=1 and e=h/2 mod h. Each eligible distance has p-e choices of r and two ordered signed source slots; equal-index sign+ gives p zero slots. The integer 2^r(2^e±1) is odd exactly when r=0, giving two labeled odd slots per eligible e.

For numerical values, positive and negative differences each contribute A distinct values and positive sums contribute B distinct values, with zero counted once. Within each family the 2-adic valuation r and strictly monotone odd factor distinguish all values. A positive sum can coincide with a positive difference only if 2^e-1=2^f+1, whose unique positive integer solution is (e,f)=(2,1), giving value 3*2^r. With odd g>1, this overlap is g-divisible exactly when g=3; there are p-2 overlaps in total and exactly one odd overlap at r=0. This proves the g>1 numeric formulas. For g=1 all 2p^2 labeled slots qualify, 4(p-1) are odd, and numeric odd values number 2(p-1) differences plus p-1 sums minus the unique odd overlap (3), namely 3p-4. The full numeric count is PREFIX-971's directly proved formula. QED.

## Theorem 972.2: provenance-aware gcd average

Let k>0 be odd. For any odd quotient gap m satisfying the adjacent-core parity law, t ranges from 1 to 2k, and the necessary source conditions are gcd(k,t)|c and c = 1-t (mod 2). Then the exact pre-XOR-sign labeled candidate count is

N_named(p,k) = sum_{g|k} phi(k/g)*|L_p(g)|,

whereas the distinct-numeric candidate count is

N_numeric(p,k) = sum_{g|k} phi(k/g)*|D_p(g)|.

Before gcd filtering the counts are k*2p^2 and k*|D_p| respectively.

Proof. Pair t=r and t=r+k for 1<=r<=k. Both have the same gcd g with k, while their parities are opposite because k is odd. Each g-divisible signed triple (respectively numeric residual) matches the prescribed parity at exactly one of these two t. There are phi(k/g) r-values with gcd(k,r)=g. Sum over g. QED.

Importantly N_named-N_numeric measures the exact multiplicity lost by mapping the upstream labeled candidate set to distinct numeric residues; it is not automatically the number of lost fully XOR-valid histories. Signed source triples and their actual XOR bit-validity must still be retained or independently reconstructed. This is a concrete BRC typed-observer distinction.

## Q19, adjacent odd cores 21 and 23

For p=19 and k=21, divisor rows (g; numeric even, odd; labeled even, odd; labeled s+,s-):
1: 446,53; 650,72; 361,361
3: 210,26; 325,36; 181,180
7: 91,12; 109,12; 121,0
21: 37,6; 55,6; 61,0

Weights phi(21/g) are 12,6,2,1. The gcd-stage source total is N_named=11,133 compared to N_numeric=7,653: 3,480 more labeled candidates than numerical candidates. The respective pre-gcd totals are 15,162 and 10,479.

## Exact computation and implementation comparison

PREFIX972_R6_PARITY_FIBER_VERIFIER.py directly constructs labeled triples and numeric projections for all odd 1<=g<2^(p-1) at p=4..9: 252 complete parity-fiber tests. It separately checks all eligible odd k: 246 exact gcd-average tests. Q19/core21 checks every divisor row by direct enumeration and the closed formulas. General assertions rest on the proofs above, not finite tests.

PREFIX972_R6_SOURCE_GCD_JOIN.py constructs the source-fiber gcd filter by exponent distances instead of numerical modulo checks; the historical PREFIX968_R6_MODULAR_BUCKET_JOIN.py is the comparison baseline. At p=19,k=21 and gaps m=1,3,5, each branch's numeric c probes fall from 10,479 to 7,653. All named tuples, with hashes ccbccc30c4171a809f7270ce59f0b72b368839e93ffeeed8df9ba1045720da71, 1360a9ca274b357d0b87058d35ef6ccd059d0c5aef995e4d93b0d1363e1aaae3, and c429ef59749f36ef295b4ac9171fb5171ab3a706beaa270563728d4962649c1b respectively, agree with the original benchmark. The corresponding named histories are 614, 1286, 3; non-diagonal modulus pairs 442, 839, 3. Independent raw-XOR enumeration checks all 168 eligible (p,k,m) cases for p=4..7. The modular C-bucket candidate totals remain 132661,134077,24996.

The local CPython benchmark used 12 alternating full three-gap runs including source-fiber construction, lookup, output recovery and XOR checks. Median times were 0.075252 s for PREFIX968 and 0.071626 s for this gcd-source variant (~1.05x). This is specific to the environment and is not a claimed speedup over the later PREFIX970 shared bounded index.

## Continuation

Apply these precomputed (g, parity, sign and source-distance) fibers in PREFIX970's cross-gap bounded index, retaining complete source labels until final XOR validation. Compare complete memory/runtime costs and test which source quotient is invariant under declared later BRC operations. The mother target B_fix,odd(32) in {19,20} remains OPEN.

Frozen science and P000/ACTIVE worldview are unchanged; this auxiliary two-core integer observer is not asserted as a primitive X6 operator. No formal admission or independent review occurred.
