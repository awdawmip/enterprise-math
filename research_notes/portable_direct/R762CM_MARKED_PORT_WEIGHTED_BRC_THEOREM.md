# R762CM — A single marked native-axis source splits the K4 triad BRC quotient (exact weighted theorem)

Status: AUTHOR_PROVED_AND_AUTHOR_EXACT_CHECKED / INDEPENDENT_REVIEW=NOT_REVIEWED.
Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS, publication TP2-8B7E13C5904A2D6F1142.
Author continuation: EM-X6-3050F6, prior R762CL, Draft PR #2590@9f3db47b222d4a63d513e537547d6da51dcc960c.
Frozen scientific task input: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Global P000 V4 and Source P000 V5 retain the native six-axis/triadic axioms.
Research type: conditional six-token triadic incidence candidate; no licensed TRIADIC_CLOSURE_E Cell/Port/Link transition is asserted.

## Question and typed carrier

R762CL proved that six distinct equal-positive-quanta tokens on six X6 native axes, labeled by the six unoriented K4 edges, have ten unordered 3+3 triadic assemblies. Uniform candidate exchange of one token between the triples gives K10 and a sufficient SF/PP two-class positive N-BRC quotient.

Here keep the same 10 source assemblies and the same candidate exchange graph. Select a single distinguished *native-axis token* e*=01. For an exchange swapping tokens a,b from opposite triples, assign an integer multiplicity lambda if e* belongs to {a,b}, and multiplicity 1 otherwise, where lambda is any nonnegative integer. If lambda=0 the marked exchanges are omitted; otherwise lambda counts distinguishable positive microbranches. No negative/signed cancellation is involved. Token names, endpoints, six-axis embedding and branch-source identities remain intact. An observer reads only the current SF versus PP assembly type and, after arbitrary subsequent weighted exchanges, positive aggregate counts of those two readouts. It does not query the exchanged token, the microbranch tag, or the named triad contents.

In a PP assembly the triple containing e* is a 3-edge K4 path. Classify PP into M (e* is the **middle edge** of that path) and O (e* is an **outer edge**). Let F denote the star/face (SF) class. The numbers of named assemblies are |F|=4, |M|=2 and |O|=4. This is a partition of ten, not a reduction of native spatial dimension.

## Theorem — exact marked-token strong lumpability and minimal repair

For every integer lambda>=0, the exact source-count transfer on the ordered classes (F,M,O), with row convention, is

\[
T_\lambda=\begin{pmatrix}
\lambda+2&2&2\lambda+2\\
4&\lambda&2\lambda+2\\
2\lambda+2&\lambda+1&3
\end{pmatrix}.
\]

Each named state has exactly 3 lambda+6 positive outgoing source microbranches; the quotient is strongly lumpable for the declared SF/PP future-readout language. Its stationary class proportions after normalization by 3 lambda+6 are exactly

\[
\pi=(2/5,\,1/5,\,2/5).
\]

The three exact eigenvalues, including algebraic multiplicity, are

\[
3\lambda+6,\qquad \lambda-2,\qquad 1-2\lambda.
\]

