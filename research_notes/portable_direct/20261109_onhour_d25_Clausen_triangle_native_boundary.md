# D25 / Original 216–2304 signed Clausen triangular-boundary certificate

Date: 2026-11-09. TASK_RESEARCH portable author-side, mathematical proof using classical Clausen identity plus original integer valuation; exact finite regression. UNREVIEWED / NOT_ADMITTED / NOT_NATIVE.
Research logical lane: chatgpt-research-onhour-enterprise-math-20260923 (not maintenance).
Parent: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; immutable publication TP2-B6F4FC938FF94941C1B7; scientific input frozen c47e13e4aba0e006366f989d6334d443f6333ae3.

## Source and exact identities

Let A_n=(2n)!(3n)!/((n!)^5*216^n), C_n=(4n)!/((n!)^4*2304^n). The ORIGINAL signed full cutoffs are W_p=sum_{0<=n<p}(6n+1)A_n and V_p=sum_{0<=n<p}(8n+1)C_n.

Define two *lower-order coefficient carriers* (all k<p; p>3):

f_k=(1/6)_k(1/3)_k / ((k!)^2*2^k),
g_k=(1/8)_k(3/8)_k / ((k!)^2*9^k).

Their exact consecutive ratios are f_{k+1}/f_k=(6k+1)(3k+1)/[36(k+1)^2] and g_{k+1}/g_k=(8k+1)(8k+3)/[576(k+1)^2].

