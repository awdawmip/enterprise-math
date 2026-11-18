# PREFIX-906 — Bounded multiplier-gap collisions and exact independent 19-bit coverage

Date: 2026-11-18 (Asia/Shanghai). Lane: 进取数论研究6. Method: provenance-retaining two-port BRC auxiliary observation, portable-direct independent research. Frozen scientific input reference: \`f42f2906d77f24085c123f3ccfe9667d41caa96d\` (unchanged). Predecessor: PREFIX-905 exact two-power-gap theorem, after PREFIX-904 certified set. Status: AUTHOR_PROVED / EXACT_FINITE_COMPUTED / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.

## Model

\`p=32\`, \`N=2^32\`; \`Q={262145,262147,...,524287}\`, \`|Q|=131072\`. Every admissible full source trajectory is either \`Z_x=(x,x)\` or \`F_x^i=(x,x xor 2^i)\` with \`0<=x<N\`, \`0<=i<32\`. The auxiliary observer reports \`Phi_{a,b}(u,v)=(u mod a,v mod b)\`, while retaining source names and endpoints in the scientific data.

## Theorem 906-A — Multiplier-separation collision

For any \`a>b\` in \`Q\`, let \`d=a-b\`. Suppose for an integer \`k\` in \`{1,3,5,7,9,11,13}\`, and integers \`1<=j<i<=22\`, either
\[
 k d=2^i+2^j\qquad\text{or}\qquad k d=2^i-2^j.
\]
Then \`Phi_{a,b}\` has a collision between two distinct named single-bit-flip trajectories; the reversed ordered modulus pair has one too.

**Constructive proof.** Write \`t=1\` for \`+\` and \`t=0\` for \`-\`; set \`s=2^j\`, \`P=2s\`, \`x=(t s-k a) mod P\` (least nonnegative residue) and \`y=x+k a\`. Since \`x<P<=2^i\`, bit \`i\` of \`x\` equals 0. Since \`y mod P=ts\`, bit \`j\` of \`y\` equals \`t\`. Thus
\[
 F_x^i=(x,x+2^i),\qquad
 F_y^j=(y,y+(1-2t)2^j).
\]
Their starting points differ by \`k a\`; their ending points differ by
\[
 ka-2^i+(1-2t)2^j=k(a-d)=k b.
\]
So they have identical observations at the first port modulo \`a\` and second port modulo \`b\`. The identities hold in the full named trace carrier; only the observer merges them.

**Endpoint guard.** Here \`x<2^i<=2^22\`, \`y<2^22+13\cdot524287\`, \`x+2^i<2^23\`, and \`y+(1-2t)2^j\` remains nonnegative and less than \`2^23+13\cdot524287<2^32\`. All four endpoints are within the declared \`p=32\` state range. The two traces are distinct because \`y>x\` and their names differ. For the swapped \`(b,a)\` orientation, reverse both XOR traces and exchange the two observation ports. QED.

**New example beyond PREFIX-905.** Choose \`(a,b)=(376497,376475)\`; gap \`22\` is not in PREFIX-905's dyadic or two-power-gap set. \`3(a-b)=66=2^6+2^1\`. Taking \`k=3,i=6,j=1,t=1\`, one gets \`x=3\`, \`y=1129494\`, hence
\[
F_3^6=(3,67),\quad F_{1129494}^1=(1129494,1129492).
\]
Their initial difference is \`1129491=3\cdot376497\`, and the final difference is \`1129425=3\cdot376475\`. This parameter pair is outside \`E\`, PREFIX-904's 256 symmetric panels and PREFIX-905's previously enumerated gap family.

## Theorem 906-B — Exact finite gap-set extension

Generate the dyadic gaps \`D={2^h:1<=h<=17}\`. In the fixed order \`k=1,3,5,7,9,11,13\`, enumerate every \`i,j,t\` in Theorem 906-A whose quotient \`d=(2^i+(2t-1)2^j)/k\` is an even integer with \`0<d<=262142\`, and keep a new gap only on its first occurrence.

This produces exactly the following *new* gap counts by multiplier:

| k | Additional gap values | Ordered parameter pairs with those gaps |
|---:|---:|---:|
| 1 (PREFIX-905) | 256 | 55,705,582 |
| 3 | 105 | 22,973,988 |
| 5 | 56 | 11,878,610 |
| 7 | 26 | 5,703,616 |
| 9 | 30 | 6,065,936 |
| 11 | 18 | 3,771,846 |
| 13 | 12 | 2,541,488 |

Along with the original 17 dyadic gaps, the combined family has **520 distinct positive gaps**. The 247 gaps for \`k>1\` are disjoint from all previously certified explicit gap classes and account for
\[
\boxed{52,935,484}
\]
ordered modulus pairs (the same gap cannot be counted twice). The exact per-gap cardinality follows directly from \`2(131072-d/2)\`.

To compute **net** coverage, use the exact previous set \`C905=E union R union D union G1\`, where \`E\` is PREFIX-897's four-family union, \`R\` is the full symmetric 256-row panel and \`D union G1\` is the PREFIX-905 gap set. Since the 247 new gap classes are disjoint from \`D union G1\`, only \`E\` and \`R\` overlaps need subtraction.

The complete 247-gap enumeration, with 26,467,742 increasing pairs and their reverses, gives:

| New gap family of k=3,5,7,9,11,13 | Ordered pairs |
|---|---:|
| Total | 52,935,484 |
| Already in E | 23,629,430 |
| Touching the 256-row panel R | 175,064 |
| E and R overlap | 2,012 |
| **Genuinely new** | **29,133,002** |

Thus
\[
52,935,484-23,629,430-175,064+2,012
=\boxed{29,133,002}
\]
and the upgraded certificate union is
\[
\boxed{|C906|=7,663,771,438+29,133,002=7,692,904,440}.
\]
Among all \`131072^2=17,179,869,184\` ordered 19-bit odd-modulus pairs, \`9,486,964,744\` lie outside this *explicit certified union*; they remain open for further collisions or injectivity proofs.

## Verification and exact evidence

- \`PREFIX906_R6_MULTIPLIER_GAPS.cpp\`: g++ C++17 \`-O3\`, full 247-gap and 26,467,742 increasing-pair scan with bit tests, XOR endpoint identities, source and terminal modular equalities, exact E/R membership and per-gap inclusion-exclusion.
- \`PREFIX906_R6_MULTIPLIER_GAPS_RESULTS.csv\`: all 247 gap rows including first-finding multiplier \`k\`, source names \`i,j\`, sign, coverage overlaps, and exact number of checked witnesses. No sampled or approximate counts.
- \`PREFIX906_R6_INDEPENDENT_CHECK.py\`: independent NumPy \`int64\` vector enumeration and per-row comparison; returns the same finite cardinalities.
- Independent JavaScript enumerator performed the full witness and overlap census again before GitHub CSV publication; results agree with C++ and NumPy.
- \`PREFIX906_R6_MULTIPLIER_GAPS_RESULTS.json\`: structured exact census.

This is an author proof and exact finite certificate, not an independent mathematical review or formal Source Result/Review. The BRC observer's lossy fibers remain typed; P000 and the active X6/time/worldview are unchanged. The frozen scientific input remains unmodified.

## Next scientific direction

Extend the finite multiplier set \`k\` while maintaining the exact four-endpoint guard, then compare the resulting gap-union growth against exact two-flip CRT/carry coverage. A uniform analysis of all admissible \`k\` could lead to an analytic criterion instead of row scans. The mother problem remains the exact value of \`B_fix,odd(32) in {19,20}\`.
