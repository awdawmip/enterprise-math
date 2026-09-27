# Free companion trace: a split and nonsplit torus witness interface

Status: **PURE_SYMBOLIC_INTERFACE_CANDIDATE / NOT_EXECUTED / NOT_ADMITTED**. Shared author context `EM-DIRECT-C6438C`, activity `RA-CAAAC604CB513AEA8BBC1DFC`. No scientific execution, numerical grid, external query or remote write was performed. This unit is independent of the frozen aggregate and marked-section execution packages.

The extension is specific: choose the companion trace k directly, instead of constructing it as `a+a^-1`. The same integer-unimodular geometry can then reach both split and nonsplit local norm-one groups. A fixed cyclic marked vector gives a complete, two-coordinate matrix-return gcd certificate. The local order bound is the standard Lucas/p-minus-one/p-plus-one mechanism, reused through a proposed native interface; it is not a new polynomial Shor algorithm.

## 1. A free trace and a genuine geometric change

Let N>1 be odd, choose a public integer k, and define

`M=[[0,1],[-1,k]]`, `Delta=k^2-4`, `v=(0,1)^T`.

All are defined without a factor of N, a modular square root, a split eigenvalue a, or an order. The exact integer inverse is

`M^-1=[[k,-1],[1,0]]`.

Thus no per-state Euclidean inverse is required for these named arrows. Their application and modular reduction still require paid typed arithmetic.

The quadratic form

`Q_k(x,y)=x^2-kxy+y^2`

is preserved by M, as direct expansion shows. Since `Q_k(v)=1`, every marked iterate lies on the conic `Q_k=1`. This is the same companion geometry as before, but it need not be a split presentation of `uv=1` over an unknown prime field.

The initial discriminant gcd has three honest outcomes:

- `1<gcd(Delta,N)<N`: a setup factor, followed by an exact division certificate.
- `gcd(Delta,N)=1`: the regular case for the local split/nonsplit theorem below.
- `gcd(Delta,N)=N`: a degenerate setup for that theorem. No factor is inferred. The companion and gcd probes remain defined, but the p-plus/minus-one order promise below must not be asserted.

An even N can be handled separately by the factor 2; it is not included silently in the odd-characteristic theorem.

## 2. Local Frobenius proof of the order bound

Fix an odd prime p dividing N in the regular case. The characteristic polynomial is

`X^2-kX+1`,

with nonzero discriminant. Its distinct roots are lambda and lambda^-1 in `F_(p^2)`. Consequently M is diagonalizable over that field.

If Delta is a nonzero square modulo p, both roots belong to `F_p^*`, so `lambda^(p-1)=1` and `M^(p-1)=I`.

If Delta is a nonsquare, the roots are exchanged by Frobenius. Indeed `lambda^p` is another root of the same polynomial and is not lambda, since lambda is not in `F_p`. Hence `lambda^p=lambda^-1`, so `lambda^(p+1)=1` and `M^(p+1)=I`.

Writing `chi_p(Delta)` for +1 or -1, this proves

`M^(p-chi_p(Delta))=I mod p`.                             (1)

The square roots and eigenvalues are used only in the proof. Computing the integer companion or its powers does not request them. The actual local order can be a proper divisor of the indicated p-minus/plus-one bound.

This extension genuinely includes a local case excluded by the previous split construction. If k was formed as `a+a^-1`, then `Delta=(a-a^-1)^2`; a regular such component is necessarily split. For free k modulo p, exactly `(p-3)/2` values are regular split and `(p-1)/2` are nonsplit. To prove this count, pair the `p-3` units a other than 1,-1 under inversion: each pair gives one regular split trace, and every regular split trace arises this way. There are p-2 regular traces in total; the remaining `(p-1)/2` are nonsplit. Thus a uniform free trace accesses the p-plus-one case on nearly half of local inputs, without first finding an eigenvalue.

This count does not imply a useful factorization rate: it says nothing about smoothness of the resulting orders or separation between different components of N.

