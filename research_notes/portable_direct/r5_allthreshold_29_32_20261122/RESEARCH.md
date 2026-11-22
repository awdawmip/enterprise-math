# R5 exact all-threshold primitive-29/32 cancellations and compound contraction

Date: 2026-11-22. Status: **AUTHOR_EXACT_DERIVATION / CHARACTERISTIC_ZERO_INTEGER_CHECKED / NOT_REVIEWED**. This is independent portable research, **not** a formal Task CLAIM, Result, Review, or alteration of P000/ACTIVE worldview. Frozen scientific input: enterprise-math@75d986aa23b68a7ecf9b29dc1006f0e322b35a15. Immediate parent: enterprise-math@96d6218d7fe6ba8c9f4f3b42bce32948a85b2d59, whose m=54..58 and m=60..64 cancellations were previously proved by CRT; the m=101..150 modular scan there was explicitly exploratory.

## Model and precise theorem

For 101 integer prices p=214,...,314, with nonnegative multiplicities a_p and total N=sum p a_p, let E_i(m) be the event that the sum over support S_i is <m:

- S0={214,215,216,217,218}
- S1={214,216,217,218,219,220,221}
- S2={215,216,217,218,219,220,221}
- S3={223,...,290}
- S4={296,...,312}.

Let D(q)=prod_{p=214}^{314}(1-q^p), F_m(q)=R_m(q)/D(q) count the union of the five events, and M_m(O_m(N)) be the *strict least common period of degree >=2 quasipolynomial coefficients* in [q^N]F_m(q).

**Theorem A (complete root-specific classification, every positive m):**

At every complex primitive 29th root ζ29 and primitive 32nd root ζ32,

    R_m(ζ29)=0  iff  m mod 58 in {0,54,55,56,57};
    R_m(ζ32)=0  iff  m mod 64 in {0,60,61,62,63}.

Both sequences R_m(ζ_d) are strictly periodic with period dividing 2d (58 or 64 respectively). The nonzero statement outside each set holds for every positive integer m, not merely the first two cycles.

By the denominator pole inventory, the only primitive order whose pole of order >=3 carries prime factor 29 is order 29 itself; the only such order carrying factor 2^5 is order 32. Both have exactly three divisible prices. Therefore **in this frozen scalar observer**

    29 | M_m(O_m(N)) iff m mod 58 NOT in {0,54,55,56,57};
    32 | M_m(O_m(N)) iff m mod 64 NOT in {0,60,61,62,63}.

These claims are about the exact cyclotomic/pole observer; they do not identify the full minimum period for every m.

**Theorem B (two new fully exact least-period windows):**

Set L=229746052653717600. For every m in 112..116,

    M_m(O_m(N)) = L/29 = 7922277677714400.

For every m in 124..128, primitive orders 32 and 43 cancel simultaneously and

    M_m(O_m(N)) = L/86 = 2671465728531600.

The order-43 cancellation at 124..128 invokes the already published **characteristic-zero** 43-phase theorem, enterprise-math@c9329abecc9963667647a2774b351a33c0456b0a. The lower bounds here are new exact finite-field nonzero witnesses for all remaining required orders, including primitive order 16.

**Corollary C (previously unavailable global simultaneous upper bound):**

Together with that established 43-phase theorem, for all m the numerator removes the unique maximal relevant 29, 32, and/or 43 factors whenever the respective congruences hold. In particular the first simultaneous three-way congruence solution is m=2492 (also 2493,2494), with residues:

    m=2492: (m mod 58,m mod 64,m mod 43)=(56,60,41)
    m=2493: (57,61,42)
    m=2494: (0,62,0).

Thus, without any extrapolation of lower witnesses at these large thresholds,

    M_m(O_m(N)) | L/(29*2*43) = 92119507880400
    for m in {2492,2493,2494}.

This is an **upper bound**, not a claimed strict minimum there. Finite congruence checking on 1<=m<2492 proves that 2492 is the first triple intersection. The common congruence pattern repeats every lcm(58,64,43)=79808.

## Proof of all-m periodicity (not finite-sample extrapolation)

Write U={214,...,221}. Let A_m(q) be the signed exact union numerator for E0,E1,E2 on U, B_m for E3, and C_m for E4, so

    R_m=1-(1-A_m)(1-B_m)(1-C_m).

