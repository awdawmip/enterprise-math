# Free Research — PNT as a Prime-Power Odd-Simplex Zero-Energy Phase

Status: `FREE_RESEARCH_FRONTIER / EXACT_FINITE_ENERGY / ASYMPTOTIC_EQUIVALENCE_PROVED / NATIVE_ENERGY_DECAY_PROOF_OPEN / NOT_WORKING_TRUTH / NOT_FOUNDATION / EXTERNAL_NOVELTY_UNVERIFIED`
Date: `2026-09-04`
Parent: `FREE_RESEARCH_PRIME_WINDING_PAIR_SIMPLEX_VARIANCE_20260904.md`

## 1. Setup

For integers `N>=4`, put

\[
Y_N:=\lfloor\sqrt N\rfloor,
\qquad
S_N:=\{a\le Y_N:\Lambda(a)>0\},
\]

so `S_N` is the set of visible prime powers up to the square-root scale. Let

\[
u_a:=\frac{\Lambda(a)}a,
\qquad
U_N:=\sum_{a\in S_N}u_a.
\]

The already proved first-mass estimate gives

\[
\boxed{
U_N=\log Y_N+O(1)=\frac12\log N+O(1).
}
\tag{1.1}
\]

Define

\[
r(m):=\frac{\psi(m)}m-1\quad(m\ge1),
\qquad r(0):=0,
\]

and quotient maps

\[
q_a(N)=\left\lfloor\frac Na\right\rfloor.
\]

For every action label `c`, write

\[
\delta_c r(m):=r(m)+r(q_c(m)).
\]

---

## 2. Finite odd-simplex energy

Define three positive finite energies:

\[
E_1(N)
:=\sum_{a\in S_N}u_a|\delta_a r(N)|^2,
\]

\[
E_{\rm dir}(N)
:=\sum_{a,b\in S_N}u_au_b
|\delta_{ab}r(N)|^2,
\]

and

\[
E_{\rm tr}(N)
:=\sum_{a,b\in S_N}u_au_b
|\delta_b r(q_a(N))|^2.
\]

The total pair-simplex energy is

\[
\boxed{
\mathfrak E_N
:=U_NE_1(N)+E_{\rm dir}(N)+E_{\rm tr}(N).
}
\tag{2.1}
\]

Every term is a positive rational combination of finite quotient-history defects after the logarithmic prime labels have been chosen.

The universal odd-triangle inequality gives exactly

\[
\boxed{
4U_N^2|r(N)|^2
\le3\mathfrak E_N.
}
\tag{2.2}
\]

Thus

\[
\frac{\mathfrak E_N}{U_N^2}\to0
\quad\Longrightarrow\quad
r(N)\to0.
\]

---

## PZE-T01 — PNT is equivalent to zero normalized pair-simplex energy

The following are equivalent:

\[
\boxed{
\frac{\psi(N)}N\to1
}
\tag{A}
\]

and

\[
\boxed{
\frac{\mathfrak E_N}{U_N^2}\to0.
}
\tag{B}
\]

### Proof that `(B) -> (A)`

This is immediate from (2.2).

### Proof that `(A) -> (B)`

Assume `r(m)->0`. Chebyshev-scale bounds give a global constant `B` with

\[
|r(m)|\le B.
\]

We treat the three channels.

#### One-step channel

Fix `Z`. If `a<=N/Z`, then `q_a(N)>=Z-1`, so `r(q_a(N))` is uniformly small once `Z` is large. The remaining boundary actions satisfy `a>N/Z`, and their normalized mass is

\[
\frac{A(N)-A(N/Z)}{A(Y_N)}
=O_Z(1/\log N).
\]

The same argument, restricted to `a<=Y_N`, is even stronger because `q_a(N)>=Y_N`. Hence

\[
\frac{E_1(N)}{U_N}\to0.
\tag{2.3}
\]

#### Direct pair channel

Since `a,b<=Y_N`, the endpoint `q_{ab}(N)` can be small only when

\[
ab>N/Z.
\]

This implies

\[
a>Y_N/\sqrt Z
\quad\text{and}\quad
b>Y_N/\sqrt Z.
\]

