# P022 — Rank Two Is the Unique Binary Multi-Channel Repair Regime

Status: `ACTIVE RESEARCH NOTE / EXACT FINITE BOUNDARY / CROSS-ROUTE GENERALIZATION CANDIDATE`  
Owner: `program/p022-geometry-v2`  
Depends on: higher-channel orbit-path lift multiplicity; two-channel `2^(E+B)` repair theorem  
Cross-route relevance: A2/P023 minimal repair; A4 witness multiplicity; P024 typed precision

## 1. Question

The higher-channel path-lift theorem replaces the rank-two binary formula

\[
2^{E+B}
\]

by a product of exact local integer lift multiplicities.

This note asks whether rank three is merely the first accidental counterexample or whether rank two is structurally unique.

The answer is sharp:

> among genuinely multi-channel signed-permutation quotients, rank two is the only dimension in which every local repair radix is forced to remain a power of two.

---

## 2. Equal positive clusters

Fix dimension `d>=1` and a positive integer magnitude `a`.  Consider the chamber state

\[
p=(a,a,\ldots,a).
\]

At one microscopic step every labelled coordinate moves either inward to

\[
a-1
\]

or outward to

\[
a+1.
\]

Suppose exactly `k` labelled coordinates move inward.  After forgetting labels, the target chamber is

\[
\boxed{
r_k=(a-1)^k(a+1)^{d-k},}
\]

where exponent notation denotes multiplicity of equal entries.

The only hidden choice is **which** `k` labels moved inward.

Therefore:

\[
\boxed{
m(p,r_k)=\binom dk.}
\]

This also follows immediately from the transition polynomial

\[
(z_{a-1}+z_{a+1})^d.
\]

---

## 3. P022-BR01 — exact equal-cluster binomial spectrum

For every `d>=1`, `a>0`,

\[
\boxed{
\{m(p,r):r\text{ reachable}\}
=
\left\{\binom d0,\binom d1,\ldots,\binom dd\right\}
}
\]

with target chambers distinguished by the number of inward coordinates.

Thus the local repair arithmetic already contains the complete binomial row of the cluster multiplicity `d`.

The microscopic step count is recovered by

\[
\sum_{k=0}^d\binom dk=2^d.
\]

---

## 4. P022-BR02 — rank two is the unique binary multi-channel rank

### Rank one

The positive equal-cluster row is

\[
(1,1).
\]

At zero, both signs collapse to the same magnitude-one state and give radix two.

So rank one is trivially binary.

### Rank two

The binomial row is

\[
(1,2,1).
\]

The established `B_2/C_2` repair theorem proves more strongly that **every** legal rank-two quotient transition has lift multiplicity

\[
1,2,\text{ or }4,
\]

and every path fiber factors as

\[
2^{E+B}.
\]

### Rank three

The equal-cluster row contains

\[
\binom31=3.
\]

Hence non-binary branching appears immediately.

### Every rank `d>=4`

Use

\[
\binom d2=\frac{d(d-1)}2.
\]

Since `d` and `d-1` are coprime and exactly one is odd, if this quotient were a power of two then the odd member of the pair `{d,d-1}` would have to equal one.  For `d>=4` that is impossible.

Therefore

\[
\boxed{
\binom d2\text{ is not a power of two for every }d\ge4.
}
\]

Combining all cases:

\[
\boxed{
\text{among }d\ge2,
\quad
 d=2
\text{ is the unique rank with purely binary local repair.}
}
\]

This is a structural boundary, not a bounded search.

---

## 5. P022-BR03 — odd-prime repair is unavoidable above rank two

A positive integer is a power of two exactly when its prime factorization has no odd prime.

BR02 therefore implies:

\[
\boxed{
\forall d\ge3,
\quad
\exists\text{ a legal local quotient transition whose lift multiplicity contains an odd prime factor.}
}
\]

Examples:

\[
d=3:\quad3,
\]

\[
d=4:\quad6=2\cdot3,
\]

\[
d=5:\quad10=2\cdot5.
\]

Thus higher-channel repair cannot be represented exactly by merely counting independent yes/no wall flags.

