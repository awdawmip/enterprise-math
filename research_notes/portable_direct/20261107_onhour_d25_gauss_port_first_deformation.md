# D25: Exact first p-adic Gauss-port deformation and second-digit obstruction

Date: 2026-11-07 (Asia/Hong_Kong). TASK_RESEARCH lane: chatgpt-research-onhour-enterprise-math-20260923. Parent publication TP2-B6F4FC938FF94941C1B7; scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3. AUTHOR_SIDE_PROVED / FINITE_VERIFIED / UNREVIEWED / NOT_ADMITTED.

## Proposition (every prime p=6m+1>3)

Let F_p(z)=sum_{k=0}^{p-1}u_k z^k, u_k=(1/6)_k(1/3)_k/(k!)^2, and define integer Pfaff ports S_m=sum_{k=0}^m binom(m,k)binom(2m+k,k), T_m=sum_{k=0}^m k binom(m,k)binom(2m+k,k), B_m=(1-12m)S_m+24T_m. All congruences use Z_(p). Put H_{n,k}=sum_{r=n-k+1}^n 1/r, H_{n,0}=0. In F_p define two *distinct provenance-bearing contributions*

C_low= -sum_{k=0}^m binom(m,k)binom(2m,k) 2^(-k) [H_{m,k}/6+H_{2m,k}/3],

C_mid= sum_{k=m+1}^{2m} (-1)^(m+k) m!(k-m-1)!(2m)!/[6(2m-k)!(k!)^2 2^k],   C=C_low+C_mid.

Then exactly:

(1) F_p(1/2) == 2^(-m) S_m + p C (mod p^2).

(2) E_p:=F_p(1/2)+6F'_p(1/2) == 2^(-m)B_m (mod p).

Whenever p divides S_m, the original216 sum W_p=sum_{n=0}^{p-1}(6n+1)(2n)!(3n)!/[216^n(n!)^5] satisfies the **second-digit transport theorem**

(3) W_p/p == 2^(-m) B_m [2^(-m)(S_m/p)+C_low+C_mid] (mod p).

If T_m != 0 (mod p), the Hensel parameter u_D=-(S_m/p)(4T_m)^(-1) gives an observer-equivalent expression

(4) W_p/p == 2^(-m)B_m [C_low+C_mid-4T_m 2^(-m)u_D] (mod p).

The hypotheses p|S and p∤T in (3)-(4) are explicit: all-target residue-class zero-port selection remains an open proof obligation. This unit does not assert the mother supercongruence.

## Complete algebraic proof

For k<=m, use the exact identities 1/6=-m+p/6 and 1/3=-2m+p/3. Expanding the two finite Pochhammer products to first order gives

u_k == binom(m,k)binom(2m,k){1-p[H_{m,k}/6+H_{2m,k}/3]} (mod p^2).

For m<k<=2m, the first Pochhammer contains exactly one p-factor at r=m; the second is still a p-unit. Factorial extraction yields

u_k/p == (-1)^(m+k)m!(k-m-1)!(2m)!/[6(2m-k)!(k!)^2] (mod p).

For 2m<k<p both Pochhammer products have one p-factor, hence u_k==0 mod p^2. All denominators shown are p-units. Sum by these three exact valuation/observer bands at z=1/2 to prove (1).

The previously established exact finite Pfaff identities 2^m D_m(1/2)=S_m and 2^m[D_m(1/2)+6D'_m(1/2)]=B_m, together with F_p == D_m mod p, give (2). The preceding finite Clausen signed boundary theorem states W_p == F_p(1/2)E_p-p^2 K_p mod p^3. In particular W_p == F_p E_p mod p^2. If p|S, then p|F. Substitute (1)-(2), divide by p and reduce mod p, yielding (3); substituting the already proved Hensel formula yields (4). QED.

## Precision and independent exact checks

Run d25_gauss_port_deformation_check_20261107.py with Python 3 standard library. It checks, independently and coefficient-by-coefficient, original Gauss recurrence mod p^2, each low harmonic p-jet term, each middle normalized p-factor, high band zero, integer Pfaff identity, both whole-series observers, and original216 W by a separate recurrence. Exhaustive test inputs are all 148 primes p=1 mod6 in [7,1999], including the 77 frozen target-class primes, plus p=5113. All checks PASS; at the 77 tested target primes p|S and W/p==1 mod p. These are finite observations, not all-prime proof.

Explicit witnesses (p; S modp², T modp, u_D, C_low, C_mid, C, F/p modp, E modp, W/p modp):
13: (26,1,6,3,1,4,11,6,1)
19: (190,4,16,6,15,2,8,12,1)
67: (335,23,40,1,44,45,61,11,1)
373: (109289,119,276,352,78,57,24,171,1).

The middle correction is essential to the actual frozen second digit: discarding C_mid changes W/p at p=19 from 1 to 11 (since 15*12==9 mod19), and at p=373 from 1 to 91 (since 78*171==283 mod373). Thus a purely Hensel-root readout loses indispensable information at the second digit. This is a precise route-specific counterexample, not a global impossibility claim.

BRC residual coordinates: population=(k, band, v_p(u_k), low baseline, signed deformation), bands low [0,m], middle (m,2m], high (2m,p), operation=parameter deformation and weighted observation. Preserve (S/p,C_low,C_mid) until the W/p product observer. No native BRC runtime claim.

## Source, next action, benchmark

Mother target W_p==p (mod p^3), p=13 or19 (mod24); frozen Delta_p-R_p==0 mod p. Consume earlier Pfaff/Hensel, three-shell, Green, Franel/E.2, signed finite Clausen boundary results; do not rederive as separate deliverables.

Next: prove the all-target zero-port selection p|S or pursue an independent route; derive the second-order Gauss p-jet A2 and first-order derivative E1, then combine with the already proved nonzero signed Clausen K_p to form and attempt to cancel the *third-digit* obstruction. Validate initially at p=19 and373, preserving every source/valuation band.

Native p=373 H0/B0 divided-power/Frobenius/independent replication under Issue #1559 remains NOT_EXECUTED / PENDING_OWNER, with its original conditions intact.

This run's authenticated Site read (2026-11-06T19:02Z) found CONFIGURED_NOT_LIVE_VERIFIED and research_authority_granted=false. The native status, original target_request_id onhour11-20261106-1400-exact-research-lane-continuation and checkpoint read returned BACKEND_IDENTITY_OR_VERSION_MISMATCH, operation_sent=false. Session/claim/run NOT_VERIFIED; historical checkpoint revision22 not newly verified; original request not retransmitted. Actual operator recovery is dedicated Site-bound client and approved credential/backend version, then read original receipt and Source continuation. No maintenance lane identity or mutation used. These author-side notes are not a native Source checkpoint or Result.
