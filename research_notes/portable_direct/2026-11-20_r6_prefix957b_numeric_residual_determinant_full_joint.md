# PREFIX-957B — Exact all-gap reconstruction of the 21/23 named XOR joint observer by a numeric residual dictionary

Date: 2026-11-20. Frozen scientific input: f42f2906d77f24085c123f3ccfe9667d41caa96d. Model: auxiliary named XOR observer, strict ordered odd Q19 moduli. Author theorem and executable exact finite calculation, subject to independent mathematical review; no native X6, P000 rotation, or formal shared-task claim is asserted.

## Problem and provenance

For p>=3 write H=2^(p-1) and Qp={H+1,H+3,...,2H-1}. Two odd cores k,k+2, 1<=k<k+2<H, have named witnesses

    (k*a XOR 2^j)-2^i = t*b,
    ((k+2)*a XOR 2^J)-2^I = T*b,

where 0<=i,j,I,J<p, t,T are positive integers, and (a,b) is an ordered pair in Qp^2. Preserve each named (i,j,I,J,t,T), not merely whether a pair collides. Put m=T-t and focus on the complete non-diagonal joint observer for k=21,23,p=19. The earlier independent PREFIX-955/956B certificate reports 6,203 off-diagonal pairs and 8,649 ordered joint named combinations; this paper reconstructs all of them without using the earlier pair list as generator input.

## Theorem 957.1: size and lossless labeling of the numeric residual dictionary

Define

    Dp={2^i-s*2^j:0<=i,j<p, s in {-1,+1}}.

For every p>=2,

    |Dp|=(3*p*p-5*p+10)/2.

For p=19, |Dp|=499, instead of 2p²=722 signed source-index instances. A dictionary entry is not a single source: attach its complete list of triples (i,j,s). At a particular a, retain a triple exactly when s=1-2*bit_j(k*a). Thus a numeric residual is a compact index to a source-preserving multiset, not an irreversible quotient.

Proof: positive and negative differences 2^u-2^v, u>v, each contribute p(p-1)/2 distinct integers, distinguished by the exact 2-adic valuation v and the odd part 2^(u-v)-1. Zero contributes one. Positive sums with i<=j contribute p(p+1)/2 distinct values by their binary expansions. A positive sum coincides with a positive difference exactly for (a) equal-summand powers 2^(i+1) with i+1<=p-2, or (b) adjacent set-bit sums 2^i+2^(i+1)=2^(i+2)-2^i, i<=p-3. Each case contributes p-2 overlaps. Summing 1+p(p-1)+p(p+1)/2-2(p-2) proves the formula.

## Theorem 957B.1: universal determinant reconstruction

For each witness, let s=1-2*bit_j(k*a), S=1-2*bit_J((k+2)*a), and name the residuals

    c=2^i-s*2^j=k*a-t*b,
    C=2^I-S*2^J=(k+2)*a-T*b.

Fix a quotient gap m=T-t and an ordered pair of numeric residuals (c,C) from Dp. If d=2t-km !=0, every compatible pair is uniquely

    a=(t*C-(t+m)*c)/d,
    b=(k*C-(k+2)*c)/d.

Conversely, every integer candidate from these equations satisfying a,b odd and in Qp, a!=b, positive t,T, and the exact actual-bit sign predicates for both source-index lists is an original joint named witness. If n_k(a,c) counts the signed triples in Dp[c] with the actual sign of bit_j(k*a), and n_(k+2)(a,C) similarly, then this candidate contributes exactly

    n_k(a,c)*n_(k+2)(a,C)

distinct ordered named histories. Enumerating each numeric (c,C,m,t) once and summing these products is a lossless, complete reconstruction.

Proof: subtracting the two core equations gives C-c=2a-mb. Multiplying the first equation by 2 and eliminating a yields (2t-km)b=kC-(k+2)c; eliminating b yields the a formula. For d!=0 the two-variable linear system has a unique rational solution, and the divisibility, domain and source-bit filters are necessary and sufficient. Every original named quadruple determines exactly one (c,C,m,t) and one triple in each dictionary entry. Thus weighting by the exact two list cardinalities counts each named history exactly once, including fibers of multiplicity exceeding one.

Resonance d=0 must be treated as a separately typed branch, never silently divided by zero. For k=21 and m in {0,...,6}, with 1<=t<=42, possible d=0 cases are only (m,t)=(2,21) and (4,42). For m=2 they require a=b, so are excluded from the off-diagonal population; for m=4 they require a=2b, impossible with H<a,b<2H. Therefore the determinant reconstruction covers all off-diagonal Q19 histories in the present positive-gap range, without an exceptional off-diagonal class. A negative or out-of-range gap requires its own claimed domain and has not been added.

