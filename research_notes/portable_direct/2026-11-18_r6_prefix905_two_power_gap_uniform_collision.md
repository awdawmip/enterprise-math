# PREFIX-905 — Uniform two-power-gap named-XOR collisions and duplicate-free 19-bit census

Date: 2026-11-18 (Asia/Shanghai). Research: independently published portable-direct BRC auxiliary observer. Freeze provenance: \`f42f2906d77f24085c123f3ccfe9667d41caa96d\` (inherited science input; not repinned). Predecessor: PREFIX-904 exactly at \`2026-11-18_r6_prefix904_fourth_panel_dyadic_exact_union.md\`. Status: AUTHOR_PROVED / EXACT_FINITE_COMPUTED / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED. Current shared X6 CLAIM: not asserted.

## Exact model

Put \`N=2^32\`, \`Q={262145,262147,...,524287}\`, \`|Q|=131072\`. The full named source trajectories are \`Z_x=(x,x)\` and \`F_x^i=(x,x xor 2^i)\` with \`0<=x<N\`, \`0<=i<32\`. The two-port observer reads \`Phi_{a,b}(u,v)=(u mod a,v mod b)\`. Different source trajectories having equal observations are **observer-relative collisions**; their names and native provenance are not identified.

## Theorem 905-A — Two different named flips give a uniform gap collision

Let \`a>b>0\`, \`d=a-b\`, and suppose for integers \`1<=j<i<=18\` either
\[
d=2^i+2^j\qquad\text{or}\qquad d=2^i-2^j.
\]
For any such \`a,b\` in \`Q\`, the observer \`Phi_{a,b}\` has a collision between two distinct trajectories with **different** flip names \`i,j\`.

**Explicit witness.** Let \`s=2^j\` and \`P=2s\`. Let \`t=1\` for the plus case and \`t=0\` for the minus case. Choose
\[
x=(ts-a)\bmod P,\qquad y=x+a,
\]
where the least nonnegative remainder is used. Thus \`0<=x<P<=2^i\`, so bit \`i\` of \`x\` is 0; \`y mod P=ts\`, so bit \`j\` of \`y\` equals \`t\`. Consequently
\[
F_x^i=(x,x+2^i),\qquad
F_y^j=(y,y+(1-2t)2^j).
\]
The starting-point difference is \`y-x=a\` and the end-point difference is
\[
(y+(1-2t)2^j)-(x+2^i)
=a-2^i+(1-2t)2^j=b.
\]
Therefore both port residues agree. All endpoints lie between 0 and \`N-1\`: \`x<2^i<=2^18\`, \`y<2^i+524287<2^19+2^18\` and the one-bit flips remain far below \`2^32\`. The trajectories are distinct and have different names. QED.

For \`b>a\`, exchange the endpoints of each trajectory and swap observation ports; XOR reversal is a bijection of this **auxiliary finite model**. The collision therefore holds for both ordered modulus orientations without a physical-time reversibility assumption.

**A previously uncovered example.** Take \`(a,b)=(376495,376489)\`, \`d=6=2^2+2^1\`, \`i=2,j=1\`. Then \`x=(2-376495) mod 4=3\`, \`y=376498\`. The two traces \`F_3^2=(3,7)\` and \`F_{376498}^1=(376498,376496)\` have identical observations, since source separation is 376495 and terminal separation is 376489. This ordered pair lies outside PREFIX-904's \`E\`, 256-panel and dyadic classes.

## Theorem 905-B — Exact new gap-family census

Let \`D={2^h:1<=h<=17}\` be the already certified dyadic gaps. Let
\[
G=\left(\{2^i+2^j,\ 2^i-2^j:1\le j<i\le18\}
\cap \{2,4,\ldots,262142\}\right)\setminus D.
\]
Direct integer set construction gives \`|G|=256\`, with no repeated values; every \`d in G\` is certified by Theorem 905-A. Since different positive gaps define disjoint pairs,
\[
\#\{(a,b)\in Q^2:|a-b|\in G\}
=2\sum_{d\in G}(131072-d/2)
=\boxed{55,705,582}.
\]
The earlier dyadic family contains 4,194,306 pairs; the combined 273-gap family has 59,899,888 ordered pairs.

For exact **new** coverage, use the certified PREFIX-897 four-family set
\[
E=\{(a,b):ab<33N\ \vee\ a\in U\ \vee\ b\in U\
 \vee\ \operatorname{lcm}(a,b)<N\
 \vee\ 33\lceil N/a\rceil>b\
 \vee\ 33\lceil N/b\rceil>a\},
\]
where the precise 552-element set \`U\` is reproduced in the checker. Let \`P4\` be the exact 256 first-port moduli in PREFIX-904, and let \`R=(P4 x Q) union (Q x P4)\`. The previous certificate is \`C904=E union R union D\`, size 7,632,945,416. The family \`G\` is disjoint from the gap family \`D\`. Hence its new contribution is exactly \`G_pairs minus (E union R)\`.

Complete enumeration of every one of the 27,852,791 **increasing** pairs (and its reverse) gives these ordered-pair totals:

| Count restricted to the new G gap family | Ordered pairs |
|---|---:|
| All two-power-gap pairs outside D | 55,705,582 |
| Already in E | 24,697,804 |
| Touching P4 (row or column) | 184,006 |
| In E and touching P4 | 2,250 |
| **Net new outside C904** | **30,826,022** |

Both exact calculations agree:
\[
55,705,582-24,697,804-184,006+2,250
=\boxed{30,826,022},
\]
\[
\boxed{|C905|=7,632,945,416+30,826,022=7,663,771,438}.
\]
The exact complement of this explicitly certified union in \`Q^2\` has \`9,516,097,746\` pairs. Being outside these sufficient-collision families is an unresolved status, **not** a claimed injective pair.

## Verification, provenance and method

- \`PREFIX905_R6_TWO_POWER_GAPS.cpp\`: C++17 \`-O3\` complete gap enumeration. It constructs and checks **27,852,791 witnesses** including both endpoints, named bit identities, XOR equalities and the two port congruences; it prints all 256 per-gap coverage rows.
- \`PREFIX905_R6_TWO_POWER_GAPS_RESULTS.csv\`: full, remotely published exact per-gap census; 256 data lines.
- \`PREFIX905_R6_INDEPENDENT_CHECK.py\`: an independent NumPy vector enumeration of all 256 gap slices with independently implemented membership and inclusion-exclusion tests; every CSV row matches.
- A third independent JavaScript full enumeration recalculated all counts and all 27,852,791 witnesses before writing the remote CSV. It agreed with the C++ and NumPy runs.
- Local environment: g++ C++17 and Python NumPy; exact integer arithmetic; all numbers used fit in exact integer ranges of the selected implementations. No floating-point approximation or random sampling occurs in the claimed census.
- Existing sources: PREFIX-903 dyadic-gap theorem and census, PREFIX-904 exact symmetric 256-panel union, PREFIX-897 prior collision family. These are reused as exact **certificate-set definitions**, not silently accepted beyond their scopes.
- This BRC observer is an auxiliary observation of provenance-bearing discrete trajectories, not a faithful representation of the entire X6 Cell/Link/Port state. P000, the ACTIVE six-dimensional native spatial worldview and separate time coordinate remain unchanged. GitHub publication establishes a research artifact, not Source Activity association, independent review or canonical admission.

## Next open scientific work

Use \`y=x+k a\` for integers \`k>=2\`: whenever \`k(a-b)=2^i ±2^j\` and the bounded endpoints fit in \`[0,N)\`, the same modular witness construction should extend the sufficient collision family to non-two-power \`a-b\`. Establish the exact admissible \`k\`-range, enumerate the genuinely new gaps, and de-duplicate them against \`C905\`. In parallel, continue the full carry/CRT checker on the remaining parameter pairs toward \`B_fix,odd(32) in {19,20}\`.
