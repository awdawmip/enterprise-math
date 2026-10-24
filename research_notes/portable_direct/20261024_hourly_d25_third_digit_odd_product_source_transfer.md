# D25/LIFT — third-digit odd-factor certificate and source-fixed successor transfer

2026-10-24 | TASK_RESEARCH | Author-side exact rational derivation, finite p-adic proof and 79/12-instance exact verification. **UNREVIEWED / NOT_ADMITTED / NO_NEW_SOURCE_CHECKPOINT**. Portable mathematical evidence only: no winning native CLAIM, authorized run, Result, freeze or independent review is asserted.

**Provenance and scope.** Mother task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen *scientific* Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged. This author's logical Research lane is chatgpt-research-hourly-enterprise-math-20260923, distinct from CONTROL_PLANE_MAINTENANCE chatgpt-hourly-enterprise-math-20260921 and the independent onhour Research lane. This unit consumes, without re-crediting, the exact source/carrier bridge and the modulo-p² transfer from 20261024_hourly_d25_divided_successor_harmonic_p2_source_transfer.md at bf48e0514f0e7eb54b8d5b36dd142786b6a8bc43. The onhour WZ five-tail equality (c7fb90fd7ec451a954b553b963dd85d4ec99fc96) and latest p³ upper-half five-port transport (7724e73f2d15c92ce98520e6a55b8231d737fa03) are other-author inputs; their proof/seed work is not repeated here.

## 1. Exact inherited rational objects

Fix a prime p=6m+1>=13, m>=2. All congruences are in Z_(p), with rational denominators invertible modulo the stated p-power. Write

\[
H=H_{2m},\qquad H_2=H_{2m}^{(2)},\qquad H_3=H_{2m}^{(3)},\qquad q=q_p(2)=\frac{2^{p-1}-1}{p}\in\mathbb Z.
\]

The inherited **exact** successor singular residue, with original source coefficients unchanged, is

\[
R_m=C(p)\,\mathcal P_m,\qquad
\mathcal P_m=2^{-(p-1)}\prod_{j=0}^{2m-1}\left(1-\frac p{2j+1}\right),
\]
\[
C(p)=\frac{18p^4-59p^3+132p^2+633p+248}
{36(p-3)(p-1)(p+2)(2p+1)}.
\tag{1}
\]

The earlier author theorem established R_m≡c_0=31/27 (mod p); hence T_m=(R_m-c_0)/p is a genuinely p-integral rational number. It also proved exactly

\[
\mathcal E_{m+1}=R_m/p+S_m,\quad S_m\in\mathbb Z_{(p)},\quad
\Xi_m=6T_m+R_m+(p+6)S_m-p\mathcal E_m,
\tag{2}
\]

and, using original B_r=(2r-1)!(2r)!/(4r)!,

\[
\mathscr F_m^{src}-\mathscr F_m^{car}
=(B_{m+1}-B_m)p\mathcal E_m+B_{m+1}\Xi_m.
\tag{3}
\]

Here S_m is the explicitly regularized two-seam finite sum of the inherited source, **not** the onhour WZ endpoint S_r with the same letter. All three equations above are inherited, not newly proved units.

## 2. New lemma: cubic odd-product expansion without a Wilson/Wolstenholme quotient

Set

\[
b=\frac{H^2}{8}-\frac{3H_2}{8},\qquad
c=-\frac{H^3}{48}+\frac{3HH_2}{16}-\frac{7H_3}{24}.
\]

**Theorem A.** For every prime p=6m+1>=13 the exact product in (1) has the following expansion at one additional p-adic digit:

\[
\boxed{\mathcal P_m\equiv1+pa_1+p^2a_2+p^3a_3\pmod {p^4},}
\tag{4}
\]
\[
\begin{aligned}
a_1&=-q-H/2,\\
a_2&=q^2+qH/2+b,\\
a_3&=-q^3-q^2H/2-qb+c.
\end{aligned}
\tag{5}
\]

In particular the cubic coefficient needs only H, H_2, H_3 and the *integer* Fermat quotient q: an auxiliary Wolstenholme quotient cancels and is **not** silently set to zero.

**Proof.** Write J_s=Σ_{j=0}^{2m-1}(2j+1)^{-s} and G_s=H_{p-1}^{(s)}. Reflection over p-1=6m, with p-unit denominators, yields

