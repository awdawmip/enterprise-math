# D25 — a signed two-variable tangent discriminator for the original 216/2304 full sums

Date: 2026-11-09 (Asia/Hong_Kong). Classification: AUTHOR-SIDE / EXACT FINITE EXPERIMENT + PROVED CONDITIONAL JET LEMMA / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE.

Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`. Publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Logical Research lane `chatgpt-research-onhour-enterprise-math-20260923`, never the separate maintenance lane. P000 ACTIVE_LOCKED is unchanged; these finite hypergeometric sums are external scalar observations, not native X6/H0/B0.

## Consumed precedent and actual new scope

The affine fourth-digit candidate `W_p-2V_p+p*chi_{-3}(p) == 0 mod p^4` was **already reported on 2026-10-31**, and checked on ALL **1,752** primes 5<=p<=15,000 in `research_notes/portable_direct/20261031_onhour_d25_affine_p4_216_2304_bridge.md`. The 2026-11-09 174-prime affine scan is strictly weaker and must not be recredited as a discovery. Prior Oct29/31 top-tier p^4 reflection/port identities also remain completed. This note investigates a **different two-variable first and second jet**, not the old univariate affine scan.

For prime p>3, in Z_(p), retain the exact weighted full-cutoff polynomials

```
a_n=(2n)!(3n)!/((n!)^5*216^n)
b_n=(4n)!/((n!)^4*2304^n)
W_p(x)=sum[n=0..p-1] (6n+1)*a_n*x^n
V_p(y)=sum[n=0..p-1] (8n+1)*b_n*y^n
chi=legendre(-3,p) = +1 if p=1 mod 3, else -1.
D_p(x,y)=W_p(x)-2*V_p(y)+p*chi.
```

The original scalar target is D_p(1,1)==0 mod p^3 (a weaker consequence of the already-observed affine p^4 conjecture). No parameter deformation replaces that fixed-point target.

## Newly observed finite-field tangent congruence (CONJECTURE, NOT PROVED UNIVERSALLY)

Define the exact modulo-p first derivatives

```
A_p=W'_p(1)=sum[n=0..p-1] n*(6n+1)*a_n mod p,
B_p=V'_p(1)=sum[n=0..p-1] n*(8n+1)*b_n mod p.
```

The discriminating candidate is

```
3*A_p + 8*chi*B_p == 0 mod p.             (TANGENT CANDIDATE)
```

Actually executed exact modular recurrences for all **548 primes 5<=p<4000**: **zero failures**. No B_p zero occurred within this finite set; no universal invertibility theorem is asserted. Eight independent direct integer-binomial checks at p=5,7,13,19,37,43,73,373 match the recurrence modulo p^2, including their original signed weights. This is a new finite observation; an all-prime derivation is an open obligation.

Small witnesses for (p,chi,A_p,B_p) are (13,+1,3,7), (19,+1,12,5), (373,+1,292,77). The last gives 3*292+8*77=1492=4*373, with original classes and signs preserved.

## PROVED exact first- and second-jet transfer, any p>3

For all integers u,v and p>3, because these are finite polynomials with coefficients in Z_(p), the binomial theorem proves

```
D_p(1+p*u,1+p*v) == D_p(1,1)
   +p*(u*W'_p(1)-2*v*V'_p(1))                 (mod p^2).       (J1)
```

The exact next digit (with 2 invertible) is

```
D_p(1+p*u,1+p*v) == D_p(1,1)
  +p*(u*W'_p(1)-2*v*V'_p(1))
  +p^2*(u^2*W''_p(1)/2-v^2*V''_p(1))          (mod p^3).       (J2)
