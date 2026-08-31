# High-Dimensional Prime Wall — Independent Proof Checkpoint

Status: `FROZEN_PRE_CLASSICAL_AUDIT`

Researcher-ID: `EM-HDPWA-03E870`

Task-ID: `RS-HIGHDIM-PRIME-WALL-FILTER-ALGEBRA-EQUIVALENCE-AUDIT`

Frozen at: `2026-08-23T18:51:04.8162675+08:00`

Input: statement-only packet at
`research_inputs/HIGHDIM_PRIME_WALL_FILTER_EQUIVALENCE_PACKET_20260823.md@0173b1ea489a4811d42b77b9e8d977d327c4d08e`.

Information firewall attestation: before this checkpoint was written, no classical-source search,
tool-catalog lookup, source free-research branch, Draft PR #595, source script/note, withheld
GLOBAL_KNOWLEDGE event, or source derivation was opened.  The only mathematical input was the
statement packet.

## 1. Definitions and conventions

Let

`S(q)=sum_{m>=1} q^(m^2)` and `theta(q)=1+2*S(q)`.

For coefficient identities, extend the packet's positive-index array by

`Wbar_{d,lambda}(0)=1` and `Wbar_{d,lambda}(n)=W_{d,lambda}(n)` for `n>=1`.

Let `delta_square(n)=1` when `n` is a positive square and `0` otherwise.  Since `A_1(n)`
counts positive solutions of `x^2=n`, `A_1(n)=delta_square(n)`.

Let `r_d(n)=[q^n]theta(q)^d`; this is only an arithmetic signed-decoration count in this
checkpoint and carries no native-axis semantics.

## 2. Independent algebraic reconstruction

### H1 — support decomposition

Partition the nonnegative shell by the support set `J={i:x_i>0}`.  For each `|J|=s`,
deleting the zero coordinates gives an ordered positive `s`-tuple counted by `A_s(n)`, and
there are `binom(d,s)` choices of `J`.  The classes are disjoint and exhaustive, hence

`C_d(n)=sum_{s=1}^d binom(d,s)A_s(n)`.

Status: `PROVED_EXACT` for `d,n>=1`.

### H2 — carrier recoloring, and its limit

In any commutative unital coefficient algebra,

`T_lambda(T_mu(F)) = 1+lambda*(mu*(F-1)) = T_(lambda*mu)(F)`.

On the support-graded coefficient `A_s`, the induced action is multiplication by
`lambda^s`; two recolorings therefore multiply by `(lambda*mu)^s`.  After support grades are
collapsed into the single sequence `n -> W_{d,lambda}(n)`, there is generally no recoverable
operator implementing this action: `T_lambda(F^d)` is not `T_lambda(F)^d`, and `T_lambda` is
not a ring homomorphism.  Thus the carrier maps form a multiplicative action, but the collapsed
`W` arrays do not acquire an additional composition law.

Status: `PROVED_WITH_EXPLICIT_NONIMPLICATION`.

### H3 — dimension convolution

Because

`sum_{n>=0} Wbar_{d,lambda}(n)q^n=(1+lambda*S(q))^d`,

Cauchy multiplication gives, for all `n>=0`,

`Wbar_{d+e,lambda}(n)=sum_{k=0}^n Wbar_{d,lambda}(k)Wbar_{e,lambda}(n-k)`.

For the packet's positive-only arrays and `n>=1`, this is equivalently

`W_{d+e}(n)=W_d(n)+W_e(n)+sum_{k=1}^{n-1}W_d(k)W_e(n-k)`.

The bare convolution statement is false if the two endpoint identity terms are silently
discarded.

Status: `PROVED_AFTER_N0_COMPLETION`.

### H4 — fixed-face survival

Let `Omega_d(n)` be the uniform finite nonnegative shell and let `S(x)` be support size.
For a fixed coordinate `j`, the surviving states after deletion are exactly the states with
`x_j=0`, in bijection with `Omega_{d-1}(n)`.  Coordinate symmetry gives

`Pr(x_j>0)=(1/d)sum_i Pr(x_i>0)=E[S]/d`.

Consequently, when `C_d(n)>0`,

`C_{d-1}(n)/C_d(n)=Pr(x_j=0)=1-E[S]/d`.

Status: `PROVED_EXACT`.

## 3. Independent wall reduction

Expanding the two wall polynomials in the positive-support variable `X` gives

`P4(X)=2(1+X)^4-4(1+X)^3+3(1+X)^2`

`     =1+2X+3X^2+4X^3+2X^4`,

and

`P8(X)=16(1+X)^8-64(1+X)^7+112(1+X)^6-112(1+X)^5`

`     +70(1+X)^4-28(1+X)^3+7(1+X)^2`

`     =1+2X+7X^2+28X^3+70X^4+112X^5+112X^6+64X^7+16X^8`.

Direct coefficient comparison with `(1+2X)^4` and `(1+2X)^8` yields the formal identities

`theta(q)^4 = 8*P4(S(q))-7-8*S(q)`,

`theta(q)^8 = 16*P8(S(q))-15-16*S(q)`.

Therefore, for every `n>=1`, not merely odd `n`,

`Q4(n)=r_4(n)/8+delta_square(n)`,

`Q8(n)=r_8(n)/16+delta_square(n)`.

The independently reconstructed theta/Lambert coefficient identities are

`r_4(n)=8*sum_{d|n, 4 does not divide d} d`,

`r_8(n)=16*sum_{d|n} (-1)^(n+d)d^3`.

