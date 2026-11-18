# PREFIX-917 — Exact equal-start / equal-terminal collision-pair mass

Date: 2026-11-19 (Asia/Shanghai). Lane: 进取数论研究6.
Status: AUTHOR_PROVED / EXACT_FINITE_COMPUTED / TWO_METHOD_MODULUS_CENSUS / SMALL_STATE_EXHAUSTIVE / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.
Frozen scientific input: \`f42f2906d77f24085c123f3ccfe9667d41caa96d\`.
Direct frontier: PREFIX-915 exact source-label multiplicity and PREFIX-916 disjoint positive-gap high-source-first collision mass. This note isolates two additional, mutually disjoint labeled trajectory classes (one common endpoint). It does not claim an increment to the old Boolean modulus-pair coverage.

## 1. Observation and precise statement

Let \`p>=2\`, \`N=2^p\`. A *named flip* is \`F_x^i=(x,x XOR 2^i)\`, with \`0<=x<N\` and \`0<=i<p\`. For positive odd moduli \`a,b>1\`, observe \`Phi_(a,b)(u,v)=(u mod a,v mod b)\`. Count distinct **unordered pairs of different named-flip trajectories**, retaining \`x\` and the two source indices \`i,j\`. Each pair belongs to at most one of the following classes:

- \`E_start(a,b)\`: both trajectories have exactly the same initial state; their final states have the same residue modulo \`b\` (the initial port agrees automatically).
- \`E_end(a,b)\`: both trajectories have exactly the same final state; their initial states have the same residue modulo \`a\` (the final port agrees automatically).

Define the integer divisor-weight function

\`\`\`text
W_p(m) = sum_{d=1}^{p-1} (p-d) *
    ( 1[m divides (2^d-1)] + 1[m divides (2^d+1)] ).
\`\`\`

**Theorem 917-A (complete, exact, disjoint mass):** for odd \`a,b>1\`,

\`\`\`text
|E_start(a,b)| = (N/2) * W_p(b),
|E_end(a,b)|   = (N/2) * W_p(a),
E_start(a,b) intersect E_end(a,b) = empty,
|E_start union E_end| = (N/2) * (W_p(a)+W_p(b)).
\`\`\`

This counts *trajectory pairs*, not pairs of observer moduli. It is exact for every \`p>=2\`, with no generic-position, headroom, or floating-point hypothesis.

**Proof.** For fixed \`x\` and distinct indices \`0<=i<j<p\`, put \`d=j-i\` and \`sigma_t(x)=1\` if bit \`t\` of \`x\` is zero, otherwise \`-1\`. The difference of the two terminal states is

\`\`\`text
(x XOR 2^j) - (x XOR 2^i)
 = sigma_j(x)*2^j - sigma_i(x)*2^i
 = 2^i*(sigma_j(x)*2^d-sigma_i(x)).
\`\`\`

Because \`b\` is odd, this difference is divisible by \`b\` precisely when \`b\` divides \`2^d-1\` (equal signs) or \`2^d+1\` (opposite signs). The two named source bits are independent across the full \`p\`-bit state set: every one of the four sign assignments occurs for exactly \`N/4\` different initial states. Each divisor alternative therefore supplies \`2*(N/4)=N/2\` different unordered trajectory pairs for this one \`(i,j)\`. There are \`p-d\` index pairs at displacement \`d\`, which proves the first formula by an exact, nonoverlapping partition by \`(x,i,j)\`.

For a common terminal state \`z\`, the two starting states are \`z XOR 2^i\` and \`z XOR 2^j\`, using the involution property of XOR. Repeating the same argument with modulus \`a\` proves the second formula. A pair with both a common start and a common terminal would force \`2^i=2^j\` and therefore \`i=j\`, contrary to the distinct-source requirement. The classes are disjoint. QED.

## 2. Strict-19-bit complete finite census (p=32)

Let \`Q={262145,262147,...,524287}\`, so \`|Q|=131072\`. Exact integer enumeration of every \`b in Q\` against all 31 displacements and both signs gives:

\`\`\`text
|{b in Q: W_32(b)>0}|                  = 24
sum_{b in Q} W_32(b)                   = 134
sum_{b in Q} |E_start(a,b)|, fixed a   = 287762808832
sum_{(a,b) in Q^2} |E_start(a,b)|      = 37717646879227904
sum_{(a,b) in Q^2} |E_end(a,b)|        = 37717646879227904
sum_{(a,b) in Q^2} |E_start union E_end|
                                          = 75435293758455808
\`\`\`

Every count is a positive integer and is weighted by labeled trajectory multiplicity. The **24** exceptional moduli are:
\`262145, 262657, 266305, 270805, 294903, 299593, 328965, 338613, 349525, 349867, 360437, 372827, 402905, 416179, 422733, 427445, 429325, 430185, 449829, 463419, 475107, 479349, 486737, 524287\`.
The complete per-modulus weights and exact divisor causes are in the companion JSON.

In particular, \`b=262145=2^18+1\` has \`W_32(b)=14\` and for **every** positive observer modulus \`a\` there are exactly \`14*2^31=30064771072\` distinct equal-start named-flip collision pairs. An elementary witness is \`F_1^0=(1,0)\` and \`F_1^18=(1,262145)\`: same start, and the final difference equals \`b\`.

Similarly, \`a=524287=2^19-1\` yields \`W_32(a)=13\`, hence \`13*2^31=27917287424\` equal-terminal collision pairs for every positive \`b\`.

## 3. Validation and numerical meaning

Reproduction: \`research_notes/portable_direct/PREFIX917_R6_COINCIDENT_ENDPOINT_MASS_CHECK.py\`; output: \`research_notes/portable_direct/PREFIX917_R6_COINCIDENT_ENDPOINT_MASS_RESULTS.json\`.

1. First exact census: independently test every \`b in Q\` and every \`1<=d<32\` via integer divisibility.
2. Second census: factor each \`2^d-1\` and \`2^d+1\`, generate all positive divisors, and intersect those divisors with \`Q\`. All 24 exceptional moduli and each weight agree exactly.
3. Direct brute force: for every \`2<=p<=8\`, all odd \`3<=m<2^p\` and both equal-start and equal-end variants, enumerate all \`2^p\` states and all distinct named index pairs, comparing with the formula. **494 exhaustive (p,m,class) comparisons, zero mismatches.**
4. For \`p=32\`, no state-space enumeration was attempted: the theorem reduces the entire computation to 131072*31 exact modulus tests and independent 31-integer factor/divisor enumerations. All arithmetic is integral, and mass is not interchangeable with Boolean modulus-pair support.

This is a concrete BRC provenance-sensitive refinement: the observation \`exists a collision\` loses the exact labeled multiplicity, while \`W_p\` and the integer mass retain it. The equal-start/end classes are disjoint from PREFIX-916's \`x<y\`, \`i>j\`, positive-terminal-gap class only where explicitly applicable: PREFIX-916 has \`x<y\`, so it is disjoint from \`E_start\`; \`E_end\` may overlap its \`x<y\` class when its terminal gap is zero, whereas PREFIX-916 requires positive terminal gap and therefore has no overlap with \`E_end\` either. Hence all three declared classes are pairwise disjoint. There is **no asserted new net count** of collision *modulus pairs* beyond PREFIX-916's earlier certificate union.

## 4. Next frontier / control

A natural next unit is an exact orientation-complete mass formula for all \`x<y\` two-flip collision pairs, including both source-index orders, zero/negative terminal gaps and equal-index cases; the kernel must explicitly handle \`i=j\` (PREFIX-915's \`j<i\` formula cannot be used unchanged). The direct and divisor-based tests above remain portable validation inputs.

This auxiliary XOR two-port observer is not an admitted native X6 event or a claim about a primitive two-dimensional plane. The immutable P000 and ACTIVE X6 world semantics remain unchanged, and no shared CLAIM, Result, independent review or Foundation promotion is asserted by this publication. Current owner status must be read from its original native control request, not from historical footer identities.
