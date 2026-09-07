# BRC Euler Phase Shadow and Multiplier Trace Collapse

Status: `RESEARCH FRONTIER / EXACT UNIVERSAL PHASE IDENTITY + EXCHANGE-PAIR CHEBYSHEV COLLAPSE + DISCRETE-LOG BOUNDARY / NO SPEEDUP CLAIM`
Date: `2026-09-08`
Parents:
- `research_notes/BRC_FINITE_GROUP_PHASE_BSGS_BOUNDARY_20260908.md`
- `research_notes/BRC_MULTIPLIER_COLLISION_ENERGY_TRACE_20260908.md`
Source snapshot before write: `main@11bb40043d6f36c210d4574a4781f2ccae873572`

## 0. Purpose

Earlier collision work searched for an N-only residue or phase shadow of the hidden collision energy `E3`. The finite-group phase audit reveals a stronger exact fact: every integer-polynomial observer in the hidden factor sum `S=p+q` has an N-only group image in every unit-generated cyclic subgroup. This includes `E3`, `g^2`, and every symmetric multiplier second-moment observer.

At the same time, the full exchange-pair multiplier phase lattice collapses to one hidden Chebyshev trace coordinate. Thus larger composite multipliers do not create independent phase dimensions. The obstacle is phase inversion / trace construction, not existence of an N-only group image.

---

## 1. Universal Euler phase shadow theorem

Let

`N=pq`

for distinct primes, and put

`S=p+q`.

Then

`N+1-S=(p-1)(q-1)=phi(N)`.

For any

`alpha in (Z/NZ)^*`,

let `M=ord_N(alpha)`. Since `M | phi(N)`,

`S == N+1 (mod M)`.

Therefore for every integer-coefficient polynomial

`F(X,N) in Z[X,N]`,

`F(S,N) == F(N+1,N) (mod M)`.

Exponentiating gives the exact N-only phase identity

`alpha^(F(S,N)) = alpha^(F(N+1,N)) (mod N)`.

Freeze:

`EVERY_S_POLYNOMIAL_OBSERVER_HAS_AN_N_ONLY_UNIT_GROUP_PHASE_SHADOW`.

This is an observer identity only. Recovering the exponent residue from its group value is a discrete-log/collision problem and is not free.

---

## 2. Collision energy phase is completely N-only

Recall

`E3 = 2*S^2 - 6*N`.

The universal theorem gives

`E3 == 2*(N+1)^2 - 6*N`

modulo `ord(alpha)`, hence

`E3 == 2*(N^2-N+1) (mod ord(alpha))`.

Therefore

`alpha^E3 = alpha^(2*(N^2-N+1)) (mod N)`.

The right side is computable directly from `N` and `alpha` by modular exponentiation.

So the earlier fixed integer congruence

`E3 mod 1152` (and the RSA-270 refinement mod 5760)

is only a small ordinary-residue shadow. In finite-group phase semantics, an arbitrarily large-order element supplies an N-only group image of the entire hidden energy exponent.

Again, this does not expose `E3 mod M` without solving the corresponding exponent-recovery problem.

---

## 3. Gap-square phase is also N-only

Since

`g=q-p`

satisfies

`g^2=S^2-4N`,

the same theorem gives

`g^2 == (N+1)^2 - 4N = (N-1)^2 (mod ord(alpha))`.

Hence

`alpha^(g^2)=alpha^((N-1)^2) (mod N)`.

Thus the hidden factor-gap square has a direct N-only group phase even though its integer value is factor-complete.

This is the phase analogue of the earlier observation that a factor-complete scalar can have an easily computable lossy observer.

---

## 4. General symmetric collision-energy family

The previous multiplier-energy note proved for symmetric odd multiplier domains

`E_K=A_K*S^2+B_K*N`

with public integers `A_K,B_K` depending only on the chosen domain.

Therefore every such energy has

`alpha^(E_K)
 = alpha^(A_K*(N+1)^2+B_K*N) (mod N)`.

So changing `K`, adding composite multipliers, or taking more second moments does not create independent group-phase information. All of them factor through the same Euler phase relation for `S`.

This is the group-phase counterpart of the earlier rank-one second-moment theorem.

---

## 5. Exchange-pair phase coordinates

Consider a hidden odd multiplier split `(a,b)` and its exchange `(b,a)`. Put

`d=(a+b)/2`,

`c=(a-b)/2`,

which are integers for odd `a,b`.

Let

`Y=alpha^S`,

`z=alpha^g`.

Using

`p=(S-g)/2`, `q=(S+g)/2`,

the two hidden phase values are

`U=alpha^(a*p+b*q)=Y^d*z^(-c)`,

`V=alpha^(b*p+a*q)=Y^d*z^c`.

Their product is

`U*V=Y^(2d)=alpha^((a+b)S)`,