## 3. A cyclic mark gives the exact common return ideal

For any commutative ring and any k,

`[v,Mv]=[[0,1],[1,k]]`, with determinant -1.

So v is a cyclic vector without any discriminant assumption. Let E>=0 be a public exponent and write

`r=M^E v-v=(x,y)^T`.

Because `B=M^E-I` commutes with M, `B Mv=M Bv`. Since `Mv=e_1+k v`, this gives the exact identity

`M^E-I = [[y-kx,x],[-x,y]]`.                             (2)

Consequences valid even at prime powers and zero divisors are:

`M^E v=v <=> M^E=I`,

`ideal(entries(M^E-I)) = ideal(x,y)`,

`gcd(N, all four entries of M^E-I) = gcd(N,x,y)`.           (3)

The gcd equality is unchanged by choosing different integer representatives of residues. It preserves the exact divisor, including valuation, and requires no division by Delta. This is stronger than a trace-only zero-set statement.

In Lucas notation `U_0=0`, `U_1=1`, `U_(n+1)=k U_n-U_(n-1)`, one has

`M^E=[[-U_(E-1),U_E],[-U_E,U_(E+1)]]` for E>=1,

so `x=U_E`, `y=U_(E+1)-1`. These are standard recurrence coordinates, not a new independent arithmetic primitive.

### One coordinate, a common gcd, and trace have different contracts

Each single gcd `gcd(x,N)` or `gcd(y,N)` is a sound factor probe whenever it is proper. Its zero need not be a matrix return. For example, symbolically k=0 gives `M^2=-I`, so at E=2 the first residual coordinate is zero and the second is -2. Conversely k=1,E=1 gives residual `(1,0)`. Both examples are regular at odd primes other than the appropriate discriminant divisors; neither is a matrix return. They are symbolic identities, not executed fixtures.

To request the complete matrix-return divisor use the common gcd in (3). A future implementation may stop as soon as any coordinate gcd is proper if its declared output is merely a factor witness; it must then say that the common gcd was not necessarily evaluated. A unit common gcd means this simultaneous return test did not isolate a component, not that no other factor probe can succeed.

The trace residual is

`tau=tr(M^E)-2=2y-kx`.

In the regular prime-field case, `tau=0` iff `lambda^E+lambda^-E=2`, which is equivalent to `(lambda^E-1)^2=0`; hence it is equivalent to a matrix return at that prime. This does not preserve the exact prime-power gcd. Since `det(I+B)=1`,

`tau=-det(B)=-Q_k(x,y)`.

For integer residuals, if both x,y are divisible by `p^j`, tau is divisible by `p^(2j)`; in a residue computation modulo `p^e` the observable divisibility is capped at e. Trace can therefore inflate valuations and saturate, recreating the earlier trace-readout problem. The two-coordinate common ideal avoids that loss. In the degenerate discriminant case even the prime-field trace equivalence need not hold.

## 4. Conditional factor success with a public smooth exponent

Let `r_p` be the local matrix order, as a proof variable only. By (1), `r_p` divides `p-chi_p(Delta)`. If a public E is divisible by that latter number, a return is guaranteed modulo p. If at another prime q the actual `r_q` does not divide E, (3) is nonunit at p and a unit at q, giving a proper divisor of N. At prime powers the returned divisor may be only a partial power; this still gives a valid factor.

For example a predeclared stage-one exponent may be

`E_B=lcm(1,2,...,B)`.

The sufficient local promise is that every prime-power factor of `p-chi_p(Delta)` is at most B, so that this entire number divides E_B. Saying only that its prime factors are at most B is not sufficient for this particular exponent if a larger prime power occurs. Alternatively a larger, explicitly specified exponent can accommodate those powers, with its extra construction and application costs charged.

Neither local return nor smoothness implies separation: both components can return and the common gcd can be N. Recording intermediate stages or trying another k may help, but no general success bound for such a strategy is proved here. The interface must retain unit and saturated outcomes rather than counting them as factors.