The **minimal** future-predictive exact quotient preserving the SF/PP readout has two states for lambda=1 (R762CL's homogeneous setting) and exactly three states for lambda!=1. Hence the least additional fixed-length BRC repair from the *known* SF/PP readout is zero bits for lambda=1 and **one bit** for lambda!=1. Full named-triad membership remains a distinct observer requiring ten states (4 fixed-length bits).

### Proof 1: weighted transitions and 3-class closure

There are ten 3+3 partitions because C(6,3)/2=10. R762CL shows all nine other states arise from a unique token exchange. Fix e*=01. The subgroup of K4 vertex relabelings preserving the unordered edge 01 has order four; it preserves the marked-exchange multiplicity. Its four orbits on the ten assemblies have sizes 2,2,2,4. The first two orbits are F, the third M, and the fourth O. Their exact total positive outgoing weights, grouped by these four orbit targets, are:

| source subgroup orbit (size) | F1 (2) | F2 (2) | M (2) | O (4) |
|---|---:|---:|---:|---:|
| F1 (2) | lambda | 2 | lambda | 2 lambda+2 |
| F2 (2) | 2 | lambda | lambda | 2 lambda+2 |
| M (2) | 2 | 2 | lambda | 2 lambda+2 |
| O (4) | lambda+1 | lambda+1 | lambda+1 | 3 |

The 4-by-4 table is an explicit finite incidence certificate: enumerate the nine exchanges from one representative of each subgroup orbit, identify whether the swapped pair contains 01, and use the subgroup's transitivity on the orbit. In particular the F1 and F2 rows become identical after merging their target columns and have the same totals as asserted for F. Summing the first two columns yields the displayed 3-by-3 T_lambda. Equivalently the unweighted class totals plus counts of marked exchanges are:

| source | ordinary K10 counts to F,M,O | exchanges involving 01 to F,M,O |
|---|---|---|
| F | (3,2,4) | (1,0,2) |
| M | (4,1,4) | (0,1,2) |
| O | (4,2,3) | (2,1,0) |

Each row contains exactly three marked exchange choices and six unmarked ones. Weighting gives the stated T_lambda. Because this same total holds for every named state inside each of F,M,O, all powers T_lambda^t give the exact future aggregate microbranch counts. This proves strong lumpability for that observer.

### Proof 2: stationary mass and spectrum

The full 10-by-10 weighted adjacency is symmetric: the unique swap from s to t is reversed by the same pair, with the same marked-token multiplicity. Its row sum is d=3 lambda+6, so the uniform distribution on ten named states is stationary for the normalized walk. Pushforward onto F,M,O gives (4,2,4)/10=(2/5,1/5,2/5). Direct computation of trace, principal minors and determinant yields

\[
\det(xI-T_\lambda)
=(x-(3\lambda+6))(x-(\lambda-2))(x-(1-2\lambda)).
\]

These equations hold also for lambda=0, where some edge multiplicities vanish.

### Proof 3: exact minimality

The current SF/PP observation distinguishes F from both M and O. If M and O were merged, then starting at an M assembly the one-step positive mass of future SF states would be 4; starting at O it would be 2 lambda+2. These values differ precisely when lambda!=1. Thus M and O must remain distinct, proving at least three future-equivalence classes for lambda!=1. The 3-state transfer establishes sufficiency.

For lambda=1 the marked status no longer affects exchange weight. The old SF/PP quotient from R762CL has matrix [[3,6],[4,5]], so exactly two current-observer classes suffice. One extra bit after the SF/PP readout distinguishes the two PP subclasses for lambda!=1; none is needed for lambda=1. Named triad-membership queries distinguish all ten assemblies as proved in R762CL.

## Corollary: the marked double-source case lambda=2

For lambda=2,

\[
T_2=\begin{pmatrix}4&2&6\\4&2&6\\6&3&3\end{pmatrix},
\quad d=12,\quad \mathrm{spec}(T_2)=\{12,0,-3\}.
\]

After one candidate exchange, F and M have identical class-level future distributions despite different *current* SF/PP readouts; the zero eigenmode is erased in one step. Starting from one named assembly in F or M, the exact (F,M,O) positive source counts for t>=1 are

\[
n_t=\frac{12^t}{5}(2,1,2)
     +\frac{(-3)^{t-1}}{5}(-4,-2,6).
\]

For an O starting assembly replace the correction vector by (6,3,-9). These are integer vectors with total 12^t. The normalized nonstationary eigenvalue is -1/4, versus -1/9 in the homogeneous R762CL two-class candidate. Thus a single marked Port-source multiplicity can change both the minimal observer-safe BRC state and its decay rate without altering the ten assemblies or the candidate adjacency K10.

## Verification, limits and next event test

The accompanying standard-library Python verifier enumerates the ten states, nine unique swaps each, marked-swap reversal symmetry, the four-element marked-edge stabilizer, exact class counts, every row of T_lambda for lambda in {0,1,2,3,4,5,7,11}, full positive microbranch walks for all ten starts and depths 0..9, stationary weighted counts, characteristic-polynomial coefficients, and the lambda=2 closed form for t=1..10. Integer arithmetic only; the loop reports 942 assertion groups. The finite certificate checks this explicit ten-state family; the parameter theorem follows from the incidence proof and polynomial identities. Independent mathematical review remains NOT_REVIEWED.

The marked lambda is a *source-multiplicity candidate*, not an observed physical interaction parameter or an authenticated TRIADIC_CLOSURE_E permission. The genuine native Cell/Link/Port event predicate and its V17/V29/V39 transport remain to be read and applied. Once it is available, restrict the ten-state candidate graph to genuinely licensed transitions, retain any separate signed path-area and provenance information required by R762CH/CK, and recalculate the minimal source-safe BRC quotient under the actual named Port observation language. One licensed rejection or named observation distinguishing a proposed quotient will give a precise refinement.