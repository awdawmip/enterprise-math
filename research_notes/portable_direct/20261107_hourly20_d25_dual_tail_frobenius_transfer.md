# D25: 216/2304 dual-tail traces and truncated Frobenius boundary operators (2026-11-07)

**Status:** AUTHOR-SIDE ALGEBRAIC PROOFS / EXACT FINITE TESTS / UNREVIEWED / NOT_ADMITTED. This is portable research, not a native task checkpoint or approved result. Configured TASK_RESEARCH logical lane: chatgpt-research-hourly-enterprise-math-20260923 (NOT control-maintenance lane chatgpt-hourly-enterprise-math-20260921). Native session/claim/run authority currently UNVERIFIED.

Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; immutable scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3. Builds on 20261107_hourly20_d25_216_2304_strata_transfer.md without altering existing science pins.

## Source inputs and proved external premise

For prime p>3 and 0<=k<p, put

A_k=(2k)!(3k)!/[216^k(k!)^5],
B_k=(4k)!/[2304^k(k!)^4],
W_p=sum_(k=0)^(p-1)(6k+1)A_k,
S_p=sum_(k=0)^(p-1)(8k+1)B_k.

Guo–Zudilin, "A q-microscope for supercongruences", Advances in Mathematics 346 (2019), 329-358, DOI 10.1016/j.aim.2019.02.008, arXiv:1803.01830 proves both the FULL p-1 and HALF (p-1)/2 truncations of S_p are congruent to p*(-3/p) mod p^3 for all primes p>3. This is previously proved external input, NOT an original theorem here. The earlier frozen Clausen/reflection source bridge Delta_p-R_p=(W_p-p)/p^2 mod p is retained as a dependency, not re-proved. Target classes p=13,19 mod24 have (-3/p)=1.

## Proposition 1: universal half-window source reduction

Set h=(p-1)/2, a=floor((2p-1)/3), b=floor((3p-1)/4). In F_p define

C_p = sum_(k=h+1)^a (6k+1)*(2k-p)!*(3k-p)!/[216^k*(k!)^5],
H_p = sum_(k=h+1)^b 2*(8k+1)*(4k-2p)!/[2304^k*(k!)^4].

Let W_p^lo and S_p^lo denote the corresponding original sums over 0<=k<=h. Then FOR EVERY prime p>3,

W_p = W_p^lo + p^2*C_p (mod p^3),
S_p = S_p^lo + p^2*H_p (mod p^3),
H_p = 0 (mod p).

**Algebraic proof.** Since k<p, Legendre gives v_p(A_k)=floor(2k/p)+floor(3k/p) and v_p(B_k)=floor(4k/p). On h<k<=a, v_p(A_k)=2; on k>a it is >=3. The factorial p-unit identity (p+r)!/p=-r! (mod p), for 0<=r<p, yields the labelled C_p formula by multiplying two factors. For h<k<=b, v_p(B_k)=2; beyond b it is >=3. The identity (2p+r)!/p^2=2r! (mod p) gives labelled H_p. This proves both tail reductions. Subtract the proved Guo–Zudilin S full/half congruences and divide by p^2 to get H_p=0 in F_p.

Consequently the OPEN 216-to-2304 supercongruence is equivalent to
W_p^lo - S_p^lo + p^2*C_p = 0 (mod p^3).
For p=6m+1, h=3m and a=4m: C_p has exactly m indexed source positions k=3m+1,...,4m. H_p vanishing as a scalar DOES NOT make its individual ports zero or redundant for other BRC observers.

## Proposition 2: original 216 shifted 4F3 derivative trace

Suppose p=6m+1>=7. Let theta=z*d/dz and
t_j=(1)_j(5/6)_j(7/6)_j/(3/2)_j^3,
T_m(z)=sum_(j=0)^(m-1)t_j*z^j,
K_p=4*(3m+2)!/[216^(3m+1)*((3m+1)!)^5] (mod p).

The denominators are p-units. Then
C_p=K_p*[1+(3/2)*theta]T_m(1/2) (mod p).

**Proof.** Shift the port index k=3m+1+j. The ratio of consecutive unweighted factorial ports is ((j+1)(6j+5)(6j+7))/(9(2j+3)^3) mod p, which equals t_(j+1)*(1/2)^(j+1)/[t_j*(1/2)^j]. The weight (6k+1)/[6(3m+1)+1] is 1+3j/2 mod p. The first port equals K_p; iterate for 0<=j<m. This proves the trace without extending beyond the valuation band.

## Proposition 3: exact 216 polynomial hypergeometric cutoff defect

Define the rational differential operator

L_A=theta*(theta+1/2)^3 - z*(theta+1)^2*(theta+5/6)*(theta+7/6).

The exact identity over Q[z] is

