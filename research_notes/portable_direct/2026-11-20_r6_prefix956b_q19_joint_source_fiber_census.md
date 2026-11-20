# PREFIX-956B — Exact Q19 non-diagonal dual-core named-fiber census and zero-residual stratum

Date: 2026-11-20. Predecessors: PREFIX-955 (the certified 6,203 non-diagonal modulus-pair IDs, three-quotient bound) and PREFIX-956 (named XOR source-fiber theorem). Frozen scientific input: \`f42f2906d77f24085c123f3ccfe9667d41caa96d\`.

**Status:** author-side exact finite-domain computation with checks against the original XOR equations, and a short universal conditional bound; independent Review/Source admission pending. **Scope:** auxiliary named XOR observer, not a verified native P000/Heartbeat/BRC space-time transport.

## 1. Original problem, population and retained histories

Strict 19-bit odd moduli \`Q19={262145,262147,...,524287}\`; \`(a,b)\` is an **ordered** pair. For each core \`k in {21,23}\`, retain all original named source-bit pairs \`(i,j)\`, \`0<=i,j<=18\`, with positive integer quotient \`t\` solving

\`\`\`text
( k*a XOR 2^j ) - 2^i = t*b.
\`\`\`

The complete input population is the **6,203 distinct off-diagonal pair IDs** in the previously published, source-checked \`PREFIX955_NONDIAGONAL_IDS.bin\` (49,624 little-endian bytes, SHA256 \`1caec71f97ddb97c60c8506629f65651f0f3030b3526aeca30195948ee0cff75\`). The code first verifies this file, sortedness and uniqueness, then directly scans each pair with \`19*19\` source-bit configurations for *each* core. Every realized quotient-fiber cardinality is independently checked using the PREFIX-956 exact signed/2-adic count. The input source's completeness is inherited from PREFIX-955; this run independently certifies **every named witness on every supplied pair**, rather than redoing global determinant candidate discovery.

For a modulus pair let \`F_k(t)\` be its exact named source-bit pair set, and \`C(a,b)=sum_{t,T}|F_21(t)|*|F_23(T)|\`. Both the quotient labels and the named histories are retained. Define the quotient gap \`m=T-t\`.

## 2. Complete finite census (exact)

| Statistic | Count |
|---|---:|
| Source-certified distinct off-diagonal Q19 pairs | 6,203 |
| Total joint named witness combinations \`sum C(a,b)\` | **8,649** |
| Pairs with total joint multiplicity 1 | 4,302 |
| Pairs with total joint multiplicity 2 | 1,685 |
| Pairs with total joint multiplicity 4 | 200 |
| Remaining pairs with total multiplicity 6–28 | 16 |
| Pairs with one or more single-core zero-offset quotient fibers | **16** |
| Nonzero-offset single-core quotient fibers with exactly two named witnesses, k=21 / k=23 | **1,058 / 1,029** |
| Zero-offset single-core quotient fibers, k=21 / k=23 | **9 / 7** |
| Maximum total joint named multiplicity on a single pair | **28** |

The **full histogram** of total joint source multiplicity per off-diagonal pair is:

\`\`\`text
{1:4302, 2:1685, 4:200, 6:2, 7:1, 8:7, 9:1, 10:1, 11:1, 20:1, 24:1, 28:1}
\`\`\`

The off-diagonal named joint witness combinations by quotient gap \`m=0,...,6\` are exactly

\`\`\`text
[6,614,6509,1286,231,3,0]   (sum=8649).
\`\`\`

The distinct off-diagonal pair memberships by gap are \`[6,442,4724,839,190,3,0]\`; one pair belongs to two gaps. The quotient-gap bit-mask histogram is \`{1:6,2:441,4:4723,6:1,8:839,16:190,32:3}\`. The unique off-diagonal pair with two gaps remains \`(278529,290817)\` with \`m=1,2\`; both are represented with original source histories. These statistics agree with the full named counts for PREFIX-955 after subtracting its 62 nonresonant **diagonal** named combinations.

An informative sharp observed source-residual example is

\`\`\`text
(a,b)=(475165,344085).
k=21: t=29, d=21*a-29*b=0; 14 different named witnesses (i=j at 14 zero bits of 21*a).
k=23: T=31, d=23*a-31*b=262160; 2 different named witnesses (i,j)=(18,4),(4,18).
Joint named combinations: 14*2=28; quotient gap m=2.
\`\`\`

Thus a single quotient-gap or Boolean collision label can erase 28 different named pairs-of-histories for this exact legal example.

## 3. New universal zero-residual classification and joint bound

**Lemma A (zero residual / exact ratio).** For any positive integers \`k,t,a,b\`, \`ka-tb=0\` iff \`k=g*k0,t=g*t0\`, with \`g=gcd(k,t)\`, \`gcd(k0,t0)=1\`, and \`(a,b)=(t0*r,k0*r)\` for an integer \`r>=1\`. For odd \`k,a,b\`, both \`t\` and \`r\` are odd. Restricting both moduli to \`Qp\` amounts to explicit inequalities on \`r\`: \`H<t0*r<2H\` and \`H<k0*r<2H\`, plus parity. The proof is the coprime divisibility lemma: \`k0 a=t0 b\` implies \`t0|a\`, \`k0|b\`, and hence the common multiplier.

**Lemma B (uniform count using PREFIX-955 and PREFIX-956).** Let \`p>=3\`, \`a,b\in Qp\`, \`k\` any positive odd integer. Denote the total number of source-bit witnesses over **all** positive integer quotient fibers by \`W_p(k;a,b)\`. Then:

- If no quotient \`t\` satisfies \`ka=tb\`, **\`W_p(k;a,b)<=6\`**.
- If some quotient \`t\` satisfies \`ka=tb\`, **\`W_p(k;a,b)<=p+3\`**.

Proof: PREFIX-955 gives at most 3 distinct quotient fibers. For nonzero residual each has at most 2 named witnesses by PREFIX-956; zero residual, if present, occurs at only one quotient and has \`p-popcount(ka mod2^p)<=p-1\` because odd \`ka\` has its lowest bit set. The remaining at most two quotients contribute at most 4. QED. This is a useful **uniform source-storage bound** for the auxiliary observer, not an assertion that the resulting minimal state is safe under arbitrary later time/branch composition.

## 4. Verification and reproducibility

The direct source scan enumerated all \`6,203*2*19*19=4,478,566\` possible named source-bit tests. Every legal positive quotient was retained; for each realized core/quotient fiber, the independent PREFIX-956 formula returned exactly the direct cardinality. Input and outputs use exact Python integers; the source pair ID decoding is \`id=((a-262145)//2)*131072+(b-262145)//2\`. The checker requires the stated binary input, supplied either raw or inside the earlier PREFIX-955 reproduction ZIP, and checks its SHA256 before arithmetic. The published JSON contains the complete histograms, zero-residual examples and the maximal pair. Additional complete per-pair CSV is not required for the quoted aggregate evidence but a future targeted audit can export it without rebuilding prior global W21/W23 sets.

The named overlap result is a **finite Q19 census conditional on the previously certified 6,203 source IDs**. The lemma on zero-residual ratios and the 6/(p+3) source-storage bound are proved for general p in the stated model.

## 5. Consequence and next research question

The main information-retention cost in the 6,203 off-diagonal joint pairs is concentrated in the 16 zero-offset ratio pairs. The second-multiplicity nonzero source fibers are a distinct 2-adic mechanism; both must remain as tagged, composable observations until a future-operation descent certificate exists. The project composite/joint observer constraint is preserved.

The next target is an analytic CRT/interval-sum formula for the **16** zero-offset stratum using Lemma A, coupled with the dyadic source-fiber formula for the remaining quotient classes, and then a direct source-preserving count of the **8,649** named combinations without full four-source-bit enumeration. This research produces no new different-moduli-pair coverage. The broader \`B_fix,odd(32) in {19,20}\` problem remains open.

Historical author provenance: \`EM-DIRECT-58C410\`, original SID \`MCP-31edc522830749ad8775ca012e02ef30\`, Activity \`RA-25432C4AAE9BF66A907F5115\`. New Activity association is pending verified legal CAS. No X6 CLAIM, independent mathematical Review or Foundation admission is asserted.
