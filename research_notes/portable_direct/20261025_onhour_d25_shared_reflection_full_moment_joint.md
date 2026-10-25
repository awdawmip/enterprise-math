# D25 — shared reflected p² carrier for Clausen full moment and cutoff corner (2026-10-25)

**Author-side proof/evidence, UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT.** Not a native Source checkpoint, CLAIM, Result, independent review, or native benchmark. This standalone note continues the prior exact Clausen cutoff proof at commit cefbad99f03e3b79e0cfc9de624481ed2010ae40 and Legendre p² moment bridge at ed286d1844dee21e69b5165cc0aba1727d173be2. Scientific frozen Source pin **c47e13e4aba0e006366f989d6334d443f6333ae3** remains unchanged. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7.

## Proven all-prime reflected recurrence and full-band reduction

For prime p=6m+1 >=7 write
$$r_n=(1/6)_n(1/3)_n/[2^n(n!)^2]=\prod_{i=0}^{n-1}(6i+1)(3i+1)/[36^n(n!)^2],\quad 0\le n<p.$$
Set M=sum(r_n), N=sum(n r_n) over 0<=n<p, and let W be the original 3F2 weighted series (6n+1)(1/2)_n(1/3)_n(2/3)_n/[2^n(n!)^3]. Denominators are p-units. Exactly one p factor in the first numerator product occurs at i=m, and one in the second at i=2m. Thus
$$v_p(r_n)=0\ (n\le m),\quad1\ (m<n\le2m),\quad2\ (2m<n<p).$$
**New full-band theorem:** for every 1<=h<=4m, define v_h=(r_(p-h)/p²) mod p (integer p-division BEFORE reduction), V_j=sum_(h<=j)v_h, H_j=sum_(h<=j)h v_h. Then
$$\boxed{v_1=1/10,\qquad v_{h+1}=v_h\,36h^2/[(6h+5)(3h+2)]\pmod p\quad(1\le h<4m).}$$
Initial value: remove the factors p in r_(p-1), leaving two products of all nonzero residues except -5 and -2, respectively. Wilson yields products (1/5) and (1/2); 36^(p-1)((p-1)!)²=1 mod p, hence v_1=1/10. For the recurrence use the **exact** rational reverse ratio r_(n-1)/r_n=36n²/[(6n-5)(3n-2)] at n=p-h. Throughout h<4m the denominators are p-units; 3h+2 first hits 2p at h=4m, so no crossing is claimed. This provides all-prime finite-field transport, not a finite-sample conjecture.

Changing variable h=p-n gives the two exact end-port congruences
$$\boxed{\sum_{n=2m+1}^{p-1}r_n/p²=V_{4m},\qquad\sum_{n=4m+1}^{p-1}r_n/p²=V_{2m}\pmod p.}$$
Let A=sum_(n=0)^(2m)r_n and B=sum_(n=0)^(2m)n r_n. Then unconditionally
$$\boxed{M\equiv A+p²V_{4m}\pmod{p³},\qquad N\equiv B\pmod{p²}.}$$

## One lossless common carrier for bulk and signed cutoff

Clausen coefficient factorization gives the exact equality
$$W=M(M+12N)-Q,\quad Q=\sum_{0\le j,k<p,\ j+k\ge p}(6(j+k)+1)r_jr_k.$$
Valuations force the only Q terms surviving mod p³ to be symmetric corners j in [1,m], k=p-h with 1<=h<=j. All middle-middle terms have j+k< p; middle-high products have valuation>=3. Therefore the **already-established** corner port can now be evaluated with the *same* full-band recurrence:
$$\boxed{Q/p²\equiv T=2\sum_{j=1}^m r_j[(6j+1)V_j-6H_j]\pmod p.}$$
Here r_j is taken mod p. This newly composes the cutoff observer with the entire bulk V_(4m) using a single exact recurrence. The two moments plus corner require V_(4m) and the short H_j prefixes; dropping the latter would lose the signed observer.

Under the still-unproved universal target-class hypothesis M=0 mod p, put U=A/p in the p-local integers, N0=N mod p. Exact substitutions give
$$\boxed{W\equiv12pUN+p²(U²+12N0V_{4m}-T)\pmod{p³}.}$$
Under the **additional** previously accepted first-digit W=p mod p², (12UN-1)/p is p-integral, and the all-target p³ theorem is strictly equivalent to the **open** scalar congruence
$$\boxed{\mathcal E_p=(12UN-1)/p+U²+12N0V_{4m}-T\stackrel{?}=0\pmod p.}$$
This is a faithful *conditional* reduction; neither the all-target Legendre root nor the final equality has been proved here. U,N must retain their p² precision, and p is divided out before taking residues.

## Exact p=13 counterexample to unsafe truncation after factorization

At p=13,m=2, the independently computed residues are V_4=11, V_8=8, N0=7, T=0. Removing Clausen-moment ranks n>4m changes the third p-digit by 12*7*11=1 mod13, **nonzero**. The original W_13=13 mod2197, whereas the faulty truncated-moment expression gives 2041 mod2197. The difference equals 13² mod2197. This refutes transferring original W cutoff n<=4m to the *factorized moment* M; it does not refute D25/JT2.

## Exact execution and limitations

Independent local Python checker d25_clausen_full_three_digit_strata_check_20261025.py evaluates original r_n, original W, three valuation strata, recurrence moments, and the Clausen convolution; it additionally performs explicit Q double sums for small targets. Exact integer modular arithmetic only, explicitly divides p-power factors in integers rather than inverting p. Executed successfully for **138 primes** p=6m+1 (137 p<=1800 plus p=19963), including **74 target primes** p=13,19 mod24; 12 small target double sums independently agreed. The scalar E was 0 in all 74 finite targets, NOT a universal proof.

Example rows (p, U mod p², N0, V_(2m), V_(4m), T, ((12UN-1)/p) mod p, U² mod p, (12N0V_(4m)-T) mod p, E): (13,141,7,11,8,0,0,4,9,0); (19,255,1,10,10,12,18,7,13,0); (211,7156,42,55,130,119,107,113,202,0); (19963,258851988,6798,8815,7392,13363,18008,7904,14014,0).

**BRC/observer composition: COMPOSE_APPLIED.** Rank n, valuation band, signed W and derivative moments, cutoff relation j+k>=p, and provenance remain typed. Compression to V_(4m) is certified for the stated moment observer and moduli, not for every possible future observer; H prefixes preserve the distinct corner operator. This is auxiliary finite-field math and changes no native P000 space or ACTIVE worldview.

**Next exact action:** establish the all-target Legendre zero M mod p with a valid CM/Gauss/Jacobi certificate, then prove/counterexample the coupled E scalar using the previously established p² binomial lift and the shared V_(4m),H prefixes. Retain original Delta_p-R_p bridge, frozen inputs and native benchmark (not executed). The Source continuation read in this turn returned CONTROL_QUOTA; connected Site has no Researcher write grant (v0.6.11). #1539 owns distinct session recovery. No verified active own session/claim/open/run or pending mutation was used. This author note is independent of formal Source-native admission and Driver review. Research logical lane chatgpt-research-onhour-enterprise-math-20260923 was not conflated with maintenance lane.
