# P022 — Structural Localization of the Half-Defect A-Support

Status: `ACTIVE RESEARCH NOTE / EXACT SUPPORT BOUND`  
Owner: `program/p022-geometry-v2`  
Depends on: canonical central-binomial prime-basis expansion; half-index composite-boundary family  
Cross-route relevance: P018 cancellation; P023 quotient-stable witness sufficiency

## 1. Why localization matters

For the target infinite half-index family

\[
p>5,\qquad p\equiv5\text{ or }23\pmod{24},
\qquad m=\frac{p-1}{2},
\]

we know

\[
p\mid F_m
\]

and

\[
2m-1=p-2
\]

is composite.

The pure defect can erase this witness only if the canonical central-binomial elimination of `A_m` uses an older Franel index which is also zero modulo `p`.

The universal midpoint companion converts that into an offset-prime problem.  This note supplies a complementary structural fact: the canonical A-support itself is strongly localized.

---

## 2. Integer prime-basis support bound

Recall the exact central-binomial recurrence

\[
\frac{A_n}{A_{n-1}}
=\frac{2(2n-1)}{n},
\qquad
A_n=\binom{2n}{n}.
\]

For an odd prime `q`, the canonical recursive representation is generated at

\[
h=\frac{q+1}{2}
\]

through

\[
q=\frac{h}{2}\frac{A_h}{A_{h-1}}.
\]

The only new A-indices are `h,h-1`, plus those recursively needed to represent `h`.

Let `P(v)` denote the largest prime factor of a positive integer `v>1`.  Induction over the prime-factor tree gives:

\[
\boxed{
\max\operatorname{supp}_A(v)
\le
\frac{P(v)+1}{2}.}
\]

For `v=1`, the support is empty.

This is an exact property of the canonical basis used by P022, not an asymptotic estimate.

---

## 3. Canonical half-index elimination

At a composite midpoint boundary,

\[
A_m
=A_{m-1}\frac{2(p-2)}{m}.
\]

Therefore the support of the canonical A-relation is contained in

\[
\{m-1,1\}
\cup
\operatorname{supp}_A(p-2)
\cup
\operatorname{supp}_A(m).
\]

The explicit term `m-1` is the only support index intrinsically adjacent to the midpoint.

The other indices are controlled by largest-prime-factor bounds.

---

## 4. P022-LI32 — `p=5 mod 24`: all nonadjacent support lies in the left third

Suppose

\[
p\equiv5\pmod{24}.
\]

Then

\[
m=\frac{p-1}{2}
\]

is even and exceeds two. Hence

\[
P(m)\le\frac m2.
\]

Also

\[
p-2=2m-1
\]

is an odd composite multiple of three. Therefore

\[
P(p-2)\le\frac{p-2}{3}=rac{2m-1}{3}.
\]

Applying the prime-basis support bound gives

\[
\max\operatorname{supp}_A(m)
\le\frac{m+2}{4},
\]

and

\[
\max\operatorname{supp}_A(p-2)
\le
\left\lfloor\frac{m+1}{3}\right\rfloor.
\]

The second bound dominates. Thus every canonical support index other than the explicit `m-1` satisfies

\[
\boxed{
j\le\left\lfloor\frac{m+1}{3}\right\rfloor.}
\]

---

## 5. P022-LI33 — `p=23 mod 24`: all nonadjacent support lies in the left half

Suppose

\[
p\equiv23\pmod{24}.
\]

Here `m` is odd and can itself be prime, so the universal bound is only

\[
P(m)\le m.
\]

Hence

\[
\max\operatorname{supp}_A(m)
\le\frac{m+1}{2}.
\]

The same factor-three argument for `p-2` gives a strictly smaller bound. Therefore every support index other than `m-1` satisfies

\[
\boxed{j\le\frac{m+1}{2}.}
\]

---

## 6. Offset form: a large automatic-safe zone

Write companion offsets as

\[
d=m-j.
\]

The explicit support index `m-1` corresponds to `d=1`.  Every other support index satisfies `j<=B`, where

\[
B=
\begin{cases}
\lfloor(m+1)/3\rfloor,&p\equiv5\pmod{24},\\
(m+1)/2,&p\equiv23\pmod{24}.
\end{cases}
\]

Thus every nontrivial support offset satisfies

\[
\boxed{d\ge m-B.}
\]

Consequently any companion zero at

\[
2\le d<m-B
\]

is **automatically safe** from canonical defect cancellation.

This gives a large support-free neighborhood around the midpoint:

- roughly the first `2m/3` offset range is safe in the `5 mod 24` family;
- roughly the first `m/2` offset range is safe in the `23 mod 24` family.

The precise endpoints are the integer formulas above.

---

## 7. What remains open

Localization does not prove full support avoidance.

Far companion zeros can still land on the recursively generated left support.  The `p=157` cancellation counterexample outside the target residue family shows that this phenomenon is real.

For the target family the remaining problem is now strictly narrower:

> **Far-offset collision problem.** Can a prime divisor of the universal companion sequence occur at an offset `d>=m-B` whose reflected index `j=m-d` lies in the canonical prime-halving support tree of `m` or `p-2`?

Finite tests have not found such a hit in the target residue family over the current pressure range, but no infinite theorem is claimed.

---

## 8. Precision consequence

A large class of locally visible Franel witnesses can now be certified quotient-stable **without inspecting their Franel values**: geometry of the canonical elimination alone excludes cancellation.

Thus support sufficiency decomposes into:

\[
\boxed{
\text{structural safe zone}
+
\text{far-offset arithmetic residue}.}
\]

This is a concrete example of separating a deterministic representation bound from the genuinely arithmetic repair frontier.

---

## 9. Executable assets

Added:

- `src/enterprise_math/p022_barlow_half_support_localization.py`;
- `tests/test_p022_barlow_half_support_localization.py`.

The tests verify the recursive largest-prime-factor support bound, both residue-class localization theorems, and exact support-offset examples.
