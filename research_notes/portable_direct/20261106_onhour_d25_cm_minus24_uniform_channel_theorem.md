# D25 — CM(-24) uniform quadratic-character channel theorem

2026-11-06 · TASK_RESEARCH author-side · mathematical theorem with cited classical inputs · FINITE-VERIFIED · UNREVIEWED / NOT_ADMITTED.

Mother task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3` (unchanged). Research-lane historical logical ID `chatgpt-research-onhour-enterprise-math-20260923`; no maintenance-lane authority is used. Original p=373 H0/B0 issue #1559 remains NOT_RUN. Source CLAIM, run, Result and admission are NOT asserted.

## New proposition (universal, not a finite-data conjecture)

For every prime `p=6m+1>3`, in `F_p`, set

`F_m(z)=sum_{k=0}^m binom(m,k) binom(2m,k) z^k`.

Then

**`F_m(1/2)=0 (mod p) if and only if (2/p)=-1`.**

In particular, for EVERY `p≡13,19 (mod 24)` the previously empirical zero-channel `S_p≡F_m(1/2)=0 (mod p)` holds. The other character class `p≡1,7 (mod 24)` has `F_m(1/2)≠0 (mod p)`.

This statement follows from classical CM reduction/Deuring, not from the 611-prime finite check. Below we specify all morphisms, coefficients and exceptional primes. The independent review/admission state is pending.

## Proof, maintaining the exact observer correspondence

**(1) Legendre coefficient.** Set `u²=1/2` in an algebraic closure of `F_p`, and `C_u : y²=x⁶-2ux³+1`. This smooth genus-two curve has good reduction for every `p>3`: the defining degree-six polynomial has distinct roots because `u²≠1`. As `p=6m+1`, `(p-1)/2=3m`; let

`(x⁶-2ux³+1)^{3m}=sum_r c_r x^r`.

The classical Hasse–Witt (Cartier–Manin transpose convention) coefficient matrix for basis `dx/y,x dx/y` is `H=(c_{pi-j})_{1<=i,j<=2}`, up to transpose/Frobenius convention (irrelevant for zero or invertible). Since all exponents are multiples of three, `c_{p-2}=c_{2p-1}=0`. Since the polynomial is reciprocal of degree `18m`, `c_{p-1}=c_{6m}=c_{12m}=c_{2p-2}`. Hence **`H=c_{6m} I_2`**.

With `t=x³`, the coefficient is

`c_{6m}=[t^{2m}](1-2ut+t²)^{3m}`.

The Legendre generating function is `(1-2ut+t²)^(-1/2)=sum_{n>=0}P_n(u)t^n`. Since `3m=(p-1)/2 ≡ -1/2 (mod p)` and `2m<p`, coefficients up to `2m` agree modulo p; thus `c_{6m}=P_{2m}(u)` in `F_p`. The identity `P_{2m}(sqrt(1-z))={}_2F_1(-m,m+1/2;1;z)` is a terminating characteristic-zero polynomial identity. As `m+1/2≡-2m (mod p)` and all denominators `n!, n<=m` are p-units, it reduces to `P_{2m}(u)=F_m(1/2)`. Therefore the **genus-two Hasse–Witt matrix is exactly `F_m(1/2) I_2`**, preserving the scalar/valuation channel.

**(2) Two explicit elliptic quotients.** The two commuting involutions `(x,y) -> (1/x, ± y/x³)` have elliptic quotients. Put `X=x+1/x` and `Y_±=y(1±x^{-3})`. Since `x³+x^{-3}=X³-3X` and

`X³-3X+2=(X-1)²(X+2)`, `X³-3X-2=(X+1)²(X-2)`,

division by the explicit double factor gives the smooth elliptic quartics

`E_+ : v²=(X+2)(X³-3X-2u)`,
`E_- : v²=(X-2)(X³-3X-2u)`.

The two degree-two quotient maps imply a degree-power-of-two isogeny of abelian surfaces `Jac(C_u) ~ E_+ × E_-` (valid in every characteristic `p>3`).

**(3) Both quotients have CM of discriminant -24.** Their quartic j-invariants by the standard binary quartic invariant formula simplify to

`j_+(u)=432(4u-5)³ / [(u-1)(u+1)³]`,
`j_-(u)=-432(4u+5)³ / [(u-1)³(u+1)]`.

On substituting `u=1/sqrt(2)` one obtains, in either order,

`{j_+,j_-}={2417472+1707264 sqrt(2), 2417472-1707264 sqrt(2)}`.

The two conjugates are exactly the roots of the **Hilbert class polynomial for discriminant -24**:

`H_{-24}(J)=J²-4834944 J+14670139392`.

Consequently, over characteristic zero, both quotients have complex multiplication by the maximal order of `K=Q(sqrt(-6))`. The curves and isogenies have good reduction at all primes `p>3`; only 2 and 3 divide the CM field discriminant and denominators/discriminants of the displayed models.

**(4) Deuring + scalar Hasse–Witt conclude the if-and-only-if.** By the classical Deuring criterion for good reduction of CM elliptic curves at `p>3`, each `E_±` is supersingular precisely when `p` is inert in `K`; otherwise each is ordinary. For `p≡1 (mod 6)`, `(-3/p)=+1` and hence `(-6/p)=(2/p)`. Thus when `(2/p)=-1`, `Jac(C_u)` has p-rank 0; when `(2/p)=+1` it is ordinary. The p-rank is invariant under isogeny. Since the Hasse–Witt matrix computed above is the scalar `F_m(1/2)I_2`, p-rank 0 means this scalar vanishes (a nonzero scalar would yield an invertible Frobenius), whereas ordinarity means it is nonzero. This proves the claim for every p in the stated domain.

Note: the result is a finite-field scalar observer of the genus-two reduction, **not a performed original-class p=373 divided-power/Frobenius experiment**, and does not change P000 or native project geometry. The only mathematical imported results are the classical Legendre generating identity, elliptic quotient isogeny, Hilbert class polynomial/CM identification, Deuring criterion and Hasse–Witt/p-rank equivalences.

## Preservation of prior exact result and remaining target

The earlier author-side identity

`W_p ≡ S_p(S_p+12T_p)-2p² J_p (mod p³)`

retains the SIGNED, nonzero triangular boundary `J_p`. This theorem proves precisely the missing universal selector **for `S_p mod p`**. For `p≡13,19 mod24`, `S_p≡0 modp`; together with the previously accepted first-digit premise `W_p≡p modp²`, `K_p=S_p+12T_p` is nonzero modp and `(S_p/p)K_p≡1 modp`. For split-character primes, `S_p≠0` and any separately established `W_p≡0 modp` forces the complementary `K_p≡0` channel. This manuscript does not claim a new independent universal theorem for `K_p` without that additional input.

The **mother second-digit target remains open**:

`(S_p/p)K_p ≡ 1 + 2p J_p (mod p²)` on the target classes, equivalent under existing interfaces to `W_p≡p modp³` and then `Delta_p-R_p≡0 modp`. Next minimal scientific unit: derive the `p²` lift of the CM-Hasse scalar and/or trace observer, retaining `J_p`; check exact first nonzero boundary at p=13,19, then prove uniform cancellation. The native fixed p=373 H0/B0 execution (#1559) requires original same-class divided-power `[X]U mod139129`, ranks, semilinear Frobenius, eta/kappa and independent replication, still pending.

## Sources and finite exact check

* LMFDB elliptic curve search with j-invariant `2417472-1707264sqrt(2)`, CM discriminant -24: https://www.lmfdb.org/EllipticCurve/?field=2.2.8.1&jinv=-1707264%2Aa+%2B+2417472
* Class polynomial `H_{-24}` explicitly quoted in class equation source: https://scholarworks.indianapolis.iu.edu/bitstreams/71290818-6500-42e8-a39d-7cf0c39e99dd/download
* Deuring criterion discussed with a reference to Serge Lang's `Elliptic Functions` theorem: https://mathoverflow.net/questions/301745/confusion-on-supersingular-reduction-of-elliptic-curves-with-complex-multiplicat/302166 ; supporting research article https://doi.org/10.1007/s40993-023-00463-9
* Finite exact checker companion `d25_cm_minus24_channel_check_20261106.py`: 611 primes `7<=p<=10007`, including 312 inert and 299 split cases; independent Legendre and two elliptic-quartic Hasse coefficient checks for p<=199, all PASS, no floating arithmetic. Exact finite checking corroborates the proof but does not substitute for CM/Deuring.
* Prior mathematical frontier Git commit `9732d01852c7c475ea443585b58c83bb5e893237`; scientific input pin `c47e13e4aba0e006366f989d6334d443f6333ae3`.

Status: AUTHOR-PROVED / FINITE-VERIFIED / UNREVIEWED / NOT_ADMITTED; SOURCE_CLAIM_NOT_ESTABLISHED; no native experiment performed.
