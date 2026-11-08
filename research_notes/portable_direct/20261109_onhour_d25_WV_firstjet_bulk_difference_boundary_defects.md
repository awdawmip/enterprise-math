# D25: the W216/V2304 first-jet has a four-pole rational discrete connection

**2026-11-09; TASK_RESEARCH / author-side theorem / exact finite regression / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE.** Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; science pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. This result uses, rather than repeats, the newly established all-prime complementary-product first jet `J_p(q)`.

## Rational first difference

For each prime `p>3`, and `1<=q<p`, define as in the preceding theorem

`J_p(q)=Q_p(32/3)+2H_((2q mod p)-1)+3H_((3q mod p)-1)-4H_((4q mod p)-1)-H_(q-1) (mod p)`.

For every `1<=q<=p-2` for which `(3q+1)(3q+2)(4q+1)(4q+3)` is a unit mod `p`, the discrete difference is the **single rational function**

```
J_p(q+1)-J_p(q) = -5(2q+1) /
 [(3q+1)(3q+2)(4q+1)(4q+3)]        (mod p).          (D)
```

### Proof

Away from a carry of `ell*q mod p`, harmonic increments yield

`H_((ell(q+1) mod p)-1)-H_((ell*q mod p)-1)=sum_(a=0)^(ell-1) 1/(ell*q+a)`.

With coefficients `(-1,2,3,-4)` for `ell=(1,2,3,4)`, the `1/q` pieces cancel, and the `2/(2q+1)` and `4/(4q+2)` pieces cancel. The remainder is

`3/(3q+1)+3/(3q+2)-4/(4q+1)-4/(4q+3)`,

whose common-numerator reduction is exactly `-5(2q+1)`, giving (D). The only other carry is at `q=(p-1)/2`; this is removable. Indeed the proven mirror law `J_p(p-q)=J_p(q)` makes this difference zero, matching the zero numerator `2q+1=0 (mod p)` and nonzero denominator for `p>3`. Thus (D) holds wherever the displayed denominator is invertible, including the half-way crossing.

Exactly the four *potential* third- and fourth-division boundary crossings remain; for small `p` some may share the same `q`. They are the only places where (D) needs an explicit direct harmonic jump. Define `B_p={q:1<=q<=p-2, p divides (3q+1)(3q+2)(4q+1)(4q+3)}`, `d_q=J_p(q+1)-J_p(q)`. These are fully defined finite-field observations; no regularization or pole assignment is assumed.

The target class `p=6m+1` has a particularly useful property: **on the entire original W216 first-valuation interval** `2m+1<=q<=3m`, formula (D) holds for every `q` (including the final half-way step). This gives an explicit, pole-free finite difference on precisely the carrier used in the previous grade1/grade2 reflection.

## Additive summation-by-parts interface

For any finite-field weights `w_1,...,w_(p-1)`, put `W_q=sum_(a=1)^q w_a` and `D(q)=-5(2q+1)/[(3q+1)(3q+2)(4q+1)(4q+3)]` on `q not in B_p`. The **exact** identity is

```
sum_(q=1)^(p-1) w_q J_p(q)
  = J_p(p-1) W_(p-1)
    - sum_(q not in B_p, q<=p-2) W_q D(q)
    - sum_(q in B_p) W_q d_q                (mod p).   (SBP)
```

It follows by ordinary finite Abel summation. Equation (SBP) reduces any *additive* test involving this first jet to one rational bulk sum and at most four exact boundary jumps, while preserving the original `w_q` and prefix provenance. For weights supported in `2m+1<=q<=3m` the interior connection is regular. This is an explicit candidate interface for a signed cross-grade telescope; whether the actual frozen `Theta_p` channels couple through these weights is the next mathematics question.

## Exact checks and boundary witness

A separate standard-library modular calculation checked (D) for **5,193 regular adjacent pairs** and the mirror law for **all 5,436 indices** over 49 primes (all primes `5<=p<=229` and `p=373`). There were 194 singular crossings in that range, whose jumps were evaluated by the original harmonic definition, not replaced by rational values.

At `p=373`, `B_p={93,124,248,279}`. Exact jumps `d_q` at these four indices are respectively `87,311,62,286` modulo 373, with the expected mirror antisymmetry `d_(p-1-q)=-d_q`. In the W first-valuation interval `125<=q<=186`, (D) has no poles. For instance `J(125)=321`, `J(126)=117` and `D(125)=169=117-321 (mod 373)`.

This is a local rational-transport theorem and exact, source-preserving finite-field test. It does not substitute an unrelated product for the original signed sums.

## Recovery

The mother task remains `Delta_p-R_p=0 mod p` for `p=13,19 mod24`; existing first-jet and grade results retain their exact proof scopes. Next: instantiate (SBP) with the **original signed W first-valuation unit and mirrored grade2 weights** (then compare against the separate V2304 and B_p channels), testing p=373 before claiming a full LIFT proof. Native original H0/B0 benchmark remains #1559 **OPEN / PENDING_OWNER / NOT_EXECUTED**, requiring `[X]U mod139129` and actual Frobenius/eta/kappa/Delta-R. No Source CLAIM/run was acquired in this author-side note.

## Source-preserving signed grade-2 mirror instance

For every prime `p=6m+1>3`, use the *actual W216 grade-1* coefficient units `U_q=A_q/p (mod p)` on `I={2m+1,...,3m}`. By the previously proved complementary-product law, the exact *original signed grade-2* W contribution satisfies

`T_(2,p)/p^2 = sum_(q in I) w_q (mod p)`, where `w_q=(1-6q)/[36 q^3 U_q] (mod p)`.

Define the source-preserving new first-jet moment `M_p=sum_(q in I) w_q J_p(q)` and prefix weights `P_q=sum_(r=2m+1)^q w_r`. The rational connection is regular on **all** `q in I`, and the *signed additive* identity is

```
M_p = J_p(3m)*(T_(2,p)/p^2)
      - sum_(q=2m+1)^(3m-1) P_q *
             [-5(2q+1)/((3q+1)(3q+2)(4q+1)(4q+3))]
      (mod p).                                                (M)
```

This is a direct application of finite Abel summation, using actual source-labelled W first-grade units and the original `1-6q` weight; no synthetic replacement or extra assumption. A second exact calculation verified (M) for all primes `p=1 mod6` up to 229 and `p=373`. At `p=373`, the interval is `125<=q<=186`; `T_(2,373)/373^2=266`, `J(186)=278`, the rational prefix bulk is `105`, and the **new weighted first-jet moment is `M_373=362 (mod 373)`**. Indeed `266*278-105=362 (mod 373)`.

This gives a concrete additive transfer for an actual signed original-model grade, ready for comparison with the distinct `B_p`, first-grade harmonic correction and V2304 channels of `Theta_p`. The criterion connecting `M_p` to that three-channel target remains open.