which is N-only because `Y=alpha^(N+1)`.

The only exchange-sensitive information is their normalized trace

`(U+V)/Y^d = z^c+z^(-c)`

when this ring addition/normalization is defined and `Y` is a unit, which it is.

Define

`tau_c=z^c+z^(-c)`.

---

## 6. Chebyshev trace collapse

The traces satisfy

`tau_0=2`,

`tau_1=z+z^(-1)`,

and

`tau_(c+1)=tau_1*tau_c-tau_(c-1)`.

Hence every exchange-pair phase trace is an integer polynomial in the single hidden coordinate

`tau_1=alpha^g+alpha^(-g)`.

Equivalently, with the usual Chebyshev normalization,

`tau_c = 2*T_c(tau_1/2)`

formally whenever the division-by-two notation is meaningful; the recurrence form is valid integrally and is the preferred composite-modulus statement.

Freeze:

`COMPOSITE_MULTIPLIER_EXCHANGE_PHASE_LATTICE -> ONE_HIDDEN_TRACE_COORDINATE`.

Thus increasing the composite multiplier horizon cannot generate independent trace dimensions. It only evaluates higher Chebyshev polynomials of the same hidden phase trace.

---

## 7. Known product / unknown trace is the exact hidden-pair geometry

The exchange pair `(U,V)` is the root pair of

`X^2 - T*X + P`,

where

`P=U*V=Y^(2d)` is N-only,

while

`T=U+V=Y^d*tau_c`

is hidden.

This exactly mirrors the integer factor pair:

- product known;
- trace/sum factor-complete;
- symmetric polynomial collapse preserves product but not the distinguishing trace.

So the finite-group lift does not bypass the original semiprime geometry; it recreates it inside the phase carrier.

---

## 8. What would a nontrivial trace constructor buy?

If `tau_1` were N-only computable for a chosen `alpha`, then the quadratic

`Z^2-tau_1*Z+1=0 (mod N)`

has roots `z=alpha^g` and `z^(-1)`.

However solving this quadratic modulo composite `N` or recovering `g` from `z` is not automatically easy; it may itself expose a factor or reduce to a discrete-log/root-finding problem depending on the chosen group and order structure.

A trace constructor is therefore potentially valuable only if its full construction and subsequent decoding cost beats standard phase search.

Special opportunistic cases exist: for example

`tau_1-2=(z-1)^2/z`,

so `gcd(tau_1-2,N)` is nontrivial if `z` is 1 modulo exactly one prime factor. This is a Pollard-p-1/order-divisibility type event, not a guaranteed generic mechanism.

---

## 9. Multi-base phase does not change the explicit support exponent by itself

Using several bases `alpha_1,...,alpha_r` replaces a candidate exponent `x` by the vector

`(alpha_1^x,...,alpha_r^x)`

in a product group.

This may enlarge the combined injectivity range through the lcm of component orders, but an explicit two-support meet-in-the-middle search over `C` exponent candidates still obeys

`A*B>=C`,

hence the same `Omega(sqrt(C))` support-count bound from the phase-BSGS note.

So multiple phase coordinates can improve collision uniqueness/capacity but do not by themselves beat the square-root explicit-support exponent.

---

## 10. Revised meaning of the earlier “find E3 residue” target

The collision program originally sought increasingly strong N-only residues of `E3`.

The universal phase theorem now separates three levels:

1. **fixed ordinary residue** — e.g. RSA-270 `E3 mod 5760`; cheap but constant information;
2. **group phase image** — `alpha^E3`, available N-only for any chosen unit `alpha`, potentially in a very large-order subgroup;
3. **decoded exponent residue/value** — `E3 mod ord(alpha)` or `E3` itself, requiring phase inversion/collision search.

The jump from level 2 to level 3 is exactly the hard step. Merely observing level 2 is not a new factor leak.

This closes the conceptual gap between the BRC collision-energy route and the classical deterministic group-phase route: they are two observer views of the same hidden sum relation.

---

## 11. Next smallest unresolved unit

The phase route can now be stated narrowly:

> Is there an N-only operation, specific to the BRC multiplier/exchange structure, that constructs a nonconstant trace `tau_c=alpha^(cg)+alpha^(-cg)` or otherwise decodes the N-only Euler phase shadow in less work than standard BSGS/large-order deterministic factoring?

Kill conditions:

- producing only another polynomial `F(S,N)` phase image, since it is automatically N-only by the universal theorem;
- producing higher `tau_c` values from a known `tau_1`, since that is just the Chebyshev recurrence;
- using ordinary discrete log, BSGS, Pollard p-1, Lucas/Frobenius, or modular root extraction without a new complexity gain;
- claiming that a large-order phase image equals a known exponent residue without decoding.

No Foundation promotion, Working Truth promotion, or factorization-speedup claim is made.