# P022 Geodesic Multiplicity Supplement 01 — HCP Contact Graph and Geodesic Growth

Status: `ACTIVE RESEARCH NOTE / EXACT INTEGER DERIVATION / NOVELTY UNVERIFIED`  
Owner: `program/p022-geometry-v2`  
Depends on: `P022_GEODESIC_MULTIPLICITY.*`  
Prior-art boundary: HCP coordination sequences and the general notion of geodesic growth are established subjects; no novelty claim is made before a focused audit.

## 1. Goal

FCC and HCP are the first nontrivial pressure test for the new multiplicity layer because both close packings have coordination number `12` at radius one.

Nearest-neighbor degree therefore cannot distinguish them. Native graph geodesic defect also cannot distinguish them because both use their own unweighted shortest-path metric, so `Gamma=0` identically.

The question is:

> **does the finite multiplicity of shortest witnesses distinguish the two close-packed contact graphs?**

Yes, already at radius two at the spectrum level, and exponentially at the shell-total growth level.

## 2. Integer HCP contact-graph coordinates

Use vertices

\[
(q,r,k)\in\mathbb Z^3.
\]

Each fixed `k` is a triangular lattice with six primitive in-layer moves

\[
(\pm1,0),\ (0,\pm1),\ (1,-1),\ (-1,1).
\]

Even `k` are A layers and odd `k` are B layers in ABAB stacking.

From an even layer, the three contacts in either adjacent B layer use horizontal offsets

\[
S_- = \{(0,0),(-1,0),(0,-1)\}.
\]

From an odd layer, the three contacts in either adjacent A layer use

\[
S_+ = \{(0,0),(1,0),(0,1)\}.
\]

Thus every vertex has

\[
6+3+3=12
\]

neighbors.

This is an entirely integer/combinatorial HCP model.

## 3. P022-HCP01 — exact native graph distance

Let

\[
h(q,r)=\max(|q|,|r|,|q+r|)
\]

be triangular-lattice distance.

Let

\[
\tau(q,r)=\min\{h(q,r),h(q+1,r),h(q,r+1)\}
\]

be distance from `(q,r)` to the B-layer base triangle `S_-`.

### Even target layer

If

\[
|k|=2m,
\]

then

\[
\boxed{
d_H(q,r,k)=m+\max(m,h(q,r)).
}
\]

### Odd target layer

If

\[
|k|=2m+1,
\]

then

\[
\boxed{
d_H(q,r,k)=m+1+\max(m,\tau(q,r)).
}
\]

### Proof

Pair consecutive cross-layer moves.

An even→odd offset comes from `S_-`; an odd→even offset comes from `S_+`. Their pairwise sum can be zero or one of the six primitive triangular moves. Hence every two cross-layer steps change horizontal triangular distance by at most one.

For an even target, any path has at least `2m` cross-layer moves. If it has `H` in-layer moves and `V` cross-layer moves, then

\[
h\le H+V/2.
\]

Therefore its length `L=H+V` satisfies

\[
L\ge2m,
\qquad
L\ge m+h.
\]

So

\[
L\ge m+\max(m,h).
\]

A monotone vertical path uses exactly `2m` cross-layer moves and can realize any triangular displacement of radius at most `m`; if `h>m`, append exactly `h-m` in-layer geodesic steps. This attains the bound.

For an odd target, one cross-layer move is unpaired and lands in `S_-`; the remaining pairs contribute at most one triangular step each. Thus

\[
\tau\le H+\lfloor V/2\rfloor,
\]

with `V>=2m+1`, which gives

\[
L\ge2m+1,
\qquad
L\ge m+1+\tau.
\]

Again monotone vertical motion attains the bound.

So the formulas are exact.

## 4. First coordination shells

The coordinate formula gives

\[
1,12,44,96,170,264,380,516,\ldots
\]

for radii `0,1,2,...`.

This is the expected HCP coordination sequence and independently verifies that the integer contact model has the intended graph geometry.

For the multiplicity research below, shell cardinality is only the first shadow.

## 5. P022-HCP02 — vertical-pair generating polynomial

