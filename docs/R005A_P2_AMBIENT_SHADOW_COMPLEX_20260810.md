# R005-A — Ambient Closure Complex × Non-Forced Shadow

Status: `PROVED R005 STRUCTURE + EXACT CROSS-CHECK / NOT CANONICAL / LEAN PENDING`  
Date: `2026-08-10`

## 1. Main correction

The squarefree closure identity

\[
\kappa_k(p,q)=r,\qquad
\kappa_k(p,r)=q,\qquad
\kappa_k(q,r)=p
\]

should **not** itself be interpreted as a residual-specific new geometry.

For

\[
A=k^2,\qquad U=k^2+2k,
\]

take an odd three-prime basin point

\[
N=pqr\in(A,U],
\]

with

\[
pq>k.
\]

Then

\[
\frac{U-A}{pq}
=
\frac{2k}{pq}<2.
\]

Since r is odd and

\[
\frac A{pq}<r\le\frac U{pq},
\]

r is automatically the unique odd integer closure

\[
r=\operatorname{oddFloor}\!\left(\frac U{pq}\right).
\]

The same holds for the other two pairs whenever their pair products exceed k.

Thus the local Steiner-like closure belongs to the **ambient multiplicative
thin shell**, not specifically to primality residuals.

The actual R005 content is the intersection of this ambient closure structure
with the non-forced witness field.

---

# 2. Ambient closure complex

Assume the fourth-root core is forced and write

\[
C_4=\lfloor U^{1/4}\rfloor.
\]

Define the ambient closure complex \(\mathcal H_k\) as follows.

Vertices are prime candidate coordinates

\[
C_4<q\le k.
\]

An ambient block is the distinct-prime support of an odd three-factor basin
integer

\[
N=abc,\qquad
C_4<a\le b\le c\le k,
\qquad
A<N\le U.
\]

The multiplicities may be:

- repeated-prime:
  \[
  q^2r,
  \]
  whose support is a 2-edge \(\{q,r\}\);
- squarefree:
  \[
  qrs,
  \]
  whose support is a 3-edge \(\{q,r,s\}\).

The closure operation

\[
\kappa_k(p,q)
=
\operatorname{oddFloor}\!\left(\frac{U}{pq}\right)
\]

reconstructs the third multiplicative coordinate whenever the pair belongs to
an ambient block.

---

# 3. T-A30 — closure-shadow factorization

Let

\[
NF_k
=
\{q\le k:
q\text{ is a non-forced divisor witness}\}.
\]

Let \(\mathcal R_k\) be the residual support hypergraph.

Then on the fourth-root-forced theorem slice:

\[
\boxed{
\mathcal R_k
=
\mathcal H_k[NF_k].
}
\]

That is:

> **residual geometry = ambient arithmetic closure complex induced on the
> non-forced prime-gap shadow.**

### Proof

If N is residual, earlier R005 results give:

- \(\Omega(N)=3\);
- every prime factor lies above \(C_4\);
- every prime factor is a candidate witness \(\le k\);
- every distinct prime factor is non-forced.

So its support is an ambient block wholly contained in \(NF_k\).

Conversely, if an ambient block has every vertex in \(NF_k\), its basin
integer has no forced candidate divisor. It therefore survives the forced core
and is residual.

This separates two logically different structures:

1. **ambient closure** — quotient/remainder/product-shell arithmetic;
2. **NF shadow** — prime-gap / witness forcedness.

Neither should be renamed as the other.

---

# 4. T-A31 — ambient linearity

Two distinct ambient support blocks cannot share two distinct witness vertices.

Suppose blocks S and T share distinct primes p,q.

Their corresponding basin integers would both have the form

\[
pqr,\qquad pqs
\]

for some odd primes r,s, with both r and s in

\[
\left(
\frac A{pq},
\frac U{pq}
\right].
\]

But on this shell

\[
pq>C_4^2>\sqrt U>k,
\]

so the interval width is

\[
\frac{2k}{pq}<2.
\]

Two distinct odd integers differ by at least 2. Therefore r=s, so the blocks
are the same.

Hence:

\[
\boxed{
S\ne T
\Longrightarrow
|S\cap T|\le1.
}
\]

Thus \(\mathcal H_k\), and therefore its induced residual subhypergraph
\(\mathcal R_k\), is a **linear rank-\(\le3\) hypergraph**.

The squarefree rank-3 sector is consequently a partial Steiner triple system
in the standard combinatorial sense.

This use of Steiner/linear-hypergraph terminology is classification by prior
mathematics, not a novelty claim.

---

# 5. Pair closure is sufficient

Ambient linearity gives a sharper interpretation of the previously derived
pair closure.

If two distinct factor vertices p,q of a residual are known, there is at most
one ambient block containing that pair.

The arithmetic formula recovers it explicitly:

\[
\boxed{
\kappa_k(p,q)
=
\operatorname{oddFloor}\!\left(\frac U{pq}\right).
}
\]

So two factor coordinates are sufficient to reconstruct the block.

For a squarefree block \(\{p,q,r\}\):

\[
\kappa(p,q)=r,\qquad
\kappa(p,r)=q,\qquad
\kappa(q,r)=p.
\]

For a repeated block \(\{q,r\}\), one closure returns an endpoint according to
which prime is repeated.

Again, the closure identity itself is ambient arithmetic; residuality requires
the vertices to lie in \(NF_k\).

---

# 6. T-A32 — pair arity is generically minimal

A single witness coordinate is **not** sufficient in general to reconstruct a
residual block.

Exact counterexample:

\[
k=1781.
\]

The same non-forced witness

\[
101
\]

belongs to two different residual blocks:

\[
3172511=101^2\cdot311,
\]

