# D25 — all-prime two-seam Green extension and new residue-class certificates

2026-11-04. AUTHOR-DERIVED / EXACT ALGEBRAIC PROOF IN DECLARED SCOPE / FINITE EXACT CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.

Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. Publication TP2-B6F4FC938FF94941C1B7. Frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3. Research logical lane chatgpt-research-hourly-enterprise-math-20260923; distinct maintenance lane chatgpt-hourly-enterprise-math-20260921. No native CLAIM, run, Source checkpoint or mathematical admission asserted.

## Increment relative to existing sources

The exact last-crossed-wall Green telescope is already authored in 20261104_onhour_d25_two_seam_last_wall_green_certificate.md, and the six-channel valuation grading in 20261104_hourly20_d25_wall_graded_green_boundary_certificate.md, previously specialized to p=6r+1. This note PROVES the extension of both prime-specific consequences and the quadratic-character midpoint digit to every prime p>=5, including previously excluded p=6r+5; it does not re-claim the general rational telescope.

Preserve the original signed coefficients:
a_k=(2k)!(3k)!/((k!)^5 216^k), b_k=(4k)!/((k!)^4 2304^k).
W_p=sum_(k=0)^(p-1) (6k+1)a_k; V_p=sum_(k=0)^(p-1) (8k+1)b_k.
For j<=p-2 let rho_j=(4j+1)(4j+2)(4j+3)/(576(j+1)^3) and gamma_j=(2j+1)(56j(j+1)+13)/(288(j+1)^3), f_j=a_j gamma_j=a_(j+1)-rho_j a_j. All denominators are units in Z_(p).

Let L=floor(p/4)+1, M=(p+1)/2, R=floor(3p/4)+1, N=p-1. For all p>=5 we have 1<L<M<R<=N. Quartic recurrence b_(j+1)=rho_j b_j has exactly three valuation jumps at L,M,R, since v_p(b_n)=floor(4n/p) for n<p. Similarly v_p(a_j)=floor(2j/p)+floor(3j/p), and
e_j=v_p(f_j)=floor(2j/p)+floor(3j/p)+v_p((2j+1)(56j(j+1)+13)).
The last equality uses the unit denominator of gamma_j. On a Green path crossing m quartic walls the source contribution has valuation >=e_j+m, so mod p^3 only the six channels (e,m)=(0,0),(0,1),(0,2),(1,0),(1,1),(2,0) survive.

Define K_j=sum_(n=j+1)^N (6n+1) prod_(i=j+1)^(n-1)rho_i and K_j^[m] its exactly-m-walls subkernel, with C_(e,m)=sum_(j:e_j=e) f_j K_j^[m]. The already established exact finite Green identity and this all-prime valuation proof give
W_p - V_p = sum_(e+m<=2) C_(e,m) - 2 sum_(n=0)^N n b_n (mod p^3).               (1)

Define E0=rho_(L-1)(a_(L-1)-b_(L-1)), E1=rho_(M-1)(a_(M-1)-b_(M-1)), E2=rho_(R-1)(a_(R-1)-b_(R-1)). Define T0,T1,T2 as quartic Green tails from L,M,R respectively to the next cut (or to N). The pre-existing exact last-wall telescope gives the total crossed-wall response E0*T0+E1*T1+E2*T2. For all p>=5 v_p(E0)>=1, v_p(E1)>=2 and v_p(E2)>=3: for p>=7, v_p(a_(R-1))>=3, v_p(b_(R-1))=2 and v_p(rho_(R-1))=1; for p=5, both a_3,b_3 have valuation 2 and rho_3 valuation 1. Therefore the NEW ALL-PRIME extension is
C_(0,1)+C_(1,1)+C_(0,2) = E0*T0+E1*T1 (mod p^3).                      (2)

## Elementary all-prime midpoint character theorem

Let h=(p-1)/2 and chi=(6/p), the quadratic Legendre symbol. For every prime p>=5:
a_h/p = -2 chi,    b_h/p = -1,    rho_h/p = -1/36 (mod p).              (3)

Proof: a_h=binom(2h,h)^2 binom(3h,h)/216^h, b_h=binom(2h,h)^2 binom(4h,2h)/2304^h. Since 2h=p-1, binom(2h,h)^2=1 mod p. The product binom(3h,h)=prod_(j=1)^h (p-1+j)/j yields binom(3h,h)/p=1/h=-2 mod p; similarly binom(4h,2h)=prod_(j=1)^(p-1) (p-1+j)/j yields binom(4h,2h)/p=1/(p-1)=-1. Euler's criterion gives 216^h=6^(3h)=chi and 2304^h=48^(p-1)=1 mod p. Substitution of h into rho yields rho_h/p=-1/36. QED.

