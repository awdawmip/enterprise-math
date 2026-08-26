# Quadratic Packet Higher-Jet Automorphism No-Section — Independent Audit RAW

Status: `FROZEN RAW / BLIND-FORWARD / SOURCE-WITHHELD`

Task-ID: `RS-QUADRATIC-PACKET-HIGHER-JET-AUTOMORPHISM-NO-SECTION-INDEPENDENT-AUDIT`

Researcher-ID: `EM-QPHJA-1473D7`

Claim-ID: `chatgpt-qphja-20260826-1051`

Frozen at: `2026-08-26T10:55:15+08:00`

Unique route-specific input read before this freeze:

`research_inputs/QUADRATIC_PACKET_HIGHER_JET_AUTOMORPHISM_NO_SECTION_AUDIT_PACKET_20260825.md@blob:7f4445982fe9a85f141c91428d3b36988f8ac897`

No originating higher-jet proof, Cartier/Grothendieck source, native rank bridge, NC3 source/audit, QP-R2 source proof, or post-freeze comparison source was read before this artifact was frozen.

## Primary raw verdict

`SEMANTICALLY_VALID_BUT_FOUNDATION_INFERENCE_REJECTED`

More precisely:

- `HJ-A`: **PROVED at the frozen exact algebraic strength**.
- `HJ-B`: **PROVED at the frozen exact algebraic strength**, with a stronger pointwise statement: the primitive hypothesis can be weakened to `g_1 != 0 mod q`.
- `HJ-C`: **PROVED**.
- `HJ-D`: the conditional statement

  `ONE PRIMITIVE CLOCK + COORDINATE-NATURAL FULL-JET REALIZATION -> m=2`

  is a valid theorem inside the stated Cartier-jet model, but

  `ONE PRIMITIVE CLOCK -> m=2`

  does **not** follow. The phrase `coordinate-natural full-jet realization` carries an additional nontrivial realization/naturality premise.

The no-section theorem is therefore a real algebraic rigidity theorem, not a proof that one-clockness by itself forces quadratic height.

---

## 1. Setup

For `m>=2`, let

`A_m = Z[epsilon]/(epsilon^m)`.

Write every element uniquely as

`a_0 + a_1 epsilon + ... + a_(m-1) epsilon^(m-1)`.

The nilradical is exactly `(epsilon)`. A `Z`-algebra automorphism is therefore determined by

`epsilon |-> a_1 epsilon + a_2 epsilon^2 + ... + a_(m-1) epsilon^(m-1)`.

For fixed `q>=2`, the class set `J_m(q)` consists of the principal Cartier representatives

`f = q + g_1 epsilon + ... + g_(m-1) epsilon^(m-1)`

modulo multiplication by units with constant term `1`.

First note that every such `f` is a non-zero-divisor. Indeed, multiplication by `f` in the ordered basis

`1, epsilon, ..., epsilon^(m-1)`

is triangular with diagonal entries all equal to `q`; equivalently, if `h!=0` and `epsilon^r` is the lowest nonzero nilpotent degree occurring in `h`, then the coefficient of `epsilon^r` in `fh` is `q` times that nonzero coefficient. Since `q!=0` in `Z`, `fh!=0`.

Thus the stated representatives do define effective principal Cartier divisors at the frozen strength.

---

## 2. HJ-A — unique normalized class theorem

### 2.1 Existence

Let

`f = q + g_1 epsilon + ... + g_(m-1) epsilon^(m-1)`

and let

`u = 1 + u_1 epsilon + ... + u_(m-1) epsilon^(m-1)`.

Suppose the coefficients below degree `k` have already been normalized. The coefficient of `epsilon^k` in `fu` has the form

`g_k + q u_k + sum_(i=1)^(k-1) g_i u_(k-i)`.

At stage `k`, all terms except `u_k` are already fixed. There is a unique integer `u_k` that sends this coefficient to its unique residue in

`{0,1,...,q-1}`.

Because `u_k` first appears at degree `k`, later choices do not disturb earlier normalized coefficients. Recursion from `k=1` to `m-1` produces a normalized representative.

### 2.2 Uniqueness

Suppose two normalized representatives `f` and `f'` satisfy `f'=fu` with `u(0)=1`.

At degree one,

`g'_1 = g_1 + q u_1`.

Both `g'_1` and `g_1` lie in `[0,q-1]`, so `u_1=0` and `g'_1=g_1`.

Inductively assume `u_1=...=u_(k-1)=0` and `g'_i=g_i` for `i<k`. Then at degree `k`,

`g'_k = g_k + q u_k`.

