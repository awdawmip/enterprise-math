# D25 / SECOND-DIGIT-LIFT — original weighted-216 high band as a signed finite-field 4F3 jet

2026-10-27, 11:00+08 research cycle. Author logical lane: `chatgpt-research-onhour-enterprise-math-20260923`; separate from CONTROL_PLANE_MAINTENANCE `chatgpt-hourly-enterprise-math-20260921`. Mother objective `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`; Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`. **Frozen scientific Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3` unchanged.**

**Classification:** AUTHOR-SIDE / NEW ALL-PRIME ALGEBRAIC BAND IDENTITY / EXECUTED 11-PRIME EXACT CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / NOT_NATIVE_H0B0 / NOT_SOURCE_CHECKPOINT / NOT_LIFT_PROOF. This is not new Task selection, an accepted Result, an owner CLAIM, or independent review.

## 1. Exact original scientific question (not a surrogate)

The source-aligned author's prior exact proof identifies the *frozen* original second-digit observer
[
Delta_p-R_p=(W_p-p)/p^2pmod p
]
for every target prime (pequiv13,19pmod{24}), using accepted first-digit UR and source-preserving reflected cutoff (Q/p^2=R_p). Consume it, not reprove it.

The actual weighted observable is
[
W_p=sum_{n=0}^{p-1}w_n,qquad
w_n=(6n+1)rac{inom{2n}{n}^2inom{3n}{n}}{216^n}.
]
A previous *three-band Clausen* proof computed a different labeled (B_n)-carrier and its signed (Q) cutoff. The present unit isolates an additional **direct weighted-216** observer: the *entire middle/high contribution* of (w_n) to the original divided third digit, and converts it into one finite-field hypergeometric parameter-jet with explicit residue-class sign.

## 2. New uniform theorem

