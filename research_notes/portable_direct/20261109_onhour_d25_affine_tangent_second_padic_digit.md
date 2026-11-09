# D25 — second p-adic digit of the signed original W216/V2304 tangent

Date: 2026-11-09 Asia/Hong_Kong. AUTHOR-SIDE / EXACT FINITE EXPERIMENT / PROVED p^3 COUNTEREXAMPLES / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE. This is a **second distinct research unit**, following `20261109_onhour_d25_affine_two_variable_tangent.md`, which proved the first/second Taylor transfer and identified the first finite tangent pattern.

Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; immutable scientific Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Research conversation `chatgpt-research-onhour-enterprise-math-20260923` (never maintenance). P000 ACTIVE_LOCKED unchanged; all arithmetic below is classical auxiliary finite-ring mathematics, not native H0/B0.

## Precise new second-digit finite conjecture

Keep the ORIGINAL weighted full p-1 cutoffs and their **separate** labeled coefficient streams:
```
a_n=(2n)!(3n)!/((n!)^5*216^n); b_n=(4n)!/((n!)^4*2304^n)
W_p(x)=SUM_{n=0}^{p-1}(6n+1)a_n*x^n
V_p(y)=SUM_{n=0}^{p-1}(8n+1)b_n*y^n
chi=(-3/p) = +1 if p=1 mod3, else -1
J_p=3*W'_p(1)+8*chi*V'_p(1)
```

New **all-prime conjectural identity** (prime p>3):
```
J_p == p*(1+3*chi)/2  (mod p^2), i.e.
  J_p ==  2p (mod p^2) if p=1 mod3;
  J_p ==  -p (mod p^2) if p=2 mod3.              (T2-CANDIDATE)
```
The first derivative mod-p relation reported in the preceding note is the reduction of this stronger statement. This unit adds the **previously unobserved p-adic divided derivative digit**, not another scalar W/V scan.

## Actual exact evidence and negative controls

Executed a modular rational-coefficient recurrence at modulus p^2 for **every one of the 548 primes 5<=p<4000**, covering both chi signs. **All 548 matched T2-CANDIDATE exactly**. Twelve independent direct *integer-binomial* evaluations at p=5,7,11,13,17,19,23,31,37,43,73,373 reproduced W'_p and V'_p **mod p^3** against the recurrences. No floating point, and all denominators are p-units since recurrence steps n+1<p.

Distinct p^3 digits disprove the natural over-strengthening `J_p==p*(1+3chi)/2 (mod p^3)`:

| p | chi | J_p mod p^2 | (J_p-p*(1+3chi)/2)/p^2 mod p |
|---:|---:|---:|---:|
| 5 | -1 | -5 | 1 |
| 7 | +1 | 14 | 3 |
| 11 | -1 | -11 | 2 |
| 13 | +1 | 26 | 5 |
| 19 | +1 | 38 | 5 |
| 373 | +1 | 746 | 340 |

For example p=373, the direct original sum produces `J_373 mod 373^3 = 47,304,606 = 2*373 + 340*373^2`; hence the p^2 identity holds, while its unmodified p^3 strengthening is refuted by an exact original-target witness. These counterexamples concern the specific stronger **derivative** statement, not the unresolved fixed-point 216/2304 p^4 conjecture.

## Proof/precision and observer structure

The prior J1/J2 polynomial Taylor identities are proved algebraically (read previous note). T2-CANDIDATE is **only an exact finite experimental conjecture**, not an all-prime theorem; its divided derivative `(J_p-p*(1+3chi)/2)/p^2` requires an actual p-adic lifting proof for universal use. Preserve original signed weights, characteristic chi, index cutoff, both derivative source tags and actual modulus. BRC exact-provenance observer is `(source, n, valuation, weight, derivative order, p-adic digit)`. An observer quotient at p misses the new nonzero p^1 coefficient `2` or `-1`, and one at p^2 loses the next tested p^3 digit.

Standalone exact verifier `d25_affine_tangent_second_digit_20261109.py` executed:
```
PASS_D25_AFFINE_TANGENT_SECOND_DIGIT 548 primes 5<=p<4000 12 independent exact binomial modp3
```
The attached compact JSON retains twelve anchor third-digit residues and the precise test domain. Existing 2026-10-31 affine p^4 scalar conjecture had already been tested on 1,752 primes and is **reused, not credited anew**.

## Next science and native debt

Attempt an exact finite-field/p-adic hypergeometric transformation proving T2-CANDIDATE, at least for p≡13,19 mod24. Specifically express J_p as a combination of the two separate original truncated derivative ports; reconcile the constant 2p source for the frozen chi=+1 classes, and search for a WZ certificate with all p-1 endpoint terms retained. Use p13,19,373 third digits 5,5,340 to falsify an overstrong lift. Next connect a *proved* tangent identity to the **fixed-parameter** `W_p-V_p=0 modp^3` mother objective if an observer-preserving map is found; parameter deformations alone do not finish JT2.

Native issue `awdawmip/enterprise-math#1559` remains OPEN/UNASSIGNED/NOT_EXECUTED as checked 2026-11-09: original p=373 H0/B0 divided-power [X]U mod139129, rank, Frobenius/eta, signed Green/Hesse, kappa, Delta-R, reproducible independent test. Historical own Researcher `EM-ENTERPRISE-4DEB43`, session `MCP-ecbfd1c046864bb3bff1a2e04c87d207`, RA `RA-9553E027FD14223807511263`; historical original start and continuation succeeded but current recovery `SESSION_CAPABILITY_REQUIRED`, no own winning claim/run/Source checkpoint. This contribution remains author-side GitHub evidence, not a Source Result/accepted theorem. Existing old staging stays separate.