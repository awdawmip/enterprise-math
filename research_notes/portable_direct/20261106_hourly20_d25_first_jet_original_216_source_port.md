# D25 — direct original-216 first-jet source port and observer-scoped exceptional cancellation

Date 2026-11-06. Status: **AUTHOR-PROVED / EXACT ALGEBRA / 207 PRIME CHECKS / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CHECKPOINT**.
Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`.
This is a portable author calculation, not the native H0/B0 or Frobenius experiment.

## Precise source maps

For every prime p=6m+1>=7 let a=2m,b=3m,c=4m; 0<=j<p. Over p-local rationals define original 216 coefficient
`h_j=2^(-j)*(1/2)_j*(1/3)_j*(2/3)_j/(j!)^3` and `W_p=sum_j (6j+1)h_j`.
Define the independently lifted regular binomial coefficient
`U_j=2^(-j)*(-a)_j*(-b)_j*(-c)_j/(j!)^3` for 0<=j<=a.
Over F_p[[t]] define
`M_j(t)=(-1/2)^j binom(a+t,j)binom(b+t,j)binom(c+t,j) j!/(1-3t)_j`,
`u_j=M_j(0), e_j=M'_j(0), Z=sum_j u_j, S=sum_j(6j+1)e_j`.
All denominators used at j<p are p-units. Signed source labels and both p-adic and t-adic valuations are retained independently.

## Theorem 1: coefficientwise valuation bridge

For every j in [0,p-1],

```
v_p(h_j) = ord_t(M_j(t))
         = 1_{j>2m} + 1_{j>3m} + 1_{j>4m}.
```

For 2m<j<=3m, `h_j/p = -e_j/3 (mod p)`.

**Proof.** The Pochhammer numerator parameters 1/3,1/2,2/3 first encounter an integer multiple of p at j=2m+1,3m+1,4m+1 respectively. Each contributes exactly one p in j<p; the binomials of M have one t-zero at the same thresholds. Within the single-carry shell only (-a)_j vanishes. The original parameter `1/3=-a+p/3` gives +1/3 of the first zero derivative, while M has upper parameter `-a-t`, giving -1 of the same derivative. All other factors agree modulo p. Hence h_j/p=-e_j/3. This proof does not divide by the vanishing base coefficient. QED.

## Theorem 2: whole-sum mod p^2 observer port

For 0<=j<=2m define
`D_j = sum_{r=0}^{j-1} [1/(3(r-a)) + 1/(2(r-b)) + 2/(3(r-c))] (mod p)`, D_0=0.
Then

```
W_p = sum_{j=0}^{2m} (6j+1)U_j
    + p * [sum_{j=0}^{2m} (6j+1)(U_j mod p)D_j
           -(1/3)*sum_{j=2m+1}^{3m} (6j+1)e_j]    (mod p^2).
```

**Proof.** The exact upper-parameter shifts are
`1/3=-a+p/3, 1/2=-b+p/2, 2/3=-c+2p/3`.
For regular indices no numerator factor vanishes, so first-order product expansion gives `h_j=U_j(1+pD_j) mod p^2`. Theorem 1 gives the single-carry contribution; all j>3m have p-adic valuation at least two and disappear modulo p². Sum with exact signed weights. The identity is unconditional and does not require beforehand that p divides W_p. QED.

## Theorem 3: exceptional pair is invisible only to the first-order Theta readout

If p divides W_p, inherited `Theta_p=W_p/p-Z+S/6 (mod p)`.
At j=m the weight is exactly 6m+1=p and
`h_m-u_m+(p/6)e_m=0 (mod p)`: its separate contribution to Theta is zero.
At j=5m the original h has valuation 3, while M has t-order 3; its contributions to W_p/p modulo p, Z and S all vanish. Thus the labelled pair (m,5m) is invisible to this *specific* first-order scalar observer. No termwise splitting of the other potentially nonintegral W_j/p terms is asserted.

