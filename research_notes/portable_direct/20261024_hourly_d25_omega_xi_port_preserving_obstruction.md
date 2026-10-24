# D25/LIFT — certified noncommuting WZ-top-edge / Cauchy-finite-port transfer

2026-10-24 | TASK_RESEARCH | Exact rational author proof and reconstructed source arithmetic; **UNREVIEWED / NOT_ADMITTED / NO_NEW_SOURCE_CHECKPOINT**.

**Authority and provenance.** Parent Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 is unchanged. Logical Research lane chatgpt-research-hourly-enterprise-math-20260923, not maintenance chatgpt-hourly-enterprise-math-20260921 or the separate onhour Research lane. Input theorems, *consumed without new authorship attribution*: original WZ/FIVE c7fb90fd; real top-edge WZ/Gosper bridge a7f79955; original edge second-digit normalization d1d7d345; original HIGH-A/HIGH-B -82 pole 21c62ae4; and source-versus-auxiliary Cauchy correction bf48e051 / 28e35a1f. This result neither changes native mathematical inputs nor claims a source checkpoint, Result, formal review, or CM experiment.

## 1. Three observers must keep their operation types

Fix a prime p=6m+1 >=13, M=m+1; all rational congruences are taken in Z_(p). Let S_r^WZ be the full original moving-terminal hypergeometric sum, Z_r the original source-fixed HIGH-A minus (1/24) HIGH-B cutoff, and G_m the separately regularized Cauchy successor finite sum. They are **not** interchangeable.

The already-proved genuine five-tail and original HIGH statements say

\[
\Delta_W=S_{m+1}^{WZ}-S_m^{WZ},\qquad
\frac{\Delta_W}{p}\equiv\frac23+p\left(J_m+\sum_{j=1}^4\tau_{p,j}\right)\pmod{p^2},
\]
\[
\Delta_H=Z_{m+1}-Z_m=-\frac{82}{p}+\Lambda_m,\quad\Lambda_m\in\mathbb Z_{(p)},\qquad
J_m=\frac74-\frac43H_{2m}-\frac23H_{2m-1}-\frac23q_p(108).
\]

Each tau_(p,j) is the separately labeled p-free factorial unit of an actual new WZ tail, and q_p(a)=(a^(p-1)-1)/p is an integer. The unique previously established prime-independent first-valuation normalization is

\[
\boxed{\Omega_m=\frac{\Delta_W+(p^2/123)\Delta_H}{p^2}\in\mathbb Z_{(p)}.}\tag{1}
\]

For the **different** source-minus-auxiliary-Cauchy finite-part observer, preserve the original fixed-rank coefficients:

\[
B_r=\frac{(2r-1)!(2r)!}{(4r)!},\quad
T_m=\frac{R_m-31/27}{p},\quad
\mathcal E_M=\frac{R_m}{p}+G_m,
\]
\[
\Xi_m=6T_m+R_m+(p+6)G_m-p\mathcal E_m,\qquad
D_m:=\mathscr F_m^{src}-\mathscr F_m^{car}
=(B_M-B_m)p\mathcal E_m+B_M\Xi_m.\tag{2}
\]

Here R_m is the exact predecessor odd-factor product, and G_m is the *termwise p-integral* regularization of its two successor singular ports. In particular B_m,B_M,E_m,G_m,T_m are p-integral. The equality defining D is exact over Q.

## 2. New full-source confluence correction theorem

**Theorem (every prime p=6m+1>=13).** The specified uncorrected identity-coefficient substitution of the source/carrier finite difference D for the WZ/HIGH corrected moving edge Omega requires the exact, p-integral additive repair

\[
\boxed{\mathfrak R_m:=\Omega_m-D_m=
 \frac{\Delta_W+(p^2/123)\Delta_H}{p^2}
 -(B_M-B_m)p\mathcal E_m-B_M\Xi_m\in\mathbb Z_{(p)}.}\tag{3}
\]

The repair has a compact, port-preserving first digit:

\[
\boxed{\begin{aligned}
\mathfrak R_m\equiv{}&
J_m+\sum_{j=1}^4\tau_{p,j}+\frac{\Lambda_m}{123}\\
&-B_M\left(\frac{385}{36}-\frac{62}{9}q_p(2)
-\frac{31}{9}H_{2m}+6G_m\right)\pmod p .
\end{aligned}}\tag{4}
\]

