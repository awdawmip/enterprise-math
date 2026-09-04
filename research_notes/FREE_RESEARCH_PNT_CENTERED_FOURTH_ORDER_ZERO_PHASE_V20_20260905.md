# Free Research — PNT as the Centered Fourth-Order Stopped Zero Phase

Status: `FREE_RESEARCH_FRONTIER / ZERO-PHASE EQUIVALENCE CLOSED / FORWARD BOUNDARY-SHELL ESTIMATE / REVERSE GROWING-DEPTH FRAME / NATIVE DECAY PROOF OPEN / NOT WORKING TRUTH / NOT FOUNDATION`
Date: `2026-09-05`
Project: `Enterprise Math / 进取数论`
Parent: `FREE_RESEARCH_CENTERED_FOURTH_ORDER_TRANSPOSITION_GATE_V20_20260905.md`
Researcher-ID: `EM-FREE-PI-PRIME-20260905`

## 1. Statement

Let

\[
r(n)=\frac{\psi(n)}n-1,
\qquad r(0)=0,
\]

and let `mathfrak D_4(r;n)` be the normalized centered fourth-order pair-transposition packet from the parent note.

Assume the already established project inputs:

\[
A(x)=\sum_{q\le x}\frac{\Lambda(q)}q
=\log x+O(1),
\]

Chebyshev boundedness of `r`, and boundedness of the full signless residual

\[
G_r=(M_A+L)r.
\]

Then

\[
\boxed{
r(n)\to0
\quad\Longleftrightarrow\quad
\mathfrak D_4(r;n)\to0.
}
\tag{1.1}
\]

Equivalently,

\[
\boxed{
\psi(n)\sim n
\quad\Longleftrightarrow\quad
\text{the centered fourth-order stopped provenance packet enters a zero-energy phase.}
}
\tag{1.2}
\]

The reverse implication uses the V19/V20 growing-depth frame.  It is not a new independent proof of PNT until decay of `mathfrak D_4` is derived intrinsically.

---

## 2. Uniform finite bound

For every bounded field `f`, put

\[
B=\|f\|_\infty.
\]

For each suffix action `c`, the folded pair field is

\[
F_c(a,b)=\delta_cf(\Phi_n(a,b)).
\]

Since

\[
|F_c|\le2B,
\]

each of the three pair-transposition differences has square at most `16B^2`.  Therefore

\[
\boxed{
0\le\mathcal D_n^{(2)}(F_c)\le8B^2,
}
\tag{2.1}
\]

and hence

\[
\boxed{0\le\mathfrak D_4(f;n)\le8B^2.}
\tag{2.2}
\]

This uniform bound controls the finite initial scales in the reverse direction.

---

## 3. Boundary-shell probability

Let `a,b,c` be sampled independently from the prime-winding probability

\[
p_n(q)=u_q/A(n),
\qquad u_q=\Lambda(q)/q.
\]

Let

\[
X=\Phi_n(a,b).
\]

For fixed `Z>=2`, the bad event for the signless edge is

\[
\mathcal B_{n,Z}
:=\{0<X<Z\}
\cup
\{0<q_c(X)<Z\}.
\tag{3.1}
\]

There is a constant `C_0`, depending only on the bounded discrepancy in `A-log`, such that

\[
\boxed{
\Pr(\mathcal B_{n,Z})
\le
C_0\frac{1+\log Z}{A(n)}.
}
\tag{3.2}
\]

### Stopped first endpoint

On `ab>n`, the fold is `X=q_a(n)`.  If `0<X<Z`, then

\[
a>\frac nZ
\]

up to replacing `Z` by `Z+1` for the floor.  Hence its normalized action mass is

\[
\frac{A(n)-A(n/(Z+1))}{A(n)}
=O\!\left(\frac{1+\log Z}{A(n)}\right).
\]

### Valid pair endpoint

On `ab<=n`, the fold is `X=q_(ab)(n)`.  The condition `0<X<Z` implies

\[
\frac n{Z+1}<ab\le n.
\]

The pair mass is

\[
\mathcal C_2(n)-\mathcal C_2(n/(Z+1)).
\]

Using

\[
\mathcal C_2(x)=\frac12(\log x)^2+O(\log x),
\]

and `A(n)^2 asymp (log n)^2`, its normalized size is again

\[
O\!\left(\frac{1+\log Z}{A(n)}\right).
\]

### Suffix endpoint

Condition on `X>=Z`.  The event

\[
0<q_c(X)<Z
\]

