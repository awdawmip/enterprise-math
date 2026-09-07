# Independent analytic audit of the RH energy-domain correction

Status: **PASS_WITH_CLASSICAL_INPUTS / INDEPENDENT_DOMAIN_AND_LIMIT_CHECK**.
Date: 2026-09-07. Role: `ANCHOR_EXPOSED` internal owner helper, not an official
review, allocated Researcher-ID, registered claim, or Foundation promotion.

**Conclusion.** The correction to the original energy domain is necessary,
and the corrected note's analytic arguments are valid. The original unshifted
P2 makes every full energy with sigma at least 2 diverge at zero, independently
of RH. The two corrected energy families are RH-equivalent using explicitly
identified classical inputs. This audit does not establish their asserted
finiteness and does not prove RH.

## Audited bytes and independent evidence

| Read-only input | SHA256 |
|---|---|
| `OWNER_RH_ENERGY_DOMAIN_AUDIT_20260907.md` | `db1dd64e4e4e709fd150c3909102efb862d07e83847b076d9efbe3096910819d` |
| `owner_rh_energy_domain_20260907_check.py` | `5a043e15b1fcbfe7374a30296c84366a925644045560ac409409eff8fc72cbcf` |
| `RH_X6_BRC_TRANSPORT_FRONTIER_20260906.md` | `693a7b2888d3eb72faca74c7d166a8af78caa9107bbf532aea918e9085873412` |

The historical definition inspected directly is

`P2(x)=sum_(n>=1) mu(n)n^(-2) exp(-x/n^2)`

and its full energy is
`E_sigma=integral_0^infinity |P2(x)|^2 x^(1-sigma) dx`.
No constant was subtracted in that definition. This audit concerns the energy
and kernel statements, not all the other routes in the historical frontier.

The new independent checker
`owner_rh_energy_independent_audit_20260907.py` has SHA256
`6a30637c687a475c53fe1342ff56ec6320a73a5ec53bf5e0df7bf77e92371253`.
Its complete output is
`owner_rh_energy_independent_audit_20260907.json`. It imports no author code
and checks only finite rational boundary calculations. The proofs of
convergence, holomorphy, and infinite limits are the analysis below; neither
the author's script nor this additional script can substitute for them.
All four recorded input hashes were checked before and after execution.

## 1. Zero-end divergence and the two valid corrections

For x>=0, every summand has absolute value at most n^(-2). The uniformly
absolutely convergent series is therefore continuous and bounded, including
at zero. Without evaluating zeta(2), the direct estimate

`P2(0) >= 1 - [1/4 + integral_2^infinity t^(-2)dt] = 1/4`

is valid. Moreover,

`|P2(x)-P2(0)| <= x sum_n n^(-4) <= 4x/3`.

Thus P2(x)>=1/6 on [0,1/16]. Upper boundedness and this positive lower bound
make the local energy comparable to the integral of x^(1-sigma).
It converges at zero exactly when sigma<2. At sigma=2 the divergence is
logarithmic; above 2 it is a power divergence. In particular, at sigma=5/2
and epsilon=(1/16)4^(-j), the integral from epsilon to 1/16 is at least
`(2/9)(2^j-1)`. This already disproves the historical claim involving
every sigma>1/2, regardless of RH.

The valid alternatives are:

- Full energy for every `1/2<sigma<2`.
- Tail energy `integral_1^infinity |P2(x)|^2 x^(1-sigma)dx` for every
  `sigma>1/2`.

These families are equivalent to one another. Tail finiteness supplies the
full energies below 2 because their zero ends are integrable. Conversely,
the full family supplies the tail for sigma<2, and any fixed sigma_0 in
(1/2,2) dominates the tail weights for all sigma>=2 on x>=1. The tail
correction changes the declared integral and must also change its kernel.

## 2. Ordinary Gram kernels versus Gamma continuation

With `f_n(x)=n^(-2)exp(-x/n^2)` and `a=m^(-2)+n^(-2)`, substituting y=ax
in the ordinary pair integral gives, for real sigma<2,

