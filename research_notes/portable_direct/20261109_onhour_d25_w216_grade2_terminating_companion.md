# D25 — exact p²-grade of the original 216 series as a terminating companion hypergeometric sum

Date: 2026-11-09 (Asia/Hong_Kong). Author-side mathematical work in the pre-existing TASK_RESEARCH objective, **UNREVIEWED / NOT_ADMITTED / NOT_NATIVE**. Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; scientific input pinned at `c47e13e4aba0e006366f989d6334d443f6333ae3`. This note continues `20261109_onhour_d25_cm_sign_to_proven_v2304_comparison.md`, without recrediting accepted D24 work or earlier finite W/V scans.

## A. A theorem on the original third-digit deficit (all primes p=1 mod 6)

Let p=6m+1>3 be prime. Use the original **full** 216 truncation and original integer binomial coefficient
[
 C_n=inom{2n}{n}^{2}inom{3n}{n}
     =rac{(2n)!(3n)!}{(n!)^{5}},quad
 W_p=sum_{n=0}^{p-1}(6n+1)C_n,216^{-n}.
]
All inverses are in (mathbf Z/p^3mathbf Z) or (mathbf F_p), as indicated; 216 is a unit for p>3. Grade by the **binomial coefficient** (v_p(C_n)), keeping the separate original weight (6n+1) (which itself is divisible by p when n=m).

For 0<=n<p the exact valuation is
[
v_p(C_n)=
egin{cases}
0 & 0le nle 2m,\
1 & 2m+1le nle 3m,\
2 & 3m+1le nle 4m,\
3 & 4m+1le nle 6m.
end{cases}
]
The nontrivial grade-2 tail is (mathcal T_{2,p}=sum_{n=3m+1}^{4m}(6n+1)C_n216^{-n}), an *original* subset of the unchanged full W sum, not a new cutoff replacing W.

Put
[
K_p=rac{(3m+2)!}{[(3m+1)!]^5},216^{-(3m+1)}inmathbf F_p^	imes
]
and (U_0=1), with
[
U_j=rac{(1)_j(5/6)_j(7/6)_j}{(3/2)_j^3,2^j},qquad
U_{j+1}=U_jrac{(j+1)(j+5/6)(j+7/6)}{2(j+3/2)^3}.
]
All the displayed denominators for (0le j<m) are p-units. In (mathbf F_p), the parameter (7/6=1-m), so the companion is naturally terminating at (j=m).

**Exact all-prime congruence**
[
oxed{
rac{mathcal T_{2,p}}{p^2}
equiv K_p,sum_{j=0}^{m-1}(6j+4)
rac{(1)_j(5/6)_j(7/6)_j}{(3/2)_j^3,2^j}
pmod p.}
]
This evaluates the actual p²-valuation layer that enters the unresolved (mod p^3) claim, and specifies a terminating hypergeometric transform as the next finite identity to attack.

## B. Exact derivation

For n=3m+1+j, 0<=j<m, we have (2n=p+(2j+1)) and (3n=p+(3m+2+3j)). Wilson's theorem yields, whenever 0<=r<p,
[
(p+r)!/pequiv-r!pmod p.
]
Therefore
[
rac{C_n}{p^2}equiv
rac{(2j+1)!(3m+2+3j)!}{[(3m+1+j)!]^5}pmod p.
]
Also (6n+1=3p+6j+4). The j=0 factorial-unit factor is K_p. The quotient of consecutive factorial-unit factors modulo p is
[
rac{(2j+2)(2j+3)
  (3m+3+3j)(3m+4+3j)(3m+5+3j)}
 {216(3m+2+j)^5}
equiv
rac{(j+1)(j+5/6)(j+7/6)}{2(j+3/2)^3}.
]
This proves the displayed identity term-by-term in the p²-grade. Terms n>4m have coefficient valuation >=3, so vanish modulo p³ without any altered source input.

## C. Direct p=373 diagnostic and cross-model obstruction

For p=373, m=62, (mod p^3=51,895,117), the exact original binomial computations give:
[
(K_{373},sum(6j+4)U_j,mathcal T_{2,373}/373^2)
=(290,217,266)pmod{373}.
]
Since (290cdot217equiv266mod373),
[
oxed{mathcal T_{2,373}equiv37,008,314=266cdot373^2
otequiv0
pmod{373^3}.}
]
Original valuation-group residues mod 51,895,117 (the group is determined by binomial coefficient valuation, not by total weighted-term valuation):
[
(W_0,W_1,W_2,W_{ge3})=(28,094,360, 38,687,933, 37,008,314, 0),
]
[
(V_0,V_1,V_2,V_{ge3})=(45,069,217, 6,826,273, 0, 0).
]
Both sums are 373 mod p³, **but the grade-2 pieces differ by 37,008,314**. Consequently a proposed grade-preserving term-by-term W/V transfer at the third digit is false already at the original p=373. Any successful W-to-V p³ transfer must contain cross-grade correction. The previously proved GZ full-vs-half mod-p³ congruence already explains V grade-2 cancellation; that is consumed, not recredited here.

## D. Exact computational checks and next discriminating experiment

The companion recurrence and original binomial-grade computation were implemented separately using Python integer arithmetic. All **18** checked primes
7,13,19,31,37,43,61,67,73,97,109,127,157,163,193,211,229,373
give identical (mathcal T_{2,p}/p^2inmathbf F_p). On a separate **611-prime exhaustive sieve range** (all primes p≡1 mod6, p<=10000) the companion value was nonzero in each case; this is finite evidence, not a universal nonvanishing theorem.

Reproducer: `research_notes/portable_direct/d25_w216_grade2_companion_20261109.py`.
Raw results: `research_notes/portable_direct/d25_w216_grade2_companion_results_20261109.json`.

**Next local scientific action:** seek an exact transformation/certificate relating the terminating companion (S_p=sum_{j<m}(6j+4)U_j) to the lower two valuation groups and the proven full 2304 sum, or explicitly locate a prime where the observed companion nonvanishing fails. A closed formula for its cross-grade cancellation would supply the unresolved third-digit W-V proof step. Do not replace the frozen same-class H0/B0 benchmark.

**Native benchmark:** issue #1559 remains the distinct original p=373 H0/B0 divided-power ([X]Umod139129) with actual module rank, semilinear direction, eta, signed Green/Hesse kappa, original Delta-R and independent reproducer. In the current run the Sites gateway reported `BACKEND_IDENTITY_CHECK_UNAVAILABLE` with `operation_sent=false` for status/capabilities/recovery; no current winning CLAIM/run or native checkpoint is claimed. Historical Researcher `EM-ENTERPRISE-4DEB43`, session `MCP-ecbfd1c046864bb3bff1a2e04c87d207`, activity `RA-9553E027FD14223807511263` are provenance only; no maintenance lane credentials used.

Source-labelled BRC grouping retains exact original integer coefficients, n-ranges, weighted terms, valuation and intended future readout; this is an auxiliary arithmetic representation, **not** a new native X6 state or accepted Result.
