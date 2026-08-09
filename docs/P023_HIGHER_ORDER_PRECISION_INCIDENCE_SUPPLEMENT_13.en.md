# P023 — Higher-Order Precision Incidence, Supplement 13

Status: `PROVED RESEARCH NOTE + NEGATIVE BOUNDARY`  
Owner: A2 / P023, with A4 witness-identity interpretation  
Depends on: P023-S12 pairwise incidence geometry  
Discipline: finite hypergraphs, joint partitions, and marginal/projection loss are established combinatorial ideas. The project contribution is the exact conditional-repair interface and the explicit no-go boundary for reconstructing joint precision from pairwise shadows.

## 1. Pairwise incidence is not the complete joint state

For precision relations

\[
E_1,\ldots,E_m
\]

on a finite nonempty state set `X`, define the **realized precision incidence hypergraph**

\[
\boxed{
\Gamma(E_1,\ldots,E_m)
=
\{(B_1,\ldots,B_m):
B_i\in X/E_i,
\ \bigcap_i B_i\ne\varnothing\}.
}
\]

For `m=2` this is exactly the bipartite incidence graph of S12.

For `m>=3`, the pairwise projections of `Gamma` can lose genuine higher-order witness identity.

## 2. P023-S13-T01 — Hyperedges are exact joint precision classes

Status: `PROVED`.

The common refinement

\[
E_1\cap\cdots\cap E_m
\]

has one block for every realized tuple in `Gamma`. Therefore

\[
\boxed{
\left|X/\bigcap_iE_i\right|
=
|\Gamma(E_1,\ldots,E_m)|.
}
\]

### Proof

A block of the common refinement is exactly a nonempty intersection of one block from each supplied partition. Distinct realized block-label tuples give disjoint common-refinement blocks. ∎

The full formal candidate count

\[
\prod_i|X/E_i|
\]

is merely the complete multipartite tuple space; the realized hyperedges are the actual joint task states.

## 3. Conditional extension degree

Suppose the tasks

\[
E_1,\ldots,E_m
\]

are already retained. Their joint precision is

\[
C_m=\bigcap_{i=1}^mE_i.
\]

Now add one more task `F`.

For one realized prefix tuple `tau`, equivalently one `C_m` block, let

\[
\operatorname{Ext}_F(\tau)
=
\{D\in X/F:\tau\text{ extends to a realized }(m+1)\text{-tuple with }D\}.
\]

The extension degree is

\[
e_F(\tau)=|\operatorname{Ext}_F(\tau)|.
\]

## 4. P023-S13-T02 — Conditional repair equals maximum extension degree

Status: `PROVED`.

The exact minimum alphabet required to add task `F` after context `C_m` is

\[
\boxed{
\rho(F\mid C_m)
:=
R(C_m\to C_m\cap F)
=
\max_{\tau\in\Gamma(E_1,\ldots,E_m)}e_F(\tau).
}
\]

### Proof

One retained prefix tuple is one coarse `C_m` block. Its target subblocks after adding `F` are exactly the distinct `F` blocks that extend that tuple. P023-S9 says the minimum shared alphabet is the maximum number of target subblocks inside one current block. ∎

Thus repair is inherently **conditional on already retained context**.

## 5. P023-S13-T03 — Conditional repair spectrum

Status: `PROVED`.

Define

\[
\boxed{
\mathcal R_k(F\mid C_m)
=
\sum_{\tau}
\binom{e_F(\tau)}k.
}
\]

This is the S11 quotient-projection spectrum of

\[
X/(C_m\cap F)\to X/C_m.
\]

Hence it recovers the full distribution of conditional local repair alphabet sizes, not only the worst-case maximum.

## 6. P023-S13-T04 — More retained context cannot increase conditional repair

Status: `PROVED`.

If

\[
C'\subseteq C
\]

is a finer known context, then for every added task `F`,