Introduce the triangular Laurent polynomial

\[
A=x+x^{-1}+y+y^{-1}+xy^{-1}+x^{-1}y.
\]

The even→odd and odd→even horizontal-choice polynomials are

\[
B_-=1+x^{-1}+y^{-1},
\qquad
B_+=1+x+y.
\]

Their product is

\[
\boxed{
B_-B_+=A+3.
}
\]

This identity has a direct graph meaning:

- a pair of vertical moves can realize each of the six triangular primitive displacements in exactly one way;
- zero horizontal displacement occurs in exactly three ways.

The coefficient `3` is already a multiplicity datum invisible to the Boolean adjacency graph.

## 6. P022-HCP03 — exact endpoint shortest-path coefficient formula

A geodesic never uses vertical backtracking. Two extra cross-layer moves cost two steps but create at most one triangular unit of horizontal displacement, which one in-layer step can realize more cheaply.

Therefore every shortest path to layer `k` uses exactly `|k|` monotone cross-layer moves.

### Even layer `|k|=2m`

Let

\[
t=\max(0,h(q,r)-m),
\]

so the total distance is

\[
d=2m+t.
\]

Then

\[
\boxed{
g_H(q,r,2m)
=\binom{2m+t}{t}
[x^qy^r](A+3)^mA^t.
}
\]

### Odd layer `|k|=2m+1`

Let

\[
t=\max(0,\tau(q,r)-m),
\qquad d=2m+1+t.
\]

Then

\[
\boxed{
g_H(q,r,2m+1)
=\binom{2m+1+t}{t}
[x^qy^r]B_-(A+3)^mA^t.
}
\]

The binomial factor chooses the positions of the `t` in-layer moves among the total geodesic word while preserving the alternating order of the cross-layer moves.

This formula is independent of the inward dynamic-programming recurrence

\[
g(v)=\sum_{u\sim v,\ d(u)=d(v)-1}g(u),
\]

and the executable reference checks that the two calculations agree on bounded shells.

## 7. P022-HCP04 — shell-total geodesic count as a finite integer sum

Define the triangular shell geodesic total

\[
E_j=6\cdot2^j-6
\quad(j\ge1)
\]

and the analogous total moving outward from the three-point base triangle

\[
O_j=9\cdot2^j-6
\quad(j\ge0).
\]

For shell radius `n>=1`, split endpoints by target layer.

### Non-extreme even layers

For `|k|=2m<n`, the number of in-layer moves is

\[
t=n-2m>0.
\]

To reach the horizontal shell boundary, none of the `m` factors `(A+3)` may choose the zero displacement: otherwise the maximum horizontal distance drops below the required boundary. Therefore the shell-boundary coefficient sum of `(A+3)^mA^t` is exactly that of

\[
A^{m+t}=A^{n-m}.
\]

The contribution of one such layer is

\[
\binom n{n-2m}E_{n-m}.
\]

There are two layers for every `m>0`; `m=0` is only the central layer.

### Extreme even layers

If `n=2m`, then `t=0` and every horizontal monomial of `(A+3)^m` belongs to the extreme shell. Summing all coefficients gives

\[
(A(1,1)+3)^m=9^m
\]

per extreme layer.

### Non-extreme odd layers

For `|k|=2m+1<n`,

\[
t=n-2m-1>0.
\]

The same boundary argument reduces `(A+3)^m` to `A^m`, but with the base-triangle factor `B_-`. The outward geodesic total is therefore `O_{n-m-1}`, with interleaving factor

\[
\binom n{n-2m-1}.
\]

There are two odd layers.

### Extreme odd layers

If `n=2m+1`, all coefficients of

\[
B_-(A+3)^m
\]

contribute. Their total is

\[
3\cdot9^m
\]

per layer, hence `6*9^m` for the pair.

Putting the pieces together gives the exact finite sum