The weight of this corner is at most

\[
\left(A(Y_N)-A(Y_N/\sqrt Z)\right)^2
=O_Z(1).
\]

Its normalized mass is therefore `O_Z(1/U_N^2)`. Outside the corner, `q_{ab}(N)>=Z-1`, so both terms in `delta_ab r(N)` are small. Thus

\[
\frac{E_{\rm dir}(N)}{U_N^2}\to0.
\tag{2.4}
\]

#### Transported pair channel

Uniformly for `a<=Y_N`,

\[
q_a(N)\ge Y_N,
\]

so the intermediate value `r(q_a(N))` tends uniformly to zero. The final endpoint `q_b(q_a(N))=q_{ab}(N)` is handled by the same small-corner estimate as above. Hence

\[
\frac{E_{\rm tr}(N)}{U_N^2}\to0.
\tag{2.5}
\]

Equations (2.3)--(2.5) prove `(B)`.

---

## 3. Collision-current form

The direct channel can be regrouped as

\[
E_{\rm dir}(N)
=
\sum_c
\frac{(\Lambda_{Y_N}*\Lambda_{Y_N})(c)}c
|\delta_c r(N)|^2,
\]

where

\[
\Lambda_Y(a)=\Lambda(a)\mathbf1_{a\le Y}.
\]

Thus the zero-energy criterion is carried by exactly the finite one-history, direct two-history, and transported two-history sectors selected by the positive provenance algebra.

---

## 4. Geometric interpretation

The normalized relative error `r(N)` is the field at the top vertex. Each pair of visible prime-power directions creates a filled quotient triangle

\[
N,\quad q_a(N),\quad q_{ab}(N).
\]

The PNT is equivalent to saying that, after normalization by the square of the total prime-power return mass, the complete signless energy of this finite quotient 2-complex tends to zero.

Therefore:

\[
\boxed{
\text{prime number theorem}
\iff
\text{macroscopic zero-energy phase of the prime-power quotient 2-complex}.
}
\]

This is stronger than merely saying `psi(N)/N->1`: it identifies a positive finite geometric observable whose vanishing is equivalent to that limit.

---

## 5. Relation to the completed real-smoothing proof

The preceding real-variable smoothing argument proves condition `(A)`, and therefore proves `(B)` as a corollary. That is a valid closure of the asymptotic theorem, but it does not yet explain the decay of `E_N` using only the intrinsic finite 2-complex.

The native problem is now exactly:

\[
\boxed{
\text{prove }\mathfrak E_N=o(U_N^2)
\text{ directly from finite provenance/RG identities.}
}
\]

No ambiguity remains about which quadratic quantity must decay.

---

## 6. Carré-du-champ reduction

The one-step energy decomposes as

\[
E_1(N)
=U_N|r(N)+\bar r_N|^2
+\operatorname{Var}_N(r),
\]

where `bar r_N` is the weighted mean of the quotient endpoint values. The scalar return equation controls the first term. The variance is

\[
2U_N\operatorname{Var}_N(r)
=
\sum_{a,b\in S_N}u_au_b
|r(q_a(N))-r(q_b(N))|^2.
\]

Hence a direct proof of `(B)` reduces to a positive degree-three transport estimate for this carré du champ together with the direct collision channel.

---

## 7. Current boundary

- The equivalence `(A) <-> (B)` is proved at research-note theorem strength.
- The finite local triangle and coercivity statements are Lean formalized.
- The exact weighted identities are covered by the pair-simplex Fraction checker.
- The asymptotic zero-energy direction currently uses the already completed PNT.
- A native independent proof of energy decay is open.
- No quantitative decay rate and no RH-scale estimate is claimed.

---

## 8. Next target

Construct a positive finite degree-three packet `P_3(N)` and prove

\[
\boxed{
\mathfrak E_N
\le o(1)\,U_N^2
+C\,\mathcal P_3(N),
}
\]

with a separately controlled normalized degree-three remainder. Equivalently, identify a Bakry--Émery-type curvature or exact polarization identity for the prime-power quotient semigroup whose carré du champ is the variance above.
