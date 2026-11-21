# R5 — Exact least cost quasipolynomial period for every positive threshold

Date: 2026-11-22 (Asia/Shanghai). Scientific status: AUTHOR_PROOF / EXACT_INTEGER_COMPUTATION / NOT_REVIEWED. Model: the **frozen independent R5 scalar cost observer**; neither P000 nor the native BRC/X6 dynamics is modified or reinterpreted.

## Main theorem (new all-threshold closure)

For prices P = {214,...,314} and integer multiplicities a_p >= 0, let f_m(N) count multiplicity vectors of total price N satisfying at least one of the five original failure events

S0={214,215,216,217,218},
S1={214,216,217,218,219,220,221},
S2={215,216,217,218,219,220,221},
S3={223,...,290},
S4={296,...,312},

E_i := {sum_{p in S_i} a_p < m}, where m is an arbitrary **fixed positive integer**. Let M_m(O_m(N^3)) be the least coefficient period of a quasipolynomial approximation of f_m(N) with remainder O_m(N^3).

**Theorem:** For every fixed integer m>=1,

    M_m(O_m(N^3)) = 232792560.

This completes the universal exact-period question for this frozen scalar model and this asymptotic precision. The genuinely coupled event inequalities are retained throughout.

## 1. Universal upper bound (no threshold-specific computation)

The ordinary generating function is exactly F_m(q)=R_m(q)/D(q), where D(q)=product_{p=214}^{314}(1-q^p). For each nonempty event mask I, put U_I=union_{i in I} S_i and let P_{I,m}(q) be the finite sum of q^(sum_{p in U_I} p*a_p) over all nonnegative multiplicities on U_I subject to **every** original event inequality in I. Then

    R_m(q)=sum_{I!=empty} (-1)^(|I|+1)
           P_{I,m}(q) * product_{p in U_I}(1-q^p).

All P_{I,m} are polynomials because every variable in U_I belongs to some selected event and hence is <m. Thus the only possible generating-function poles are roots of D, with order at a primitive d-th root at most

    k(d) = floor(314/d)-floor(213/d).

For a contribution larger than O_m(N^3), the pole order must be >=5. Exactly the orders

    d in {1,2,...,20,22,24}

satisfy k(d)>=5. All d>=26 have k(d)<=4 (five multiples would span 4d>100), and d=21,23,25 also have k(d)<5. Their least common multiple is

    L=lcm(1,...,20,22,24)=232792560.

The standard partial-fraction expansion of a rational function with root-of-unity poles now yields, for every m, M_m(O_m(N^3)) | L. This upper bound is unconditional within the frozen counting model.

As an independent refinement, at every primitive 24th root the numerator has a zero for every m. Each of S0,S1,S2 contains 216; S3 contains 240,264,288; S4 contains 312. Thus every mask term in R_m contains a factor 1-q^p with 24|p, giving R_m(zeta_24)=0 and reducing the primitive-24 pole from 5 to at most 4. This is the **universal** version of the m=1 cancellation, not a finite extrapolation. Removing order 24 does not change L because its prime powers already occur in other candidate orders.

## 2. New primitive-5 all-threshold lower bound

Write z for any primitive 5th root and D_q=q*d/dq. The five original event sets contain respectively 1,1,2,14,3 prices divisible by 5. Among the 31 inclusion-exclusion masks, only the two singleton masks E0 and E1 can contribute the **first** q-jet of R_m at z: every other mask term has at least two vanishing (1-q^p) factors. Therefore R_m(z)=0, and

    B_m := -D_q R_m(z) = 215 C0_m + 220 C1_m,

where C0_m and C1_m are the genuine singleton finite numerator polynomials with the unique zero factor 1-q^215 and 1-q^220, respectively, removed before evaluation.

The five price residues of S0 are exactly 0,1,2,3,4 mod 5. Hence C0_m=5*ceil(m/5). The seven price residues of S1 are 0,1,1,2,3,4,4, so their complete homogeneous multiplicity generating function is

    H1(t) = 1/[(1-t^5)(1-z*t)(1-z^(-1)*t)].

