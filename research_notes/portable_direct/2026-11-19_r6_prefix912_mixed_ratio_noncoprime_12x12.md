# PREFIX-912 — Complete bounded opposite-parity multiplier square, including reversed ratio and non-coprime channels

Date: 2026-11-19 (Asia/Shanghai). Lane: 进取数论研究6.
Type: independent, provenance-preserving BRC / named XOR two-port auxiliary mathematics.
Scientific input remains frozen at \`f42f2906d77f24085c123f3ccfe9667d41caa96d\`; current normative rules and Source inputs are separated.
Direct scientific predecessor: PREFIX-911, \`enterprise-math@0a4fd48a264b1062895fa3e427570d735484695a\`.
Verification: \`AUTHOR_PROVED / EXACT_FINITE_COMPUTED / TWO_DIRECTION_SET_EQUALITY_CHECKED / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED\`.

## 1. Model and theorem

Set \`N=2^32\` and \`Q={262145,262147,...,524287}\`, containing exactly \`M=131072\` odd moduli. Retain *named* admissible trajectories \`Z_x=(x,x)\` and \`F_x^j=(x,x XOR 2^j)\` for integer states \`0<=x<N\`, \`0<=j<32\`. The observation is \`Phi_(a,b)(u,v)=(u mod a,v mod b)\` on \`(a,b) in Q^2\`.

**Theorem 912-A (coprimality-free, ordering-free, opposite-parity collision).**
Let \`a,b\` be odd positive integers, \`k,ell>=1\` have opposite parity, \`1<=i<32\`, and \`s in {-1,+1}\`. Suppose

\[
        k a-\ell b=2^i+s. \tag{1}
\]

Assume \`1+k a<N\` and \`1+2^i<N\`. Then \`Phi_(a,b)\` is not injective on the complete set of named admissible trajectories. Neither \`gcd(k,ell)=1\` nor \`k>ell\` is required.

**Proof.** Set \`x=1-(k mod 2)\` for \`s=+1\`, and \`x=k mod 2\` for \`s=-1\`. Let \`y=x+k a\`. Because \`a\` is odd, \`y mod 2=x+k mod 2\`. Thus \`y\` is odd for \`s=+1\` and even for \`s=-1\`, so \`y XOR 1=y-s\`. Since \`x in {0,1}\` and \`i>=1\`, bit \`i\` of \`x\` is unset, and \`x XOR 2^i=x+2^i\`. Consider

\[
 F_x^i=(x,x+2^i),\qquad F_y^0=(y,y-s).
\]

Both are legitimate named XOR tracks by the endpoint bounds; their start points differ by \`y-x=ka\`. Their ending points differ by \`(y-s)-(x+2^i)=ka-s-2^i=ell*b\` from (1). Hence both first-port and second-port residues agree. The starts are distinct since \`ka>0\`. Reversing the two trajectories and exchanging the ports proves the corresponding collision for \`(b,a)\`. QED.

For the entire present census, \`1<=k,ell<=12\`, \`1<=i<=22\`, \`a,b<=524287\`, so the endpoint guards hold uniformly: \`1+12*524287<2^32\` and \`1+2^22<2^32\`.

**New structural content.** PREFIX-908 through PREFIX-911 used the opposite-parity equation with one-sided \`k>ell\` and usually coprimality. Neither restriction is needed for the actual XOR witness. Including \`k<ell\` adds a previously omitted ratio regime; including \`gcd(k,ell)>1\` adds non-primitive lattice channels.

## 2. Exact finite classification of previously omitted channels

Consider all 72 ordered pairs \`(k,ell)\` with \`1<=k,ell<=12\` and \`k-ell\` odd. Exactly 31 channels had already been explicitly treated: \`(2,1)\` by PREFIX-908 and 30 coprime \`k>ell\` channels in PREFIX-909 through PREFIX-911. The remaining 41 comprise 36 channels with \`k<ell\` and five with \`k>ell, gcd(k,ell)>1\`.

For every new \`(k,ell)\`, every \`i=1,...,22\`, both signs, and all 131,072 odd first-port moduli, solve (1) for the second modulus. The primary implementation solves the first-port progression

\[
2kt\equiv(2^i+s)+\ell-k\cdot262145\pmod{2\ell},
\qquad a=262145+2t,
\]

with the congruence enforcing integral odd \`b\`. It checks every valid pair's two XOR tracks, legal states and two modular equalities. No sampling is used.

Deduplication builds the precise known certificate set from PREFIX-908's symmetric sufficient families, the preceding named-gap and panel families, all raw PREFIX-909 witnesses and the exact canonical PREFIX-910 / PREFIX-911 residual sets. The inherited cardinalities are independently regenerated as regression assertions: 1,900,472 raw oriented PREFIX-909 pairs; 1,785,728 unordered new PREFIX-910 pairs; and 1,562,198 unordered new PREFIX-911 pairs.

Encode an oriented pair as \`z=((a-262145)/2)*131072+(b-262145)/2\`; the canonical *unordered* key is \`min(z,transpose(z))\`. Since collision is invariant under trajectory reversal and port exchange, every novel unordered pair produces two distinct oriented pairs in this new family (a diagonal candidate is possible, but direct finite checking finds only \`a=b=349525\` with \`k-ell=3, i=20, s=-1\`, already covered by the older capacity certificate \`a*b<33*2^32\`; therefore the **new** residual set contains no diagonal). The program counts canonical pair IDs and checks all overlaps against the previously certified union.

The complete exact result is:

| Quantity | Exact value |
|---|---:|
| Newly evaluated channels | 41 |
| Channels contributing at least one previously uncounted pair | 23 |
| Parameter witnesses (counting repeated parameters) | 8,768,859 |
| Sum of familywise unique oriented pairs | 8,494,676 |
| Distinct new **unordered** pairs after all overlaps | **4,082,495** |
| New certified **ordered** pairs | **8,164,990** |
| Old PREFIX-911 certified ordered union | 7,787,364,838 |
| **Updated PREFIX-912 certified ordered union** | **7,795,529,828** |
| Full finite domain \`|Q|^2\` | 17,179,869,184 |
| Outside the current explicit certified union | 9,384,339,356 |

Under the lexicographic first-hit order of the code, the 36 reversed-ratio \`k<ell\` families contribute 3,543,044 new unordered keys and five non-coprime \`k>ell\` families contribute 539,451 more (these are order-dependent disjoint attributions, not independent union counts).

**Concrete new witness.** Take
\[
a=271731,\ b=521617,\ k=6,\ \ell=3,\ i=16,\ s=-1.
\]
Then \`6a-3b=65535=2^16-1\`, \`x=0\`, \`y=1630386\`. The distinct named tracks are

\[
F_0^{16}=(0,65536),\qquad F_{1630386}^{0}=(1630386,1630387).
\]

The start difference is \`1630386=6a\`; the terminal difference is \`1564851=3b\`. This is a non-coprime multiplier collision omitted by the older channels.

## 3. Verification and evidence

The standalone C++17 source:

- Rebuilds seven preceding sufficient-collision family inventories and checks exact reference inventory cardinalities \`(258,276,857,552,192,169,37)\`.
- Rebuilds the old 909/910/911 multiplier sets and asserts their known exact sizes before adding anything.
- Enumerates all 41 new families *twice*. The independent method starts from \`b=262145+2t\` and solves
  \[
  2\ell t\equiv k-\ell\cdot262145-(2^i+s)\pmod{2k},
  \]
  enforcing an odd integer \`a\`. It independently checks the valid XOR witness for every parameter.
- Asserts equality of all per-family witness totals and raw unique counts and then verifies equality **of every one of the 4,082,495 canonical novel pair identifiers** between the two enumeration methods.

Local executable test: \`g++ -std=c++17 -O3 -Wall -Wextra PREFIX912_R6_MIXED_12X12_CENSUS.cpp -o prefix912 && ./prefix912\`; observed exit 0, primary total \`TOTAL 41 8768859 8494676 4082495 8164990 7795529828 9384339356\`, independent total \`INDEPENDENT_B_FIRST_PASS 41 4082495 exact canonical pair IDs\`. All 41 full rows and exact parameters are in the accompanying JSON result certificate. Arithmetic and set comparisons are exact.

Code: \`research_notes/portable_direct/PREFIX912_R6_MIXED_12X12_CENSUS.cpp\`, publication \`enterprise-math@646d14b5349acb9f7bc049d9b7029eb8c36ebd09\`.
Results: \`research_notes/portable_direct/PREFIX912_R6_MIXED_12X12_RESULTS.json\`, publication \`enterprise-math@2411a030be87f4e608dde810e6d93217f70a266b\`.

## 4. Research and control boundary; continuation

This is a specified sufficient-collision union for the auxiliary 32-bit named two-port observation, with source-bit labels preserved and physical X6/natively typed BRC event attribution not asserted. The unresolved mother question remains \`B_fix,odd(32) in {19,20}\`; 9,384,339,356 pairs still lie outside this particular constructive certificate union.

The most valuable next new mathematics is to eliminate the **other** artificial one-sided channel restriction: for \`i>j>=1\`, construct two distinct named XOR tracks from \`k a-\ell b=2^i+/-2^j\` with general \`k!=ell\`. This extends the older same-multiplier gap theorem to unequal endpoint multipliers in the same-parity class. A second direction is exact carry-based two-flip analysis of the complement.

The contemporaneous X6 native continuation read was attempted with original request \`r6-20261119-0253-x6-owner-read-prefix912\` and returned \`FAILED / SOURCE_TREE_BLOB_SIZE_INVALID\`, so current shared owner/claim was not established in this unit and no shared CLAIM or authenticated protected execution write was attempted. Reuse the previously established research session metadata \`EM-DIRECT-084DAB / MCP-fe28d5880a1e4a3ea308960ced4a03a1\` only as provenance unless current native authority is confirmed. The scientific files have their own independent GitHub source evidence.