```

Under the experimentally observed tangent candidate, `v=-4*chi*u/3 mod p` makes the J1 linear term zero modulo p. This is a conditional implication; J1 and J2 themselves are algebraic theorems for every p>3.

When the base D_p(1,1) is divisible by p^2 and B_p is nonzero mod p, fixing x=1+p and v0=(-4*chi/3 mod p), the second-digit residual `r=D_p(1+p,1+p*v0)/p^2 mod p` is well defined if the J1 tangent test passes. Setting `w=r*(2*B_p)^(-1) mod p` then uniquely makes
`D_p(1+p,1+p*v0+p^2*w)=0 mod p^3`.
This is the direct Taylor/Hensel correction in the declared local model; it does not prove D_p(1,1)=0 for all p.

## Actual exact input/output witnesses: a failed naive path, a repaired first jet, and nonzero second-jet defects

At each anchor below D_p(1,1)==0 mod p^2 was separately checked using the original exact sums, and the following deformations were rechecked by *independent literal binomial sums*, not only recurrence/Taylor expansion.

| p | A mod p | B mod p | common-shift D_p(1+p,1+p) mod p^2 | v0=(-4chi/3) mod p | D_p(1+p,1+p*v0) mod p^2 | r mod p | unique w mod p |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 13 | 3 | 7 | 26 | 3 | 0 | 7 | 7 |
| 19 | 12 | 5 | 38 | 5 | 0 | 18 | 17 |
| 373 | 292 | 77 | 51474 | 123 | 0 | 348 | 259 |

For p=13,19,373, the corrected first jet does **not** itself lift to p^3: r=7,18,348 are nonzero. Adding the displayed p^2*w correction makes the literal D vanish mod p^3 in all three cases. These are exact finite counterexamples to the *specific naive common-shift* and *uncorrected second-jet* claims, not counterexamples to the original fixed-point p^4 conjecture. The adapted tangent is a concrete new parameterization to investigate through finite-field/hypergeometric transformations.

## Reproducibility and evidence

The exact standalone standard-library Python checker `d25_affine_two_variable_tangent_reproducer_20261109.py` tests all 548 primes, eight independent literal-binomial anchors at modulus p^2, and original p^3 second-jet corrections at p=13,19,373. Executed output:
```
SECOND_JET 13 slope 3 defect 7 lift 7
SECOND_JET 19 slope 5 defect 18 lift 17
SECOND_JET 373 slope 123 defect 348 lift 259
PASS 548 primes, 8 independently verified binomial anchors
```

All arithmetic is exact: integer factorial/binomial, modular inverse of p-units, and finite polynomial derivatives. The experimental tangent identity is an *unreviewed conjecture within the tested finite domain*, not a claimed all-prime proof.

BRC/coordinate usage: `(p,n,original weight,source label A/B,valuation, x/y parameter, derivative order)` is a provenance-preserving carrier; the observer is the signed D_p mod p^2/p^3 jet. The J1/J2 quotient explicitly declares precision and operations. The prior scalar p^4 equality does not determine a tangent without retaining both separately labeled derivative streams.

## Highest frontier and next exact action

1. Seek a source-preserving finite-field hypergeometric/CM transformation proving or falsifying `3W'_p(1)+8chi V'_p(1)==0 mod p`; initially try the two frozen residue classes, preserving original n=0..p-1 cutoffs and weights. A proof of this derivative identity would establish only a parameter-jet relation, not the frozen mother LIFT, without further comparison.
2. Reuse the prior 1,752-prime scalar affine p^4 work and 6-port reflection; no rescan or recredit. Test whether the adapted second-jet correction has a closed finite-harmonic/CM form, with p=13,19,373 as boundary witnesses; then connect a proved identity to the original fixed point.
3. Independent native experiment remains `awdawmip/enterprise-math#1559`: original p=373 fixed H0/B0 divided-power [X]U mod139129, native rank, semilinear Frobenius/eta, signed odd Green/Hesse, original kappa/Delta-R and reproducer. On 2026-11-09 issue OPEN/unassigned; NOT_EXECUTED, PENDING_OWNER.

Formal Source read: historical own-lane session-start and continuation request IDs both SUCCEEDED. Historical Researcher EM-ENTERPRISE-4DEB43, session MCP-ecbfd1c046864bb3bff1a2e04c87d207, RA-9553E027FD14223807511263. Current recovery_status returned SESSION_CAPABILITY_REQUIRED: no current private capability, winning claim or open run verified. No source checkpoint, task Result, Driver review or mathematical admission; three historic staging objects remain independent. No attempt was made to use the maintenance lane or to replay a denied mutation.