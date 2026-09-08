# RH prime connection: pure-gauge audit, continuum-flat diagnostic, and degree-homotopy no-go

Status: `RESEARCH FRONTIER / EXACT PROJECT-DERIVED IDENTITIES + PRIOR-ART FACTORIZATION / NOT A PROOF OF RH`
Date: `2026-09-08`
Project: `Enterprise Math / 进取数论`
Scope: `RH / Möbius / degree-marker Euler product / prime-discrete source / BRC / X6 local port`

## 0. Typing guard

P000 is unchanged. Prime labels, factor-count depth, and ordered prime factors are arithmetic provenance, not additional X6 axes. X6 remains a fixed-width local carrier. Any depth growth below is BRC/provenance depth.

BRC priority remains:

`PROVENANCE > MULTIPLICITY > BOOLEAN SUPPORT`.

Positive capacity, Taylor-shift identities, and coordinate changes must not be confused with signed RH cancellation.

---

## 1. Correction to the pointwise prime-adapted vector field

Let

`P=P(s,y)`

and consider

`nabla = partial_z + A(s,y) partial_s`.

To annihilate the rank-one term `z P(s,y)` at the Möbius point `z=-1`, one needs

`P - A P_s = 0`,

hence

`A=P/P_s`.

The earlier sign `-P/P_s` is incorrect for this stated convention.

Freeze:

`POINTWISE_NULL_DIRECTION_SIGN = P/P_s`.

---

## 2. Self-adapted connection is pure gauge

Do not restrict to `z=-1`. Define

`q=z P(s,y)`.

The exact level-set vector field is

`D_z = partial_z - P/(z P_s) partial_s`,

for which

`D_z q=0`.

Likewise, the exact horizontal lift of the y-direction preserving q is

`D_y = partial_y - P_y/P_s partial_s`,

and

`D_y q=0`.

In coordinates `(q,z,y)`, these are simply coordinate derivatives at fixed q. Therefore

`[D_z,D_y]=0`

identically wherever the coordinate chart is valid.

Hence any curvature obtained by comparing `D_z` with the bare `partial_y` is a coordinate artifact caused by failing to horizontally lift the y-motion.

Freeze:

`SELF_ADAPTED_PRIME_CONNECTION = PURE_GAUGE`.

Consequence: bounded holonomy of a connection defined using the exact unknown prime source itself cannot supply new RH content.

---

## 3. Source-independent continuum-flat connection

A non-tautological comparison must be fixed before seeing the discrete primes.

Put

`eta=log y`,

and for a finite logarithmic prime window `(e^eta,e^(u eta)]` define the continuous prime-density channel

`P_0(s;eta,u)=int_(e^eta)^(e^(u eta)) t^(-s)/log(t) dt`.

After `t=e^(eta v)`, this becomes

`P_0(s;eta,u)=int_1^u exp(-(s-1) eta v) dv/v`.

Define, with u held fixed,

`D_0 = partial_eta - (s-1)/eta partial_s`.

Since `xi=(s-1)eta` is invariant under `D_0`,

`D_0 P_0(s;eta,u)=0`

exactly.

This operator depends only on the continuum density `dt/log t`, not on actual prime locations.

### Higher Euler power-sum channels

For the j-th channel,

`P_0(j s;eta,u)=int_1^u exp(-(j s-1)eta v) dv/v`.

Because

`D_0((j s-1)eta)=j-1`,

one gets the exact formula

`D_0 P_0(j s;eta,u)=-(j-1) int_1^u exp(-(j s-1)eta v) dv`.

Thus:

- j=1 is the unique continuum-null channel;
- every j>=2 leaves an explicit stable residual.

This is a source-independent reappearance of the existing project statement

`MOBIUS_PRIME_CRITICAL_RANK = 1`.

---

## 4. Prime-discrete defect isolated exactly

Define the actual finite prime channel

`P_pi(s;eta,u)=sum_(e^eta < p <= e^(u eta)) p^(-s)`.

Write

`Delta_pi=P_pi-P_0`.

Then

`D_0 P_pi = D_0 Delta_pi`.

