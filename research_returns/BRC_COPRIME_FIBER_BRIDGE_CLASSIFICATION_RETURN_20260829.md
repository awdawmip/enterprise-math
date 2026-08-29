# BRC 互素纤维桥分类研究回报

Researcher-ID: `EM-MBGB0-4D9A72`

Task: `RS-BRC-COPRIME-FIBER-BRIDGE-CLASSIFICATION`

Publication: `TP2-E2C0B1C2A3334B54BAAD`

Claim: `chatgpt-mbgb0-20260829-1853-4d9a72`

Execution branch: `research/brc-coprime-fiber-bridge-em-mbgb0-4d9a72`

Execution base: `1b134d8c55ccd941e4b338752825443589726be2`

Frozen accepted source:

`driver_reviews/CBRC_F3R2_SURVIVOR_MEMBERSHIP_PREDICATE_DRIVER_REVIEW_20260823.md`

Accepted F3R2 owner head:

`bb020ddc567bfc8b0a240bf3df0fd83ae7e1ad6d`

Primary verdict:

`SUCCESS / NEGATIVE_BOUNDARY_AT_ONE_SIDED_COLLAPSE_LAYER`

Hard-target disposition:

`B0-B5_CLASSIFIED / CURRENT_F3R2_SUPPLIES_EXACT_COEFFICIENT_SUPPORT_SPLITTING_BUT_NOT_A_GENUINE_FACTOR_BLIND_ONE_SIDED_COLLAPSE_OPERATOR`

## 1. Executive result

The accepted F3R2 theorem does support an exact and useful **bridge-existence layer**, but its natural carrier is the prime support of the **operator coefficients**, not automatically the hidden CRT factors of an unrelated semiprime target `N=pq`.

For

`A=[[a,b],[c,d]] in GL_2(Z)`

define

`g(A)=gcd(|a|,|d|)`

and

`h(A)=gcd(|b|,|c|)`.

The accepted theorem is exactly

`SURVIVOR(A) <=> g(A)>1 and h(A)>1`.

Because `det(A)=+-1`,

`gcd(g(A),h(A))=1`.

Every survivor therefore admits distinct primes

`r | g(A)`

and

`s | h(A)`,

with `A mod r` anti-diagonal monomial and `A mod s` diagonal monomial. This is an exact coefficient-support splitting theorem.

The crucial negative boundary is that `A` itself can never be a one-sided CRT collapse operator: unimodularity makes `A mod N` invertible for every modulus `N`. Thus the opposite monomial orientations are **orientation contrast, not rank collapse**.

For a hidden semiprime `N=pq`, the exact factor-blind coupling test is

`u_N(A)=gcd(N,g(A))`

and

`v_N(A)=gcd(N,h(A))`.

A genuine hidden-channel split occurs exactly when both `u_N(A)` and `v_N(A)` are proper nontrivial divisors of `N`. For distinct-prime semiprimes this forces

`{u_N(A),v_N(A)}={p,q}`.

Therefore the first exact factor-blind test that says the F3R2 coefficient bridge is actually aligned with both hidden CRT channels already **returns the two factor endpoints by Euclidean gcd**. At this interface there is no nontrivial middle layer

`hidden bridge observable but endpoint still hidden`.

The only canonical one-sided residues directly available from the accepted invariants,

`C_g = g(A) mod N`

and

`C_h = h(A) mod N`,

collapse one CRT channel exactly when `gcd(N,g(A))` or `gcd(N,h(A))` is a proper divisor. But that is definitionally the same direct-gcd extraction and is therefore classified here as

`DEGENERATE_COEFFICIENT_PROJECTION / NOT_A_NEW_BALANCED_COUPLING_COLLAPSE`.

So the current CBRC result is best interpreted as:

`EXACT FACTOR-AWARE COEFFICIENT-SUPPORT BRIDGE EXISTENCE`

plus

`FACTOR-BLIND SURVIVOR MEMBERSHIP`,

not yet as

