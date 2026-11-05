# D25 — simple-root and Hensel lifting certificate for the signed Clausen observer

Date: 2026-11-05 (+08). Role: TASK_RESEARCH; portable author-side evidence, not a Source-native claim. Logical lane: `chatgpt-research-hourly-enterprise-math-20260923`.
Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; **frozen science pin** `c47e13e4aba0e006366f989d6334d443f6333ae3`.
Status: **AUTHOR-PROVED finite-polynomial algebra / 94-prime exact validation / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CM**.

## Theorem (observer-zero cannot have multiplicity two)

Let p=6n+1>=7 be prime, work over Z_(p), and put

```
G_p(z) = _2F1(-n,-2n;1-p/2;z), a polynomial of degree n;
L_p(z) = G_p(z) + 12 z G_p'(z);
Psi_p(z) = G_p(z) L_p(z);       x=1/2.
```

The denominator factors in G_p are p-adic units for k<=n. Let the first-digit premise be `W_p ≡ 0 (mod p)`, where W_p is the *original signed 216* truncated weighted sum. That first digit is an inherited, frozen input for the task's target primes p≡13,19 (mod 24); it is **not** newly proved here for other prime classes. The previously proved exact first-digit shadow reduction and terminating Clausen identity give

```
W_p ≡ S_n ≡ Psi_p(1/2)   (mod p).
```

Then exactly one of G_p(x) and L_p(x) vanishes modulo p, and **the zero of Psi_p at x is simple**:

* If G_p(x)=0 mod p, then J=(zG'_p(z))|_(x) is nonzero mod p, L_p(x)=12J and

  `Psi_p'(x) ≡ 24 J^2 (mod p)`, a unit.

* If L_p(x)=0 mod p, then G_p(x) is nonzero mod p and

  `Psi_p'(x) ≡ G_p(x)^2/6 (mod p)`, a unit.

Consequently there exists a **unique** root `x_p ∈ Z_p` of Psi_p(z) in the disk `x_p ≡ 1/2 (mod p)`. That root lifts the *same vanishing factor* (G or L), since the other factor remains a p-adic unit in the disk. This is an exact structural result; it does not identify which residue class selects which factor.

More precisely, with `f=Psi_p(x)`, `a=Psi_p'(x)`, `b=Psi_p''(x)/2` in Z_(p), and `d=f/a` (a a unit),

```
x_p ≡ x - d                      (mod p^2),
x_p ≡ x - d - (b/a)d^2           (mod p^3).
```

These formulas preserve the original `z=1/2` normalization; they **do not** identify x_p as a native H0/B0 geometric parameter.

## Proof

Mod p, the hypergeometric polynomial g(z)=G_p(z) satisfies its exact Gauss differential equation

```
z(1-z)g'' + [1-(1-3n)z]g' - 2n^2 g = 0.
```

At x=1/2 its leading coefficient is 1/4, a unit. If g(x)=g'(x)=0, repeated differentiation of this equation forces g^(j)(x)=0 for all j≥0. Since deg(g)=n<p, Taylor expansion over F_p then forces g=0 as a polynomial, contradicting g(0)=1. Therefore g and g' cannot simultaneously vanish at x.

Now `L(x)=g(x)+6g'(x)`. If g(x)=0, then g'(x)≠0 and L(x)=6g'(x), which is nonzero for p≥7. Hence Psi'(x)=g'(x)L(x)=6g'(x)^2=24J^2.

If L(x)=0 then necessarily g(x)≠0 and g'(x)=-g(x)/6. Differentiating L and eliminating g'' by the Gauss equation yields

```
L'(x) = (1-36n)g'(x)+48n^2 g(x).
```

Since `6n≡-1 (mod p)`, this becomes `L'(x)≡7g'(x)+(4/3)g(x)`. In the L-vanishing case, `L'(x)≡g(x)/6`, whence Psi'(x)=g(x)L'(x)=g(x)^2/6≠0.

The first-digit premise makes Psi(x) vanish modulo p, so one of the two factors vanishes. Mutual exclusion and the derivative calculations prove the simple-root dichotomy. Hensel's lemma gives the unique Z_p root. Taylor expansion `0=Psi(x-delta)=f-a delta+b delta^2+O(delta^3)` for delta∈p Z_p gives the displayed mod p^2 and mod p^3 formulas. QED.

## Exact arithmetic validation / semantic scope

A new standalone BigInt checker uses two independent finite routes: recurrence at x for g,g',g'',g''', and polynomial Horner evaluation at the independently calculated Hensel root. It checks all **94 primes** `7<=p<=1200, p≡1 (mod 6)`: first-digit Psi=0, mutually exclusive factor zero, explicit derivative branch formula, and `Psi(x_p)=0 (mod p^3)`. **94/94 PASS**. These are finite checks, not the proof of the universal first-digit premise outside the frozen target class.

Examples (`G,L,J,Psi'(x) mod p`): p13=(0,6,7,6); p19=(0,12,1,5); p373=(0,171,294,211); p31=(21,0,6,27). Unique root x_p modulo p^3: p13=1918 modulo 2197; p19=675 modulo 6859; p373=31342631 modulo 51895117.

## BRC and mother-target use

The observer is the signed `1+6 z ∂_z` applied to the Clausen square. Retain `(G,L,J,Psi'(x), branch label, p-adic precision, coefficient provenance)`. Compressing their product to a zero scalar **erases the factor branch**, whereas the above derivative is a nonzero certificate of a transversal crossing. A single active factor plus a unit factor can now replace an undifferentiated product in the next LIFT calculation; this is an observer-level reduction, not a claim about the full native X6/H0-B0 carrier.

Combine this exact factor certificate with the existing signed six-port and second harmonic jet:

```
W_p ≡ Psi_p(1/2)
  + p [A+B-(3/2)U_1]
  + p^2[C+D+E-(9U_11+5U_2)/8]         (mod p^3).
```

This is inherited algebraic substitution with **new factor-local interpretation**, not a proof of `W_p≡p (mod p^3)`. Next: use the unit/nonunit split to reduce the nontrivial p-adic cancellation to one factor's expansion, seek a uniform arithmetic evaluation (especially the observed but still unproved Legendre-symbol factor selection), and compare with frozen `Delta_p-R_p` without dropping the signed derivative/frobenius ports.

Native D25 p373 original-class H0/B0 divided-power, `[X]U mod 139129`, rank, Frobenius direction, eta/kappa and independent review remain `NOT_RUN / OPEN`. Do not substitute this ordinary hypergeometric polynomial or its Hensel zero for those native computations.

## Control / provenance boundary

Read canonical-global entry and current Enterprise Math control/method entries on 2026-11-05. Preexisting Source checkpoint `SOURCE_BYTES_AND_RECORDED_CLAIM_VERIFIED` has previous owner contributions and source pins; no prior Source `completed_units` are newly claimed here. New read-only control requests `em-h20-20261105-1920-task-current` and `em-h20-20261105-1920-continuation-current` use the original IDs for receipt reconciliation. This file is *portable author-side material*, not `publish_checkpoint`, RESULT or admission. Formal claim/open awaits exact current Researcher session and authorized Source route.
