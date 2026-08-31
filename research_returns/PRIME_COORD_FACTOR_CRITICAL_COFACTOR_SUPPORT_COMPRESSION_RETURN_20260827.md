# Prime Coordinate Critical-Cofactor Support Compression — Research Return

Status: `FROZEN / AWAITING DRIVER REVIEW`

Task-ID: `RS-PRIME-COORD-FACTOR-CRITICAL-COFACTOR-SUPPORT-COMPRESSION`  
Publication-ID: `TP2-DBFC9A296E6085FF8B38`  
Researcher-ID: `EM-PCF5-3432B6`  
Claim-ID: `chatgpt-pcf5-20260829-0036-3432b6`

## Primary verdict

`RESTRICTED_SUPPORT_COMPRESSION_PROVED`

The hard target `CRITICAL_COFACTOR_NBLIND_SUPPORT_COMPRESSION_PROVED_OR_NO_GO` is met at restricted-family research-return strength.

For every fixed public integer \(\kappa\ge1\), an explicit \(N\)-blind Perfect-Prime-Table support of cardinality \(O_\kappa(N^{1/3})\) is constructed. It contains the table coordinate of **every** prime divisor of every composite input satisfying
\[
P^+(N)^2\le \kappa N,
\]
where \(P^+(N)\) is the largest prime divisor. The family contains all prime powers \(p^e,\ e\ge2\), all multifactor inputs with \(P^+(N)\le\sqrt{\kappa N}\), and semiprimes \(N=pq,\ p\le q\) with balance ratio \(q/p\le\kappa\).

The same analysis gives an exact single-layer failure boundary: a prime \(p\) is visible in layer \(m\) if and only if
\[
p\le U_m:=m^3+m+1.
\]
Thus strongly unbalanced composites can have a true prime factor outside the support. For the explicit control
\[
N=2018=2\cdot1009,\qquad \kappa=4,
\]
the canonical layer is \(m=5\), \(U_m=131\); the factor \(2\) is visible while \(1009\) is not.

This result uses the frozen Perfect Prime Table entries themselves. It does **not** use, assume, or close the still-open all-\(m\) critical-cofactor determinant lemma. Consequently the compression proved here comes from the exact arithmetic-progression packing of the table plus batch evaluation, not from critical-cofactor nonvanishing.

## 1. Frozen input and N-blindness firewall

Use the frozen table
\[
A_{ij}^{(m)}
=
\prod_{k=0}^{m-1}\bigl(1+i+mj+k m^2\bigr),
\qquad 1\le i,j\le m,\quad m\ge2.
\]

The constructor is allowed to use only \(N\), fixed public constants, and independent public parameters. Hidden prime divisors may appear only in the proof of coverage. In particular, no factor-derived phase, row, column, minor, residue class, or postselected coordinate is used to define the support.

## 2. Exact interval-partition theorem

Define the cell
\[
C_{ij}^{(m)}
=
\{1+i+mj+k m^2:0\le k<m\}.
\]
Then
\[
A_{ij}^{(m)}=\prod_{x\in C_{ij}^{(m)}}x.
\]

Let
\[
L_m=m+2,\qquad U_m=m^3+m+1,\qquad
I_m=[L_m,U_m]\cap\mathbb Z.
\]

### Theorem 2.1 — mixed-radix partition

For every \(m\ge2\),
\[
I_m=\bigsqcup_{1\le i,j\le m} C_{ij}^{(m)}.
\]
Hence the \(m^2\) cells partition exactly \(m^3\) consecutive integers and every cell has cardinality \(m\).

**Proof.**
For \(x\in I_m\), put
\[
z=x-(m+2)\in\{0,\ldots,m^3-1\}.
\]
There is a unique mixed-radix expansion
\[
z=(i-1)+m(j-1)+m^2 k,
\]
with \(1\le i,j\le m\) and \(0\le k<m\). Rearranging gives
\[
x=1+i+mj+k m^2.
\]
Uniqueness of the base-\(m\) digits gives disjointness. Conversely every declared cell element lies between \(L_m\) and \(U_m\). ∎

