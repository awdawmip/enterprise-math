# N-Coupled Asymmetric Singularization Primitive — Research Return

Researcher-ID: `EM-NCAS1-5F7A3C`
Task: `RS-N-COUPLED-ASYMMETRIC-SINGULARIZATION-PRIMITIVE`
Publication: `TP2-4A71C8D2E9065F3B1C44`
Claim: `chatgpt-ncas1-20260830-1031-5f7a3c`
Execution record: `ER-B526CD89EBB2F9F5AD68`

## 1. Terminal verdict

`SUCCESS / DECLARED_GRAMMAR_OBSTRUCTED`

Hard target disposition:

`N_COUPLED_ASYMMETRIC_SINGULARIZATION_PRIMITIVE_CONSTRUCTED_OR_DECLARED_GRAMMAR_OBSTRUCTED = DECLARED_GRAMMAR_OBSTRUCTED`.

The obstruction is exact for the frozen first-round grammar below. It is **not** a universal no-go for BRC/CBRC, and it does not prove that every public factor-blind asymmetric singularization mechanism is impossible.

The main result is stronger than a failed search:

> In any fixed finite-step grammar whose state and operators are built inside `Z/NZ` from fixed-dimensional matrices/tensors, fixed integer constants, the public scalar `N`, ring operations, fixed-denominator unit-safe rational coefficients, and fixed matrix/tensor contractions, all explicit dependence on `N` is erased modulo `N`. Every hidden CRT channel therefore sees only the reduction of one `N`-independent integral/rational object. One-sided rank singularity can occur only at the finite prime support of the corresponding determinantal divisors, and whenever it occurs its factor is already recovered by an ordinary gcd with that fixed support integer.

Consequently, after the accepted prior-art guard removes fixed support-prime schedules/direct coefficient-support gcds, this grammar has no surviving asymmetric singularization primitive.

## 2. Frozen candidate grammar `G_poly-loc`

Fix once and for all:

- a finite state dimension and finite number `T` of update steps;
- finitely many matrix/tensor slots over `R_N = Z/NZ`;
- fixed integer constants;
- the public scalar `N`;
- `+,-,*`, fixed matrix multiplication, tensor product/contraction and fixed polynomial expressions;
- optionally fixed rational denominators from a finite set `D`, under the declared admissibility condition that every `d in D` is coprime to the tested `N`;
- determinant/minor/rank/nonunit observables of fixed matrix flattenings.

Excluded from `G_poly-loc`:

- branching on gcd/nonunit/rank outcomes;
- factor-aware or candidate-prime selectors;
- variable-time loops whose iteration count depends on `N` or an evolving state;
- exponent/order annihilation;
- canonical-integer-representative, floor, quotient/remainder or carry operations not expressible as a fixed ring term;
- generic collision/rho or congruence-of-squares mechanisms;
- division by a quantity not certified a unit on the declared family.

The pre-state may be chosen CRT-invertible; in particular `X_0=I_d` is allowed. The theorem applies to every state and every fixed observable produced by the grammar.

## 3. Lemma A — exact `N`-erasure

Let `E(N)` be any scalar entry produced by `G_poly-loc` before reduction modulo `N`. After clearing the fixed admissible denominators, `E(N)` is an integer polynomial in `N`. Hence

`E(N) - E(0)` is divisible by `N`,

so in `R_N`

`E(N) = E(0)`.

For a fixed denominator `d` with `gcd(d,N)=1`,

`P(N)/d = P(0)/d  (mod N)`

because `d` is invertible in `R_N`.

Structural induction over the fixed computation proves the same statement entrywise for every matrix/tensor state and every fixed polynomial observable:

`STATE_t(N) = STATE_t(0)  in R_N`.

Thus the advertised `N`-coupling is algebraically erased inside this grammar. Multiplication by `N` gives zero on **both** CRT channels; adding `N` changes neither channel; `N+1` is `1`; and no finite composition of such ring terms repairs the loss.

## 4. Lemma B — CRT product naturality

For `N=pq` with distinct odd primes,

`R_N ~= F_p x F_q`.

Every fixed commutative-ring term commutes with this product decomposition. Combining this with Lemma A, any matrix observable `M_t(N)` has hidden-channel images

`M_t(N) mod p = M_t(0) mod p`,

`M_t(N) mod q = M_t(0) mod q`.

The two channels are not coupled by the grammar. They are two characteristic reductions of the same `N`-independent object.

This is the exact point at which the first-round candidate grammar fails to generate a new hidden selector. A future positive mechanism must break this product-natural / `N`-erasing interface somewhere.

## 5. Theorem C — determinantal-divisor support theorem

First take an integral matrix observable `B=M_t(0) in Mat_{m x n}(Z)`. Let

`k = rank_Q(B)`.

If `k=0`, every prime reduction has rank zero, so no one-sided rank pattern exists.

If `k>0`, define the top nonzero determinantal divisor

`delta_k(B) = gcd{|det B[I,J]| : |I|=|J|=k}`.

At least one `k x k` minor is nonzero over `Z`, so `delta_k(B)>0`.