L_A T_m=-m^2*(m-1/6)*(m+1/6)*t_(m-1)*z^m
       =-p*m^2*(m-1/6)*t_(m-1)*z^m/6.

**Proof.** The coefficient recurrence is
t_j/t_(j-1)=j*(j-1/6)*(j+1/6)/(j+1/2)^3.
It cancels coefficients z^0,...,z^(m-1) exactly. There is just the single displayed cutoff coefficient z^m. Since m and m-1/6 and t_(m-1) are p-units, the displayed coefficient has exact p-adic valuation one; therefore

L_A T_m=0 mod p,
v_p([z^m]L_A T_m)=1,
[z^m]L_A T_m/p=t_(m-1)/648 !=0 mod p.

This supplies a *genuine polynomial mod-p solution with a nonzero first lifting defect*, not a completed proof of the mother LIFT target.

## Proposition 4: shifted 2304 derivative root and independent defect

For p>=7 let n=floor((p+1)/4), k0=(p+1)/2, and

u_j=(1)_j(3/4)_j(5/4)_j/(3/2)_j^3,
Z_n(z)=sum_(j=0)^(n-1)u_j*z^j,
D_p=20/[2304^k0*(k0!)^4] !=0 mod p.

By the same factorial-ratio shift applied to H_p,

H_p=D_p*[1+(8/5)*theta]Z_n(1/9) (mod p),

so the already-proved external full-minus-half 2304 theorem entails the **new explicit finite-field derivative root**
[1+(8/5)*theta]Z_n(1/9)=0 (mod p).

Define L_B=theta*(theta+1/2)^3-z*(theta+1)^2*(theta+3/4)*(theta+5/4). Then over Q[z] we have the exact identity

L_B Z_n=-n^2*(n-1/4)*(n+1/4)*u_(n-1)*z^n.

Indeed u_j/u_(j-1)=j*(j-1/4)*(j+1/4)/(j+1/2)^3. Its first n coefficients cancel. If p=1 mod4, n=(p-1)/4 makes n+1/4=p/4; if p=3 mod4, n=(p+1)/4 makes n-1/4=p/4. In either case u_(n-1) is a p-unit and

L_B Z_n=0 mod p,
v_p([z^n]L_B Z_n)=1,
[z^n]L_B Z_n/p = (-1/p)*u_(n-1)/128 !=0 mod p,

where (-1/p) is the Legendre symbol.

**Research meaning:** L_A and L_B yield two distinct truncated finite 4F3 polynomial solutions, two distinct readouts (z=1/2 vs z=1/9), and two exact nonzero p-adic boundary defects. A p-adic intertwiner/WZ certificate connecting them and the low-window difference would advance the mother target. None has been proved in this note.

## Executed arithmetic and scope

Companion exact Python checker: research_notes/portable_direct/d25_half_window_transfer_20261107.py.

- 11/11 selected primes: independent full modular term recurrence and Wilson-labelled tail ports agree mod p^3.
- 301/301 primes 5<=p<2000: H_p=0 exactly as implied by the external theorem.
- 611/611 primes 7<=p<10000 with p=1 mod6: C_p equals its shifted 4F3 trace and the exact L_A polynomial defect is checked mod p^2. All examined C_p !=0; this is a finite observation only.
- 1226/1226 primes 7<=p<10000: 2304 shifted readout root and exact L_B polynomial boundary checks pass.

Selected (p,C_p,H_p,lower-window-difference/p^2 modp):
7:(5,0,2), 13:(10,0,3), 19:(9,0,10), 181:(152,0,29), 373:(266,0,107).
The displayed quotients are verified for those inputs, not asserted universally.

Retain source labels (216 vs 2304), index k, valuation band, p^2 Wilson unit, weight and sign; H_p=0 concerns the declared scalar observer at this precision, not generic X6/native/phase/trajectory observer equivalence.

## Current control and exact continuation

Gateway status read 2026-11-07 returned BACKEND_IDENTITY_OR_VERSION_MISMATCH with operation_sent=false, Site CONFIGURED_NOT_LIVE_VERIFIED and research_authority_granted=false. Original pending requests: em-h20-20261106-1324-d25-task-r13 and em-h20-20261106-1324-d25-cont-r13. Preserve pending and protected session/claim/run/uploads as UNKNOWN; no restart/reclaim and no native Source checkpoint. Control support is awdawmip/enterprise-math#1558.

Next action is an explicit contiguous/WZ or differential intertwining between (L_A,T_m,1/2) and (L_B,Z_n,1/9), keeping both p-times-leading-coefficient cutoff terms and the 216/2304 valuation labels. Test candidates on p=7,13,19,181,373. The mother goal Delta_p-R_p=0 modp for p=13,19 mod24, equivalently original216 W_p=p modp^3, remains OPEN; source/admission/review/independent reproduction remain pending. REGISTER_PENDING/SYNC_DEBT refers to native activity/authority only.