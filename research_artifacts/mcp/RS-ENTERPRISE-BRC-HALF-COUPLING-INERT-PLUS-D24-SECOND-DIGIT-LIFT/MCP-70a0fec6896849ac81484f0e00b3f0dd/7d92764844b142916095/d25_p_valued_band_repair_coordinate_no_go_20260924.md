# D25 LIFT — p-valued source band forces a first-digit repair coordinate, and the repaired pure-band path still has a universal terminal curvature defect

Status: PROVED_STRICT_REDUCTION_NO_GO_UNIT / LIFT_NOT_YET_CLOSED / NOT_A_RESULT / UNREVIEWED
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT
Publication: TP2-B6F4FC938FF94941C1B7
Date: 2026-09-24
Consumed canonical Source frontier: awdawmip/enterprise-math@030fee9a5e5ddec6995ce1f14d1de9b5dbc7ab61

## 0. Consumed frontier

Consume the durable supersingular repair-coordinate checkpoint and the just-published terminal p^2-band negative control. Do not reopen D24, prior D25 reductions, the prior-art audit, or the terminal p^2-band calculation. The live instruction is to expose a lower-valuation source layer while retaining the first-digit/repair information that division by p can otherwise erase.

Keep the accepted half-series

    B_k=(1/6)_k(1/3)_k / [(k!)^2 2^k],
    g=sum_{k=0}^{p-1} B_k,
    h=sum_{k=0}^{p-1}(12k+1)B_k,
    G=g/p,

for p=6m+1, p == 13 or 19 (mod 24). Accepted UR gives

    G h == 1 (mod p),

so Gbar:=G mod p and hbar:=h mod p are units with Gbar=hbar^{-1}.

## 1. Exact valuation stratification

For 0<=k<p, the denominators in B_k are p-units. The (1/6)_k numerator first acquires p at j=m, while the (1/3)_k numerator first acquires p at j=2m. Hence exactly

    v_p(B_k)=0,  0<=k<=m;
    v_p(B_k)=1,  m+1<=k<=2m;
    v_p(B_k)=2,  2m+1<=k<=p-1.

The middle band is therefore a genuine p-valued source layer. Put

    x_s := B_{m+s}/p (mod p),    1<=s<=m.

Every x_s is nonzero. The source recurrence gives

    BOXED:
    x_{s+1}/x_s = 3s(6s+1)/(6s+5)^2                 (mod p).       (X)

## 2. Why the scalar divided observer cannot cross one p-valued port

Remove a suffix of the p-valued band and add it back one port at a time:

    g_s = g - sum_{r=s+1}^m B_{m+r},
    h_s = h - sum_{r=s+1}^m (12(m+r)+1)B_{m+r},
    G_s = g_s/p.

Because every removed term is p-divisible, p|g_s and h_s==h (mod p). Define the first-digit coordinate

    I_s := G_s h_s (mod p).

Adding B_{m+s}=p x_s+O(p^2) changes G_s by x_s modulo p while h_s does not change modulo p. Therefore

    BOXED:
    I_s-I_{s-1}=hbar x_s != 0                       (mod p).       (I)

Consequently two adjacent single-port cutoffs cannot both lie on the fiber I=1. In particular the naive divided residual

    (G_s h_s-1)/p

is not p-integral along an adjacent p-valued cutoff chain. This is an information-loss theorem: a source construction that exposes a p-valued port cannot retain only the already-divided second digit; it must retain a first-digit mismatch/repair coordinate or an equivalent deformation.

## 3. Exact source repair coordinate

The missing coordinate can be retained without fitting. Put

    A_s := (g-g_s)/p = sum_{r=s+1}^m B_{m+r}/p.

Then G_s+A_s=G exactly. Define the compensated source path

    Q*_s := [ (G_s+A_s)h_s -1 ]/p
          = [ G h_s -1 ]/p                         (mod p).

Since h_s==h (mod p), Q*_s is p-integral for every s, and at the endpoint

    BOXED: Q*_m = (Gh-1)/p = Delta_p.

Thus A_s is an explicit source-derived repair port for the first-digit information that the naive quotient lost. No new axiom is introduced.

For one inserted p-valued port, 12(m+s)+1 == 12s-1 (mod p), so

    BOXED:
    U*_s:=Q*_s-Q*_{s-1}=Gbar(12s-1)x_s.             (U)

