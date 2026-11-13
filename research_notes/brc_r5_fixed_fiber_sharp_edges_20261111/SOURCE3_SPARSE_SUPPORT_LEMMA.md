# R5 supplemental exact lemma — dynamic source 3 requires at least four target branches

**Frozen auxiliary model:** the same rational physical witness and seven likelihood-ratio numerators from the accompanying fixed-fiber research. This is a mathematically exact, observer-scoped author result; formal Source review/admission remains pending.

## Statement

For **every** nonnegative transfer $E$ in the single fixed fiber $\mathcal F=\{E\ge0:CE=CE^0\}$, at least **four distinct positive dynamic arcs** must originate at source port $j=3$.

Consequently, a sharp $K_4+$doubled-high-pair 14-arc edge circuit (whose four dynamic source degrees are $(3,3,4,4)$) **cannot** place source 3 among its two degree-three ports. This gives an exact structural reason that the three low-pair choices containing source 3 yield zero physically realizable sharp edges in the main 49-edge census.

## Proof: an exact three-target capacity/moment inequality

Let $M_i$ denote the available dynamic target marginal mass at target index $i$ computed from the frozen witness, and let $R_i$ be its unscaled ratio numerator. Exactly,

| $i$ | $R_i$ | $M_i$ |
|---|---:|---:|
| 0 | 2 | $10022571/135903376$ |
| 1 | 10 | $1898238/8493961$ |
| 2 | 15 | $1460251/8493961$ |
| 3 | 20 | $377644447/2548188300$ |
| 4 | 25 | $1544855/16987922$ |
| 5 | 30 | $2161731/33975844$ |
| 6 | 38 | $10022571/135903376$ |

The frozen source-3 marginal and first moment are
\[
Q_3=\frac{1076926147}{2548188300},\qquad
T_3=\frac{1076926147}{127409415}=20Q_3.
\]
If source 3 used at most three targets, enlarge its target support to some triple $J\subset\{0,\ldots,6\}$. Necessarily there would be nonnegative allocations $x_i\le M_i$ for $i\in J$, with
\[
\sum_{i\in J}x_i=Q_3,\qquad
\sum_{i\in J}R_i x_i=T_3.
\]
There are exactly $\binom73=35$ possible triples. For **26** triples, $\sum_{i\in J}M_i<Q_3$, so even their entire capacity cannot supply the observed source mass. For the remaining **nine**, the maximum achievable weighted moment at fixed mass $Q_3$ is obtained by filling target capacities in strictly decreasing ratio order (a standard exchange argument). This maximum can be computed exactly for each of those nine triples.

Across all nine, the **largest** possible moment is attained at triple $J=\{1,3,6\}$ and equals
\[
\max_{|J|=3}\ \max_{\substack{0\le x_i\le M_i\\\sum_{i\in J}x_i=Q_3}}
\sum_{i\in J}R_i x_i
=\frac{3961511143}{509637660}.
\]
The required moment exceeds this **global three-target maximum** by the strictly positive rational gap
\[
\boxed{
T_3-\frac{3961511143}{509637660}
=\frac{23079563}{33975844}>0.
}
\]
Therefore no transfer in the fixed fiber can have three or fewer positive target branches at source 3. In a sharp circuit with two source degrees 3 and two source degrees 4, source 3 must be one of the degree-4 source ports. QED.

## Exact calculation evidence

The complete finite-domain certificate is independently implemented by VERIFY_SOURCE3_SPARSE_SUPPORT.py using only Python 3 standard-library Fraction and combinations, no solvers or numerical tolerances. The expanded local script R5_SOURCE3_SPARSE_SUPPORT_LEMMA.py was actually run; its terminal marker is

    PASS_EXACT_SOURCE3_SPARSE_SUPPORT_OBSTRUCTION

The repository copy uses the same rational inputs and complete 35-triple algorithm and was persisted separately; actual byte-for-byte independent execution of that copy and independent review remain pending. Its observed local output is included in EXACT_SOURCE3_OUTPUT.txt.

The lemma is **stronger than** the zero counts in the sharp-edge table: it constrains *every* transfer in this one fixed physical observer fiber, regardless of vertex or edge status. It does **not** assert a four-branch bound for other physical parameters or observer right-hand sides.

**Next:** seek an analytic non-enumerative upper bound giving the same strict moment deficit and study which of the nine sharp-edge tree components are linked by other residual types.
