# D25/LIFT — original WZ old-edge third digit through Fermat quotients and one short harmonic range

2026-10-24 | TASK_RESEARCH, portable author proof | **UNREVIEWED / NOT_ADMITTED / NO_NEW_SOURCE_CHECKPOINT**. This note does not claim Source CLAIM/open, CM experiment, Result, independent mathematical acceptance, or completion of the mother task.

**Source and prior inputs.** Mother \(\mathrm{RS\!-\!ENTERPRISE\!-\!BRC\!-\!HALF\!-\!COUPLING\!-\!INERT\!-\!PLUS\!-\!D24\!-\!SECOND\!-\!DIGIT\!-\!LIFT}\), publication \(\mathrm{TP2\!-\!B6F4FC938FF94941C1B7}\). Frozen *scientific* pin: \(\mathtt{c47e13e4aba0e006366f989d6334d443f6333ae3}\), unchanged. This Research lane's logical label is \(\mathtt{chatgpt-research-hourly-enterprise-math-20260923}\), distinct from the maintenance label. Consumed, **not re-credited**: original WZ FIVE and top-edge identity in \(\mathtt{20261024\_hourly\_d25\_original\_top\_edge\_wz\_seam\_bridge.md}\); exact terminal product, \(C(p)\), and its three-range fourth-digit expansion in \(\mathtt{20261024\_hourly\_d25\_wz\_old\_edge\_fourth\_digit\_confluence\_p3.md}\); genuine four tails \(\tau_{p,j}\); original source-fixed HIGH \(-82/p+\Lambda_m\). The separate onhour composite-parameter obstruction is not redone.

## 1. New theorem: a short-range, two-Fermat-quotient third digit

Let \(p=6m+1\ge13\) be prime, \(r=2m=(p-1)/3\). Work in \(\mathbb Z_{(p)}\) and set
\[
a=q_p(2)=\frac{2^{p-1}-1}{p},\quad
b=q_p(3)=\frac{3^{p-1}-1}{p},\quad
H=H_r=\sum_{k=1}^{r}\frac1k,\quad
K=H_r^{(2)}=\sum_{k=1}^{r}\frac1{k^2}.
\]
All four are precise integers or rational numbers, not fitted decimal parameters. Let \(E_0=W_{m,4m+1}g(m,4m+1)\) denote the *actual original WZ old-rank boundary* from FIVE, not the auxiliary fixed-prime HIGH cutoff. Define
\[
\begin{aligned}
A_p&=-\frac14-\frac43a-2b-2H,\\
B_p&=\frac{73}{120}+\frac a2-\frac{3b}{8}
      +2a^2-2ab+\frac74b^2-\frac K3.
\end{aligned}
\tag{1}
\]

**Theorem A (third digit, all stated primes).**
\[
\boxed{\displaystyle
\frac{E_0}{p}\equiv\frac23+pA_p+p^2B_p\pmod{p^3}.}
\tag{2}
\]
Every displayed denominator is a \(p\)-unit. Compared to the inherited three-range harmonic expression, the new formula has only \(H_{(p-1)/3}\), \(H_{(p-1)/3}^{(2)}\), \(q_p(2)\) and \(q_p(3)\). No \(H_{p-2}^{(j)}\), \(H_{2m-1}^{(j)}\), Wilson quotient, unrecorded p-adic constant or replacement WZ endpoint remains.

**Theorem B (Fermat-only second digit).**
\[
\boxed{\displaystyle
\frac{E_0}{p}\equiv
\frac23+p\left(b-\frac43a-\frac14\right)\pmod{p^2}.}
\tag{3}
\]
Hence the exact prime-level exceptional condition for the original old edge to have its second digit vanish is
\[
\frac{E_0}{p}\equiv\frac23\pmod{p^2}
\quad\Longleftrightarrow\quad
12q_p(3)-16q_p(2)-3\equiv0\pmod p.
\tag{4}
\]
The criterion is proved for every stated prime; absence of solutions outside any finite search range is **not** asserted.

## 2. Proof using the source-preserved exact rational edge

