# D25 / W216 — all-prime degree-filtered p-block transfer

Date: 2026-11-10 Asia/Hong_Kong. Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; frozen scientific Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3`.

**Classification:** AUTHOR_SIDE / EXACT PROOF (p-block interpolation) / FINITE EXACT COMPUTATION (Frobenius defect) / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0_B0. Scientific input pin is unchanged. No Source native CLAIM, run, Result or review is inferred.

## 1. Original observer and precise question

Put
[
A_k=rac{inom{2k}{k}^2inom{3k}{k}}{216^k}=rac{(2k)!(3k)!}{(k!)^5,216^k},qquad
W_n=sum_{k=0}^{n-1}(6k+1)A_k.
]
These are the original signed W216 coefficients/weights. Prior author work proved the terminal prime-power boundary and reported a finite-only Dwork-style conjecture for
(W_{p^r}-chi_p pW_{p^{r-1}}), where (chi_p=1) for (pequiv1pmod3) and (-1) otherwise. This unit asks how to compute and analyze (W_{p^2}) with a bounded block operator, rather than redoing the prior terminal lemma.

## 2. NEW theorem: all-prime p-block polynomial and p-adic degree filtration

**Theorem.** Let (pge5) be prime, (1le mle p-1). For (age0) define the exact rational p-local quantity
[
B_p(a)=sum_{b=0}^{p-1}(6(pa+b)+1)A_{pa+b},qquad
C_p(a)=B_p(a)/A_a.
]
There is a polynomial (P_{p,m}(X)=sum_{d=0}^{m-1}h_dX^d) over (mathbb Z/p^mmathbb Z) satisfying
[
C_p(a)equiv P_{p,m}(a)pmod{p^m}quad	ext{for every nonnegative integer }a,
qquad h_din p^d(mathbb Z/p^mmathbb Z).
]
Equivalently, with Newton differences (q_j=(Delta^j C_p)(0)mod p^m),
[
oxed{C_p(a)equivsum_{j=0}^{m-1}q_jinom ajpmod{p^m},quad q_jequiv0pmod{p^j}.}
]
For (j<m<p), (j!) is a p-adic unit, so the Newton and monomial bases are equivalent. The result is a *global congruence in the block index a*, not just interpolation at the first m anchors.

**Proof.** In (mathbb Z_p[X]/p^m), let (mathcal F_m) be the coefficient-filtered subring consisting of polynomial classes (sum_{d<m}h_dX^d) with (v_p(h_d)ge d). This subring is closed under products and under inverses of elements whose constant term is a p-unit.

For nonnegative integer (x), write
[
F(x)=prod_{u=0}^{x-1}prod_{j=1}^{p-1}(1+up/j).
]
In the p-adic unit group, modulo (p^m),
[
log F(x)=sum_{t=1}^{m-1}rac{(-1)^{t-1}p^t}{t}
H_{p-1}^{(t)}sum_{u=0}^{x-1}u^t .
]
For (tle m-1le p-2), (H_{p-1}^{(t)}=sum_{j=1}^{p-1}j^{-t}equiv0pmod p). Also (sum_{u<x}u^t) is a polynomial in x of degree at most (t+1<p), with p-unit denominators (e.g. the finite-difference formula). Thus every coefficient of (X^d) in the t-th logarithmic summand has p-valuation at least (t+1ge d). Hence (log Finmathcal F_m); p-adic exponential preserves this filtration, and (Finmathcal F_m), with unit constant. (The required finite exponential coefficients have p-unit factorials in this range.)

The exact factorial block identity
[
rac{inom{Up}{Vp}}{inom UV}=rac{F(U)}{F(V)F(U-V)}
]
then shows that
[
R_p(a):=rac{A_{pa}}{A_a}
=(216^{1-p})^a
left(rac{inom{2pa}{pa}}{inom{2a}{a}}ight)^2
rac{inom{3pa}{pa}}{inom{3a}{a}}inmathcal F_m .
]
Indeed (216^{1-p}in1+pmathbb Z_p), whose integer powers are filtered polynomials via their binomial expansion to degree (m-1).

For (0le b<p), use the **exact** ratio
[
rac{A_{pa+b}}{A_a}
=R_p(a)A_b
rac{prod_{j=1}^{2b}(1+2pa/j),
      prod_{j=1}^{3b}(1+3pa/j)}
     {prod_{j=1}^{b}(1+pa/j)^5}.
]
Since (b<p), all denominator factors have p-unit j. The numerator contains precisely
(
u_b=lfloor 2b/pfloor+lfloor3b/pfloor=v_p(A_b))
factors with p dividing j; these yield ordinary linear polynomials in a whose coefficients need not be p-small. Their degree is at most (
u_b); multiplication by the actual (p^{
u_b})-divisibility of (A_b) restores the degree filtration. All remaining factors expand with coefficients divisible by (p^{deg}). Thus each individual normalized summand (A_{pa+b}/A_a) lies in (mathcal F_m), as does its signed original weight (6pa+6b+1). Finite summation proves (C_pinmathcal F_m).

Finally, for an integer polynomial of degree less than m, the Newton difference (Delta^jP(0)=sum_{dge j}h_d j!,S(d,j)) is divisible by (p^j), and Newton interpolation holds for *all* integer inputs. This proves the boxed formula. QED.

## 3. Exact moment reconstruction; computational consequence

Partition the original signed sum into p consecutive blocks:
[
W_{p^2}=sum_{a=0}^{p-1}B_p(a)=sum_{a=0}^{p-1}A_aC_p(a).
]
Define the retained BRC valuation/observer moments
[
M_j=sum_{a=0}^{p-1}A_ainom aj,qquad 0le j<m.
]
The theorem gives the rigorous **exact modular transfer**:
[
oxed{W_{p^2}equivsum_{j=0}^{m-1}q_jM_jpmod{p^m}.}
]
Compute the first m blocks (B_p(0),ldots,B_p(m-1)) and the m initial (A_j); use exact p-local division, not inversion of a nonunit, to obtain (C_p(j)), then take forward differences. Because (v_p(A_j)le3) for (j<p), modulus (p^{m+3}) suffices for the anchor numerator/denominator reconstruction. Accumulate the m moments in one pass over (a<p). Complexity is (O(mp)) p-adic modular ring operations and O(m) auxiliary registers at fixed m (bit complexity additionally depends on (log(p^m))), compared with (O(p^2)) original summands. This is not a lower bound or a complexity claim for computing a native H0/B0 object.

For target p=13,19 (mod 24), precision m=7 gives a *sextic* block transfer sufficient to test the unproved r=2 Frobenius-defect conjecture modulo (p^7) while retaining the signed weight and digit-carry structure.

## 4. Deterministic finite checks and discrimination

The accompanying reproducible exact Python checker uses (i) factorial-ratio p-unit coefficient streaming, (ii) the independently complete original (p^2)-term sum as a cross-check, and (iii) finite differences/moments. Eight r=2 checks (p=13,19,37,43,73,109,373,379) produced exact equality between compressed and uncompressed (W_{p^2}mod p^7). They also match the **finite-only** proposal
[
rac{W_{p^2}-chi_p pW_p}{p^6}equiv
rac{W_p-chi_pp}{p^3}pmod p
]
with the right side interpreted only where the already checked base congruence holds. No all-prime Frobenius defect theorem is asserted.

| p | p mod 24 | W_(p²) mod p⁷ | base c_p; observed defect /p⁶ |
|---:|---:|---:|---:|
| 13 | 13 | 37386518 | 9 |
| 19 | 19 | 434881538 | 12 |
| 37 | 13 | 39492321961 | 19 |
| 43 | 19 | 238218636728 | 19 |
| 73 | 1 | 9927173111699 | 46 |
| 109 | 13 | 144119659229661 | 86 |
| 373 | 13 | 660904927112870125 | 228 |
| 379 | 19 | 1122276622230271689 | 65 |

Independent coefficientwise checks on p=5,7,11,13,19,31,37,73,373 and m≤6, plus m=7 where p≥11, found (Delta^m C_p(a)equiv0pmod{p^m}) for the full tested a-range, consistent with the proved global filtration. Finite checks support the implementation, not the theorem's proof.

The BRC reuse is concrete: preserve the original index pair (a,b), the valuation (
u_b), signed weight (6(pa+b)+1), and the full Newton coefficient vector through the declared future moment projection. For this one scalar (W_{p^2}) the moments (M_j) form a proven sufficient projection modulo (p^m); they are not automatically a sufficient state for native Frobenius, rank, kappa or arbitrary later observers.

## 5. Source firewall, unsettled objective and continuation

The frozen D25 mother target remains the *original* (Delta_p-R_pequiv0pmod p) at both p≡13,19 mod24, with full original sign/cutoff/Frobenius ports and existing accepted UR input. The newly proved p-block transfer is a portable finite-coefficient tool, not a direct all-prime proof of this target. The experimental Dwork-style defect still has only exact finite witnesses.

Native H0/B0 same-original-class p=373 divided-power ([X]Umod139129), rank, semilinear direction and normalization eta, signed odd branch, kappa, Delta-R, independent reproduction remain **NOT_RUN/PENDING_OWNER**, tracked by existing support Issue #1559; no executor assigned. Do not treat this checker as that native run.

**Next mathematical unit**: apply the degree-filtered q_j to derive a provable congruence for the *Dwork defect* (sum_{j<m}q_jM_j-chi_ppW_p), identifying the first nonzero p-adic Newton moments uniformly over the two residue classes. Try m=4 then m=7, keeping (
u_b) branches and exceptional-factor provenance. Failure yields a concrete exact residual, not an unsupported negation. Separately obtain native H0/B0 from actual authorized executor under #1559.

**Control:** Existing exact Source continuation request `onhour11-20261110-1337-exact-cont` returned SUCCEEDED for read and current `HANDOFF_READY / NEEDS_DISPATCH`; `em_site_control(recovery_status)` returned `SITE_CONTROL_OWN_ISSUED_SESSION_REQUIRED`. No authenticated own winning claim or run; this note is author-side only. Research logical lane is `chatgpt-research-onhour-enterprise-math-20260923`; maintenance lane was neither accessed as an owner nor written. Original D24 result and frozen Source pin unchanged.
