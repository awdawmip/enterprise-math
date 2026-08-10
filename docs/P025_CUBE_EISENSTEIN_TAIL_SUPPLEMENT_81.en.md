# P025 Supplement 81 — Global Eisenstein Tail for the Prime-Cube Shell

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-cyclotomic-stage76`  
Depends on: P025 Supplements 75–80  
Hard block: `NONE`

## 1. The Stage-80 hard boundary is soluble for exponent three

Stage 80 isolates the supermodular region

\[
M>P
\Longrightarrow
m(F)>\sqrt P,
\]

but leaves its global count open for general odd prime exponent.

For exponent three there is extra algebraic structure: the two nonlinear cyclotomic factors are positive-definite Eisenstein norm forms. This gives a value-side representation bound strong enough to close the supermodular region and, after retaining the exact linear-factor radical from Stage 79, to prove a global power saving for the entire prime-cube shell.

## 2. Setup

Let

\[
3\le q<p\le P
\]

be distinct odd primes. Define

\[
F_+(p,q)=p^2-pq+q^2,
\]

and

\[
F_-(p,q)=p^2+pq+q^2.
\]

Then

\[
p^3+q^3=(p+q)F_+(p,q),
\]

and

\[
p^3-q^3=(p-q)F_-(p,q).
\]

The exact projective atoms are

\[
\rho_{3,+}
=\frac{m(p^3+q^3)}{3(p+q)},
\qquad
\rho_{3,-}
=\frac{m(p^3-q^3)}{3(p+q)}.
\]

For a fixed parameter

\[
0\le\tau\le1,
\]

we count pairs satisfying

\[
\boxed{\rho_{3,\pm}\ge P^\tau.}
\]

## 3. P025-T164 — activation retains the linear-factor radical

Write

\[
L_+=p+q,
\qquad
L_-=p-q.
\]

Stage 79 gives

\[
m(F_+)
\ge
\frac{3P^\tau(p+q)}{\gcd(L_+,3)m(L_+)}.
\]

Since `gcd(L_+,3)<=3` and

\[
\frac{L_+}{m(L_+)}=\operatorname{rad}(L_+),
\]

we obtain

\[
\boxed{
m(F_+)\ge P^\tau\operatorname{rad}(p+q).}
\]

For the difference branch,

\[
m(F_-)
\ge
\frac{3P^\tau(p+q)}{\gcd(L_-,3)m(L_-)}
\]

and hence

\[
\boxed{
m(F_-)>P^\tau\operatorname{rad}(p-q),}
\]

because `p+q>p-q`.

Thus in both branches the nonlinear cyclotomic residual is bounded below by the projective threshold times the radical of the corresponding linear factor.

This retained radical is the key extra information that was discarded by the universal `m(F)>=2T` bound in Stage 79.

## 4. P025-T165 — the nonlinear factors are Eisenstein norms

Let

\[
Q(x,y)=x^2-xy+y^2.
\]

This is the norm form on the Eisenstein integers `Z[omega]`.

Then

\[
\boxed{F_+(p,q)=Q(p,q),}
\]

while

\[
\boxed{F_-(p,q)=Q(p,-q).}
\]

Therefore both cube branches are represented by the same positive-definite binary quadratic norm form.

The classical representation formula gives

\[
r_Q(n)
=6\sum_{d\mid n}\chi_{-3}(d),
\]

so in particular

\[
\boxed{r_Q(n)\le6\tau(n).}
\]

Equivalently, the unique factorization of Eisenstein integers gives at most a divisor-function number of norm representations, up to the six units.

Using the standard divisor bound,

\[
\boxed{r_Q(n)\ll_\varepsilon n^\varepsilon.}
\]

No novelty is claimed for this representation theory.

## 5. External radical-count input

We use the classical de Bruijn estimate in the form recalled as equation (1.1) in Bernert–Browning–Lichtman–Teräväinen, *Bounds on the exceptional set in the abc conjecture*, arXiv:2410.12234v2:

for fixed

\[
\lambda>0,
\]

and every

\[
\varepsilon>0,
\]

\[
\boxed{
\#\{n\le x:\operatorname{rad}(n)\le x^\lambda\}
=O_\varepsilon(x^{\lambda+\varepsilon}).
}
\]

This theorem is external prior art.

## 6. The balanced radical split

Set

\[
\boxed{H=P^{(1-\tau)/2}.}
\]

We split activated pairs according to whether the corresponding linear factor has radical at most `H` or greater than `H`.

The choice of `H` is not heuristic: it exactly balances the two independent counts below.

## 7. P025-T166 — small-linear-radical branch

Suppose

\[
\operatorname{rad}(L_\pm)\le H.
\]

For `tau<1`, de Bruijn's estimate with

\[
\lambda=\frac{1-\tau}{2}
\]

shows that the number of possible linear factors

\[
L_\pm\le2P
\]

is

\[
O_{\tau,\varepsilon}
\left(P^{(1-\tau)/2+\varepsilon}\right).
\]

For each fixed sum `L_+=p+q` or difference `L_-=p-q`, there are at most `O(P)` ordered integer pairs in the height-`P` box; imposing primality only reduces this number.

Therefore the small-radical branch contributes

\[
\boxed{
O_{\tau,\varepsilon}
\left(P^{3/2-\tau/2+\varepsilon}\right).
}
\]

At `tau=1`, the chosen cutoff is `H=1`, while `L_±` is an even integer at least two, so this branch is empty.

## 8. P025-T167 — large-linear-radical branch

Now suppose

\[
\operatorname{rad}(L_\pm)>H.
\]

P025-T164 gives

\[
m(F_\pm)
>P^\tau H
=P^{(1+\tau)/2}
\]

(up to the harmless non-strict sum boundary).

Also

\[
F_+(p,q)\le P^2,
\]

and

\[
F_-(p,q)<3P^2.
\]

Thus every value in this branch lies below

\[
X:=3P^2
\]

and has multiplicity residual at least

\[
Y:=P^{(1+\tau)/2}.
\]

Hence

\[
\operatorname{rad}(F_\pm)
=\frac{F_\pm}{m(F_\pm)}
\ll
P^{(3-\tau)/2}.
\]

Relative to the value height `X asymp P^2`, this is radical exponent

\[
\frac{3-\tau}{4}.
\]

Applying de Bruijn and absorbing fixed constants into `epsilon`, the number of possible norm values is

\[
O_{\tau,\varepsilon}
\left(P^{(3-\tau)/2+\varepsilon}\right).
\]

Each such value has at most

\[
O_\varepsilon(P^\varepsilon)
\]

Eisenstein representations. Therefore the large-radical branch contributes

\[
\boxed{
O_{\tau,\varepsilon}
\left(P^{3/2-\tau/2+\varepsilon}\right).
}
\]

## 9. P025-T168 — global prime-cube projective tail

Combining P025-T166 and P025-T167 gives, for either sign and every fixed

\[
0\le\tau\le1,
\]

\[
\boxed{
N_{3,\pm}(P;\rho_{3,\pm}\ge P^\tau)
\ll_{\tau,\varepsilon}
P^{3/2-\tau/2+\varepsilon}.
}
\]

Here `N_{3,+}` and `N_{3,-}` count distinct odd prime pairs

\[
3\le q<p\le P
\]

in the cube-sum and cube-difference shells respectively.

In particular, at threshold one,

\[
\boxed{
N_{3,\pm}(P;\rho_{3,\pm}\ge1)
\ll_\varepsilon P^{3/2+\varepsilon}.
}
\]

The ambient prime-base pair universe has order at most `P^2`, so this is an unconditional power saving in the prime-cube shell.

No statement about the full abc problem follows from this special-shell theorem.

## 10. Why the exponent is exactly the balanced one

The two branches have costs

\[
P\cdot H
\]

and approximately

\[
\frac{P^2}{P^\tau H}
\]

at the exponent level supplied by radical counting.

Balancing them gives

\[
H^2=P^{1-\tau},
\]

hence

\[
H=P^{(1-\tau)/2}
\]

and common exponent

\[
\boxed{\frac32-\frac\tau2.}
\]

So the `3/2` at threshold one is not an arbitrary artifact of one proof branch. It is the meeting point between:

1. rare low-radical linear factors;
2. rare high-residual Eisenstein norm values.

## 11. Relation to Stage 80

Stage 80 divides signatures into

\[
M\le P
\]

and

\[
M>P.
\]

Stage 81 does not continue the modulus count beyond its horizon. Instead it changes language:

\[
\boxed{
\text{root-of-unity congruence state}
\to
\text{Eisenstein norm value state}.
}
\]

For exponent three, the value state has bounded representation multiplicity, so the supermodular region becomes countable without losing the desired power saving.

This is a concrete success of theorem-native coordinate switching.

## 12. Prior-art / novelty discipline

External/classical ingredients:

- Eisenstein integers and their norm form;
- the representation formula / `6 tau(n)` envelope;
- the divisor bound;
- de Bruijn's radical-count estimate, as recalled in current abc exceptional-set literature.

P025 claims none of those individually.

The project-side candidate is the exact projective activation inequality retaining `rad(p±q)`, the balanced small-linear-radical / large-Eisenstein-residual split, and its use to obtain the stated projective-tail theorem for the prime-cube shell. Historical novelty remains `NOVELTY_UNVERIFIED`.

## 13. Executable assets

Added:

- `src/enterprise_math/abc_cube_eisenstein_tail.py`;
- `tests/test_abc_cube_eisenstein_tail.py`.

The executable compiler checks:

- both nonlinear cube factors as Eisenstein norm values;
- exact rational power thresholds without floating point;
- the retained lower bound `m(F)>=T rad(L)` on activated fixtures;
- the balanced small/large linear-radical branch predicate;
- the exact `6 tau(F)` representation envelope.

## 14. Next frontier

No hard block exists. Continue with:

1. test exponent four as the first parity counter-pressure: determine precisely which part of P025-T155 fails and exhibit minimal activated states with squarefree nonlinear factor;
2. determine whether any higher odd-prime exponent admits an equally cheap norm/Thue representation bound strong enough to close its Stage-80 supermodular region;
3. compare the `3/2-tau/2` shell exponent with direct square-divisor counting to identify which gain truly comes from the Eisenstein value coordinate;
4. relay the successful congruence-to-value coordinate switch to A2/E002 after the parity boundary is fixed.
