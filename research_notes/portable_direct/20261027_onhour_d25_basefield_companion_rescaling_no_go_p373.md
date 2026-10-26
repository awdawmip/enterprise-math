# D25 / E3 p=373: base-field fixed-z companion rescaling no-go

**Classification:** TASK_RESEARCH author-side exact finite **implementation exclusion**, not a native H0/B0 divided-power execution, not a universal LIFT theorem. `UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT / NOT_SOURCE_CHECKPOINT / NOT_RESULT`.

**Research lane:** `chatgpt-research-onhour-enterprise-math-20260923` (not the maintenance lane). **Task:** `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; **publication:** `TP2-B6F4FC938FF94941C1B7`; **mother objective:** `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`. Frozen scientific source `c47e13e4aba0e006366f989d6334d443f6333ae3` unchanged. Account P000 and its X6 observer typing are respected; the quadratic finite-field extension below is an arithmetic coefficient ring, **not** a newly asserted native spatial plane.

## Consumption and precise question

Consume the previously checked original-E3 invariant-differential and fixed-z derivative from [original E3 dual exact computation](https://github.com/awdawmip/enterprise-math/blob/149d1fa78f7622ce4f8fa75a245c4a303fd33adc/research_notes/portable_direct/20261027_onhour_d25_original_E3_fixedz_companion_negative_control.md). That note excluded the **specific** naive companion `b_plain=a+6 J`. This unit asks the sharper question: **could *any* coefficient-scaled linear combination over the base p-adic ring of the same fixed-z derivative and a repair it, even at the first digit, under Proposition 16's precise normalized-product condition?**

The original curve is `E3(t): y²+xy+(t/27)y=x³`, `t=(2−T)/4`, `T²=2`, `p=373`. Work in
`k=F_373[T]/(T²−2)`. Here `2^186 ≡ −1 (mod 373)`, so `k` is a **field** and its odd `T` coefficient is an independent observable. In the fixed-z original-differential normalization the already verified coefficients are

```
A := a(372)/373  ≡ 349 + 48*T  (mod 373)
J := (partial_lambda|z a(372)) ≡ 215 + 0*T  (mod 373).
```

These coefficients came from two distinct exact integer computations (formal differential ODE and original Lemma 12 binomial formula), not from an ordinary Hesse replacement.

## Exact obstruction, with finite certificate

**Conditional normalization contract.** The supersingular Proposition 16 normalized eigen-companion with determinant choice `b2=p` requires `a(372)*b(372) ≡ −p (mod p²)`. Thus its first digit `B=b(372) mod p` must satisfy `A*B=−1` in `k`; **do not impose this condition on an untyped/untwisted operator**.

Compute `N(A)=(349)^2−2*(48)^2 ≡71`, `71^(-1)≡352` (mod 373). Hence there is exactly **one** admissible first-digit companion for this conditional normalization:

```
B_required = −(349−48*T)/71 ≡ 242 + 111*T  (mod 373)
(349+48*T)*(242+111*T) ≡ 372 + 0*T = −1.
```

For arbitrary `c,d ∈ Z_373` (or even arbitrary elements with residue in `F_373`), any fixed-z ansatz
`b_candidate = c*a(372) + d*J`
has `b_candidate mod373 = 215*(d mod373) ∈ F_373`, because `a(372)≡0`. Its `T`-coefficient is **identically zero**, whereas the required eigen-companion has `T`-coefficient `111 ≠ 0`. Therefore **every base-field scalar linear combination of those two untransported coefficients fails** the conditional normalized first-digit target at p=373. This is stronger than the preceding counterexample for the single fixed multiplier 6, but is still only a typed one-prime native-implementation exclusion.

If one writes `b=a+gamma*J` but permits `gamma∈k`, then the *necessary first-digit* coefficient is uniquely

```
gamma_required = B_required/J = 159 + 318*T  (mod 373),
215*(159+318*T) ≡ 242+111*T.
```

The previously tested multiplier `gamma=6` yields `B_plain=171` and misses the required first-digit coefficient by `71+111*T`. The new calculation **does not prove** that the correct geometric normalized Gauss–Manin transport is given by multiplication by `gamma_required`; a basis transformation, a twist, a different derivation, or a higher-dimensional operator may be necessary. It only records a necessary port-level constraint **if** a scalar-derivative ansatz is proposed.

## Reproducibility (exact integers)

```python
p=373
assert pow(2,(p-1)//2,p)==p-1
A=(349,48); J=(215,0)
norm=(A[0]**2-2*A[1]**2)%p
assert norm==71 and pow(norm,-1,p)==352
B=((-A[0]*pow(norm,-1,p))%p,(A[1]*pow(norm,-1,p))%p)
assert B==(242,111)
product=((A[0]*B[0]+2*A[1]*B[1])%p,(A[0]*B[1]+A[1]*B[0])%p)
assert product==(372,0)
gamma=((B[0]*pow(J[0],-1,p))%p,(B[1]*pow(J[0],-1,p))%p)
assert gamma==(159,318)
assert (6*J[0])%p==171
```

Author-side local exact arithmetic completed with all displayed assertions, **not** a Source-host original H0/B0 benchmark.

## Information, interface and independent next action

BRC **COMPOSE_APPLIED / first-digit signed observer**: keep original E3 curve and formal coordinate, coefficient ring `F_373[T]`, tagged `a/p` and fixed-z derivative `J`, the `T`-odd port, and the *conditional* normalized geometric eigen-companion requirement. Collapsing to a norm or base-field total erases the distinguishing `111*T` obstruction; we use no new BRC axiom or theorem admission.

**Actual missing native experiment unchanged:** authorized same-original-class H0/B0 divided-power representative and `[X]U mod 373²`, native module rank, Frobenius direction/twist/two-digit normalization, odd Green/Hesse observer and original `κ` and `Δ_p−R_p`. The responsible support request is [#1559](https://github.com/awdawmip/enterprise-math/issues/1559), currently **PENDING_OWNER / NATIVE_NOT_EXECUTED**. The existing `p=373` product checkpoint cannot be promoted into a native Result, and no `session/claim/run` ownership is asserted. Next authorized scientific action: native owner *first types the operator and normalization*, computes its original H0/B0 ports, then uses the conditional `B_required` and base-field no-go as falsifiable implementation checks; if a different eigen-companion hypothesis is used, carry its exact determinant/twist contract rather than forcing this calibration. Preserve the earlier accepted UR/CM0 and the 815-prime Wp regression without recomputation.

No research Source checkpoint, publication admission, formal review, result freeze, dispatch or scheduler mutation is claimed. Site-side execution permissions were read-only on this turn; no old request was blindly replayed.
