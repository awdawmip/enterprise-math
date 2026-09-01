# R005-B — Gafni–Tao Full-Table Audit of the Cubic Knife-Edge Threshold

Status: `EXTERNAL-THEOREM TRANSFER AUDIT / PROVED ALGEBRAIC CHECK / NOT CANONICAL`  
Date: `2026-08-10`  
Program: `R005 — Enterprise Prime Toolkit`  
Track: `B — Prime–Collapse Field Geometry`  
Depends on: Supplement 11  
External source: A. Gafni and T. Tao, *On the number of exceptional intervals to the prime number theorem in short intervals*, Essential Number Theory 5 (2026), 221–241.

## 1. Question audited

Supplement 11 obtained the current quantitative cubic knife-edge threshold

\[
\boxed{\theta_*=31/107}
\]

by using the zero-density branch of Gafni–Tao's exceptional-set machinery.

Their actual Theorem 1.3 is stronger: it takes the minimum of an L^2/zero-density
bound and an L^4/additive-energy bound.  The obvious concern was therefore:

> is 31/107 merely an artifact of ignoring the additive-energy branch?

This supplement checks the complete current Table-1 / Table-2 machinery at the
R005 transfer boundary.

Result:

\[
\boxed{
\text{No.  The refined additive-energy branch is inactive at the R005 critical
optimizer, and the same }31/107\text{ threshold survives.}
}
\]

This is a statement about the **current published Gafni–Tao tables and this
specific R005 transfer inequality**, not a claim that 31/107 is an intrinsic or
optimal number-theoretic constant.

---

## 2. External theorem used

Gafni–Tao define the exceptional-set exponent `mu(theta)` and prove

\[
|\mathcal E_\theta\cap[X,2X]|
\ll X^{\mu(\theta)+o(1)}.
\]

Their Theorem 1.3 gives

\[
\mu(\theta)
\le
\inf_{\varepsilon>0}
\sup_{A(\sigma)\ge 1/(1-\theta)-\varepsilon}
\min\{\mu_{2,\sigma}(\theta),\mu_{4,\sigma}(\theta)\},
\]

where

\[
\mu_{2,\sigma}(\theta)
=(1-\theta)(1-\sigma)A(\sigma)+2\sigma-1,
\]

and

\[
\mu_{4,\sigma}(\theta)
=(1-\theta)(1-\sigma)A^*(\sigma)+4\sigma-3.
\]

Table 1 supplies the current piecewise upper bounds for `A(sigma)`; Table 2
supplies those for the additive-energy exponent `A*(sigma)`.

---

## 3. R005 transfer inequality

For a second-order supercritical cubic gap

\[
g=3a^{1/3}+a^\theta,
\]

Supplement 11 showed:

- the activated k-lifetime is of order `a^(theta+1/3)`;
- each reciprocal q-window has width of order `a^theta`;
- exceptional q-starts have total measure `a^(mu(theta)+o(1))`.

The bounded-overlap amplification wins whenever

\[
\boxed{
\mu(\theta)<2\theta+\frac13.
}
\]

So the exact audit question is where the best published Gafni–Tao upper bound
first drops below the line

\[
2\theta+\frac13.
\]

---

## 4. Active Table-1 branch

At the transition found in Supplement 11, the relevant Table-1 zero-density
majorant is

\[
\boxed{
A(\sigma)\le\frac{11}{48\sigma-36}
}
\]

on the Tao–Trudgian–Yang branch immediately above `sigma=31/34`.

At the admissibility boundary

\[
A(\sigma)=\frac{1}{1-\theta},
\]

this gives

\[
\boxed{
\sigma(\theta)=\frac{47-11\theta}{48}.
}
\]

At such a boundary point the L^2 expression simplifies:

\[
\begin{aligned}
\mu_{2,\sigma}(\theta)
&=(1-\theta)(1-\sigma)\frac{1}{1-\theta}+2\sigma-1\\
&=\sigma.
\end{aligned}
\]

Thus the zero-density transfer crosses the R005 target when

\[
\frac{47-11\theta}{48}
=2\theta+\frac13.
\]

Solving gives

\[
\boxed{
\theta_*=\frac{31}{107}=0.289719626\ldots
}
\]

and

\[
\boxed{
\sigma_*
=\frac{47-11\theta_*}{48}
=\frac{293}{321}.
}
\]

