# X6 Unit75 — adjacent-depth native BRC: shortest plus one backtrack coefficient determines every uniform path count

Date: 2026-11-17. Parent: \`PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905\`. Historical mother Task: \`RS-X6-LEGACY-PLANE-RECONCILIATION\`, immutable publication \`TP2-B4A441B23DA3159232C2\`. Scientific model **frozen** at P000 V5 signed six-axis Cell torsor \`awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03\`; historical comparison pin \`fd2bcff10ca6e147348b6c1236027fc0d2877df3\`.

Classification: **EXACT AUTHOR PROOF + EXECUTED FINITE INTEGER CENSUS / UNREVIEWED / NOT_ADMITTED**. This is a source-backed portable mathematical increment. It does **not** assert an X6 Source CLAIM, session adoption, native semantic PROGRESS, Result freeze, Driver review, or formal authorship by a previously recorded Researcher.

## 1. New universal theorem at adjacent native depths

Let \`z∈Z^6\` be a six-axis signed-native displacement from a chosen Cell and let \`w=z+D\`, where \`D=(1,1,1,1,1,1)\`. Define

- \`can6(z)=z−min_i(z_i)D\`, the min-zero **observer**, not native Cell identity;
- \`G(z)=Σ_i z_i²\`, the native quadratic readout;
- \`T(z)=Σ_i |z_i|\`, native shortest signed primitive-path length;
- \`C_L(z)\`, the number of all **ordered** six-axis signed ±unit-step words of length \`L\` ending at \`z\`, counted as nonnegative integers.

**Theorem U75-A (two-coefficient all-length sufficiency, adjacent depths):**

If \`G(z)=G(w)\` and \`T(z)=T(w)=T\`, then the following conditions are equivalent:

1. \`C_T(z)=C_T(w)\` **and** \`C_(T+2)(z)=C_(T+2)(w)\`.
2. The unordered six-element multisets \`{|z_1|,…,|z_6|}\` and \`{|w_1|,…,|w_6|}\` coincide.
3. \`C_L(z)=C_L(w)\` for **every** integer \`L≥0\`.

This statement retains the native signed six-axis domain and is about **uniform unlabelled positive path counts**. Named-axis, direction-labelled, port/provenance and signed/amplitude observers remain separate interfaces.

The shortest count \`C_T=T!/Π_i|z_i|!\` and first backtrack count
\`C_(T+2)=C_T(T+1)(T+2)Σ_i1/(|z_i|+1)\`
are exact original native BRC quantities. The second formula was already available in Unit74; the new result is the sufficiency/equivalence for **all lengths** under the adjacent-depth hypotheses.

### Proof

First, \`G(w)−G(z)=2Σ_i z_i+6\`, hence \`Σ_i z_i=−3\`. For integer \`u\`, the increment \`|u+1|−|u|\` equals \`+1\` if \`u≥0\` and \`−1\` if \`u<0\`. Thus equality of \`T\` forces **exactly three nonnegative and three negative native components**.

On the three nonnegative components put \`A_i=z_i+1≥1\`; on the three negative components put \`B_j=−z_j≥1\`. The sum condition becomes

\`S:=A_1+A_2+A_3=B_1+B_2+B_3\`.

The absolute-component multisets of \`z,w\` are therefore respectively
\`{A_1−1,A_2−1,A_3−1,B_1,B_2,B_3}\` and
\`{A_1,A_2,A_3,B_1−1,B_2−1,B_3−1}\`.

The ratio of shortest counts is exactly
\`C_T(w)/C_T(z)=(B_1B_2B_3)/(A_1A_2A_3)\`.
Under condition (1), the products are equal:
\`P:=Π_i A_i=Π_j B_j≥1\`.

Write \`R_1(v)=Σ_i1/(|v_i|+1)\`, so the already-established first-excess identity shows that equality of \`C_(T+2)\` is equivalent to \`R_1(w)=R_1(z)\`, because \`C_T\` is nonzero and equal. Subtraction gives

\`R_1(w)−R_1(z)=F(B)−F(A)\`, with
\`F(x_1,x_2,x_3)=Σ_i1/[x_i(x_i+1)]\`.

For any positive triple with sum \`S\`, product \`P\`, and second elementary symmetric sum \`E=x_1x_2+x_1x_3+x_2x_3\`, the exact rational identity is

\`F(E)=E/P−(E+2S+3)/(P+E+S+1)\`.

**Strict injectivity in E at fixed S,P.** For \`E_2>E_1≥0\`, direct subtraction yields

\`F(E_2)−F(E_1)=(E_2−E_1)[1/P−(P−S−2)/((P+S+1+E_1)(P+S+1+E_2))]\`.

The square bracket is strictly positive: if \`P−S−2≤0\`, immediately so; otherwise each denominator factor is strictly larger than \`P\`, and \`0<P−S−2<P\`, making the second term strictly less than \`1/P\`. Hence \`F(A)=F(B)\` implies \`E(A)=E(B)\`.

Both triples now have the **same** \`S,E,P\`, so they are the same multiset of roots of \`X³−SX²+EX−P\`. Consequently \`{A_i}={B_j}\` as unordered positive triples. Their shifted/non-shifted union descriptions above show that \`{|z_i|}={|w_i|}\`; thus (1) implies (2).

For any integer \`k≥0\`, the native exact all-length count with \`a_i=|z_i|\`, \`T=Σa_i\` is

\`C_(T+2k)(z)=(T+2k)! Σ_{q_1+⋯+q_6=k} Π_{i=1}^6 1/[q_i!(a_i+q_i)!]\`.

The right-hand side is symmetric in the absolute-axis multiset. All other lengths have zero count. Therefore (2) implies (3). Finally (3) trivially implies equality of the two coefficients in (1). **QED.**

### Exact information consequence

Within an adjacent-depth double fiber, the additional **first nonminimal** positive BRC count is a sufficient discriminator for whether the *entire uniform positive path-count series* factors through the passive min-zero/G/T/shortest-count observer. A difference in this coefficient proves the saved shortest count inadequate. When both counts agree, no further **uniform all-length** count is needed for this particular fiber; sign- or axis-sensitive operations must retain their own information.

## 2. Required witness: Unit74's other adjacent-depth pair

\`z=(-8,-3,-3,1,5,5)\`, \`w=(-7,-2,-2,2,6,6)=z+D\`.

Both have \`can6=(0,5,5,9,13,13)\`, \`G=133\`, \`T=25\`, and \`C_25=742096122768000\`. The positive triples above are \`A=(2,6,6)\`, \`B=(8,3,3)\`, with \`S=14\`, \`P=72\`, but \`E_A=60≠E_B=57\`. Hence the first-excess counts must diverge:

- \`C_27(z)=752485468486752000\`;
- \`C_27(w)=734913692436924000\`;
- \`R_1(w)−R_1(z)=−17/504\`;
- \`C_27(w)−C_27(z)=−17571776049828000\`.

These numbers reuse the already verified Unit74 original-code witnesses; the new theorem explains **why** the second coefficient is complete for the adjacent-depth uniform series, not merely why this witness differs.

## 3. Actually executed independent finite census

Reproducible standard-library checker:
\`research_checks/X6_UNIT75_ADJACENT_DEPTH_TWO_BRC_COEFFICIENT_CLASSIFIER_20261117.py\`, immutable commit \`1203451da496e85ba1ca57d577f1d79747c342f0\`, Git blob \`5021b4252b684d36f0b72449b7cc57f6dedf695b\`.

Actually emitted JSON certificate:
\`research_checks/X6_UNIT75_ADJACENT_TWO_COEFF_RESULTS_20261117.json\`, immutable commit \`c75f051eb7ee3b9d654a5fe3059e7ae0e911b5a5\`, Git blob \`2a02c4efbdfb1a5d4ae8e1ca690e01ca5039eec9\`, file SHA256 \`9f27775e6fcf20d15129c89c20c986063c35c7fcb5f41fc02b026d726a68a109\`.

Executed \`python checker.py --max-M 20 --output certificate.json\`, and executed \`-O\`, \`-OO\` modes with \`--max-M 8\`; all completed with zero assertion- or exception-level failures. Certificate's semantic SHA256 (excluding optimization-mode metadata) for M20: \`fb99a53bebb26ad192db5f1905556c4fe3838635a6e63e62f9f8cbbfde9a4493\`. The code uses explicit \`raise\` conditions, never removable \`assert\`, and exact integer/fraction arithmetic.

Each M scan covers **all coordinate-permutation representatives** \`z_1≤⋯≤z_6\`, \`z_i∈[-M,M]\`, all distinct positive integer depth shifts \`c=-Σ_i z_i/3\` satisfying \`w=z+cD∈[-M,M]^6\`, and then checks \`G,T,C_T,C_(T+2)\` exactly. Completeness follows because simultaneous coordinate permutations preserve these uniform observations, and the G identity uniquely determines c for any fixed z. This is a **finite cube** claim, not a universal extension to \`c>1\`.

| M | Sorted input representatives | G,T,shortest-count equal pairs | Different absolute multisets | Such pairs with same first-excess count |
|---:|---:|---:|---:|---:|
| 8 | 74,613 | 662 | 2 | 0 |
| 12 | 593,775 | 2,754 | 24 | 0 |
| 16 | 2,760,681 | 7,814 | 62 | 0 |
| 20 | 9,366,819 | 17,830 | 120 | 0 |

At M20, **1,628** shortest-count-equal pairs have adjacent depth \`c=1\` and satisfy the independent positive-triple/e2/F(E) check. Of these, 88 have different absolute multisets, and every one is distinguished by the first-excess coefficient. This supports, but is not needed for, the all-integer proof.

An optional \`M=28\` extended attempt in this turn exceeded the local runner limit and did **not** emit a certificate; only the completed M≤20 rows are attributed to this checker.

## 4. Source/recovery boundary and mother work

Unit74's **original** native request \`onhour-20261117-unit74-full6-shortest-equal-plus2-native-progress-v1\` was read through \`em_control_result\` in this run and has the authentic terminal **SUCCEEDED / SOURCE_CHECKPOINT_PUBLISHED**, \`canonical_publication_verified=true\`, \`authenticated_readback=true\`, Source commit \`cc3368100f8de3b00c89b7f4d1567f008b9944c4\`. This supersedes the prior local QUEUED end-state; it was consumed, not replayed.

The ordinary GitHub Chat \`recovery_status\` at logical label \`chatgpt-research-onhour-enterprise-math-20260923\`, request \`onhour-20261117-0503-recovery-status-x6-v1\` / bridge Issue #6991, returned a **D25** active session \`MCP-de3e5bafb24f43f4a5e6285e7601676a\` and no X6 run. A bridge-only \`receipt\` request for the Unit74 native ID was correctly rejected \`CHAT_REQUEST_NOT_FOUND\`, whereas the native Source read confirms its success. This is a transport/subject identity split, **not** a reason to adopt the D25 session for X6. A separate exact native X6 continuation read \`onhour-20261117-0504-x6-source-continuation-read-v1\` remains in a read-only retry/queue until terminal. Current X6 write authority and ownership have not been established by this run. **No new X6 CLAIM, resume, Activity #99, or semantic PROGRESS was submitted.** This new note/checker/certificate is Source GitHub scientific evidence pending authorized Activity and Native linkage; old Activity #98 remains untouched.

Remaining exact obligations: resolve/consume the pending **read-only** X6 continuation via its original request ID; inspect the actual LP011 purported signed-native singleton-argmax and LP019 purported subtraction of positive path-multiplicity *historical source:line*, or preserve their evidence-limited unresolved classification; close the remaining live 28-LP consumer dependencies and obtain independent Driver \`REQUEST_REVISION\` disposition. Keep the original frozen R063/Helly runs, accepted results and P000 unchanged. **Next scientific direction:** test whether the two-coefficient sufficiency above extends to \`c>1\` by deriving a full algebraic criterion for intermediate sign-crossing coordinates; the completed M≤20 census gives a bounded positive probe but not a universal proof.

This work is an independent proof increment under the existing mother scientific question, with documented session/source limits; no scheduler, notification or separate lane identity has been changed.
