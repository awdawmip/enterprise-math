# P022 — A Local Transfer Formula for Composite Franel Defects

Status: `ACTIVE RESEARCH NOTE / EXACT LOCAL DEFECT RECURRENCE / PRIOR-ART SENSITIVE`  
Owner: `program/p022-geometry-v2`  
Depends on: central-binomial elimination / pure Franel-defect reduction  
Cross-route relevance: P011 structured collision identifiability; P018 defect language; P023/P024 task-relative observation sufficiency

## 1. From a global defect lattice to a local formula

The central-binomial elimination theorem reduces low-order Barlow collision identifiability to multiplicative independence of

\[
2
\quad\text{and}\quad
D_n
\]

for indices with composite

\[
2n-1.
\]

That identifies the correct global objects, but a raw rational `D_n` still looks nonlocal because it is defined by an exponent vector involving several earlier Franel numbers.

This note introduces a multiplicative transfer `Psi` that makes each defect recursively local in the factorization trees of `n` and `2n-1`.

---

## 2. The central-binomial integer basis

The preceding theorem constructs a canonical multiplicative expression of every positive integer `m` in the generators

\[
A_j=\binom{2j}{j}.
\]

Write

\[
\boxed{
m=\prod_jA_j^{e_j(m)}.}
\]

The exponent vector is obtained recursively from

\[
2=A_1
\]

and, for every odd prime

\[
q=2j-1,
\]

\[
\boxed{
q=\frac j2\frac{A_j}{A_{j-1}}.
}
\]

The recursion terminates because `j<q`.

---

## 3. P022-TD01 — Franel transfer

Substitute

\[
F_j=\sum_{k=0}^j\binom jk^3
\]

for every `A_j` in the canonical integer basis and define

\[
\boxed{
\Psi(m)=\prod_jF_j^{e_j(m)}
\in\mathbb Q_{>0}.}
\]

Because the integer exponent representation is additive under multiplication,

\[
\boxed{
\Psi(ab)=\Psi(a)\Psi(b).}
\]

Thus `Psi` is a multiplicative rational transfer determined by the Franel sequence and the central-binomial prime recursion.

It is **not** asserted to be a standard arithmetic function or a homomorphism naturally attached to Franel numbers outside this construction.

---

## 4. P022-TD02 — odd-prime transfer recursion

Let

\[
q=2j-1
\]

be an odd prime.

Replacing `A` by `F` in

\[
q=\frac j2\frac{A_j}{A_{j-1}}
\]

gives the exact transfer recursion

\[
\boxed{
\Psi(q)
=
\frac{\Psi(j)}2
\frac{F_j}{F_{j-1}}.
}
\]

For a valuation prime `p`, define

\[
\psi_p(m)=v_p(\Psi(m)),
\qquad
f_p(j)=v_p(F_j).
\]

Then `psi_p` is completely additive and

\[
\boxed{
\psi_p(q)
=
\psi_p(j)
-\mathbf1_{p=2}
+f_p(j)-f_p(j-1).
}
\]

So every valuation of `Psi(m)` can be computed recursively from:

1. the prime factorization of `m`;
2. smaller half-prime arguments `(q+1)/2`;
3. local differences of Franel valuations.

No joint `(A,F)` determinant enters this recursion.

---

## 5. P022-TD03 — one unified boundary defect

For every

\[
n\ge2,
\]

define

\[
\boxed{
\Delta_n
=
\frac{F_n\Psi(n)}
{2F_{n-1}\Psi(2n-1)}.
}
\]

This single formula unifies the prime and composite cases.

### Prime odd boundary

If

\[
2n-1
\]

is prime, TD02 with `j=n` gives

\[
\Psi(2n-1)
=
\frac{\Psi(n)}2
\frac{F_n}{F_{n-1}}.
\]

Substitution gives

\[
\boxed{\Delta_n=1.}
\]

So the Franel transfer has **no defect** at a prime boundary.  This matches the structural fact that the corresponding segment already acquires a genuinely new `A`-prime pivot.

### Composite odd boundary

If

\[
2n-1
\]

is composite, the central-binomial relation expresses `A_n` entirely using earlier `A_j`.  Substituting `F_j` into that relation gives exactly the pure defect `D_n`.

Hence

\[
\boxed{
\Delta_n=D_n
\qquad(2n-1\text{ composite}).}
\]

Thus the entire hard part of the low-order identifiability problem is the nontrivial portion of one unified defect sequence `Delta_n`.

---

## 6. P022-TD04 — local valuation formula

For every valuation prime `p`,

\[
\boxed{
\begin{aligned}
d_p(n)
:=v_p(\Delta_n)
={}&f_p(n)-f_p(n-1)\\
&+\psi_p(n)
-\mathbf1_{p=2}
-\psi_p(2n-1).
\end{aligned}}
\]

If

\[
2n-1=\prod_iq_i^{a_i},
\]

then complete additivity gives

\[
\psi_p(2n-1)
=
\sum_i a_i\psi_p(q_i),
\]

