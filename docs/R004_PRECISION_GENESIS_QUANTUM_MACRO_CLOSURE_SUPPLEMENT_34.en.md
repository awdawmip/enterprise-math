# R004 precision genesis — Supplement 34: binary k-local storage/update/readout Pareto

Status: `PROVED_WIP + EXECUTABLE_REFERENCE + RESOURCE-PARETO SPECIALIZATION`
Parent: `R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_33.en.md`

Work in the full binary additive semantic module `F_2^r`. For `1<=k<=r`, let the primitive ISA contain every nonzero vector of Hamming weight at most k.

## 1. Exact family

Primitive storage count:

`S_k=sum_(j=1)^k binom(r,j)`.

Streaming witness-update incidences:

`U_k=sum_(j=1)^k j*binom(r,j) = r*sum_(j=0)^(k-1) binom(r-1,j)`.

A semantic vector of Hamming weight w has exact shortest readout length

`ell_k(w)=ceil(w/k)`,

because one primitive covers at most k support coordinates and the support can be partitioned into chunks of size at most k.

Therefore the worst readout depth is `D_k=ceil(r/k)`, and total readout word length over all nonzero semantic queries is

`R_k=sum_(w=1)^r binom(r,w)*ceil(w/k)`.

## 2. Pareto interpretation

- `k=1`: basis/Hasse ISA, minimum storage and update surface, worst readout depth r.
- `k=r`: full semantic table, `2^r-1` primitives, every query one-step.
- intermediate k trades persistent storage/write work for shorter future semantic execution.

This is the counter-ISA analogue of the Stage131 rule-table storage/execution-depth Pareto.

## 3. Important negative boundary

This k-local family is constructive, not generally storage-optimal at a fixed readout depth. Supplement 35 identifies the true unrestricted optimization problem with linear covering codes, whose best constructions can be exponentially smaller than the k-local table.

## 4. Validation

Reference formulas were checked by exact support partitioning and exhaustive semantic-vector enumeration for small ranks.