Reuse only the inherited exact *original* factorial product (not the Cauchy approximation):
\[
U_m=\frac{2m}{108^{p-1}}
\left(\prod_{k=2}^{r}(1-p/k)\right)^2
\frac{\left(\prod_{j=1}^{p-2}(1+p/j)\right)^2}
{\prod_{j=1}^{r-1}(1+p/j)},\qquad
\frac{E_0}{p}=U_m C(p).
\tag{5}
\]
Here the inherited exact rational \(C(p)\) has
\[
C(p)\equiv
-2+\frac34p-\frac{393}{40}p^2\pmod{p^3}.
\tag{6}
\]
Write \(q=q_p(108)\), \(P_i=H_{p-2}^{(i)}\) and \(\widetilde H_i=H_{r-1}^{(i)}\). Formal \(p\)-adic logarithm of the finite \(1+p\)-unit factors in (5), valid modulo \(p^3\), has
\[
\ell_1=-q-2(H-1)+2P_1-\widetilde H_1,\qquad
\ell_2=\frac{q^2}{2}-(K-1)-P_2+\frac{\widetilde H_2}{2}.
\tag{7}
\]
Consequently \(U_m/(2m)\equiv1+p\ell_1+p^2(\ell_2+\ell_1^2/2)\pmod{p^3}\). Multiplying by (6) and using \(2m=(p-1)/3\) **exactly**, obtains
\[
\frac{E_0}{p}\equiv\frac23+p\theta_0+p^2\theta_1\pmod{p^3},\quad
\theta_0=\frac23\ell_1-\frac{11}{12},\quad
\theta_1=\frac{141}{40}-\frac{11}{12}\ell_1+
\frac23\ell_2+\frac13\ell_1^2.
\tag{8}
\]
These are the inherited edge operations, recorded here only to show the valid reduction.

For every prime \(p\ge5\), the elementary identities
\[
H_{p-1}\equiv0\pmod{p^2},\qquad
H_{p-1}^{(2)}\equiv0\pmod p
\]
follow by pairing \(1/k\) with \(1/(p-k)\) and using the finite-field square-sum. Thus
\[
P_1\equiv1+p\pmod{p^2},\quad
P_2\equiv-1\pmod p,\quad
1/r=\frac3{p-1}\equiv-3-3p\pmod{p^2},\quad
1/r^2\equiv9\pmod p.
\]
Since \(\widetilde H_1=H-1/r\) and \(\widetilde H_2=K-1/r^2\),
\[
\boxed{\ell_1\equiv1-q-3H-p\pmod{p^2}},\qquad
\boxed{\ell_2\equiv\frac{q^2-K-5}{2}\pmod p}.
\tag{9}
\]
The exact integer identity
\[
108^{p-1}=(1+pa)^2(1+pb)^3
\]
implies
\[
q\equiv2a+3b+p(a^2+6ab+3b^2)\pmod{p^2}.
\tag{10}
\]

For completeness, the short-harmonic Fermat reduction needed for the coefficient of \(p^2\) is elementary. For \(k=1,\ldots,p-1\), let \(u_k=3k-p\lfloor3k/p\rfloor\), a permutation of \(1,\ldots,p-1\). The product
\[
\prod_{k=1}^{p-1}\left(1-\frac{p\lfloor3k/p\rfloor}{3k}\right)
=3^{-(p-1)}
\]
gives \(q_p(3)\equiv\frac13\sum_{k=1}^{p-1}\lfloor3k/p\rfloor/k\pmod p\). As \(p=3r+1\), the sum is \(2H_{p-1}-H_r-H_{2r}\equiv-2H_r\pmod p\), using reflection \(H_{2r}\equiv H_r\pmod p\). Therefore
\[
\boxed{H\equiv-\frac32b\pmod p}.
\tag{11}
\]
Using (9)--(11) in (8), first obtain
\[
\theta_0\equiv-\frac14-\frac43a-2b-2H
-\frac{2p}{3}(1+a^2+6ab+3b^2)\pmod{p^2}.
\]
Also, setting \(\ell_1\equiv1-2a+\frac32b\) and
\(\ell_2\equiv((2a+3b)^2-K-5)/2\pmod p\), obtain
\[
\theta_1\equiv-\frac K3+\frac83a^2+2ab+\frac a2+
\frac{15}{4}b^2-\frac{3b}{8}+\frac{51}{40}\pmod p.
\]
Subtracting \(\frac23(1+a^2+6ab+3b^2)\) from this expression yields exactly \(B_p\) in (1), proving (2). Finally \(A_p\equiv-\frac14-\frac43a+b\pmod p\) by (11), proving (3)--(4). No finite-prime experiment is used as a universal proof. QED.

## 3. Retained original five-port and HIGH observer corollaries

Let \(E_j=W_{m+1,4m+j}\), \(j=1,\ldots,4\), denote the four authentic new-rank WZ tails. The inherited theorem gives \(E_j/p^2\equiv\tau_{p,j}\pmod p\), including their individual source labels. The *original* moving-rank FIVE identity immediately gives the **new reduced formula**
\[
\boxed{\frac{S_{m+1}-S_m}{p}\equiv\frac23+
p\left(b-\frac43a-\frac14+\sum_{j=1}^4\tau_{p,j}\right)\pmod{p^2}.}
\tag{12}
\]
For the distinct fixed-prime original-HIGH source \(\Delta_H=-82/p+\Lambda_m\), the previously defined source-faithful normalized bridge
\(\Omega_m=(S_{m+1}-S_m+(p^2/123)\Delta_H)/p^2\)
therefore satisfies
\[
\boxed{\Omega_m\equiv b-\frac43a-\frac14+
\sum_{j=1}^4\tau_{p,j}+\frac{\Lambda_m}{123}\pmod p.}
\tag{13}
\]
Equation (13) is a new **Fermat-only old-port simplification** of an existing bridge, *not* an identity with an auxiliary Cauchy carrier and *not* the original same-class CM/divided-power map. The sum symbol preserves four separately named, already available tails; no future port-sensitive operation may silently quotient them.

