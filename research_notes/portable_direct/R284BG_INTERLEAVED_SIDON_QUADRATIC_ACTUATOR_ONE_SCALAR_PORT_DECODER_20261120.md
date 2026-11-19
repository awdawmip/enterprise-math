# R284BG — Interleaved Sidon packing with quadratic actuator exponents

Date: 2026-11-20 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FINITE_CHECK_PASSED / NOT_REVIEWED.
Lineage: R284AT → R284AX → R284BC → R284BF; same declared finite directed/named star-Port observation, inherited frozen scientific scope. Independent portable scientific result; no native Task CLAIM or Result/review asserted.

## Theorem BG1 (quadratic actuator exponent, one exact scalar read)

For every integer n≥3 and known H≥2, any unknown matrix C∈{1,…,H}^{n×n} can be recovered in deterministic polynomial bit time from a single exact integer determinant
[
y=det(operatorname{diag}(d_0,ldots,d_{n-1})-C-sum_{i=1}^{n-1}z_iE_{0i}).
]
More generally, for any fixed finite nonnegative rational error bound δ known beforehand, the single read y+ε, |ε|≤δ, suffices with the radix enlarged as below.

Let p be the smallest odd prime p≥n; for 0≤j<n put
[
a_j=2pj+(j^2mod p),quad A=max_j a_j,quad R=A+1,quad Q=4A+2.
]
Set
[
e_j=Q+a_j,quad S=sum_j e_j,quad t_i=R+2a_i (1≤i<n),quad
d_j=b^{e_j}, z_i=b^{t_i}.
]
Choose L=n n!(1+H)^n and b=2L+1 without noise, or b=4L+8⌈δ⌉+9 with the declared error. Both are odd positive integers.

Then the **maximum radix exponent used in any controlled d_j or z_i is O(n²)**, rather than O(n³) in R284BF. The **ideal readout** still has at most O(n³) radix exponent and O(n³ log b) bits. All control inputs require O(n² log b) bits each. Decoding uses O(n²) addressed coefficient extractions and exact integer divisions, with a running time polynomial in the bit length of the readout and controls. In particular, log b=O(n log n+n log(H+1)+log(1+δ)). An arbitrary rational error denominator has its own actual input length and is not included in the ideal-integer output bound.

## Proof: a *target-only interleaving* instead of placing cofactors entirely above the baseline

Write F(d)=det(diag(d)-C) and G_i(d) for the signed coefficient of the row-zero edit z_i in the determinant. Row multilinearity gives y=F(d)+Σ_{i≥1}b^{t_i}G_i(d). Since all edits are in the same row, there are no cross-products in z_i.