Combining (X) and (U),

    r_s:=U*_{s+1}/U*_s
       = 3s(6s+1)(12s+11)/[(6s+5)^2(12s-1)].

## 4. Canonical curvature comparison

Use the already-canonical prefix factors

    lambda_s=s^2(6s+1)/[(s+1)(2s+1)(3s+2)],

    mu_s=(2s+1)(3s+1)(3s+2)(6s+7)^2
         /[36(s+1)(6s+1)(s+2)(2s+3)(3s+5)].

Set

    V*_s=U*_{s+1}-lambda_s U*_s

and

    delta*_s=V*_{s+1}-mu_s V*_s.

Because U*_{s+1}=r_sU*_s,

    BOXED:
    delta*_s=U*_s E_s,

    E_s=r_s(r_{s+1}-lambda_{s+1})-mu_s(r_s-lambda_s).

Exact expansion gives

    E_s = -s(6s+7) P(s)
          /[36(s+1)^2(s+2)(2s+3)(3s+5)(6s+5)^2(6s+11)^2(12s-1)],

where

    P(s)=279936s^7+1819584s^6+4562244s^5+5448384s^4
         +2971197s^3+407769s^2-162200s-23910.

For every integer s>=1,

    407769s^2-162200s-23910 > 0,

and all higher terms are positive, hence P(s)>0 and E_s<0 as a rational number. Therefore even after preserving the required first-digit repair coordinate, the pure p-valued band does not satisfy the canonical mu-transport as a universal rational identity. The residual is retained, not fitted away.

## 5. Uniform terminal nonzero defect

At the final defect site s=m-2 (which exists for target p>=19), use m==-1/6 (mod p). Direct exact specialization yields

    E_{m-2} == 273403/9408,
    x_{m-2}/x_m == 128/819,
    12(m-2)-1 == -27.

Therefore

    BOXED:
    delta*_{m-2}
      = -(42062/343) Gbar x_m                         (mod p).      (T)

Here 42062=2*21031, and deterministic trial division through sqrt(21031)<146 gives 21031 prime; moreover 21031==7 (mod 24). Thus no target prime p==13 or 19 (mod 24) can divide 42062, while 343=7^3 is a p-unit. Since Gbar and x_m are units,

    BOXED: delta*_{m-2} != 0 (mod p)

for every target prime p>=19. For p=13, m=2 and the local defect site does not exist.

So the strongest local matching route is now ruled out for both isolated source layers tested so far:
- terminal valuation-two band: nonzero terminal curvature defect (previous checkpoint);
- middle valuation-one band, even after the necessary first-digit repair coordinate: nonzero terminal curvature defect (this checkpoint).

This does not refute LIFT. It proves that a successful local-transport construction must mix additional source information/layers or use a genuine parameter/Frobenius deformation; alternatively an endpoint proof must exploit the full Green defect pairing including earlier defects and initial mismatch coordinates.

## 6. BRC audit

Population: the p-valued source ports B_{m+s}, 1<=s<=m.
Observer: the terminal divided second digit Delta_p together with adjacent-cutoff operations and the canonical lambda/mu comparison.
Preserved: p, cutoff s, source index m+s, valuation one, x_s, first-digit coordinate I_s, repair port A_s, Gbar/hbar, U*,V*,delta*.
Unsafe quotient: divide G_s h_s-1 by p after dropping I_s/A_s. Equation (I) proves a single p-valued port leaves the I=1 fiber.
Safe repair: retain A_s until the compensated numerator is proved p-divisible.
BRC_REUSE_RESOLUTION=COMPOSE_APPLIED.

## 7. Exact regression

A companion checker reconstructs B_k modulo p^3 and verifies, for all 166 target primes p<5000 (83 in each residue class): exact valuation-band behavior on the tested source; (X); the first-digit jump (I); integrality and endpoint value of Q*_s; (U); the curvature formula; and (T), including nonzero terminal defect whenever the site exists. Failures: 0. The finite run is falsification/regression only; the all-target statements above are symbolic plus the fixed finite factorization of 42062.

## 8. Narrow next action

Do not seek another scalar one-band cutoff. Construct the smallest two-layer or parameterized source extension that keeps the first-digit repair coordinate and allows interaction between the p-valued contribution and the previously studied p^2 terminal band. Compute its source U,V,delta and the full Green endpoint pairing before any quotient. A cancellation seen only after erasing layer identity is not admissible. LIFT/JT2 remains open.
