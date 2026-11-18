# R762EA — Exact second 3-adic spectral stratum of full-three-coordinate positive BRC

Date: 2026-11-18 (Asia/Shanghai). Task RS-X6-TRIADIC-CLOSURE-DYNAMICS, publication TP2-8B7E13C5904A2D6F1142. Author lineage EM-X6-3050F6, original SID MCP-4b2d70a97f594366a7c94a0f8b45df38, claim MCP-d6d2c143cc4d2df4dea1c00c. Author proof and exact BRC checker; independent review NOT_REVIEWED.

Frozen P000 V5: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json. Frozen taskbook: @e3f42efac29a2da2d95be391f3231a664e2fade0:research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md. Reuse R762DZ@d892b3caced676c47e0f008a84358060aee76fe9 and the same six named BRC branch increments 000,100,001,110,011,111.

## Theorem (complete first two cyclotomic strata)

Let Q=3^a, a>=2, d=3^(a-1), and let ζ be a primitive Qth root in K=Q_3(ζ). Write w=ζ−1, v_w(w)=1, v_3=v_w/(2d). For the integer six-branch BRC polynomial

\[
P(X,Y,Z)=1+X+Z+XY+YZ+XYZ,\qquad
\lambda_{ijk}=P(\zeta^i,\zeta^j,\zeta^k),\quad (i,j,k)\in(\mathbb Z/Q)^3,
\]

every finite v_w(λ) is even. The exact distribution of the first two finite valuation strata is

\[
\boxed{\begin{array}{c|c|c}
v_w(\lambda)&v_3(\lambda)&\#\text{characters}\\ \hline
2&1/d&(2/3)Q^3\\
4&2/d&(16/81)Q^3\\
\ge6\ \text{or}\ \infty&\ge3/d&(11/81)Q^3
\end{array}}
\]

The first stratum agrees with R762DZ. The second stratum and parity are new. An explicit second-stratum witness is (i,j,k)=(0,1,3), for every a>=2.

## Proof: palindromic BRC and even valuations

The six BRC branches pair under complement of the exponent triple. Hence the exact Laurent identity

\[
P(X,Y,Z)=XYZ\,P(X^{-1},Y^{-1},Z^{-1}).
\]

Choose the unique residue s modulo odd Q with 2s=i+j+k (mod Q), and put β=ζ^{-s}λ. Cyclotomic conjugation ζ↦ζ^{-1} gives bar(λ)=ζ^{-(i+j+k)}λ, hence bar(β)=β. Thus β belongs to the index-two fixed field K^+. Since K/Q_3 is totally ramified of degree 2d, K^+/Q_3 is totally ramified of degree d. The w-valuation on K^+ is therefore even. The factor ζ^{-s} is a unit, proving evenness of every finite v_w(λ).

## Proof: exact quadratic and quartic coefficients

Set x=X−1,y=Y−1,z=Z−1. The exact six-branch identity is

\[
P=6+3(x+y+z)+2xy+xz+2yz+xyz.
\]

For a>=2, v_w(3)=2d>=6, so constant 6 and linear 3(x+y+z) do not contribute at degrees below w^6. Use ξ_t=(1+w)^t−1 and b_m(t)=\binom t m. Direct expansion of the named branches gives degree-two coefficient D=2ij+ik+2jk, degree-three coefficient

\[
E_3=2[ib_2(j)+b_2(i)j]+[ib_2(k)+b_2(i)k]+2[jb_2(k)+b_2(j)k]+ijk
\]

and degree-four coefficient

\[
\begin{aligned}
E_4={}&2[ib_3(j)+b_2(i)b_2(j)+b_3(i)j]\\
&+[ib_3(k)+b_2(i)b_2(k)+b_3(i)k]\\
&+2[jb_3(k)+b_2(j)b_2(k)+b_3(j)k]\\
&+b_2(i)jk+ib_2(j)k+ijb_2(k).
\end{aligned}
\]

The exact integer identity

\[
2E_3=(i+j+k-2)D-3ijk
\]

proves E_3≡0 (mod 3) whenever D≡0 (mod 3). Thus v_w(λ)=2 iff D≠0 mod 3; when D=0 the value is at least 4. D has residue frequencies 0:9, 1:6, 2:12 on the 27 first-digit triples.

Write the first two base-three digits as i=a0+3A (mod 9), j=b0+3B, k=c0+3C, all six digits 0,1,2, and h(t)=1 for the digit 2, else 0. By the mod-three binomial digit identity, b_2(t)≡h(t mod 3), b_3(t)≡floor(t/3) mod 3. Consequently

\[
E_4\equiv (2b_0+c_0)A+(2a_0+2c_0)B+(a_0+2b_0)C+K_0\pmod3,
\]
where
\[
\begin{aligned}
K_0={}&2h(a_0)h(b_0)+h(a_0)h(c_0)+2h(b_0)h(c_0)\\
&+h(a_0)b_0c_0+a_0h(b_0)c_0+a_0b_0h(c_0).
\end{aligned}
\]

On the nine triples (a0,b0,c0) with D=0, the linear coefficient vector (2b0+c0,2a0+2c0,a0+2b0)=grad(D) vanishes only at 000, where K_0=0. Each of the other eight triples has a nonzero linear functional of (A,B,C), so E_4 takes each residue precisely nine times among its 27 lifts. Exactly 8×18=144 first-two-digit triples have D=0,E_4≠0; exactly 8×9+27=99 have D=E_4=0. There are 9^3=729 possible first-two-digit triples, and each occurs (Q/9)^3 times modulo Q. Hence the second stratum contains 144(Q/9)^3=(16/81)Q^3 characters. The complement from the D-zero set contains 99(Q/9)^3=(11/81)Q^3; its w-valuation is at least 5 by the coefficient expansion and at least 6 by the parity lemma. The D-nonzero 18/27 class completes the theorem.

## Reproducible evidence and scope

The companion R762EA_VERIFY.py sums all six original character monomials directly, expands ζ^t=(1+w)^t to coefficients through w^5 with integer binomial coefficients, and reduces modulo 3. Since 3 has w-valuation at least 6, its first nonzero coefficient in this range is a rigorous low-valuation witness. This direct checker is independent of the quadratic/quartic product-formula derivation.

Exhaustive runs: Q=9 (9^3=729 characters) gave valuation 2:486, 4:144, at least 6:99. Q=27 (27^3=19,683 characters) gave valuation 2:13,122, 4:3,888, at least 6:2,673. All exact assertions PASS. R762EA_EVIDENCE.json records the output. All-a proof comes from the first-two-digit classification, not finite extrapolation.

This theorem concerns the full three-coordinate *candidate positive endpoint BRC observer*. Its future-safe quotient has not been certified for native signed TRIADIC_CLOSURE_E Cell/Link/Port updates or V17/V29/V39 transport. The project P000 six-dimensional signed spatial foundation, three-force provenance, and joint-observer safety remain unchanged.

Next questions: classify the w-valuation >=6 stratum, noting that the integer 3 first enters at w-degree 2d; derive an explicit coefficient nondivisibility witness to decide the R762DN all-horizon content conjecture v_3(c_Q(n))=max(0,floor(n/d)-2); and obtain actual native triadic event admission and V17/V29/V39 source mapping. This is a reusable author proof, not independent review or a promoted Result.
