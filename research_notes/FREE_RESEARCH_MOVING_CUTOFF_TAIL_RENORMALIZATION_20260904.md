# Free Research — Moving-Cutoff Tail Renormalization

Status: `FREE_RESEARCH_FRONTIER / BOUNDARY_SMALLNESS_NO_GO / MACROSCOPIC_TAIL_MASS / EXACT_HALF_SCALE_LANDING / CASCADE_ESTIMATE_OPEN / NOT_WORKING_TRUTH / NOT_FOUNDATION`
Date: `2026-09-04`
Parent: `FREE_RESEARCH_RELATION_FIELD_RETURN_LIFT_20260904.md`

## 1. Executive advance

The V10 frontier isolated moving-cutoff compatibility as the remaining obstacle.  A first natural hope would be that replacing the global square-root action cloud by the local natural cloud at each quotient vertex creates only a negligible boundary term.

That hope is false.

At the clean scale `n=Y^2`, the omitted tail has asymptotic weighted mass

\[
\boxed{
\frac12U_Y^2+O(U_Y),
}
\]

so it is macroscopic.  However, the tail has a compensating exact geometry: every omitted suffix sends the history to a scale at most `Y/2`.

Therefore the cutoff mismatch must be treated by a lower-scale renormalization cascade, not by a small-boundary estimate.

---

## 2. Setup

Let

\[
u_c=\frac{\Lambda(c)}c,
\qquad
A(X)=\sum_{c\le X}u_c,
\qquad
U_Y=A(Y).
\]

The already established first-mass estimate is

\[
\boxed{A(X)=\log X+O(1).}
\tag{2.1}
\]

For a finite field `f`, define the signless residual with cutoff `X` by

\[
\rho_X(f;m)
:=\sum_{c\le X}u_c\delta_cf(m).
\tag{2.2}
\]

Take

\[
n=Y^2,
\qquad
m_a=q_a(n)=\left\lfloor\frac{Y^2}{a}\right\rfloor,
\qquad a\le Y.
\]

Then `m_a>=Y`, so the local natural residual at `m_a` contains an action tail beyond the global cutoff `Y`.

---

## MCT-T01 — Exact residual decomposition

Let

\[
T_{a,Y}(f)
:=\sum_{Y<c\le m_a}u_c\delta_cf(m_a).
\]

Then

\[
\boxed{
\rho_Y(f;m_a)=\rho_{m_a}(f;m_a)-T_{a,Y}(f).
}
\tag{3.1}
\]

Consequently, for two first actions `a,b`,

\[
\boxed{
\rho_Y(m_a)-\rho_Y(m_b)
=ho_{m_a}(m_a)-\rho_{m_b}(m_b)
-T_{a,Y}+T_{b,Y}.
}
\tag{3.2}
\]

This is the exact forcing decomposition in the relation-field return lift.

---

## MCT-T02 — Exact lower-scale landing of every tail history

For every `c>Y`, quotient composition gives

\[
q_c(m_a)=q_{ac}(Y^2).
\]

Since

\[
ac\ge a(Y+1),
\]

we have

\[
\frac{Y^2}{ac}<\frac Ya.
\]

Therefore

\[
\boxed{
q_c(m_a)
\le\left\lfloor\frac{Y-1}{a}\right\rfloor.
}
\tag{4.1}
\]

Every nontrivial first action is a prime power and hence `a>=2`, so

\[
\boxed{
q_c(m_a)\le\left\lfloor\frac{Y-1}{2}\right\rfloor.
}
\tag{4.2}
\]

Thus all omitted suffix endpoints lie in a strict half-scale subspace.

This is stronger than ordinary triangularity: the entire moving-cutoff tail lands below one common macroscopic threshold, independently of the particular prime powers `a` and `c`.

---

## MCT-T03 — Tail mass is macroscopic

The tail mass seen from the first action `a` is

\[
V_Y(a):=A(m_a)-A(Y).
\]

Using (2.1) and

\[
m_a=Y^2/a+O(1),
\]

we obtain uniformly at the aggregate level

\[
V_Y(a)=\log(Y/a)+O(1).
\tag{5.1}
\]

Consider its action-weighted total

\[
\mathcal V(Y)
:=\sum_{a\le Y}u_aV_Y(a).
\]

From partial summation applied to (2.1),

