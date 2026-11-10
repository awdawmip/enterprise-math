# D25/W216 — two new exact target-class diagonal carry witnesses (p=109,139)

Date: 2026-11-10, 21:00 +08:00. Research lane: `chatgpt-research-onhour-enterprise-math-20260923`.
Classification: **AUTHOR_SIDE / FINITE_EXACT_COMPUTATION / UNREVIEWED / NOT_ADMITTED / NATIVE_H0_B0_NOT_RUN**.
Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; immutable publication `TP2-B6F4FC938FF94941C1B7`; frozen scientific Source `c47e13e4aba0e006366f989d6334d443f6333ae3` (unchanged).

## 1. New discriminating input, preserving original observer

Consume the predecessor's exact W216 original signed coefficients without changing their definitions:

\[
A_k=\frac{\binom{2k}{k}^2\binom{3k}{k}}{216^k},\qquad
W_n=\sum_{k=0}^{n-1}(6k+1)A_k.
\]

For target primes \(p\equiv13,19\bmod24\), put \(\chi_p=1\) (since \(p\equiv1\bmod3\)), \(W_1=1\), and for \(r\ge1\)
\[
D_{p,r}=W_{p^r}-\chi_ppW_{p^{r-1}},\qquad
E_{p,r}=\frac{D_{p,r}}{p^{3r}}\in\mathbf Z_{(p)}
\]
at each tested input (integrality explicitly checked). The previous finite note at commit `c75eebea65ac724d1545534c6bc82d39b587c2ad` found constant diagonal digits for p=13,19,37,43,61,67. This unit checks **two previously untested original target primes**, 109 (class 13) and 139 (class 19), each at scales \(r=1,2,3\), rather than repeating those prior samples.

The tested candidate is
\[
E_{p,r+1}-E_{p,r}\stackrel{?}{\equiv}\delta_p p^r\pmod{p^{r+1}}
\]
with the same \(\delta_p\) at both transitions \(r=1,2\) for each new p.

## 2. Complete exact p-adic witnesses

Each \(W_{p^r}\) below is computed modulo the **same exact modulus** \(p^{13}\) with two independently coded original-coefficient constructions. The table gives \(E_{p,r}\bmod p^4\); its output is determined by those W residues. All differences \(D_{p,r}\) were checked divisible by \(p^{3r}\) *before division*. No floats, approximate equality, or non-unit inverses are used.

| p | class mod 24 | \(W_p\bmod p^{13}\) | \(W_{p^2}\bmod p^{13}\) | \(W_{p^3}\bmod p^{13}\) |
|---:|---:|---:|---:|---:|
| 109 | 13 | 70269954303420154889106740 | 50845448821298988397275985 | 129538326046278468867734745 |
| 139 | 19 | 6172957772469749019232058935 | 6725260932517571183538223246 | 4957652226525797405934924919 |

| p | \(E_{p,1}\bmod p^4\) | \(E_{p,2}\bmod p^4\) | \(E_{p,3}\bmod p^4\) | \(r=1:\ (E_2-E_1)\bmod p^2\) | \(r=2:\ (E_3-E_2)\bmod p^3\) |
|---:|---:|---:|---:|---:|---:|
|109|64750664|90905868|48728318|5123 = 47·109|558407 = 47·109²|
|139|100717108|124405627|151397064|973 = 7·139|135247 = 7·139²|

**Proved by exhaustive exact execution over this finite input set:** for \((p,r)\in\{(109,1),(109,2),(139,1),(139,2)\}\),
\[
v_p(E_{p,r+1}-E_{p,r})=r,\qquad
\delta_{109}=47,\quad\delta_{139}=7.
\]
The two independent methods agree for all six \((p,r)\) scale residues. The full coefficient sums cover respectively \(109^3=1295029\) and \(139^3=2685619\) original signed terms. This constitutes four *new* transition witnesses, not a theorem for every p or r.

## 3. Independent constructions and observer fidelity

The accompanying standard-library checker `d25_w216_diagonal_target_primes_20261110.py` implements:

- **Ratio construction:** advance the original recurrence
  \[
  A_{k+1}/A_k=\frac{(2k+1)(3k+1)(3k+2)}{36(k+1)^3},
  \]
  isolating \(v_p(A_k)\) and the \(p\)-unit before modulus reduction.
- **Factorial construction:** independently advance the \(p\)-unit factorials of \(k!, (2k)!, (3k)!\), then reconstruct
  \(A_k=(2k)!(3k)!/(k!)^5\,216^{-k}\).
- **Exact oracle:** assert equality of all independent \(W_{p^r}\bmod p^{13}\) values, integrality of each \(D_{p,r}/p^{3r}\), and the two identical diagonal digits in each target class.

BRC / residual-fidelity carrier: \((p,r,k,v_p(A_k),u_p(A_k),6k+1,W_{p^r},D_{p,r},E_{p,r}\bmod p^4)\). Operations: original signed accumulation, \(p^{3r}\)-divided defect, adjacent-scale difference, \(p^{r+1}\) projection. The scalar mod-p² summary alone loses the \(r=2\rightarrow3\) digit. Neither coefficient method computes the native H0/B0 module; this is an original-W216 finite observer study, not a substitute native run.

## 4. Frozen mother objective and exact continuation

The accepted D24 UR/JT0 is already completed. The live mother goal remains the original **signed** \(\Delta_p-R_p\equiv0\bmod p\) for both target prime classes. The prior author source-port proof at `research_notes/portable_direct/20261026_onhour_d25_native_lift_source_port_identity.md` gives the exact equivalence with \(W_p\equiv p\bmod p^3\), keeping the cutoff correction \(R_p\), not dropping it. This finite unit checks \(W_p\equiv p\bmod p^3\) at its two new primes but supplies no uniform LIFT proof.

Highest native evidence debt: the *same-original-class*, fixed \(p=373\) divided-power H0/B0 \([X]U\bmod139129\), actual module rank, Frobenius semilinear direction and basis-normalization \(\eta\), signed odd Hesse/Green \(\kappa\), original \(\Delta-R\), and independent replication. Existing support Issue #1559 is the responsible intake, OPEN / PENDING_OWNER; no native executor is asserted.

Source continuation read `onhour11-20261110-1957-exact-continuation` was **SUCCEEDED**, as-of Source `abf7c03205b83f96b114747e2fc326dbc3615cdb`; current own recovery_status attempted this run returned `SITE_CONTROL_OWN_ISSUED_SESSION_REQUIRED`. Previous historical Researcher session `MCP-5378d3819d8947bda9049c9428493e2d` is public history, not a currently recoverable private capability. No new winning CLAIM, open run, Source-native checkpoint, Result, review or formal admission is claimed; maintenance logical conversation is not used.

**Next exact mathematical action:** derive or find a counterexample to the \(p\)-block transfer bound \(v_p(E_{p,r+1}-E_{p,r})\ge r\) from the already built finite Newton/moment transfer, rather than widening the sample census again. **Next native owner action:** obtain authorized original H0/B0 evaluator and independently publish the exact fixed p373 benchmark with all rank/normalization/signed checks under the frozen source, then route for independent review.

Do not repeat: predecessor accepted UR/CM0/JT0; previous finite scale sets and their 16 transitions; already completed W216 auxiliary proofs; Source's inherited checkpoint units. Keep old staging and separate Research vs Maintenance contribution histories intact.
