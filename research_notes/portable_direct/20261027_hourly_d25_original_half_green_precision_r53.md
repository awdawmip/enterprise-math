# D25/LIFT R53 — Original R23 low-half observer cancels every R51 exceptional Green pole

Date: 2026-10-27 Asia/Hong_Kong. Portable author-side TASK_RESEARCH for logical conversation chatgpt-research-hourly-enterprise-math-20260923. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; parent D25/LIFT/JT2 OPEN; frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged. AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Exact unchanged-input task and statement

R23 expresses the open original supercongruence as

$$
W_p-S_p\equiv L_p+p^2 U_p\pmod{p^3},\qquad
L_p:=\sum_{k=0}^{(p-1)/2}(w_k-s_k),
$$

where \(w_k,s_k\) are the original distinct factorial sources and \(U_p\) is R23's independently labelled W-high sum. The displayed *reduction* is already proved in R23; the obligation \(L_p\equiv-p^2U_p\pmod{p^3}\) remains OPEN.

For prime \(p\ge13,\ p\equiv1\pmod6\), let \(N=\lfloor(3p-1)/4\rfloor+1\). Apply R50's two-endpoint Green identity to the **actual** low-half observer \(c_k=1\) for \(0\le k\le(p-1)/2\), and \(c_k=0\) otherwise. Keep two source responses

$$ L_W=\sum_{k=0}^{(p-1)/2} w_k,\qquad
L_S=\sum_{k=0}^{(p-1)/2} s_k,\qquad L_p=L_W-L_S.
$$

The Green coefficients \(C_N^{\mathrm{half}},C_{N+1}^{\mathrm{half}}\) are uniquely specified by the exact R52 Cramer formulas with this actual \((L_W,L_S)\).

**R53 theorem.** For *every* target prime as above,

$$
\boxed{v_p(C_N^{\mathrm{half}})\ge-3,\qquad
v_p(C_{N+1}^{\mathrm{half}})\ge-3.}
$$

Moreover at each \(p=139,199,277\), both valuations are **exactly \(-3\)**. Thus the genuine R23 low-half observer never incurs R51's fourth-order endpoint poles, even though the simpler isolated \(d_1\) observer has two fourth-order poles at those three primes.

## Complete proof of the exceptional case

R51 already proves that \(v_p(D_N)=6\) except at precisely \(E=\{139,199,277\}\), where \(v_p(D_N)=7\). At every other target p, all low-half original coefficients \(w_k,s_k\) are p-integral (since \(k<p\), their factorial denominators and bases are units). Hence the two R52 Cramer numerators are divisible by \(p^3\), yielding both endpoint coefficients in \(p^{-3}\mathbb Z_{(p)}\). This establishes the theorem off E without any assumption on the still-open supercongruence.

The set E has exactly three elements. Direct exact factorial rational modular arithmetic therefore supplies a **complete finite exceptional-prime certificate**, not a sample-based universal extrapolation:

| p | N | L_W/p mod p | L_S/p mod p | (w_N/p³,s_N/p³) mod p | (p³ C_N,p³ C_{N+1}) mod p |
|---:|---:|---:|---:|---:|---:|
| 139 | 105 | 1 | 1 | (66,105) | (138,110) |
| 199 | 150 | 1 | 1 | (138,68) | (81,141) |
| 277 | 208 | 1 | 1 | (251,224) | (227,230) |

For each of the three primes, the independently calculated exact sums obey
\(L_W\equiv L_S\equiv p\pmod{p^2}\). This is asserted and checked **for the three displayed primes only**, not assumed for every prime.

Write \(\bar U=w_N/p^3\bmod p,\ \bar V=s_N/p^3\bmod p,\ t=a_N=b_N\bmod p,\ \delta=D_N/p^7\bmod p\); R52 proves \(\delta\) is a unit. Since both response sums are p times units, the fourth-order pole functional \(T_p(c)=L_W\bar V-L_S\bar U\pmod p\) vanishes. The leading possible third-order polar residues are instead

$$
\boxed{
p^3C_{N+1}^{\mathrm{half}}\equiv
\frac{\bar V-\bar U}{\delta},\qquad
p^3C_N^{\mathrm{half}}\equiv
-t\frac{\bar V-\bar U}{\delta}\pmod p.
}
$$

The three values \(\bar V-\bar U\) are \(39,129,250\), respectively, all nonzero. Therefore both coefficients have valuation exactly \(-3\). The last table column evaluates the displayed formulas and was independently checked from exact Cramer rational coefficients. This exhausts all possible resonant primes, proving the universal bound. QED.

## Exact evidence and precision meaning

Companion Python 3 standard-library checker uses the immutable R51 source formulas and calculates the true original low-half sums and Green coefficients with rational arithmetic. It checked all 44 target primes \(13\le p\le500\), every Cramer equality, and the **complete finite E** unit/residue table. Result: PASS. The all-prime theorem is supported by the R51 algebraic resonance classification plus these three exhaustive finite checks, not by generalizing the 44-prime sample.

With independently perturbed original high endpoints, recovering \(L_p\bmod p^t\) from the exact low-half Green coefficients is guaranteed by retaining each endpoint through \(p^{t+3}\) for every target p. For \(t=3\) this gives a **uniform p^6 requirement**; its worst-case sharpness is witnessed at p=139,199,277. This is a precision bound for a declared reconstruction procedure, not a proof of \(L_p\equiv-p^2U_p\pmod{p^3}\), and not permission to delete source provenance.

BRC COMPOSE_APPLIED to original W/S source labels, p-adic valuations, rank and future observer. The safe quotient is observer-specific; X6 native dimensions/P000/ACTIVE worldview remain fixed.

**Frontier:** R51 exceptional Green poles, R52 rank-one safe-observer criterion, R53 proof that the *genuine unchanged* R23 low-half observer lies in that safe class at all exceptional primes. **Do not redo:** R23 proved half-tail reduction, R47–R50 recurrence and Green, or R51/R52 certificates as fresh discoveries.

**Next precise task:** investigate the actual p²-divided difference \(L_p/p^2\) and R23 W-high term \(U_p\) with R36's exact integral PF Green inverse, keeping the two different Green source carriers separate until a lawful intertwiner is explicitly proved. Start p=13,19,181,373 with original finite endpoint and positive-infinity labels. The unchanged-input cross-rank WZ cancellation, six z=2 Hasse J/E ports, original H0/B0, [X]U mod p², eta/kappa, native p=373 experiment and independent Driver review remain OPEN.

This GitHub note/checker is durable *portable* author evidence, not a service CLAIM/open/native Source checkpoint/Result or Research-Activity semantic registration. Previous session/request/staging and control Issue #1558 remain retained for lawful recovery.