---

## 6. Prime-valuation repair coordinates

For any positive integer lift multiplicity `m`, let

\[
v_p(m)
\]

be the ordinary prime valuation.

For a coarse path with local radices

\[
m_1,m_2,\ldots,m_N,
\]

the exact fiber size is

\[
F=\prod_tm_t.
\]

Hence for every prime `p`,

\[
\boxed{
v_p(F)=\sum_tv_p(m_t).}
\]

The finite vector

\[
\boxed{
\nu(F)=\{(p,v_p(F)):v_p(F)>0\}
}
\]

is therefore an additive integer coordinate of total fiber size.

For the rank-three path

\[
(0,0,0)
\to(1,1,1)
\to(0,0,2),
\]

local radices are

\[
(8,3)
\]

and

\[
\boxed{
F=24=2^3\cdot3,
\qquad
\nu(F)=\{(2,3),(3,1)\}.
}
\]

Rank-two paths have only a `p=2` coordinate; higher rank generically introduces additional prime channels.

This is an exact integer alternative to forcing every repair state into a rounded base-two bit budget.

---

## 7. Important information boundary

Prime valuations reconstruct the **total fiber cardinality** exactly, but they do not reconstruct the ordered sequence of local radices.

Likewise, the scalar product

\[
F=\prod_tm_t
\]

forgets when and why each local branch occurred.

So there is a hierarchy:

\[
\boxed{
\text{local radix sequence}
\longrightarrow
\text{prime-valuation total}
\longleftrightarrow
\text{total fiber cardinality}.
}
\]

The first arrow can lose future-relevant mechanism information.

This is the higher-rank analogue of the established rank-two distinction between typed `(E,B)` repair and the scalar total `E+B`: equal final fiber size does not imply equal repair mechanism.

---

## 8. Consequence for precision mathematics

The primitive exact object is now clear:

\[
\boxed{
\text{repair state}
=
\text{finite set / local branch choice among }m(p,r)\text{ lifts},
}
\]

not

\[
\text{repair state}=\text{some number of bits}.
\]

Binary bits are one efficient coordinate only when every local branch multiplicity factors into independent two-way choices, as happens in the rank-two Barlow quotient.

For general future-compatible quotient theory, the safe formulation should therefore be:

> retain the minimum finite witness state required to choose a legal lift for the declared future language.

Whether that state admits a binary factorization is a secondary theorem, not part of the definition.

This is directly relevant to A2/P023 and P024.  P022 retains the exact signed-channel counterexample proving why the distinction is necessary.

---

## 9. Relation to higher collision structure

P011 collision statistics see fiber cardinalities.  In the present path-lift setting, prime valuations provide one exact arithmetic encoding of those cardinalities.

But two coarse paths can have the same total fiber size while different local radix sequences generate it.  Thus collision cardinality alone does not generally recover the time-labelled lifting mechanism.

This mirrors several earlier P022 findings:

- shell cardinality can lose path multiplicity;
- global multiplicity can lose layer allocation;
- total repair can lose repair type;
- total fiber size can lose local mixed-radix history.

The same structural lesson keeps recurring:

\[
\boxed{
\text{aggregation is legal only relative to the declared future observable.}
}
\]

---

## 10. Prior-art boundary

Binomial coefficients, prime valuations, unique factorization, hyperoctahedral group actions and orbit transitions are established mathematics.

P022 does not claim these ingredients.

The project-specific content is their exact occurrence as repair radices of the signed-channel quotient and the sharp theorem that the rank-two binary repair architecture is exceptional rather than generic.

Historical novelty of that combination remains `NOVELTY_UNVERIFIED`.

---

## 11. Executable assets

Added:

- `src/enterprise_math/p022_barlow_binary_repair_boundary.py`;
- `tests/test_p022_barlow_binary_repair_boundary.py`.

The tests verify the binomial spectrum through multiple ranks/magnitudes, prove executable non-binary witnesses through rank 49, recover the rank-three prime signature, and confirm that representative rank-two paths remain purely 2-adic.
