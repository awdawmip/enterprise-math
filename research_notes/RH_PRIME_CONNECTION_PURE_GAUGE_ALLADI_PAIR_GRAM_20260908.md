# RH prime-window pure-gauge no-go / Alladi pair-BRC Gram bridge

Status: `RESEARCH FRONTIER / EXACT FINITE-WINDOW IDENTITIES + PRIOR-ART ALLADI INPUT / NOT A PROOF OF RH`
Date: `2026-09-08`
Project: `Enterprise Math / 进取数论`
Scope: `RH / Möbius / finite Euler windows / critical rank one / Alladi higher duality / Pair-BRC`

## 0. Typing guard

P000 remains unchanged. Prime labels and ordered prime factors are arithmetic provenance, not native X6 axes. X6 remains fixed-width; any growing arithmetic depth is BRC/provenance depth.

BRC order remains

`PROVENANCE > MULTIPLICITY > BOOLEAN SUPPORT`.

The purpose of this note is partly corrective: a previous candidate `prime-adapted connection` used an infinite prime tail at `Re(s)=1/2` and an incorrect sign. The corrected finite-window calculation shows that the candidate connection is pure gauge and has zero insertion holonomy.

---

## 1. Finite prime window and the exact rank-one coordinate

Let `S` be any finite set of primes and define

`P_S(s)=sum_{p in S} p^{-s}`.

For `z != 0` and `P'_S(s) != 0`, define

`q_S(z,s)=z P_S(s)`.

The exact vector field tangent to `q_S=constant` is

`V_S = partial_z - [P_S(s)/(z P'_S(s))] partial_s`.

Indeed

`V_S(q_S)=P_S - [P_S/(zP'_S)] zP'_S = 0`.

On the Möbius slice `z=-1`,

`V_S|_{z=-1}=partial_z + [P_S/P'_S] partial_s`.

Since `P'_S<0` on the positive real axis, this coefficient is negative.

Freeze correction:

`PRIME_ADAPTED_NULL_VECTOR_SIGN = P/P' ON z=-1`.

The earlier sign `-P/P'` was wrong.

---

## 2. Pure-gauge theorem and zero discrete insertion holonomy

The scalar `q_S=zP_S(s)` is an explicit first integral of `V_S`. Therefore the integral curves of `V_S` are merely level sets of one scalar coordinate.

Consider adding a prime `p` to a finite window. At fixed `z`, define the compensated insertion map `T_p` by choosing the unique real `s'` satisfying

`P_{S union {p}}(s')=P_S(s)`

whenever monotonicity guarantees uniqueness.

For two new primes `p,q`, both compositions `T_q o T_p` and `T_p o T_q` end at the unique `s''` satisfying

`P_{S union {p,q}}(s'')=P_S(s)`.

Hence

`T_p T_q = T_q T_p`.

More generally, any finite insertion order gives the same final compensated state; it depends only on the final prime set and the conserved value of `q_S`.

Freeze:

`FINITE_PRIME_WINDOW_COMPENSATED_INSERTION_HOLONOMY = 0`.

Therefore any nonzero `y`-curvature obtained solely by differentiating the frozen coefficient `P/P'` is not a new arithmetic invariant; it is a coordinate artefact of replacing the exact first-integral flow by a partial continuous parametrization.

Consequence:

`PRIME_ADAPTED_CONNECTION_ALONE CANNOT CREATE RH CANCELLATION`.

---

## 3. Stable Euler channels have one-sign residual along the primitive null flow

For the same finite prime set, write

`L_S(z,s)=sum_{p in S} log(1+z p^{-s})`

and its power-sum expansion

`L_S(z,s)=sum_{k>=1} (-1)^{k+1} z^k P_S(ks)/k`.

The `k=1` channel is exactly `q_S=zP_S(s)` and is killed by `V_S`.

For `k>=2`, evaluation at `z=-1` gives

`V_S L_{S,k} = P_S(ks) - [P_S(s)/P'_S(s)] P'_S(ks)`.

Define the weighted log-prime means

`ellbar_k(s)= -P'_S(ks)/P_S(ks)`.

Then

`V_S L_{S,k}=P_S(ks)[1-ellbar_k/ellbar_1]`.

For real `s>0`, the probability weights proportional to `p^{-ks}` are an exponential tilt toward smaller primes as `k` increases. If

`m(r)=sum log(p) p^{-rs}/sum p^{-rs}`,

then

`m'(r)=-s Var_r(log p) <= 0`.

Therefore

`ellbar_k <= ellbar_1`

and hence

`V_S L_{S,k} >= 0` for every `k>=2`.

Equivalently, with `a_p=p^{-s}` and

`W=sum a_p/(1-a_p)`,

`ellbar_geom = [sum log(p)a_p/(1-a_p)]/W`,

we have

`V_S L_S(-1,s)=W[1-ellbar_geom/ellbar_1] >= 0`.

Equality holds only in the degenerate one-log-level case.

Freeze:

`STABLE_EULER_CHANNELS_ARE_MONOTONE_ALONG_THE_PRIMITIVE_NULL_FLOW`.

Thus the absolutely stable channels do not feed back with alternating sign to annihilate the critical primitive channel. They give a one-sign residual.

---

## 4. Alladi higher duality as an exact generating polynomial

Let `n` have distinct prime factors

`q_1 < q_2 < ... < q_r`.

For any prime test function `f`, define

`G_n(t;f)=sum_{1<d|n} mu(d) t^{omega(d)-1} f(p_1(d))`,

where `p_1(d)` is the least prime factor.

Group divisors by their least prime `q_j`. A divisor with least prime `q_j` contains `q_j` and an arbitrary subset of `q_{j+1},...,q_r`. Hence