For every prime `r`:

`rank_{F_r}(B mod r) < k`

iff every `k x k` minor vanishes modulo `r`,

iff

`r | delta_k(B)`.

All `(k+1) x (k+1)` minors are already zero over `Z`, so the modular rank can never exceed `k`. Therefore the rank law is exact.

For fixed-denominator localized matrices, clear a common denominator `d` with `gcd(d,N)=1`; multiplication by this unit does not change hidden-channel rank. The same theorem applies to the cleared integral matrix.

### CRT consequence

For `N=pq`, one-sided rank drop occurs exactly when

`p | delta_k(B), q not| delta_k(B)`

or vice versa.

In that case

`gcd(N, delta_k(B))`

is exactly the hidden factor on the singular side.

So every one-sided rank singularity in `G_poly-loc` is a **fixed determinantal-support event**. The matrix layer does not contain an information type beyond the ordinary support gcd.

For a determinant observable this specializes to the simpler law with `delta=|det B|`.

## 6. Corollary D — finite-support adversarial family

A fixed finite computation has only finitely many declared rank/minor observables. Let `S_G` be the finite set of primes dividing:

- the fixed admissible denominators; and
- the nonzero top determinantal divisors of all `N=0` specialized observables.

Choose any two distinct odd primes `p,q notin S_G` and set `N=pq`. Then every declared matrix observable has the same generic rank on both hidden channels. No proper nonempty rank-singularity pattern occurs at any step.

There are infinitely many such semiprimes because `S_G` is finite.

Conversely, any infinite semiprime family on which `G_poly-loc` does exhibit one-sided rank singularity must contain a factor from the finite set `S_G` infinitely often. By pigeonhole, some fixed support prime is being repeatedly tested. This is exactly the candidate-prime/static-support mechanism class excluded by the accepted Driver prior-art guard.

Therefore:

`G_poly-loc + PRIOR_ART_CLEAN_FAMILY => NO_ONE_SIDED_RANK_SINGULARIZATION`.

## 7. Corollary E — the R059D complementary selector cannot be generated here

R059D freezes the local complementary-collapse normal form

`C(n;b)=L+(U-L)b`, with `b^2=b`,

but leaves the selector source unresolved.

Suppose `G_poly-loc` produces a scalar idempotent selector. After `N`-erasure and clearing a fixed unit denominator, write

`b = a/d  (mod N)`, `gcd(d,N)=1`,

with fixed integers `a,d` independent of the hidden factors.

The idempotence law gives

`b(b-1)=0 (mod N)`

iff

`N | a(a-d)`.

A nontrivial CRT selector has channel values `(0,1)` or `(1,0)`. Hence, up to swapping `p,q`,

`p | a` and `q | (a-d)`.

Therefore

`gcd(N,a)=p`,

`gcd(N,a-d)=q`.

The selector itself is already a static endpoint certificate. It does not solve the missing R059D selector problem without prior support exposure.

In the pure integer-polynomial subgrammar, `b=f(N)` satisfies the even simpler identity

`b = f(0) (mod N)`.

A fixed polynomial selector can therefore be nontrivial only on semiprimes supported by the finite prime divisors of `f(0)(f(0)-1)`. On every cofinite prime family, an everywhere-idempotent fixed polynomial has only the trivial selectors `0` or `1`.

This gives an exact task-local selector obstruction rather than a symmetry slogan.

## 8. Why exchange symmetry alone was not used as the proof

The current toolbox contains finite symmetry/equivariance machinery, and R059D explicitly warns about a stateless deterministic branch selector under transverse exchange symmetry. That boundary is relevant, but it is insufficient for the present hard target.

Swapping the hidden labels `p<->q` does **not** by itself forbid an unlabeled asymmetric outcome: a construction could in principle produce the orbit `{singular, nonsingular}` without canonically naming which side is `p`.

Accordingly, no impossibility claim here is derived merely from `p/q` symmetry. The actual obstruction is the stronger `N`-erasure plus determinantal-support theorem.

## 9. Exact mechanism classification

### Candidate 1: `diag(N+c,1)`

Modulo every hidden factor, `N+c` becomes `c`.

- For `N=15,c=3`, the matrix is singular mod `3` and invertible mod `5`.
- But `gcd(15,3)=3` already exposes the endpoint.

Classification: `PRIOR_ART_EQUIVALENT / FIXED_SUPPORT_PRIME`.

### Candidate 2: `diag(N+1,1)`

Both channels see the identity diagonal.

Classification: `BILATERALLY_INVERTIBLE / NO_COLLAPSE`.

### Candidate 3: `N I_d`

Both channels see zero.

Classification: `BILATERAL_COLLAPSE / NOT_SELECTIVE`.

### Candidate 4: fixed unimodular completion

A fixed `GL_d(Z)` operator remains invertible modulo every prime.

Classification: `NO_SELECTIVE_COLLAPSE`, consistent with the accepted BRC boundary.

### Candidate 5: nontrivial idempotent generated as a fixed polynomial/rational ring term

When it exists, its fixed numerator/support already splits `N` by gcd as proved above.

