# P004 — Fixed points of finite collapse words

Status: `PROVED`  
Open problem: `P004`  
Scope: ordinary mathematics

## 1. Question

Let a finite word of positive-exponent perfect-power collapse operators be

\[
W=C_{p_m}\circ\cdots\circ C_{p_1}.
\]

P004 asks for the fixed points of \(W\).

The answer is completely controlled by the least common multiple of the exponents.

Let

\[
L=\operatorname{lcm}(p_1,\ldots,p_m).
\]

For the empty word, take \(W=\operatorname{id}\) and \(L=1\).

## 2. Fixed points of a composition of reductive maps

### P004-T01 — Fixed-point intersection lemma

Status: `PROVED`

Let \(f_1,\ldots,f_m\) be maps on a partially ordered set such that

\[
f_i(x)\le x
\]

for every \(i,x\). Let

\[
F=f_m\circ\cdots\circ f_1.
\]

Then

\[
\operatorname{Fix}(F)=\bigcap_{i=1}^m\operatorname{Fix}(f_i).
\]

### Proof

The inclusion from right to left is immediate: if every \(f_i\) fixes \(x\), then their composition fixes \(x\).

Conversely suppose \(F(x)=x\). Define

\[
x_0=x,
\qquad
x_i=f_i(x_{i-1}).
\]

Reductivity gives the chain

\[
x=x_0\ge x_1\ge\cdots\ge x_m=F(x)=x.
\]

By antisymmetry, every term in the chain equals \(x\). Hence

\[
f_i(x)=x
\]

for every \(i\), so \(x\) lies in every fixed-point set. ∎

This lemma does **not** require the maps to commute or be idempotent; reductivity alone is enough.

## 3. Intersection of perfect-power state sets

For positive \(p\), T006 gives

\[
\operatorname{Fix}(C_p)=\{a^p:a\in\mathbb N\}.
\]

### P004-T02 — Perfect-power intersection theorem

Status: `PROVED`

For positive integers \(p_1,\ldots,p_m\) and

\[
L=\operatorname{lcm}(p_1,\ldots,p_m),
\]

an integer \(n\in\mathbb N\) is simultaneously a perfect \(p_i\)-th power for every \(i\) if and only if it is a perfect \(L\)-th power.

### Proof

The states \(0\) and \(1\) are powers of every positive exponent, so assume \(n>1\).

Write the unique prime factorization

\[
n=\prod_r r^{e_r}.
\]

The integer \(n\) is a perfect \(p_i\)-th power exactly when every prime exponent \(e_r\) is divisible by \(p_i\). Therefore \(n\) is a perfect \(p_i\)-th power for every \(i\) exactly when every \(e_r\) is divisible by every \(p_i\), which is equivalent to

\[
L\mid e_r
\]

for every prime \(r\). That is exactly the condition that \(n\) be a perfect \(L\)-th power. ∎

## 4. Complete P004 classification

### P004-T03 — Fixed points of a collapse word

Status: `PROVED`

Let

\[
W=C_{p_m}\circ\cdots\circ C_{p_1}
\]

with every \(p_i\ge1\), and let

\[
L=\operatorname{lcm}(p_1,\ldots,p_m).
\]

Then

\[
\operatorname{Fix}(W)
=
\bigcap_{i=1}^m\operatorname{Fix}(C_{p_i})
=
\operatorname{Fix}(C_L).
\]

Equivalently,

\[
W(n)=n
\iff
\exists a\in\mathbb N:\ n=a^L.
\]

For the empty word, \(L=1\), \(W=\operatorname{id}=C_1\), so the same statement remains valid.

### Proof

Every \(C_{p_i}\) is reductive by T004. P004-T01 therefore gives the first equality. T006 and P004-T02 give the second equality. ∎

## 5. What the theorem does and does not say

The fixed-point set depends only on the least common multiple of the exponents. Therefore it is invariant under:

- reordering the word;
- repeating an exponent;
- replacing the exponent list by any other list with the same least common multiple.

But the **single-pass transformation itself is not determined by the lcm**.

For example, with exponents \(2\) and \(3\), both words have \(L=6\) and the same fixed states, but at \(n=8\):

\[
C_2(C_3(8))=4,
\qquad
C_3(C_2(8))=1.
\]

Thus

\[
\operatorname{Fix}(C_2C_3)=
\operatorname{Fix}(C_3C_2)=
\operatorname{Fix}(C_6),
\]

while

\[
C_2C_3\ne C_3C_2.
\]

P003 classifies exactly when that stronger operator equality holds.

## 6. Structural consequence

P003 showed that pairwise commutation is controlled by comparability in the divisibility order. P004 shows that **fixed-point semantics forgets the order completely** and remembers only the join of the exponents in the divisibility lattice:

\[
p_1\vee\cdots\vee p_m
=
\operatorname{lcm}(p_1,\ldots,p_m).
\]

So the collapse word has two distinct layers of information:

1. **transient/action layer** — sensitive to word order when exponents are incomparable;
2. **fixed-state layer** — determined only by the lcm.

This separation is important for P009: iteration can erase the transient word-order dependence even though one pass does not.

## 7. Prior-art and novelty discipline

The fixed-point intersection lemma is an elementary order argument, and the perfect-power intersection step is an elementary consequence of unique prime factorization and the defining property of least common multiples. These ingredients are established mathematics.

A targeted prior-art/API search during this pass did not identify an exact published statement phrased as the fixed-point classification of the Enterprise Math collapse family. That absence is not a historical-priority result.

Accordingly:

- P004-T03 is `PROVED` as ordinary mathematics;
- its exact historical novelty remains `NOVELTY_UNVERIFIED`;
- no priority claim is made.

## 8. Consequence for P009

P004 immediately supplies the fixed-state part of the collapse-semigroup problem.

For a fixed word \(W\), repeated iteration produces a nonincreasing integer sequence because \(W(n)\le n\). Hence every orbit stabilizes after finitely many strict decreases. Once stabilized, P004-T03 forces the limit to be a perfect \(L\)-th power.

A stronger result is available: the limit is exactly

\[
C_L(n_0),
\]

not merely some perfect \(L\)-th power. That statement belongs to P009 and should be proved there separately.