Again the normalized range forces `u_k=0` and `g'_k=g_k`.

Hence the normalized representative is unique.

### 2.3 Cardinality and first-order reduction

There are exactly `q` independent normalized choices for each of the `m-1` coefficients, hence

`|J_m(q)| = q^(m-1)`.

Reduction modulo `epsilon^2` sends multiplication by a constant-one unit in `A_m` to multiplication by a constant-one unit in `A_2`, so

`pi_1 : J_m(q) -> J_2(q)`

is well-defined. It is surjective: any normalized first-order class `q+g_1 epsilon` is lifted by setting all higher coefficients to zero.

Therefore HJ-A holds exactly.

---

## 3. Exact integral automorphism group

Any `Z`-algebra endomorphism of `A_m` must send the nilpotent `epsilon` into `(epsilon)`, so it is determined by

`phi(epsilon)=a_1 epsilon + a_2 epsilon^2 + ... + a_(m-1) epsilon^(m-1)`.

On the nilpotent ideal, the substitution matrix in the basis

`epsilon, epsilon^2, ..., epsilon^(m-1)`

is triangular with diagonal

`a_1, a_1^2, ..., a_1^(m-1)`.

It is invertible over `Z` exactly when `a_1=+1` or `a_1=-1`. Conversely, if `a_1=±1`, triangular recursive inversion gives an integral inverse substitution.

Hence

`G_m = Aut_Z-alg(A_m)`

consists exactly of substitutions

`epsilon |-> ±epsilon + a_2 epsilon^2 + ... + a_(m-1) epsilon^(m-1)`, `a_i in Z`.

The action on `J_m(q)` is well-defined because an automorphism carries constant-one units to constant-one units and preserves the constant coefficient `q`.

Reduction modulo `epsilon^2` gives the induced action on `J_2(q)`. Since the first coefficient transforms by `g_1 |-> ±g_1 (mod q)`, the primitive subset `gcd(g_1,q)=1` is invariant.

---

## 4. HJ-B — all-order no-section theorem

Fix any `m>=3` and `q>=2`.

For each integer `a`, define the top shear

`T_a(epsilon) = epsilon + a epsilon^(m-1)`.

This is an element of `G_m`, with inverse `T_(-a)`, and it reduces to the identity modulo `epsilon^2`.

For every `k>=2`,

`(epsilon + a epsilon^(m-1))^k = epsilon^k mod epsilon^m`,

because every cross term containing `epsilon^(m-1)` has degree at least `m`.

Therefore on a normalized representative

`f = q + g_1 epsilon + ... + g_(m-1) epsilon^(m-1)`,

the shear changes only the top coefficient before renormalization:

`g_(m-1) |-> g_(m-1) + a g_1`.

By HJ-A, normalization at the top degree is reduction modulo `q`, so on normalized classes

`T_a : g_(m-1) |-> g_(m-1) + a g_1 (mod q)`.

Take `a=1`.

If the first-order class is primitive, then `gcd(g_1,q)=1`, so in particular

`g_1 != 0 mod q`.

Thus `T_1` has **no fixed point in that fiber** of `pi_1`.

But `T_1` acts trivially on the first-order base because it is the identity modulo `epsilon^2`. If an equivariant section `s` existed on the primitive base, then for every primitive `x`,

`T_1 s(x) = s(T_1 x) = s(x)`,

contradicting the absence of a fixed point in the fiber over `x`.

Therefore no `G_m`-equivariant section exists for any `m>=3`, `q>=2` over the primitive base.

### Premise sharpening

The proof never uses invertibility of `g_1 mod q`; it only uses

`g_1 != 0 mod q`.

Hence the pointwise obstruction is stronger:

> For every first-order normalized class with `g_1 != 0 mod q`, the kernel element `T_1` fixes the base class but has no fixed higher-jet lift.

The primitive hypothesis is sufficient but not minimal.

At `g_1=0`, this particular obstruction disappears; for example the constant class `[q]` is fixed by every substitution and gives a positive control at the zero first-order class.

This sharpening does not narrow or refute the frozen HJ-B statement; it strengthens its algebraic scope.

---

## 5. HJ-C — quadratic positive control

For `m=2`, the source and target of first-order reduction coincide:

`pi_1 : J_2(q) -> J_2(q)`

is the identity. Its only section is the identity, which is equivariant.

Therefore HJ-C holds.

---

## 6. Mandatory pressure tests

### 6.1 `q=2`

The primitive first coefficient is `g_1=1`. The top shear sends

`g_(m-1) |-> g_(m-1)+1 mod 2`,

so it toggles the top coefficient and has no fixed lift. The proof is fully effective at the smallest allowed shell.

