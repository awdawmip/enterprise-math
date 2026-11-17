# R257 — Sharp labelled-output denominator at a 23-adic exceptional parameter

Date: 2026-11-18 (Asia/Shanghai). Status: **AUTHOR_PROVED / EXACT_MODULAR_CERTIFICATE / NOT_REVIEWED**.

Frozen scientific input: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Reuses R254’s exact denominator method (commit `d97f5cb6d3cae6fc35107b605da809a2eb12e5dc`), R255B’s global rational characteristic scaling (commit `6c12b514474d865d3fb8efb940a1b100b14d9208`) and R256’s delayed 13-adic counterexample (commit `c7b15b956ec9fb996c5b72eaae06bed14399e234`).

## Theorem (all future horizons, exactly 63 labelled sources)

Use the same seven-source **positive rational auxiliary scalar observer**, with `s=770/1973`, `t=(1691s-2615)/(2615s-3539)=1285775/1656299`, `a=(1/5,1/4,3/10,9/20,s,2/3,t)`, `b_0=13/60`, `b_i=(5/18)|1/2-a_i|` (i>=1), `pi_i=b_i/(1-a_i)`, `Z=sum_i b_i/(1-a_i)^2`, `rho_i=b_i/(Z(1-a_i)^2)`. For each `m=0,...,62`, put `D_m={0} union {i+1 : bit_i(m)=1}`, `W=(144,576,1440,4320,17280,86400,518400)`, and

```
P_D[i,j] = a_i*delta_ij+(1-a_i)*pi_j,  i,j in D  (no renormalization)
h_(m,k)=W_popcount(m)*sum_(i in D_m) rho_i*(P_D^k*1)_i.
```

For **every integer k>=3**, the exact least common multiple of the *reduced positive denominators* of these 63 labelled outputs is

```
LCM_(0<=m<=62) den(h_(m,k)) = J*T^k/K
J = 327870790093
T = 153448180920
K = 166791501000.
```

The right-hand side is integral for every k>=3, and its denominator encoding grows as `k*log2(T)+O(1) = 37.15896... k+O(1)` bits. In event numbering `n=k+1`, the theorem starts at n=4. Unlike the 13-exception parameter in R256, this **23-adic exceptional parameter has no denominator dip** at any k>=3.

## Proof

**1. Integral recurrence, retaining the source masks.** For each mask of size d, the monic characteristic polynomial is

```
c_m(x) = product_(i in D_m)(x-a_i)
         - sum_(i in D_m) b_i*product_(j in D_m\{i})(x-a_j).
```

By R255B, the coefficient-denominator least common multiple `E=3529308161160=23*T` has the precise 23-adic exception; thus `T` is the least positive integer such that `C_m(y)=T^d*c_m(y/T)` has integer coefficients for every mask. The independent checker recomputes **all 249 nonleading coefficients** and for each prime divisor of T checks that `T/p` fails at least one scaled coefficient.

The initial observation denominators give `J=lcm_(m,i in D_m) den(W_popcount(m)*rho_i)=327870790093`. Let `H_(m,k)=J*T^k*h_(m,k)`. All `H_(m,k)` are integers at each of the 249 values `k=3,...,d_m+2`; their global gcd is `K=166791501000`. Define `q_(m,k)=H_(m,k)/K` for k>=3. Every mask's initial d consecutive `q` values is integral, and `q` obeys the *monic integral recurrence* `C_m` by Cayley–Hamilton. Induction therefore proves `q_(m,k)` integral for every m and k>=3. Thus the denominator of every output divides the integer `D_k=J*T^k/K`.

**2. Exact prime-wise nonvanishing.** The prime support of D_k (over all k>=3) is contained in `{2,3,5,7,11,23,31,101,401,1973,3061,3469}`. For each listed p, the table gives a mask whose `q_(m,k)` is **nonzero modulo p for every k>=3**. `G` means `C_m(y)=y^(d-1)(y-u) (mod p)` with a nonzero unit u and nonzero d consecutive starting residues. After the starting window the sequence is nonzero geometric. `O` means a complete zero-free modular recurrence orbit with no transient.

| prime p | mask m | type | unit u / orbit period | initial residues (k=3,...,d+2) |
|---:|---:|:---:|---:|---|
| 2 | 3 | G | 1 | 1,1,1 |
| 3 | 17 | G | 1 | 2,2,2 |
| 5 | 2 | G | 1 | 1,3 |
| 7 | 2 | G | 3 | 1,3 |
| 11 | 4 | O | 10 | 5,6 |
| **23** | **42** | **G** | **17** | **17,13,14,8** |
| 31 | 32 | G | 15 | 18,22 |
| 101 | 32 | G | 57 | 35,76 |
| 401 | 49 | O | 200 | 192,88,13,246 |
| 1973 | 8 | G | 761 | 511,190 |
| 3061 | 0 | G | 476 | 180 |
| 3469 | 0 | G | 1985 | 726 |

For p=11 and p=401 the script explicitly enumerates the full 10- and 200-state cycles and checks that the initial state returns with no earlier repetition and every first-coordinate residue is nonzero. For p=23 the especially simple congruence is `C_42(y) ≡ y^4-17*y^3 (mod 23)` with the four starting residues shown. Hence every p dividing D_k appears at its full power in at least one reduced output denominator. Their lcm is exactly D_k. QED.

## Reproduction and evidence boundary

`R257_sharp_23adic_denominator_certificate.py` is a standalone Python standard-library checker. It reconstructs all 63 labelled matrices/characteristics and 249 initial observations from rational inputs, certifies the 249 integral recurrence bases and scaling minimality, checks the 12 modular witnesses and independently propagates the original Fraction matrices at k=3,4,5,6,7,8,10,12,16. The local independent checker `R257_sharp_23adic_denominator_certificate.py` (fuller diagnostic variant) also passed; its structured result is preserved in the companion evidence record. The theorem's infinite horizon is established by the integer recurrence plus complete modular-cycle certificates, rather than extrapolating the nine finite direct checks.

This result is for a fixed **positive scalar labelled observer**. It does not claim an equivalence with a native signed/port BRC consumer or alter P000, ACTIVE worldview, frozen input, task owners or review state. Formal CLAIM: none; independent mathematical review: pending.

## Next unanswered question

Determine which other rational 23-adic exceptional parameters exhibit joint p-adic denominator dips, including combined 13/23 exceptional parameters. Seek a parameter-dependent finite-state criterion and an effective period bound that avoids 63-mask enumeration when possible. The continuous real-parameter 270/403 two-mode thresholds remain open independently.
