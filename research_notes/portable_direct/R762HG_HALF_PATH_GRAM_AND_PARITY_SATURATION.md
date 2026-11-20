# R762HG — Positive-BRC half-path Gram formula, finite parity saturation to 12 events, and an infinite centered-support theorem

Status: **AUTHOR-PROVED (algebraic statements) / EXACT FINITE ENUMERATION (m<=12) / NOT_REVIEWED**.
Formal Task: \`RS-X6-TRIADIC-CLOSURE-DYNAMICS\`; immutable publication \`TP2-8B7E13C5904A2D6F1142\`.
Same research line: \`EM-X6-3050F6\`; predecessor R762HF at \`dddb76441cae8928afcc9e9d9eddda53275ab869\`. Frozen P000 input: \`a72226e2430ffa4786321ac86e7f0c599d5f0389\`.
These are exact conclusions about the already defined **candidate signed Port composite language**, not native primitive \`TRIADIC_CLOSURE_E\` admission. There are six signed spatial Cell coordinates relative to a chosen Cell, and a separate ordered event index. The observer below does not collapse Port histories or positive BRC multiplicity.

## Definitions and newly proved all-length half-path identities

Let \`X={0,...,5}\`, let \`P*={0,1}\`, and let Port states be all 15 two-element subsets of \`X\`. A single unsigned source step \`P->Q\` is allowed when \`|P∩Q|=1\` and has **named triple support** \`S=P∪Q\`. Its signed choice \`sigma=+1/-1\` adds \`sigma*h_S\` to a six-component Cell displacement, where \`h_S=sum_{i in S}e_i\`. This triple is a labeled composite support, not a native one-axis primitive segment.

For any unsigned Port walk \`w\` of length \`m\` from \`P*\` back to \`P*\`, let \`n(w)\` be the number of ordered sign choices with total signed displacement zero. Define:
- \`U_m\`: unsigned Port-return histories;
- \`H_m\`: histories whose XOR of all six-bit support masks equals zero;
- \`F_m\`: histories with \`n(w)>0\`;
- \`Z_m=sum_w n(w)\`: signed positive-BRC return multiplicity.

For each half-length \`n\`, define \`a_n(p,r)\` as the **positive integer number** of signed length-\`n\` paths from \`P*\` to Port \`p\` with six-axis signed sum \`r∈Z^6\`. Define \`b_n(p,eta)\` as the number of unsigned such paths with XOR-of-supports mask \`eta∈(Z/2)^6\`. Define \`V_n(p,eta)\` as the collection of signed sums attainable by any unsigned half-history of the specified endpoint and mask; more precisely keep each individual history's set \`V(w)\` for the support predicate.

**Theorem HG1 (all lengths, positive Gram factorization):**
\`\`\`text
Z_(2n) = sum_{p,r} a_n(p,r)^2 ;
H_(2n) = sum_{p,eta} b_n(p,eta)^2 .
\`\`\`
Proof. Reverse the second half of a return walk. Reversal preserves each named three-support label and converts a length-\`2n\` return uniquely into an ordered pair of half-histories starting at \`P*\`, ending at the same middle Port \`p\`. Signed return of the concatenation requires the two signed half-sums to be negatives. Global sign inversion is a bijection between half-histories of sum \`r\` and \`-r\`, so the signed multiplicity is \`sum a_n(p,r)^2\`. The total six-bit parity is zero exactly when the two half-parities agree; this gives \`sum b_n(p,eta)^2\`. Every summand is a nonnegative integer, so the factorization does not interpret physical sign reversal as cancellation of BRC source mass.

**Theorem HG2 (Boolean intersection criterion):** For two unsigned length-\`n\` halves \`u,v\` with the same final Port and XOR mask, the full return made from \`u\` followed by the reverse of \`v\` has a signed zero-Cell completion **iff**
\`\`\`text
V(u) ∩ V(v) != empty,
V(w) = { sum_{j=1}^n epsilon_j*h_(S_j) : epsilon_j in {+1,-1} }.
\`\`\`
Indeed \`V(v)=-V(v)\` by the sign-flip involution. Thus the parity condition is sufficient for *all* length-\`2n\` return walks iff every pair in each common \`(middle Port, XOR mask)\` bucket has intersecting attainable signed-sum sets.

## Theorem HG3: finite parity saturation extended to twelve events

Using the exact half-path criterion and complete enumeration of all \`8^n\` named unsigned half-histories for each \`n=1,2,3,4,5,6\`, every pair in the same endpoint/mask bucket has a nonempty signed-sum intersection. Therefore
\`\`\`text
F_m=H_m   for m in {0,2,4,6,8,10,12}.
\`\`\`
All possible parity-zero full return histories are covered without enumerating \`8^(2n)\` full walks: the checker explicitly compares each unordered pair once, because intersection is symmetric. It never collapses named Port paths into distinct-support multisets.

| m | U_m | H_m=F_m | Z_m |
|---:|---:|---:|---:|
| 0 | 1 | 1 | 1 |
| 2 | 8 | 8 | 16 |
| 4 | 288 | 168 | 624 |
| 6 | 17,536 | 4,960 | 34,688 |
| 8 | 1,118,720 | 177,536 | 2,413,424 |
| 10 | 71,583,744 | **7,289,184** | **200,986,368** |
| 12 | 4,581,302,272 | **333,869,824** | **19,705,107,552** |

The new finite counts are at lengths 10 and 12. The earlier m<=8 window is consumed from R762HF, and independently matched by the new half-path method. At n=5, exactly 32,768 half paths yield 3,660,976 unordered compatible pairs (7,289,184 ordered pairs); at n=6, 262,144 half paths yield 167,065,984 unordered compatible pairs (333,869,824 ordered pairs). **Zero compatible pairs failed the signed-set intersection test** in either case. A separate exact positive-state dynamic program computed the signed \`Z_10,Z_12\`, and a parity DP computed \`H_10,H_12\`. Finite coverage is exhaustive, not statistical, and these are candidate-language statements only.

## Theorem HG4: infinite common-axis support family

Suppose all labeled triple supports \`S_t\` in an *arbitrary* length-\`m\` source sequence contain a fixed axis \`c∈X\`. If each of the six coordinates occurs an even number of times, then the sequence admits signed labels making all six signed sums exactly zero, for **every** length \`m\`.

Proof. Remove \`c\` from each triple and regard the remaining two axes as an edge of a loopless multigraph \`G\` on the five vertices \`X\{c}\`, retaining edge occurrences separately. Even coordinate-incidence counts imply all vertex degrees in \`G\` are even. The total incidence over all six coordinates equals \`3m\`, so \`m\` is even. Every nonempty connected Eulerian component of odd edge-count uses at least three distinct vertices: a loopless one- or two-vertex Eulerian multigraph necessarily has even edge-count. Two disjoint odd-edge components would therefore require at least six vertices, while \`G\` has only five. Since \`m\` is even, the number of odd-edge components is even, hence none exists. Every component has an even number of edges. Traverse an Euler circuit in each component and color its successive edges alternately \`+,-,+,-,...\`. At each vertex, entrance/exit edge pairs have opposite colors; the first/last pair at the circuit basepoint is also opposite because the circuit length is even. Thus the signed degree at each noncentral vertex vanishes. Each component also has the same total number of positive and negative edges, so the signed count of central axis \`c\` vanishes. QED.

This **unbounded-length theorem** holds for any support word meeting the common-axis condition; in particular it applies to every Port-admissible closed walk with that property. It does not claim that all Port paths share a common axis.

## Certificate specification / reproducibility

- \`R762HG_HALFPAIR_CHECK.cpp\`: enumerates all named Port half histories for lengths 1 through 6. For each half, retains endpoint, full ordered port/support list, XOR mask, and exact set of six-coordinate signed sums (encoded injectively in six four-bit lanes as \`sum_i+8\`, valid for half-length <=6). Tests all same-bucket unordered pairs by a sorted two-pointer set intersection, and reports a concrete counterexample if found. The identity \`H_(2n)=sum b_n^2\` checks exhaustive coverage.
- \`R762HG_POSITIVE_DP.py\`: independently computes \`U,H,Z\` using positive integer recurrences on \`(Port,parity)\` and \`(Port,signed X6 vector)\`. The latter is exactly the typed signed-source extension, not a signed-mass cancellation operation.
- \`R762HG_EVIDENCE.json\`: executable claim boundary, all exact integer outputs and coverage observations.

Author-side C++17 enumeration (optimized build) and independent Python3 exact DP both ran successfully; see evidence. The uploaded sources are plain UTF-8 reproductions of the described checks; independent CI/mathematical review has not been obtained. The task's native \`TRIADIC_CLOSURE_E\` force incidence/Link/Port/time permission remains open; no new native result/review/foundation promotion is claimed.

## Next scientific unit

Determine whether the \`V(u)∩V(v)\` property holds for **all** half-lengths in the Port language, or find a shortest finite false-positive with an explicit ordered named Port word, its six-bit parity evidence and a disjoint signed-sum certificate. Test further structural families (e.g. all supports not sharing one axis) without replacing the frozen P000 universe. Separately construct a typed native \`TRIADIC_CLOSURE_E\` permission and distinguish its allowed language from the candidate signed Port composite language. Preserve exact prior progress receipts and current Researcher/Activity attribution.