\[
\begin{aligned}
J_1&\equiv H/2+pH_2+p^2H_3+G_1\pmod {p^3},\\
J_2&\equiv-5H_2/4-2pH_3+G_2\pmod {p^2},\\
J_3&\equiv7H_3/8\pmod p.
\end{aligned}
\tag{6}
\]

For p>=13, Wolstenholme gives G_1∈p² Z_(p), and the finite-field power-sum rule gives G_3≡0 (mod p). More precisely, permuting j↦p-j in G_1 and expanding to the indicated order proves

\[
2G_1\equiv-pG_2-p^2G_3\pmod{p^3},
\quad\text{so}\quad G_1\equiv-\frac p2G_2\pmod {p^3}.
\tag{7}
\]

In the finite elementary-symmetric expansion

\[
\prod_j(1-p/(2j+1))
\equiv1-pJ_1+\frac{p^2}{2}(J_1^2-J_2)
-\frac{p^3}{6}(J_1^3-3J_1J_2+2J_3)\pmod{p^4},
\]

the only apparent full-range harmonic contribution at order p³ is
\(-pG_1-p^2G_2/2\equiv0\pmod{p^4}\) by (7). Direct substitution of (6), retaining ordinary integer coefficients and all third-order cross terms, gives

\[
\prod_j(1-p/(2j+1))\equiv
1-\frac{pH}{2}+p^2b+p^3c\pmod{p^4}.
\tag{8}
\]

Finally, 2^{p-1}=1+pq exactly, so its reciprocal is
\(1-pq+p^2q^2-p^3q^3\pmod{p^4}\).
Multiplying this by (8) proves (4)-(5). QED.

**BRC observer:** preserve the signed rational multiplicative factors, individual p-valuations, harmonic jets and Fermat quotient through the third-digit observer; only then quotient to the declared scalar modulo p⁴. This is an arithmetic interface, not an X6 physical experiment.

## 3. New third-digit theorem for the source-specific divided residue

Taylor expansion of the *exact* rational prefactor C(p) at formal p=0 (legitimate since its constant denominator is a p-unit for p>=13) yields

\[
C(p)\equiv c_0+c_1p+c_2p^2+c_3p^3\pmod{p^4}
\]
with

\[
c_0=\frac{31}{27},\quad c_1=\frac{1031}{648},\quad
c_2=\frac{4087}{3888},\quad c_3=\frac{52643}{23328}.
\tag{9}
\]

**Theorem B.** Put

\[
t_0=c_1+c_0a_1,\qquad
t_1=c_2+c_1a_1+c_0a_2,\qquad
\boxed{t_2=c_3+c_2a_1+c_1a_2+c_0a_3}.
\tag{10}
\]

Then, for *every* target prime p=6m+1>=13,

\[
\boxed{T_m=\frac{R_m-31/27}{p}
\equiv t_0+pt_1+p^2t_2\pmod{p^3}.}
\tag{11}
\]

Proof: multiply the exact product (1) using (4) and (9) to obtain
\(R_m\equiv c_0+pt_0+p^2t_1+p^3t_2\pmod{p^4}\).
The constant term difference is p-divisible and the rational denominator is a p-unit, so division by p is valid. QED.

This strengthens the **prior** modulo-p² statement by exactly one p-adic digit without recomputing already proved source ports. No claim about the original D25 full LIFT obstruction is inferred.

## 4. New third-digit, pole-free source/carrier observer transfer

Retain the predecessor's exact finite, source-labelled S_m and rank-m \(\mathcal E_m\). They are p-integral for all the stated target primes (the two successor singular ports have been removed *at the summand level*). Substitute (11) into (2)-(3).

**Theorem C.** The following two full-source formulas are valid modulo p³:

\[
\boxed{\begin{aligned}
\Xi_m\equiv{}&
c_0+6t_0+6S_m\\
&+p(t_0+6t_1+S_m-\mathcal E_m)
+p^2(t_1+6t_2)\pmod{p^3},
\end{aligned}}
\tag{12}
\]

\[
\boxed{\begin{aligned}
\mathscr F_m^{src}-\mathscr F_m^{car}\equiv{}&
B_{m+1}\big[
c_0+6t_0+6S_m\\
&\quad+p(t_0+6t_1+S_m)
+p^2(t_1+6t_2)
\big]-pB_m\mathcal E_m
\pmod{p^3}.
\end{aligned}}
\tag{13}
\]

