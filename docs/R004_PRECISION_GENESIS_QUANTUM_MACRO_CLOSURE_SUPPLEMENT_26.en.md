# R004 precision genesis — Supplement 26: matroid temporal retirement

Status: `PROVED_WIP + EXECUTABLE_REFERENCE + MODULE-CUT TEMPORAL SPECIALIZATION`  
Parent: `R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_25.en.md`  
Owner branch: `research/r004-precision-genesis-closure-20260810`

Supplement 25 showed that generic temporal instruction retirement can require anticipatory redundancy because stagewise minimum hitting sets need not nest. This supplement isolates a sharp positive specialization for the exact-state Module Cut backend, and then shows exactly where it fails again.

## 1. Matroid cut translation

In the exact-state Module Cut Compiler, each suffix point i has a representable matroid `M_i` on the reset-instruction ground set E.

Deletion cuts are the circuits of `M_i`. A retained reset set `S_i` hits every circuit iff its complement

`H_i=E\S_i`

is independent in `M_i`.

A cardinality-minimum retained set corresponds exactly to `H_i` being a basis of `M_i`, so

`|S_i|=|E|-r(M_i)`.

## 2. Future weakening as nested independent families

Assume suffix requirements weaken so that

`I(M_i) subseteq I(M_(i+1))`.

Every hidden set that was safe/independent earlier remains safe later. In particular, any basis `B_i` of `M_i` is independent in `M_(i+1)`.

By the ordinary matroid basis-extension theorem, `B_i` extends to some basis `B_(i+1)` of `M_(i+1)`:

`B_i subseteq B_(i+1)`.

Taking complements gives

`S_(i+1) subseteq S_i`.

Thus no-reacquisition is compatible with stagewise cardinality optimality throughout the chain.

## 3. Exact retirement count

Because every stage uses a basis complement,

`|S_i|-|S_(i+1)| = r(M_(i+1))-r(M_i)`.

Each newly available independent hidden direction retires exactly one primitive reset instruction.

Therefore, for unit instruction cost, the temporal exact-state Module Cut problem has a closed rank solution and does not exhibit Supplement 25's anticipatory-redundancy penalty.

## 4. Why this is special

The theorem uses two matroid facts simultaneously:

1. adequacy is exactly independence of the hidden complement;
2. every independent set extends to a basis.

Generic obstruction clutters have neither property. Structural Target cuts from Supplement 20 already need not be matroidal, so the result cannot be promoted to the entire Representation Compiler.

## 5. Nonuniform costs restore anticipatory tradeoffs

With generator-specific holding costs, minimizing retained cost is equivalent to maximizing the total weight of the hidden matroid basis.

Maximum-weight bases of nested matroids need not themselves nest.

A binary-representable four-element example is enough.

Early columns over `F_2`:

`(0,1), (1,0), (1,1), (0,1)`.

Later columns:

`(0,0,1), (0,1,0), (1,0,0), (0,1,1)`.

The early independent family is contained in the later one. Give element weights

`(3,2,1,3)`.

The early maximum-weight bases are

`{0,1}` and `{1,3}`,

while the unique later maximum-weight basis is

`{0,2,3}`.

No early weighted-optimal basis is contained in the later weighted-optimal basis. Equivalently, no later weighted-minimum retained set is contained in an early weighted-minimum retained set.

Thus

`nested matroid + unit cost => nested stagewise optimum`,

but

`nested matroid + nonuniform cost !=> nested stagewise weighted optimum`.

Anticipatory retention returns as soon as the resource axis is richer than cardinality/rank.

## 6. Exhaustive representable-matroid pressure test

All labeled binary-representable matroids on four elements obtainable from ambient dimensions up to three were enumerated, giving 66 distinct independent-set systems.

There are **1,270** ordered pairs with nested independent families. For positive element weights in `{1,2,3}^4`, this gives **102,870** pair/weight instances.

- the cardinality basis-extension theorem held mechanically for every nested pair;
- **792** of the 1,270 nested pairs admit at least one tested weight vector for which no early maximum-weight basis nests into any later maximum-weight basis;
- across the tested weight vectors there were **15,672** such nonnested weighted-optimum instances.

So weighted failure is not exceptional even inside binary-representable matroid families.

## 7. Architecture consequence

The temporal compiler must keep its resource objective typed just like its future semantics.

- If primitive cost is pure cardinality, Module Cut can use rank and basis extension.
- If costs are nonuniform, time-dependent, acquisition-sensitive or p-adic-depth-weighted, fall back to the general temporal cut-cover optimizer unless stronger structure is proved.

A scalar phrase such as "minimum instruction set" is therefore incomplete until the cost model and acquisition policy are declared.

## 8. Next frontier

The next useful specialization is p-adic Structural Target retirement. There cuts carry missing-target modules and exponent depths rather than ordinary matroid circuits. The open question is whether nested target-defect exact sequences yield a tractable temporal cost law for depth-weighted repairs, or whether extension data reintroduces the full generic temporal optimization problem.
