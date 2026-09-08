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

Let `P=P(s,y)` and consider

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

Define `q=zP(s,y)`. The exact level-set vector field is

`D_z = partial_z - P/(z P_s) partial_s`,

for which `D_z q=0`.

Likewise, the exact horizontal lift of the y-direction preserving q is

`D_y = partial_y - P_y/P_s partial_s`,

and `D_y q=0`.

In coordinates `(q,z,y)`, these are coordinate derivatives at fixed q, hence

`[D_z,D_y]=0`

wherever the chart is valid.

Therefore curvature obtained by comparing `D_z` with bare `partial_y` is a coordinate artifact caused by failing to horizontally lift the y-motion.

Freeze:

`SELF_ADAPTED_PRIME_CONNECTION = PURE_GAUGE`.

A connection defined using the exact unknown prime source itself cannot supply new RH content merely through holonomy.

---

## 3. Source-independent continuum-flat connection

A non-tautological comparison must be fixed before seeing the discrete primes.

Put `eta=log y`. For the finite logarithmic prime window `(e^eta,e^(u eta)]`, define

`P_0(s;eta,u)=int_(e^eta)^(e^(u eta)) t^(-s)/log(t) dt`

so that

`P_0(s;eta,u)=int_1^u exp(-(s-1)eta v) dv/v`.

At fixed u define

`D_0 = partial_eta - (s-1)/eta partial_s`.

Since `xi=(s-1)eta` is invariant,

`D_0 P_0(s;eta,u)=0`

exactly.

This operator depends only on the continuum density `dt/log t`, not on actual prime locations.

### Higher Euler power-sum channels

For

`P_0(j s;eta,u)=int_1^u exp(-(j s-1)eta v) dv/v`,

one has

`D_0((j s-1)eta)=j-1`,

hence

`D_0 P_0(j s;eta,u)=-(j-1) int_1^u exp(-(j s-1)eta v) dv`.

Thus j=1 is uniquely null, while j>=2 leaves an explicit residual. This is a source-independent reappearance of

`MOBIUS_PRIME_CRITICAL_RANK = 1`.

---

## 4. Prime-discrete defect isolated exactly

Define

`P_pi(s;eta,u)=sum_(e^eta < p <= e^(u eta)) p^(-s)`

and `Delta_pi=P_pi-P_0`. Then

`D_0 P_pi = D_0 Delta_pi`.

Equivalently, at fixed `xi=(s-1)eta`, define the scaled harmonic prime measure

`nu_eta = sum_(e^eta<p<=e^(u eta)) p^(-1) delta_(log p/eta)`.

Then

`P_pi(1+xi/eta;eta,u)=int_[1,u] e^(-xi v) d nu_eta(v)`,

whereas the continuum carrier is

`int_1^u e^(-xi v) dv/v`.

Hence `D_0` is the scale derivative of the discrepancy between actual ordered prime-location mass and the fixed measure `dv/v`.

This is a diagnostic interface, not an estimate.

---

## 5. Explicit zeta-zero response: diagnostic-only no-go

For one explicit-formula zero mode, let

`Z_rho(s;eta,u)=int_1^u exp((rho-s)eta v) dv/v`.

Since

`D_0((rho-s)eta)=rho-1`,

we obtain

`D_0 Z_rho=(rho-1) int_1^u exp((rho-s)eta v) dv`.

Therefore the continuum-flat operator annihilates only the main-density mode `rho=1`; every nontrivial zeta zero has nonzero transfer factor `rho-1`.

Freeze:

`CONTINUUM_FLAT_CONNECTION_IS_ZERO_TRANSPARENT`.

Controlling this defect at RH strength still requires controlling zero locations.

---

## 6. Degree-marker factorization and abscissa rigidity

Let

`F(z,s)=prod_p(1+z p^(-s))`.

Standard Selberg-Delange factorization gives, for bounded z,

`F(z,s)=zeta(s)^z G(z,s)`,

with the remainder factor holomorphic/nonzero in the relevant `Re(s)>1/2` region after separating the first prime channel. One convenient logarithmic form is

`log G(z,s)=sum_(m>=2) [((-1)^(m+1) z^m-z)/m] P(ms)`.

Near a nontrivial zero rho,

`F(z,s) ~ (s-rho)^z * nonzero analytic factor`

for fixed `z != 0`.

Therefore changing the degree marker changes singularity/log order but not the horizontal exponent `Re(rho)` entering Perron/Mellin asymptotics.

Freeze:

`DEGREE_MARKER_DEFORMATION_PRESERVES_ZERO_ABSCISSA_FOR_ALL_FIXED_z_NE_0`.

Consequences:

1. moving partway from `z=-1` toward `z=0` cannot create a fixed power saving against an off-critical zero;
2. only the exact endpoint `z=0` removes the zeta-zero singularity;
3. parity-to-positive homotopy at fixed nonzero z changes logarithmic powers, not the critical abscissa.

---

## 7. Fixed finite-order mixed differential annihilators cannot regularize the zero set

At `z=-1`, `F(-1,s)=1/zeta(s)`. Near a simple nontrivial zero rho,

`F(-1,s) ~ c/(s-rho)`.

The first z-derivative introduces the unique critical logarithmic channel; higher z-derivatives have leading behavior

`partial_z^k F(-1,s)=F(-1,s)[L_1(s)^k + lower log degree]`,

