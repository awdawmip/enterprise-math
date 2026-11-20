# R5 — Exact fifth-order nondecodable-design density law (2026-11-20)

**Status:** author symbolic proof + finite exact checks; independent mathematical Review = NOT_REVIEWED. Portable independent mathematical continuation, no formal Task CLAIM/RUN.

## Frozen input and prior result

Scientific input: awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551, EXACT_R5_ALL_101_BUDGETS.json, SHA-256 50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b. Prior research: awdawmip/enterprise-math@15fcf2a6a659ba0c06287b3dd27a5b0e67b78475, research_notes/portable_direct/r5_nonadaptive_low_excess_425_20261120/GLOBAL_RATIONAL.md. Reuse the same 256-hypothesis frozen scalar observation; 101 positive integer-priced query labels 214,...,314, unordered multisets, repeatable queries.

There are 32,640 hypothesis pairs, 53 distinct nonempty separating patterns and five inclusion-minimal separating sets:

A = {214,215,216,217,218} (5 types);
B = {214,216,217,218,219,220,221} (7 types);
C = {215,216,217,218,219,220,221} (7 types);
M = {223,...,290} (68 types);
L = {296,...,312} (17 types).

For any fixed nonnegative error and erasure budgets f,e, let m=2f+e+1. An unordered query design is robustly distinguishing iff its total multiplicity in each of the five sets is at least m. Define T(N) as the number of all query multisets of exact price N, F_m(N) as the number that satisfy these five constraints, and Delta_m(N)=T(N)-F_m(N). Limits below take N to infinity **for each fixed m >= 1**.

## Theorem — sharp N^-5 defect with the first correction

Let P=product_{k=214}^{314} k, Pout=product_{k=219}^{314} k, and J_m=binom(m+4,5). Then

Delta_m(N) = J_m N^95/(95! Pout)
           + J_m (12972-180m) N^94/(94! Pout)
           + O_m(N^93).

The unrestricted partition count satisfies

T(N) = N^100/(100! P) + 13332 N^99/(99! P) + O(N^98).

Consequently, with the explicit positive integer

K_m = (100!/95!) * (214*215*216*217*218) * J_m
    = 4247432144558152704000 * binom(m+4,5),

the **fraction of robustly distinguishing fixed-cost designs** obeys

F_m(N)/T(N)
 = 1 - K_m/N^5 + K_m(100860+17100m)/N^6 + O_m(N^-7).

In particular the fifth power is optimal; the failure proportion is Theta_m(N^-5). The early five-label separating set A alone controls both first two terms of the failure count; the other four minimal witnesses start at most at order N^93.

## Full proof

For S in {A,B,C,M,L}, let E_S(N) be the exact-price-N designs containing strictly fewer than m query copies whose labels lie in S. The failure family is their union. In particular,

0 <= Delta_m(N)-|E_A(N)|
   <= |E_B(N)|+|E_C(N)|+|E_M(N)|+|E_L(N)|.

For fixed m and a witness set S with r price types, fewer than m copies in S admits only finitely many S-multiplicity vectors. Once such a vector is fixed, an exact-price choice among the remaining 101-r types has O(N^(100-r)) solutions: freely bound the first 100-r nonnegative multiplicities and the last is determined. Thus the B, C, M and L upper bounds are respectively O_m(N^93), O_m(N^93), O_m(N^32) and O_m(N^83). It follows that

Delta_m(N) = |E_A(N)| + O_m(N^93).

Define the exact finite polynomial

Q_m(q) = sum_{s=0}^{m-1} sum_{alpha_0+...+alpha_4=s, alpha_i>=0}
         q^(214 alpha_0+215 alpha_1+216 alpha_2+217 alpha_3+218 alpha_4).

Then

|E_A(N)| = [q^N] Q_m(q) product_{k=219}^{314} (1-q^k)^(-1).

Stars-and-bars and symmetry across the five types (mean price 216) give

Q_m(1)  = sum_{s=0}^{m-1} binom(s+4,4) = binom(m+4,5) = J_m,

Q'_m(1) = 216 sum_{s=0}^{m-1} s binom(s+4,4)
        = 1080 binom(m+4,6) = 180(m-1) J_m.

Put t=1-q. For the 96 consecutive prices 219,...,314, sum k=25584, and

product_{k=219}^{314} (1-q^k)^(-1)
 = t^(-96)/Pout * [1 + (sum_{k=219}^{314}(k-1)/2)t + O(t^2)].

Multiply this by Q_m(1-t)=J_m-180(m-1)J_m t+O_m(t^2). The standard identities
[q^N](1-q)^(-96)=binom(N+95,95) and
[q^N](1-q)^(-95)=binom(N+94,94)
give

|E_A(N)| = J_m N^95/(95! Pout)
          + J_m (25584/2-180(m-1)) N^94/(94! Pout)
          + O_m(N^93).

The omitted nontrivial root-of-unity poles have order at most 48 because, for any order d>=2, at most 48 of the 96 consecutive prices are divisible by d. Their coefficients contribute much lower powers and do not change the stated expansion. This proves the Delta formula.

The unrestricted 101-factor product has a unique highest-order pole of order 101 at q=1, with sum of prices 26664. The same calculation yields T(N)=N^100/(100!P)+(26664/2)N^99/(99!P)+O(N^98). Nontrivial roots have pole order at most 51. Divide Delta by T to obtain the density formula: the next relative coefficient is -(100860+17100m) times the leading K_m. K_m>0 proves the exponent is exactly 5. QED.

The large-N asymptotic concerns a count of integer-priced multisets, not a continuous physical limit, native six-dimensional motion, or native BRC/heartbeat dynamics.

## Verification and exact scope

The companion Python verifier reconstructs the complete 53 separating masks directly from SHA-matched frozen 256-hypothesis input, checks the five minimal sets, validates Q_m(1) and Q'_m(1) for m=1,2,3,5,17 and, for m=1, independently computes exact counts at costs 735, 840, 1000, 1200 and 1500 with two algorithms: (i) 5-bit state dynamic programming over all 101 prices; (ii) inclusion-exclusion over the five failure events. All tested integer counts agree. See RESULT_R5_DEFECT_EXPONENT.json and VERIFY_R5_DEFECT_EXPONENT.py. The general result follows from the displayed symbolic proof, not from finite extrapolation.

**Next discriminating question:** the first N^93 contribution of B and C and any inclusion-exclusion intersections, then algorithmic extraction of lower-order quasipolynomial terms. The original adaptive eight-error interval 8335 <= C_8^* <= 8343 is unchanged by this fixed-query result.