**BRC/Enterprise coordinates: COMPOSE_APPLIED.** Use the labeled signed-rational, valuation/unit, old-edge/four-tail/HIGH-A/HIGH-B carrier. Equations (2) and (13) are observation maps applied only after retaining the provenance and p-adic jets; a total-only readout is not a safe replacement for all future operations. This is external p-adic arithmetic, not a claim about native X6 physical dynamics or a modification of P000.

## 4. Exact author checks, finite search, and limits

The original \(E_0\) was independently reconstructed as \(W_{m,4m+1}g(m,4m+1)\), using the source factorial \(W\) and its exact \(g\) at the boundary; it was checked to equal the independently evaluated finite product \(pU_mC(p)\) **as a rational identity** for each tested \(p\). In each case the difference between that original fraction \(E_0/p\) and (2) has p-adic order at least three (denominator invertibility checked). The 13 checked primes were \(13,19,31,37,43,61,67,73,79,97,103,127,211\). Exact residues include:

| \(p\) | \(a\bmod p\) | \(b\bmod p\) | \(A_p\bmod p\) | \(B_p\bmod p\) | \(E_0/p\bmod p^3\) |
|---:|---:|---:|---:|---:|---:|
| 13 | 3 | 8 | 7 | 4 | 1669 |
| 19 | 3 | 18 | 9 | 2 | 3902 |
| 31 | 6 | 17 | 1 | 30 | 21494 |
| 211 | 109 | 18 | 101 | 188 | 6313613 |

An additional **finite computation**, distinct from the universal proof, sieved all 4,784 primes \(7\le p\le100000\) with \(p\equiv1\pmod6\); the exact criterion \(12b-16a-3\pmod p\) had no zero in that bounded set (including 2,398 primes in the original \(13/19\bmod24\) classes). Here \(a\bmod p\) and \(b\bmod p\) were computed by modular exponentiation modulo \(p^2\): \(q_p(c)\bmod p=((c^{p-1}\bmod p^2)-1)/p\). This is **not a theorem of non-vanishing for unbounded primes**. The underlying all-prime identities are algebraic and independent of this sieve.

The original native CM/divided-power class representative, map direction, semilinearity, leading normalization and same-class \(\kappa\) comparison are still unknown from the published materials. The Source task's original \(p\equiv13,19\pmod{24}\) LIFT target stays open. In particular, this Fermat reduction is a new necessary arithmetic interface to respect in any proposed WZ/CM bridge, but cannot be substituted for its absent source-native class map.

## 5. Recovery and next exact unit

**Completed here:** formula (2) at the third digit, short-range reduction (11), the exact Fermat exceptional criterion (4), and source-labeled observer consequences (12)--(13). All are author-level proofs and checks, not independent review; previously derived four-range coefficients and WZ/FIVE are explicitly reused rather than claimed new. Highest immutable *scientific* source remains \(\mathtt{c47e13e4aba0e006366f989d6334d443f6333ae3}\).

**Next minimal unit:** inspect the current Source-authenticated same-prime CM/divided-power primitive class and determine whether its ordinary \(\omega+6\nabla_\lambda\omega\) first jet produces the specific short-range Fermat combination in (12)--(13), with the four genuine WZ tails and original LOW/HIGH seam labels conserved. If that map cannot yet be sourced, an independent portable arithmetic unit is to determine a prime-only formula for the *tail-labeled* \(\sum_j\tau_{p,j}\) modulo \(p\), without collapsing the four original ports or upgrading a finite fit to a theorem.

**Control:** direct gateway read-only exact continuation this turn returned \(\mathtt{CONTROL_QUOTA}\), not \(\mathtt{NO_DISPATCH}\); the prior own canonical dispatch \(\mathtt{rsch20-dispatch-a11-20261024T0821Z}\) (#6264) has terminal \(\mathtt{FAILED: TimeoutExpired}\). A fresh own \(\mathtt{recovery_status}\) (#6265) has matched \(\mathtt{SUCCEEDED}\) but \(\mathtt{source_authority_verified=false}\), no own live winning claim/run, and neutral historic staging only. Exact continuation request #6266 is read-only and must be consumed by its final receipt. There is no native task-run authorization or Source checkpoint for this proof. Control support path: enterprise-math #1558. Preserve stable Research lane ID, no maintenance impersonation, no session reset or claim replay. No scheduler or notification changes.
