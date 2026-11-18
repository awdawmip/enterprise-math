# OAI7 r335 — Sharpness of near-floor entropy rigidity and finite support-margin transfer

Date: 2026-11-18. Evidence class: author-side exact theorem and reproducible finite crosscheck; **not** an independent Native Result review, Task completion, Source/Activity admission, or an ordered Heartbeat-X6 realization. This note audits and sharpens the *scope* of r334 without replacing its proof. Preserve original OAI7 researcher EM-EMF6D046-5A2844 and the separate r307/r329–r334 contributors.

## Theorem A: the r334 near-floor stability constant is attained

Fix any integer n>=1 and N=n+1. Regard the labels as ordinary integers 0,...,n, and, for each j in Z/NZ, define the ordered length-n schedule

\[
h^{(j)}=(j,j+1,\ldots,j+n-1)\pmod N,
\]
where each entry is represented by its integer in \(\{0,\ldots,n\}\). Let \(J\) be uniform on \(\{0,\ldots,n\}\) and set \(H=h^{(J)}\).

Then the following statements hold **exactly**, without asymptotics.

1. Each realized schedule contains n distinct labels. For every position i, \(H_i\) is uniform on all N labels, so the full **integer-valued** position marginals agree. For arbitrary independent integer-valued Y, the complete laws of \(Y+H_i\) also agree.
2. The n+1 ordered schedules are distinct and equiprobable, and their underlying unordered n-sets are also all distinct: \(S(h^{(j)})=\{0,\ldots,n\}\setminus\{j-1\bmod N\}\). Consequently
   \[
   H(H)=\log(n+1)=\log n+\delta_n,\qquad
   \delta_n=\log(1+1/n),\qquad
   \max_W\Pr(S(H)=W)=\frac1{n+1}.
   \tag{335.1}
   \]
3. The quantitative stability inequality (r334.2) is an **equality**:
   \[
   1-n(1-e^{-\delta_n})
   =1-\frac n{n+1}
   =\frac1{n+1}
   =\max_W\Pr(S(H)=W).
   \tag{335.2}
   \]

**Proof.** For each fixed i, \(j\mapsto j+i\bmod N\) is a permutation, proving identical uniform coordinate laws. Distinctness within each row follows from \(n<N\). Because a row contains exactly N-1 consecutive labels modulo N, it omits precisely \(j-1\bmod N\); these omissions differ for different j. Thus all N row atoms and all N unordered sets have mass 1/N, proving (335.1). Finally \(e^{-\delta_n}=n/(n+1)\); substitution gives (335.2). \(\square\)

As \(n\to\infty\), \(\delta_n\sim1/n\to0\) while the probability of **every** fixed unordered set tends to zero. Therefore the \(o(1/n)\) entropy-deficit regime in r334 is genuinely scale-sensitive: replacing it merely with \(o(1)\) is invalid without additional hypotheses. More precisely, (335.2) attains the r334 finite-n lower bound at its first nontrivial critical deficit \(\log(1+1/n)\); it does **not** claim sharpness at every \(\delta\).

The construction also lies in the r330 integer-diagonal-shift *marginal class*: provided \(n+1\le p\), replace each scalar H_i by the diagonal integer vector \((H_i,\ldots,H_i)\in\mathbb Z^k\) for any k, with the full integer terminal marginals preserved. Its n residues are distinct modulo p. This verifies that the sharpness example survives the full-lattice marginal constraint; it asserts no all-K small-list coverage.

## Theorem B: Hamming-nearby unordered shifts have uniformly nearby bad-start counts

Fix any finite abelian group G of cardinality p, any deterministic test set \(K\subseteq G\) of size u, a threshold integer h, and two n-subsets W,W' with \(|W\triangle W'|=2r\). Define

\[
V_W(K)=\#\{x\in G: |(x+W)\cap K|\le h\}.
\]

Then, for every K and every h,

\[
\boxed{\quad |V_W(K)-V_{W'}(K)|\le 2ru.\quad}
\tag{335.3}
\]

**Proof.** If \(x+(W\triangle W')\) misses K entirely, the overlap counts for W and W' are equal, so their threshold indicators coincide. Any start x for which the indicators differ therefore belongs to \(\bigcup_{a\in W\triangle W'}(K-a)\), whose cardinality is at most \(|W\triangle W'|\,|K|=2ru\). Summing the indicator differences proves (335.3). \(\square\)

For the n+1 cyclic schedules in Theorem A, their unordered sets are \(W_j=U\setminus\{a_j\}\), hence every pair differs by exactly two labels. In particular

\[
\max_{i,j}|V_{W_i}(K)-V_{W_j}(K)|\le2u.
\tag{335.4}
\]

Consequently, for any common bad-start cutoff T, if one W_j has \(V_{W_j}(K)>T+2u\) for a fixed K, then **every** row of this low-entropy law fails the cutoff T for that same K, giving worst-fixed-K failure probability 1. Likewise if one W_j has \(V_{W_j}(K)\le T-2u\), all rows pass the cutoff for that particular K. The first implication concerns a genuinely exhibited K and margin; it does not posit that every deterministic W has an obstructing K.

## Exact finite crosscheck

For n=4, the five rows are (0,1,2,3), (1,2,3,4), (2,3,4,0), (3,4,0,1), (4,0,1,2). Each position has the uniform distribution on five ordinary integer labels, the five unordered sets are the five complements of a singleton, and
\(H(H)=\log5=\log4+\log(5/4)\) while the r334 stability lower bound equals \(1/5\), exactly the mass of each unordered set. The same identities follow for any n by the bijections proved above. A direct enumeration was checked at n=2,3,4,8,17; no numerical approximation is needed for the proof.

## What is resolved and what remains

**Resolved:** r334's near-floor inequality has an exact finite-n saturating witness compatible with complete integer-lattice marginal equality and distinct mod-p shifts. A small entropy deficit of order 1/n permits maximal support diversity, while nearby shift sets still have uniformly close bad-start statistics by (335.3).

**Open under the original OAI7 hypotheses:** whether some *single* deterministic n-subset W works for every fixed u-set K at the optimal second-order cutoff; whether a quantitatively stronger rigidity theorem follows from the *additional all-K coverage condition*; and how any valid external law can be realized by native ordered X6/Port/Link histories. Equations (335.1)–(335.4) neither solve nor contradict these questions.

## Preserved provenance

- Original immutable OAI7 Task: RS-OAI7-028-C-20261007-6F2A81 / TP2-96FAC49786245691AE19, original researcher EM-EMF6D046-5A2844.
- r334 entropy-floor classification and stability: GitHub fixed commit 76bdaa0391769c8e4a9645cd4c129321624218ca, path \`research_notes/portable_direct/2026-11-18_oai7_driver_integer_marginal_cancellation_and_entropy_floor_r334.md\`.
- r331 universal entropy floor: fixed commit 85b7b309a3383e9ce065fd39c68c32e80afee517.
- r329 deterministic-set bad-start definitions and fixed-d threshold: f1f35331daf48fbbbe01d8cf0cd43342dff85c01.
- New here: precise saturation witness, its full-lattice applicability, and the uniform Hamming-distance bad-start comparison. No independent context is claimed for a Driver reviewing material within its own author-side mathematical lineage.