where `L_1` has the prime-zeta logarithmic singularity at rho, while higher Euler channels are locally stable. s-derivatives raise pole order.

Hence a nonzero fixed finite-order constant-coefficient operator

`D=sum_(a<=A,b<=B)c_(a,b) partial_s^a partial_z^b`

leaves a nonremovable pole/log singularity at generic zeta zeros. Maximal s-order and then maximal log degree form a triangular leading singularity that lower-order terms cannot cancel unless coefficients vanish recursively.

Freeze for this declared operator class:

`FIXED_FINITE_ORDER_SOURCE_INDEPENDENT_MIXED_ANNIHILATOR != RH_REGULARIZER`.

---

## 8. Infinite translation identity and the meaning of Alladi jets

The exact source-independent degree-marker operation removing the zero singularity is the full translation to z=0:

`exp(partial_z)F(z,s)|_(z=-1)=F(0,s)=1`.

For

`R(z,s)=(F(z,s)-1)/z`,

one has

`exp(partial_z)R(z,s)|_(z=-1)=R(0,s)=P(s)`.

Thus the Alladi/Taylor jet hierarchy is a finite-order approximation to unit translation in degree-marker space.

For

`R(z)=sum_(r>=1)e_r z^(r-1)`,

the K-jet truncation has the exact identity

`sum_(k=0)^K R^(k)(-1)/k!`
`=e_1+sum_(r>=K+2)(-1)^(r-1+K) C(r-2,K)e_r`.

Therefore the primitive prime channel is selected, arities `2,...,K+1` cancel exactly, and the remainder is arity `>K+1` with the binomial/Bonferroni weight.

Freeze:

`ALLADI_HIGH_ORDER_JETS = FINITE_TRANSLATION / BONFERRONI_PRIMITIVE_EXTRACTION`.

The measure-valued form still retains ordered-prime provenance, but the scalar cancellation itself is not an escape from sieve parity.

---

## 9. Finite translation remainder retains the full zero singularity

The positive high-arity capacity of the finite Taylor remainder must not be confused with analytic harmlessness.

Near a simple zeta zero rho, use

`F(z,s)=zeta(s)^z G(z,s)`.

For fixed k,

`(1/k!) partial_z^k F(-1,s)`

has leading local form

`[G(-1,rho)/(zeta'(rho)(s-rho))] * [log(s-rho)^k/k! + O(log(s-rho)^(k-1))]`.

Therefore every finite K Taylor truncation at z=-1 still contains a singularity of the form

`(s-rho)^(-1) log(s-rho)^K`

at highest logarithmic degree.

Since the full infinite translation equals the regular function `F(0,s)=1`, the exact Taylor remainder must carry the opposite singularity. Hence:

`FINITE_K_HIGH_ARITY_REMAINDER_RETAINS_ZERO_CRITICALITY`.

This remains true even when a positive/factorial capacity bound makes the high-arity remainder small in a Perron-near-1 or counting norm.

Freeze the norm boundary:

`POSITIVE_CAPACITY_SMALL != SIGNED_ANALYTIC_CRITICALITY_SMALL`.

This explains why the previously obtained `K~log x/(2loglog x)` square-root positive tail estimate does not itself provide an analytic continuation or zero-free conclusion in `Re s>1/2`.

---

## 10. New frontier after the no-go stack

Frozen as insufficient by themselves:

- self-adapted prime connection / holonomy;
- fixed finite-order mixed `(s,z)` annihilators;
- any fixed nonzero degree-marker homotopy `z in (-1,0)`;
- fixed-depth X6/fixed-label arithmetic transport;
- scalar finite Taylor/Bonferroni extraction;
- treating a high-arity tail as analytically harmless merely because its positive capacity is small.

A viable Enterprise route must therefore have all of:

1. fixed X6 local width;
2. BRC/provenance depth growing with scale;
3. source-independent coefficients;
4. nonlocal retention of the ordered-prime chain, not only factor-count moments;
5. a genuinely collective mechanism acting on signed/phase coherence, not only positive capacity;
6. an explicit norm bridge from provenance-level cancellation to the critical analytic/Riesz norm.

The next smallest unresolved object remains

`GROWING_DEPTH_ORDERED_PRIME_PROVENANCE_TRANSFER`,

at depth

`K(x)~log x/(2loglog x)`.

The key new requirement is that the transfer must control the signed analytic remainder itself, not merely the number/mass of arity>K Cells.

---

## 11. Prior-art references checked

- Selberg-Delange factorization for `sum mu^2(n) z^omega(n)n^-s = zeta(s)^z G(s,z)`; standard analytic number theory, also present in modern references on fake Möbius functions and Selberg-Delange.
- Alladi & Sengupta (2026), `Duality Between Prime Factors and The Prime Number Theorem For Arithmetic Progressions -- Higher Order Dualities`, arXiv:2604.17832.
- Y. Alamoudi (2026), `On subradically sifted sums related to Alladi's higher order duality between prime factors`, arXiv:2601.10636.
- O. Gorodetsky (2023), `Smooth numbers and the Dickman rho function`, Journal d'Analyse Mathematique 151.
- de la Bretèche & Tenenbaum, `Friable averages of oscillating multiplicative functions`, arXiv:2207.04777.

No claim in this note is a proof of RH.
