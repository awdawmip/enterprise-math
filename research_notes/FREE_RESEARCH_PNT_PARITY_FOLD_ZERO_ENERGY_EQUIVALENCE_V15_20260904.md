# Free Research — PNT as a Parity-Folded Zero-Energy Phase

Status: `FREE_RESEARCH_FRONTIER / ASYMPTOTIC EQUIVALENCE CLOSED / POSITIVE FINITE SQUARE AND DEGREE-THREE CRITERIA / NATIVE INDEPENDENT DECAY PROOF OPEN / NOT_WORKING_TRUTH / NOT_FOUNDATION`
Date: `2026-09-04`
Project: `Enterprise Math / 进取数论`
Parent: `FREE_RESEARCH_SYMMETRIC_PARITY_FOLD_STRENGTHENING_V15_20260904.md`
Researcher-ID: `EM-FREE-PI-PRIME-20260904`

## 1. Statement

Let

\[
r(n)=\frac{\psi(n)}n-1,
\qquad
u_a=\frac{\Lambda(a)}a,
\qquad
A_N=\sum_{a\le N}u_a,
\qquad
p_N(a)=u_a/A_N.
\]

Define the symmetric parity-fold field

\[
\widetilde F_N(a,b)=
\begin{cases}
r(\lfloor N/(ab)\rfloor),&ab\le N,\\
\dfrac{r(\lfloor N/a\rfloor)+r(\lfloor N/b\rfloor)}2,&ab>N.
\end{cases}
\tag{1.1}
\]

Let

\[
\widetilde{\mathcal F}_N
:=\operatorname{Var}_{p_N\otimes p_N}(\widetilde F_N)
\tag{1.2}
\]

and let the shared-first degree-three energy be

\[
\widetilde{\mathcal G}_N
:=\mathbb E_{a,b,c\sim p_N}
|\widetilde F_N(a,b)-\widetilde F_N(a,c)|^2.
\tag{1.3}
\]

Then

\[
\boxed{
\frac{\psi(N)}N\longrightarrow1
\iff
\widetilde{\mathcal F}_N\longrightarrow0
\iff
\widetilde{\mathcal G}_N\longrightarrow0.
}
\tag{1.4}
\]

The implication from either energy to PNT is native to the parity-fold resolvent. The reverse implication uses PNT only to establish the equivalence classification; it is not used in the still-open native energy-decay direction.

---

## 2. Energy decay implies PNT

The symmetric parity-fold scalar theorem gives

\[
|r(N)|
\le
\sqrt{\widetilde{\mathcal F}_N}
+O(1/\log N).
\tag{2.1}
\]

Therefore

\[
\widetilde{\mathcal F}_N\to0
\quad\Longrightarrow\quad
r(N)\to0.
\tag{2.2}
\]

The pair-`S_3` Poincare theorem gives

\[
\widetilde{\mathcal F}_N
\le\widetilde{\mathcal G}_N,
\tag{2.3}
\]

so

\[
\widetilde{\mathcal G}_N\to0
\quad\Longrightarrow\quad
r(N)\to0.
\tag{2.4}
\]

---

## 3. Small-endpoint mass

Assume PNT, so `r(n)->0`; Chebyshev already gives a global bound

\[
|r(n)|\le B.
\tag{3.1}
\]

Fix an integer `Z>=2`. We estimate the probability that a folded endpoint is below `Z`.

### Stopped-tail part

A stopped endpoint `q_a(N)` is below `Z` only if

\[
a>N/Z.
\]

Hence its probability is at most

\[
\boxed{
\frac{A_N-A_{\lfloor N/Z\rfloor}}{A_N}
=O_Z(1/\log N).
}
\tag{3.2}
\]

### Valid two-step part

A valid endpoint `q_{ab}(N)` is below `Z` only if

\[
ab>N/Z.
\]

Let

\[
C_2(X)=\sum_{ab\le X}u_au_b.
\]

The bad valid-pair mass is bounded, up to the harmless integer endpoint adjustment, by

\[
C_2(N)-C_2(N/Z).
\]

Using

\[
C_2(X)=\frac12\log^2X+O(\log X),
\]

we obtain

\[
\boxed{
\frac{C_2(N)-C_2(N/Z)}{A_N^2}
=O_Z(1/\log N).
}
\tag{3.3}
\]

Thus the total probability that any endpoint used by the symmetric fold lies below `Z` tends to zero:

