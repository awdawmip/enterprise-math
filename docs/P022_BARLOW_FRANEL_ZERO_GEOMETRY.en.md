# P022 — Franel Zero-Digit Geometry and Primitive Midpoints

Status: `ACTIVE RESEARCH NOTE / EXACT ZERO-SET STRUCTURE`  
Owner: `program/p022-geometry-v2`  
Depends on: Jarvis--Verrill mirror congruence; Franel recurrence; p-Lucas basin theorem

## 1. Three structures act on the digit-zero set

For an odd prime `p`, write

\[
Z_p=\{1\le d\le p-1:p\mid F_d\}.
\]

Three exact facts are available:

1. p-Lucas makes `Z_p` the complete digit alphabet controlling divisibility of all future Franel terms;
2. Jarvis--Verrill gives reflection symmetry
   \[
   d\in Z_p\iff p-1-d\in Z_p;
   \]
3. the second-order Franel recurrence forbids adjacent zero digits.

The last point is elementary but useful.  The recurrence is

\[
(k+1)^2F_{k+1}
=(7k^2+7k+2)F_k+8k^2F_{k-1}.
\]

If `F_k=F_(k+1)=0 mod p` for `1<=k<=p-2`, then `8k^2` is a unit modulo `p`, so `F_(k-1)=0`.  Backward propagation would force `F_0=0`, contradicting `F_0=1`.

Therefore

\[
\boxed{Z_p\text{ contains no adjacent integers}.}
\]

---

## 2. P022-LI18 — primitive forced midpoint iff the zero alphabet is minimal

Assume

\[
p\equiv5,7\pmod8
\]

and put

\[
m=\frac{p-1}{2}.
\]

The half-index theorem gives

\[
m\in Z_p.
\]

Reflection fixes `m`.  Every other zero occurs in a distinct pair

\[
\{d,p-1-d\},
\]

with one member below `m` and one above `m`.

Hence the following are equivalent:

\[
\boxed{
\begin{aligned}
&p\text{ is primitive at }F_m;\\
&r_p=m;\\
&Z_p=\{m\};\\
&z_p=1.
\end{aligned}}
\]

Thus **primitive half-index divisibility is exactly the minimal p-Lucas basin**.

If the midpoint is not primitive, then the zero alphabet has size at least three and in fact

\[
\boxed{z_p=1+2s\quad(s\ge1).}
\]

The example `p=29` is the first clean boundary:

\[
Z_{29}=\{12,14,16\},
\qquad r_{29}=12<14.
\]

---

## 3. P022-LI19 — infinitely many primitive-divisor events exist in the Franel sequence

The half-index theorem gives a direct proof that infinitely many distinct primes divide the Franel sequence.

Indeed, Dirichlet's theorem supplies infinitely many primes in, for example,

\[
p\equiv5\pmod8.
\]

For every such prime,

\[
p\mid F_{(p-1)/2}.
\]

For each of these primes define its first Franel appearance

\[
r_p=\min\{n\ge1:p\mid F_n\}.
\]

At `F_(r_p)`, the prime `p` is by definition a primitive divisor relative to the Franel sequence.

The set of ranks `r_p` cannot be finite: a finite collection of fixed integers `F_1,...,F_R` contains only finitely many prime divisors, whereas the forced residue family supplies infinitely many distinct primes.

Therefore

\[
\boxed{
\text{the Franel sequence has infinitely many distinct primitive-divisor events}.}
\]

Equivalently, the ranks of apparition of the forced half-index prime family are unbounded.

This does **not** prove that every `F_n` has a primitive divisor, nor that every composite-boundary defect gets one.

---

## 4. Composite-boundary consequence

Restrict further to the infinite prime classes

\[
p\equiv5,23\pmod{24},\qquad p>5.
\]

Then `n=(p-1)/2` lies on the composite A-boundary because

\[
2n-1=p-2
\]

is a multiple of three greater than three.

Thus the composite-boundary half-index family contains infinitely many **distinct** prime witnesses.  Even if some of those primes first appeared at earlier Franel indices, they cannot all be explained by a finite initial prefix.

This rules out a weak interpretation in which the infinite composite family merely recycles finitely many old Franel primes.

---

## 5. Relation to the primitive-defect sufficient condition

The existing sufficient condition for global low-order identifiability says that a fresh primitive prime for each composite-boundary `F_n` would triangularize the pure defect family.

LI19 is weaker but still useful:

- primitive Franel events occur infinitely often;
- forced half-index primes give an explicit infinite source of divisibility;
- midpoint primitivity has the exact local criterion `z_p=1`;
- the unresolved gap is now the placement of those first appearances relative to the composite-boundary indices.

So the global question is no longer "do primitive Franel primes occur at all?"  They do infinitely often.  The hard question is whether the relevant defect indices receive sufficiently independent first-appearance/valuation information.

---

## 6. Executable assets

Added:

- `src/enterprise_math/p022_barlow_franel_zero_geometry.py`;
- `tests/test_p022_barlow_franel_zero_geometry.py`.

The tests verify reflection symmetry, recurrence-based nonadjacency, odd zero-alphabet size in the forced midpoint classes, and the exact primitive/nonprimitive contrast `p=23` versus `p=29`.