`sum_{d: p_1(d)=q_j} mu(d)t^{omega(d)-1}`
`= -sum_T (-t)^{|T|}`
`= -(1-t)^{r-j}`.

Therefore exactly

`G_n(t;f) = -sum_{j=1}^r f(q_j)(1-t)^{r-j}`.

This packages Alladi's full higher-order hierarchy in one polynomial.

Taking the `(k-1)`st normalized derivative at `t=1` gives

`1/(k-1)! G_n^{(k-1)}(1;f)`
`= sum_{1<d|n} mu(d) C(omega(d)-1,k-1) f(p_1(d))`
`= (-1)^k f(P_k(n))`,

where `P_k(n)` is the kth largest distinct prime factor.

This recovers the general higher-order duality stated in Alladi--Sengupta (2026, arXiv:2604.17832, eq. (1.10)).

---

## 5. Alladi-jet kernel no-go

The polynomials

`1,(1-t),...,(1-t)^{r-1}`

are linearly independent. Therefore the full jet vector

`(G_n(1),G'_n(1),...,G_n^{(r-1)}(1))`

is a triangular invertible change of basis for the ordered-prime data

`(f(P_1(n)),...,f(P_r(n)))`.

Consequently:

`FULL_ALLADI_JET_TRANSFORM_HAS_TRIVIAL_KERNEL`.

There is no universal nonzero linear combination of the full Alladi jets that annihilates the primitive-prime channel while preserving all arithmetic information.

For a truncation to the first `K` jets, the only lost information is exactly the ordered-prime tail

`P_{K+1}(n),P_{K+2}(n),...`.

Thus the correct interpretation of the high-order hierarchy is

`ALLADI_JETS = LOSSLESS_ORDERED_PRIME_CHANGE_OF_BASIS`,

not an algebraic source annihilator.

At the RH-critical growing depth `K~(1/2)log x/loglog x`, previous positive capacity bounds show that the unobserved high-arity tail can already be square-root size. This remains a useful truncation interface, but it creates no extra cancellation in the visible primitive channel.

---

## 6. Exact Alladi--Pair--BRC Gram identity

Define

`A_k(n;f)=sum_{1<d|n} mu(d) C(omega(d)-1,k-1) f(p_1(d))`
`=(-1)^k f(P_k(n))`.

For two integers `n,m` and prime test functions `f,g`, sum over `k`:

`sum_{k>=1} A_k(n;f)A_k(m;g)`
`=sum_{k>=1} f(P_k(n))g(P_k(m))`.

Expanding the divisor sums and using Vandermonde

`sum_{j>=0} C(a,j)C(b,j)=C(a+b,a)`

gives the exact identity

`sum_{k>=1} f(P_k(n))g(P_k(m))`
`= sum_{d|n,e|m,d,e>1}`
`  mu(d)mu(e)`
`  C(omega(d)+omega(e)-2,omega(d)-1)`
`  f(p_1(d))g(p_1(e)).`

The coefficient

`C(omega(d)+omega(e)-2,omega(d)-1)`

is exactly the two-arm shortest-path shuffle multiplicity

`(a+b)!/(a!b!)`

with arm lengths `a=omega(d)-1`, `b=omega(e)-1`.

Hence this is an exact Pair-BRC composition using the existing T0 BRC multiplicity, not a new combinatorial primitive.

For `f=g`, define

`K_f(n,m)=sum_k f(P_k(n))f(P_k(m))`.

Then `K_f` is positive semidefinite because it is the Gram kernel of the ordered-prime feature vectors

`v_f(n)=(f(P_1(n)),f(P_2(n)),...)`.

Freeze project interface:

`ALLADI_PAIR_BRC_GRAM_KERNEL`.

It is a provenance-preserving positive kernel whose divisor-cloud representation contains Möbius signs but whose total value is PSD.

---

## 7. Immediate limitation of the Gram bridge

The Gram identity preserves ordered-prime information but does not itself estimate Möbius parity. The parity of a squarefree integer is the parity of the feature-vector length, while `K_f` is a positive quadratic overlap statistic.

Thus

`ORDERED_PRIME_GRAM_POSITIVITY != PARITY_CANCELLATION`.

Any use toward RH must add a quantitative cross-Cell statement linking rank/provenance overlap to the earlier Pair-BRC collision kernel

`H_x(-1) <= x^eps H_x(0)`.

No such inequality is proved here.

---

## 8. Current frontier after the two no-go results

The following two tempting mechanisms are now closed:

1. `prime-adapted connection / y-holonomy` -- pure gauge for finite prime windows, with exact zero insertion holonomy;
2. `Alladi-jet algebraic annihilator` -- full hierarchy is triangular invertible, so there is no nontrivial universal kernel.

The surviving exact positive structure is the Alladi--Pair--BRC Gram kernel.

Therefore the next admissible target is not a new local coordinate change. It is a genuinely quantitative cross-Cell estimate, preferably on a PSD/provenance-preserving pair kernel, that can be compared to the existing RH collision criterion without collapsing prime labels.

Candidate next question:

`Can the Alladi--Pair--BRC Gram kernel be coupled to the Riesz pair-distance kernel in a way that controls the parity boundary by collision, with at most x^o(1) loss?`

Any negative result should identify the missing degree of freedom explicitly.

---

## 9. Prior-art boundary

- Alladi's higher-order duality is prior art; the 2026 Alladi--Sengupta paper states the general identity quantitatively.
- Alamoudi 2026 studies the corresponding subradically sifted sums for fixed `k`.
- The generating-polynomial packaging, pure-gauge finite-window audit, monotone stable-channel residual, and Pair-BRC Gram packaging are project-derived interfaces/identities in this note.
- None of these results proves RH or gives a new zero-free region.