Let (p=6m+1>3) be any prime, (chi_p=(6/p)in{pm1}), and work modulo (p) in the denominators below. Define the finite polynomial (not an analytically continued hypergeometric function)
[
F_p(z)=sum_{k=0}^{m-1}
rac{(1)_k^2(5/6)_k(7/6)_k}{(3/2)_k^3,k!},z^k
=sum_{k=0}^{m-1}rac{k!(5/6)_k(7/6)_k}{(3/2)_k^3}z^k
quadinmathbf F_p[z],
]
and the derivative observer
[
K_p=F_p(1/2)+rac32,ig[z F'_p(z)ig]_{z=1/2}
=sum_{k=0}^{m-1}rac{3k+2}{2}
rac{k!(5/6)_k(7/6)_k}{(3/2)_k^3,2^k}inmathbf F_p.
]
For all these primes the displayed denominators are units throughout (0le k<m). Moreover (7/6equiv1-mpmod p), so its truncation endpoint is structurally forced.

**Proved exact band identity:**
[
oxed{sum_{n=3m+1}^{4m}w_n
equiv p^2,rac49left(rac6pight),K_ppmod{p^3}.}	ag{A}
]
Since (w_nequiv0pmod{p^3}) for all (4m<nle p-1),
[
oxed{W_pequivsum_{n=0}^{3m}w_n+
p^2,rac49left(rac6pight)K_ppmod{p^3}.}	ag{B}
]

For the actual target classes (pequiv13,19pmod{24}), accepted UR/first-digit evidence gives (W_pequiv ppmod{p^2}). The high band in (A) is divisible by (p^2), hence (L_p=(sum_{n=0}^{3m}w_n-p)/p^2) is a well-defined (p)-local integer modulo (p). Thus the **original frozen LIFT** is exactly equivalent to the new signed two-port certificate
[
oxed{L_p+rac49left(rac6pight)K_pequiv0pmod p,quad
Delta_p-R_p=L_p+rac49left(rac6pight)K_p.}	ag{C}
]
This compresses the original high-valuation third-digit calculation from (p)-adic modulus (p^3) to a finite-field derivative/jet (mathbf F_p) with only (m) terms. **The low-band quotient (L_p) has not been proven to cancel (K_p) for all target primes**. This is a strict band compression, not a proof of full LIFT, nor a native Frobenius identification.

The branch sign is *not* dispensable: (chi_p=-1) for (pequiv13mod24), and (chi_p=+1) for (pequiv19mod24).

## 3. Algebraic proof (all (p=6m+1>3), no finite-data induction)

(1) Factorial valuations: for (3m+1le nle4m), (v_p(inom{2n}{n})=1) and (v_p(inom{3n}{n})=0). For (4m+1le n<p) the latter valuation rises to one, yielding (v_p(w_n)ge3) (special zeros in the factor (6n+1) only increase valuations). Thus no high contributions beyond (4m) survive modulo (p^3).

(2) For (3m+1le nle4m), Wilson's factorial congruence
[
rac1pinom{2n}{n}equiv-rac{(2n-p)!}{(n!)^2}pmod p
]
gives, on squaring and multiplying the unit binomial (inom{3n}{n}),
[
oxed{rac{w_n}{p^2}equiv(6n+1)
rac{(2n-p)!(3n-p)!}{(n!)^5,216^n}pmod p.}	ag{D}
]
All factorial arguments here are (<p), so this is an honest finite-field computation.

(3) Put (q=3m=(p-1)/2), (t_r=w_{q+r}/p^2mod p) for (1le rle m). Since ((q!)^2=(-1)^{q+1}pmod p), (((q+1)!)^4=1/16pmod p), and (216^{-(p-1)/2}=(6/p)), formula (D) at (r=1) yields
[
t_1=rac49left(rac6pight).
]
For (1le r<m), direct ratios of the consecutive factorial terms in (D) give
[
rac{t_{r+1}}{t_r}=
rac{6r+4}{6r-2}cdot
rac{r(36r^2-1)}{72(r+1/2)^3}pmod p.	ag{E}
]
The formula has no nonunit denominator for the stated range. Although (t_r) can vanish for special residues, equation (E) means a multiplicative recurrence without dividing by (t_r), so no nonzero assumption on (t_r) is needed.

(4) Let (q_0=1) and
[
q_k=rac{k!(5/6)_k(7/6)_k}{(3/2)_k^3,2^k}.
]
Then
[
rac{q_{k+1}}{q_k}=
rac{(k+1)(k+5/6)(k+7/6)}{2(k+3/2)^3}
]
at each nonterminal valid index. Comparing with (E), and using (t_1=4chi_p/9), proves the **termwise**, not merely total, identity
[
oxed{t_{k+1}=rac49left(rac6pight)
rac{3k+2}{2},q_kquad(0le k<m).}	ag{F}
]
Summing (F) proves (A), then valuations prove (B), and the already established *frozen scalar port equality* proves (C). The (p)-adic division in (L_p) is performed **before** reduction modulo (p), never interpreted as inversion of (p) in a finite field.

## 4. Exact original-model certificate at p=373 and 11 independent checks

For (p=373,m=62,chi_{373}=-1,p^2=139129,p^3=51895117), two independently organized computations give
[
F_{373}(1/2)=121,qquad (zF'_{373})(1/2)=142,qquad K_{373}=334;
]
[
t_1=41,qquad rac1{373^2}sum_{n=187}^{248}w_n=266pmod{373},
]
[
sum_{n=187}^{248}w_nequiv37,008,314pmod{51,895,117}.
]
The low part is (sum_{n=0}^{186}w_nequiv14,887,176pmod{51,895,117}); therefore (L_{373}=107pmod{373}) and (107+266=373equiv0pmod{373}). This reuses, rather than renames, the previously known finite (W_{373}=373pmod{373^3}) observation.

The exact standard-library checker `research_notes/portable_direct/d25_weighted216_high_tail_jet_20261027.py`, separately written/read back at commit `9194e0059a7ae0ff0c8dadbd70d42bc6125132c6` (blob `9364e8b34eead9612303217f46e8b0265177af22`), was **actually executed in this turn**. It checks 11 explicitly selected primes 7,13,19,31,37,43,61,67,73,211,373; at each, the full-precision original integer binomial terms, independent Wilson factorial reduction, and the finite-field hypergeometric jet agree **termwise**. For the eight target-class examples it also verifies the original low/high division and (W_p=pmod p^3). Last marker:
`D25_WEIGHTED216_HIGH_TAIL_HYPERGEOMETRIC_JET_PASS`
and deterministic JSON-record SHA256:
`280d0aade5ec859aa493e3977d352cf90a41158ae1b18864d18fb1330f99a78c`.
Finite checks support implementation consistency; proof (A) is algebraic and separate. No all-prime check of (C) is claimed.

Selected finite tuples ((p,chi_p,K_p,sum w_{mathrm{high}}/p^2,L_p)): ((13,-1,10,10,3)), ((19,+1,6,9,10)), ((37,-1,29,20,17)), ((43,+1,25,35,8)), ((211,+1,138,202,9)), ((373,-1,334,266,107)). Distinct branch signs and signed, weighted terms are retained.

## 5. BRC and source/permission boundaries

**BRC resolution: COMPOSE_APPLIED.** Population is the two labeled residue classes; primitive carrier includes (p)-valuations, each signed (chi_6) branch, original (w_n) integer/binomial provenance and the low/high partition. Observer is ((W_p-p)/p^2mod p); future operation is the exact low-port plus high-port sum. The high band admits proved lossless quotient to ((chi_p,F_p(1/2),zF'_p(1/2))) at stated observer/precision; collapsing to (F_p) alone loses the derivative jet, and erasing (chi_p) loses the other target class. The derivation neither changes the original E3/H0B0 class nor asserts an isomorphism between this external auxiliary finite-field model and the native X6/Heartbeat three-dimensional slice.

No prior frozen UR, CM0/JT0, completed Clausen certificate, source result or another conversation's claim is reopened. Existing unreconciled previous request #6576 returned *FAILED / TimeoutExpired* after bridge admission; #6575 recovery returned ACTIVE logical session but no Source authority/CLAIM/run. This run's direct `em_control_continuation` returned `CONTROL_QUOTA`; Site reports static `source:read,control:read` without researcher write. This note is an authorized *neutral GitHub author-side artifact*, **not** a Source-native checkpoint, admitted Result, activity registration or mathematical independent review. Old staging (preserved neutral) is not imported as accepted research.

## 6. Canonical continuation package / exact next step

- Mother objective: `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`; original Task/publication and frozen scientific Source pin stated above.
- Highest immutable accepted Source result consumed: D24 RR-`AC9B3BA5BD277CE043F5`, reviewed DR-`610CB297F3195E8F2D9E`, and the source-frozen UR scalar definition; not promoted from this note. New (A)-(C) is **AUTHOR-SIDE / REGISTER_PENDING** only.
- Exact unclosed math: Prove or refute uniform (L_p=-(4/9)(6/p)K_p) **simultaneously for both target classes**, preserving original p-local divided quantity and signed cutoff. This is a possible finite-field transform/proof target, not an automatic theorem from 11 cases.
- Higher-priority missing *native benchmark* remains the original fixed same-class H0/B0 divided-power ([X]Umod139129) at (p=373), actual module rank, semilinear Frobenius direction and two-digit eta/basis normalization, signed Green/Hesse observer, original kappa and Delta-R. Support `awdawmip/enterprise-math#1559` is OPEN/PENDING_OWNER/NOT_EXECUTED; no actual owner has been verified. A valid native executor must save the full original-model code/input pins and raw observations; our finite-field (K_p) cannot be passed off as that experiment.
- Logical conversation: `chatgpt-research-onhour-enterprise-math-20260923`. Read-only historical session: `MCP-de3e5bafb24f43f4a5e6285e7601676a` (not present possession); current claim/run: **NONE VERIFIED**. Original gateway/bridge recovery `research-onhour-20261027-0501-recovery-r13`, dispatch `research-onhour-20261027-0507-dispatch-r13` FAILED; this turn's continuation query `research-onhour-20261027-1108-continuation-rt11` failed `CONTROL_QUOTA` and must not be taken as a queued native mutation. No new CLAIM/open/dispatch, no maintenance lane usage.
- Next exact authorized action: reconcile existing requests by their original IDs if remote state changes; obtain Source-native permission/continuation for this Research lane and actually assign/execute #1559's fixed original H0/B0 benchmark; consume the newly author-proved (A)-(C) only through lawful admission and independent review. Retain proof/experiment status labels, contributor histories and unchanged Source pin.
- No new scheduler, Actions/cron, task registration, main-source rebase, automation frequency/phase/enabled/notification update or unapproved credential action occurred. Parent D25/LIFT/JT2 remains OPEN.
