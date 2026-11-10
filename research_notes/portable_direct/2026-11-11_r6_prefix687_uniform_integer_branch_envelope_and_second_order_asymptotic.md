# PREFIX-687-R6 — Uniform integer-slot crossover enclosures, a second-order law, and an exact result-artifact correction

Date: 2026-11-11 Asia/Shanghai. Mode: independent author-side TASK_RESEARCH, no shared-task CLAIM or formal Result/Review. Frozen scientific input: `f42f2906d77f24085c123f3ccfe9667d41caa96d`. This is the finite 189-level Poissonized stopping-time *observer* model, not a new native Heartbeat spatial/arithmetic claim.

## Scope and inherited exact evidence

With `Y(p,z)` the maximum of two independent Poissonized first-stop clocks, put

```
A(z) = Var(Y(z,z)) - Var(Y(0,z))
B(z) = E[Y(z,z)] - E[Y(0,z)]
F_q(z) = q A(z) - B(z)
I = [L,U] = [2663/50000, 53261/1000000]
```

PREFIX-682/683/684 collectively certify on I: `-1800<A'(z)<-1600`, `100<B'(z)<150`, `793/100<B(z)<794/100`, `|A''(z)|<110000000`, a unique `z_A` with `A(z_A)=0`, and, for every real `q>=q_c=B(L)/A(L)`, a unique `z_q in I` satisfying `F_q(z_q)=0`, with `L<=z_q<z_A`. For `q>q_c`, `z_q>L`. PREFIX-685 certifies the **exact** rational endpoint enclosures, all strict, with denominator `S=10^24`:

```
803334881118283114227/S < A(L) < 803334881118283114228/S
7930886194096894324395803/S < B(L) < 7930886194096894324395804/S
9872.453419496357 < q_c < 9872.453419496358.
```

All scientific inputs and prior proof scope are retained at the immutable cited predecessor sources; the present verifier checks new rational consequences, not the original 189-level recurrence.

## Theorem 1: a uniform exact interval for every integer q >= 9873

Let `a_-=803334881118283114227/S`, `a_+=803334881118283114228/S`, `b_-=7930886194096894324395803/S`, `b_+=7930886194096894324395804/S`. Then for **each integer** `q>=9873` the unique local crossing `z_q` obeys

```
L + (q*a_- - b_+)/(1800*q+150)
      < z_q <
L + (q*a_+ - b_-)/(1600*q+100).
```

Indeed `F_q(L)=qA(L)-B(L)>0` and `-(1800q+150)<F'_q(z)<-(1600q+100)`. Apply the mean value theorem on `[L,z_q]` and insert the exact endpoint enclosures. This is a theorem for an **unbounded infinite family of integers**, using finite verified input and analytic inequalities, not finite enumeration.

For the two first eligible integers, direct exact rational cross-products further imply

```
L + 247/10^13 < z_9873 < L + 278/10^13,
L + 699/10^13 < z_9874 < L + 787/10^13.
```

The second bracket is new; the two windows are strictly disjoint and ordered. PREFIX-686 had already certified the q=9873 bracket.

## Theorem 2: an explicit uniform second-order error and exact second-order asymptotic coefficient

For **every real** `q>=q_c`, define `delta_q=z_A-z_q>0`, `a=-A'(z_A)` and `b=B(z_A)`. Then `1600<a<1800`, `793/100<b<794/100`, and

```
0 < delta_q < C/q,                     C = 397/80000,
|delta_q - (b/a)/q| < K/q^2,           K = 8673259/10240000 < 847/1000.
```

Proof: by mean value, `q*delta_q*(-A'(xi))=B(z_q)`, yielding the first bound with `C=(794/100)/1600`. Taylor around `z_A` gives `A(z_q)=a*delta_q+R_A`, with `|R_A|<110000000*delta_q^2/2`, and `|B(z_q)-b|<150*delta_q`. From `qA(z_q)=B(z_q)`,

```
|q*a*delta_q-b| < 150*delta_q + q*55000000*delta_q^2
                 < (150*C + 55000000*C^2)/q.
```

Divide by `q*a>1600*q`; the exact constant simplifies to `K=8673259/10240000`.

Because A and B are finite polynomials (finite survivor model), the inverse function at the simple zero `z_A` is analytic near `u=1/q=0`. With `a=-A'(z_A)`, `b=B(z_A)`, the coefficient of order `q^-2` is fully specified:

```
delta_q = c1/q + c2/q^2 + O(q^-3),   q -> +infinity,
c1 = b/a,
c2 = -b*B'(z_A)/a^2 - A''(z_A)*b^2/(2*a^3).
```

Expand `A(z_A-delta)=a*delta+A''(z_A)*delta^2/2+O(delta^3)` and `B(z_A-delta)=b-B'(z_A)*delta+O(delta^2)` in `qA=B`; coefficient matching proves the displayed formula. The exact jet values at `z_A` remain symbolic, so the formula does not invent a numerical second coefficient.

## Integrity repair to predecessor result

The original committed `PREFIX685_R6_RESULTS.json` accidentally stored `q_c_12digit_floor=9872453419496356`, whereas both its strict bracket and its published Python source establish the true integer floor **9872453419496357**. The error was in the recorded JSON datum, not in the strict inequality or its rational witness.

The direct-main one-field correction is independently persisted and remotely read back at `enterprise-math@c35be76e7231600d9dfd54601e0f1db8d11f18c3`; immutable historical versions remain available. The new checker enforces the exact integer cross-products and consistency of the corrected tick. Avoid IEEE-754/JavaScript Number decoding for this >2^53 integer: inspect exact decimal strings or use arbitrary-size integers.

## Execution, evidence level, continuation

Exact author-side standard-library Python `Fraction` implication checker: `ALL_CHECKS_PASS PREFIX687-R6`. It checks the scaled integer witnesses, constant K, both integer windows, ordering and an additional q=10000 bound. Original source recurrences and independently reviewed mathematical admission were not rerun in this unit.

Status: `AUTHOR_DERIVED / EXACT_RATIONAL_IMPLICATION_CHECKED / UNREVIEWED / NOT_ADMITTED`.

Next: certify `F'_q=qA'-B'` on `[0.052,0.0532600]` and `[0.0532610,0.054]` by local signed Bernstein patches for q=12,24, while continuing the PREFIX-675 two-variable variance-maximum comparison. The uniform local integer-q envelope can serve as a reference test of future branch tracers.
