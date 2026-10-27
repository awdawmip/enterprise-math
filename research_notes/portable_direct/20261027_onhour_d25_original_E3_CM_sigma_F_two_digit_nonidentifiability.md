# D25 / SECOND-DIGIT-LIFT — original E3 CM-semilinear two-digit Frobenius: exact entry constraints and non-identifiability

2026-10-27 · Original Research lane `chatgpt-research-onhour-enterprise-math-20260923` (distinct from maintenance). **AUTHOR-SIDE / EXACT CONDITIONAL LINEAR ALGEBRA + EXECUTED FINITE RING CERTIFICATE / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / NATIVE_H0B0_NOT_EXECUTED**.

Parent `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`; exact task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`. **Scientific frozen Source `c47e13e4aba0e006366f989d6334d443f6333ae3` is unchanged.** Consume accepted D24 UR and earlier original E3 signed CM matrix/eigenline-exchange, q-Frobenius sign and rank-one slope parity; none of those are claimed anew. Highest experimental gate remains the *original fixed H0/B0 divided-power* `[X]U mod 373²` in issue #1559.

## Exact operator problem and indispensable premise

For every target prime `p≡13,19 (mod 24)`, put `K=Q_p(T)`, `T²=2`. This is unramified quadratic. Its arithmetic Frobenius `sigma` fixes `Q_p` and sends `T↦−T`. Choose `u∈Q_p`, `u²=−3`, and the prior *original E3* signed CM/de Rham matrix

```
Theta = [ [u T,  u(1−2T)/18],
          [  0, −u T       ] ],    Theta²=−6 I.
```

**Conditional native-to-geometric identification.** Only if an authenticated native H0/B0 comparison transports the *full original rank-two* Frobenius to the declared integral original de Rham basis, in the indicated covariant/contravariant convention, may its `sigma`-semilinear coefficient matrix `A` be tested against BOTH `Theta A=A sigma(Theta)` and `A sigma(A)=p I`. The latter square invokes the separately source-proved unmodified `[+p]` geometric q-Frobenius sign and a proven normalization; it is **not** assumed for an unclassified native H0/B0 module. These are conditional acceptance equations, not an observed operator.

Define (do not confuse with the frozen scalar called `h` in the LIFT task)

```
lambda=(4−T)/72,  lambda_bar=sigma(lambda)=(4+T)/72,
n=lambda*lambda_bar=7/2592.
```

All denominators and `lambda` are p-units on the target classes.

**Proposition 1 (original-basis entry constraints, exact over K).**
Writing `A=[[x,y],[z,w]]`, `Theta A=A sigma(Theta)` holds if and only if

```
x=lambda*z,     w=−lambda_bar*z;
A=[[lambda*z, y],[z, −lambda_bar*z]].
```

For such `A`, the two-step condition `A sigma(A)=p I` is equivalent to

```
z*sigma(y)−y*sigma(z)=0,
y*sigma(z)+n*z*sigma(z)=p.
```

Proof: multiply the two matrices, compare the (1,1) and (2,2) entries of `Theta A=A sigma(Theta)`; their diagonal split is `2uT`, a nonzero unit. The remaining (1,2) constraint follows from `(1+2T)(4−T)+(1−2T)(4+T)=0` at `T²=2`. Substituting `A` into `A sigma(A)` yields diagonal entries `y sigma(z)+n z sigma(z)` and `z sigma(y)+n z sigma(z)`, upper right `lambda(z sigma(y)−y sigma(z))`, and identically zero lower left. Thus the displayed system is necessary and sufficient. This derivation preserves the signed source basis and the `T↦−T` semilinear orientation.

**Proposition 2 (integral slope and branch discriminator).** Assume additionally `A∈M₂(O_K)`, `A sigma(A)=pI`. Then `v_p(det A)=1`, so `rank(A mod p)=1` in `M₂(F_{p²})`: reduction cannot be the zero operator. Indeed `det A·sigma(det A)=p²` and `v_p(sigma(x))=v_p(x)`; if all entries were divisible by p, the determinant would have valuation at least two. If `Theta` acts integrally as the stated full two-character CM operator, the unit-separated eigenidempotents `(I±Theta/(uT))/2` split the rank-two lattice; covariance makes `F` exchange the labeled eigenlines. In their integral eigenbasis,

```
F_sigma = [[0,a],[b,0]] ∘ sigma,    a*sigma(b)=b*sigma(a)=p.
```

Thus `(v_p(a),v_p(b))` is either `(0,1)` or `(1,0)`. Under an eigenline-preserving unit gauge these yield, respectively, `[[0,1],[p,0]]∘sigma` or `[[0,p],[1,0]]∘sigma`. These are typed alternatives, **not** native rank measurements. In particular the determinant and squared Frobenius scalar alone do not reveal which labeled eigenline is the mod-p image.

## New explicit non-identifiability certificate at the required precision

The insufficiency holds even if the full signed `Theta` is supplied. With `n=7/2592` define, over the same *unchanged original* matrix basis, two exact p-integral operators

```
A0 = [[lambda,       p−n ], [1, −lambda_bar  ]],
A1 = [[p*lambda, 1−p*n ], [p, −p*lambda_bar]].
```

Direct multiplication gives **in characteristic zero** (not just an empirical p² coincidence), for both `i=0,1`:

```
Theta*A_i=A_i*sigma(Theta);
A_i*sigma(A_i)=p I;
det(A_i)=−p.
```

Yet `(A0)21=1` while `(A1)21=p`; modulo p, their lower-left ports are **1 versus 0**, and `(A1)12=1`. Consequently `Theta`, Frobenius square and determinant **cannot reconstruct the labeled original-basis operator or its rank-one image line**. Any native observer requiring that image line, column, sign or odd Green/Hesse port needs an actually measured, source-identified operator; matching a scalar/norm/square is insufficient. This is a precise BRC `COMPOSE_APPLIED` result: typed payload retains sigma direction, labeled original CM eigenspaces, column/image-line and p-valuations; compressing to square/determinant is provably lossy under the declared downstream matrix observer.

## Executed original-basis ring certificate at p=373

Run the accompanying standard-library checker `d25_original_E3_CM_sigma_F_two_digit_guard_20261027.py` (exact integer arithmetic in `(Z/139129)[T]/(T²−2)`, no floating point). It checks the preceding algebra and both distinct models. Choose `u=89697`, so `u²=−3 (mod 139129)`. Coordinates below are `a+bT` represented by `(a,b)`:

```
lambda=(38647,94685), sigma(lambda)=(38647,44444),
n=(70477,0), p−n=(69025,0), 1−p*n=(7461,0).