The derivation is algebraic substitution into the **exact rational** inherited bridges, not an assertion of p-adic cancellation among undefined \(1/p\) terms. In (13) the two rank-m source corrections combine exactly to \(-pB_m\mathcal E_m\). Every term shown is individually p-integral. The finite sum S_m is evaluated at p³ precision and E_m at p² precision; neither is discarded. This is an operational third-digit interface for future full-endpoint/WZ comparisons, not the completion of those comparisons.

## 5. Exact rational checks and discriminating residues

An author-only independent Fraction calculation rebuilt C, the entire odd product, H/H_2/H_3, and the exact finite source definitions
\(D_r=2^r(2r)!/[r!(r-1)!]\),
\(h_r(t)=r!(t-1)!/[2^t(t+r)!]\),
\(k_s^B=(2-3s)(6s+1)/[3s(3s+1)]\),
\(K_r(s)=1/[27s(r+s+1/6)]+1/[18(s+1/3)(r+s+1/2)]-k_s^B/(12r)\),
\(\mathcal E_r=D_r\sum_{s=1}^{2r-1}h_r(r+s)K_r(s)\).
The two exceptional successor summands s=2m-1 and s=2m were regularized exactly as in the inherited source; the complete source \(S_m\), \(R_m\), \(\mathcal E_m\), \(\Xi_m\), and both B's were independently reconstructed before modular reduction.

Theorem B passed **79/79** target primes 13<=p<1000, p≡1 (mod 6), using exact rational arithmetic and modular inversion of p-unit denominators. The stronger coupled assertions (12)-(13), including their *exact predecessor rational identities*, passed all **12** primes
13,19,31,37,43,61,67,73,79,97,103,211.
These are reproducible arithmetic regressions, **not** independent mathematical review; generality rests on the proof above.

| p | T_m mod p³ | Xi_m mod p³ | (F_src−F_car) mod p³ |
|---:|---:|---:|---:|
| 13 | 1066 | 473 | 1511 |
| 19 | 1904 | 4992 | 290 |
| 31 | 18370 | 14717 | 14256 |
| 37 | 47746 | 46910 | 7323 |
| 43 | 4076 | 15529 | 64332 |
| 61 | 172026 | 74736 | 44837 |
| 67 | 243264 | 235170 | 108540 |
| 73 | 78401 | 32155 | 83026 |
| 79 | 348363 | 328318 | 176547 |
| 97 | 879550 | 504553 | 275801 |
| 103 | 242601 | 248362 | 507961 |
| 211 | 884078 | 3083400 | 151744 |

In particular the p=31 and p=211 third-digit source-vs-carrier discrepancies remain nonzero. This cannot be erased by the p=31 successor pole exception or the p=211 auxiliary seam rank exception.

## 6. Highest valid frontier and next executable question

**New completed author units:** cubic odd-product cancellation (A), the full p³ divided successor (B), and third-digit source-fixed finite-part transfer (C). Their provenance is this file; not yet a registered Source Task contribution. **Already completed and not re-credited:** preceding p² source transfer, all prior seam/pole and LOW jets, other lane's original all-m five-tail WZ and later upper-half p³ WZ transport, accepted D24 Result. Frozen input pin remains unchanged.

**Next independent scientific unit:** compare the *unchanged original full source* terminal observable with the distinct onhour WZ p³ five-tail observer at p=31 and p=211, using (13) as a third-digit correction rather than equating an auxiliary Cauchy rank-cutoff to the original hypergeometric endpoint. Derive the precise boundary map, or give a rigorous obstruction to such a map. Do not take over the other Researcher's unfinished low-seed/CM work. There is no proved equivalence yet.

**Native duties remain:** same-class CM/divided-power primitive representative, map direction and semilinearity, ordinary omega+6 nabla_lambda omega comparison, exact leading normalization, same-class kappa bridge, the original unmodified native benchmark, and formal Source/Driver admission. D25/LIFT mother objective remains OPEN. Source's last matched continuation (ordinary Chat bridge #6256, request rsch20-continuation-r11-20261024-d25) completed read-only with execution_authorized=false and route REGISTER_NEW_SESSION_AND_CLAIM_CURRENT_PUBLICATION; last matched recovery (#6255) showed ACTIVE service session but no own winning claim/run/pending upload. This note performs no session transition, claim, publication checkpoint, role review or scheduler change. Existing control/support ownership stays with enterprise-math issue #1558, and future role-bound operations require current exact authority.