\[
\boxed{
\begin{aligned}
T_H(n)=\;&E_n
+2\sum_{m=1}^{\lfloor(n-1)/2\rfloor}
\binom n{n-2m}E_{n-m}\\
&+2\sum_{m=0}^{\lfloor(n-2)/2\rfloor}
\binom n{n-2m-1}O_{n-m-1}\\
&+\mathbf 1_{2\mid n}\,2\cdot9^{n/2}
+\mathbf 1_{2\nmid n}\,6\cdot9^{(n-1)/2}.
\end{aligned}
}
\]

All quantities are exact integers.

The first values are

\[
\boxed{
1,12,84,384,1524,5592,19812,68808,236628,\ldots
}
\]

for radii `0,1,2,...`.

## 8. P022-HCP05 — fixed integer recurrence and growth root

The finite-sum formula can be reduced by the standard even/odd binomial identities. For `n>=8`, the shell-total geodesic count satisfies

\[
\boxed{
\begin{aligned}
T_n={}&10T_{n-1}-35T_{n-2}+42T_{n-3}+28T_{n-4}\\
&-112T_{n-5}+92T_{n-6}-24T_{n-7}.
\end{aligned}
}
\]

with

\[
T_1,\ldots,T_7
=12,84,384,1524,5592,19812,68808.
\]

The characteristic polynomial factors exactly as

\[
\boxed{
(\lambda-3)(\lambda-2)(\lambda-1)
(\lambda^2-2)(\lambda^2-4\lambda+2).
}
\]

The dominant algebraic root is

\[
2+\sqrt2.
\]

Thus the HCP shell-total shortest-path multiplicity has exponential rate

\[
T_H(n)=\Theta((2+\sqrt2)^n).
\]

The recurrence and finite-sum formula are exact integer statements. The algebraic root is only a compact asymptotic descriptor.

## 9. P022-HCP06 — FCC/HCP separation hierarchy

For the `A_3/FCC` working graph, the preceding P022 note proved

\[
T_{FCC}(n)
=6\cdot4^n+8\cdot3^n-24\cdot2^n+12,
\]

so

\[
T_{FCC}(n)=\Theta(4^n).
\]

HCP instead grows like

\[
(2+\sqrt2)^n.
\]

Therefore FCC and HCP have:

- the same nearest-neighbor degree `12`;
- polynomial shell-size growth of the same dimension;
- identically zero native graph geodesic defect;
- but **different exponential geodesic witness growth rates**.

This is a strong finite-structure discriminator.

## 10. The full spectrum is strictly stronger than the shell total

At radius two:

### FCC / `A_3`

\[
\{1:12,\ 2:24,\ 4:6\}.
\]

### HCP

\[
\boxed{\{1:18,\ 2:18,\ 3:2,\ 4:6\}.}
\]

Both totals are

\[
84.
\]

Yet the spectra are already different. In HCP the two endpoints

\[
(0,0,2),\qquad(0,0,-2)
\]

have exactly three shortest paths; no radius-two `A_3` endpoint has multiplicity three.

So there is a strict information ladder:

\[
\text{coordination number}
<
\text{shell size}
<
\text{shell-total geodesic count}
<
\text{geodesic multiplicity spectrum}.
\]

At radius three even the shell totals separate:

\[
T_{FCC}(3)=420,
\qquad
T_{HCP}(3)=384.
\]

## 11. Interpretation boundary

This result does **not** show that one close packing is physically correct, dynamically preferred, or more fundamental.

It establishes a mathematical fact relevant to P022's finite-geometry search:

> **equal local coordination and equal Boolean geodesic completeness do not imply equal finite path structure.**

If later dynamics, collision support, transport, or precision rules count alternative minimal witnesses, then the multiplicity layer is observable and the two geometries are no longer equivalent at that declared future language.

That sufficiency question belongs to A2/P023; the concrete geometry and its multiplicity spectrum belong to P022.

## 12. Executable assets

- `src/enterprise_math/p022_hcp_geometry.py`
- `tests/test_p022_hcp_geometry.py`

The tests independently compare:

- closed distance versus BFS;
- recursive shortest-path counts versus BFS path counts;
- Laurent-coefficient counts versus both;
- shell endpoint summation versus the finite-sum formula;
- finite-sum formula versus the fixed integer recurrence.