Multiplying by the exact singleton prefactor 5(1-z)(1-z^(-1)), taking the threshold prefix, and cancelling factors of 1-t^5 gives the **exact infinite-m identity**

    sum_{m>=1} B_m t^(m-1)
      = [1075(1+t+t^2+t^3+t^4)
         +1100(1-z)(1-z^(-1))(1-z^2*t)(1-z^3*t)]
        / (1-t^5)^2.

Put s=z^2+z^3. For m=5k+r, 1<=r<=5, k>=0, coefficient extraction yields

    B_m=(k+1)*beta_r,
    beta_1=beta_3=4375+1100s,
    beta_2=-25-2200s,
    beta_4=beta_5=1075.

These are nonzero algebraic integers in the integral basis 1,z,z^2,z^3. Their coordinate vectors are, respectively, (4375,0,1100,1100), (-25,0,-2200,-2200), and (1075,0,0,0). Consequently B_m != 0 for every m>=1. Since k(5)=20, R_m has a simple zero at primitive fifth roots, and F_m has a nonzero nineteenth-order pole. Therefore

    5 | M_m(O_m(N^3)) for every m>=1.

The attached program also checks the displayed identity by a second, cyclic-integer complete-homogeneous computation for m=1,...,15.

## 3. New primitive-7 and primitive-9 all-threshold lower bounds

For d=7 let p0=217, and for d=9 let p0=216. In either case **each** of S0,S1,S2 contains p0 as its unique d-divisible price. S3 has respectively 10 or 8 multiples, and S4 has two. Thus R_m at primitive d-th roots is divisible by (1-q^p0), and all masks involving E3 or E4 have a zero of order >=2. Its exact first-order coefficient is the seven-mask genuinely constrained expression

    B_m^(d)(z)=[R_{A,m}(q)/(1-q^p0)]_{q=z},
    A=E0 union E1 union E2.

Put a=z^214, b=z^215, U(t)=prod_{p=216}^{218}(1-z^p*t)^(-1), J(t)=prod_{p=219}^{221}(1-z^p*t)^(-1), and UB'=prod_{p=216,217,218;p!=p0}(1-z^p), JB=prod_{p=219}^{221}(1-z^p).
Set B0=UB'(1-a)(1-b), B1=UB'(1-a)JB, B2=UB'(1-b)JB and B*=B0*JB. For x,y,j>=0, keep the **three distinct loads** L0=x+y+u, L1=x+j+u, L2=y+j+u. Define

    V0=1/((1-a*t)(1-b*t)),
    V1=J(t)/(1-a*t), V2=J(t)/(1-b*t),
    V01=sum_{x,y,j>=0} a^x*b^y*h_j*t^(x+max(y,j)),
    V02=sum_{x,y,j>=0} a^x*b^y*h_j*t^(y+max(x,j)),
    V12=J(t)*sum_{x,y>=0}a^x*b^y*t^max(x,y),
    V012=sum_{x,y,j>=0}a^x*b^y*h_j*t^(x+y+j-min(x,y,j)),

where h_j=[w^j]J(w). Every expression is an exact rational function of t, derived by decomposing the actual maxima; no event-intersection is replaced by an upper bound on the union of price variables. Then

    G_d(t)=sum_{m>=1}B_m^(d)(z)*t^(m-1)
          = U(t)/(1-t) *
            [B0*V0+B1*V1+B2*V2-B* (V01+V02+V12-V012)].

The three characters z^219,z^220,z^221 are distinct for d=7,9, so h_j has a three-term partial-fraction expansion. Its elementary kernels are

    W(b,c;t)=(1-b*c*t^2)/[(1-b*t)(1-c*t)(1-b*c*t)],
    X(a,b;t)=(1-a*b*t^2)/[(1-a*t)(1-b*t)(1-a*b*t)],
    T(a,b,c;t)=(1-a*b*c*t^3)/
               [(1-a*t)(1-b*t)(1-c*t)(1-a*b*c*t^2)].

For each individual rational summand of G_d, direct integer congruence comparison of linear poles 1-z^e*t and quadratic poles 1-z^e*t^2 shows **maximum multiplicity 3** at any root of t^(2d)=1. The accompanying code enumerates every summand and every 2d-th root, verifying this bound for d=7 and 9 without floating point. Each summand is proper at infinity. Hence

    G_d(t)=H_d(t)/(1-t^(2d))^3,   deg H_d < 6d,