with support

\[
\{101,311\},
\]

and

\[
3175339=101\cdot149\cdot211,
\]

with support

\[
\{101,149,211\}.
\]

Therefore

\[
(k,101)
\]

does not determine a unique residual block.

But every distinct factor pair in either block determines its block uniquely
by T-A31 / \(\kappa_k\).

Hence, in the current factor-coordinate language:

\[
\boxed{
\text{generic residual reconstruction arity}=2.
}
\]

This is a real negative boundary against trying to compress the complete
square-basin residual object to one witness coordinate.

It does **not** rule out a different one-coordinate encoding carrying extra
metadata; it rules out reconstruction from k plus one literal factor witness
alone.

---

# 7. T-A33 — repair is exactly a transversal problem

Let \(F_k\) be the forced witness core.

Take an additional witness set

\[
T\subseteq NF_k.
\]

Every non-residual composite is already rejected by \(F_k\).

A residual block S is rejected by the extension exactly when

\[
T\cap S\ne\varnothing.
\]

Therefore:

\[
\boxed{
F_k\cup T
\text{ is a safe composite-covering witness family}
\iff
T
\text{ is a transversal of }\mathcal R_k.
}
\]

Consequences:

- minimum number of extra witnesses:
  \[
  \boxed{\tau(\mathcal R_k)};
  \]
- inclusion-minimal safe repairs:
  inclusion-minimal transversals of \(\mathcal R_k\);
- least safe basis exists:
  exactly when
  \[
  \mathcal R_k=\varnothing.
  \]

This gives an exact factorization of the bounded witness-language optimization
problem:

\[
\text{forced core}
+
\text{transversal of induced closure shadow}.
\]

No novelty is claimed for hypergraph transversals themselves.

---

# 8. Mixed packing bound

Because the residual hypergraph is linear, each unordered vertex pair is used
by at most one block.

Let:

- \(v=|NF_k|\);
- \(E_2\) = number of repeated-prime 2-edges;
- \(E_3\) = number of squarefree 3-edges.

A 2-edge consumes one unordered vertex pair; a 3-edge consumes three.

Hence:

\[
\boxed{
E_2+3E_3\le {v\choose2}.
}
\]

This is a standard packing consequence of linearity.

It is useful here because the arithmetic thin shell forces the residual repair
object into that classical sparse combinatorial class.

---

# 9. Exact cross-check on the current certificate family

The executable builds the **ambient** closure complex first and only then
applies the non-forced shadow.

Across the 49 exact no-least basins:

- ambient closure blocks generated: **2497**;
- ambient rank-2 blocks: **148**;
- ambient rank-3 blocks: **2349**;
- residual blocks after NF induction: **50**;
- residual rank-2 blocks: **45**;
- residual rank-3 blocks: **5**.

Thus only a small part of the ambient closure complex survives the prime-gap
shadow in the current finite family.

The exact induced-subhypergraph identity agrees with the independently
certified direct residual list in every basin.

All 49 currently certified no-least basins happen to have

\[
\tau(\mathcal R_k)=1.
\]

That is **finite evidence only**, not a theorem.

The existing k=1781 basin has two residual blocks sharing the vertex 101, so
its unique one-witness repair is 101.

---

# 10. Important correction to the “Steiner geometry” interpretation

The squarefree triangle closure should be described carefully.

Incorrect overstatement:

> residual primes mysteriously form a new Steiner geometry.

Correct statement:

> the multiplicative square shell already carries a partial Steiner-type
> pair closure; the primality problem selects the induced substructure whose
> vertices are non-forced witnesses.

So the mathematical object of interest is not:

\[
\text{closure geometry alone},
\]

but:

\[
\boxed{
\text{ambient closure complex}
\cap
\text{prime-gap non-forced shadow}.
}
\]

This correction prevents an automatic arithmetic identity from being mistaken
for new residual information.

---

# 11. Prime–Collapse Field interpretation

This gives a more disciplined meaning to “field” in R005-B-compatible
language.

There are two fields on the same candidate-prime coordinates.

### Closure field

Generated from product-shell quotient/remainder data:

\[
(p,q)
\mapsto
\kappa_k(p,q).
\]

### Forcedness field

Generated from local next-prime / pure-power observations:

\[
q
\mapsto
\operatorname{FORCED/NONFORCED}.
\]

The residual object is their intersection:

\[
\boxed{
\text{closed ambient block whose every vertex is NONFORCED}.
}
\]

This is much more precise than plotting primes in a geometric picture.

---

# 12. What remains hard

The reduction does **not** make minimum repair trivial.

A linear rank-3 hypergraph may still have nontrivial transversal structure.

The current exact family has repair number 1, but no theorem says this must
continue.

The right next counterexample target is therefore:

\[
\boxed{
\tau(\mathcal R_k)\ge2.
}
\]

Such a basin would be the first point where one additional witness is no
longer enough to repair the residual language.

That is a more meaningful frontier than merely finding the 51st residual
composite.

---

# 13. Foundation status

Candidate reusable pieces:

- T-A30 closure-shadow factorization;
- T-A31 ambient/residual linearity;
- T-A32 pair reconstruction arity and exact one-witness negative boundary;
- T-A33 repair-transversal factorization.

Classification:

`A2 observation sufficiency + A4 support/correspondence + A0 quotient/remainder`.

Status:

`PROVED R005 STRUCTURE / EXACT FINITE CROSS-CHECK / PRIOR-ART NOVELTY UNVERIFIED`.

Do not promote before:

1. Lean validation of the generic witness-cover layer;
2. formalization of the shell-width / pair uniqueness lemmas;
3. prior-art review of the combined observation-language packaging.