\[
\boxed{
\rho(F\mid C')
\le
\rho(F\mid C).
}
\]

### Proof

Every `C'` block lies inside one `C` block. Therefore it can meet only a subset of the `F` blocks met by its parent `C` block. Its extension degree cannot be larger. Taking maxima proves the claim. ∎

This is a pure finite-partition version of the operational rule:

\[
\boxed{
\text{more exact context}
\Longrightarrow
\text{no larger additional repair requirement}.
}
\]

No probability or entropy notion is involved.

## 7. P023-S13-T05 — Pairwise weighted incidence does not determine triple precision

Status: `PROVED BY EXPLICIT COUNTEREXAMPLE`.

Take the same eight-state set in two different triple-partition systems.

### System A — duplicated even parity

Realized triples are

\[
000,011,101,110,
\]

each realized by two raw states.

### System B — full binary cube

All eight triples

\[
000,001,010,011,100,101,110,111
\]

are realized once.

In both systems:

- every single binary partition has block sizes `4+4`;
- every pair of partitions realizes all four pair-label combinations;
- every pairwise intersection cell has cardinality exactly `2`.

Thus **all pairwise weighted incidence tables are identical**.

Yet the joint precision differs:

\[
\boxed{
|X/(E_1\cap E_2\cap E_3)|
=4
\quad\text{in System A},
}
\]

while

\[
\boxed{
|X/(E_1\cap E_2\cap E_3)|
=8
\quad\text{in System B}.
}
\]

Therefore neither pairwise incidence graphs nor pairwise intersection cardinalities determine the triple common refinement.

## 8. P023-S13-T06 — Pairwise repair geometry does not determine conditional repair

Status: `PROVED BY THE SAME COUNTEREXAMPLE`.

In both systems, for every distinct pair `i,j`,

\[
\boxed{
\rho(E_i,E_j)=2.
}
\]

Hence all pairwise directed repair factors, integer depths, and symmetric S12 distances agree.

But after retaining `E_1` and `E_2`:

### System A

Even parity determines the third label exactly, so

\[
\boxed{
\rho(E_3\mid E_1\cap E_2)=1.
}
\]

### System B

Both third labels remain possible under every `(E_1,E_2)` pair, so

\[
\boxed{
\rho(E_3\mid E_1\cap E_2)=2.
}
\]

Thus pairwise precision geometry cannot reconstruct higher-order conditional task cost.

This is the precision analogue of A4's witness-identity boundary: pairwise shadows can preserve every marginal count while losing the identity tying several relations together.

## 9. Hypergraph interpretation of task redundancy

An added task `F` is redundant under known context `C` exactly when

\[
\boxed{
\rho(F\mid C)=1.
}
\]

Equivalently every realized `C` hyperedge has a unique extension to an `F` block.

This is stronger than pairwise label recovery. A task may be nonredundant relative to every single existing task but become redundant after several tasks are retained together, as in the even-parity example.

## 10. Sequential task addition

For an ordered task family

\[
E_1,E_2,\ldots,E_m,
\]

let

\[
C_j=\bigcap_{i=1}^jE_i.
\]

At stage `j+1`, the exact local repair factor is

\[
\rho(E_{j+1}\mid C_j).
\]

The final joint class count obeys the exact recurrence

\[
|X/C_{j+1}|
=
\sum_{B\in X/C_j}
\#\{E_{j+1}\text{ blocks meeting }B\},
\]

and hence the bound

\[
\boxed{
|X/C_m|
\le
|X/E_1|
\prod_{j=2}^m
\rho(E_j\mid C_{j-1}).
}
\]

The bound can be strict because stagewise worst extension degrees need not occur on the same branch.

This connects directly to P018 adaptive query/precision scheduling.

## 11. Research-tool rule

For `m>=3` task families:

1. pairwise incidence graphs remain useful for local costs and upper bounds;
2. never reconstruct the joint state from pairwise data alone without a theorem;
3. compile the realized tuple hypergraph or an exact sufficient representation of it;
4. compute added-task repair conditionally on the **current joint context**, not from pairwise costs in isolation.

## 12. Executable specification

- `src/enterprise_math/precision_incidence_hypergraph.py`
- `tests/test_precision_incidence_hypergraph.py`

The regression pins the eight-state even-parity/full-cube counterexample, including equality of all weighted pairwise incidence tables, different triple class counts, and conditional repair `1` versus `2`.

## 13. Foundation boundary

S12 provides a valid pairwise metric geometry; S13 proves that such a metric is not a complete invariant of a multi-task precision system. Higher-order context lives in realized hyperedges/witness identity and must be represented separately when the task language can query it.
