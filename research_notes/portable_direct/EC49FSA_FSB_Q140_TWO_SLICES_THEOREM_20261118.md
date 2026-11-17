# EC49FSA–FSB — Two exact q140 discount phase diagrams

**Scientific evidence:** AUTHOR_PROVED / EXACT_FINITE_BELLMAN_CROSSCHECKED / NOT_REVIEWED. **Observed:** 2026-11-18 (Asia/Shanghai). **Frozen pin:** \`fc0f038e7bfd12c886b4d37f900bfb770c0f61ab\`. **Continuation:** EC49FRZ2; immutable scientific foundation is the same as https://github.com/awdawmip/enterprise-math/pull/2669 .

## Scope and native data

The finite native BRC class 16943 consists of 141 distinct complete named-state profiles, 310 raw configurations, and **all 228 physically named original observations** with their full response fibers. The prior here is uniform over the 141 profiles, not over the 310 configurations. Its raw master SHA256 is \`cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e\`, the profile CSV SHA256 is \`a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f\`. No native joint observer is discarded or replaced with a collapsed port. This is an observer-cost experiment under P000, not an additional physical X6 dynamics axiom.

An admissible finite adaptive complete deterministic decision tree must distinguish all 141 profiles, using the original response partition for every selected physical observation. Let \(F=141V/t\) denote the **sum** of observation costs over all 141 profiles divided by a fixed reference cost \(t>0\); all unspecified queries cost \(t\). Repeated nonsplitting queries may be removed without raising cost, including at zero-price endpoints. Both new statements quantify over **every** admissible complete native decision tree.

## Theorem A: only q140 is discounted

For \(p_{140}=(1-z)t\) and \(0\le z\le1\), the exact global optimum is

\[
F_A(z)=\begin{cases}
296-27z,&0\le z\le1/57,\\
298-141z,&1/57\le z\le1.
\end{cases}
\]

The optimal witness affine types \((U,N_{140})\) are precisely \((296,27)\) and \((298,141)\), with physical roots q34 and q140 respectively. Exact full-Bellman anchor values are \(F_A(0)=296\), \(F_A(1/57)=5615/19\), and \(F_A(1)=157\). The first type is baseline-optimal even at \(z=0\), and a positive discount immediately yields slope \(-27\); at \(z=1/57\), the q140-root saturated type takes over. Exactly two fixed affine tree-cost types are necessary and sufficient.

## Theorem B: q32 is free and q140 is discounted

For \(p_{32}=0\), \(p_{140}=(1-z)t\), \(0\le z\le1\), and \(p_q=t\) for all other physical observations (including q34),

\[
F_B(z)=
\begin{cases}
155,&0\le z\le1/6,\\
156-6z,&1/6\le z\le1/3,\\
158-12z,&1/3\le z\le1/2,\\
161-18z,&1/2\le z\le2/3,\\
173-36z,&2/3\le z\le4/5,\\
185-51z,&4/5\le z\le13/15,\\
198-66z,&13/15\le z\le1.
\end{cases}
\]

The corresponding q32-root witness tree types \((A=U-N_{32},K=N_{140})\) are \((155,0),(156,6),(158,12),(161,18),(173,36),(185,51),(198,66)\). Every one of these seven witnesses has \(N_{32}=141\), retains the full original response fibers, and distinguishes all 141 states. The complete exact Bellman anchor table is:

| z | 0 | 1/6 | 1/3 | 1/2 | 2/3 | 4/5 | 13/15 | 1 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| F_B | 155 | 155 | 154 | 152 | 149 | 721/5 | 704/5 | 132 |

Thus the q140 discount has an **exact no-response region** \(0\le z\le1/6\) when q32 is free; the right derivative is 0 until this threshold, unlike Theorem A. There are seven full-dimensional strict affine phases and the minimal universal fixed-tree menu has seven cost types.

## Proof: exact Bellman anchors + concavity + complete witnesses

Every fixed complete native tree \(Q\) has affine normalized cost \(A(Q)-zK(Q)\), where \(K=N_{140}\) and either \(A=U\) (A) or \(A=U-N_{32}\) (B). Therefore the unrestricted optimum over all admissible trees, \(\inf_Q(A-zK)\), is concave in the real variable \(z\).

For any subset of named states \(S\), compute the exact native integer Bellman recurrence
\[
D(S)=\min_{\substack{q\in\{0,\ldots,227\}\\q\text{ splits }S}}\bigl(|S|p_q+\sum_{\substack{B\text{ child fiber of }q\\|B|>1}}D(B)\bigr),\qquad D(\{s\})=0.
\]
Every child has strictly fewer states; hence the exhaustive finite recursion covers all admissible complete adaptive trees. The stated endpoints have been evaluated by this recursion from all 228 physical named observations with rational costs; the resulting trees have been replayed path-by-path on all 141 states. A second implementation independently constructs the observation arrays from the original 94-family master and CSV and reproduces all 18 recorded anchor/diagnostic Bellman outputs.

For any adjacent anchors \(u<v\) in either theorem, a complete native witness has affine cost \(L(z)\) equal to the Bellman optimum at **both endpoints**. Concavity supplies \(F(z)\ge(1-\theta)F(u)+\theta F(v)=L(z)\) at \(z=(1-\theta)u+\theta v\); this witness supplies \(F(z)\le L(z)\). Thus \(F=L\) across each **entire real interval**. Each stated segment has a distinct slope on a nonempty open interval, forcing at least one different fixed-tree affine type per segment. The explicit trees show these numbers suffice.

## Reproducibility and actual limitations

Two native raw-data reconstruction paths agree on all 228 physical-observation response vectors. The 18 rational Bellman computations, including redundant interior validation points, match between separate recursive solvers. All generated witnesses distinguish 141/141 states; they contain no same-path repeated observation, and their exact use counts reconstruct the Bellman costs. The inherited EC49FRZ2 archive's 38 listed files pass size and SHA256 checks. The 2026-11-18 full portable local evidence bundle adds every oracle witness, source, logs, and manifest. Its SHA256 is \`181a91f4ba2912e6abe1ad2ce3104c603a0407e0b65d10c72fcf2281ead1023a\`.

The mathematical result is author-proved with exact finite checks, **not independently reviewed**. A native Source lookup on 2026-11-17 19:33:04 UTC found \`RS-EC49AS\` = \`NO_CANONICAL_PUBLICATION_DIRECTORY\` at Source \`37170cd77ff951c64c28cc1f4b46a5989441343b\`; this portable manuscript does not assert formal CLAIM, Result or Review. Publication of this manuscript and code does not alter those statuses.

**Next unresolved research unit:** full three-price BRC surface with independent discounts to q32, q34 and q140; a discriminating cross-section fixes \(a=b=1/2\), varies \(z\), and tests whether any full native tree combines the former two-observer saturation with q140 use deeper in a path. Retain all 228 named observers and the frozen science pin.
