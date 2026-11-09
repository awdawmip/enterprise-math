# BRC-X6 source-balance spectral 13-minor bound and base-6388 witnesses

2026-11-09. **AUTHOR_PROVED / EXACT_INTEGER_VERIFIED / UNREVIEWED / NOT_ADMITTED.**

Frozen scientific input: `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Original 96 native ports, 576 labelled actions, nine frozen roots, full signed next-port/seven-reward observations. Four source ports (6,7,28,29), signs (+,-,-,+), each with six original actions. The 38 lawful deterministic policies have a 24-by-38 binary source/action incidence matrix, rational rank 13. This report preserves all source labels and is author-side portable evidence, not a D25 native Frobenius/CM experiment or an admitted Source Result.

## Theorem: universal four-source 13-column determinant bound

Let U be any 24-by-13 0/1 matrix whose 24 rows are grouped into four groups of six source-action labels, and whose every column has exactly one 1 in each group. Every 13-by-13 row minor satisfies

**|det(U_R)| <= 6387.**

*Proof.* Put G=U^T U (PSD), tr G=52, and e=(1,...,1)^T in R^13. If rank U<13 all 13-minors vanish. Each of four source groups has occupancy counts n_1,...,n_6 (nonnegative integers, total 13). The minimum of sum n_a^2 is 3^2+5*2^2=29, attained only at (3,2,2,2,2,2); by parity the next possible value is >=31. If at least one source is unbalanced, e^T G e >=3*29+31=118, and the maximal eigenvalue Lambda of G obeys Lambda>=118/13>259/29.

Otherwise all four source groups have one triple-occupied cell and five double-occupied cells. For each column i, let q_i be its number of appearances in a triple-occupied cell. Then q_i is a nonnegative integer, sum_i q_i=4*3=12, and (G e)_i=8+q_i. Consequently e^T G e=116, while
||G e||^2=sum_i(8+q_i)^2 =13*64+16*12+sum_i q_i^2 >=1036
since q_i^2>=q_i for integers. PSD spectral decomposition yields e^T G^2 e <= Lambda e^T G e; hence Lambda>=1036/116=259/29. Thus for every U, Lambda>=259/29.

AM-GM for the other 12 eigenvalues gives det G<=Lambda*((52-Lambda)/12)^12. The right side decreases for Lambda>=4, so

det G <= (259/29)*(1249/348)^12 < 6388^2.

The last strict inequality has an exact rational integer-multiplication certificate; no floating rounding is used. By Cauchy-Binet, det G is the sum of squared integer 13-by-13 row minors of U. Therefore each minor has integer absolute value at most 6387. QED.

This **strengthens the previously published bound 6971**, and unlike that five-pair Fischer result requires neither Hamming distance >=2 nor legality of each deterministic policy: it is a general source-labelled one-hot incidence theorem.

## 9–13 strictly positive optimal decompositions

For k<=12 the 24-coordinate policy columns have Euclidean norm 2, so Hadamard gives |k-minor|<=2^k<=4096. Together with the 13-minor theorem, **all order <=13 minors have absolute value <=6387**.

Reuse (without rediscovery/recrediting) the following exact earlier lawful, linearly independent 13-policy prefix in this order:

```
(0,0,2,2) (1,0,3,2) (2,2,4,4) (3,3,5,5) (4,4,0,0)
(4,4,5,5) (4,5,0,1) (5,1,1,3) (5,5,5,5)
(0,0,0,0) (0,0,1,1) (0,0,4,4) (0,1,2,3)
```

Let c(v_j) denote the 24-component binary source-labelled policy vector, B=6388, D_k=sum_{j=0}^{k-1} B^j and x_k=sum_{j=0}^{k-1} B^j c(v_j) / D_k, for 9<=k<=13. Every prefix is independent and covers all 24 source/action coordinates, so all x_k are strictly positive, lawful and have a displayed k-term convex decomposition. For an arbitrary subspace spanned by <=k-1 legal columns, extend its basis to k-1 independent legal columns. At least one selected prefix column is outside that span, so a nonzero k-by-k determinant functional L on original labelled rows has integral coefficients a_j=L(c(v_j)) with |a_j|<=6387=B-1. For the largest d with a_d !=0,

|a_d| B^d >= B^d > (B-1)*sum_{j<d} B^j = B^d-1,

so L(D_k*x_k)!=0; x_k is outside every <=k-1-policy span. Therefore **minSupport(x_k)=k**.

Exact unreduced denominators and bit lengths:
- k=9: 2773238693467644936246753443781 (102 bits)
- k=10: 17715448773871315852744260998873029 (114 bits)
- k=11: 113166286767489965667330339260800909253 (127 bits)
- k=12: 722906239870725900682906207197996208308165 (140 bits)
- k=13: 4617925060294197053562404851580799778672558021 (152 bits)

Prior B=6972 bit lengths [103,115,128,141,154]; the new base gives [102,114,127,140,152]. These are fully **explicit** exact witnesses, though the separate **existential-only <=35-bit 13-support** challenge still needs an explicit short witness and exclusion certificate.

## Exact verification and authority

Two distinct author-side scripts were run. The native checker reconstructs 38 policies from 1296 candidates and verifies all nine roots, rational incidence rank, 24 positive coordinates, 9–13 exact decompositions and spectral integer inequality. A second standalone checker verifies the rational inequality and original action occupancy directly; the universal theorem is the *symbolic proof*, not an alleged exhaustive search over all hypothetical 13-column matrices. Full program, per-coordinate certificates, proof and clean eight-file ZIP are retained in the current conversation artifact: `BRC_X6_SOURCE_BALANCE_SPECTRAL_BASE6388_AUTHOR_PORTABLE_20261109.zip`. Local certificate SHA-256 `d1a86275dccdb3afc06acd91ff3d276834af9173662653770fb073217daf94a9`. A local ZIP is not itself Source publication.

Reuse original five-pair/6971 author work: `awdawmip/enterprise-math@1fe044cc70f7553020bdd59d52cfb66564df4e0d:research_notes/portable_direct/2026-11-09_prefix577_r6_matching_five_fischer_base6972_author_portable.md`. P000/ACTIVE worldview unchanged; no new claim of proof beyond the precise four-source-one-hot and frozen-kernel setting.

Original UR V2 four-file 94,687-byte SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76` is still not recovered from visible files. Do not recompute completed UR mathematics; original provenance/writer is outstanding. Original D25 original-class H0/B0, [X]U mod p^2, source semilinear Frobenius eta/kappa/Delta-R/CM remain NOT_RUN/UNFINISHED; original D25 continuation historical receipt succeeded but execution_authorized=false. Existing service-issued own researcher `EM-DIRECT-B65969`, session `MCP-8375f0482abf46d191c1bd7bba3bf24e`, RA `RA-C8A528E52B511A73C8BEF944` are registered history without recoverable private session capability, winning CLAIM or native task checkpoint here. No identity switching. All present evidence remains AUTHOR/UNREVIEWED/NOT_ADMITTED pending legitimate writer/provenance and independent Driver review.

**Next unit:** seek a shorter exact explicit <=35-bit 13-minimal instance and certificate, or a tighter source-incidence/eigenvalue bound; preserve prior work and avoid Research1 J1/J2 duplication.
