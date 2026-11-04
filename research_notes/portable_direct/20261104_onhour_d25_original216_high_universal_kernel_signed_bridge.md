# D25: original-216 second-valuation band as a terminating universal hypergeometric kernel

2026-11-04 (Asia/Hong_Kong). **Author-side exact scoped derivation, finite exact verified; UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.** This is not a native Source checkpoint or claim.

Frozen task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Research logical lane `chatgpt-research-onhour-enterprise-math-20260923` stays distinct from maintenance `chatgpt-hourly-enterprise-math-20260921`.

## Exact result for the unchanged 216 family

For any prime p=6r+1>=7 define chi=(6/p), k0=3r+1=(p+1)/2, and the original rational coefficients
[
a_k=(2k)!(3k)!/((k!)^5 216^k).
]
Set the p-independent rational sequence
[
q_0=1,quad q_{n+1}/q_n=(n+1)(6n+5)(6n+7)/(9(2n+3)^3).
]
All denominators for 0<=n<=r are p-units.

**Theorem.** For every 0<=n<=r-1, the exact coefficient valuation is 2 and
[
oxed{a_{k0+n}/p^2 equiv (chi/9)q_npmod p.} 	ag{1}
]
Consequently the original weighted high band has the complete signed-port expression
[
oxed{H_p:=p^{-2}sum_{k=3r+1}^{4r}(6k+1)a_k
equiv (chi/9)sum_{n=0}^{r-1}(6n+4)q_npmod p.} 	ag{2}
]
The rational sequence has an arithmetic terminal zero q_r=0 mod p since at n=r-1 the numerator contains 6n+7=p.

Equivalently let theta=z d/dz and define the genuinely terminating mod-p rational truncation
[
Q_{r-1}(z)=sum_{n=0}^{r-1}
rac{(1)_n^2(5/6)_n(7/6)_n}{(3/2)_n^3n!}z^n.
]
Then
[
oxed{H_p=(chi/9)(4+6	heta)Q_{r-1}(1/2)pmod p.}	ag{3}
]
It is a truncated 4F3 kernel with fixed parameters; (7/6)_n=(1-r)_n mod p. The output is a scalar observation of the **original 216** weighted valuation-two port; it does not replace native X6, H0/B0 or Frobenius data.

### Proof

For k0=(p+1)/2, both 2k0 and 3k0 have precisely one p factor in their factorials. Wilson gives (m!)/p=-(m-p)! mod p for p<=m<2p, so
[
a_{k0}/p^2equiv(k0+1)/((k0!)^4 216^{k0})pmod p.
]
Writing h=(p-1)/2 and using (h!)^4=1 mod p, (k0!)^4=(h+1)^4(h!)^4=1/16 mod p and k0+1=3/2 mod p yields
[
a_{k0}/p^2equiv24,216^{-(p+1)/2}
equiv24/(216(216/p))=chi/9pmod p,
]
where Euler's criterion and 216=6^3 give (216/p)=(6/p)=chi. The original exact rational consecutive ratio is
[
a_{k+1}/a_k=(2k+1)(3k+1)(3k+2)/(36(k+1)^3).
]
For k=k0+n this reduces to
[
a_{k0+n+1}/a_{k0+n}
equiv(n+1)(6n+5)(6n+7)/(9(2n+3)^3)pmod p.
]
All interior factors are units for 0<=n<r-1, so induction proves (1). Because 6(k0+n)+1=3p+6n+4, weighted summation proves (2). Finally q_n=(1)_n(5/6)_n(7/6)_n/[2^n(3/2)_n^3], identifying (3). QED.

## Signed cross-family port and still-open proof obligation

Consume existing exact 2304 half/full-cutoff Guo–Zudilin theorem (2019, *A q-microscope for supercongruences*, Adv Math 346, 329–358, arXiv:1803.01830), plus the previously published all-p quartic valuation-two cancellation:
[
V_p=sum_{k=0}^{p-1}(8k+1)(4k)!/((k!)^4 2304^k)
equiv V_h equiv p(-3/p)pmod{p^3},quad h=(p-1)/2.
]
Let A0,A1 be original 216 weighted valuation-zero and -one bands, W_p their full sum including p² H_p. If and only if the additional *unproved* condition p² | (A0+A1-V_h) holds, define
[
M_p=(A0+A1-V_h)/p^2pmod p.
]
Then the exact (conditional on that integrality) reduction is
[
W_p=V_ppmod{p^3}
iff
oxed{M_p+(chi/9)(4+6	heta)Q_{r-1}(1/2)=0pmod p.}	ag{4}
]
This exposes the full high band through a universal finite mod-p kernel, instead of factorial terms at precision p³, while retaining the low/middle-to-quartic compensation as an explicit independent observer. Both the integrality of M_p and the all-prime signed equality remain open.

## Actual exact regression and scoped interpretation

A separately executed Python standard-library integer checker regenerated the original a_k from its unshifted ratio modulo p³ **independently** of generating q_n modulo p; it checked all 148 primes 7<=p<=2000 with p=1 mod6, **22,952 coefficient comparisons**, all PASS, and ten independent factorial/binomial spot-prime cross-checks (7,13,19,31,37,43,61,73,103,373). Finite results: p=13, chi=-1, sum q weighted=1, H=10; p=19, chi=1, sum=5, H=9; p=373, chi=-1, sum=217, H=266. These validate the algebraic derivation on the declared finite range and are not the universal proof.

Full standalone proof and checker evidence in this run's portable artifacts:
`20261104_onhour_d25_original216_high_universal_kernel_signed_bridge.md`,
`d25_original216_high_universal_kernel_checker_20261104.py`,
`d25_original216_high_universal_kernel_results_20261104.json`.

## Continuation and control boundary

**Mother** remains frozen D25 Delta_p-R_p=0 mod p at p=13,19 mod24 (prior scalar bridge W_p=p mod p³). **Highest author-only immutable scientific frontier:** existing F4/Gauss/CM and quartic val2 closure plus theorem (1)-(3), conditional equivalence (4). **Do not redo:** accepted D24 UR, CM0, first digit, Guo–Zudilin quartic tail, earlier p² reflection or all-sum finite scans. **Next exact unit:** construct a source-preserving terminating signed WZ/Green identity for (A0+A1-V_h) at p=13,19,373 first, proving its p²-divisibility and negative of kernel (3), with original low/mid/high endpoints and valuation information. Alternative original F4 signed Green/WZ stays live.

**Native frozen benchmark debt:** `awdawmip/enterprise-math#1559` open/unassigned on 2026-11-04 read; same-original-class H0/B0 [X]U mod 139129, module rank, authentic semilinear Frobenius, eta/odd Green and kappa, independent replay remain NOT_EXECUTED. Site config status `research_authority_granted=false`, `write_relay_enabled=false`, backend version 0.6.11; original `research-onhour-20261031-0205-dispatch-r15` read returned `CONTROL_REQUEST_NOT_FOUND`, read-only continuation returned `CONTROL_QUOTA`. Do not resend original request or borrow a maintenance identity. GitHub author-side proof publication is not Source Researcher authorization or formal scientific admission. Native research session/claim/run/checkpoint/Result: NOT_VERIFIED / NOT_WRITTEN; formal registration REGISTER_PENDING. Reinstatement needs separately approved Site-bound backend client/secure credential.

**Status**: EXACT SCOPED PROOF / FINITE EXACT CHECKED / AUTHOR-SIDE PUBLISHED IF VERIFIED / UNREVIEWED / NOT_ADMITTED / D25 OPEN.