`FACTOR-BLIND HIDDEN-CRT ENDPOINT RECOVERY`.

A new noninvertible or nonlinear public response primitive is required for the latter.

---

## 2. B0 — semantic translation table

| Current CBRC/F3R2 object | Multiplicative bridge interpretation | Status |
|---|---|---|
| free coordinate `n in Z` in the accepted carrier | integer carrier coordinate on which prime divisibility can be tested | `EXACT` |
| full operator `M=(A,B,D)` | balanced two-slot automorphism; free block controls membership | `EXACT` |
| `g=gcd(|a|,|d|)`, `h=gcd(|b|,|c|)` | coefficient-support invariants selecting opposite matrix orientations modulo prime divisors | `EXACT` |
| `p|g`, `r|h` in the accepted sufficiency proof | two coefficient prime sectors with opposite anti-diagonal/diagonal monomial behavior | `EXACT` |
| `q_{p,r}(n,t)=1/2*(1_{p∤n}+1_{r∤n})` | explicit support-splitting conserved witness | `EXACT`, but factor-aware because `p,r` are explicitly selected |
| `SURVIVOR(A)` | existence of at least one coefficient-support split | `EXACT` |
| coefficient-support split = bridge between hidden factors of arbitrary `N=pq` | requires an additional alignment condition | `NOT_JUSTIFIED` without coupling to `N` |
| opposite monomial orientation mod two primes = one-sided collapse | false: both reductions remain invertible | `NOT_JUSTIFIED` |
| `g,h` survivor membership can be decided without factoring them | bridge-existence membership is factor-blind | `EXACT` |
| explicit prime-pair witness can be produced without factoring/selecting divisors of `g,h` | not supplied by F3R2 | `NOT_JUSTIFIED` |

This table freezes the main semantic distinction:

`COEFFICIENT SUPPORT != HIDDEN TARGET SUPPORT`.

---

## 3. Definitions for the hidden-semiprime interface

Let

`N=pq`

with distinct primes `p,q`, unknown to the proposed factor-blind mechanism but available to a verifier.

For `A in GL_2(Z)`, define

`g=g(A)=gcd(|a|,|d|)`

and

`h=h(A)=gcd(|b|,|c|)`.

Define the factor-blind target intersections

`u=gcd(N,g)`

and

`v=gcd(N,h)`.

### DEFINITION 3.1 — coefficient bridge

`COEFF_BRIDGE(A)` iff `g>1 and h>1`.

By accepted F3R2 this is exactly `SURVIVOR(A)`.

### DEFINITION 3.2 — hidden split alignment

`N_SPLIT_BRIDGE(A,N)` iff

`1<u<N`

and

`1<v<N`.

For a distinct-prime semiprime this means one hidden prime lies in the `g` support and the other lies in the `h` support.

### DEFINITION 3.3 — direct coefficient endpoint

`DIRECT_ENDPOINT(A,N)` iff

`1<u<N`

or

`1<v<N`.

This means one of the public coefficient invariants itself has one-sided CRT vanishing.

### DEFINITION 3.4 — genuine new BRC collapse response

A candidate

`C_lambda(A,N) in Z/NZ`

counts as a genuine new BRC collapse response only if:

1. its formula is factor-blind;
2. it is derived from a predeclared BRC/balanced construction, not by inserting a desired factor witness;
3. for some public `lambda`, its CRT zero-status is nonconstant:
   `C_lambda=0 mod p` and `C_lambda!=0 mod q`, or vice versa;
4. it is not merely the coefficient projection `g mod N`, `h mod N`, or an algebraically equivalent direct-gcd repackaging.

The current accepted F3R2 theorem does not supply such a `C_lambda`.

---

## 4. THEOREM B1-A — exact coefficient bridge existence

For `A in GL_2(Z)`,

`COEFF_BRIDGE(A)`

iff

`g(A)>1 and h(A)>1`.

Moreover, if this holds then there exist distinct primes `r|g`, `s|h` such that:

- `A mod r` is anti-diagonal monomial;
- `A mod s` is diagonal monomial;
- the accepted conserved witness `q_{r,s}` exists.

### Proof

The iff is exactly the accepted F3R2 membership theorem.

If `r|g`, then `r|a,d`. Since `det(A)=+-1`, neither `b` nor `c` can vanish modulo `r`; hence the reduction is anti-diagonal monomial.

If `s|h`, then `s|b,c`, and unimodularity forces `a,d` nonzero modulo `s`; hence the reduction is diagonal monomial.

Also `gcd(g,h)=1`: a prime dividing both would divide all four entries and hence the determinant, contradicting `det(A)=+-1`.

Therefore `r!=s`, and the accepted F3R support-splitting theorem supplies `q_{r,s}`.

`QED`.

Classification:

`THEOREM / EXACT`.

---

## 5. THEOREM B2-A — unimodular balanced operators cannot linearly collapse one CRT channel

Let `A in GL_2(Z)` and let `N>=2`.

Then the reduction

`A_N in GL_2(Z/NZ)`

is invertible.

If `N=pq` is squarefree semiprime, under CRT

`(Z/NZ)^2 ~= F_p^2 x F_q^2`

both channel maps `A_p` and `A_q` are invertible.

Therefore no nonzero channel vector is sent to zero by the linear action of `A` in exactly one hidden channel.

### Proof

`det(A)=+-1`, which is a unit modulo every `N`. Hence `A_N` is invertible. Its CRT components have determinant `+-1 mod p` and `+-1 mod q`, so each is invertible.

`QED`.

Consequences:

1. F3R2's opposite diagonal/anti-diagonal orientations are not singularities.
2. A one-sided endpoint witness must be produced by a new noninvertible/nonlinear observable, quotient, projection, singularization, collision, or equivalent post-processing.
3. Calling the accepted survivor matrix itself a “collapse bridge” would overstate the theorem.

Classification:

`THEOREM / NEGATIVE_BOUNDARY`.

---

## 6. THEOREM B1-B — exact hidden-channel alignment criterion

Let `N=pq` with distinct primes and `A in GL_2(Z)`.

Put

`u=gcd(N,g(A))`

and

`v=gcd(N,h(A))`.

Then the following are equivalent:

1. `N_SPLIT_BRIDGE(A,N)`;
2. `u` and `v` are both proper nontrivial divisors of `N`;
3. `{u,v}={p,q}`;
4. one hidden prime sees the anti-diagonal F3R2 orientation and the other hidden prime sees the diagonal orientation.

### Proof

Because `gcd(g,h)=1`, also `gcd(u,v)=1`.

The only positive divisors of `N=pq` are `1,p,q,N`. If both `u` and `v` are proper nontrivial divisors and are coprime, they must be `p` and `q` in some order.

If a hidden factor divides `g`, the preceding monomial argument makes its reduction anti-diagonal. If it divides `h`, the reduction is diagonal. Conversely, opposite F3R2 orientations of the two hidden factors put one factor into the `g` support and the other into the `h` support.

`QED`.

Classification:

`THEOREM / EXACT`.

### Corollary 6.1 — alignment observability collapses directly to endpoints

The factor-blind computation

`u=gcd(N,g(A))`, `v=gcd(N,h(A))`

decides hidden split alignment.

But in the positive case it simultaneously outputs

`{u,v}={p,q}`.

Thus, at the accepted F3R2 invariant interface,

`N_SPLIT_BRIDGE_OBSERVABLE -> ENDPOINTS_ALREADY_EXTRACTED`.

There is no additional BRC endpoint mechanism in this test.

---

## 7. B2 candidate collapse objects and why the canonical ones are degenerate

The most immediate factor-blind residues are

`C_g(A,N)=g(A) mod N`

and

`C_h(A,N)=h(A) mod N`.

For `N=pq`,

`C_g` has one-sided CRT vanishing iff

