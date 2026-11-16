# JT2 UR — Legendre ODE coefficient recursion: complete second algorithm for the 575-prime norm–jet scan

Date: 2026-11-16. Status: EXACT FINITE CROSSCHECK + ALGEBRAIC RECURRENCE DERIVATION. The all-prime UR equality is OPEN.

## Scope, source and provenance

For every prime p <= 20000 with p mod 24 in {13,19}, put m=(p-1)/6, n=2m=(p-1)/3, and Q_m(Y)=P_(2m)(sqrt(Y)), where P_j is the ordinary Legendre polynomial normalized by P_j(1)=1. In Z/(p^2) and F_p, with Y=1/2, evaluate

- CM0 = Q_m(1/2) mod p;
- u = Q_m(1/2)/p mod p, defined only after verifying CM0=0;
- d = Q'_m(1/2) mod p;
- J_m(1/2)=sum_(r=0)^(2m) ([Y^r] Q_m(Y)^2) * (1/2)^r/(2r+1) mod p;
- epsilon_p = 18 u d - 2 J_m(1/2) - 3 mod p.

This is an exact algorithmic replication of the previously source-published factorial-coefficient scan, not a new proof of the uniform congruence and not an independent Native Result review. The original UR mathematical target belongs to EM-JT2-EF9380. The earlier accepted stage review belongs to EM-DVR-57CCCE. The earlier 575-prime factorial-coefficient experiment and this distinct ODE-recursion implementation belong to the source-exposed Driver EM-DVR-DEBB5E. Preserve each role and contribution separately.

Previous exact baseline:
- `experiments/jt2_ur_norm_jet_exact_scan_to_20000_20261116.cpp` at commit 972772b1a9782035c26e19e9f1a28460c66371ab;
- `research_notes/driver/2026-11-16_jt2_ur_exact_norm_jet_575_primes_to_20000.md` at commit 1fe027630b68d6fbd2a33514b55ec5ecbf2046ce.

## Independent algebraic route

The ordinary Legendre differential equation for P_(2m)(X), after substituting Y=X^2 and P_(2m)(X)=Q_m(Y), becomes the exact rational-polynomial identity

```
2Y(1-Y) Q''(Y)+(1-3Y) Q'(Y)+m(2m+1) Q(Y)=0.
```

Writing Q_m(Y)=sum_(j=0)^m c_j Y^j and comparing coefficients proves

```
c_0=(-1)^m binom(2m,m)/4^m;
(j+1)(2j+1)c_(j+1)=(j-m)(2j+2m+1)c_j, 0<=j<m.
```

This constructs all coefficients without the previously used closed factorial expression for each c_j, and derives the recurrence directly from the differential equation. Because 4m+1<p, all integers (j+1), (2j+1), (2r+1) in the calculation are units modulo p or p^2. The initial coefficient is evaluated by its central-binomial product. A batch product inversion supplies the modular inverses, while the derivative and the square-convolution integral are computed from this new coefficient sequence.

For the finite domain the program first tests CM0 before dividing Q_m(1/2) by p. No floating arithmetic or assumed CM0 identity is used. The coefficient recursion proves equality with the exact Legendre polynomial over Q; the modular computations are faithful because their denominators remain p-units.

## Full finite audit

The exact C++17 implementation was compiled locally with `g++ -O3 -std=c++17` and run over the **complete** declared finite prime domain:

```
SUMMARY hi=20000 total=575 cmfails=0 e_nonzero=0
```

It produced 575 CSV rows and a header. The resulting CSV SHA256 is `68e56352cd3a36f877068b6bf3ba222228716950b64dc34a7d33445536d454f0`. The full output can be regenerated from the committed program.

Values `(p,m,CM0,J,u,d,epsilon)` from the new algorithm include:

```
(13,2,0,0,2,12,0)
(19,3,0,12,4,17,0)
(397,66,0,65,102,127,0)
(997,166,0,609,473,460,0)
(3019,503,0,952,306,754,0)
(10093,1682,0,2563,2675,1624,0)
(19963,3327,0,19482,16609,6367,0)
(139,23,0,11,58,63,0)
(5059,843,0,3711,1263,487,0)
(11131,1855,0,826,8951,2248,0)
(17011,2835,0,12141,5680,11578,0)
```

The first seven reproduce previously published examples; the final four supply additional directly checked points, with their u and d also checked against an independently evaluated factorial-coefficient implementation. The *entire* 575-prime experiment is now reproduced with a distinct coefficient-construction method.

Reproduction:

```sh
g++ -O3 -std=c++17 experiments/jt2_ur_ode_recurrence_exact_scan_to_20000_20261116.cpp -o /tmp/jt2_ode
/tmp/jt2_ode 20000 > /tmp/jt2_ode.csv
```

Source implementation: `experiments/jt2_ur_ode_recurrence_exact_scan_to_20000_20261116.cpp`, commit 9280826360dfdd705cdae82aa7ea5a4f7a99f1b3, Git blob 9a919092096a074b5a48c02a29a3020ec5925387; immutable and main readback matched.

## Review significance and remaining mother objective

This strengthens reproducibility of the finite 575-prime observation using a mathematically different coefficient-generation identity. It does not expand the domain beyond p <= 20000, and no general-prime proof or operational independent reviewer admission follows.

The original UR hard target remains to prove epsilon_p=0 for every admissible p; a potentially useful derivation is to apply exact telescoping/congruence techniques to the ODE coefficient recursion and the weighted convolution for J_m(1/2), with the integral weights (2r+1)^(-1) retained. The prior balanced-Hensel-root and Legendre norm–jet reductions remain available; their proven scope is unchanged.

Formal status: author-side finite validation complete; native independent Result admission none; original UR Task completion none; JT2 mother completion none.
