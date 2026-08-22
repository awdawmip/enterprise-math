# R065 Phase A — Composition Law Classification

Researcher-ID: `EM-R065A-7E6F46`

## 1. Primitive composition

For labeled contents, `n ⊕ m` is componentwise addition when `supp(n+m)` has cardinality at most two.  This is the only composition law supplied by the blind packet.  No scalar law is assumed.

## 2. Canonical structural quotient does not inherit composition without alignment

Let every unit state have orbit signature `Lambda=(0,0,1)`.

Two individually identical unit-orbit inputs admit two different admissible relative alignments:

- same component: `(1,0,0) ⊕ (1,0,0) = (2,0,0)`, so `Lambda=(0,0,2)`;
- distinct components: `(1,0,0) ⊕ (0,1,0) = (1,1,0)`, so `Lambda=(0,1,1)`.

Therefore there is **no single-valued binary operation on `Lambda`-classes alone** reproducing primitive composition.  The missing datum is relative component alignment between the two operands.

This is a structural result, not a failure of `Lambda` as an invariant.

## 3. Scalar composition laws

### `TOTAL`

`N(n)=sum_i n_i`.

For every admissible composition,

`N(n⊕m)=N(n)+N(m)`.

This follows directly from componentwise addition and finite disjoint-union cardinality.

### `SUPPORT`

Not additive.  Smallest counterexample:

`(0,0,1) ⊕ (0,0,1) = (0,0,2)`,

while `1 != 1+1`.

### `MAXBLOCK`

Not additive.  Smallest counterexample:

`(0,0,1) ⊕ (0,1,0) = (0,1,1)`,

while `1 != 1+1`.

### `CROSS2`

Let `X(n)` count unordered two-token subsets with distinct types.  Exact labeled-content law:

`X(n⊕m)=X(n)+X(m)+sum_{i<j}(n_i m_j+n_j m_i)`.

It is not additive.  Smallest counterexample is two unit tokens on distinct components, where `0+0` becomes `1`.

### `SAME2`

Let `H(n)` count unordered two-token subsets with the same type.  Exact labeled-content law:

`H(n⊕m)=H(n)+H(m)+sum_i n_i m_i`.

It is not additive.  Smallest counterexample is two unit tokens on the same component, where `0+0` becomes `1`.

The cross terms are derived by partitioning unordered two-token subsets according to whether both tokens came from one operand or one from each operand.

## 4. Conditional additive-classification theorem

Suppose, **as an extra hypothesis**, that an `N`-valued readout `F` satisfies:

1. full `S3` invariance;
2. `F(0)=0`;
3. `F(n⊕m)=F(n)+F(m)` for every admissible composition.

Let `e_i` be a unit on component `i`.  `S3` invariance gives a common value

`c=F(e_1)=F(e_2)=F(e_3)`.

Repeated admissible composition gives `F(a e_i)=a c`.  Every two-supported state is `a e_i+b e_j`, hence additivity gives

`F(n)=(a+b)c = c N(n)`.

Therefore all such additive invariant readouts are exactly `c*N`.  If one **also** adds unit normalization `F(e_i)=1`, then `c=1` and

`F=N`.

This is a genuine conditional uniqueness theorem, but its selecting assumptions are not primitive data.  In particular:
- without additivity, `TOTAL` and `MAXBLOCK` already coexist;
- with additivity but without unit normalization, the family `c*N` remains.

## 5. Checker status

The deterministic checker tested:
- all `127` sector-supported states with multiplicities `0..6`;
- all `6` `S3` relabelings (`762` state-permutation checks);
- `7057` admissible ordered composition pairs from the tested input domain;
- the claimed additive and nonadditive laws;
- the orbit-alignment obstruction;
- the conditional family `c*N` for `c=0..6`.

Unclassified mismatch count: `0`.

`COMPOSITION_LAWS_DERIVED_OR_FALSIFIED_NOT_ASSUMED = PASS`.
