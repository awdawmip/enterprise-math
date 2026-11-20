# PREFIX-955 — Sharp three-quotient fiber bound and Q19 two-core gap rigidity

Date: 2026-11-20. Frozen scientific input: \`f42f2906d77f24085c123f3ccfe9667d41caa96d\`. Predecessors: PREFIX-948 (determinant classification), PREFIX-952–954 (named-source multiplicities). Scope: auxiliary named-XOR two-port observer, not native X6/BRC/Heartbeat time evolution. Status: author proof and two exhaustive finite calculations; independent mathematical Review and Activity linkage pending.

## 1. Universal sharp quotient-fiber theorem

Let \`p>=3\`, \`H=2^(p-1)\`, \`Q_p={H+1,H+3,...,2H-1}\`. Fix any positive integer core \`k\` and odd \`a,b in Q_p\`. Define \`T_p(k;a,b)\` as the set of positive integer quotients \`t\` for which some named pair \`(i,j)\`, \`0<=i,j<p\`, solves

    (k*a XOR 2^j) - 2^i = t*b.

**Theorem.** All elements of \`T_p(k;a,b)\` lie within an interval of at most three consecutive integers. The bound three is sharp, already for p=4.

**Proof.** Put \`sigma=1-2*bit_j(k*a)\`, \`c=2^i-sigma*2^j\`. The source-preserving XOR identity is \`k*a-t*b=c\`. Every legal \`c\` lies in the closed integer interval \`[1-2^(p-1),2^p]\`. The span is \`3*2^(p-1)-1=3H-1\`, strictly less than \`3b\` because \`b>=H+1\`. For any two solutions, \`(t_1-t_2)*b=c_2-c_1\`, so \`|t_1-t_2|<3\`, hence at most 2. Therefore the possible quotients occupy a subset of three consecutive integers. The example \`(p,k,a,b)=(4,3,13,9)\` supplies all three values: \`t=3\` via \`(i,j)=(3,2)\`; \`t=4\` via \`(1,0)\` or \`(0,1)\`; \`t=5\` via \`(1,3)\`. Each satisfies the original XOR equation, proving sharpness. QED.

The theorem bounds distinct quotients at fixed core and modulus pair, not the number of distinct named \`(i,j)\` witnesses. It relies on the auxiliary XOR observer and does not identify a native X6 state.

## 2. Exact nonresonant gap census for cores 21 and 23

Fix \`p=19\`, \`Q19={262145,262147,...,524287}\`, cores \`21,23\`. A joint named collision consists of the pair

    (21*a XOR 2^j) - 2^i = t*b,
    (23*a XOR 2^J) - 2^I = T*b,

with \`0<=i,j,I,J<=18\` and positive quotients. Set \`m=T-t\`, \`s=1-2*bit_j(21a)\`, \`S=1-2*bit_J(23a)\`, \`c=2^i-s*2^j\`, \`C=2^I-S*2^J\`, and \`d=23*t-21*T=2*t-21*m\`. From the two integer-linear equations,

    21*a-t*b=c,    23*a-T*b=C,

one obtains the exact inverse whenever \`d!=0\`:

    a=(t*C-T*c)/d,
    b=(21*C-23*c)/d.

This is the PREFIX-948 determinant identity, with source-bit signs retained. The exhaustive quotient bounds \`1<=t<=42\`, \`1<=T<=46\` and \`0<=m<=6\` were proved for this strict domain in PREFIX-947A. For the new census, enumerate all possible signed-source terms, \`t\`, and \`m\`, skip \`d=0\`, compute these two integer fractions, and check: both divisions exact, odd \`a,b\` in Q19, actual source bits equal the declared signs, both original XOR identities exact, positive right sides and legal 32-bit endpoints. Sorting pair IDs then gives every possible **nonresonant** joint modulus pair, with its precise set of quotient gaps.

The original source witness count and gap membership results are:

| gap m | named joint witness combinations | distinct nonresonant ordered pairs | distinct non-diagonal pairs |
|---:|---:|---:|---:|
| 0 | 6 | 6 | 6 |
| 1 | 644 | 443 | 442 |
| 2 | 6,513 | 4,725 | 4,724 |
| 3 | 1,314 | 840 | 839 |
| 4 | 231 | 190 | 190 |
| 5 | 3 | 3 | 3 |
| 6 | 0 | 0 | 0 |

These gap memberships include repeats when a modulus pair supports more than one gap. Across all gaps there are **6,204 distinct nonresonant pairs**: exactly one diagonal \`(262145,262145)\` and **6,203 non-diagonal pairs**. Among the latter, 2,563 have \`a<b\` and 3,640 have \`a>b\`.

**Finite gap-rigidity certificate.** Of the 6,203 non-diagonal pairs, **6,202 support exactly one nonresonant quotient gap**. The unique multiple-gap pair is \`(a,b)=(278529,290817)\`, supporting gaps \`m=1\` and \`m=2\`. Source-retaining witnesses:

- \`m=1\`: core21 \`(t,i,j)=(21,12,18)\`; core23 \`(T,I,J)=(22,13,0)\`.
- \`m=2\`: core21 \`(t,i,j)=(20,15,0)\`; core23 \`(T,I,J)=(22,13,0)\`.

The single nonresonant diagonal \`(262145,262145)\` has gap mask \`{1,2,3}\`. The exact mask histogram (mask as bitset \`sum 2^m\`) is

    {1:6, 2:441, 4:4723, 6:1, 8:839, 14:1, 16:190, 32:3}.

Mask 6 is the unique off-diagonal double-gap, and mask 14 is the one diagonal triple-gap. The sum of gap memberships, 6,207, exceeds the 6,204 distinct pairs by exactly these three additional memberships. Hence uniqueness is a **precise finite-domain result**, not a general uniqueness theorem. The off-diagonal shared-collision pair population of 6,203 is unchanged from PREFIX-948.

## 3. Reproduction, independent calculation, and exact byte identity

**Determinant method.** Run \`g++ -O3 -std=c++17 PREFIX955_R6_NONRESONANT_GAP_CENSUS.cpp -o prefix955 && ./prefix955\`. It generates and deduplicates only the nonresonant pair candidates; it does not read an earlier W21/W23 binary as input. It writes \`PREFIX955_NONDIAGONAL_IDS.bin\` (6,203 ordered pair IDs; 49,624 bytes) and \`PREFIX955_W21_W23_INTERSECTION_IDS.bin\`. The latter combines the proven 131,071 resonant diagonal pairs with newly generated non-diagonals, and deduplicates by sorted ID.

**Independent direct-XOR verification.** After running the C++ program, execute \`python PREFIX955_R6_DIRECT_PAIR_GAP_VERIFY.py\`. The Python program reads the newly generated 137,274 pair IDs, and for each of those pairs enumerates each of the 361 original \`(i,j)\` configurations for both cores, directly tests divisibility by \`b\`, derives the exact quotient sets, forms every nonresonant \`m\`, and reproduces all seven raw witness counts, seven pair-membership counts, eight masks and the exceptional diagonal. It does **not** use the determinant formula or signed-source enumeration for its verification.

**Immutable byte checks.** Pair ID is \`id=((a-262145)/2)*131072+(b-262145)/2\`, serialized as little-endian unsigned 64-bit integers. The non-diagonal 49,624-byte file has SHA-256

    1caec71f97ddb97c60c8506629f65651f0f3030b3526aeca30195948ee0cff75

The full 1,098,192-byte file has SHA-256

    54c35a06874167484f0028443be45d3b03e69bc3bdf0e64fc97cf371522f6223

The latter agrees exactly with the previously independently generated complete \`W21 ∩ W23\` stream in PREFIX-948. The full-file assembly uses that prior proven resonant-diagonal classification; the direct Python routine checks actual original named equations for every reconstructed pair. All arithmetic is exact integers. Observed local runtimes for these versions: C++ computation 0.38 seconds (excluding compile/startup), independent Python scan 15.74 seconds, not an end-to-end benchmark.

The finite computation proves the quoted finite totals when run and checked under the stated input semantics. The universal three-quotient statement above has a standalone proof. Neither is claimed to have independent mathematical review or formal Source admission.

## 4. Residual significance and next direction

For the auxiliary named observer, the quotient-gap value is **almost uniquely identified by a non-diagonal shared pair** in Q19, with exactly one certified ambiguity. The ambiguous pair must retain both named witness histories: collapsing to an unqualified one-gap label would discard a real future-relevant multiplicity. The next tractable question is to count nonresonant gap classes directly by \`(m,d,source-bit residue)\` using CRT/floor sums, avoiding enumeration of the 150-million-ish raw signed-source configurations. The three-quotient theorem bounds quotient fibers per core and can reduce candidate cross-products.

Scientific model is still auxiliary; no new native BRC/Heartbeat physical rotation relation is inferred. The mother question \`B_fix,odd(32) in {19,20}\` remains open. This result does **not** increase the distinct-pair certificate union.

Historical R6 provenance: Researcher \`EM-DIRECT-58C410\`, SID \`MCP-31edc522830749ad8775ca012e02ef30\`, Activity \`RA-25432C4AAE9BF66A907F5115\`. These recorded names are source attribution, not a fresh private capability or live shared-task CLAIM. Source Activity linkage and independent review are pending.