\[
\boxed{
\Pr\{\text{folded endpoint}<Z\}
=O_Z(1/\log N).
}
\tag{3.4}
\]

For the stopped average `(r(q_a)+r(q_b))/2`, it is enough that both one-step endpoints exceed `Z`; the union bound contributes only another fixed factor.

---

## 4. PNT implies folded-square zero energy

Given `epsilon>0`, choose `Z` such that

\[
|r(m)|\le\epsilon
\qquad(m\ge Z).
\]

On the good folded histories, every value entering `widetilde F_N` has magnitude at most `epsilon`. On the bad histories its magnitude is at most `B`.

Using zero as a trial variance center,

\[
\widetilde{\mathcal F}_N
\le
\mathbb E|\widetilde F_N|^2
\le
\epsilon^2+B^2\Pr\{\text{bad endpoint}\}.
\]

By (3.4),

\[
\limsup_{N\to\infty}\widetilde{\mathcal F}_N
\le\epsilon^2.
\]

Letting `epsilon` tend to zero gives

\[
\boxed{
r(N)\to0
\quad\Longrightarrow\quad
\widetilde{\mathcal F}_N\to0.
}
\tag{4.1}
\]

Together with Section 2, this proves the first equivalence in (1.4).

---

## 5. PNT implies degree-three zero energy

Each integrand in `widetilde G_N` is a squared difference of two folded values. If all endpoints involved are at least `Z`, its value is at most

\[
(2\epsilon)^2=4\epsilon^2.
\]

Otherwise it is at most `4B^2`. The union of bad endpoint events still has probability `O_Z(1/log N)`.

Hence

\[
\limsup_{N\to\infty}\widetilde{\mathcal G}_N
\le4\epsilon^2,
\]

and therefore

\[
\boxed{
r(N)\to0
\quad\Longrightarrow\quad
\widetilde{\mathcal G}_N\to0.
}
\tag{5.1}
\]

Combining this with (2.4) proves the second equivalence in (1.4).

---

## 6. Geometric meaning

The criterion is carried by a finite stopped two-history square and its canonical three-history Dirichlet lift.

- `ab<=N`: two prime-winding directions complete a valid quotient history;
- `ab>N`: the second winding crosses the available scale and is folded back to the retained one-step boundary;
- the parity sign records collision versus stopped boundary;
- symmetric projection removes orientation information invisible to the scalar parity observable;
- the degree-three energy measures sensitivity under replacing one history slot while retaining the other.

Thus

\[
\boxed{
\text{PNT}
\iff
\text{macroscopic zero-energy phase of the parity-folded prime-winding square}
\iff
\text{zero transposition energy of its shared-first }S_3\text{ lift}.
}
\tag{6.1}
\]

This criterion differs from the earlier square-root-cutoff odd-simplex energy, although both are positive finite PNT-equivalent observables. The parity fold is tailored to the exact full adaptive residual and supplies the missing scalar output map.

---

## 7. Quantitative two-way form

Let

\[
R(Z):=\sup_{m\ge Z}|r(m)|.
\]

The preceding proof gives, for fixed `Z`,

\[
\boxed{
\widetilde{\mathcal F}_N
\le
R(Z)^2
+B^2 O_Z(1/\log N),
}
\tag{7.1}
\]

and

\[
\boxed{
\widetilde{\mathcal G}_N
\le
4R(Z)^2
+4B^2 O_Z(1/\log N).
}
\tag{7.2}
\]

In the opposite direction,

\[
\boxed{
|r(N)|
\le
\sqrt{\widetilde{\mathcal F}_N}
+O(1/\log N)
\le
\sqrt{\widetilde{\mathcal G}_N}
+O(1/\log N).
}
\tag{7.3}
\]

Equation (7.3) is the direction required for a new proof. Equations (7.1)--(7.2) certify that no extraneous asymptotic condition has been introduced.

---

## 8. Boundary

Closed:

1. PNT equivalence with the symmetric folded-square variance;
2. PNT equivalence with the shared-first degree-three transposition energy;
3. finite small-endpoint mass estimate from the first- and second-history mass laws;
4. quantitative comparison in both directions.

Open:

1. prove `widetilde G_N->0` directly from the finite V14/V15 return system rather than from PNT;
2. establish the profile-valued block recurrence and its critical exponent;
3. obtain a native quantitative remainder.

The equivalence theorem establishes that the new finite energy is neither too weak nor artificially too strong. It is exactly another geometric form of the prime number theorem.