`K_sigma(m,n)=Gamma(2-sigma)(m^2 n^2)^(-1)a^(sigma-2)`.

Using `a=2 cosh(log(m/n))/(mn)` produces exactly the historical sech form.
At sigma=1/2 its coefficient is `sqrt(pi)/2^(5/2)`. There is no missing
factor of two. Every individual pair has exponential decay at infinity;
its only domain restriction is the zero-end condition sigma<2.

On that domain, every finite coefficient vector has the exact quadratic
form integral of its squared finite sum, so the matrix is positive
semidefinite. This reasoning uses ordinary integrals and cannot be extended
just by continuing the Gamma factor. Euler's Gamma integral applies for
positive real part of its parameter; elsewhere Gamma is defined by analytic
continuation. [NIST DLMF §5.2](https://dlmf.nist.gov/5.2)

At sigma=5/2 and m=n=1 the continued expression is
`sqrt(2)Gamma(-1/2)=-2sqrt(2pi)`, a negative diagonal entry. The actual
positive pair integral is +infinity. A one-by-one negative matrix cannot
be the original positive Gram matrix. Cancellations in special finite
coefficient combinations do not repair the missing full Gram matrix of
individual f_n vectors.

For the tail integral, the correct kernel is instead

`K_tail(sigma;m,n)=(m^2n^2)^(-1)a^(sigma-2) Gamma(2-sigma,a)`,

where the upper incomplete Gamma is its integral from a>0 to infinity.
It is positive and finite for every real sigma, because the lower endpoint
is bounded away from zero and exponential decay controls infinity. This
gives a valid finite tail Gram matrix for all real sigma. It is a different
kernel, not the continued value of the original full integral.

## 3. Exact absolute-Fubini domain

Let `A_x=sum_n |mu(n)| n^(-2)exp(-x/n^2)`. Tonelli identifies the sum of
absolute pair integrals with `integral A_x^2 x^(1-sigma)dx`, allowing
infinity. For sigma<2 the individual kernels are finite, so this is exactly
the absolute double-series question.

Near zero A_x has a finite positive limit. At infinity, its two-sided
comparison with x^(-1/2) has an unconditional proof. For the upper bound,
drop |mu(n)| and compare the single-peaked positive function
`t^(-2)exp(-x/t^2)` with its integral plus at most two maximal terms. The
integral is `sqrt(pi)/(2sqrt(x))` and the maximum is 1/(ex). For the lower
bound, the identity `mu(n)^2=sum_(d^2|n)mu(d)` gives

`Q(t)=sum_(n<=t)mu(n)^2=t/zeta(2)+O(sqrt(t))`.

Indeed there are O(sqrt(t)) floor errors; replacing the truncated sum of
mu(d)/d^2 by its absolutely convergent infinite sum contributes another
O(sqrt(t)). Hence [sqrt(x),2sqrt(x)] contains order sqrt(x) squarefree
integers for sufficiently large x. Each contributes at least e^(-1)/(4x).
This establishes both comparisons without RH or a pointwise Möbius bound.

The two ends are consequently controlled by x^(1-sigma) near zero and
x^(-sigma) near infinity. The absolute full double sum is finite **exactly
for 1<sigma<2**. The absolute tail double sum is finite exactly for sigma>1.
At sigma=1 the latter diverges logarithmically; at sigma=2 the former has
zero-end divergence. No RH assumption changes these positive-carrier facts.

This leaves room for signed energy cancellation when sigma<=1. Failure of
absolute Fubini there does not prove divergence of the signed energy.
Conversely, a finite signed energy would not by itself prove the absolute
double sum finite. The corrected note preserves this distinction.

## 4. Ordered limits and the squared L2 truncation error

On a fixed window [delta,R], 0<delta<R<infinity, uniform convergence of
P2_N implies convergence of squared integrals. Every finite sum can first
be integrated on that window. Only after that N limit does monotone
convergence apply as the positive integration window expands. It applies
to the nonnegative integrand/window, not to the sequence of signed finite
Gram quadratic forms. A concrete check at sigma=1 gives

`E_1(P2_1)=1/2`, while `E_1(P2_2)=9/40`.

The latter is smaller by 11/40. Thus the N sequence is not monotonically
increasing, even though each individual Gram matrix is positive definite.
The author's stated `lim_J lim_N` window contract is correct.

Now impose the separate arithmetic assumption `|M(t)|<=C t^theta` for
t>=1, with `0<theta<sigma<2`. For integer N, partial summation of the tail
has the exact boundary term

`R_N(x)=-M(N)f_x(N)-integral_N^infinity M(t)f_x'(t)dt`,

where `f_x(t)=t^(-2)exp(-x/t^2)` and
`f_x'(t)=2t^(-3)exp(-x/t^2)(x/t^2-1)`.
The boundary term at infinity vanishes because theta<2. For x<=N^2,
absolute integration gives a bound C_theta N^(theta-2). For x>=N^2,
the substitution u=x/t^2 makes the derivative integral a constant times

`x^((theta-2)/2) integral_0^(x/N^2) u^(-theta/2)e^(-u)(1+u)du`.

That u integral is uniformly bounded because theta<2. The boundary term
has the same bound, since a^((2-theta)/2)e^(-a) is bounded for a>=1.
Thus the author's two-zone pointwise estimate is correct, with a constant
that includes the assumed Mertens constant C.

Squaring and integrating on [0,N^2] and [N^2,infinity] yields

`||R_N||_sigma^2 <= C_theta^2 [1/(2-sigma)+1/(sigma-theta)] N^(2(theta-sigma))`.

The first power follows from
`N^(2theta-4)(N^2)^(2-sigma)`; the second from integrating
x^(theta-sigma-1). Both are `N^(2(theta-sigma))`, not an exponent with a
missing factor of two. The stated rate concerns the **squared** L2 norm;
the norm itself is O(N^(theta-sigma)). Both denominator conditions are
strict and correctly recorded.

Each P2_N is in the full L2 space because sigma<2. The tail bound therefore
also proves that P2 belongs to this space and that the norms converge.
This justifies the particular square cutoff m,n<=N in the infinite Gram
expression. It does not authorize arbitrary rearrangements of a
non-absolutely convergent double series. The Mertens hypothesis is not
deduced from finite Gram values.

## 5. Both RH implications and the exact external dependencies

The [Agarwal–Garg–Maji paper](https://arxiv.org/pdf/2202.00637) was read
directly. Its equation (1.5), printed page 2, states the classical Riesz
criterion for this same P2. Theorem 1.2 is on printed page 3 and has a proof
in §3. Equation (3.20), printed page 10, invokes Littlewood's RH-implies-
Mertens estimate as a classical input; that estimate is not proved there.
The local correction likewise **cites**, rather than independently proves,
these classical inputs. Theorem 1.2's criterion does not require the
simple-zero assumption of the paper's separate Theorem 1.1.

For the forward implication, the cited bound
`P2(x)=O_epsilon(x^(-3/4+epsilon))` makes the energy tail integrable whenever
`2epsilon<sigma-1/2`; zero-end integrability requires sigma<2. Alternatively,
the local partial-summation estimate just checked proves this implication
directly from the classical RH bound `M(t)=O(t^theta)` for every theta>1/2:
choose theta<sigma. Thus it need not borrow the cited paper's problematic
cross-domain Mellin integral formula.

For the converse, assume every full energy in 1/2<sigma<2 is finite.
Define the ordinary Mellin integral

`F(s)=integral_0^infinity P2(x)x^(s-1)dx`.

At zero it converges absolutely when u=Re(s)>0. For any u<3/4 choose
`1/2<sigma<2-2u`. Cauchy–Schwarz bounds its absolute tail by

`E_sigma^(1/2) [integral_1^infinity x^(2u+sigma-3)dx]^(1/2)`,

which is finite because the exponent is strictly below -1. On each compact
substrip 0<a<=Re(s)<=b<3/4 choose the same sigma with strict slack at b.
The same integrals with any fixed power of log(x) remain finite at both
ends. Differentiation under the integral, or an equivalent dominated
holomorphy argument, now proves F holomorphic on 0<Re(s)<3/4. The ordinary
integral's holomorphy is established before invoking any continuation.

In the smaller strip 0<Re(s)<1/2, absolute summability of
`Gamma(u)sum_n |mu(n)|n^(-2+2u)` justifies termwise Mellin integration and
the absolutely convergent Möbius Dirichlet identity. Thus

`F(s)=Gamma(s)/zeta(2-2s)`

there. Both sides are meromorphic on the connected larger strip, so their
identity extends there. Gamma is finite and nonzero throughout that strip;
its poles are confined to nonpositive integers and it has no zeros.
[NIST DLMF §5.2](https://dlmf.nist.gov/5.2)

Any zeta zero rho with Re(rho)>1/2 in the nontrivial strip would give a pole
of the right side at `s=1-rho/2`, inside the established holomorphy strip.
This is impossible, regardless of the zero's multiplicity. The zeta pole
at 1 instead gives a zero of 1/zeta at s=1/2; it is not a pole of F and is
not an obstruction. Zeta's unique pole is simple, with residue one.
[NIST DLMF §25.2](https://dlmf.nist.gov/25.2)

The standard functional equation and nontrivial-zero reflection symmetry
then exclude zeros left of the critical line as well, giving RH under the
assumed energy family. These are classical facts, not newly proved here.
[NIST DLMF §25.4](https://dlmf.nist.gov/25.4),
[NIST DLMF §25.10](https://dlmf.nist.gov/25.10)

The parameter inequalities are strict. Neither argument establishes the
critical energy at sigma=1/2. A single energy at a fixed sigma is also not
the full quantified family: approaching sigma=1/2 is what reaches the
entire Mellin strip up to, but not including, Re(s)=3/4.

## 6. Explicit boundary in the cited Mellin formula

The cited paper's Lemma 2.4 writes an integral beyond its ordinary convergence
range. With k=2 and its variable s=1/4, its left side is
`integral_0^infinity P2(x)x^(-5/4)dx`. The proven positive lower bound makes
its zero end diverge to +infinity; its tail is absolutely convergent simply
because P2 is bounded. Its displayed right side is
`Gamma(-1/4)/zeta(5/2)`, a finite negative number. Consequently the wider
formula can only be used as a continuation statement, not as equality with
that ordinary integral. [Agarwal–Garg–Maji, Lemma 2.4](https://arxiv.org/pdf/2202.00637)

This is a concrete source-domain limitation. It does not invalidate the
local correction, which explicitly avoids that step and establishes the
needed Mellin holomorphy directly from its energy assumption. This audit
does not certify every proof or every formula in the external paper.

## Actual finite guard run and final scope

```text
python -X utf8 research_notes/owner_rh_energy_independent_audit_20260907.py
exit_code: 0
status: PASS
elapsed_seconds: 0.109
zero_lower_on_0_to_1_over_16: 1/6
L2_squared_tail_exponent_cases: 19
N2_minus_N1_Gram: -11/40
continued_sigma_5_over_2_diagonal_over_sqrt_2pi: -2
```

The checker independently calculates eight rational sigma=5/2 divergence
lower bounds, seven endpoint-domain cases, six admissible Mellin-CS parameter
choices, nineteen L2 exponent identities, and positive leading principal
determinants of the actual sigma=1 kernel through size eight. Its Möbius
coefficients use a divisor recurrence, independently of the author's
factorization routine. These are finite guard checks. The recorded time
does not certify asymptotic computational complexity or analytic convergence.

No correction to the audited new note or checker is required. The historical
unrestricted energy claim remains false and is repaired by the separate
domain note; no historical file was edited. Full finite Gram positivity,
infinite signed energy, absolute pair summation, and a permitted cutoff
limit remain distinct contracts. General kernels involve real transcendental
values and are not automatically exact rational BRC branch weights.
Positive BRC carriers and the final Möbius signed observation stay separately
typed. This work neither alters P000/X6 nor claims to have proved RH.

Global-Knowledge-Sync: main@4fa7d7d / GLOBAL_KNOWLEDGE_V1