The support fibers therefore have an **exact**, not visual, multiplicity \(m\). No hidden enumeration of the \(m^3\) interval points is needed below.

## 3. Exact prime-visibility theorem

For a prime \(p\), say that \(p\) is **layer-\(m\) visible** if \(p\mid A_{ij}^{(m)}\) for at least one cell.

### Theorem 3.1 — visibility iff \(p\le U_m\)

For every \(m\ge2\) and every prime \(p\),
\[
p\text{ is layer-}m\text{ visible}
\quad\Longleftrightarrow\quad
p\le U_m.
\]

**Proof.**

If \(p>U_m\), every factor occurring in every \(A_{ij}^{(m)}\) is a positive integer \(<p\), so no cell product is divisible by \(p\).

Assume \(p\le U_m\). If \(p\ge L_m\), then \(p\in I_m\), hence the partition theorem places \(p\) in a unique cell.

If \(p<L_m=m+2\), let
\[
r=p\left\lceil\frac{L_m}{p}\right\rceil.
\]
Then \(r\ge L_m\), \(p\mid r\), and
\[
r<L_m+p\le 2m+3\le m^3+m+1=U_m
\]
for \(m\ge2\). Thus \(r\in I_m\), so the unique cell containing \(r\) has product divisible by \(p\). ∎

For proof-side bookkeeping only, define
\[
r_m(p)=p\left\lceil\frac{L_m}{p}\right\rceil
\]
when \(r_m(p)\le U_m\), and recover the unique \((i,j,k)\) from
\[
r_m(p)-(m+2)=(i-1)+m(j-1)+m^2k.
\]
The coordinate \((i,j)\) proves membership after the prime is named; it is **not** supplied to the algorithm.

## 4. N-native support and divisor coverage

Fix once and for all a public integer \(\kappa\ge1\). For composite \(N\ge4\), define
\[
m_\kappa(N)
=
\max\!\left(
2,\,
\min\{m\in\mathbb Z_{\ge1}:m^6\ge\kappa N\}
\right)
=
\max(2,\lceil(\kappa N)^{1/6}\rceil).
\]

Define the support
\[
\mathcal F_N^{(\kappa)}
=
\{(i,j):1\le i,j\le m_\kappa(N)\}.
\]
This set depends only on \(N\) and the precommitted public parameter \(\kappa\).

Since \(m^6\ge\kappa N\),
\[
U_m\ge m^3\ge\sqrt{\kappa N}.
\]

### Theorem 4.1 — restricted all-divisor coverage

If
\[
P^+(N)^2\le\kappa N,
\]
then for every prime divisor \(p\mid N\),
\[
\operatorname{coord}_{m_\kappa(N)}(p)\in\mathcal F_N^{(\kappa)}.
\]

**Proof.**
Every prime divisor \(p\le P^+(N)\le\sqrt{\kappa N}\le U_m\). The visibility theorem supplies a cell coordinate for each such \(p\), and the full support contains every layer-\(m\) cell. ∎

### Explicit covered families

1. **Balanced semiprimes.** If \(N=pq\), \(p\le q\), then
   \[
   q^2\le\kappa pq
   \Longleftrightarrow
   q/p\le\kappa.
   \]
   Thus every fixed balance-ratio family \(q/p\le\kappa\) is covered.

2. **Prime powers.** For \(N=p^e,\ e\ge2\),
   \[
   p^2\le N\le\kappa N,
   \]
   so every prime power is covered for every \(\kappa\ge1\).

3. **Multifactor inputs.** Every composite satisfying
   \[
   P^+(N)\le\sqrt{\kappa N}
   \]
   is covered without any restriction on the number or multiplicities of its prime factors.

Prime inputs are not claimed to satisfy an all-prime-divisor support theorem at this layer; primality testing is a distinct preprocessing question and is outside this task.

## 5. Support cardinality

