# PREFIX-619-R6 — Exact asymmetric BRC confidence-stopping cost is a finite rational polynomial

Date: 2026-11-09 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_RATIONAL_CERTIFICATE_EXECUTED / UNREVIEWED / NOT_ADMITTED.

Frozen science pin: `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Reuse: PREFIX-610 native-derived signed-label observation law, PREFIX-613 anytime confidence e-process, PREFIX-615 neutral thinning, PREFIX-617 confidence-diameter first passage, PREFIX-618 exact integer survival certificate. No repinning of scientific inputs; original native action graph PREFIX-565 has not been re-executed here.

## Model and first-passage carrier

There are `d=2` null directions, each with positive-label probability `p_l/q`, negative-label probability `(1-p_l)/q`, and a neutral label for all other outcomes. Here `q=12` for Boolean slot 0 and `q=24` for Boolean slot 1/2. These are compressed statistics of a provenance-preserving original BRC port/slot experiment; the stated sufficiency is for the current confidence-diameter stopping decision, not arbitrary future graph operations.

Use `beta=1/40`, a p-confidence width target `delta=1/4`, and the first-passage stopping time `J_l` for each direction defined in PREFIX-618. That earlier certificate proved every sign string stops by 189 informative observations, with first possible stop at 25.

Define `A_m(k)` as the exact number of length-m binary sign strings with k positive signs whose first-passage diameter stopping event has *not yet occurred*. These are defined independently of p by

```
A_0(0)=1,
A_m(k)=1{D_beta(m,k)>1/4} (A_(m-1)(k-1)+A_(m-1)(k)).
```

The finite integer certificate in PREFIX-618 establishes `A_189(k)=0` for every k.

## Theorem — Exact cost function for every rational parameter pair

For any `(p1,p2) in [0,1]^2`, let

```
s_m(p)=sum_(k=0)^m A_m(k)*p^k*(1-p)^(m-k),   0<=m<189.
```

Then `P_p(J>m)=s_m(p)`. For each `q=12,24`, the exact expected number of native one-step trials required for **both directions** to achieve the target confidence diameter is

```
E_[p1,p2] T_q = q * (
  sum_(m=0)^188 s_m(p1) + sum_(n=0)^188 s_n(p2)
  - sum_(m,n=0)^188 s_m(p1)*s_n(p2)*C(m+n,m)/2^(m+n+1)
).
```

The right-hand side is a finite bivariate polynomial in `p1,p2` with rational coefficients. In particular, for every rational parameter pair its expectation is **an exact rational number**, and it extends continuously to p=0 and p=1 (where the sign law may be degenerate). For every permitted parameter pair,

`E_[p1,p2] T_24 = 2 E_[p1,p2] T_12`.

**Proof.** Each length-m sign string with k positives has probability `p^k(1-p)^(m-k)`; summing the surviving strings proves the first identity. The pathwise 189 bound makes every sum finite. Poissonize total native trials at unit rate and thin into two independent direction clocks, each of rate `1/q`. Under scaled time `u=t/q`, the one-direction survival function is `F_p(u)=e^(-u)sum_(m<189)s_m(p)u^m/m!`. The survival probability for their maximum completion time is `F_p1+F_p2-F_p1*F_p2`. Integrate this finite expression over u; use `integral_0^infty e^(-u)u^m/m!du=1` and `integral_0^infty e^(-2u)u^(m+n)/(m!n!)du=binom(m+n,m)/2^(m+n+1)`. The Poisson compensation identity converts duration to expected total trial count. This proves the displayed formula. The factor 2 between q=12 and q=24 follows directly (and agrees with PREFIX-615's exact neutral-thinning coupling).

## Reproducible exact special cases

The independent Fraction summation in `PREFIX619_R6_rational_parameter_cost_certificate.py`, which imports and rechecks the exact PREFIX-618 stopping carrier, returned the following slot-0 native-trial means:

| p1 | p2 | Exact-rational value, decimal display |
|---:|---:|---:|
| 1/2 | 1/2 | 2350.88710139993296743368469582 |
| 1/4 | 1/2 | 2259.00069216683390465440483899 |
| 1/4 | 1/4 | 1797.01105916920674607330395780 |
| 1/8 | 1/2 | 2257.53851901247784532746266037 |
| 1/8 | 1/8 | 1083.21790110186833216632810135 |

Exact numerators/denominators are produced by the certificate; companion `PREFIX619_R6_RESULTS.json` captures the compact run summary. The balanced line equals PREFIX-618's independently derived exact rational result.

A structural observation follows directly from these exact examples: speeding up the already easier direction gives diminishing total-cost gains if the other direction remains balanced. Both directions becoming easy produces a much larger reduction. This is a sampling bottleneck phenomenon within the declared BRC observer.

## Verification and next mathematical unit

The certificate was executed locally in Python standard-library exact arithmetic on 2026-11-09, with output `ALL_CHECKS_PASS` for the exact-reproduction checks and all five rational parameter pairs. The finite carrier's root comparisons are inherited from and rerun by PREFIX-618. No external claims of novel general sequential-inference theory are made. Related prior art is the beta-binomial mixture confidence sequence literature, including Howard et al., Annals of Statistics 49 (2021), DOI 10.1214/20-AOS1991.

Next: establish whether `E T_q` is globally maximal at `p1=p2=1/2` by proving or disproving the relevant symmetric binomial-path survival ordering. The explicit finite bivariate rational polynomial now makes an exact derivative/sign certificate possible; do not infer global monotonicity from the five listed instances.

BRC reuse resolution: `COMPOSE_APPLIED` (native signed-label sufficient observer, first-passage survivor recurrence, independent Poisson thinning); `EXTEND_EXISTING_TOOL` with exact asymmetric rational cost. This is project research provenance, not a Foundation promotion or formal Result/Review.