At the same point

\[
\boxed{
2\theta_*+\frac13
=\frac{293}{321}
=\sigma_*.
}
\]

---

## 5. Full additive-energy check at the critical optimizer

Because

\[
\sigma_*=rac{293}{321}>\frac56,
\]

Table 2 uses the Heath-Brown branch

\[
\boxed{
A^*(\sigma)\le\frac{12}{4\sigma-1}.
}
\]

At `sigma_*` this is exactly

\[
\boxed{
A^*(\sigma_*)
=\frac{3852}{851}.
}
\]

Substituting `theta_*=31/107` and `sigma_*=293/321` into the L^4 expression gives

\[
\boxed{
\mu_{4,\sigma_*}(\theta_*)
=\frac{254467}{273171}.
}
\]

The L^2 branch is

\[
\boxed{
\mu_{2,\sigma_*}(\theta_*)
=\frac{293}{321}.
}
\]

Their exact difference is

\[
\boxed{
\mu_4-\mu_2
=\frac{1708}{91057}>0.
}
\]

Therefore

\[
\boxed{
\min(\mu_2,\mu_4)=\mu_2
}
\]

at the R005 critical optimizer, with an explicit positive additive-energy
margin.

So the L^4 refinement does **not** move the crossing left of 31/107 at the point
where the zero-density branch first reaches the required amplification line.

---

## 6. Full piecewise table audit

A finite branch audit was then performed over the relevant Table-1 and Table-2
pieces in Theorem 1.3's admissible sigma range.

The audit checks the piecewise rational formulas and their transition endpoints,
using exact rational arithmetic wherever the endpoints are rational and a dense
numerical cross-check across the complete relevant sigma interval.

The first crossing of the R005 target

\[
\mu(\theta)<2\theta+1/3
\]

remains at the same boundary:

\[
\boxed{
\theta>31/107.
}
\]

No earlier Table-2/additive-energy branch undercuts the active L^2 branch enough
to improve the R005 transfer threshold.

This is consistent with Gafni–Tao's own observation that the explicit evaluation
of their full Theorem 1.3 is naturally computer-assisted and piecewise.

---

## 7. What 31/107 now means

After the full-table audit, the correct interpretation is sharper:

\[
\boxed{
31/107
\text{ is the current complete Gafni–Tao Table-1/Table-2 transfer threshold
for this R005 cubic amplification argument.}
}
\]

It is **not**:

- a conjectured optimal exponent for prime gaps;
- a Foundation constant;
- a proof that better analytic number theory cannot improve the shell;
- a claim that Gafni–Tao optimized specifically for the R005 problem.

Indeed Gafni–Tao explicitly note that their prime-gap exceptional-set consequence
could potentially be improved by combining their methods with Harman-type
sieves, a direction they do not pursue in that paper.

So the next analytic improvement should not waste effort merely re-running the
same current tables.  It needs genuinely stronger input: improved zero-density,
additive-energy, Harman-sieve, direct prime-gap moments, or a route exploiting
the new quotient/carry structure of Supplement 12.

---

## 8. Combined consequence with Supplement 12

The research frontier is now split cleanly.

### Mesoscopic second-order surplus

If

\[
h=g-3a^{1/3}\ge a^\beta,
\qquad
\beta>31/107,
\]

current Gafni–Tao exceptional-set technology already amplifies the gap into many
full cubic failures.

### Fixed or thinner integer surplus

If h is O(1), or more generally lies below the currently controlled analytic
shell, Supplement 12 shows that the state does **not** remain an arbitrary
short interval.  It collapses to

\[
\text{quotient jump}
+
\text{two carry corrections}
+
\text{bounded predecessor-prime lag}
\]

along

\[
m_k=\lfloor k^3/a\rfloor.
\]

This creates a new project-native attack surface that is structurally different
from improving general almost-all short-interval theorems.

---

## 9. Status boundary

External facts in this supplement are exactly the published Gafni–Tao theorem
and their current Table-1/Table-2 bounds.  The rational substitutions and the
R005 transfer inequality are internal derivations.

No claim is made that infinitely many gaps satisfying any supercritical
condition exist.  No current theorem decides finite versus infinite cubic
full-forcing failure.

Historical novelty of the R005 transfer interpretation remains unverified.
