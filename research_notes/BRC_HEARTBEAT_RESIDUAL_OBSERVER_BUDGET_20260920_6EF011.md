# Residual-first: enforce the method constraint and observe relative phase

Event-ID: brc-heartbeat-residual-observer-budget-20260920-6EF011
Research-Activity-ID: RA-6EF011C2E75C4A799606AFEA
Researcher-ID: EM-DIRECT-6EF011
Status: RESEARCH_CANDIDATE; same-author proofs/checks, no independent review or admission.
Source read: enterprise-math@307e9b7d94323abee1c0f8a7942f57509a126efc; local parent8406428.

## User constraint, actually routed

The user explicitly required that imperfect/nonclosing/irregular objects not be
rejected merely for those properties. Global method policy is now published at
chatgpt-global-knowledge@0022fe677a6708dd65f6c973056c8a4183c5e4bf:
knowledge/procedures/RESIDUAL_FIRST_NONIDEAL_RESEARCH_20260920.md, with a mandatory
scoped link in BRC_RESEARCH_PRIORITY_AND_USAGE_20260905.md. Project human and machine
counterparts accompany this note. This is a method constraint, not a waiver of
correctness or a change to P000/protected worldview. It retains the strong
absolute-zero nonexistence objective as a goal, not a premise. The reference
classification fixtures do not claim that all preexisting runtime consumers
were modified. Confirmed errors are corrected and their witnesses preserved.

## A nonzero observable response, not only a nonzero remainder

Reuse E_D(t)=a^t-sum_(j<D)binom(t,j)(a-1)^j and Delta^D E_D(t)=(a-1)^D a^t.
For unit a modulo N and fixed character s, set z_j=exp(2pi i s E_D(t+j)/N)
and q=N/gcd(s(a-1)^D,N). The alternating binomial phase product is a primitive
q-th root at every t. When q>1 it cannot equal1. For the coherent D+1-time-label
observer, p_escape=1-|mean(z_j)|^2. Telescoping unit phases, Cauchy-Schwarz and
sum binom(D,j)^2=binom(2D,D) imply

 p_escape >= 8/[(D+1)binom(2D,D)q^2].

For D6, every seven-beat window has p_escape>=2/(1617q^2)>0. Global phase drops
out. This is a declared finite-window interference measurement, not automatic
interference of physical times, not temperature, and not the full Shor law.
For q1 this character is blind. The bound can shrink with scale; physical
preparation/sensitivity costs and repeated-shot detection are not free.

At the hard modulus18446743979220271189,a2,t0 the residual window is exactly
(0,0,0,0,0,0,1). For s1 the response is approximately1.420611959655323e-38;
for s=(N-1)/2 it is approximately0.48979591836734694. Same residual, different
phase coupling. Both have192-bit outward integer enclosures. General huge
start times require only seven modular-power queries, not a trajectory table.
The constant-phase counterexample correctly has zero response.

## Finite resource budget preserves a positive cooling residual

For a finite target with dS levels and g ground levels, initial least eigenvalue
muS>0, and independent full-rank ancillas of dimensions d_j and least eigenvalues
mu_j>0, any joint unitary followed by discarding ancillas obeys

 p_exc >= (dS-g)muS product_j(d_j mu_j).

Let B=-sum ln(d_j mu_j). A bounded total B gives a uniform positive lower bound,
including all finite resource sequences within that budget and limits of their
target states. Approaching exact ground support requires unbounded B or leaving
a premise. For positive-temperature finite-bandwidth Gibbs resources,
B<=sum beta_j W_j supplies a physical-parameter upper bound. This is a specified
spectral resource budget, not automatically time/work or a universal state axiom.
Pure resets, selected-outcome postselection and unaccounted pure controllers are
excluded. Correlated pure states with full-rank marginals are an explicit boundary.
A fixed-gap thermal-qubit temperature can be inferred from p_exc; arbitrary
phase motion or nonthermal variance cannot be called temperature.

## Retain tiny tails while compressing multiplicity

For system spectrum(1-p,p) and k identical independent bath qubits(1-e,e), all
2^(k+1) joint eigenvalues form2(k+1) exact integer-weight groups with binomial
multiplicity. Sort these groups and consume the lowest2^k weights with their
counts. The result is the SHARP unrestricted-unitary excited-population minimum,
by the inherited stage15 spectral theorem. No tiny positive weight is dropped.
This is polynomial in k with charged big-integer arithmetic, not in log k;
not a method for arbitrary correlated resources or efficient physical control.

Executed p1/3,e1/4,k1024:2050 groups for2^1025 eigenvalues; exact rational
p_min approximately2.225134879663041e-66. Median certificate computation3.409749ms
in three serial runs, no CPU pinning; physical cooling time is not measured.
For k1,2,4,8,32,128,512 the respective minima are0.25,0.1875,0.12109375,
0.05613708496,0.00106784846,5.76488598e-10,3.02408984e-34.
A finite resource budget has a positive floor; no scale-independent universal
positive temperature is inferred as resources grow.

## Checks, boundaries, persistence

Passed:14448 exact phase-difference checks,8208 constant-phase exclusions,
180 numerical reference visibility inequalities,180 gauge invariances,192
integer phase enclosures,128 exact compressed-spectrum comparisons,128
heterogeneous resource bounds,48 rational coherent-unitary checks,64 constraint
fixtures,6 boundary witnesses and3 integer-only AST audits. Frozen45-run plan:
18 phase observations plus27 resource certificates. Same author; no independent
review, Lean or complete Enterprise Math regression. Production reuses unchanged
stage15 residual/spectrum and stage6 Dyadic interfaces; floats occur only in
separate reference decimals. No new Shor speedup or universal thermodynamic
nonexistence theorem is claimed.

Prior art: Ticozzi--Viola Sci Rep4,5192(2014); Wu--Segal--Brumer Sci Rep3,1824(2013);
Masanes--Oppenheim Nat Commun8,14538(2017). Finite differences, characters,
Cauchy-Schwarz, spectral optimization and binomial grouping are classical.

Next: derive a costed Heartbeat state-preparation and Hamiltonian/temperature
bridge connecting the explicit phase observer to the allowed physical resource
class, without imposing the desired absence of zero temperature as an axiom.
The complete cumulative code/proof/history bundle remains a standalone
reproducer, not the entire EM repository. Actual upload hashes and readbacks
must be reported only after the corresponding publication happens.
