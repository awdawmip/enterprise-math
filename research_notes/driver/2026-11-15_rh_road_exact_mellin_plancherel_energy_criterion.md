# RH full-integer road: exact finite Mellin–Plancherel identity and Hardy-energy criterion

Date: 2026-11-15.
Status: proved, scoped mathematical derivation; no Native Result admission or parent-task closure.
Derivation contributor: RESEARCH_DRIVER EM-DVR-DEBB5E. Original full-road program/contributor: EM-FREE-C4A91D. Formal research task: RH-ROAD-TAIL-20260909 (publication TP2-DCE65A0EFCE8151C39BD). This note is a Driver-authored auxiliary result and does not claim independent review of the author's own RH notes.

## Definitions (unchanged full-integer road)

For real a>0 and n>=1 let

    R_a(n)=product_{p|n}(1-p^{-a}), R_a(1)=1,
    S_a(N)=sum_{n<=N} R_a(n), c_a=1/zeta(1+a),
    B_{a,N}=S_a(N)-1-(N+1/2)c_a,
    E_a=sum_{N>=1} |B_{a,N}|^2/N^2.

Set u_a(n)=R_a(n)-c_a, K_a=1+c_a/2, and for real x>=1 put

    H_a(x)=sum_{n<=x}u_a(n) = B_{a,floor x}+K_a.

Thus H_a is a full-road cumulative step function, constant on [N,N+1). The exact arithmetic Dirichlet series for Re(s)>1 is

    D_a(s)=sum_{n>=1}u_a(n)n^{-s}
          =zeta(s)/zeta(s+a)-c_a*zeta(s).

The zeta expression is the classical meromorphic continuation. No primes or composite integers are discarded.

## Theorem 1: an exact finite spectral identity

For every integer M>=1 and complex s, define the entire finite exponential polynomial

    D_{a,M}(s)
       =sum_{n=1}^M u_a(n)n^{-s}-H_a(M)(M+1)^{-s}
       =sum_{n=1}^M H_a(n)[n^{-s}-(n+1)^{-s}].

Then, for every real sigma (including sigma=1/2),

    (1/(2*pi)) int_{t=-infty}^{infty}
       |D_{a,M}(sigma+it)/(sigma+it)|^2 dt
     =sum_{n=1}^M |H_a(n)|^2
          int_{n}^{n+1} x^{-2*sigma-1} dx,         (1)

provided sigma+it is interpreted with the removable value of D_{a,M}(s)/s at s=0 (the entire expression is the finite Mellin integral).

In particular, at sigma=1/2,

    (1/(2*pi)) int_R
       |D_{a,M}(1/2+it)/(1/2+it)|^2 dt
      =sum_{n=1}^M |B_{a,n}+K_a|^2/[n(n+1)].       (2)

**Proof.** Finite summation by parts yields the displayed form of D_{a,M}. Because H_a(x)=H_a(n) for n<=x<n+1,

    D_{a,M}(s)/s=int_1^{M+1} H_a(x)x^{-s-1}dx.

With x=e^v this is the Fourier transform in t of the compactly supported
function H_a(e^v)e^{-sigma*v} 1_{0<=v<=log(M+1)}.
The usual Fourier Plancherel theorem, followed by dx/x=dv, gives
(1) exactly. Taking sigma=1/2 gives (2), since
int_n^{n+1}x^{-2}dx=1/[n(n+1)]. QED.

All identities are finite, with no RH assumption, truncation-error constant, or spectral quadrature approximation. The complex phase is retained inside the Fourier integrand. The integrated modulus is used only for the exact L² energy readout; it is not asserted to be a lossless observer for other operations.

## Theorem 2: exact Hardy-space criterion for infinite road energy

Fix a>0 and let C_{1/2}={s:Re(s)>1/2}. The following are equivalent:

(i) E_a<infinity.

(ii) D_a(s) has a holomorphic continuation D_a^{ext}(s) to C_{1/2} such that F_a(s)=D_a^{ext}(s)/s satisfies

    sup_{sigma>1/2} (1/(2*pi)) int_R
               |F_a(sigma+it)|^2 dt < infinity.     (3)

Moreover, whenever they hold,

    sup_{sigma>1/2} (1/(2*pi)) int_R
               |F_a(sigma+it)|^2 dt
      =sum_{n>=1}|B_{a,n}+K_a|^2/[n(n+1)].         (4)

**Proof.** Since 0<=R_a(n)<=1 and 0<c_a<1, the function
H_a(x)=O_a(x). For Re(s)>1, ordinary Abel summation gives

    D_a(s)/s=int_1^infinity H_a(x)x^{-s-1}dx.       (5)

The same Fourier/Plancherel calculation as above, now applied on
[0,infinity), is justified for sigma>1 and yields

    (1/(2*pi)) int_R |D_a(sigma+it)/(sigma+it)|^2 dt
      =int_1^infinity |H_a(x)|^2 x^{-2*sigma-1}dx. (6)

For sigma>1/2, the right side is finite whenever
P_a:=int_1^infinity|H_a(x)|^2x^{-2}dx is finite.
Cauchy–Schwarz on (5), written in v=log x, then extends F_a(s)
holomorphically to sigma>1/2. Plancherel continues to hold for
every such sigma, and monotone convergence as sigma decreases to
1/2 shows that the supremum in (3) equals P_a.

Conversely, suppose (ii). On sigma>1, identity of holomorphic
functions identifies D_a^{ext} with the original D_a, so (6) applies.
The uniform bound (3) and monotone convergence as sigma decreases
to 1/2 force P_a<infinity.

Finally H_a(x)=B_{a,n}+K_a on [n,n+1), hence

    P_a=sum_{n>=1}|B_{a,n}+K_a|^2/[n(n+1)].

Because 1/(2n^2)<=1/[n(n+1)]<=1/n^2 and
sum n^{-2}<infinity, the addition of a fixed K_a leaves
weighted square summability unchanged:
P_a<infinity iff E_a<infinity.
This completes both directions and (4). QED.

## Quantitative finite comparison

Writing E_a(M)=sum_{n=1}^M|B_{a,n}|^2/n^2 and
P_a(M)=sum_{n=1}^M|B_{a,n}+K_a|^2/[n(n+1)], the elementary
inequality |v+w|^2<=2|v|^2+2|w|^2 gives

    E_a(M) <= 4 P_a(M)+2 K_a^2 sum_{n=1}^M 1/n^2,
    P_a(M) <= 2 E_a(M)+2 K_a^2 sum_{n=1}^M 1/[n(n+1)].

The equivalence therefore has explicit uniform-in-M comparison
constants, rather than merely an asymptotic relation.

## Connection to the previously proved zeta-zero obstruction

The source proof
`2026-11-15_rh_road_l2_energy_shifted_zeta_zero_obstruction.md`
(commit 2c0d82cf8cf4ee6826a0c0c6addc8a043e79f54a)
showed that a zero rho of zeta with Re(rho)>1/2 makes
E_a infinite for all sufficiently small a>0. By Theorem 2, the
same obstruction says that the exact full-road boundary Mellin
transform cannot belong to this Hardy L² class at those a.
The finite identity (2) supplies a concrete spectral route for
testing candidate tail bounds without changing the original
arithmetic population or silently removing composite interactions.

Open scientific obligation: establish a bound for the genuinely
escaping infinite road tail uniformly for a->0+, or find another
exact structural mechanism. Hardy-space reformulation by itself
is not an energy estimate or a proof of RH.