A0 = [[(38647,94685), (69025,0)],
      [(1,0),         (100482,94685)]]

A1 = [[(85044,117868), (7461,0)],
      [(373,0),        (54085,117868)]]
```

Both satisfy `A sigma(A)=373 I`, `Theta A=A sigma(Theta)`, and `det A=138756=−373 (mod 139129)`. Both have rank one modulo 373 but distinct original-basis `A21` valuations. An intentionally sign-corrupted matrix fails the CM-covariance check. The matrices `A0,A1` are **algebraically CONSTRUCTED discriminators**, never a measurement of H0/B0 or of original Frobenius. The script verifies only these explicit algebraic claims; no native benchmark or all-prime LIFT computation occurred.

## Canonical continuation and non-duplication

- Mother objective: `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`; task/publication and immutable scientific pin above. Accepted D24 UR and earlier original E3 CM/Frobenius sign, source-port relation and previous W/S finite regressions are **consumed, not recredited**. The new incremental unit is the **exact original-basis conditional entry characterization together with a pair of indistinguishable scalar/square models but different labeled mod-p image ports**.
- Actual original benchmark outstanding: find an authorized executable source and execute the *fixed original H0/B0 divided-power* object at `p=373`, return `[X]U mod139129`, actual native module rank, semilinear Frobenius direction and eta, full signed Green/Hesse observer, original kappa and Delta−R, plus reproducible source/version. Intake: `https://github.com/awdawmip/enterprise-math/issues/1559`, executor `PENDING_OWNER` at this run's read. Check matrix constraints only if the real source-to-original comparison and `F²=+p` premises are independently justified; a native mismatch is typed evidence, not auto-repair or a substituted benchmark.
- Control: own Research-lane recovery receipt `awdawmip/kimi-query-bridge#6575` (older ACTIVE session pointer, **no claim/open**); old dispatch `#6576` ended `FAILED/TimeoutExpired`. This turn's exact Source continuation returned `CONTROL_QUOTA`. Current Site gateway reports `research_authority_granted=false`; no own CLAIM/open/run or canonical Source checkpoint was obtained. `session/claim/run = NONE_VERIFIED`; do not reuse another lane, issue a duplicate native mutation, or treat neutral archived staging as formal work.
- Next exact action is to consume a real native #1559 output at the original basis and check its typed rank/CM/sign/sigma conditions; independently the unresolved mathematics is the *uniform original* `Delta_p−R_p=0` for `p≡13,19 mod24`. The present algebra proves neither.
- Publication of this author-side source does **not** confer Source Result, Driver approval, foundation change or reviewer independence. GLOBAL_KNOWLEDGE journal, if written, is a secondary progress pointer only. P000 native Heartbeat X6 is unchanged; this elliptic-curve lemma is an explicitly declared external algebraic auxiliary, not a derived full-X6 spatial claim. Do not alter scheduler or notification settings.