### 6.2 Composite `q`

Nothing in HJ-A or the shear argument requires primality. For primitive `g_1`, nonzero modulo `q` is automatic. In fact every nonzero residue is obstructed, including nonprimitive residues.

### 6.3 Primitive versus nonprimitive

- primitive `g_1`: no equivariant lift;
- nonprimitive but nonzero `g_1`: the same `T_1` obstruction still applies;
- zero `g_1`: the top-shear obstruction vanishes, and `[q]` is a fixed lift of the zero first-order class.

Thus primitiveness is not the exact algebraic threshold; nonzero first-order phase is.

### 6.4 Every `m>=3`

The top shear `epsilon -> epsilon+epsilon^(m-1)` exists uniformly for every `m>=3`, so the proof is not an `m=3` accident.

### 6.5 Full integral automorphism group

The group has been classified above: leading coefficient exactly `±1`, arbitrary higher integral coefficients. The obstruction uses an actual element of the kernel of `G_m -> G_2`, so it is intrinsic to full coordinate naturality.

### 6.6 External coordinate/frame or restricted automorphism group

If an external coordinate/frame is supplied and equivariance under the full `G_m` is dropped, a section exists trivially as a set-theoretic choice, for example

`q+g_1 epsilon |-> q+g_1 epsilon`

with all higher normalized coefficients set to zero.

Therefore the obstruction is specifically an obstruction to **full coordinate naturality**. Some proper nontrivial subgroups may still obstruct sections; no stronger restricted-group classification is needed for HJ-B.

### 6.7 Unit quotient has not removed the obstruction

The top coefficient in the unique normalized representative is a genuine residue modulo `q`. Multiplication by a constant-one unit can alter it by multiples of `q`, but cannot identify a shift by nonzero `g_1 mod q`. Thus the quotient by units does not kill the top-shear orbit.

### 6.8 Nonlinear assignments do not evade the theorem

The contradiction is pointwise: the stabilizer of each nonzero first-order base point contains `T_1`, while its fiber has no `T_1`-fixed point. No nonlinear dependence on lower or higher coefficients can create a fixed point where none exists.

### 6.9 Fixed-coordinate artifact check

With a fixed coordinate, the zero-higher-coefficient section exists. It fails precisely because a top shear changes its top coefficient. Hence the theorem is not a statement that higher coefficients cannot be selected; it is a statement that they cannot be selected **naturally under all integral coordinate changes**.

### 6.10 Arbitrary one-clock collapse chains

The argument applies only after a one-clock object is represented as the first-order quotient of the specific full Cartier jet `J_m(q)` with the full `G_m` naturality requirement. It says nothing directly about arbitrary finite one-clock collapse chains or unrelated objects merely named `J_3`.

---

## 7. HJ-D — exact semantic consequence

The proved theorem package yields the following exact conditional rigidity statement:

> Let `m>=2`, `q>=2`, and consider the specified Cartier jet system `J_m(q)`. If a nonzero (hence in particular primitive) first-order phase is required to admit a full higher-jet realization via a section of `pi_1` that is natural under **every** integral algebra automorphism of `A_m`, then necessarily `m=2`.

This implication is non-circular as an algebraic theorem: the proof uses only the explicit jet quotient, its automorphism group, and a kernel stabilizer with no fiber fixed point.

However, the phrase

`coordinate-natural full-jet realization`

is an additional premise. It asserts at least all of the following:

1. the native/physical one-clock datum is identified with the first-order reduction of this particular Cartier-jet object;
2. a full `m`-jet completion is part of the semantic state to be selected from that datum;
3. there is no privileged nilpotent coordinate/frame;
4. the selection must be equivariant under the entire integral automorphism group `G_m`, not merely under a smaller native symmetry group.

None of these requirements follows from the bare statement “there is one primitive cyclic clock.”

Therefore the strongest raw conclusion is:

`ONE PRIMITIVE CLOCK + COORDINATE-NATURAL FULL-JET REALIZATION -> m=2`

inside the specified model, while

`ONE PRIMITIVE CLOCK -> m=2`

is rejected as an unsupported semantic upgrade.

This is why the primary raw verdict is

`SEMANTICALLY_VALID_BUT_FOUNDATION_INFERENCE_REJECTED`.

---

## 8. Raw freeze boundary

This artifact is the source-withheld independent result. It must remain unchanged during post-freeze comparison except for an explicitly labeled metadata-only correction.

The next permitted action is source comparison against the exact post-freeze references named in the blind packet. Any agreement with an originating proof discovered later is provenance comparison, not part of this raw derivation.
