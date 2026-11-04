# D25 216 upper shell: exact 3F2 port and nonzero terminal forcing
2026-11-05 · TASK_RESEARCH author-side · UNREVIEWED / NOT_ADMITTED / NATIVE_SYNC_DEBT
Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT · TP2-B6F4FC938FF94941C1B7 · frozen source c47e13e4aba0e006366f989d6334d443f6333ae3.
Research conversation chatgpt-research-onhour-enterprise-math-20260923 (never maintenance conversation). Source: research_notes/portable_direct/20261105_onhour_d25_weighted_shell_literature_reduction.md, which establishes W_full-W_half = p²*T_A(p) (mod p³) with T_A the signed 216 original upper shell. The Guo–Zudilin 2019 Adv. Math. result independently establishes both 2304 full and half sums = p*(-3/p) (mod p³); its DOI is 10.1016/j.aim.2019.02.008. That finished source is consumed, not reproved.

## Theorem 1 — fixed-parameter hypergeometric transport with original provenance
For **every prime p=6n+1>=7** put
C_p = 216^(2n)*((2n)!)^5/((4n+1)!) in F_p*,
h_r = ((2/3)_r)^3/((7/6)_r (4/3)_r r!) in F_p*, 0<=r<n,
H_n(z)=sum(r=0..n-1)h_r*z^r, theta=z*d/dz.
Then

    T_A(p) = 3*C_p*(1+2*theta)H_n(2) mod p.

PROOF: The exact source factorial shell is
T_A=sum(j=floor(p/3)+1..(p-1)/2) (6j-1)*216^(j-1)*((j-1)!)^5/((2j-1)!*(3j-p-1)!) mod p.
Write j=2n+1+r, r=0..n-1, and let u_r denote its *unweighted* factorial summand. u_0=C_p and
u_(r+1)/u_r=216*(2n+r+1)^5/((4n+2r+2)*(4n+2r+3)*(3r+2)*(3r+3)*(3r+4))
= 2*(r+2/3)^3/((r+7/6)*(r+4/3)*(r+1)) mod p
= 2*h_(r+1)/h_r.
The displayed denominators are units for the used transitions r<=n-2. The original signed weight 6j-1 = 12n+5+6r = 3*(2r+1) mod p. Hence the announced finite sum. The j↔r source index, signed weight and valuation-two port are retained. QED.

## Theorem 2 — unavoidable nonzero terminal differential source
Let L=theta(theta+1/6)(theta+1/3)-z(theta+2/3)^3. In F_p[z],

    L H_n(z) = (h_(n-1)/8)*z^n,   h_(n-1) != 0 mod p.

PROOF: The hypergeometric coefficient recurrence makes the coefficients of z^0,...,z^(n-1) of L H_n vanish. The coefficient of z^n is -(n-1+2/3)^3*h_(n-1)=+h_(n-1)/8 because n-1/3=-1/2 in F_p. All factors of h_(n-1) are nonzero for the stated range, so the source is a unit. In particular the next denominator (7/6)_n contains (n+1/6)=p/6 and is zero mod p, whereas the numerator is a unit. Thus H_n cannot be replaced by a homogeneous mod-p infinite 3F2 without losing this terminal source. QED.

At z=2 let tlast=h_(n-1)*2^(n-1), ulast=C_p*tlast, the last unweighted original upper-shell term j=3n. The last **signed** shell term is (18n-1)ulast=-4ulast (mod p); and

    (L H_n)(2)=tlast/4= -(last signed shell term)/(16 C_p).

This is an explicit mandatory signed boundary for candidate WZ/Green operators, not yet an all-prime proof of W_p=V_p (mod p³). On target classes p≡13,19 (mod24), the open *equivalent* half-sum target is

    W_half ≡ p - 3p² C_p(1+2 theta)H_n(2) (mod p³).

## Actual integer checks
Two independent carrier computations (original shifted factorial shell versus finite 3F2 recurrence) and full polynomial coefficient verification of L H_n=(h_(n-1)/8)z^n were run for all **611** primes 7<=p<=10000, p≡1(mod6): zero mismatches, zero boundary failures. The whole T_A sum was nonzero in those 611 *finite* tests; the all-prime nonzero theorem concerns the **terminal forcing**, not the full T_A sum.
(p,n,T_A,C_p,H_n(2),theta H_n(2),[z^n]L H_n):
(13,2,10,3,2,1,9); (19,3,9,17,4,2,16);
(139,23,13,31,112,33,24); (373,62,266,192,334,361,251).
Checker: research_notes/portable_direct/d25_216_shell_pole_3f2_checker_20261105.py.
BRC: COMPOSE_APPLIED, exact signed provenance carrier (216,p,j,r,p-adic valuation=2,weight,coefficient,terminal pole); projection is limited to T_A and derivative/terminal observers, never a native H0/B0 transfer.

## Source/liveness and next discriminating action
Mother objective Delta_p-R_p=0 mod p on p≡13,19 mod24, with original fixed p373 H0/B0 divided-power [X]U mod139129, actual module rank, semilinear Frobenius eta, kappa, odd branch and independent replica still NOT_EXECUTED / PENDING_OWNER at Issue #1559. Our last native read request onhour11-20261105-0103-current-cont was SUCCEEDED but execution_authorized=false; no own native session/CLAIM/run/checkpoint or Result is asserted. Historical failed request onhour-d25-20261104-1702-continuation-read is not reissued. Next: construct a terminating WZ/q/CM half-sum certificate with boundary flux h_(n-1)/8 (equivalently -last_signed/(16 C_p)); compare its p² correction to 3 C_p(1+2 theta)H_n(2) at p=13,19,139,373, then establish or falsify the uniform claim. Separately pursue the independent original-class native H0/B0 support item using genuine Source authority. Prior Sun/Green/CM results and historical staging remain separate.
