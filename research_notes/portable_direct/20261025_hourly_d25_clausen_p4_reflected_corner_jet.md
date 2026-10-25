# D25/LIFT — Clausen reflected cutoff corner lifted from p^3 to p^4

Date: 2026-10-25. TASK_RESEARCH portable author-side derivation; logical research lane chatgpt-research-hourly-enterprise-math-20260923 (separate from control maintenance). Parent Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 remains unchanged.

**Claim/evidence status:** AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY. This is neither a winning Source CLAIM, native checkpoint, original CM/divided-power experiment, independent proof review, nor proof of D25/LIFT/JT2. In particular, it does not assert the full target supercongruence.

## Precise consumed source and new unit

Consume (without re-crediting) the exact rational Clausen identity and the mod-p^3 reflected corner theorem in research_notes/portable_direct/20261025_onhour_d25_clausen_reflected_p2_tail.md (source commit cefbad99f03e3b79e0cfc9de624481ed2010ae40), as well as the original W_p source-marked four-band factorization. The old result computes Q_p/p^2 only modulo p. The new unit computes its **entire next digit modulo p^2**, including both (i) deformation of the extreme reflected source and (ii) the previously invisible middle-rank cross-branch contribution.

Let p=6m+1>=7 be prime. All rational denominators are evaluated in Z_(p). Put

    r_n=(1/6)_n(1/3)_n/[2^n(n!)^2],
    a_n=(1/2)_n(1/3)_n(2/3)_n/[2^n(n!)^3],
    W_p=SUM_(n=0)^(p-1) (6n+1)a_n,
    R_p=SUM_(n=0)^(p-1) r_n,
    D_p=SUM_(n=0)^(p-1) n*r_n,
    Q_p=SUM_(0<=j,k<p; j+k>=p) (6(j+k)+1)r_j r_k.

The already proven exact rational identity is W_p=R_p(R_p+12D_p)-Q_p. For 0<=n<p, v_p(r_n)=1_(n>m)+1_(n>2m).

## New universal reflected two-digit corner theorem

For 1<=h<=2m define the **exact source-extracted** p-adic integer s_h=r_(p-h)/p^2; every such original coefficient has valuation exactly two. Define the endpoint s_1 by the following rational product, reduced modulo p^2 only *after* cancelling the two indicated p factors:

    s_1 =
       [PROD_(0<=i<=p-2, i != m) (6i+1)]
       [PROD_(0<=i<=p-2, i != 2m) (3i+1)]
       / [36^(p-1) ((p-1)!)^2].                            (1)

No denominator here is divisible by p. Define source-normalized reflected jets recursively (all terms read modulo p^2 unless explicitly marked modulo p):

    rho_1=1,  L_1=0;
    rho_(h+1)=rho_h * 36h^2 / [(6h+5)(3h+2)]  (mod p^2);
    L_(h+1)=L_h-2/h+6/(6h+5)+3/(3h+2)       (mod p).

For 1<=h<=2m,

    s_h = s_1 rho_h (1+p L_h)                  (mod p^2).   (2)

Write t_h=rho_h(1+pL_h), V_j=SUM_(h=1)^j t_h, and
M_j=SUM_(h=1)^j h*t_h. The complete source-labelled reflected corner is

    C_p = 2 s_1 SUM_(j=1)^(2m)
                r_j [(6j+1+6p)V_j-6M_j]       (mod p^2).   (3)

Then, for **every** prime p=6m+1>=7,

    Q_p = p^2 C_p                              (mod p^4),   (4)
    W_p = R_p(R_p+12D_p)-p^2 C_p               (mod p^4).   (5)

This uses O(m) modular recurrence/summation operations after generation of the necessary source r_j values. At lower precision, reduce C_p modulo p: middle ranks m<j<=2m vanish, s_1=1/10 modulo p, and (3) reduces to the previously proven reflected p^3 corner T_p. Thus (4) is a strict new precision lift, not a restatement of T_p.

### Proof and coverage of branches

All terms of Q_p with valuation below four have one index in 1..2m and the other in 2m+1..p-1; the threshold j+k>=p forces that other index to equal p-h with 1<=h<=j. A pair with both indices >2m has valuation >=4; pairs with both indices <=2m cannot cross the threshold since j+k<=4m<p. There are exactly two ordered orientations of each surviving pair. Therefore

    Q_p = 2 SUM_(j=1)^(2m) SUM_(h=1)^j
               [6(p+j-h)+1] r_j r_(p-h)       (mod p^4).  (6)

