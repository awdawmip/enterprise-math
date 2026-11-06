# D25: p-adic lift of the complementary finite Gauss endpoint pair

Date 2026-11-06. TASK_RESEARCH, AUTHOR-PROVED exact finite operator / independently FINITE-VERIFIED / UNREVIEWED / NOT_ADMITTED. Same frozen D25 publication TP2-B6F4FC938FF94941C1B7 and Source c47e13e4aba0e006366f989d6334d443f6333ae3. This extends the newly proved mod-p complementary signed kernel at Enterprise Math main@50a0dc4bf6ae6a495d6cd870e410cd6e78e48367 without replacing native fixed H0/B0 experiment (#1559).

Let p=6m+1>3 prime, theta=z d/dz. Set d_i=(1/6)_i(1/3)_i/(2^i(i!)^2), 0<=i<=m, and e_1=1/10, e_(r+1)=36r^2 e_r/[(6r+5)(3r+2)] for 1<=r<m, rational numbers. Define D_m(z)=sum_(i=0)^m d_i z^i, E_m(z)=sum_(r=1)^m e_r z^r. All their displayed denominators are p-units.

**NEW exact rational pair of inhomogeneous operator equations (all primes p=6m+1>3)**:

  [36 theta^2-z(6theta+1)(3theta+1)] D_m(z)
       = -p(3m+1)d_m z^(m+1),                            (D1)

  [(6theta-1)(3theta-1)-36z theta^2] E_m(z)
       = z-36m^2 e_m z^(m+1).                             (D2)

Proof: 36i^2 d_i=(6i-5)(3i-2)d_(i-1), for i>=1. Every interior coefficient in (D1) cancels. The missing degree m+1 coefficient equals -(6m+1)(3m+1)d_m=-p(3m+1)d_m. Similarly e_(r+1)/e_r=36r^2/[(6r+5)(3r+2)], interior coefficients of (D2) cancel; its degree-1 coefficient equals 10e_1=1 and top degree m+1 equals -36m^2e_m. These equalities are in Q[z], not just mod p.

**Valuation information needed for the p-adic second digit.** d_m,e_m,(3m+1),m are p-adic units; hence the low-Gauss source in (D1) has valuation exactly one, while both companion sources of (D2) have valuation zero. Thus the homogeneous mod-p equation for D_m from the previous note does not remain homogeneous modulo p^2: discarding the p*z^(m+1) term destroys precisely a first p-adic digit potentially needed by D25 LIFT. At z=1, letting S_low=sum_(i=0)^m d_i, T_low=sum i d_i and M2_low=sum i^2d_i, (D1) gives the exact endpoint moment equation

  18 M2_low -9 T_low - S_low = -p(3m+1)d_m.            (D3)

This is a *different truncated population* from the already established full p-term Picard source of valuation two. Neither low-cutoff equality may silently replace the full source. This witnesses the BRC information that a low/high branch projection loses beyond mod p.

**Existing parameter-jet identity consumed, not newly credited:** b_i=2^(-i)C(m,i)C(2m,i) and H_i=sum_(t=0)^(i-1)[1/(6t+1)+1/(3t+1)]. For 0<=i<=m,

  d_i = b_i(1+p H_i) mod p^2.                           (D4)

Its immediate proof is the exact factorization (-m)_i(-2m)_i/( (1/6)_i(1/3)_i )=product_t (1-p/(6t+1))(1-p/(3t+1)). We use it to transport the established parameter jet into the same low branch and to check the lift; novelty of (D4) is not asserted.

**Executed exact finite checks:** New independent Python standard-library code d25_gauss_low_boundary_padic_check_20261106.py verifies *every coefficient* of (D1)-(D2) through degree m+1 modulo p^2, the exact valuation-one endpoint, and (D4), for all 80 primes p=6m+1, 7<=p<=997. All assertions pass. Representative pairs [source of (D1)/p modp, top source of (D2) modp] are p13 (9,4), p19 (13,18), p67 (31,31), p373 (180,336). These are distinct sources, both needed for an honest coupled Green construction.

**Next precise science:** Construct a p-adic coupled finite Green/Lagrange bilinear concomitant from (D1)-(D2) and the exact signed convolution observer J. Keep the valuation-one low endpoint, valuation-zero complementary endpoints, existing middle/high signed cutoff and full p-term Gauss moments separately. Seek equality 24GM2-(p/3)G^2=1+2pJ (mod p^2) for the frozen p13,19 (mod24) scope; a candidate must match nonzero J19,J373 without assuming the target identity. This is OPEN. The author proof and finite checker are not Source native CLAIM, Result, independent review, or the original same-class divided-power Frobenius computation (#1559).