\[
\sum_{a\le Y}u_a\log a
=\frac12(\log Y)^2+O(\log Y).
\tag{5.2}
\]

Hence

\[
\begin{aligned}
\mathcal V(Y)
&=U_Y\log Y-\sum_{a\le Y}u_a\log a+O(U_Y)\\
&=\frac12(\log Y)^2+O(\log Y).
\end{aligned}
\]

Since `U_Y=log Y+O(1)`, this is

\[
\boxed{
\mathcal V(Y)=\frac12U_Y^2+O(U_Y).
}
\tag{5.3}
\]

Therefore

\[
\boxed{
\mathcal V(Y)/U_Y^2\longrightarrow\frac12.
}
\tag{5.4}
\]

The cutoff mismatch is not `o(U_Y^2)` and cannot be discarded as a boundary remainder.

---

## MCT-N01 — Small-boundary strategy is ruled out

Any proposed proof step of the form

\[
\sum_{a\le Y}u_a
\bigl\|\rho_{m_a}-\rho_Y\bigr\|
=o(U_Y^2)
\]

based only on tail mass is impossible: the mass alone has limiting normalized size `1/2`.

Cancellation or recursive lower-scale control is indispensable.

This is a structural no-go, not a failure of constants.

---

## 6. Tail decomposition into vertex and lower endpoint

Write

\[
T_{a,Y}(f)
=V_Y(a)f(m_a)
+\sum_{Y<c\le m_a}u_cf(q_c(m_a)).
\tag{6.1}
\]

The second term is supported entirely below `Y/2` by MCT-T02.  The first term remains at the intermediate vertex but has the explicit coefficient `V_Y(a)`.

For a pair `a,b`,

\[
V_Y(a)f(m_a)-V_Y(b)f(m_b)
\]

splits into

\[
\frac{V_Y(a)+V_Y(b)}2
\bigl(f(m_a)-f(m_b)\bigr)
+
\frac{V_Y(a)-V_Y(b)}2
\bigl(f(m_a)+f(m_b)\bigr).
\tag{6.2}
\]

The first term is a positive diagonal contribution to the relation coordinate and can be moved to the coercive side of the return equation.  Only the coefficient-mismatch term and the half-scale endpoint field remain as true forcing.

This indicates the correct renormalization mechanism:

1. absorb the symmetric tail mass into a strengthened diagonal relation weight;
2. send all endpoint tails to the common half-scale region;
3. control the antisymmetric coefficient mismatch through the `S_3` standard-sector field.

---

## 7. Relation-field return equation with tail split

Substituting (3.2) into the exact relation lift gives

\[
UZ_{ab}(n)+\sum_{c\le Y}u_cZ_{ab}(q_c(n))
=u_au_b\Bigl(
\rho_{m_a}(m_a)-\rho_{m_b}(m_b)
-T_{a,Y}+T_{b,Y}
\Bigr).
\tag{7.1}
\]

After the decomposition (6.2), the average tail mass contributes additional coercivity proportional to

\[
\frac{V_Y(a)+V_Y(b)}2Z_{ab}(n).
\]

The unresolved terms are now strictly typed:

- full local residual difference;
- antisymmetric tail-mass coefficient defect;
- half-scale endpoint tail.

This is substantially narrower than the undifferentiated “moving cutoff error” of V10.

---

## 8. Exact checker

The script

- `scripts/check_free_research_moving_cutoff_tail.py`

verifies with exact integers and `Fraction`:

1. quotient composition for every tail history;
2. the sharp bound `q_c(q_a(Y^2)) <= floor((Y-1)/a)`;
3. common half-scale landing;
4. exact full/truncated residual decomposition;
5. exact pairwise tail-difference decomposition.

The asymptotic mass law uses the already proved analytic estimate `A(X)=log X+O(1)` and is not represented as a floating-point experiment.

---

## 9. Updated next theorem

The next target is a dyadic tail-cascade inequality of the form

\[
\boxed{
\mathcal E_Z(Y^2)
\le \theta\,\mathcal E_Z^{\rm local}(Y^2)
+C\,\mathcal E_Z(\le Y/2)
+\text{controlled coefficient-defect energy},
}
\]

with `theta<1` after the symmetric tail mass is absorbed.

A successful estimate would turn the macroscopic cutoff tail from an obstruction into the source of additional diagonal damping, while all unresolved endpoint information descends by a factor of at least two.