and every `psi_p(q_i)` recursively descends through

\[
(q_i+1)/2<q_i.
\]

Therefore a composite defect coordinate depends only on:

- the local Franel valuation increment `f_p(n)-f_p(n-1)`;
- the factor tree of `n`;
- the prime-factor tree of the composite boundary `2n-1`;
- smaller Franel valuation increments encountered on those trees.

This is the requested local arithmetic description of a composite certificate column.

---

## 7. Example: `n=67`

Here

\[
2n-1=133=7\cdot19.
\]

So for every prime `p`,

\[
\boxed{
\begin{aligned}
d_p(67)
={}&f_p(67)-f_p(66)+\psi_p(67)\\
&-\mathbf1_{p=2}-\psi_p(7)-\psi_p(19).
\end{aligned}}
\]

For the historical certificate row

\[
p=337,
\]

all terms in this local expression vanish, and therefore

\[
\boxed{d_{337}(67)=0.}
\]

This is important: the successful `337` row at the 66→67 extension is **not a local valuation of the new defect**.

Its role is global.  The old selected rows produce one candidate dependence of `D_67` on earlier defects; `v_337` rejects that candidate because it sees an incompatible combination of earlier defect columns.

So there are two distinct mechanisms:

1. **local defect support** — `d_p(n) != 0` directly measures the new composite defect;
2. **global dependency detection** — a row may have `d_p(n)=0` and still disprove that `D_n` lies in the old defect span.

The raw determinant had obscured this distinction.

---

## 8. Prime-boundary versus composite-boundary logic

The combined structural picture is now:

### If `2n-1` is prime

\[
\boxed{
A_n\text{ creates a new prime direction},
\qquad
\Delta_n=1.
}
\]

No Franel defect needs to carry the extension.

### If `2n-1` is composite

\[
\boxed{
A_n\text{ creates no new direction},
\qquad
\Delta_n=D_n.
}
\]

The extension succeeds exactly when this new defect escapes the multiplicative subgroup of the earlier defects.

Thus the old empirical observation that composite boundaries require `F3`-side pivots is now a theorem-level consequence of the central-binomial recurrence.

---

## 9. A sufficient primitive-defect criterion

Let the composite indices in increasing order be

\[
n_1<n_2<\cdots.
\]

A strong sufficient condition for global defect independence would be:

> for each `n_r`, there exists a prime `p_r` such that
> \[
> v_{p_r}(D_{n_r})\ne0
> \]
> but
> \[
> v_{p_r}(2)=0,
> \qquad
> v_{p_r}(D_{n_s})=0\quad(s<r).
> \]

Then the defect valuation matrix is triangular after selecting those rows.

A primitive prime divisor of `F_(n_r)` that divides no earlier Franel number would be one way—though not the only way—to obtain such a row, because the denominator of `D_(n_r)` contains only earlier `F_j`.

However the `n=67` certificate shows that **fresh local support is not necessary** for a finite independence proof: old-prime global dependency detectors can also close the rank.

No theorem asserting primitive divisors for all Franel numbers is claimed here.

---

## 10. Global frontier after the transfer reduction

The infinite low-order identifiability question can now be stated without central-binomial clutter:

\[
\boxed{
\text{Are }
2,D_n
\text{ multiplicatively independent over all composite odd-boundary indices?}
}
\]

TD04 says each valuation vector is generated recursively by smaller Franel valuation data and the factor trees of `n` and `2n-1`.

This suggests three concrete attack routes:

1. prove a primitive-defect valuation theorem;
2. exploit the Franel recurrence/congruence theory to control `d_p(n)` on carefully chosen primes;
3. find an exact multiplicative relation among the `D_n`, which would produce a genuine global alias for `(J1,J2,J3)` and close the conjectured route negatively.

All three are structurally sharper than extending the determinant cutoff again.

---

## 11. Prior-art boundary

Franel numbers, their three-term recurrence, congruences, `p`-adic valuations, central binomial coefficients and prime factorization are established mathematics.

The current external literature search located substantial congruence theory for Franel numbers, including work of Zhi-Wei Sun and later authors, but did not locate a general primitive-divisor or multiplicative-independence theorem for the defect sequence defined here.  Absence from this search is **not** a novelty proof.

The P022-specific result is the transfer construction `Psi`, the unified `Delta_n`, and the exact reduction of composite certificate coordinates to the local valuation recursion TD04.

Historical novelty remains `NOVELTY_UNVERIFIED`.

---

## 12. Executable assets

Added:

- `src/enterprise_math/p022_barlow_franel_transfer_defect.py`;
- `tests/test_p022_barlow_franel_transfer_defect.py`.

The tests verify:

- multiplicativity of `Psi` on finite integer products;
- `Delta_n=1` for every prime odd boundary through segment 150;
- `Delta_n=D_n` on composite samples;
- the exact valuation formula against explicit rational defects;
- the odd-prime transfer recursion;
- agreement with the A-elimination defect coordinates;
- the `n=67,p=337` zero local defect that separates local support from global dependency detection.