After factoring p^2 from the reflected coefficient, the bracket is 6j+1+6p-6h, which yields (3) and (4).

For h<2m, the **exact rational** backward source ratio is

    s_(h+1)/s_h =
       36(p-h)^2/[(6p-6h-5)(3p-3h-2)]
     = 36h^2/[(6h+5)(3h+2)]
       * (1-p/h)^2
       / [(1-6p/(6h+5))(1-3p/(3h+2))].

Each displayed denominator is a p-unit on this bounded interval. Expanding only p-unit factors through the first jet gives (2), while (1) follows directly by stripping the unique p factor 6m+1 and the unique p factor 3(2m)+1 from the exact source numerator of r_(p-1). Finally substitute in (6), and apply the previously proven exact rational Clausen cutoff identity. QED.

## New source-information witness: vanishing at one digit hides the next

Define C_low from (3) with 1<=j<=m and C_mid with m<j<=2m, both modulo p^2. The second part is necessarily divisible by p but need not vanish modulo p^2; it was absent at p^3.

| p | C_low mod p^2 | C_mid mod p^2 | C_p mod p^2 | T_p=C_p mod p | next carry floor(C_p/p) |
|---:|---:|---:|---:|---:|---:|
| 13 | 78 | 26 | 104 | 0 | 8 |
| 19 | 183 | 38 | 221 | 12 | 11 |
| 373 | 7283 | 58561 | 65844 | 196 | 176 |
| 1327 | 982028 | 1386715 | 607814 | 48 | 458 |
| 19963 | 238990436 | 132015319 | 371005755 | 13363 | 18584 |

Most notably, at p=13 the entire previous reflected observer has T_13=0, while the **same actual cutoff corner** is Q_13=13^3*8 (mod 13^4), nonzero. Of the carry 8, six units arise from the higher precision of the original low-to-extreme corner, and two from the newly admitted middle-to-extreme source branch. This is an explicit signed, valuation-labelled BRC information-preservation witness: zero at one precision is not a license to delete a branch at the next precision.

Here the bracket values, modular ranks and signed arithmetic are exact source coefficients; no positive-mass histogram was substituted for a signed sum. The finite auxiliary indices do not represent native Enterprise X6 spatial axes, and no P000 geometric claim or native BRC/CM execution is made.

## Independent author arithmetic checks

Companion: research_notes/portable_direct/20261025_hourly_d25_clausen_p4_reflected_corner_jet_check.py.

The program generates r_n using the original exact hypergeometric recurrence modulo p^4, generates W_p separately using the original 3F2 recurrence, evaluates s_1 independently by the factorial product (1) and s_h via the jet recurrence (2), and verifies **each** source-reflected coefficient against independently computed r_(p-h)/p^2. Then it checks (5). For every p<=300 it also computes the complete O(p^2) ordered double-sum Q_p and checks (4) independently. All 28 primes p=1 (mod6) <=300 and additional p=373,1327,19963 passed (31 primes in total). These finite checks corroborate, but do not replace, the all-prime argument above.

## Parent and exact continuation

The original *p^3* mother target remains the coupled moment condition

    R_p(R_p+12D_p) = p+p^2 T_p (mod p^3)

for p=13,19 (mod24). This document proves no universal RHS identity. Next mathematical action: use the verified first two reflected digits and the p^3 T_p branch provenance to seek an exact Gauss/Jacobi-sum, finite hypergeometric, or Picard–Fuchs/Frobenius certificate of the p^3 **coupled moment**; an independent all-target source certificate is required, not a prime scan. Next native scientific evidence remains authenticated same-original-class H_0/B_0, [X]U mod p^2, Frobenius rank/direction/normalization, and the valid kappa / Delta_p-R_p map; native CM is NOT_RUN.

The last Research lane control reports no new winning CLAIM/open and a typed predecessor-CAS obstacle tracked in enterprise-math Issue #1558; neither the author-source Git commit nor this notebook creates canonical predecessor progress. Preserve the existing native checkpoint, source pins, contributor history and original requests. No new scheduler, GitHub Actions, cron or notification changes.