So `D_0` removes the continuum prime-density carrier exactly and exposes only the prime-discrete defect.

Equivalently, at fixed `xi=(s-1)eta`, define the scaled harmonic prime measure

`nu_eta = sum_(e^eta<p<=e^(u eta)) p^(-1) delta_(log p/eta)`.

Then

`P_pi(1+xi/eta;eta,u)=int_[1,u] e^(-xi v) d nu_eta(v)`,

whereas the continuum carrier is

`int_1^u e^(-xi v) dv/v`.

Hence `D_0` is the scale derivative of the discrepancy between the actual ordered prime-location measure and the fixed measure `dv/v`.

This is a diagnostic interface, not yet an estimate.

---

## 5. Explicit zeta-zero response: diagnostic-only no-go

For one explicit-formula zero mode, use the finite-window model

`Z_rho(s;eta,u)=int_1^u exp((rho-s)eta v) dv/v`.

Since

`D_0((rho-s)eta)=rho-1`,

we get

`D_0 Z_rho = (rho-1) int_1^u exp((rho-s)eta v) dv`.

Therefore the continuum-flat operator annihilates only the main-density mode `rho=1`.

Every nontrivial zeta zero has a nonzero transfer factor `rho-1`.

Freeze:

`CONTINUUM_FLAT_CONNECTION_IS_ZERO_TRANSPARENT`.

Consequently, controlling its defect at RH strength still requires controlling the zeta-zero locations; no automatic cancellation has been created.

---

## 6. Degree-marker factorization and abscissa rigidity

Let

`F(z,s)=prod_p (1+z p^(-s))`

in the absolutely convergent region and continue by the standard Selberg-Delange factorization. For bounded z,

`F(z,s)=zeta(s)^z G(z,s)`,

where `G(z,s)` is holomorphic and nonzero in `Re(s)>1/2` away from the standard boundary issues, because all Euler channels with multiplicity >=2 are absorbed into an absolutely convergent factor.

A direct logarithmic form is

`log G(z,s)=sum_(m>=2) [((-1)^(m+1) z^m - z)/m] P(m s)`.

Near a nontrivial zero `rho` of zeta,

`F(z,s) ~ (s-rho)^z * nonzero analytic factor`

for fixed `z != 0`.

Therefore changing the degree marker from the Möbius point `z=-1` to any fixed nonzero `z` changes only the algebraic/logarithmic singularity order. It does NOT change the horizontal exponent `Re(rho)` carried into Perron/Mellin asymptotics.

Freeze:

`DEGREE_MARKER_DEFORMATION_PRESERVES_ZERO_ABSCISSA_FOR_ALL_FIXED_z_NE_0`.

Consequences:

1. Moving partway from `z=-1` toward `z=0` cannot produce any fixed power saving `x^{-delta}` against an off-critical zero.
2. Only the exact endpoint `z=0` removes the zeta-zero singularity.
3. A continuous parity-to-positive homotopy can at best change logarithmic powers unless it reaches `z=0` exactly.

This matches the general Selberg-Delange/fake-Mobius literature, where zeta powers govern the leading analytic singularity.

---

## 7. Finite-order mixed differential annihilators cannot regularize the zero set

At `z=-1`,

`F(-1,s)=1/zeta(s)`.

Near a simple nontrivial zero `rho`,

`F(-1,s) ~ c/(s-rho)`.

The first z-derivative introduces the unique critical logarithmic channel; higher z-derivatives have leading behavior

`partial_z^k F(-1,s) = F(-1,s) [L_1(s)^k + lower log degree]`,

where `L_1(s)` has the same prime-zeta logarithmic singularity at rho, while the higher Euler channels are locally stable.

Likewise, s-derivatives raise pole order.

Hence any nonzero fixed finite-order constant-coefficient operator

`D=sum_(a<=A,b<=B) c_(a,b) partial_s^a partial_z^b`

leaves a nonremovable pole/log singularity at every generic zeta zero. Taking the maximal s-order and then maximal z-log degree gives a triangular leading singularity that cannot be canceled by lower-order terms unless the corresponding coefficients vanish recursively.

