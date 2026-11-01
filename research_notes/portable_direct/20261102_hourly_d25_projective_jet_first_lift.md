# D25 — exact first p-adic lift defect of the weighted projective 2-jet (2026-11-02)

**AUTHOR-DERIVED / EXACT ALGEBRA / EXACT-CHECKED 107 TARGET PRIMES p<=3000 / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_EXECUTED.** This is the next scientific unit after `d5d2fe19b8cfd3d8702a8e7f1ebd7113b1fc1093`; it does not repeat the other onhour lane's previously proven weighted PF gauges. Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; **frozen** scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`.

## Algebraic theorem over Z_(p), every prime p>3

Define the *original* finite unweighted hypergeometrics

```
F_A(z)=sum_{0<=k<p} [(1/2)_k(1/3)_k(2/3)_k/(k!)^3]z^k,
F_B(z)=sum_{0<=k<p} [(1/4)_k(1/2)_k(3/4)_k/(k!)^3]z^k;
theta=z*d/dz; Y_A=(1+6theta)F_A; Y_B=(1+8theta)F_B.
f_j=(theta^j F_A)(1/2); g_j=(theta^j F_B)(1/9);
a_j=(theta^j Y_A)(1/2); b_j=(theta^j Y_B)(1/9).
```

Let `c_p=(1/2)_p(1/3)_p(2/3)_p/(p!)^3` and `d_p=(1/4)_p(1/2)_p(3/4)_p/(p!)^3`; these are p-local. Define original weighted slope defects `E_A=a_2-(5/3)a_1`, `E_B=b_2-(5/16)b_1`, and cross-model first-lift defect `D_p=16 b_2 a_1-3 b_1 a_2`. **Exact equalities before any reduction**:

```
E_A = (8/3)f_1+(2/3)f_0 - 12p^3 c_p 2^(-p),
E_B = (3/8)g_1+(3/32)g_0 - 9p^3 d_p 9^(-p),
D_p = 16a_1 E_B - 3b_1 E_A
    = 6a_1 g_1 + (3/2)a_1 g_0 - 8b_1 f_1 - 2b_1 f_0
      + p^3[36b_1 c_p 2^(-p)-144a_1 d_p 9^(-p)].
```

**Proof.** The exact finite 3F2 equation has `(1-z)theta³F=z[(3/2)theta²F+e_1 theta F+e_0 F]-p³ c_p z^p`. For A, `(e_1,e_0)=(13/18,1/9)`, and at `z=1/2`,

```
theta³F_A=(3/2)f_2+(13/18)f_1+(1/9)f_0-2p³c_p2^(-p).
```

For B, `(e_1,e_0)=(11/16,3/32)`, and at `z=1/9`,

```
theta³F_B=(3/16)g_2+(11/128)g_1+(3/256)g_0-(9/8)p³d_p9^(-p).
```

Insert into `a_1=f_1+6f_2`, `a_2=f_2+6theta³F_A`, `b_1=g_1+8g_2`, `b_2=g_2+8theta³F_B`. The f2/g2 terms cancel in `E_A,E_B`; expanding `16a1 EB-3b1 EA` gives the stated exact identity. QED. These precise terminal p³ terms remain visible for higher precision; they are *not* the separately typed original signed Clausen cutoff.

## Conditional first-digit theorem

Assume double zeros `f_0=f_1=g_0=g_1=0 modp`, with nonzero mod-p weighted derivatives `a_1,b_1`. Then `E_A,E_B,D_p` belong to `p Z_(p)` and their genuine first digit is

```
D_p/p ≡ 6a_1(g_1/p)+(3/2)a_1(g_0/p)
        -8b_1(f_1/p)-2b_1(f_0/p)  (mod p).
```

The first digits `f_j/p,g_j/p` are *true p-local quotients* after verifying divisibility. Since `a_1,b_1` are units, `D_p=0 modp²` is equivalent to the **fixed normalized projective 2-jet** relation `16 b_2/b_1 = 3 a_2/a_1 modp²`. It is NOT equivalent to the mother 216/2304 weighted-sum congruence. The B double-zero hypothesis still requires a uniform proof beyond finite checks.

## Finite exact original-coefficient certificates

The actual integer `mod p²` original 216/2304 sums and four Euler moments, evaluated by the companion Python standard-library checker at **all 107 target primes `p<=3000`**, satisfy both exact formulas mod p², the double-zero hypotheses, and `D_p∈p Z_(p)`. At all 107, `D_p/p` was **nonzero**, a finite-range observation only:

```
p  D_p (mod p²)  D_p/p(mod p)  E_A/p  E_B/p
13       91           7         12     10
19      285          15         11     14
37      703          19         21     33
61     2501          41         14      1
373  136145         365        332    239
```

**Special p13 next-digit failure.** The preceding scientific unit showed that *derivative* rays are scalar-proportional mod13. The exact full original weighted jets mod169 are `A=(13,68,44)`, `B=(13,20,94)`. The unique scalar matching the first derivative is `lambda=50 mod169`, which leaves zeroth residual `39 mod169` and second residual `91 mod169`. Thus this p13 accidental mod-p match does **not** lift to full 3-jet scalar equality mod169; and the projective normalized diagonal relation already has `D_13=91 !=0 mod169`.

## BRC and continuation

BRC **COMPOSE_APPLIED**: retain original finite-coefficient identity, explicit prime/coefficient ring, ordered 2-jet ports, exact terminal p³ sources and future operation (projective comparison then p-adic lift). The new repair coordinate `D_p/p` captures information lost by mod-p slope compression; neither unsigned scalar equality nor positive branch mass reproduces it. All-prime nonzero `D_p` is **not** asserted.

**Next science:** source-classify the four p-adic first-digit CM ports `f_0/p,f_1/p,g_0/p,g_1/p`; build and test a non-scalar, possibly p-dependent weighted 2x2 jet transport at p19,p373 through the first lifted digit. Only then connect the original **signed** Clausen cutoff to `Delta_p-R_p=0 modp`. The p373 original fixed-class native H0/B0 benchmark ([EM #1559](https://github.com/awdawmip/enterprise-math/issues/1559)) remains PENDING_OWNER/NOT_EXECUTED. Research control was last observed Gateway 0.6.11 `UPSTREAM_CODE_REVIEW_REQUIRED`, `research_authority_granted=false`, `executor_binding_configured=false`; own prior recovery bridge #6637 SUCCEEDED, prior continuation #6638 FAILED, and support #1558 already owns the fault. This neutral publication grants **no** CLAIM, OPEN, Source checkpoint, Result, activity registration or independent mathematical admission. `REGISTER_PENDING / NOT_ADMITTED`; P000/ACTIVE worldview and frozen scientific pin intact, original scheduler and notifications untouched.
