# R5 — Second distinct strict reduction of the degree-≥1 quasipolynomial period (m=78)

Date: 2026-11-23. Status: **AUTHOR_EXACT_PROOF / MODULAR_CRT_CERTIFIED / NOT_REVIEWED**.
Scope: frozen five-event scalar observer, **not** a native X6/BRC theorem or a formal Result/CLAIM.
Scientific pin: `awdawmip/enterprise-math@75d986aa23b68a7ecf9b29dc1006f0e322b35a15`.
Predecessors: `@882ac53313bd4536df22f2bd963002bc1304aa29` (m=1..73, first drop at 69), `@9194681d8b318cca415df3b178b30b876ea89fcd` (finite Hasse jets).

## Exact frozen problem
Let `D(q)=∏_{p=214}^{314}(1-q^p)`, and let `R_m(q)` be the integral numerator of the generating function counting nonnegative price vectors of total value N satisfying at least one of the failure inequalities `∑_{p∈S_i}a_p<m`. Sets are:
`S0=214..218`, `S1={214,216,217,218,219,220,221}`,
`S2={215,216,217,218,219,220,221}`,
`S3=223..290`, `S4=296..312`.
The three overlapping failures `S0,S1,S2` use exact multivariate intersection counting; `S3,S4` use complete-homogeneous total-count generating functions.
Let `M_m^{(>=1)}` denote the smallest simultaneous quasipolynomial period of all coefficients in powers `N^j`, `j>=1`.
Let `Lambda=814202665467037976682352800`.

## Theorem A — exact second distinct strict drop
For all integer thresholds `74<=m<=77`, `M_m^{(>=1)}=Lambda`. At `m=78`,
```
M_78^{(>=1)} = Lambda/41 = 19858601596757023821520800.
```
Thus after the first drop `m=69..73` by 73, the period returns to Lambda at m=74 and the next strictly shorter period begins at m=78, this time by 41.

**Lower bound.** The previously archived first-jet verifier `VERIFY_FIRST_DROP.cpp` at exact commit `882ac53313bd4536df22f2bd963002bc1304aa29` was rerun on thresholds 74..78. It computes Hasse coefficients `[t^j]R_m(z(1+t))` over finite fields, using a prime p and an element z of exact order d. A nonzero coefficient with `0<=j<=n_d-2`, where `n_d=#{p∈[214,314]:d|p}`, proves a characteristic-zero pole of order at least 2 and hence `d|M_m^{(>=1)}`. Each of the 18 lcm-covering orders `{32,54,25,49,11,13,17,19,23,29,62,37,41,43,47,59,61,73}` has a valid nonzero witness at m=74..77. At m=78 all except d=41 have a nonzero witness. The lcm of the 17 surviving orders is precisely Lambda/41. The full finite-field outputs (including auxiliary order 27) are in `R5_M74_M78_HASSE.csv`.

**Exact characteristic-zero vanishing of the missing d=41 component.** At any primitive 41st root ζ, `B_m(ζ)=0` identically because S3 contains the two multiples 246 and 287 of 41. For m=78, the block S4 has 17 distinct nonzero residues 9..25 modulo 41 and the complement-residue lemma proves `C_78(ζ)=0`. Consequently `R_78(ζ)=A_78(ζ)`, where `A_m` is the seven-term inclusion–exclusion numerator of the first three overlapping events. We show `Φ_41(q)|A_78(q)` over **integers**, not merely modulo one prime:

For each prime p in `[83,739,821,1231,1559,2297,2707]`, evaluate the original overlap DP at all 40 primitive 41st roots in F_p. The primitive base roots are respectively `[4,478,159,1000,1490,1862,632]`. Exact runs returned zero at **all 280 primitive roots**; see `R5_M78_D41_CRT.csv` and `VERIFY_M78_D41_CRT.cpp`.