The inherited exact reciprocal `M_m(0)*[t^3]M_{5m}(t)=m^(-2)` and its five-jet extension remain valid higher-jet source data; their invisibility to Theta does **not** prove redundancy for future p-adic/Frobenius observables. The appropriate remaining Theta dependency is the regular/single-carry first-order sum, rather than the complementary triple-carry coefficient by itself.

## Verification and next

Independent exact integer implementation (original h recurrence modulo p²; regular U and D; two-register u/e derivative recurrence) verified: each regular-index Taylor relation; each one-carry h_j/p map; full weighted W_p identity; exceptional pair; and first-digit examples for **all 207 primes p<=3000 with p=1 mod 6: 207/207 PASS**. All 207 had Theta=0 in this finite test, not a general Theta proof.

Examples `(p, h_m mod p, Z, S, S_singlecarry, W_p/p mod p, Theta)`:
`(13,6,0,7,8,1,0)`; `(19,8,0,13,17,1,0)`; `(373,122,0,367,292,1,0)`; `(1009,184,482,868,863,1,0)`.
Finite verification is a sign/implementation check distinct from the universal algebraic proofs.

Continue by looking for an exact first-order telescope for the regular + one-carry source against original W_p/p, starting p=13,19,373 and without redoing earlier four-shell, Clausen and five-jet results. Frozen mother objective remains `Delta_p-R_p=0 mod p` for p=13,19 mod24. Original-class H0/B0, [X]U mod p², Frobenius eta/kappa, odd branch and independent review remain open. BRC readout must retain p-adic/t-order, signed weight, regular/carry provenance and later operations before any projection.

## Status separation

Original read requests `em-h20-20261106-1030-d25-task-r11` and `em-h20-20261106-1030-d25-cont-r11` were reconciled to SUCCEEDED at pinned Source `8aacd7312fd930dcf093c942730cc887c0005367`; existing `SOURCE_BYTES_AND_RECORDED_CLAIM_VERIFIED` preserved. They do NOT establish current execution authority. No service-issued current Researcher identity, winning CLAIM, OPEN, native checkpoint, Result, admission or independent review is claimed. The previous session's protected staging remains unverified. This file is author-side durable evidence only.

## Corollary 4: compensated first-order telescope with exact exceptional-index removal

Assume p divides W_p (the inherited first-digit premise), and put
`T=sum_{j=0}^{2m}(j-m)U_j` over p-local rationals.
Write `C=sum_{j=0}^{2m}(6j+1)(U_j mod p)D_j` and
`S_regular=sum_{j=0}^{2m}(6j+1)e_j`.
Then `T` is p-integral **and divisible by p**, and the full first-order target is exactly

```
Theta_p = (6*T)/p + C + (S_regular - S_singlecarry)/6 (mod p).
```

**Proof.** Put `B=sum_{j=0}^{2m}(6j+1)U_j` and
`Z0=sum_{j=0}^{2m}U_j`. Since p=6m+1,
`B-p*Z0=6*T` as an exact p-local identity. Theorem 2 and
`p|W_p` imply `p|B`, hence `p|T`; and `Z0 mod p=Z`.
Divide Theorem 2 by p, use `S=S_regular+S_singlecarry`, and
substitute `B/p-Z0=6*T/p`. QED.

At the **exceptional** index j=m, each of the three terms on the
right has an identically zero coefficient: `j-m=0` in T and the
weight `6m+1=p` vanishes mod p in C and S_regular. Index j=5m is
outside the regular and one-carry shells entirely. This is therefore a
strict **observer-scoped** elimination of the exceptional pair from
the *first-order* Theta readout. The earlier nonzero t^3/t^4/t^5
reciprocal transfer remains essential for higher-jet/future
observers; no higher-order information, p-adic source branch or
native original-class state is erased by this corollary.

The independent modular verifier also checked the compensated
moment identity at all **207/207** primes p=1 (mod 6), p<=3000.
The first-order telescoping target has not thereby been universally
evaluated: the next nontrivial problem is to prove the displayed
combination vanishes by finite summation/WZ, retaining full labelled
regular and one-carry provenance.
