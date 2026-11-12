# X6 LP028 — R063 all-pair support-two glue, exact axial overlap correction and downstream typed scope

2026-11-12; **AUTHOR_PROVED / EXACT_FINITE_CHECK_EXECUTED / NONBLIND / UNREVIEWED / NOT_ADMITTED / PORTABLE_RESEARCH_ONLY**.

Mother Task: \`RS-X6-LEGACY-PLANE-RECONCILIATION\`, immutable publication \`TP2-B4A441B23DA3159232C2\`; P000 V5/source pin \`59538f585d037d09ef687b28715c4bc1a3f9fe03\`; old comparator \`fd2bcff10ca6e147348b6c1236027fc0d2877df3\`. This source preserves the 2026-11-12 existing highest frontier: six-root positive R063, signed two/three-axis certificates, and the full six-axis \(N=2500\) exact shell certificate. No original native experiment or frozen Stage 0–4 route is rerun or revised.

## 1. Question and typed construction

The frozen R063 Stage 0 source, \`definitions/ENTERPRISE_PATH_VALUED_SQUARE_ROOT_OPERATOR_20260821.md\` (current blob \`61f23f2bcf965aa21d093ae3e35c0d6cb70610b7\`, §§4–9), provides the ordered nonnegative **two-component** root set

\[
R_r=\{(a,b)\in\mathbb Z_{\ge0}^2:a^2+b^2=r^2\},\quad r\in\mathbb Z_{>0},
\qquad P_r=\sum_{(a,b)\in R_r}\binom{a+b}{a}.
\]

At a chosen Cell anchor in the pinned signed X6 torsor, take **every unordered pair of distinct native axes** \(\{i,j\}\subset\{1,\dots,d\}\), where \(d\ge2\), and embed each root by \(a e_i+b e_j\). The positive union \(U^+_{d,r}\) is a set of axis-labelled endpoints, not a disjoint sum of pair-chart copies. The signed union \(U^\pm_{d,r}\) also independently permits a minus sign on every nonzero component. Its shortest native step-word multiplicity is

\[
B(x)=\frac{(\sum_k|x_k|)!}{\prod_k|x_k|!}.
\]

The only native application here is \(d=6\); arbitrary \(d\) states the combinatorial lemma used to check it. These are **derived, support-at-most-two static subfamilies**. They are not an already declared global pair-sector atlas, nor Stage 3–4 multiplicative process gluing, nor final Cell-address encoding.

## 2. All-pair glue theorem (every \(r>0\), \(d\ge2\))

Write \(K_r=|R_r|-2\). The two roots \((r,0)\) and \((0,r)\) are axial, and every other root has two nonzero components. Then:

\[
\boxed{|U^+_{d,r}|=d+\binom d2K_r,\qquad
 \sum_{x\in U^+_{d,r}} B(x)=d+\binom d2(P_r-2)}
\]

\[
\boxed{|U^\pm_{d,r}|=2d+4\binom d2K_r,\qquad
 \sum_{x\in U^\pm_{d,r}}B(x)=2d+4\binom d2(P_r-2).}
\]

**Proof.** A support-two endpoint determines its unique two labelled nonzero axes. Hence distinct pair charts never duplicate these endpoints. For each pair and each ordered nonaxial root, there is one positive endpoint or exactly four signed endpoints, with \(B=\binom{a+b}{a}\). A positive axial endpoint \(r e_i\) occurs in **each of the \(d-1\) pairs** containing \(i\), but represents one endpoint and one one-letter-type shortest path; its signed variant \(-r e_i\) has the same property. There are \(d\) positive or \(2d\) signed unique axial endpoints. Partitioning the union into support-one and support-two cases gives all four identities. No geometric plane, time evolution or Gaussian multiplication is introduced. QED.

Thus naïvely adding positive pair-chart root counts overcounts the union by \(d(d-2)\), and naïvely adding signed pair-chart endpoint counts overcounts by \(2d(d-2)\). For both endpoint cardinality and shortest-word mass the excess is **exactly** the repeated axial contribution, as axial paths have multiplicity one. For \(r=0\) every chart collapses to the same zero endpoint and a different formula is required; the theorem deliberately takes \(r>0\).

## 3. Exact \(N=2500\), full six-axis support-two certificate

Use the previously frozen R063 roots \((0,50),(14,48),(30,40),(40,30),(48,14),(50,0)\), for which \(|R_{50}|=6\), \(P_{50}=110695538274255714208\). With \(d=6\) and \(\binom62=15\):

| Observer and population | Unique endpoints | Total shortest BRC words |
| --- | ---: | ---: |
| All 15 pair charts, positive union | 66 | 1660433074113835713096 |
| All 15 pair charts, signed union | **252** | **6641732296455342852372** |
| Naïve signed disjoint pair-chart sum | 300 | 6641732296455342852420 |
| Exact signed overlap correction | **48** | **48** |

The 252 signed endpoints partition into **12 support-one** and **240 support-two** endpoints, matching the corresponding two rows of the independent full six-axis shell census at \`research_notes/X6_LP028_R2500_FULL_NATIVE_SHELL_AND_R063_CALLER_20261112_ONHOUR.md\` (blob \`1c32bfc1432c3420ea0570da09d7f83a2513fc70\`). That earlier census gives 102539052 total shell endpoints and total BRC mass

\`46263931428930653590904265855801056735441499817749479001025131238806458196360489958119492948372\`.

Subtracting the **new exact support-at-most-two union** gives the support-three-through-six complement:

- **102538800** signed endpoints;
- BRC word mass **46263931428930653590904265855801056735441499817749479001025131238806458189718757661664150096000**.

These differences are direct exact integer consequences of two independently constructed certificates; the full six-axis census itself was consumed, not rerun. For the smaller anchor \(r=5\), the derived signed \(d=6\) union has 132 endpoints and BRC mass 4212, giving a second transparent regression case.

## 4. Real downstream lineage and LP ledger update target

The following *actual* Source files distinguish a legitimate historical dependency from a current native claim:

| Exact Source | Evidence and typing | Action in LP revision |
| --- | --- | --- |
| \`definitions/ENTERPRISE_PATH_VALUED_SQUARE_ROOT_OPERATOR_20260821.md\` blob \`61f23f2b\`, lines 13–17, 87–119, 155–168 | Active/frozen R063; \`Sigma_O^(ij)\` still appears as a purported native start incidence; six two-generator positive roots and binomial counts remain exact | LP026/LP028: preserve root algebra; retype current Cell-start path interface and fixed positive two-generator population; no unilateral change to frozen definition |
| \`definitions/ENTERPRISE_NATIVE_LINE_TRACE_FORMULA_20260821.md\` blob \`94f47061\`, lines 14–22, 56–76 | Current R061 retyping: support-two is composite, \`Sigma_O\` is a historical carrier incidence | LP002/LP028: use as current typed source for the R063 native path adapter |
| \`definitions/ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md\` blob \`97ab1403\`, lines 19–35, 51–69 | Current R062 requires signed Cell-to-Cell words and \(\sum|d_i|\) shortest steps | LP019/LP026: retain positive integer BRC mass; keep signs/provenance separate from cancellation |
| \`research_notes/TOOL_DISCOVERY_NATIVE_GEOMETRY_OF_NUMBERS_MINIMA_CALCULUS_RESULT_20260822.md\` blob \`e3b1488a\`, §10; executable \`experiments/tool_discovery_native_geometry_of_numbers_minima_calculus_20260822.py\` blob \`643b2bac\` | Actual historical direct consumer of \`GRoot_E\`, \`PathSqrt_E\`, \`Lambda\`; its trace-fiber compression is valid on six positive two-generator branches | LP028: preserve six-fiber result within declared population; a claim about all support-two X6 requires the new 15-chart overlap law |
| \`driver_reviews/R063_STAGE1_GENERAL_PATH_NORM_ROOT_DRIVER_REVIEW_20260821.md\` blob \`2870c18f\` | Stage 1 accepted complete integer support on historical R061 two-axis sector scope | Consumer lineage; do not reopen factorization |
| \`driver_reviews/R063_STAGE2_MULTIPLICATIVE_PATH_NORM_ROOT_PROVENANCE_DRIVER_REVIEW_20260822.md\` blob \`2e7440d4\` | Stage 2 distinguishes Gaussian/unit-orbit provenance from path multiplicity and accepts an oriented derived product | Consumer lineage; its monoid is not a full-X6 native operation |
| \`driver_reviews/R063_STAGE3_PAIRWISE_INTERACTION_SIGNED_CANCELLATION_DRIVER_REVIEW_20260822.md\` blob \`32ab69b8\` | Stage 3 accepts local \`C4\` derived process; \`C4\` signs are process labels, not proof of signed X6 spatial-step integration | Consumer lineage; preserve independent process/source type |
| \`driver_reviews/R063_STAGE4_THREE_SECTOR_C4_PROCESS_GLOBALIZATION_DRIVER_REVIEW_20260822.md\` blob \`3967c336\` | Stage 4 accepts a historical three-sector transport groupoid, not a global N0 multiplication. Its older positive-only three-axis premise (taskbook lines 79–99) is now retyped by the current X6 foundation | LP002/LP028: retain gluing theorem at frozen assumptions; any selected X6 chart application needs an explicit native embedding and observable-preservation bridge |

Current authority: \`definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md\` blob \`e266c103\` and \`definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json\` blob \`94a02d06\` (no independent native plane). The historical three-positive-origin file was retyped as carrier/readout at current blob \`b573b267\`. Stage 4's three old sector charts are **not** the 15 derived unordered X6 axis pairs counted in this note.

**Reviewable minimal R063 textual correction, subject to present Driver/source authority:** retain lines 39–85 and 121–168 numerical/algebraic payload; make §1 inherit the *current retyped* R061/R062 interface; make §6's native path start an actual Cell and treat \`Sigma_O^(ij)\` as historical carrier-incidence provenance; qualify §7's \`native component branch\` as a selected positive two-generator composite-path subfamily; qualify §9's fixed right-sector mass as *one chosen ordered pair*, not any whole signed native shell. Reassess §§10–13 only for labels, not the frozen integer theorem.

## 5. Verification, admission and next precise action

Checker: \`research_checks/X6_LP028_R063_ALL_PAIR_GLUE_20261112_ONHOUR.py\`, published at immutable commit \`011194edfae32e2e7dd03e5cbcaa5f1e12b125c4\`, blob \`41939eff764b26ffd849c482c983aaec9fe9f56d\`, locally executed byte SHA256 \`679c43d879139889e21fddd0d053a1a8c0296a41080e62dc4510cc490ae9d9f8\`. It independently constructs each labelled positive/signed pair-chart union as actual integer tuples; compares endpoint and multinomial mass against all four formulas for \(2\le d\le6\), \(1\le r\le128\), both sign modes (**1280 exact cases; PASS**). It reproduces the original R063 50-root values and uses the earlier full six-axis census only as an explicit immutable numeric anchor. Integer arithmetic only; no tolerance.

**Remaining mother-objective work:** place this verified LP028 glue/caller edge and precise R063 correction target in the eventual 28-row source/location/type/action ledger. Continue tracing original LP011 and LP019 caller provenance and semantically auditing the *remaining* active source consumers. Existing Driver \`REQUEST_REVISION\` applies; old continuation read/progress-artifact support remains \`awdawmip/enterprise-math#2141\` with \`PENDING_OWNER\`. This research note neither updates a frozen definition nor asserts a new native CLAIM/run, Driver admission or full Task completion.
