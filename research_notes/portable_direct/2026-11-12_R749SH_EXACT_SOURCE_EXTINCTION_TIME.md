# R749SH — Exact all-parameter extinction time of initial signed-source ancestry

Date: 2026-11-12. Independent R749SF/R749SG continuation by researcher EM-DIRECT-13AD93, activity RA-C3E6E78E217BE668B5B93660. Frozen scientific input enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Author-side mathematical theorem, not independently reviewed nor native V29/V39 Cell/Link/Port event licensing.

## Question

R749SG supplies a path-specific Walsh ancestry rank 2^k, where k is the number of the three initial named signs whose descendants survive in the final signed edge. What is the probability and expected observation length until the whole initial signed-source ancestry disappears, when future unsigned supports themselves are sampled under the R749SF homogeneous kernel P_p?

## Theorem 1 — Exact 8-state ancestry-mask reduction, all p∈[0,1]

For an unsigned directed edge (A,B), label its three axes (i,j,k) by i∈A\B, j∈A∩B, k∈B\A. Attach survival bits (x,y,z)∈{0,1}³ to these positions: bit 1 means this *current* token descends from one of the three initial named signs, bit 0 means its provenance was reset by some nonforced observer step. Under every legal next edge (B,C):

- The unique forced unsigned completion C=A△B, with probability a=(1+7p)/8, changes (x,y,z) to (y,z,x).
- Three nonforced completions keep the B-only axis k and introduce a freshly sourced sign, with *total* probability b=3(1-p)/8; they change the mask to (y,z,0).
- Four nonforced completions keep the common axis j and introduce a freshly sourced sign, with total probability c=4(1-p)/8; they change the mask to (z,y,0).

All three weights sum to 1. The mask process therefore closes as an exact autonomous 8-state Markov chain, even though its full signed-Port provenance still requires the richer R749SG lineage labels for source-specific queries. This reduction is for **the ancestry survival observer only**, and does not identify distinct named signed-Port histories.

This follows by enumerating the eight unsigned next supports: exactly four contain j and four contain k, exactly one of the latter is forced. The forced step transports the exposed initial sign with optional BSC flip, preserving ancestry; every nonforced step resets the newly inserted sign even if an axis name reappears.

## Theorem 2 — Universal almost-sure extinction and exact expected loss time

Let T be the number of unsigned-support transitions from the fully ancestral mask (1,1,1) until it first reaches (0,0,0). For every 0≤p<1:

\[
\boxed{\mathbb{E}_p[T]=
\frac{147p^3+427p^2+529p+305}
{7(1-p^2)(7p+9)}.}
\]

At p=0 this is exactly 305/63 ≈ 4.84127 steps; at p=1/2 it is 5557/525 ≈ 10.58476; at p=9/10 it is 1234133/20349 ≈ 60.64834. The exact near-deterministic asymptotic is

\[
\lim_{p\uparrow1}(1-p)\mathbb{E}_p[T]=44/7.
\]

**Almost sure absorption proof.** Any three consecutive nonforced moves in the (y,z,0) branch erase every original ancestor, independent of the initial mask. Each such move has probability b=3(1-p)/8>0. Thus from every mask P(T≤3 | current state)≥b³; independence of fresh transitions and the Markov property gives P(T>3h)≤(1-b³)^h, proving extinction almost surely and finite expectation for p<1.

**Exact expectation proof.** Index the eight masks lexicographically 000,001,010,011,100,101,110,111, and let Q_p be the 7×7 submatrix on the nonzero masks obtained from the three-transition formula. For each nonzero mask u, the expected remaining time e_u solves (I−Q_p)e=1. The following explicit entries solve the complete system (the order is 001,010,011,100,101,110,111):

\[
\begin{aligned}
e_{001}&={24}/{[7(1-p)]},\\
e_{010}&={2(7p^2+5p+12)}/{[7(1-p)(1+p)]},\\
e_{011}&={2(49p^3+154p^2+225p+148)}/{[7(1-p)(1+p)(7p+9)]},\\
e_{100}&={2(7p+5)}/{[7(1-p)]},\\
e_{101}&={2(49p^2+126p+113)}/{[7(1-p)(7p+9)]},\\
e_{110}&={(147p^3+371p^2+401p+233)}/{[7(1-p)(1+p)(7p+9)]},\\
e_{111}&={(147p^3+427p^2+529p+305)}/{[7(1-p)(1+p)(7p+9)]}.
\end{aligned}
\]

Substitution in each of the seven rational linear equations gives identity zero. Almost-sure absorption gives uniqueness of the finite expected-time solution; the stated e_111 is the formula. At p=1, only forced moves occur, (1,1,1) is fixed and T=∞.

## Theorem 3 — Exact finite survival distributions and rank transition frequencies

For a fixed starting unsigned directed edge, all 8^m legal unsigned-support words of m transitions are distinct and equally weighted only at p=0. Enumerating them without probability weighting and classifying the terminal ancestry rank k yields:

| m | k=0 | k=1 | k=2 | k=3 |
|---|---:|---:|---:|---:|
| 1 | 0 | 0 | 7 | 1 |
| 2 | 0 | 49 | 14 | 1 |
| 3 | 147 | 343 | 21 | 1 |

These exact counts are independent of the starting edge by S6 relabeling covariance. For general p the probability generating operator is the 8×8 stochastic matrix with weights (a,b,c) from Theorem 1, not the uniform counting matrix.

At p=0 the 8-state *integer-count* transition matrix has characteristic polynomial

\[
\lambda(\lambda-8)(\lambda-2)(\lambda-1)(\lambda^2-4\lambda-4)(\lambda^2+2\lambda+4).
\]

The nonzero-mask transient operator has spectral radius (2+2√2)/8=(1+√2)/4≈0.6035533906. From its exact scalar generating function, the tail of the survival probability satisfies

\[
\Pr_0(T>m)\sim \left(\frac32+\frac{11\sqrt2}{8}\right)
\left(\frac{1+\sqrt2}{4}\right)^m.
\]

One exact rational ordinary generating function for the *number* of paths retaining at least one initial ancestor at time m (per fixed start) is

\[
\sum_{m\ge0} \left(8^m-\#\{k_m=0\}\right) t^m=
\frac{4t^5-24t^4+41t^3+24t^2+3t+1}
{(1-t)(1-2t)(1+2t+4t^2)(1-4t-4t^2)}.
\]

Here the coefficient at m=0 is 1; asymptotic follows from the simple dominant positive pole at t=(2+2√2)^{-1}. These p=0 spectral statements are additional exact mathematical consequences of the eight-mask reduction, distinct from the all-p expectation result.

## Verification

The standard-library rational checker R749SH_WEIGHTED_ANCESTRY_EXTINCTION_CHECK.py implements the exact mask reduction, tests explicit seven-entry expected-time solutions against Gaussian elimination over Fraction for p=0,1/4,1/2,3/4,9/10,99/100, calculates survival probabilities for 0..8 steps, and independently enumerates the 120-edge unsigned support graph for sample initial edges at lengths m=1,2,3 to verify the matrix classification. Assertions pass exactly; no floating arithmetic is used to validate finite identities.

The seven rational expressions and all-parameter result follow from explicit linear system algebra (symbolically checked by direct simplification); sampled rational checks are evidence, not the universal proof. The physical Event guard V29/V39 remains an independent open mapping question.

## Next

Develop a declared observer-specific tolerance ε stopping criterion, using the exact ancestry survival Markov chain and the p-dependent rank-loss probabilities; compare the exact expected retention cost with BRC provenance ledger size under different user-defined query families. Any practical source discarding must be justified by its specified future observer/horizon.