and for all m>=1,

    B_(m+6d) - 3 B_(m+4d) + 3 B_(m+2d) - B_m = 0.

For 1<=r<=2d and k>=0, write A_r=B_r, C_r=B_(r+2d), E_r=B_(r+4d). Thus

    B_(r+2d*k) = A_r+k(C_r-A_r)+k(k-1)/2*(E_r-2*C_r+A_r).

The attached dependency-free exact checker calculates the first 6d vectors in Z[z]/Phi_d, obtains a quadratic polynomial in k for each coordinate, then exhausts all r=1,...,2d:

* d=7, phases r=1,...,9: two coordinate polynomials are coprime over Q for each r. For phases r=10,...,14: C_r=2A_r and E_r=3A_r with nonzero A_r, hence B_(r+14k)=(k+1)A_r !=0.
* d=9, phases r=1,...,13: two coordinate polynomials are coprime over Q for each r. For phases r=14,...,18: C_r=2A_r and E_r=3A_r with nonzero A_r, hence B_(r+18k)=(k+1)A_r !=0.

Coprimality is stronger than necessary: the two coordinate polynomials cannot vanish simultaneously for any complex k, so in particular the entire cyclotomic vector cannot vanish for any nonnegative integer k. Full first-6d vectors are recomputed, and the direct seven-mask bounded-load method independently agrees for m=1,...,5. Additional third-difference checks agree beyond the base window.

Thus for every positive m, the numerator has **exactly one** zero at each primitive d=7,9 root. The denominator has k(7)=14 and k(9)=11, respectively, so the retained Fourier terms have degrees 12 and 9. Consequently

    7 | M_m(O_m(N^3)),     9 | M_m(O_m(N^3))  for every m>=1.

## 4. Closing the exact period

Existing author-derived genuine-intersection all-threshold results at their immutable source versions establish

    11, 13, 16, 17, 19 | M_m(O_m(N^3)).

Precise parent sources:

* d=11,13: enterprise-math@d535077a9f29c268ced6b5667819f7ddc7904809 / research_notes/portable_direct/r5_genuine_11_13_next_universal_20261121/RESEARCH.md
* d=16: enterprise-math@5aefe382332056f38cf942775097bf09afbcbb58 / research_notes/portable_direct/r5_true16_allm_generator_20261121/RESEARCH.md
* d=17: enterprise-math@caeceb3e790ad9d9ef2813bbfa6a6bf66cdbb0fd / research_notes/portable_direct/r5_true17_next_universal_20261121/RESEARCH.md
* d=19: enterprise-math@0f480b89bccf1f637735918eca1c3177a6848de3 / research_notes/portable_direct/r5_true19_allm_20261122/RESEARCH.md

The **newly proved** factors 5,7,9 together with the above previously proved factors give

    lcm(5,7,9,11,13,16,17,19)=232792560 = L.

Combined with the universal upper bound, M_m(O_m(N^3))=L for all positive m.

This is a proof *conditional only on the correctness of the cited prior author-side universal factors*; those proofs and the new certificate remain NOT_REVIEWED by an independent mathematical reviewer. In particular, this is **not** a formal Result, Review or P000 promotion. The previously falsified four-class formula at weaker precision is not reused. The m=1 exact result 232792560 at ba976ca1d5ea32392e409b5dec08c1607140a610 is recovered as a special case.

## Reproduction and unfinished question

Run Python 3 on VERIFY.py in this directory; it uses only the standard library and writes a complete JSON certificate containing the 14+18 phase witnesses, direct finite intersection crosschecks, pole collision bound, exact d=5 vectors and upper-bound audit. For a separate local implementation, the same frozen-model certificate was calculated using an independent 7-mask enumerator; this is not reviewer independence.

Open scientific directions: (i) independently audit the complete assembled all-threshold proof and its inherited factors; (ii) classify the exact least periods at other error orders O_m(N^a), especially where a root's Laurent order changes with m; (iii) explore how the observer's insufficient single-union load quotient generates and preserves structural residuals, without claiming native X6 transfer.

Exact frozen predecessor: enterprise-math@0f480b89bccf1f637735918eca1c3177a6848de3. Original model and true-intersection repair: enterprise-math@75d986aa23b68a7ecf9b29dc1006f0e322b35a15. P000, ACTIVE worldview and scientific input pins are unchanged.