restricts `c` to a multiplicative shell of ratio at most `Z+1`.  Its `u_c`-mass is at most

\[
\log(Z+1)+O(1).
\]

After division by `A(n)`, this gives the same bound.

---

## 4. Forward implication

Put

\[
\varepsilon_Z:=\sup_{m\ge Z}|r(m)|.
\]

On the complement of `B_(n,Z)`, both values in

\[
\delta_cr(X)=r(X)+r(q_cX)
\]

are either zero at the absorbing state or have scale at least `Z`.  Hence

\[
|\delta_cr(X)|\le2\varepsilon_Z.
\]

On the bad event, use `|delta_c r|<=2B`.  Since any pair Dirichlet form is bounded by twice the second moment,

\[
\mathcal D_n^{(2)}(F_c)
\le2\mathbb E_{a,b}|F_c(a,b)|^2.
\]

Averaging over `c` and using (3.2),

\[
\boxed{
\mathfrak D_4(r;n)
\le
8\varepsilon_Z^2
+C_1B^2\frac{1+\log Z}{A(n)}.
}
\tag{4.1}
\]

If `r(n)->0`, first let `n->infinity` for fixed `Z`, then let `Z->infinity`.  This proves

\[
\boxed{r(n)\to0\Longrightarrow\mathfrak D_4(r;n)\to0.}
\tag{4.2}
\]

---

## 5. Growing-depth endpoint escape

For the reverse implication choose an even depth

\[
k(n)\to\infty,
\qquad
k(n)=O(\log\log n),
\]

and put

\[
h(n)=k(n)-1.
\]

The positive `h`-history endpoint measure has total mass `C_h(n)`.  The mass whose final quotient endpoint is below a fixed `Z` is bounded by the terminal shell

\[
\mathcal C_h(n)-
\mathcal C_h(n/(Z+1)).
\]

The uniform growing-depth factorial law gives

\[
\frac{\mathcal C_h(n/(Z+1))}{\mathcal C_h(n)}
=
\left(
1-rac{\log(Z+1)}{\log n}
\right)^h
\exp\!\left(O\!\left(\frac{h^2}{\log n}ight)
\right).
\]

Therefore

\[
\boxed{
\Pr\{X_h<Z\}
=O\!\left(
\frac{h(1+\log Z)}{\log n}
+rac{h^2}{\log n}
\right)
\longrightarrow0.
}
\tag{5.1}
\]

Thus a growing history of length `O(log log n)` still ends above every fixed arithmetic scale with probability tending to one.

---

## 6. Reverse implication

Assume

\[
\mathfrak D_4(r;m)\to0.
\]

For every `epsilon>0`, choose `Z` such that

\[
\mathfrak D_4(r;m)\le\epsilon
\qquad(m\ge Z).
\]

By (2.2) and (5.1), the history average satisfies

\[
\operatorname{HistAvg}_{h(n)}
\bigl[\mathfrak D_4(r;\cdot)\bigr]
\le
\epsilon+8B^2\Pr\{X_h<Z\}
=\epsilon+o(1).
\]

Hence

\[
\boxed{
\operatorname{HistAvg}_{h(n)}
[\mathfrak D_4(r;\cdot)]\to0.
}
\tag{6.1}
\]

The V20 centered reverse frame gives

\[
|Dr(n)|^2/A(n)^4\to0.
\]

Finally the exact parametrix

\[
A(n)^2r(n)
=(M_A-L)G_r(n)-Dr(n)
\]

and boundedness of `G_r` imply

\[
\boxed{r(n)\to0.}
\tag{6.2}
\]

This proves the reverse implication in (1.1).

---

## 7. Meaning and boundary

The earlier pair-simplex zero-phase criterion used the full coercive terminal graph norm.  The present criterion is more dynamically adapted:

- it is centered before squaring;
- it is a pair-valued `S_3` transposition Dirichlet form;
- it is exactly the final channel produced by the growing-depth Volterra reverse frame;
- all mass, placement, parity-imbalance and rectangle errors have already been removed.

Closed:

1. uniform finite boundedness of the packet;
2. quantitative boundary-shell estimate;
3. `PNT -> fourth-order zero phase`;
4. growing-depth endpoint escape;
5. `fourth-order zero phase -> PNT` through the exact parametrix.

Open:

1. prove `mathfrak D_4(r;n)->0` from the finite relation/provenance dynamics without using PNT;
2. derive a native quantitative rate;
3. Lean formalization and CI closure;
4. any Working Truth, Foundation, or RH-scale promotion.