`1<gcd(N,g(A))<N`.

Likewise for `C_h`.

So they satisfy the formal target event

`C=0 mod p, C!=0 mod q`

or the symmetric version exactly when a hidden factor divides the corresponding coefficient gcd.

However the extraction map is simply

`gcd(C_g,N)=gcd(g(A),N)`

or

`gcd(C_h,N)=gcd(h(A),N)`.

Nothing balanced, iterative, or dynamical has created the singularity. The endpoint was already present as a common divisor between `N` and a public coefficient invariant.

Therefore:

`C_g, C_h = COUNTERMODEL_TO_NOVEL_COLLAPSE_INTERPRETATION`.

They are useful as exact diagnostics, but not as a new BRC bridge mechanism.

Classification:

`MODEL / DEGENERATE / PRIOR-ART-EQUIVALENT_TO_DIRECT_GCD`.

---

## 8. B3 — symmetry obstruction, stated at the correct strength

A pure hidden-label exchange

`p <-> q`

does **not** by itself forbid unordered factor recovery.

Factor-blind classical mechanisms can produce a public integer whose residue vanishes in exactly one hidden channel without ever naming that channel. Therefore the statement

`factor-blind + p/q symmetric => factoring impossible`

would be false and is not claimed.

What symmetry does forbid is a canonical **labeled orientation**:

a factor-blind rule cannot intrinsically declare “the p-channel is the collapsing side” rather than “the q-channel” when the labels are only verifier names.

The actual necessary primitive for endpoint extraction is stronger and operational:

### DEFINITION 8.1 — channel discriminator

A public factor-blind response `C_lambda(A,N)` is a channel discriminator when its CRT zero-status vector is nonconstant:

`(1_{p|C_lambda}, 1_{q|C_lambda}) in {(1,0),(0,1)}`.

Once such a response exists,

`gcd(C_lambda,N)`

extracts a nontrivial endpoint.

Therefore the missing ingredient is not a factor label but a mechanism that **creates channel-selective vanishing** from factor-blind public data.

Current F3R2 gives:

- a factor-blind survivor boolean;
- factor-blind coefficient invariants `g,h`;
- factor-aware explicit support witnesses `q_{r,s}`;
- no canonical new channel discriminator distinct from the degenerate coefficient projections.

Classification:

`THEOREM_BOUNDARY / MODELING_CHOICE`.

---

## 9. B4 — rank-two hidden-semiprime classification

For `A in GL_2(Z)` and `N=pq`, use

`S = [g>1 and h>1]`,
`u=gcd(N,g)`,
`v=gcd(N,h)`.

### Class 0 — NONSURVIVOR

Condition:

`not S`.

Interpretation:

No accepted F3R2 coefficient-support bridge exists.

Endpoint statement:

No conclusion about other factorization mechanisms.

### Class 1 — SURVIVOR / HIDDEN UNALIGNED

Condition:

`S`, `u=1`, `v=1`.

Interpretation:

A coefficient support-splitting witness exists for some primes dividing `g,h`, but neither hidden target factor is among them.

Endpoint statement:

F3R2 survivor membership says nothing about the factors of `N`.

### Class 2 — SURVIVOR / ONE HIDDEN FACTOR DIRECTLY EXPOSED

Condition:

exactly one of `u,v` is a proper nontrivial divisor of `N`, the other is `1`.

Interpretation:

One hidden factor appears in one coefficient-support side, but there is no two-hidden-channel F3R2 split.

Endpoint statement:

A factor is already recovered by direct Euclidean gcd.

This is endpoint recovery **without** a balanced p/q bridge.

### Class 3 — SURVIVOR / BOTH HIDDEN FACTORS SAME ORIENTATION

Condition:

`u=N, v=1`

or

`u=1, v=N`.

Interpretation:

Both hidden factors divide the same cross-gcd invariant, so both CRT channels see the same F3R2 monomial orientation.

Endpoint statement:

The canonical invariant gives only gcd `N`, not a proper endpoint. The current theorem supplies no new channel discriminator.

### Class 4 — HIDDEN SPLIT / DIRECT ENDPOINTS

Condition:

`1<u<N` and `1<v<N`.

Interpretation:

The two hidden factors occupy opposite F3R2 support sides and see opposite monomial orientations.

Endpoint statement:

`{u,v}={p,q}` immediately. The bridge-alignment test is already the extraction.

This is the strongest exact hidden-CRT statement derivable from the accepted invariants, but it is not a new endpoint algorithm.

---

## 10. B5 — exact counterexamples

All matrices below have determinant `+-1`.

### Counterexample A — survivor but no multiplicative bridge to the chosen N

`A=[[-4,-3],[-3,-2]]`

has

`g=2`, `h=3`,

so it is an exact F3R2 survivor.

For

`N=35=5*7`,

`u=gcd(35,2)=1`,
`v=gcd(35,3)=1`.

Hence:

`SURVIVOR(A)`

but

`not N_SPLIT_BRIDGE(A,35)`.

This refutes

`F3R2 survivor => bridge between arbitrary hidden factors of N`.

### Counterexample B — both hidden factors lie on the same F3R2 side

`A=[[-35,-68],[-18,-35]]`

has determinant `1`,

`g=35`, `h=2`.

For `N=35`,

`u=35`, `v=1`.

Both mod-5 and mod-7 reductions are anti-diagonal monomial. There is no opposite p/q orientation and no proper gcd endpoint from the canonical pair `(g,h)`.

This refutes

`hidden factors appear in survivor support => they are support-split`.

### Counterexample C — endpoint without a balanced hidden split

`A=[[-5,-6],[-4,-5]]`

has determinant `1`,

`g=5`, `h=2`.

For `N=35`,

`u=5`, `v=1`.

The factor `5` is recovered immediately from `gcd(N,g)`, but the other hidden factor is not represented on the opposite F3R2 side.

This refutes

`endpoint recovery => balanced p/q bridge`.

### Positive alignment example — split exists but endpoints are already direct gcds

`A=[[-10,-7],[-7,-5]]`

has determinant `1`,

`g=5`, `h=7`.

For `N=35`,

`u=5`, `v=7`.

Mod 5 the matrix is anti-diagonal monomial; mod 7 it is diagonal monomial.

This is an exact hidden split, but the factor-blind alignment computation has already returned both factors.

---

## 11. Implication diagram

The exact implication structure is:

```text
F3R2_SURVIVOR(A)
    <=> COEFF_BRIDGE(A)
    -> EXISTS factor-aware prime-pair witness (r|g, s|h)
    -/-> N_SPLIT_BRIDGE(A,N)
    -/-> FACTOR_BLIND_EXPLICIT_q_{r,s}
    -/-> ONE_SIDED_LINEAR_COLLAPSE_BY_A

N_SPLIT_BRIDGE(A,N)
    -> F3R2_SURVIVOR(A)
    <=> [1<gcd(N,g)<N and 1<gcd(N,h)<N]
    -> {gcd(N,g), gcd(N,h)} = {p,q}
    -> ENDPOINTS_EXTRACTED_BY_DIRECT_GCD

DIRECT_ENDPOINT(A,N)
    -/-> N_SPLIT_BRIDGE(A,N)

CHANNEL_DISCRIMINATOR C_lambda
    -> 1<gcd(C_lambda,N)<N
    -> ENDPOINT_RECOVERY
```

The missing nontrivial arrow is:

```text
F3R2_BALANCED_STRUCTURE
    ?-> NEW_FACTOR_BLIND_CHANNEL_DISCRIMINATOR
```

F3R2 does not currently supply it.

---

## 12. Exact finite checker

Checker:

`research_checks/BRC_COPRIME_FIBER_BRIDGE_CLASSIFICATION_CHECK_20260829.py`

The checker uses exact integer arithmetic only.

Bounded domain:

- all unimodular `2x2` integer matrices with entries in `[-16,16]`;
- semiprimes from distinct pairs in `{3,5,7,11}`;
- four explicit regression examples above.

Observed exact regression counts:

- bounded unimodular matrices: `5096`;
- bounded F3R2 survivors: `384`;
- matrix-semiprime pairs: `30576`;
- hidden-split cases: `32`;
- direct-endpoint cases: `4640`;
- both-hidden-factors-same-orientation cases: `112`;
- survivor/hidden-unaligned cases: `1120`;
- assertion failures: `0`.

The checker verifies:

1. `gcd(g,h)=1` for every bounded unimodular matrix;
2. a split pair of proper `u,v` necessarily multiplies to `N` and equals the hidden prime set;
3. split cases have anti-diagonal orientation on the `g`-side factor and diagonal orientation on the `h`-side factor;
4. same-side cases give the same monomial orientation in both hidden channels;
5. `A` remains invertible modulo every tested semiprime;
6. one-sided zero-status of the coefficient projections is exactly equivalent to proper Euclidean gcd with `N`.

Finite enumeration is regression evidence only. The arbitrary-integer claims above rest on the exact proofs.

---

## 13. Required-output disposition

### B0 Semantic translation

`COMPLETE`.

The exact/analogy/not-justified boundary is frozen.

### B1 Bridge-existence theorem

`COMPLETE_AT_TWO_LEVELS`.

- coefficient-support bridge existence is exactly F3R2 survivor membership;
- hidden-N split alignment has an exact factor-blind criterion, but that criterion immediately exposes endpoints.

### B2 One-sided collapse object

`NEGATIVE_BOUNDARY`.

The balanced operator `A` cannot collapse linearly because it is unimodular.

The only canonical factor-blind collapse residues supplied by current invariants are `g mod N` and `h mod N`, which reduce directly to Euclidean gcd and are rejected as a genuinely new BRC collapse primitive.

### B3 Symmetry obstruction

`COMPLETE_WITH_CORRECTION`.

Hidden label symmetry blocks labeled channel orientation, not unordered factor recovery. The necessary primitive is channel-selective vanishing, which can in principle arise factor-blindly.

### B4 Rank-two classification

`COMPLETE`.

Five exact classes are given.

### B5 Counterexamples

`COMPLETE`.

Survivor-without-N-bridge, same-side-hidden-support, endpoint-without-balanced-split, and positive split examples are all explicit.

---

## 14. Final mathematical classification

The accepted F3R2 structure should be called:

`FACTOR_BLIND_DECIDABLE COEFFICIENT-SUPPORT BRIDGE EXISTENCE`

with

`FACTOR_AWARE EXPLICIT SUPPORT WITNESS`.

It should **not yet** be called:

`FACTOR_BLIND HIDDEN-CRT COLLAPSE BRIDGE`.

The exact obstruction is structural, not merely computational:

1. the balanced matrix is invertible in every CRT channel;
2. its survivor theorem selects coefficient-support orientations, not target-factor channels;
3. coupling those supports to `N` through the canonical gcd interface either misses the hidden factors, places them on the same side, or directly reveals them by ordinary gcd;
4. no new public channel-discriminating response is present in the current axioms.

Therefore the next worthwhile mathematical object is:

`NEW_BRC_DERIVED_NONINVERTIBLE_OR_NONLINEAR_CHANNEL_DISCRIMINATOR`

subject to:

- factor-blind precommitment;
- no `|p-q|`, Fermat offset, additive-distance, or factor-edit metric;
- no hidden factor labels in operator selection;
- explicit proof that the response is not algebraically equivalent to `gcd(N,g(A))`, `gcd(N,h(A))`, or another classical direct coefficient-gcd exposure.

Only after such a discriminator exists does a separate endpoint-recovery algorithm become mathematically distinct from the coefficient-support classifier.

No competitive factorization claim is made.

No Working Truth, Foundation truth, or canonical theorem promotion is requested by this return.