Proof certificate: insert the Jacobi triple product for `theta`; the displayed Lambert
series are the corresponding weight-2 and weight-4 level-4 forms.  Their differences from
`theta^4` and `theta^8` are level-4 modular forms.  The level-4 Sturm bounds are respectively
`1` and `2`; the constant term and coefficients through those bounds agree.  This establishes
the formal identities without finite-range extrapolation.  The checker separately recomputes
both sides from definitions.

Thus the all-integer arithmetic form is

`Q4(n)=sum_{d|n,4 does not divide d}d+delta_square(n)`,

`Q8(n)=sum_{d|n}(-1)^(n+d)d^3+delta_square(n)`.

For odd `n`, every divisor is odd, hence

`Q4(n)=sigma_1(n)+delta_square(n)`,

`Q8(n)=sigma_3(n)+delta_square(n)`.

### H5 — four-dimensional prime wall

If odd `n>1` is prime, `delta_square(n)=0` and `sigma_1(n)=n+1`.  Conversely, if it is
composite, `sigma_1(n)` contains `1`, `n`, and at least one additional positive proper divisor;
the square correction is nonnegative.  Hence `Q4(n)>n+1`.  This proves the biconditional.

For distinct odd primes `p,q`, the square correction vanishes and

`Q4(pq)=(1+p)(1+q)=pq+p+q+1`,

so `Q4(pq)-(pq+1)=p+q`.

Status: `PROVED_EXACT_AT_STATED_ODD_SCOPE`.

### H6 — eight-dimensional prime wall

The same argument with `sigma_3` gives, for odd `n>1`,

`n prime iff Q8(n)=n^3+1`.

For the requested composite extensions, if `n=product p_i^(a_i)` is odd, then

`Q4(n)=product_i (1+p_i+...+p_i^(a_i))+delta_square(n)`,

`Q8(n)=product_i (1+p_i^3+...+p_i^(3a_i))+delta_square(n)`.

These formulas cover prime powers and arbitrary odd composites exactly.

Status: `PROVED_EXACT_AT_STATED_ODD_SCOPE`.

## 4. H7 criterion-level audit before prior-art lookup

In the `A_s` basis, the nonconstant support weights of `Q4` are `(2,3,4,2)` for
`s=(1,2,3,4)`.  At an odd prime, `A_1(p)=0`.  The only structural reading under which
"support-composition independent" is a coefficient-vector property is:

> There is one scalar `kappa`, independent of support grade, such that on the formal
> prime-admissible grades `s in {2,3,4}`, `binom(4,s)lambda^s=kappa*(3,4,2)_s`.

The three ratios are

`2lambda^2`, `lambda^3`, and `lambda^4/2`.

Over any characteristic-zero field, a nonzero `lambda` makes them equal iff `lambda=2`,
and then `kappa=8`.  Thus uniqueness is exact under the structural-grade quantifier.

However, if "admissible" means only grades for which `A_s(p)` is nonzero at one fixed prime,
the stated uniqueness is false.  For example, `p=3` has only grade `s=3`, so every nonzero
`lambda` is vacuously proportional on that singleton.  Therefore H7 requires the structural
quantifier and cannot be advertised as a per-prime numerical uniqueness result.

Status: `PROVED_UNDER_STRUCTURAL_GRADE_READING / REFUTED_UNDER_PER_INSTANCE_READING`.

## 5. H8 pre-source reconstruction

Define

`f(q)=eta(2z)^12=q*product_{m>=1}(1-q^(2m))^12=sum_{n>=1}a(n)q^n`.

The reconstructed weight-6 identity is

`theta(q)^12 = (64*E6(4z)-E6(z))/63 + 16*f(q)`.

Equivalently,

`r_12(n)=8*sigma_5(n)-512*sigma_5(n/4)+16*a(n)`,

where `sigma_5(n/4)=0` unless `4|n`.  Both sides are weight-6 level-4 forms; the level-4
Sturm bound is `3`.  The coefficients at `n=0,1,2,3` are respectively
`(1,24,264,1760)` on both sides, which supplies an exact modular-form certificate.

For odd `n`, and in particular odd primes,

`r_12(n)=8*sigma_5(n)+16*a(n)`.

Thus the source experiment's normalized residual can only be a rescaling of the normalized
coefficient `a(p)/p^(5/2)`.  Whether the governing distribution theorem applies to this exact
newform, and under what normalization/density statement, is intentionally left
`OPEN_PENDING_PRIMARY_SOURCE_AUDIT` at this firewall checkpoint.  No novelty is inferred.

## 6. Computation layer kept separate

`experiments/highdim_prime_wall_filter_equivalence_checker.py` independently computes
`A_s`, `C_d`, `W`, `Q4`, and `Q8` from the definitions.  At freeze it passed through
`n<=256`, `d<=12`, including:

- the `n=0` convolution identity;
- separate divisor-function evaluation;
- prime powers, two-prime and three-prime squarefree composites;
- 4-adic examples;
- the odd twelve-square eta identity;
- an intentionally wrong `Q4` vector, whose first odd failure is `n=5`.

This computation is corroboration, not the proof of H5/H6 or the future H8 distribution audit.

## 7. Frozen pre-classical statuses

| Item | Independent checkpoint status | Scope repair retained |
|---|---|---|
| H1 | proved exact | none |
| H2 | proved carrier/support-graded | no collapsed-array semigroup |
| H3 | proved | must adjoin `W(0)=1`, or show endpoint terms |
| H4 | proved exact | require `C_d(n)>0` |
| H5 | proved exact | odd `n>1`; all-`n` formula recorded |
| H6 | proved exact | odd `n>1`; all-`n` formula recorded |
| H7 | structural reading proved | per-fixed-prime reading refuted |
| H8 | exact modular residual identified | distribution theorem pending primary-source audit |

No classification in this checkpoint uses a prior-art or source-branch conclusion.