Let \(n=\lceil\log_2 N\rceil\). Since
\[
m_\kappa(N)<(\kappa N)^{1/6}+1,
\]
we have
\[
|\mathcal F_N^{(\kappa)}|
=m^2
<
\kappa^{1/3}N^{1/3}
+2\kappa^{1/6}N^{1/6}
+1.
\]

For fixed \(\kappa\),
\[
|\mathcal F_N^{(\kappa)}|
=O_\kappa(N^{1/3})
=O_\kappa(2^{n/3}).
\]
This is strictly below the ordinary square-root candidate scale
\[
N^{1/2}=2^{n/2},
\]
with exponent gain \(\varepsilon=1/6\).

## 6. N-blind construction without expanding the m-point fibers

Put \(M=m^2\) and define over \(\mathbb Z/N\mathbb Z\)
\[
P_m(X)=\prod_{k=0}^{m-1}(X+1+kM).
\]
Then exactly
\[
A_{ij}^{(m)}\bmod N=P_m(i+mj)\bmod N.
\]

The points
\[
i+mj,\qquad 1\le i,j\le m,
\]
are pairwise distinct and form the consecutive set
\[
\{m+1,m+2,\ldots,m^2+m\}.
\]

Therefore all \(m^2\) cell residues can be constructed from \(N,m\) by:

1. building the degree-\(m\) polynomial \(P_m\) with a product tree;
2. evaluating it at the \(m^2\) public points by a monic subproduct/remainder tree;
3. computing \(\gcd(P_m(i+mj),N)\) for the resulting cell residues.

All divisors in the remainder tree are monic, so polynomial remainder reduction requires no inversion of a possibly nonunit coefficient in \(\mathbb Z/N\mathbb Z\).

Let \(\mathsf M(n)\) be the bit complexity of multiplying \(n\)-bit integers. Standard product-tree / multipoint-evaluation arithmetic gives
\[
\widetilde O(m^2)
\]
ring operations and
\[
\widetilde O(m^2\mathsf M(n))
=
\widetilde O_\kappa(2^{n/3}\mathsf M(n))
\]
bit operations for the batch, followed by \(m^2\) \(n\)-bit gcd computations of the same support order. With quasi-linear integer multiplication this is
\[
\widetilde O_\kappa(2^{n/3}n).
\]

Thus the construction charges the \(m^2\) actual cells, not the \(m^3\) integers inside their fibers.

## 7. Integerization / gcd interface

For each \((i,j)\in\mathcal F_N^{(\kappa)}\), compute
\[
g_{ij}=\gcd(A_{ij}^{(m)}\bmod N,N).
\]

- If \(1<g_{ij}<N\), output \(g_{ij}\) as a proper factor.
- If \(g_{ij}=N\), refine **only that cell** by a binary product/gcd descent over its \(m\) public linear factors. Whenever \(U_m<N\), no individual leaf factor can itself be divisible by \(N\), so any cell whose product has gcd \(N\) must contain at least one leaf with a proper nontrivial gcd. A verifier may scan those \(m\) leaves directly; a production implementation may use the product tree.

On the covered family, at least one cell has nontrivial gcd with \(N\) because every prime divisor is visible. The extra within-cell refinement is \(O(m)\) leaf work in the direct version and remains lower order than the \(m^2\) cell support.

This is a candidate-testing interface for the benchmark/gcd lanes. It is not promoted here to a claim of end-to-end state-of-the-art factorization, and recursive factor splitting is outside the task.

## 8. Duplicate coordinates, gauge and support-cost accounting

The possible compression accounting is exact:

- the \(m^2\) table cells are distinct;
- \(q=i+mj\) is a bijection from \([m]^2\) to \(\{m+1,\ldots,m^2+m\}\);
- the interval map has exactly \(m\) integers per cell;
- different prime divisors may land in the same cell, but this does not lose divisibility because the cell product preserves all such prime factors;
- a cell gcd equal to \(N\) is not silently discarded: the one-cell refinement cost is charged explicitly;
- no phase, gauge, symmetry representative, hidden row, or factor-labelled orbit is used to reduce the support;
- the declared support remains the full \(m^2\) cell set. Any further symmetry reduction would require an additional \(N\)-derived selector theorem not proved here.