The disjointness of U,S3,S4 is exact; the three constraints inside U are **joint**, never independent.

Let x=a214,y=a215, u=a216+a217+a218, j=a219+a220+a221. Their constraint counts are

    s0=x+y+u, s1=x+u+j, s2=y+u+j.

The minimum is

    min(s0,s1,s2) = u+x+y+j-max(x,y,j).

The event union indicator is 1_{min(s0,s1,s2)<m}. Multiplying the full 8-price generating function by D_U(q)=prod_{p in U}(1-q^p), and summing over thresholds, gives the exact rational identity

    G_A(t,q):=sum_{m>=1} A_m(q)t^(m-1)
      =D_U(q)/(1-t) * sum_{a in N^8}
         q^(sum_{p in U} p*a_p)
         t^[u+x+y+j-max(x,y,j)].

This holds first as an algebraic identity in the convergence domain and then rationally where specialization is defined.

Now fix q=z, a primitive root of order d=29 or 32. None of the eight q^p is 1. The complete homogeneous sums over the three u-prices and three j-prices have simple root-of-unity partial fractions:

    h_U(u)=sum_{s=216}^{218} alpha_s (z^s)^u,
    h_J(j)=sum_{r=219}^{221} beta_r (z^r)^j,

where alpha_s, beta_r are exact elements of Q(z), with distinct bases and no singular denominators. Let X=z^214, Y=z^215, J=z^r, V=z^s. Define

    T(X,Y,J;t)=sum_{x,y,j>=0} X^xY^yJ^j
                   t^[x+y+j-max(x,y,j)].

Using the exact-max layer difference
prod_{W in {X,Y,J}}sum_{0<=a<=h}(Wt)^a
 minus the analogous product up to h-1, and summing over h, yields

    T(X,Y,J;t)=
      [1/((1-Xt)(1-Yt)(1-Jt))]
      * sum_{empty!=I subset {X,Y,J}}
          (-1)^|I| * (P_I*t^|I|-1)/(1-P_I*t^(|I|-1)),

    P_I=prod_{W in I} W.

Consequently

    G_A(t,z)=D_U(z)/(1-t)
              * sum_{s,r} alpha_s beta_r T(X,Y,z^r;t)/(1-z^s*t).

Every denominator in each summand is selected from: 1-t; 1-z^s t; 1-Xt,1-Yt,1-Jt; at most one pair factor 1-P_I t; or one triple factor 1-XYZ t^2. Each factor divides 1-t^(2d).

It remains to rule out repeated factors, because merely having a common root-of-unity order is not enough. For d=29, the linear exponent residues are {0}, {11,12}, {13,14,15}, {16,17,18}, and (when present) the pair exponents 23,27,28,0,1. The only collision is a pair exponent 0, when P_I=1. Its numerator equals t^2-1, which *cancels* its factor 1-t, leaving a regular polynomial -(t+1). For d=32, the corresponding linear residues are {0},{22,23},{24,25,26},{27,28,29} and pair exponents 13,17,18,19,20; no collision. The quadratic exponents XYZ are, respectively, 10,11,12 mod 29 and 8,9,10 mod 32. For each fixed r and s, 2k is unequal to its quadratic exponent for every linear factor exponent k present in that summand. Direct checking of the finite residue lists proves coprimality. After the d=29 removable cancellation, all t-dependent factors within a summand are pairwise coprime factors of 1-t^(2d).

Each rational summand thus has a denominator dividing 1-t^(2d). Its numerator after multiplication by this common denominator has degree <2d (in fact <=2d-4 before any removable cancellation). Hence

    (1-t^(2d)) G_A(t,z) is a polynomial of degree <2d.

This proves A_(m+2d)(z)=A_m(z) for **every m>=1**, using rational identities, not the repeated first two sample cycles.

For d in {29,32}, S3 includes three prices divisible by d (232,261,290 for 29; 224,256,288 for 32). Therefore B_m(z)=0 for every finite m. S4 contains exactly 17 consecutive nonzero residues mod d; its homogeneous generating function is P_d(v)/(1-v^d), deg P_d=d-17, with P_d(1)=0 because residue zero is among the omitted factors. Thus C_m(z) has period d and is zero on m mod d in {d-16,...,d-1,0}. Therefore

    R_m(z)=A_m(z)+C_m(z)-A_m(z)C_m(z)

