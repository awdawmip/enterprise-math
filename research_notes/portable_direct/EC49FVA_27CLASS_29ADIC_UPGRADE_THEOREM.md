# EC49FVA addendum — signed 29-adic valuations certify 27 of 29 classes

Date: 2026-11-20 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_SIGNED_VALUATION_CASE_SPLIT / NOT_REVIEWED.

This strengthens the EC49FVA 24-class theorem at PR #2868, using the same frozen BRC16943 Bernoulli variables a,T0,TE,R,S,t. It retains the EC49FUZ and FUQ/FUR author-proof dependencies for composite minimax asymptotics.

## Strengthened theorem

If x is a rational number in (0,1), its reduced denominator is not divisible by 29, and the residue r=x modulo 29 belongs to
\[
\boxed{\mathbb F_{29}\setminus\{1,23\}},
\]
then \(t(x)=\log R(x)/\log S(x)\) is irrational. Thus **27 of 29** 29-integral residue classes yield explicit irrational phases. The resulting set of rational widths is dense in every open real interval of (0,1). The conditional second-order composite minimax risk oscillation and least-favorable-weight accumulation results of the preceding EC49FVA note extend to this larger family for each fixed x, with the same endpoint-only reduction premise and x-dependent error constants.

The omitted classes 1 and 23 are unresolved by this residue-level certificate.

## Exact proof

The preceding note proves
\[
v_{29}(u_E)=-1,\quad
Z_{29}(a)=\{0,20\},\quad
Z_{29}(T_0)=\{1,19\},\quad
Z_{29}(T_E)=\{1,23\},
\]
and \(1<R<S\). Let
\[
v_R=v_{29}(R)=v_{29}(T_0)-v_{29}(u_E)-v_{29}(T_E),
\quad
v_S=v_{29}(b)-v_{29}(a)+v_R,\quad b=1-u_ET_E.
\]

**Case 1: r outside {0,1,19,20,23}.**
The prior theorem gives \(v_R=1,v_S=0\).

**Case 2: r=0 or 20.**
Here \(a\equiv0\pmod{29}\) while \(T_0,T_E\) are units. Hence \(v_{29}(a)\ge1\), \(v_{29}(b)=-1\), and
\[
\boxed{v_R=1,\quad v_S=-v_{29}(a)\le-1}.
\]

**Case 3: r=19.**
Here \(T_0\equiv0\pmod{29}\) while \(T_E\) is a unit.
Put \(k=v_{29}(T_0)\ge1\). Then \(a=1-T_0\) is a unit, \(v_{29}(b)=-1\), and
\[
\boxed{v_R=k+1,\quad v_S=k}.
\]

All such rational widths satisfy \(0<t<1\). If \(t=h/\ell\) were rational in lowest terms, then \(0<h<\ell\) and
\(R^\ell=S^h\), giving
\[
\ell\,v_R=h\,v_S.
\]
Case 1 forces \(\ell=0\). Case 2 equates a positive to a negative valuation. Case 3 gives \(\ell(k+1)=hk\), impossible since \(\ell>h>0\). Thus t is irrational throughout all 27 classes.

For density, fix any nonempty real open subinterval I of (0,1), and choose arbitrarily large denominators d=29m+1. A numerator k of any specified permitted residue class exists in dI when the length of dI exceeds 29. The fractions k/d are eligible, and the argument yields infinitely many distinct widths. Thus each certified residue class itself gives a dense rational family.

The phase and risk corollaries require only the strict probability order \(p_E<a<b<q_0\) and irrationality of t. These hypotheses remain valid. Their geometric-overlap derivation and conditional full-game transfer are the preceding note's proofs, not new native X6 claims.

## Exact examples and reproducibility

Companion checker: EC49FVA_27CLASS_29ADIC_UPGRADE_VERIFY.py, using standard-library Fraction.

| Width x | Residue r | v29(R) | v29(S) |
|---|---:|---:|---:|
| 29/30 | 0 | 1 | -1 |
| 20/59 | 20 | 1 | -1 |
| 19/30 | 19 | 2 | 1 |
| 7/20 | 25 | 1 | 0 |

The exact case split certifies the infinitely many asserted widths; finite computations cross-check arithmetic. No independent mathematical review or formal shared Result is asserted.

Next: classify residue classes 1 and 23 with finer 29-adic digits and independent prime valuation witnesses; seek stronger complete rational-width criteria.