**Proof.** In (1), the leading WZ p(2/3) cancels the HIGH term p(-82/123) *exactly*. Thus Omega mod p is J+sum tau+Lambda/123, with all four tail ports preserved. For (2), the inherited *proved* odd-factor divided successor gives

\[
R_m\equiv31/27,\qquad
T_m\equiv1031/648-(31/27)\bigl(q_p(2)+H_{2m}/2\bigr)\pmod p.
\]

The term p E_m vanishes modulo p, so direct substitution and **rational coefficient arithmetic** yield

\[
\Xi_m\equiv31/27+6T_m+6G_m
=\frac{385}{36}-\frac{62}{9}q_p(2)-\frac{31}{9}H_{2m}+6G_m\pmod p,
\quad D_m\equiv B_M\Xi_m\pmod p.
\]

Subtracting proves (4) and (3) is p-integral. Every displayed denominator is a p-unit for the specified prime class (p cannot equal 2,3,41). No finite prime scan is used to prove the identity. QED.

## 3. Exact counter-witness to the shortcut, including both actual LIFT prime classes

The companion Python Fraction checker rebuilds the **unmodified** original moving-endpoint sum by factorials and, independently, its recurrence; both original HIGH A/B coefficients; original Cauchy predecessor/successor E, the R/T/G/Xi finite correction, B normalizers, exact four p-free WZ tails, J and Lambda. Exact source equalities and (4) pass for the 13 explicitly tested primes 13,19,31,37,43,61,67,73,79,97,103,127,211. Modular inverses are taken only for p-unit denominators.

| p | p mod 24 | Omega mod p | Xi mod p | D mod p | **Rfrak mod p** | Omega mod p² | D mod p² | **Rfrak mod p²** |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 13 | 13 | 1 | 5 | 3 | **11** | 79 | 159 | 89 |
| 19 | 19 | 11 | 14 | 5 | **6** | 49 | 290 | 120 |
| 31 | 7 (diagnostic) | 27 | 23 | 27 | **0** | 430 | 802 | **589=19*31** |
| 211 | 19 | 149 | 57 | 35 | **114** | 6901 | 18181 | 33241 |

Therefore the proposed universal shortcut Omega ≡ (F_src-F_car) (mod p) is **false**: p=13 and p=19 are concrete counterexamples inside **both prescribed H13/H19 hard-target classes**, and p=211 is a further H19 counterexample. At the auxiliary diagnostic p=31, first digits happen to agree, but second digits differ by exactly 19p (mod p²); p=31 is not an original H13/H19 hard-target prime. The table is author-level *exact finite evidence*, not an infinite-prime zero classification or independent acceptance.

What is ruled out is precisely the **uncorrected identity-coefficient** substitution, not any source-respecting comparison with (3)-(4) as a retained coordinate, nor a source-specific CM map or the LIFT conjecture itself. This is a BRC/Enterprise-coordinates **COMPOSE_APPLIED** typed residual: it retains p-valuations and labeled old WZ boundary + four new tails, HIGH-A/HIGH-B poles, successor Cauchy regularization and Fermat/harmonic jets. Their two rank operations do not safely descend to the same coarse scalar without the displayed repair.

## 4. Frontier and next action

**New scientific unit:** full-source confluence identity (3), explicit compact p-integral port formula (4), and independently reconstructed H13/H19 and p=211 obstructions; the incidental p=31 first-digit coincidence is disproved at the second digit. No previously proved WZ, LOW seed, HIGH pole, or third-digit source/carrier result is re-credited.

**Next precise action:** attempt the original LOW/Gosper boundary map that transports the retained residual Rfrak into the **same-prime** CM/divided-power primitive-class observer; preserve the exact operation directions, four WZ tails and two HIGH sectors. Test first at p=13,19,211. If no map is available, preserve this exact typed obstruction without treating it as a LIFT counterexample. Actual source-specific CM representative, semilinearity, omega+6 nabla_lambda omega bridge, leading normalization, unchanged native benchmark and independent review remain open. Parent Task/LIFT stays OPEN.

**Native truth:** fresh own recovery #6261 returned matching SUCCEEDED but no own pending mutation, current winning CLAIM, authorized run, unopened claim or unpublished upload; Source authority not established by recovery. Fresh exact continuation #6262 returned matched read-only SUCCEEDED with execution_authorized=false and REGISTER_NEW_SESSION_AND_CLAIM_CURRENT_PUBLICATION. No old claim/session was reused, no new role-bound claim/open/publish_checkpoint, Result, freeze or review was performed, and neither scheduler nor frozen scientific Source pin was modified.