## 9. Exact failure boundary and unbalanced counterexample

The visibility theorem is also a sharp obstruction:
\[
p>U_m\Longrightarrow
p\nmid A_{ij}^{(m)}
\quad\text{for every }i,j.
\]

For
\[
N=2018=2\cdot1009,\qquad \kappa=4,
\]
the \(N\)-native rule gives
\[
m=5,\qquad I_m=[7,131].
\]
The small factor \(2\) is represented by \(8\in C_{2,1}^{(5)}\), while
\[
1009>131=U_5
\]
so \(1009\) divides no cell product. Hence the fixed-\(\kappa\) theorem cannot be extended to arbitrary imbalance.

More generally, if one insists that **one full layer** visibly contain every prime divisor for arbitrary composites, the family \(N=2q\) with large prime \(q\) forces
\[
U_m\ge q\asymp N,
\]
hence \(m=\Omega(N^{1/3})\) and the full layer has
\[
m^2=\Omega(N^{2/3})
\]
cells. Therefore universal all-prime single-layer visibility is not itself a sub-square-root support strategy. This lower bound is scoped to this full-layer Perfect-Prime-Table visibility interface; it is not a lower bound on factorization algorithms in general.

## 10. Independent exact regression

Checker:
`./scripts/check_prime_coord_factor_critical_cofactor_support_compression.py`

Authoring-time run:

`PCF5_SUPPORT_CHECK_PASS partition_cases=8 visibility_cases=354 polynomial_cases=450 sufficient_family_cases=5224 visible_family_extract_cases=6600 counterexample=N2018_kappa4_q1009_outside_U131`

The regression independently checks:

- exact partition identity for \(m=2,\ldots,9\);
- visibility iff \(p\le U_m\) for 354 prime/layer instances;
- polynomial/cell-product equality for 450 composite-modulus cell instances;
- all 5224 covered theorem instances with \(N\le5000\), \(\kappa\in\{1,2,4\}\);
- 6600 covered composite-layer instances where the direct gcd verifier produces a proper divisor;
- the exact \(2018=2\cdot1009\) unbalanced failure.

These finite checks are regression/certificate evidence only. The interval partition, visibility equivalence, restricted-family support theorem and asymptotic support bound are proved above for all stated inputs.

## 11. Dependency and scope disposition

The PCF1 information-leakage audit is respected: the support constructor uses only \(N\) and precommitted \(\kappa\). Prime labels appear only after construction in the proof.

The parent critical-cofactor all-\(m\) return remains unresolved at its Beta–Bernstein/Mobius quotient lemma. The present result does not rely on that lemma. It therefore does not promote the parent theorem or claim that critical-cofactor nonsingularity creates the selector.

The exact positive conclusion is narrower and cleaner:

> the frozen Perfect Prime Table **cell products** admit a genuinely \(N\)-blind, strictly sub-square-root full-cell support on an explicit infinite balance/smoothness family, with an exact visibility boundary outside that family.

## 12. Downstream transition recommendation

Freeze this task as `RESTRICTED_SUPPORT_COMPRESSION_PROVED` and send to Driver review.

If accepted:

1. expose \(\mathcal F_N^{(\kappa)}\), \(P_m\) batch evaluation and the cell-gcd interface to the benchmark suite;
2. compare its \(N^{1/3}\) fixed-\(\kappa\) family behavior against the program's admissible baselines;
3. treat the exact boundary \(p>U_m\) as a regression guard against overselling the route as universal;
4. pursue a separate successor only if there is a genuinely \(N\)-native selector that chooses fewer than all \(m^2\) cells or adapts \(\kappa\) without factor leakage.

No further research is required inside the declared PCF5 task scope before Driver review.