Classical Clausen identity (DLMF 16.12.2, https://dlmf.nist.gov/16.12.E2) with (a,b)=(1/6,1/3), respectively (1/8,3/8), gives the **coefficientwise exact rational identities**

A_n=sum_{k=0}^n f_k f_{n-k}, C_n=sum_{k=0}^n g_k g_{n-k} (n>=0).

For X=A or C put h=f or g, weight d=6 or 8, S_X=sum_{k=0}^{p-1}h_k, D_X=sum_{k=0}^{p-1} k h_k, and define the triangular boundary

T_{X,p}=sum_{0<=k,l<p, k+l>=p} [d(k+l)+1] h_k h_l.

Then the **exact finite full-cutoff relation over Q** is

sum_{n=0}^{p-1}(dn+1)X_n = S_X^2 + 2d*S_X*D_X - T_{X,p}.                     (1)

The entire truncation boundary, original signed weight and both summation sources remain present. Omitting T is a different model.

## Theorem 1: p-adic triangular boundary for 216, p=6m+1

For EVERY prime p=6m+1, the 216 triangular tail T_{A,p} is in p^2 Z_(p). More precisely, let

L_A(j)= [2^(j-1)*(j-1)!^2] / [18*(5/6)_j*(2/3)_j] in F_p, 1<=j<=m.

All denominators here are p-units, and

f_{p-j}/p^2 == L_A(j) (mod p),        1<=j<=m.                               (2)

Consequently the *full* signed triangular boundary has the low-index certificate

T_{A,p}/p^2 == 2 * sum_{j=1}^m sum_{k=j}^m [6(k-j)+1] f_k L_A(j) (mod p).     (3)

Proof: for p=6m+1, the numerator roots of f at indices m and 2m give v_p(f_k)=0 for 0<=k<=m, 1 for m<k<=2m, and 2 for 2m<k<p. If k+l>=p, both indices cannot lie in the first two bands, and any pair except one 0-band and one 2-band is at least valuation 3. For a valuation-2 pair the low index k obeys 1<=k<=m; setting the high index l=p-j forces 1<=j<=k. Both orientations give factor 2. In this range weight 6(k+p-j)+1 reduces to 6(k-j)+1 modulo p.

For a rational alpha with exactly one p-factor at t_alpha in (alpha)_{p-j}, remove the root, use Wilson's product of all nonzero residues, and divide off the last j factors. It gives (alpha)_{p-j}/p == ((alpha+t_alpha)/p)*(-1)^(j+1)/(1-alpha)_j mod p. For alpha=1/6 and 1/3 the two root factors divided by p are 1/6 and 1/3. Furthermore (p-j)! == (-1)^j/(j-1)! modulo p and 2^(-(p-j))==2^(j-1) modulo p. The signs cancel to give (2), then the valuation split yields (3).

## Theorem 2: p-adic triangular boundary for 2304, p == 1 or 3 (mod 8)

For EVERY prime p==1 or 3 (mod 8), set a=floor((p-1)/8). Then T_{C,p} is in p^2 Z_(p). Define

L_C(j)= 3*9^(j-1)*(j-1)!^2/[64*(7/8)_j*(5/8)_j] in F_p, 1<=j<=a.

All denominators are p-units. The original 2304 tail obeys

g_{p-j}/p^2 == L_C(j) (mod p),         1<=j<=a,                              (4)

T_{C,p}/p^2 == 2 * sum_{j=1}^a sum_{k=j}^a [8(k-j)+1] g_k L_C(j) (mod p).     (5)

Proof: for p=8a+1 the roots of (1/8)_k,(3/8)_k are at a and 3a; for p=8a+3 they are at 3a+1 and a. Thus g_k has valuations 0 on 0..a, 1 until the second root, and 2 thereafter. No pair with k+l>=p can have both valuations <=1, and only 0+2 pairs contribute modulo p^3. The reflection product has root quotients 1/8 and 3/8 in either order, so their product is 3/64; (p-j)! and 9^(-(p-j)) give (4). The same low/high separation proves (5). This includes the frozen class p==19 (mod 24); its companion class p==13 (mod 24) lies in the other 2304 valuation regime and is treated by (1) without discarding its nonzero p-level tail.

## Exact arithmetic and class asymmetry

Original W,V and (1) are exact rational equalities. In modulo p^3 tests, A,C are computed separately using integer binomial coefficients with p-unit denominators. T/p^2 is recomputed from the two lower-index boundary kernels, not inferred from W,V. No float or numerical approximation.

- p=13: T_A/p^2 mod13 =0, while T_C/p mod13=12 (so the 2304 triangular boundary is not universally p^2-divisible in the p==13 class).
- p=19: T_A/p^2 mod19=12; T_C/p^2 mod19=3.
- p=37: T_A/p^2 mod37=11; T_C/p mod37=36.
- p=43: T_A/p^2 mod43=15; T_C/p^2 mod43=14.
- p=73: T_A/p^2 mod73=49; T_C/p^2 mod73=49.
- p=373: T_A/p^2 mod373=196; T_C/p mod373=372.

Executed script d25_Clausen_triangle_boundary_exact_20261109.py over all 72 primes 5<=p<=373 checks both original weighted Clausen coefficient reconstructions (144 model-prime checks) and all 68 eligible valuation/reflection/low-triangle cases; PASS.

## Use in the actual parent and remaining proof

For EVERY p==19 mod24, (1), (3), (5) yield two exact reduced lower-index observations mod p^3:

W_p == S_A^2+12 S_A D_A - p^2 R_A (mod p^3),
V_p == S_C^2+16 S_C D_C - p^2 R_C (mod p^3),

where R_A and R_C are precisely the right sides of (3),(5), not omitted corrections. The original AF4 combination W_p-2V_p+p*(-3/p) modulo p^3 therefore admits a two-period-plus-low-triangle certificate. In the p==13 class use full T_C as given by (1); p13 and p373 prove that simply discarding it at precision p^2 is invalid.

This is a new alternate Clausen/symmetric-square reduction for the exact original signed observer, using residual-preserving paired index coordinates (k,l) and the low/high carry across k+l=p. Its scope is the displayed mod-p^3 interface, not the all-prime AF4 mod-p^4 cancellation or the frozen native LIFT conclusion. Next science action: evaluate whether the bounded low triangular sums admit a Jacobi/Fricke evaluation for p==19 mod24, then extend the 2304 p==13 class while retaining its earlier p-level tail. The authoritative native p373 fixed H0/B0 [X]U mod139129, rank, semilinear Frobenius direction/eta, signed odd kappa, original Delta-R and independent validation remain NOT_EXECUTED, tracked by existing #1559 (PENDING_OWNER); this note is not that experiment.