The a_j form a complete Sidon set of nonnegative integers. For two unordered pairs (i,j),(k,l), an equality a_i+a_j=a_k+a_l gives 2p(i+j-k-l) equal to a difference of two residues each in [0,p-1], hence i+j=k+l. Equality modulo p of square sums gives ij=kl (mod p), forcing the same unordered pair of roots of the polynomial X²-(i+j)X+ij over F_p; indices j lie in {0,…,n−1}⊂F_p. Thus all unordered pair sums (including doubled indices) are distinct; in particular ordered nonzero differences a_i−a_j are unique for ordered i≠j. By the elementary bound p=O(n), A=O(n²) (e.g. Bertrand's postulate, or another elementary polynomial bound for the next prime).

Index a monomial by its exponent's **deficit** h=S−k, where k is its radix exponent. Baseline monomials missing a set W of m diagonal variables have
[
h_F(W)=mQ+sum_{jin W}a_j.
]
For a row-zero cofactor indexed by i≥1 and additionally missing W⊆{1,…,n−1}\{i}, with m=|W|, the exponent after multiplying by b^{t_i} has deficit
[
h_G(i,W)=(2+m)Q-R-a_i+sum_{jin W}a_j.
]
The *only* coefficients the decoder needs occupy the following four address ranges:
[
egin{array}{c|c|c}
	ext{target}&h=S-k&	ext{closed interval}\
F: m=1&Q+a_i&[Q,Q+A]\
G_i: m=0&2Q-R-a_i&[2Q-R-A,2Q-R]\
F: m=2&2Q+a_i+a_j&[2Q,2Q+2A]\
G_i: m=1&3Q-R-a_i+a_j&[3Q-R-A,3Q-R+A].
end{array}
]
With R=A+1 and Q=4A+2 these occur strictly in the displayed order: the first two are separated by Q>R+2A; the middle pair by R>0; and the last two by Q>R+3A. Crucially, the highest cofactor-one-deletion deficit is 3Q−1, strictly before the first baseline m≥3 deficit, 3Q. The cofactor m≥2 deficits are ≥4Q−R−A, above all four target bands; baseline m=0 has deficit zero. Thus *no monomial outside these intended classes* contributes to a target address. Within each target class, distinct a_i, distinct pair sums, and distinct ordered nonzero differences respectively ensure a unique source monomial. The lower untargeted classes may collide arbitrarily without affecting recovery.

The four recovered target coefficients are exactly
[
egin{aligned}
[k=S-e_i]&: -C_{ii},\
[k=S-e_i-e_j]&: C_{ii}C_{jj}-C_{ij}C_{ji},quad i<j,\
[k=t_i+S-e_0-e_i]&: -C_{i0},quad i≥1,\
[k=t_i+S-e_0-e_i-e_j]&: C_{i0}C_{jj}-C_{ij}C_{j0},quad i,j≥1, i
e j.
end{aligned}
]
Consequently compute all diagonals, P_{ij}=C_{ij}C_{ji}, then C_{i0}>0, C_{0i}=P_{0i}/C_{i0}, and C_{ij}=(C_{i0}C_{jj}-g_{ij})/C_{j0} for i,j≥1, i≠j. Strict positivity makes the denominators nonzero and all exact divisions integral.

For an individual coefficient of the determinant expansion, the absolute value of any minor is bounded by n! (1+H)^n. Summing at most n families (F plus n−1 cofactors) bounds *every aggregated digit coefficient*, including collisions of unwanted monomials, by L=n n!(1+H)^n. Since b>2L, the balanced base-b digits are recovered uniquely from the integer readout. In the error model b=4L+8⌈δ⌉+9 has strictly enough margin that rounding the observed rational at each addressed power b^k returns the exact balanced target coefficient; every target address has exponent k≥1 (in particular, its cofactor component contains t_i≥R≥1, and its baseline component retains at least one positive e_j). At such k the lower-position tail contributes at most L/(b−1) in scaled units and the error contributes at most δ/b^k≤δ/b, giving L/(b−1)+δ/b<1/2, while higher positions contribute multiples of b. The signed coefficient is recovered by balanced modulo b.

Since p=O(n), A,R,Q,e_j,t_i=O(n²), while S=O(n³); the output degree is at most S (indeed all star terms sit below baseline top). The largest control exponent is max(Q+A,R+2A)=Q+A=5A+2, while BF used S_BF+1+2A=Ω(n³). The result is an improvement in **actuator precision**, not in the leading asymptotic exponent of the ideal output, and does not assert an information-theoretic lower bound outside the stated construction.

## Exact author-side evidence

The standalone companion Python checker uses exact Bareiss integer determinants and Fraction arithmetic. It performs 562 reconstructions (including all 512 positive binary 3×3 matrices), 128 bounded-noise trials at δ=7000, and a complete *monomial-to-target address census* for each 3≤n≤12. All checks PASS; they are author-side finite evidence, not independent review. Verification JSON contains per-size input/output hashes, control-bit comparisons and exact coverage.

For H=2 the maximum *individual control* bit counts (BF → BG) were: n=3: 1271→666; n=4: 5765→2396; n=5: 11038→3758; n=6: 28595→8403. The 6×6 case's maximum observed determinant length was 45,422 bits. Controls are exact, not hardware feasibility measurements.

Checker: `research_notes/portable_direct/R284BG_interleaved_sidon_star_checker.py`.
Evidence: `research_notes/portable_direct/R284BG_interleaved_sidon_verification.json`.

## Relation to P000 and next scientific question

This is an exact finite-matrix observation/representation theorem. It makes no new P000, BRC, native X6 or three-dimensional-slice statement. Retain directed Port labels and measurement precision as part of the declared observer. R284BF's cubic lower bound remains correct for *its stronger whole-cofactor-above-baseline guard*, which this interleaved construction deliberately abandons.

Open: can the **ideal output** encoding exponent also be reduced to O(n²) while retaining deterministic polynomial-time one-read reconstruction? Determine the true bit-complexity Pareto boundary between control magnitude, readout length, noise tolerance and decoding time. Additional experiments can compare nonuniform target bands and adaptively chosen smaller Sidon constructions.