Write `A_78(q) mod (q^41-1)=∑_{r=0}^{40} b_r q^r` with integer b_r. For an inclusion-exclusion mask of selected overlapping events, let u be the union-support size; u<=8. Each selected coordinate is <m, hence at most `m^u` configurations, and multiplying by the union-block `∏(1-q^price)` creates at most `2^u` monomials per configuration. Therefore every `|b_r|<=B=7*2^8*78^8=2455244952264179712`. At each prime, the 40 zero evaluations imply `b_0≡...≡b_40 (mod p)` because those are all roots of `Φ_41` and the residue polynomial has degree <=40. Their product `P=600923387789680224007>2B=4910489904528359424`. Hence `b_r=b_0` as **integers** for all r, so the residue polynomial is an integer multiple of Φ41 and `A_78(ζ)=0` in characteristic zero.

The denominator has exactly two 41-divisible prices (246,287) and no other primitive order divisible by 41 with `n_d>=2` (in the complete interval 214..314). Thus the canceled 41-order double pole cannot contribute to degree>=1 terms, and no other double pole introduces a factor 41. All other double-pole orders divide Lambda/41. Consequently `M_78^{(>=1)}|Lambda/41`, matching the lower bound.

## Theorem B — global exact zero/nonzero classes for primitive 54 and 73
For every m>=1 and every primitive root of the specified order,
```
R_m(ζ_54)=0  iff  m mod 54 ∈ {0,38,39,...,53};
R_m(ζ_73)=0  iff  m mod 73 ∈ {0,69,70,71,72}.
```
At d=54 every overlap numerator contains `1-q^216`, while S3 contains 270; hence `R_m(ζ_54)=C_m(ζ_54)`. The S4 residues are the 17 nonzero distinct residues 26..42 modulo 54. The standard complement identity `∑_{j>=0}h_j t^j=U(t)/(1-t^d)` has `U(1)=0` and `deg U=d-17=37`. Thus the prefix sum is periodic in m mod 54 and vanishes for residues 38..54. At d=73 the overlap inclusion-exclusion terms touching S1 or S2 vanish by `1-q^219`, leaving `A_m=C_{S0,m}`. The S0/S3/S4 sets have respectively 5/68/17 distinct nonzero residues mod 73, with prefix-sum zero ranges 69..73 / 6..73 / 57..73. Each prefix sum is period-73, so the entire R_m is period-73 at primitive ζ73 and is zero on their intersection 69..73.

To establish the **only if** directions, independently evaluate the actual singleton numerators in F_109 (primitive order54 root36) and F_293 (primitive order73 root16). All 37 other residues of d54 and all 68 other residues of d73 are nonzero; these values match the archived full five-event Hasse rows for m<=73, and four consecutive modular periods were checked (`VERIFY_GLOBAL_54_73.py`). A nonzero reduction at one exact-order root disproves cyclotomic divisibility over integers. Hence the classes are exact in characteristic zero.

Since d=73 is the only possible double-pole primitive order divisible by 73 in D, this also yields the **global classification of the factor 73**:
```
v_73(M_m^{(>=1)}) = 0  iff m mod73 ∈ {0,69,70,71,72};
v_73(M_m^{(>=1)}) = 1  otherwise.
```
By contrast, losing the *primitive order 54* alone does not determine whether 54 divides the overall lcm: the primitive order 27 may preserve its factor 3^3, as in archived thresholds 38..54.

## Reproduction and review boundary
Files: `VERIFY_M78_D41_CRT.cpp`, `R5_M78_D41_CRT.csv`, `R5_M74_M78_HASSE.csv`, `VERIFY_GLOBAL_54_73.py`, `VALIDATE_M78_EXACT.py`.
The first-73 predecessor code is reused at its exact immutable source. Compile the C++ with `g++ -O3 -std=c++17`, execute the 74..78 Hasse routine and the 280-root CRT routine; run Python checks on their CSV output. The CRT magnitudes, primes and 41-order checks are part of the proof, not a heuristic pattern search.
Review status: **NOT_REVIEWED**. The result concerns exactly the frozen scalar observer and its coefficient-period readout, with no unproved promotion to P000/native X6, BRC, Result/Review, or formal claim.
Next question: determine whether the experimentally observed zero 41-order residues at thresholds 79..82 also hold in characteristic zero, and seek a general polynomial-in-quotient proof for the 41-order numerator along m mod41; characterize the third distinct global drop and interaction with 73.