Freeze for this declared operator class:

`FIXED_FINITE_ORDER_SOURCE_INDEPENDENT_MIXED_ANNIHILATOR != RH_REGULARIZER`.

This is the differential-operator version of the earlier fixed-depth/fixed-label BRC no-go.

---

## 8. Infinite translation identity and the meaning of Alladi jets

The only source-independent degree-marker operator that removes the zero singularity exactly is the full translation to z=0:

`exp(partial_z) F(z,s)|_(z=-1) = F(0,s)=1`.

For the regularized primitive extractor

`R(z,s)=(F(z,s)-1)/z`,

we have

`exp(partial_z) R(z,s)|_(z=-1)=R(0,s)=P(s)`.

Thus the Alladi/Taylor jet hierarchy is exactly a finite-order approximation to a unit translation in the degree-marker coordinate.

For a formal expansion

`R(z)=sum_(r>=1) e_r z^(r-1)`,

the K-jet Taylor truncation at z=-1 has the exact coefficient identity

`sum_(k=0)^K R^(k)(-1)/k!`
`= e_1 + sum_(r>=K+2) (-1)^(r-1+K) C(r-2,K) e_r`.

Therefore:

- the primitive prime channel `e_1` is selected exactly;
- all arities `2,...,K+1` cancel exactly;
- the entire remainder is arity `>K+1` with the familiar binomial/Bonferroni weight.

This identifies the project primitive-selector with a provenance-preserving version of truncated inclusion-exclusion.

Freeze:

`ALLADI_HIGH_ORDER_JETS = FINITE_TRANSLATION / BONFERRONI_PRIMITIVE_EXTRACTION`.

The measure-valued Alladi form still preserves ordered-prime provenance and is richer than a scalar sieve weight, but the scalar cancellation mechanism itself is not an escape from the classical parity barrier.

---

## 9. New frontier after the no-go stack

The following routes are now frozen as insufficient by themselves:

- self-adapted prime connection / holonomy;
- fixed finite-order mixed `(s,z)` differential annihilators;
- any fixed nonzero degree-marker homotopy `z in (-1,0)`;
- fixed-depth X6/fixed-label arithmetic transport;
- scalar finite Taylor/Bonferroni extraction without growing provenance.

A viable Enterprise route must therefore have all of:

1. fixed X6 local width;
2. BRC/provenance depth growing with scale;
3. source-independent coefficients (no operator defined from the exact unknown prime discrepancy itself);
4. nonlocal retention of the ordered-prime chain, not only factor-count moments;
5. a genuinely collective mechanism, because individual zeta-zero modes are not killed by any fixed finite-order local filter.

The next smallest unresolved object is:

`GROWING_DEPTH_ORDERED_PRIME_PROVENANCE_TRANSFER`.

Concretely, study the full ordered-prime chain behind Alladi's measure-valued duality at depth

`K(x) ~ log x/(2 loglog x)`,

and ask whether the joint provenance/shuffle structure supplies a collective contraction that is absent after scalar Bonferroni compression.

Do NOT return to a self-adapted connection unless an invariant is defined independently of the actual prime source.

---

## 10. Prior-art references checked

- Selberg-Delange factorization for squarefree degree-marked series `sum mu^2(n) z^omega(n) n^-s = zeta(s)^z G(s,z)`; standard analytic number theory, also summarized in modern references and MathOverflow discussions.
- Alladi & Sengupta (2026), `Duality Between Prime Factors and The Prime Number Theorem For Arithmetic Progressions -- Higher Order Dualities`, arXiv:2604.17832.
- Y. Alamoudi (2026), `On subradically sifted sums related to Alladi's higher order duality between prime factors`, arXiv:2601.10636.
- O. Gorodetsky (2023), `Smooth numbers and the Dickman rho function`, Journal d'Analyse Mathematique 151.
- de la Bretèche & Tenenbaum, `Friable averages of oscillating multiplicative functions`, arXiv:2207.04777.

No claim in this note is a proof of RH.