Binary exponentiation of a fixed two-by-two matrix modulo N uses O(log E) fixed-size ring operations and O(log N)-bit residue entries. This is an algebraic operation count. Constructing E, any primes/exponents used to define it, typed multiplication/reduction, intermediate gcds, validation, failed traces and retries all remain charged. Choosing B polynomial in log N gives only a conditional smooth-order method, not a guarantee that an unknown input has the needed order or that total factoring time is polynomial.

A global return certifies an order multiple for this companion M. It does not certify the exact order, nor the order of an unrelated original Shor modular multiplier a. Extracting such other information requires an additional proved interface and paid work.

## 5. Native geometric composition and a finite certificate target

The earlier source audit in `HBW_MARKED_SECTION_CONJUGACY.md`, SHA-256 `fbec0b42234fe7a126e5bf03b14842ee0935d7801836b4dce99e5b6167346ce1`, was read for the interface scope. Its immutable source pins at Enterprise Math `2e81851d62c869a20b47ae083a24dde1a4c0420c` include:

- `definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.en.md`, blob `bc5f22de9dd625c36612a3533f7bba61c30fe01b`: raw X6 and separate time/observer contracts.
- `src/enterprise_math/brc_transport.py`, blob `be1debe367263931bd5e93fd750be3ed54624fe1`: explicit integer/rational affine macro-effects and compositions; it is not already a modular gcd executor.
- `src/enterprise_math/finite_symmetry.py`, blob `ae96a32cb6b6fdd974bd9f44fb28a1b643c9b8a2`: finite-action/equivariance scope, not a free complete modular-orbit compiler.

These are reused source-audit pins, not newly fetched files or execution evidence in this unit. The macro `M direct-sum I_4` is integer-unimodular on a declared two-axis invariant slice; the marked displacement is `(0,1,0,0,0,0)`. It is not one primitive adjacency or a metric-preserving rotation.

There is also a marked reversing symmetry

`R_v=[[-1,0],[-k,1]]`,

with `R_v^2=I`, `R_v v=v`, and `R_v M R_v=M^-1`. It preserves the conic and the common gcd because `R_v(w-v)` is an integer-unimodular change of the residual coordinates. This supplies a small exact algebraic symmetry certificate if a later equally weighted forward/backward kernel needs it. It does not permit quotienting arbitrary named directional operations, and no such histogram algorithm is implemented here.

Reduction modulo N commutes with the integer matrix program and preserves (3). It is therefore an observer-scoped quotient for this modular witness. Raw X6 endpoints, primitive path length, time and carries remain separate data. For a raw state `z=r+Nq`, a step has `Mr=r'+N kappa`, hence new carry `Mq+kappa`. Discarding that carry is not lossless for later raw-world questions. Unreduced entries of a large expanding M^E can require order E log|k| bits, even though modular entries stay short.

A bounded future interface can take only `(N,k,E)` and return:

1. The discriminant setup outcome and its typed arithmetic/gcd receipts.
2. The actual modular matrix-power chain and the residual `(x,y)` at the fixed cyclic mark, with (2) bound to the same k,E and source.
3. A proper-factor/division receipt; or a unit/saturated common-gcd result; or an explicit partial state with its paid work retained.
4. Separate setup, exponent preparation, matrix arithmetic, observer, gcd and replay costs. If early coordinate probing stops before the common gcd, that distinct contract is recorded.

No unknown p, local character, local order, split eigenvalue or factor is an input. No numerical or native implementation of this candidate has yet been run. The genuine new reach within the existing project is free-trace access to nonsplit local conics plus an exact cyclic marked-return ideal. The underlying Lucas/Frobenius/p-plus-minus-one mathematics is **REUSE**; the native observer composition is an **EXTENSION CANDIDATE**. A generally efficient selector and complete native Shor closure remain unproved.

Global-Knowledge-Sync: main@7a63984 / GLOBAL_KNOWLEDGE_V1.