Classification: `STATIC_CRT_IDEMPOTENT / ENDPOINT_ALREADY_ENCODED`.

### Outside the frozen grammar

- variable exponent/order dynamics can make residues depend on hidden group order, but the accepted guard requires classification against Pollard/Williams/order-annihilation prior art;
- generic collision or congruence-of-squares leaves this grammar but is already prior-art bounded;
- factor-aware/nonunit-conditioned branching is not a valid selector source if the branch predicate has already recovered the nonunit endpoint;
- history/context/completion state remains a genuine unresolved route **only if** it breaks `N`-erasure without first exporting a direct support gcd.

## 10. Deterministic exact checker

Checker:

`research_checks/N_COUPLED_ASYMMETRIC_SINGULARIZATION_PRIMITIVE_CHECK_20260830.py`

Certificate:

`research_artifacts/N_COUPLED_ASYMMETRIC_SINGULARIZATION_PRIMITIVE/exact_regression_certificate.json`

Executed result: `PASS`.

Regression envelope:

- `2401` integral `2x2` base matrices with entries in `[-3,3]`;
- `8` fixed affine `N`-coefficient patterns each;
- `19208` affine matrix templates total;
- `28` semiprimes from the eight odd primes `3,5,7,11,13,17,19,23`;
- `537824` channel-pair rank checks;
- `72960` observed one-sided support cases;
- `0` support-law mismatches;
- `5628` scalar selector checks;
- `170` nontrivial idempotent cases in the finite selector window;
- `0` selector endpoint-law mismatches.

The checker also freezes the three explicit controls `diag(N+3,1)`, `diag(N+1,1)` and `N I`.

The finite checker is only a regression/certificate. The all-grammar result is the symbolic proof in Sections 3–7.

## 11. Tool/method reuse resolution

### `T0_BRC`

- coverage verdict: `REUSE_EXISTING_TOOL`
- reuse state: `REUSE_APPLIED`
- application: preserved the exact separation between public support structure, hidden-channel selective collapse and endpoint readout; used the accepted rule that renaming direct gcd/support exposure is not a new singularization layer.
- hard boundary checked: no erased provenance or support witness is promoted into hidden-target collapse.

### R059D pure-algebra complementary collapse

- coverage verdict: `COMPOSE_EXISTING_TOOLS`
- reuse state: `COMPOSE_APPLIED`
- application: reused the frozen `b^2=b` complementary-collapse interface as the downstream selector target; proved that `G_poly-loc` cannot generate a nontrivial selector without static endpoint support.
- hard boundary checked: the selector is not assumed or manually injected.

### `T7_FINITE_SYMMETRY_EQUIVARIANCE`

- coverage verdict: `REUSE_EXISTING_TOOL`
- reuse state: `REUSE_APPLIED_AS_GUARD`
- application: used only to prevent an invalid canonical-choice inference. Exchange symmetry was explicitly **not** treated as a proof that unlabeled asymmetry is impossible.
- hard boundary checked: no canonical hidden label is inferred from symmetry.

### Prime toolkit / quotient / collision tools

- reuse state: `NOT_APPLICABLE` to the proof core.
- reason: this return neither benchmarks a factoring algorithm nor constructs a predictive quotient/collision mechanism; gcd appears only as an exact mechanism-classification readout.

No new global tool family is proposed. Method-harvest classification: `RESULT_ONLY`.

## 12. Smallest surviving extension

The exact missing capability is now sharper than “try a more nonlinear matrix.”

A successor must introduce at least one public operation/state whose semantics do **not** factor as a fixed ring term under

`Z/NZ ~= F_p x F_q`

and therefore is not erased by `N=0` in both channels.

Candidate semantic forms include:

1. explicit history/context state whose evolution depends on a residue-sensitive event;
2. a non-ring completion operation with a canonical rule not reducible to fixed support, order annihilation, generic collision or congruence-of-squares;
3. a variable-time/nonlinear process whose generated state is not a fixed polynomial/rational function of `N` — but it must survive the classical order/collision guard;
4. a typed non-scalar selector source whose scalar projections remain units before coupling, so the selector is not already a direct gcd witness.

The recommended next hard target is:

`CRT_PRODUCT_NATURALITY_BREAK_WITHOUT_SCALAR_SUPPORT_EXPOSURE`.

That target should be tested directly against the R059D complementary-collapse bit interface. The key condition is not merely “nonlinear”; it is **non-`N`-erasing and non-support-revealing before the selective-collapse layer**.

## 13. Scope firewall

This return proves only the obstruction for `G_poly-loc` and its fixed finite observables. It does not establish:

- impossibility of all factor-blind hidden-channel singularization;
- impossibility of stateful/history-dependent BRC/CBRC;
- a lower bound for integer factorization;
- novelty of any proposed successor mechanism;
- Foundation, Working Truth or canonical theorem status.

It does establish that simply adding more fixed `N`-polynomial coefficients, more fixed-dimensional matrices, more finite ring compositions, or more unit-safe fixed rational coefficients cannot solve the open residue. That entire first layer collapses to static determinantal support.
