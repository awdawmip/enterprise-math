# Free Research — Cube-to-Simplex Spacings Intertwiner

Status: `FREE_RESEARCH_FRONTIER / IDEAL PATHWISE INTERTWINER CLOSED / FACTORIAL PROVENANCE EXPLAINED / ENDPOINT PRESERVED / ARITHMETIC CAPACITY CURVATURE BOUNDED / VALUE-SENSITIVE QUANTIZATION OPEN / NOT WORKING TRUTH / NOT FOUNDATION`
Date: `2026-09-05`
Project: `Enterprise Math / 进取数论`
Parent: `FREE_RESEARCH_STOPPED_BETA_BLOCK_VARIANCE_V18_20260905.md`
Researcher-ID: `EM-FREE-PI-PRIME-20260904`

## 1. Executive advance

The ideal identity

\[
(U^df)(1)=d!(J^df)(1)
\]

is not merely equality of two endpoint densities. It has an explicit pathwise, endpoint-preserving, measure-preserving intertwiner.

The stopped process driven by `d` independent uniform action coordinates is the running minimum of `d` independent uniform endpoint proposals. Sorting those proposals and taking their spacings produces a fully valid `d`-step simplex history with exactly the same terminal endpoint.

Each of the `d!` ordering chambers of the cube maps with Jacobian one to the valid simplex. Thus

\[
\boxed{
\text{stopped cube histories}
\longleftrightarrow
S_d\text{-labelled valid simplex histories},
}
\]

and the factorial coefficient is literal provenance multiplicity.

For `d=3` this recovers the six histories underlying the original `3!` factor. For the V18 block, `d=4` gives the exact `24` in `L_4=U^4-24J^4`.

---

## 2. Ideal stopped kernel as a running minimum

On `[0,1]`, let

\[
(Uf)(t)=(1-t)f(t)+\int_0^tf(u)\,du.
\tag{2.1}
\]

Let `Y` be uniform on `[0,1]`. Then

\[
\min(t,Y)
\]

has an atom of mass `1-t` at `t` and Lebesgue density one on `[0,t]`. Therefore

\[
\boxed{(Uf)(t)=\mathbb E f(\min(t,Y)).}
\tag{2.2}
\]

Starting from `t_0=1` and using independent uniforms `Y_1,...,Y_d`,

\[
\boxed{t_d=\min(Y_1,\ldots,Y_d).}
\tag{2.3}
\]

Hence `t_d` has density

\[
\boxed{d(1-t)^{d-1}\,dt.}
\tag{2.4}
\]

---

## CSI-T01 — Sorting and spacing map

Outside the measure-zero diagonals, let `sigma in S_d` be the unique permutation such that

\[
0<Y_{\sigma(1)}<\cdots<Y_{\sigma(d)}<1.
\]

Put

\[
t:=Y_{\sigma(1)}
\]

and define `d` nonnegative spacings

\[
\begin{aligned}
x_1&:=1-Y_{\sigma(d)},\\
x_2&:=Y_{\sigma(d)}-Y_{\sigma(d-1)},\\
&\ \vdots\\
x_d&:=Y_{\sigma(2)}-Y_{\sigma(1)}.
\end{aligned}
\tag{3.1}
\]

Then

\[
\boxed{x_1+\cdots+x_d=1-t.}
\tag{3.2}
\]

Thus `(x_1,...,x_d)` is a valid additive history in the simplex

\[
\Delta_d=
\{x_i\ge0:x_1+\cdots+x_d\le1\},
\]

and its terminal residual coordinate is

\[
1-\sum_ix_i=t.
\]

The map from one ordering chamber to `Delta_d` is triangular linear with absolute Jacobian one. It is invertible after the permutation label `sigma` is retained.

Consequently, Lebesgue measure on the cube pushes forward to

\[
\boxed{d!\,dx_1\cdots dx_d}
\tag{3.3}
\]

on the valid simplex, and the endpoint is preserved pointwise.

---

## CSI-T02 — Exact operator identity from the path map

The `d`-fold Volterra operator satisfies

\[
(J^df)(1)
=
\int_{\Delta_d}
 f\!\left(1-\sum_ix_i\right)
 dx_1\cdots dx_d.
\]

The sorting-spacings map gives

\[
\begin{aligned}
(U^df)(1)
&=\int_{[0,1]^d}f(\min_iY_i)dY\\
&=d!\int_{\Delta_d}
 f\!\left(1-\sum_ix_i\right)dx\\
&=d!(J^df)(1).
\end{aligned}
\]

Therefore the ideal stopped/Beta identity is a direct finite change of variables, not merely an induction from commutators.

---

## 4. Record minima and Stirling chambers

The stopped path retains an action exactly when a new record minimum appears. Partitioning cube histories by the set partition induced by equal record blocks reproduces the Stirling image-size hierarchy.

At depth three, the record/provenance partition yields

\[
3^3=6+18+3,
\]

with the six full-order histories corresponding to the six sorting chambers.

