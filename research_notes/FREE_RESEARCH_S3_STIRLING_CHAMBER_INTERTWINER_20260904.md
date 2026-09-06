# Free Research — `S_3` Standard Energy and the Deepest Stirling Chamber

Status: `FREE_RESEARCH_FRONTIER / EQUIVARIANT_CHAMBER_INDEX_INTERTWINER / EXACT_COEFFICIENT_MATCH / ARITHMETIC_VALUE_INTERTWINER_OPEN / NOT_WORKING_TRUTH / NOT_FOUNDATION`
Date: `2026-09-04`
Parent: `FREE_RESEARCH_PRIME_WINDING_STIRLING_CHAMBERS_20260904.md`

## 1. Executive advance

The equality

\[
\frac19
=
\text{weighted }S_3\text{ relation-energy survival}
=
\text{normalized deepest degree-three cutoff mass}
\]

has an `S_3`-equivariant representation carrier, not merely matching numerical coefficients.

The deepest cutoff chamber has three connected components, indexed by the unique coordinate that does **not** cross the cutoff.  The three constant maps from the history-slot set to the scale-bin set are indexed by their unique image label.  The natural identification of these indices is `S_3`-equivariant.

Both carriers are the three-dimensional permutation representation

\[
\mathbf 1\oplus\mathrm{Std}.
\]

The same two-dimensional standard representation that carries quotient fluctuation is therefore present in the deepest cutoff sector.

---

## 2. Deepest chamber components

Inside

\[
\Delta_3
=\{t_1,t_2,t_3\ge0:\ t_1+t_2+t_3\le3\},
\]

define

\[
D_j
:=\{t\in\Delta_3:\ t_j\le1,\ t_i>1\text{ for }i\ne j\}.
\]

Exactly two coordinates are overcut in `D_j`, and `j` is the unique uncut coordinate.

If `i,k` are the two overcut coordinates, set

\[
s_i=t_i-1,
\qquad
s_k=t_k-1,
\qquad
s_j=t_j.
\]

Then

\[
s_i,s_j,s_k\ge0,
\qquad
s_i+s_j+s_k\le1.
\]

Thus every `D_j` is affinely equivalent to the unit three-simplex and has volume

\[
\boxed{\operatorname{Vol}(D_j)=1/3!=1/6.}
\tag{2.1}
\]

The three components have total volume `1/2`.

---

## SCI-T01 — Equivariant component correspondence

Let

\[
C_j:\{1,2,3\}\to\{1,2,3\}
\]

be the constant map with image `j`.

Define

\[
\boxed{\Phi(D_j)=C_j.}
\tag{3.1}
\]

A permutation `sigma in S_3` acts on chamber coordinates and on scale-bin labels.  It sends

\[
D_j\mapsto D_{\sigma(j)}
\]

and

\[
C_j\mapsto C_{\sigma(j)}.
\]

Therefore

\[
\boxed{\Phi(\sigma D_j)=\sigma\Phi(D_j).}
\tag{3.2}
\]

The component-index space of the deepest chamber and the constant-map space are canonically the same `S_3` set.

---

## SCI-T02 — Representation decomposition

Functions on the three components form the permutation representation

\[
\mathbb R^{\{D_1,D_2,D_3\}}
\cong
\mathbb R^{\{C_1,C_2,C_3\}}.
\]

It decomposes as

\[
\boxed{\mathbf 1\oplus\mathrm{Std}.}
\tag{4.1}
\]

The trivial line is the common component mass.  The standard plane is the zero-sum difference among the three possible surviving coordinates.

This is the same standard representation that appears in the six-history first-label readout after the sign sector vanishes.

Hence the quotient-cloud fluctuation representation has a canonical copy in the deepest cutoff chamber.

---

## SCI-T03 — Exact normalized coefficient

The complete degree-three log simplex has volume

\[
\operatorname{Vol}(\Delta_3)=\frac{3^3}{3!}=\frac92.
\]

Using (2.1), the normalized deepest mass is

\[
\boxed{
\frac{3(1/6)}{9/2}=\frac19.
}
\tag{5.1}
\]

The weighted lift–transpose–project mixer satisfies

\[
\mathcal E_u(\mathcal K_3x)=\frac19\mathcal E_u(x).
\]

Therefore

\[
\boxed{
\mathcal E_u(\mathcal K_3x)
=rac{\operatorname{Vol}(D_1\sqcup D_2\sqcup D_3)}
       {\operatorname{Vol}(\Delta_3)}
\mathcal E_u(x).
}
\tag{5.2}
\]

This coefficient identity is formalized directly.

---

## 6. Selector-square dilation

The global `S_3` mixer may also be written as

\[
\mathcal K_3
=\frac13I+\frac23\Pi,
\]

where `Pi` projects to the weighted mean.

On the standard sector,

\[
\mathcal K_3=\frac13I.
\]

In the tensor-square energy, survival therefore requires both selector copies to retain their original coordinate, contributing

\[
\left(\frac13\right)^2=\frac19.
\]

A selector pair has `3^2=9` possibilities and one double-retention state.  Adjoining the three possible surviving coordinate labels gives `3^3=27` maps, of which the three constant maps are the survival states.

Thus the constant-map sector is the finite dilation of the quadratic standard-energy survival event.

---

## 7. What is and is not proved

Proved:

1. the deepest chamber has three equal simplex components;
2. these components and constant maps are canonically `S_3`-equivariantly indexed;
3. their representation is `1 plus Std`;
4. the normalized deep mass is exactly the `S_3` energy survival coefficient;
5. the coefficient identity holds for every finite weighted value channel.

Not yet proved:

1. a measure-preserving operator taking actual prime-winding relation values on the whole simplex to values supported on the deepest chamber;
2. that the surviving `1/9` energy after one arithmetic history step is literally carried only by doubly overcut prime histories;
3. the lower-scale cascade estimate required for a quantitative prime remainder.

The current result is an equivariant carrier intertwiner, not yet a full arithmetic value intertwiner.

---

## 8. Formal status

Lean file:

- `EnterpriseMath/Relation/S3StirlingIntertwiner.lean`.

It proves:

1. the deepest normalized chamber coefficient is `1/9` over `R`;
2. weighted `S_3` energy equals that chamber fraction times the original energy;
3. the component and constant-map index sets are canonically equivalent.

The exact chamber-count checker independently verifies the `3/27` constant-map count.

---

## 9. Next theorem

Construct a finite chamber-resolved transition kernel whose:

- core action is the stationary triple transposition mixer;
- deepest component is the standard-energy survival state;
- nondeep components are dissipative or pushed to lower-dimensional marginals;
- arithmetic endpoint map sends the deepest component below the current cutoff.

This would upgrade the equivariant coefficient correspondence into an actual renormalization intertwiner.
