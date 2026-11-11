# PREFIX-688-R6 — Exact local uniqueness for the first two low-slot crossover branches

Date: 2026-11-11 Asia/Shanghai. Research mode: independent author-side TASK_RESEARCH. Frozen scientific input: `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Source model: immutable 189-level first-stop Poissonized observer recurrence used in PREFIX-680 and PREFIX-685. This mathematical object is a finite stopping-time observer model; no native Heartbeat physical residual or X6 evolution is claimed.

## Statement

Let Y(p,z) be the maximum of two independent Poissonized first-stop clocks of the frozen 189-level model, and set

- A(z) = Var(Y(z,z)) - Var(Y(0,z)).
- B(z) = E[Y(z,z)] - E[Y(0,z)].
- F_q(z) = q A(z) - B(z).

The two precise assertions are:

**(I) For q=12**, there is exactly one real zero of F_12 in the closed interval [0.0528706,0.0528708], with its zero in the open interval. Across that interval F_12 is strictly decreasing, while A(z)>0 and B(z)>0.

**(II) For q=24**, there is exactly one real zero of F_24 in the closed interval [0.0530655,0.0530659], with its zero in the open interval. Across that interval F_24 is strictly decreasing, while A(z)>0 and B(z)>0.

The widths are respectively 2/10^7 and 4/10^7. These shrink the existence windows [0.052,0.053] (q=12) and [0.053,0.054] (q=24) from PREFIX-676, by factors 5000 and 2500. The local zeros are separated and ordered. Local uniqueness is certified in these windows; additional roots elsewhere in the larger intervals remain an open question.

## Exact computation and analytic certificate

The verifier `PREFIX688_R6_CROSSING_BRACKETS.py` independently reconstructs each of the 189 survivor rows using the original integer threshold predicate and checks 9,529 nonzero survivor coefficients. At each rational z endpoint it evaluates S_n(z) as a rational Bernstein sum, then forms exactly the independent-Poissonized moments:

- mu_d = 2 sum(S) - K(S,S), mu_e = sum(S0)+sum(S)-K(S0,S).
- H_d = 2 sum((n+1)S_n)-J(S,S), H_e=sum((n+1)(S0_n+S_n))-J(S0,S).
- B = mu_d-mu_e and A=2(H_d-H_e)-mu_d^2+mu_e^2.
- K[n,m]=binom(n+m,n)/2^(n+m+1); J[n,m]=(n+m+1)K[n,m]/2.

The exact signs, with conservative signed floors of 10^9 F_q(z), are:

| q | left endpoint: floor(10^9 F) | right endpoint: floor(10^9 F) |
|---|---:|---:|
| 12 | 2028625 | -2009751 |
| 24 | 8857119 | -7369717 |

Thus continuity gives at least one zero in each open window. For uniqueness, calculate the exact jets A,A',A'' and B,B',B'' at the midpoint c, using differentiated survivor polynomials. Preserve all exact Fraction values in the checker; the following floors of 10^6 times these values are included solely as compact witnesses:

| q | c | floor(10^6 A') | floor(10^6 A'') | floor(10^6 B') | floor(10^6 B'') |
|---|---|---:|---:|---:|---:|
| 12 | 0.0528707 | -1671941380 | -66726857069 | 128587655 | -989565080 |
| 24 | 0.0530657 | -1684945674 | -66650317279 | 128394438 | -992151722 |

Reuse the previously source-derived uniform **third-derivative** certificate from PREFIX-680, valid on [0,1/2]:

M_A3 = 218571424275456, M_B3 = 69527880576.

For every z in [c-r,c+r], the rigorous Taylor inequality is

F'_q(z) <= F'_q(c) + |F''_q(c)|r + (q*M_A3 + M_B3)r^2/2 =: U_q.

The checker evaluates U_q with exact Fraction arithmetic; floor(U_12) = -20179 and floor(U_24) = -40462. Consequently F'_12(z) < -20178 and F'_24(z) < -40461 throughout their respective windows, proving strict local uniqueness.

Likewise, both A and B stay positive on each window: at center subtract |G'(c)|r+|G''(c)|r^2/2+M_G3*r^3/6 from G(c) for G=A,B; the exact lower bounds are strictly positive, as asserted by the checker.

## Scientific meaning and next unit

These are exact, narrow, distinct local crossover certificates for practical small sampling slots, complementing PREFIX-687's large-q=9873+ branch. The proof uses BRC's provenance-preserving finite survivor count carrier: the frozen rows, two clock identities and their joint moment kernels are retained until the declared variance/mean observer is formed. No arbitrary native-coordinate interpretation is introduced.

Evidence: two endpoint checks and two center-jet/Taylor checks executed locally with Python arbitrary-precision integers and Fraction; all four returned PASS. The original 189-level recurrence was rerun for each independent check. The script's `ends` and `center` modes permit separate bounded verification; `all` combines them. Previously published PREFIX-680 third-derivative proof is a named mathematical dependency, not recreated in this note.

Status: AUTHOR_DERIVED / EXACT_RATIONAL_RECOMPUTED / UNREVIEWED / NOT_ADMITTED.

Next: construct signed Bernstein certificates for F'_12 and F'_24 across the portions of [0.052,0.054] outside these local windows; determine the full root counts and connect them to the PREFIX-675 two-parameter global variance-maximum search.