is periodic in m with period 2d.

## Exact finite characteristic-zero phase certificate

Only the 58 or 64 base phases remain to be checked. File VERIFY_PHASES.cpp implements integer unbounded-knapsack dynamic programming on every nonempty subset of the three **joint** event constraints; a price belonging to several selected events increments every such counter simultaneously. Inclusion-exclusion applies the exact support factor prod(1-z^p). The S4 one-event numerator is computed separately, and R=A+C-AC.

All operations are in characteristic zero, in the quotient rings:

- d=29: Z[x]/(x^29-1), represented by 29 integer coefficients. The image vanishes at primitive 29th roots **iff all 29 coefficients are equal**, i.e. divisible by Phi_29.
- d=32: Z[x]/(x^16+1)=Z[x]/Phi_32, represented by 16 integer coefficients. Vanishing **iff all 16 are zero**.

The 64-bit DP counts are bounded by M^8 at M=58/64 (at most 2^48); numerator accumulation and multiplication use signed 128-bit integers. Compilation and execution under -fsanitize=undefined -fno-sanitize-recover=all completed without overflow or runtime warnings.

Actual output:

    order=29 zero phases: 54 55 56 57 58
    order=32 zero phases: 60 61 62 63 64

Full two-cycle independent reruns up to m=116/128 verified all 58/64 equality pairs A_m=A_(m+2d), agreeing with the algebraic proof; this is a regression check only, not the justification for all m.

## Strict minimum periods in new windows

The 40 denominator orders with pole multiplicity >=3 have global LCM L. For m112..116, exact root-29 cancellation removes that unique 29 contribution; for m124..128 exact root-32 cancellation and the earlier characteristic-zero root-43 theorem remove both unique factors. Thus the claimed upper bounds follow.

File CHECK_SURVIVORS.cpp evaluates, for each of the ten thresholds, the full signed numerator R and its Euler first jet (q d/dq)R at modular primitive roots of orders

    W={7,9,11,13,17,19,23,25,27,29,31,32,37,43}

over appropriate primes p with d | p-1. A nonzero zero jet leaves a pole of order >=3; when the denominator order is >=4, a nonzero first jet also suffices. Nonzero finite-field evaluations certify characteristic-zero nonvanishing; they are **not** used to certify characteristic-zero zeros.

Actual output summary, every row covering all 14 W orders:

    m=112,113,114,115,116: missing only {29};
    m=124,125,126,127,128: missing only {32,43};
    d=16: nonzero at every one of m124..128, retaining the 2^4 factor.

The m60..64 order-16 regression reproduces the earlier residues 7049,1456,1847,1665,162 modulo 10177. Consequently lcm(W\{29})=L/29, and lcm((W\{32,43}) union {16})=L/86. Lower and upper bounds match in both new windows.

## Validation and scope

- Exact source code: VERIFY_PHASES.cpp, CHECK_SURVIVORS.cpp.
- Recorded outputs: PHASE_OUTPUT.txt, SURVIVOR_SUMMARY.md and SURVIVORS.csv (all 155 original modular evidence rows). Full CSV SHA256: cf8ed8c223898a809205821903195d5f8bb255e186f5a4d69b15d5f5033c55b9.
- Local actual VERIFY_PHASES.cpp SHA256: 670bd356b97dd139e0744ac85f0784b238d2e0eb41629b86c8c5ccd0047c120e; CHECK_SURVIVORS.cpp: 7851e447341f931d544c994fd61ab8fcc41658ded8558d69833db98abab177a1.
- Symbolic proof uses exact rational identities and finite residue disjointness; modular computations provide separate lower-bound nonzero witnesses.
- No formal Lean proof and no independent mathematical peer review occurred.
- Fixed scalar observer only. The signed root-of-unity cancellations must **not** be treated as positive Weighted-BRC branch mass; joint event incidence is retained.
- The complete all-m least-period function is still unknown because other primitive orders may cancel at other thresholds. The triple m2492..2494 statement is a rigorous upper bound, not an exact minimum.

## Next work

Classify remaining relevant primitive orders with an analogous rational threshold identity, and determine whether other cancellations coincide with m2492..2494. Investigate simultaneous minimality using genuine nonzero witnesses and preserve separate all-m upper / finite exact lower levels. Existing Researcher/Activity provenance and formal CLAIM ownership remain independent of this source publication.