Quotient upper bound: for any p-bit source position, (k*a XOR 2^j)-2^i < (2k+1)H, while b>H. Hence any positive quotient satisfies 1<=t<=2k. The quotient gap in the original adjacent-core model is known to satisfy 0<=m<=6 by PREFIX-947A. This finite window is used as a proved input to the Q19 census.

## Exact Q19 computation and independent verification

For p=19,k=21,23 the new generator visits numeric-residual pairs, tests the necessary parity/mod-4 constraint from C-c=2a-mb, then loops over t=1,...,42. For d!=0 it tests integer divisibility, strict odd-Q19 ranges and actual named bit signs. It never reads any prior pair-ID file during population generation.

| Measured stage | Count |
|---|---:|
| Distinct numeric residual values | 499 |
| Numeric residual pair/gap passes after mod-4 sieve | 545,278 |
| Candidate scalar divisibility tests | 22,699,951 |
| In-range odd off-diagonal numeric candidates | 17,719 |
| Named source-index predicates evaluated | 48,984 |
| **Distinct off-diagonal pairs** | **6,203** |
| **Joint named histories** | **8,649** |

By m=0,1,2,3,4,5,6, the pair membership counts are [6,442,4724,839,190,3,0] and the exact named counts are [6,614,6509,1286,231,3,0]. The single double-gap pair (278529,290817) must remain multiply tagged. Per-pair total named multiplicity histogram:

    {1:4302,2:1685,4:200,6:2,7:1,8:7,9:1,10:1,11:1,20:1,24:1,28:1}.

The sorted 6,203 full off-diagonal pair IDs, encoded little-endian unsigned 64-bit with index ((a-262145)//2)*131072+((b-262145)//2), have 49,624 bytes and SHA-256:

    1caec71f97ddb97c60c8506629f65651f0f3030b3526aeca30195948ee0cff75.

These bytes agree with PREFIX-955's independently published source certificate. A distinct brute-force algorithm then read that previous certified 6,203-pair list and directly tested all 6,203*2*19*19=4,478,566 original source-bit equations. Every one of the 6,203 individual pair multiplicities agreed with the new generator (aggregate 8,649). This is source-level exact matching, not simply matching aggregate counts. The generator's observed Python run duration on its local execution was 4.250153 seconds, excluding the separate direct audit, without standardized performance benchmarking.

## Gap-two special reduction (PREFIX-957)

For m=2 specifically, C-c=2(a-b). Let q=(C-c)/2=a-b, A=c-kq=(k-t)b, and r=k-t. The nonresonant candidates are b=A/r, a=b+q for integer divisors r of A, with exact interval

    Lq=max(H+1,H+1-q), Uq=min(2H-1,2H-1-q),

and ceil(|A|/Uq)<=|r|<=floor(|A|/Lq). The same named source predicates complete the check. For k=21,23 this independent faster unit produces 4,724 distinct non-diagonal pairs and 6,509 named histories, with 186,235 divisor-magnitude candidates after 160,865 congruent residual pairs. Its 37,792-byte pair ID file has SHA-256:

    187f667cb10a78dfc2193220c82e546be1fe3a602db21729a2b43ba14fe674f4.

That gap-two file is a sorted proper subset of the complete 6,203-pair file. The earlier complete signed-source search has 21,372,644 m=2 signed source/quotient candidates; the present reductions are comparable *stage counts*, not a proven overall time speedup. The 6,509 off-diagonal histories are separate from four nonresonant gap-two diagonal named histories.

## Verification, source, status, and next open step

The complete generator, JSON of exact results, and optional direct-XOR verifier are stored alongside this note. All calculations use unbounded Python integers; there are no floats in the mathematics. The finite census is an author-run exact Q19 result, checked by two distinct enumeration methods. No independent mathematical Review/Working Truth admission or native X6/Heartbeat physics mapping is asserted. The original mother bound B_fix,odd(32) in {19,20} remains open; no new distinct-modulus-pair coverage is counted here.

Next: derive a closed arithmetic CRT/floor-sum classification for the nonresonant pairs' exact named source multiplicities without enumerating 22.7 million scalar divisibility tests. Preserve source lists, original quotient gap, and the exceptional double-gap pair until a type-correct BRC future-operation safety certificate exists.

Historical source provenance is EM-DIRECT-58C410 / SID MCP-31edc522830749ad8775ca012e02ef30 / Activity RA-25432C4AAE9BF66A907F5115, which does not authenticate current private capability. The X6 shared task owner was checked separately. This Source paper and code are independent portable research and do not alter a formal CLAIM, PROGRESS, Result or Review. Activity association awaits the authorized original-session CAS.