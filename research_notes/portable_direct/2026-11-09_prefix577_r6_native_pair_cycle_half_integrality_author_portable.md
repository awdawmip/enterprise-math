# BRC-X6 native source-pair cycles: exact half-integrality at support ≤12

Date: 2026-11-09. Status: **AUTHOR_PROVED / EXACT_FINITE_ENUMERATION / TWO_CODE_CROSSCHECK / UNREVIEWED / NOT_ADMITTED**. Author-portable evidence only; not a Source task checkpoint, Driver review, or D25 CM/Frobenius result.

## Frozen input and exact claim

Scientific pin `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Preserve the original four source ports `(6,7,28,29)`, 96 native ports, 576 tagged actions and all nine signed joint-observer roots. Reconstruct lawful source-quadruple deterministic policies by checking the full signed next-port/reward joint observer at every frozen root: exactly **38** of `6^4=1296` tuples are lawful. Represent them as the columns of the 24×38 integer one-hot incidence matrix `C`, retaining the four source labels and six labelled actions at each source.

Let `x=b/D` be a genuine native stochastic policy with `D>0`, `b∈Z_{≥0}^{24}`, and each of its four source blocks summing to `D`. For two sources `p,q`, assume all their six marginal numerators are strictly positive and that the sum of any nonempty **proper** subset of the six `p` entries differs from every nonempty proper subset sum of the six `q` entries. Call this pair *subset-indecomposable*.

**Theorem.** If at least one pair is subset-indecomposable, then an exact decomposition of `x` into at most twelve lawful deterministic policies exists **if and only if**

```
there exists n ∈ Z_{≥0}^38 such that C n = 2 b and |{j:n_j>0}| <= 12.
```

In particular, any support-minimal decomposition with at most twelve terms has scaled coefficients `D α_j` in `(1/2)Z_{≥0}`. The result gives an **exact rational-to-integer reduction** for the bounded support problem; it makes no claim of a polynomial-time integer solver.

## Proof

For a nonnegative decomposition build a labelled bipartite multigraph on the six `p`-action and six `q`-action vertices, one edge for each nonzero legal policy. Since all twelve action marginals are positive, every graph vertex has positive incident weight. If the graph is disconnected, any connected component yields equal positive, proper total marginal mass on the two source sides, contradicting the subset-indecomposable condition. Thus the graph is connected, requiring at least eleven edges.

With eleven edges, the graph is a tree. Repeatedly remove leaves; every scaled edge weight is an integer combination of the integer marginal numerators. With twelve edges it is a connected unicyclic multigraph (a two-edge parallel cycle counts). Delete one cycle edge, solve the remaining tree with that edge weight set to zero, and obtain an integer particular solution `w0`. The general solution of the two-source marginal equations is `w=w0+t z`, where `z` has alternating signs `+1,-1` on the unique cycle and zero off the cycle. The other two source blocks impose `c t∈Z^12`, with `c=C_other z`.

When `c=0`, all 24-dimensional incidence columns have a linear dependence, hence a positive twelve-term representation can be reduced to a smaller support (the source-block normalization forces positive and negative dependence coefficients). Otherwise `g=gcd(|c_1|,...,|c_12|)>0`, so Bézout yields `g t∈Z`. The complete frozen native-cycle census below establishes **`g∈{0,1,2}` for all six source pairs**, giving `2w∈Z^12`; the tree case already has `w∈Z^11`. An arbitrary nonminimal representation reduces to one of these cases. Conversely, any nonnegative integral `n` with `C n=2b` and at most 12 positive coordinates gives the desired decomposition with weights `n_j/(2D)`, normalized automatically by any full source block. QED.

## Complete labelled-cycle census

For each of the six unordered source pairs, build the bipartite multigraph of the **38 legal policy IDs**. Enumerate each undirected simple cycle (length 2,4,6,8,10,12), including two-edge parallel cycles with distinct IDs. For each oriented cycle, assign alternating ±1 to its policy edges and compute the exact twelve integer residuals in the other two source blocks and their gcd. The orientation changes only a global sign, not the gcd.

| Pair | All cycles | gcd=0 | gcd=1 | gcd=2 | gcd≥3 |
|---|---:|---:|---:|---:|---:|
| (0,1) | 3,706 | 283 | 3,375 | 48 | 0 |
| (0,2) | 32,782 | 4,901 | 27,122 | 759 | 0 |
| (0,3) | 103,653 | 20,196 | 77,916 | 5,541 | 0 |
| (1,2) | 103,653 | 20,196 | 77,916 | 5,541 | 0 |
| (1,3) | 32,782 | 4,901 | 27,122 | 759 | 0 |
| (2,3) | 3,706 | 283 | 3,375 | 48 | 0 |
| **TOTAL** | **280,282** | **50,760** | **216,826** | **12,696** | **0** |

Two independently written exhaustive implementations agree: (A) native edge-ID DFS with least-node and orientation canonicalization; (B) NetworkX `simple_cycles` on distinct projected edge types, followed by exact Cartesian expansion of all policy IDs and separate parallel-pair handling. Both rederive all six rows without floating-point arithmetic. An exact checker also rechecks the nine signed native roots, the 38 legal policies, integer source marginals and the example below. All returned **PASS** after fresh extraction of the local reproducibility bundle.

## Sharp factor-two example: positive 12-column independent carrier

Select the original 38-policy indices
`[0,10,8,14,13,18,20,27,23,5,33,4]`,
and assign their *twice-scaled* integer weights
`n=[117,149,113,117,13,187,199,131,175,171,122,174]`.
Their exact four-source numerator matrix is

```
b =
  231 131  65 193 153  61
  202 173  65 193 140  61
  207 100 144 131 165  87
  194 100 115 173 165  87
D = 834
```

Every one of 24 native probabilities is positive; each row sums to 834, and `C_ids n=2b` exactly. All nine native roots pass their signed joint-observer constraints. The 12 columns have rational rank **12**. Proper subset sums of source rows 0 and 3 have empty intersection. Odd entries of `n` show that the **unique decomposition on this fixed independent set** genuinely requires half-integer `D α_j`, demonstrating sharpness of factor two for independent fixed supports. This example does not assert that its global minimum support is twelve.

## Scientific use, provenance, and remaining work

Use the theorem as an exact integer-residual criterion to test a proposed all-positive 13-policy witness with at least one subset-indecomposable pair: an exhaustive certificate of integer infeasibility for `C n=2b` with support ≤12, together with an explicit 13-policy decomposition, would prove exact `minSupport=13`. A target is a small public common denominator (≤35 bits). The proof tree and complete preprocessing, numerical/integer precision, search, and verification costs must be preserved; a floating-point MILP status alone is not a proof of infeasibility.

Reproducible locally: `all_pairs_census.py`, `independent_cycles.py`, `verify_half_integrality.py`, `exact_min_support.py`, original frozen native kernel, JSON evidence and manifest, in the author's 2026-11-09 reproducibility bundle. Frozen science pin and original authors remain unchanged. Previous D25 H0/B0 original-class Frobenius/η/κ/CM work and the authentic D24 UR V2 (94,687-byte, SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`) writer/provenance debt remain distinct and pending. Current own private native session/CLAIM authority is unverified; no Source checkpoint, Result, review or P000 change is claimed.

**Author scope:** exact finite graph-algebra theorem and bounded integer criterion, independent author-code crosscheck, preserved native observer; **not Source-admitted or independently Driver-reviewed**.
