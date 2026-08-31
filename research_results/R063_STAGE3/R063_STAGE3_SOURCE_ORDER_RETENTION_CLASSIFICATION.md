# R063 Stage 3 — Source-Order Retention Classification

Status: `CANONICAL_SOURCE_SENSITIVE_RELATION / STRICT_IMPROVEMENT_OVER_WHOLE_TARGET_FIBRE`
Researcher-ID: `EM-R063S3-F1CF9D`

## Choice-free path relation

For source paths `p,q`:

1. form the labelled interaction product poset;
2. take the set `NF` of all maximal signed-cancellation residual induced subposets;
3. apply the already-declared Stage 2 unit/orientation readout to each residual label set;
4. take every linear extension of each residual poset;
5. read its `X_i/X_j` label word.

Call the resulting set `Lift_i(p,q)`. This uses only source path order, the derived interaction table, the nondeterministic cancellation relation taken in full, and the declared ordered readout. It contains no target-word selector.

## W2: exact nine-pair census

For the three `(2,1)` source paths `iij, iji, jii`, every product has target trace `(3,4)` and full native target fiber size `35`. The exact `Lift_i` support-size matrix is

```
          iij  iji  jii
iij         5   14    8
iji        14   11   14
jii         8   14    5
```

All nine relations are nonempty proper subsets of the 35-path fiber, and they are not equal. Thus path order survives multiplication in the process layer.

Across **all nine** source path pairs, the union contains `31/35` target words. The four native target paths never produced by this W2 interaction process are

`iijjjji`, `ijjjjii`, `jiiijjj`, `jjjiiij`.

Hence even union over every source representative does not collapse to the whole target fiber in W2.

## Multiplicity beyond support

The process also defines a formal witness multiplicity: count concrete `(residual normal form, order-respecting linearization)` witnesses mapping to each target word. This coefficient is distinct from native path multiplicity.

Example with full support: `p=jij` (trace `(1,2)`) and `q=jiiij` (trace `(3,2)`) have ordered target `(8,1)`, whose full native fiber has 9 words. The process reaches all 9 words, but its formal coefficients range from `14` to `41`, with `260` total process witnesses. Thus multiplicity information can remain nontrivial even when Boolean/path support is already full.

## Single-valued lift

A nontrivial fiber does not force one target path. For example `Lift_i(iij,iij)` contains five target words. Any choice of one of them adds a selector not supplied by the interaction law.

`SOURCE_PATH_ORDER_RETENTION = PROVED`.

`TRIVIAL_WHOLE_TARGET_FIBRE_RELATION_STRICTLY_IMPROVED = true`.
