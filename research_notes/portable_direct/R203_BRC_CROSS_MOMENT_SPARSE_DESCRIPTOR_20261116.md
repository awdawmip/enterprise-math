# R203 — BRC paired-provenance mixed moments without dense observer matrices

Date: 2026-11-16. Status: AUTHOR_PROVED / EXACT_INDEPENDENT_FRACTION_CHECKED / NOT_REVIEWED / NATIVE_PACKAGE_EXECUTION_PENDING.

Scientific input frozen at \`awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34\`. Depends on [R201 affine paired observer](https://github.com/awdawmip/enterprise-math/blob/b2f62925ba31ddb273035c713aab8ebd3c88028f/research_notes/portable_direct/R201_BINARY_AFFINE_BRC_JOINT_OBSERVER_20261116.md), R200 paired event provenance quotient, and the frozen [BRC transport source](https://github.com/awdawmip/enterprise-math/blob/43ec6098b1330ae86d0a7863be336c5d97f6ef34/src/enterprise_math/brc_transport.py) (Git blob \`be1debe367263931bd5e93fd750be3ed54624fe1\`).

## Scope and question

The native X6 universe has six spatial axes and twelve signed native directions. The selected finite observer in R200/R201 has complete event alphabet \`a=84\` (12 directions × 7 independent provenance tags, including bottom), \`k=6\` selected source identities, and suffix depth \`L=2\`. The paired observer has R201's exact affine dimension \`D=k+k(k-1)/2+L ceil(log2(a+1))=35\`. Physical affine dimension is \`n\`.

This study asks whether exact positive-weight BRC second moments and **physical–provenance cross moments** can be transported through R201 while keeping its source action as a short selector/constant descriptor rather than a dense \`D×D\` rational matrix. Only the declared paired finite quotient and fixed-weight total-affine future family are compressed. Full native paths, independent branch identities, phases and signed interactions remain typed upstream when their future observers require them. P000 and the six native axes are unchanged; observer coordinates are auxiliary, not new spatial axes.

## R203-A. Exact row-descriptor closure

An observer affine map \`R(y)=Cy+d\` is a **selector/constant descriptor** when every output coordinate is either one input coordinate \`y_j\` or the literal constant 0 or 1. Record each output row as one of \`SELECT(j), CONST(0), CONST(1)\`.

All R201 event generators are selector/constant descriptors: \`U_i\` and \`V_ij\` either retain a coordinate or reset it to a bit; suffix registers copy the next register or reset to an event code bit. These maps are closed under chronological composition: if a later output selects row j of the earlier transformation, substitute that earlier row; if it is constant, retain its constant. Therefore composition of two D-row descriptors takes **O(D) selector operations**, with no rational arithmetic in the observer block and no matrix materialization.

With \`D\` input indices, one row has at most \`D+2\` alternatives, so a fixed-width full affine-action descriptor needs at most

\`D ceil(log2(D+2))\` bits.

For \`D=35\`: 35×6 = **210 bits per source action**, independent of physical rational coefficient precision. The physical \`n×n\` affine matrix plus \`n\` translations is stored separately. This 210-bit descriptor represents the *complete affine action*, whereas the 21-bit optimal R200 code represents a *reachable observation state*; they support different operation interfaces.

## R203-B. Exact joint second-moment update

For physical dimension \`n\` and source dimension \`D\`, write each weighted branch as \`(q,c,P,R)\`, with \`q∈Q_{>0}\`, \`c∈Z_{>0}\`, \`P(x)=Ax+b\`, \`R(y)=Cy+d\`; C is a selector/constant matrix with 0/1 entries and each row either one unit entry or zero. Let the symmetric *unnormalized* homogeneous joint second moment be

\`\`\`
             [ M_xx   M_xy   mu_x ]
M =          [ M_yx   M_yy   mu_y ]
             [ mu_x^T mu_y^T   s  ]
\`\`\`

where \`s\` is total input mass. For a single branch:

\`\`\`
X  = A mu_x + s b
Y  = C mu_y + s d
XX = A M_xx A^T + (A mu_x)b^T + b(A mu_x)^T + s bb^T
XY = A M_xy C^T + (A mu_x)d^T + b(mu_y^T C^T) + s bd^T
YY = C M_yy C^T + (C mu_y)d^T + d(C mu_y)^T + s dd^T
s' = s
\`\`\`

The output homogeneous moment is assembled from \`XX, XY, YY, X, Y, s'\`. The actual BRC packet operation is **the sum of these branch outputs weighted by \`q c\`**. Thus its total mass is \`s × Σ(qc)\`.

*Proof.* The physical/source block direct sum yields homogeneous map

\`\`\`
             [ A  0  b ]
H =          [ 0  C  d ].
             [ 0  0  1 ]
\`\`\`

Expand the blocks of \`H M H^T\`; each displayed identity follows by ordinary exact distributivity over rational numbers. In \`C M_yy C^T\`, every entry is one input-moment lookup or an appropriate zero; constant rows are handled through \`d\` and homogeneous column. The \`XY\` block selects columns of \`A M_xy\` and includes their source/physical translations. These rules are therefore equal to the existing \`EffectHistogram.moment_action\` algebra, without constructing the dense R201 observer block.

Let \`T_H(M)=Σ_{j in H}(q_j c_j) H_j M H_j^T\`. Positive-weight alternative coalescence satisfies \`T_{H+G}=T_H+T_G\`. For serial convolution, \`(H_j.then(G_l))=G_l H_j\`, so by associativity and distributivity

\`T_{H.then(G)}(M)=T_G(T_H(M))\`

for every rational symmetric input M and all finite positive rational branch weights/multiplicities. This is exact and preserves the mixed \`M_xy\` block. No probability normalization is assumed.

### Arithmetic and storage accounting

For a dense physical A and D-row selector C, compute all \`n\` physical output rows against M, then fill physical–physical, physical–source and source–source blocks by contractions and coordinate lookups. One branch costs **O(n³+n²D+D²) rational arithmetic/lookup operations**, apart from coefficient bit complexity. Direct dense homogeneous multiplication costs O((n+D)³) operations. The full moment still occupies Θ((n+D)²) rational slots: sparsity improves the *action* and transport operation, not the full mixed-moment storage requirement.

A dense lifted affine action has \`(n+D)²+(n+D)\` rational slots versus \`n²+n\` physical-only slots; extra source-related slots are \`2nD + D² + D\`. At \`n=2,D=35\`, this is **1,400 extra rational slots per action**. Replacing the observer block with its full 210-bit descriptor retains the physical rational action and permits exact row-descriptor composition. Rational numerator/denominator growth in physical actions, branch weights, and moments still governs true bit complexity; these are representation-level algebraic operation bounds, not elapsed-time speed measurements.

## R203-C. Exact joint-correlation counterexample

Take initial physical/source state \`(x,y)=(0,0)\`, and two branches with equal positive weight \`1/2\` and count 1. Define their constant affine outputs:

- Pairing A: \`(x,y)=(+1,0),(-1,1)\`.
- Pairing B: \`(x,y)=(+1,1),(-1,0)\`.

Both give the same physical marginal (x=±1 equally), the same source marginal (y=0 or1 equally), and the same separate second moments. But

\`E_A[xy]=-1/2\`, \`E_B[xy]=+1/2\`.

Hence any carrier that keeps only the separate physical and provenance second moments loses a declared joint future observable. The \`M_xy\` block is an exact, necessary repair for this observation class. This is a scoped counterexample to marginal factorization, not a claim about all possible provenance compression.

## Exact reproducibility

Files: \`R203_compact_mixed_moment_check.py\` and \`R203_compact_verification.json\` in the same directory.

The exact Python \`Fraction\` script uses a fixed RNG seed \`20261116\`. It checks 75 row-descriptor concatenations; 54 equality checks of dense \`H M H^T\` against selector-aware moment transport (including 4 checks at X6 \`a=84,k=6,L=2,D=35\`); 24 branch packet serial/second-moment identities; and both rational mixed-moment counterexample values. Every finite check passed in the author reference environment. The general equations above have a direct symbolic proof. Independent mathematics review remains \`NOT_REVIEWED\`.

The script is an **independent exact reference** and not execution of the native installed \`enterprise_math\` package. R201's native package probe is still available separately; the pinned source \`Affine\`, \`EffectHistogram\`, \`moment_action\` and \`then\` method definitions were inspected, but this R203 run does not assert installed-native test success. No real timing, serialization benchmark or hidden provenance preservation beyond the declared observer has been claimed.

## Next useful research

1. Execute R201's existing native probe against the frozen source package and add a native \`EffectHistogram.moment_action\` comparison for nonzero physical–source cross moments; record exact package/environment and outputs.
2. Implement the descriptor as an optional transport without adding a new P000 axis. Compare full input conversion, physical rational bit growth, serial cost, memory and serialization against dense \`Affine\` and the 21-bit reachable-state rank codec. Quantify when retaining all cross moments costs more than retaining joint keys.
3. Find the smallest observer/future-operation scope permitting exact cross-moment compression; test whether restricted readout classes admit a smaller invariant block than the complete \`M_xy\`.

Control provenance: portable independent research; no formal TASK CLAIM/Result/Review asserted, no mutation of protected P000 or active owner records.