As M=h+1, E1/p^2=(rho_h/p)(a_h/p-b_h/p)=(2chi-1)/36 mod p, for EVERY p>=5 (the earlier note proved it only on p=1 mod6). Define G0=C_(0,0)+C_(1,0)+C_(2,0). The source-faithful proven scalar reduction is
W_p - V_p = G0+E0*T0+p^2[(2chi-1)/36]T1 - 2 sum_(n=0)^(p-1) n b_n (mod p^3).   (4)
This is a true algebraic theorem, NOT a proof of the cancellation of its right side.

## Executed finite certificates and candidate

Using the companion Python standard-library program, original coefficients, both signed observers, 3 walls, 6 independently graded Green channels, exact to-two-seam reduction, chi6 midpoint digit and (4) were checked for ALL 667 primes 5<=p<=5000, including 337 primes p=5 mod6 and 330 p=1 mod6. Eight primes 5,7,11,13,19,23,97,373 also used an independent factorial/binomial reconstruction for every original coefficient. All checks PASS.

The further identity
W_p = V_p = ( (-3)/p ) p (mod p^3)                                         (5)
was verified for these 667 primes. The quartic V_p part is an **already published theorem**, as recorded in the literature-aware refinement below; the 216 W_p part and equality of the two remain finite-data candidates in this work. For p=5 mod6 the observed common residue is -p; for p=1 mod6 it is +p. No all-prime proof or novelty claim is made for (5), and existing published results on these exact weighted sums need specific prior-art checking. Examples: p=5,11,23 yield respectively residues 120 mod125, 1320 mod1331, 12144 mod12167; p=13,19,97,373 yield p itself.

BRC observer: indexed signed original a,b populations, arithmetic p-valuations, path/cut provenance and future finite Green operation; no unproved native X6 transfer, no replacement of a fixed-373 native benchmark.

## Continuation and status

Next small scientific problem: an actual terminating hypergeometric/WZ certificate for the remaining cancellation on the RHS of (4). Test proposed identity including endpoints for p=5,11,13,19,23,97,373, then check prior-art status of all-class (5). The frozen D24 Delta_p-R_p second-digit bridge and native fixed-373 H0/B0/rank/Frobenius/independent replay stay separate.

Observed gateway 0.6.11: UPSTREAM_CODE_REVIEW_REQUIRED, research_authority_granted=false, executor_binding_configured=false, active_jobs 5/5. Standalone recovery_status not exposed in this client. No request reissue, cross-lane session, CLAIM, OPEN, native checkpoint, Result or admission. Control issue #1558 and native-373 issue #1559 remain assigned support paths; current detailed status was not mutated. GitHub author-side evidence is neutral, not Source durable checkpoint.

## Literature-aware refinement (same research turn)

Guo and Zudilin, *A q-microscope for supercongruences* (arXiv:1803.01830, revised 2019), Theorem 1.1 and its q→1 specialization establish for **all primes p>3**:
[
V_p=sum_{k=0}^{p-1}rac{inom{4k}{2k}inom{2k}{k}^{2}}{2^{8k}3^{2k}}(8k+1)
equiv pleft(rac{-3}{p}ight)pmod{p^3}.
]
Exact coefficient match: the denominator 2^(8k)*3^(2k)=2304^k, and the two binomial factors multiply to (4k)!/(k!)^4. Source: https://arxiv.org/abs/1803.01830 (abstract; text equations (2), (5), theorem 1.1). This is **established external mathematics**, not a discovery of Enterprise Math or merely numerical evidence.

Therefore the experimentally checked *pair* (5) has **asymmetric status**: its quartic V_p branch is a proven published theorem, while the 216 W_p branch and their comparison remain finite-data candidates here. On the mother target classes p≡13,19 (mod24), (-3/p)=+1, so the 216 target W_p≡p is *equivalent* (using this published theorem) to the unresolved mixed-kernel cancellation W_p−V_p≡0 mod p³. The exact all-prime Green/two-seam reduction (4) supplies an independent source-preserving representation of that obligation, not a substitute proof. For p≡5 (mod6), the known V_p value is −p, so testing the 216 signed extension on those primes adds a genuinely different diagnostic regime.

The 2019 published proof does not establish the six-channel/source-provenance Green decomposition or native X6/BRC interpretation. Conversely this author-side decomposition does not extend the theorem's admission status. Next action: use the Guo–Zudilin V theorem as a consumed input and seek a terminal certificate for W−V (or a sourced pre-existing W theorem), retaining the D24 second-digit bridge as separate.
