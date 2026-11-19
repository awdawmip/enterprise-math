# PREFIX-940 — Elevenfold odd-core named XOR collision: exact disjoint union and bit-sign sieve

Date: 2026-11-19. Scientific input: immutable project pin \`f42f2906d77f24085c123f3ccfe9667d41caa96d\` (inherited from PREFIX-939). Scope: **auxiliary** fixed-19-bit odd-modulus, named XOR two-port observer. This is **not** a native six-dimensional X6 assertion. Work status: AUTHOR_PROVED / EXACT_FINITE_COMPUTED / TWO_INDEPENDENT_IMPLEMENTATIONS_AGREE / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.

Prior result: \`research_notes/portable_direct/2026-11-19_r6_prefix939_ten_a_2adic_boundary_exact_union.md\` with certified union \`7,552,811,074\`. Historical R6 Researcher \`EM-DIRECT-58C410\`, SID \`MCP-31edc522830749ad8775ca012e02ef30\`, Activity \`RA-25432C4AAE9BF66A907F5115\` are provenance only; no new source-associated checkpoint, authenticated claim or Result is asserted by this paper.

## 1. Object and constructive proof

Let \`N=2^32\` and \`Q={262145,262147,...,524287}\` (131,072 integers). For each named source bit \`j\`, the legal trajectory is \`F_x^j=(x,x XOR 2^j)\` with both endpoints in \`[0,N)\`. The ordered moduli \`(a,b) in Q^2\` determine the observer

\`\`\`
Phi_(a,b)(u,v)=(u mod a, v mod b).
\`\`\`

For \`k=11\`, define \`W11\` to consist of all ordered \`(a,b)\` for which there exist \`i,j in {0,...,18}\` and a positive integer \`t\` such that

\`\`\`
D11(a,i,j)=(11*a XOR 2^j)-2^i=t*b.                  (1)
\`\`\`

**Theorem.** Every \`(a,b) in W11\` has two distinct legal named trajectories \`F_0^i\` and \`F_(11a)^j\` with exactly equal two-port observations.

*Proof.* Both starting observations are zero since \`11a ≡ 0 mod a\`. The final observations agree by (1), since \`11a XOR 2^j ≡ 2^i mod b\`. Their starts differ (\`11a > 0\`), so the histories remain distinct even if source bits happened to be equal. The largest start \`11*524287=5,767,157\`, and a single XOR flip at bit at most 18 keeps the endpoint strictly below \`2^32\`. The zero-start history is also legal. QED.

For all input configurations, the conservative inequalities

\`\`\`
11*262145-2^19 <= D11 <= 11*524287+2^18-1
2,359,307 <= D11 <= 6,029,300 < 23*262145
\`\`\`

prove that any positive quotient in (1) satisfies \`1<=t<=22\`; this is a complete scan window, not a sampling assumption. There is no floating point arithmetic. In fact no solutions occurred for \`t=1,2,3,4,22\`, but that last fact is from the finite census, not the bound.

## 2. Reusable exact bit-sign sieve for odd cores

For every integer \`x >=0\`, put \`epsilon_j(x)=1-2*((x >> j) & 1)\`. Then

\`\`\`
x XOR 2^j = x + epsilon_j(x)*2^j, epsilon_j(x) in {-1,+1}.
Dk = k*a + epsilon_j(k*a)*2^j - 2^i.
\`\`\`

For fixed odd \`k,a,b\`, \`t*b=Dk\` has odd \`t\` precisely when \`(i==0) == (j==0)\`. This follows from parity: \`k*a\` is odd, flipping bit zero changes parity, and subtracting \`2^i\` changes parity exactly when \`i=0\`. For fixed \`j\`, the sign \`epsilon_j(k*a)\` depends only on \`k*a mod 2^(j+1)\`, a finite exact congruence-cell property; all candidate quotients must also satisfy the single signed linear relation above. This sieve is useful when replacing a full \`(a,i,j,t)\` scan by congruence-class arithmetic. No BRC or native X6 map is claimed for this auxiliary identity.

## 3. Exact finite census and old-certificate subtraction

Enumerate \`a in Q\`, all 361 named source-bit pairs \`(i,j)\`, and \`t=1,...,22\`. Retain precisely the cases in (1) with \`b=D11/t in Q\`. Pair IDs are the strictly increasing uint64 little-endian encoding

\`\`\`
ID(a,b)=((a-262145)/2)*131072 + ((b-262145)/2).
\`\`\`

The scalar C++17 implementation iterates \`a,j,i,t\` and partitions the resulting set through sorted linear merges and the prior closed predicates. An independently written NumPy implementation iterates \`j,i,t\` and vectorizes over \`a\`, then uses independent binary searches, vectorized gcd and direct recomputation of the old B/Z/S and V predicates. Both enumerate the whole prescribed domain; neither samples candidates.

| Measure | Count |
|---|---:|
| Raw \`(a,i,j,t)\` witnesses | 16,974,425 |
| Distinct ordered \`W11\` pairs | 13,144,330 |
| Prior B/Z/S overlap | 6,510,937 |
| Additional U overlap | 2,356 |
| Additional V overlap | 25,991 |
| Additional W2/W3 overlap | 711,646 / 765 |
| Additional D4/W5/D6 overlap | 283 / 768 / 501 |
| Additional W7/D8/W9/D10 overlap | 710 / 414 / 942 / 103 |
| **New pairs outside all earlier families** | **5,888,914** |
| **Old plus new exact certificate union** | **7,558,699,988** |
| **Remaining pairs without these certificates** | **9,621,169,196** |

The overlap categories are *priority-disjoint*, ordered exactly as printed; they sum with the new category to 13,144,330. The count of remaining pairs is \`131072^2 - 7558699988\`; it does **not** assert that any complement pair is injective.

First lexicographically new witness:

\`\`\`
(a,b)=(272161,520807), i=0, j=17, t=6.
11*a=2993771, (11*a XOR 131072)=3124843.
3124843-1=3124842=6*520807.
Phi_(a,b)(0,1)=Phi_(a,b)(2993771,3124843)=(0,1).
\`\`\`

## 4. Reproduction and evidence

The exact executed source programs, committed with this paper:
- \`PREFIX940_R6_ELEVEN_A_EXACT_CPP.cpp\` (g++ -O3 -std=c++17)
- \`PREFIX940_R6_ELEVEN_A_INDEPENDENT_NUMPY.py\` (NumPy independent enumeration and priority-membership check)
- \`PREFIX940_R6_ELEVEN_A_EXACT_RESULTS.json\` (all category counts, original input SHA-256, outputs, witness, review scope)

All ten previous sorted input files were extracted from the preceding, user-supplied \`PREFIX939_R6_full_reproduction_bundle.zip\` and SHA-256 checked against its manifest before computing. The \`PREFIX928\` pair set and prior W2/W3/D4/W5/D6/W7/D8/W9/D10 all match their recorded hashes. Reproducing this partition **requires the exact frozen bytes**; a different universe or priority hierarchy would define a different count.

Both independent implementations generated identical 105,154,640-byte complete \`W11.bin\` and identical 47,111,312-byte \`NEW11.bin\`; binary comparisons returned equality. Exact output SHA-256:

\`\`\`
W11.bin    8212f0472ebe72ae93db8a205c8631f5eb96abbe952588cc08a5eb4087aeecf5
NEW11.bin  b17896465cb38ca5b87e48f88ebaf7d709888a9d0ef343c1c056916fb6c03ad9
\`\`\`

Source-code publication and result JSON do not mean an independent Source CLI audit, formal theorem review, canonical admission or native Shared CLAIM was performed. A full local reproducibility ZIP contains the frozen binary inputs and outputs, both original executed programs, their raw stdout, this proof, and a SHA-256 manifest.

## 5. Remaining scientific question

A useful next direction is to derive a counting formula by splitting \`ka\` into signed-bit congruence cells for odd \`k\`, and to determine whether it can compute incremental nonoverlapping coverage for \`k=13,15,...\` without separately enumerating every \`(a,i,j,t)\` combination. Preserve these certificates as named history collisions; transferring them to X6 native space would require a separately proven embedding, observer map and provenance-preservation theorem. Shared X6 ownership is external to this independent mathematical experiment.

Mother problem \`B_fix,odd(32) in {19,20}\` remains OPEN.