At arbitrary depth, the factorial simplex sector is the full-order stratum, while repeated/rejected record blocks form the lower-image Stirling chambers.

Thus the previously separate structures

- factorial provenance;
- stopped histories;
- Stirling cutoff chambers;
- Beta endpoint profiles;

are four views of one sorting-spacings geometry.

---

## 5. Arithmetic prime-mass coordinate

Let

\[
A(x)=\sum_{q\le x}\frac{\Lambda(q)}q,
\qquad
|A(x)-\log x|\le C,
\]

and fix top cutoff `N` with `A=A(N)>0`. Define the normalized capacity coordinate

\[
\boxed{c_N(n):=A(n)/A.}
\tag{5.1}
\]

For `a<=n` and

\[
m=q_a(n)=\lfloor n/a\rfloor\ge1,
\]

write `n=am+r`, `0<=r<a`. Then

\[
0\le\log(n/a)-\log m
<\log(1+1/m)\le\log2.
\]

Therefore

\[
\boxed{
|A(m)-A(n)+A(a)|
\le3C+\log2.
}
\tag{5.2}
\]

After normalization,

\[
\boxed{
|c_N(q_a(n))-c_N(n)+c_N(a)|
\le
\frac{3C+\log2}{A(N)}.
}
\tag{5.3}
\]

Thus quotient transport is uniformly approximately additive in the prime-mass coordinate.

---

## CSI-T03 — Fixed valid-history endpoint curvature

For a valid ordered history

\[
a_1\cdots a_d\le N
\]

and endpoint

\[
m=q_{a_1\cdots a_d}(N),
\]

the same calculation gives

\[
\boxed{
\left|
 c_N(m)-1+\sum_{j=1}^dc_N(a_j)
\right|
\le
rac{(d+2)C+\log2}{A(N)}.
}
\tag{6.1}
\]

For every fixed depth, the fully valid arithmetic simplex therefore lies within `O_d(1/log N)` of the ideal additive simplex in capacity coordinate.

---

## 7. Atomic mesh

The normalized action atom at a prime power `q=p^k` has mass

\[
p_N(q)=\frac{\log p}{p^kA(N)}.
\]

Since `log x/x<=1/e` for positive real `x`,

\[
\boxed{
\max_qp_N(q)
\le\frac1{eA(N)}
=O(1/\log N).
}
\tag{7.1}
\]

Hence the cumulative prime-mass coordinate has mesh `O(1/log N)`.

Combining (5.3), (6.1), and (7.1), the sorting-spacings cube/simplex map can be discretized at every fixed depth with endpoint-capacity transport error `O_d(1/log N)` in expectation. Large pathwise errors occur only when a sampled action falls inside an `O(1/log N)` neighborhood of a validity boundary.

This recovers and geometrically explains the fixed-depth Wasserstein/Gamma estimates from V16.

---

## 8. Why this does not yet close arbitrary value transport

Capacity-coordinate closeness does not imply

\[
|r(m)-r(m')|\ll1
\]

for an arbitrary bounded arithmetic field. A point mass can oscillate across adjacent capacity atoms.

Therefore Wasserstein closeness of endpoints cannot be inserted directly into the one-variance scalar readout. The remaining theorem must control the value-sensitive transport cost

\[
\mathbb E|r(M_{\rm stop})-r(M_{\rm simplex})|^2.
\]

Valid routes are:

1. dominate this cost by the complete retained relation energy on the common four-action lift;
2. prove a native capacity-coordinate regularity estimate for the actual prime error;
3. add a finite adjacent-capacity Dirichlet channel and prove it is absorbed by the multichannel return state.

The first route is preferred because no external smoothness assumption is then needed.

---

## 9. Exact common-lift target

Let `Gamma_(N,4)` be the sorting-spacings coupling between the stopped cube and factorial simplex after atomic refinement. The next target is

\[
\boxed{
\int|r(x)-r(y)|^2d\Gamma_{N,4}(x,y)
\le
C\,\mathcal E_{\rm retained}^{(4)}(N)
+O((\log N)^{-\gamma})
}
\]

with a coefficient compatible with the depth-four margin.

Because the coupling retains the sorting permutation, the six defect edges and all intermediate vertices are available before recoalescence. This is exactly the state required by the `S_4` Gram theorem.

---

## 10. Classification

Closed exactly:

1. stopped kernel as running minimum;
2. sorting-spacings map on every permutation chamber;
3. Jacobian-one endpoint-preserving cube/simplex intertwiner;
4. pathwise origin of the factorial coefficient;
5. unification with record-minimum/Stirling chambers;
6. uniform one-step arithmetic capacity-curvature bound;
7. fixed valid-history capacity-curvature bound;
8. `O(1/log N)` atomic mesh.

Open:

1. value-sensitive arithmetic coupling estimate;
2. exact chamberwise relation-energy domination;
3. integration with the `S_4` Gram block;
4. native logarithmic prime remainder.
