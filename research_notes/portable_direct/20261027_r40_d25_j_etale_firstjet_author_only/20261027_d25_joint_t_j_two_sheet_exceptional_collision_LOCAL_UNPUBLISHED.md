# D25/LIFT — exact joint-\(t,j\) two-sheet collision and the minimal source tag

**2026-10-27 · Researcher-side portable mathematical unit**  
**Status:** `AUTHOR_DERIVED / EXACT_ALGEBRA / FINITE_RING_AUTHOR_CHECKED / LOCAL_UNPUBLISHED / UNREVIEWED / NOT_ADMITTED / NATIVE_SYNC_DEBT`. This is not a Source checkpoint, native H0/B0 experiment, proof/rebuttal of LIFT/JT2, or new independent mathematical review.

**Canonical parent:** `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`.  
**Task:** `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; immutable publication `TP2-B6F4FC938FF94941C1B7`.  
**Frozen scientific source:** `awdawmip/enterprise-math@c47e13e4aba0e006366f989d6334d443f6333ae3`; taskbook blob SHA-1 `53a3ef039325534e3715add837f0eee332289984`. Current control/git head is not a replacement for this pin.

## 1. Scope and previously consumed result

Earlier author-only units established the CM fibre \(t=1/216\), the two parameters \(x_\pm=27h_\pm=3\pm2s\) with \(s^2=2\), and an **étale overlap of the images under \(j\) alone** when local \(h\) is allowed to deform at \(p=13,19\). This result is used rather than recredited. Other published on-hour E3/3-isogeny and signed-basis evidence is not new work claimed here; native H0/B0 comparison in existing issue #1559 remains a separate owner-bound benchmark. The original accepted UR/JT0 proof and frozen \(R_p\) reduction are not repeated.

**New precise question:** adding **both** the natural scalar parameter \(t\) and the full \(p\)-adic modular \(j\) invariant to the observer, does the map \(x\mapsto(t(x),J(x))\) recover which of the two original \(h\)-source balls the deformed point came from? This is strictly stronger than the earlier j-only overlap question.

## 2. Exact global algebraic identity

Set
\[
 x=27h,\quad t(x)=\frac{x}{27(1+x)^2},\quad
 J(x)=\frac{27(1+x)(1+9x)^3}{x},\quad
 \iota(x)=x^{-1}.
\]
The involution preserves \(t\), and \(S=x+x^{-1}=1/(27t)-2\). Direct polynomial factorization gives the **exact rational identity**
\[
\boxed{
 J(x)-J(1/x)
 =27(x-x^{-1})(27S-10)(27S+46)
 =27(x-x^{-1})(t^{-1}-64)(t^{-1}-8).
}\tag{1}
\]
To check the factorization without any approximation, clear the denominator in \(J(x)-J(1/x)\) and factor its numerator:
\[
 \frac{27(x-1)(x+1)(27x^2-10x+27)(27x^2+46x+27)}{x^3}.
\]
All denominators in (1) are units on the local CM balls at every target prime.

At the CM point \(x_\pm=3\pm2s\), \(S=6\), so \(t=1/216\) and
\[
 J(x_+)-J(x_-)
 =27(4s)(216-64)(216-8)
 =2^9 3^3\cdot13\cdot19\,s.\tag{2}
\]
This recovers the previous **fixed-point** collision valuation without claiming the factorization itself is a full CM Frobenius theorem.

## 3. New theorem: complete joint-observer classification near the original CM fibre

**Theorem.** Fix any prime \(p\equiv13,19\pmod{24}\) and let \(\mathcal O_p=\mathbb Z_p[s]/(s^2-2)\). Let
\[
 \mathcal B_\pm=\{x\in\mathcal O_p:x\equiv3\pm2s\pmod p\},\qquad
 \mathcal T=1/216+p\mathcal O_p.
\]
Then \(t:\mathcal B_\pm\to\mathcal T\) are each bijections. The **joint observer**
\[
 x\longmapsto\bigl(t(x),J(x)\bigr),\qquad x\in\mathcal B_+\cup\mathcal B_-,
\]
is source-injective if \(p\notin\{13,19\}\). At \(p=13\) and \(19\), there are two distinct sources in the two balls with **identical full** \((t,J)\), with exact pairs
\[
\boxed{
 p=13:\quad (t,J)=(1/8,8000),\qquad
 p=19:\quad (t,J)=(1/64,-32768).
}\tag{3}
\]
These are equalities over \(\mathcal O_p\) (not merely modulo a tested precision); the two source coordinates in each pair remain distinct modulo \(p\).

**Proof.** Write \(x_\pm^0=3\pm2s\) and for \(t\in\mathcal T\) let
\[
 F_t(x)=x^2-S(t)x+1,\qquad S(t)=\frac{1}{27t}-2.
\]
At \(t_0=1/216\), \(S(t_0)=6\), and the two roots are \(x_\pm^0\). The derivative \(F_{t_0}'(x_\pm^0)=\pm4s\) is a \(p\)-adic unit (\(p>3\)). The simple-root Hensel lemma over the complete unramified quadratic \(\mathcal O_p\) therefore supplies, for each \(t\in\mathcal T\), a **unique** root \(x_\pm(t)\in\mathcal B_\pm\). Since \(F_t(x)=0\) is equivalent to \(t(x)=t\) on these unit balls, each \(t\) is indeed a bijective coordinate on the individual source ball. The two roots multiply to 1, so \(x_-(t)=1/x_+(t)\), and their difference is a unit modulo \(p\).

Equation (1) now gives the exact difference of the two \(j\)-readouts **at the same specified \(t\)**:
\[
\boxed{
 D(t)=J(x_+(t))-J(x_-(t))
 =27\bigl(x_+(t)-x_-(t)\bigr)(t^{-1}-64)(t^{-1}-8).
}\tag{4}
\]
For every \(t\equiv1/216\pmod p\), the reductions of the last two factors are \(216-64=152=8\cdot19\) and \(216-8=208=16\cdot13\). Thus when the target prime is neither 13 nor 19, both are units, and \(D(t)\) is a unit; equality of joint observer outputs from different balls is impossible.

When \(p=13\), put \(t_*=1/8\). It satisfies
\[
 t_*-t_0=\frac{13}{108}\in13\mathcal O_{13}\setminus13^2\mathcal O_{13}.
\]
Then \(F_{t_*}(x)\), after multiplication by 27, is \(27x^2+46x+27\); its two unique Hensel roots \(x_\pm(t_*)\) lie in the opposite source balls, and by (1) their \(j\) values agree. More precisely, polynomial division yields
\[
 27(1+x)(1+9x)^3-8000x
 =(27x^2+46x+27)(729x^2-270x+1).
\]
Therefore \(J(x_+(t_*))=J(x_-(t_*))=8000\) exactly.

When \(p=19\), put \(t_*=1/64\), satisfying
\[
 t_*-t_0=\frac{19}{1728}\in19\mathcal O_{19}\setminus19^2\mathcal O_{19}.
\]
Here \(F_{t_*}(x)\) becomes \(27x^2-10x+27\), and the corresponding exact identity is
\[
 27(1+x)(1+9x)^3+32768x
 =(27x^2-10x+27)(729x^2+1242x+1).
\]
Both roots hence yield \(J=-32768\) exactly. In either case the roots have distinct reductions \(3\pm2s\), because \(4s\) is a unit. This proves the classification. \(\square\)

**Quantitative precision corollary (same input scope).** Formula (4) in fact gives an **exact valuation budget** for every \(t\in\mathcal T\):
\[
\boxed{
\begin{array}{ll}
 p=13:&v_{13}(D(t))=v_{13}(t-1/8),\\
 p=19:&v_{19}(D(t))=v_{19}(t-1/64),\\
 p\notin\{13,19\}:&v_p(D(t))=0.
\end{array}}
\tag{5}
\]
Here \(v_p(0)=+\infty\). For \(p=13\), \(t^{-1}-64\) is a unit throughout \(\mathcal T\), while \(t^{-1}-8=-8(t-1/8)/t\); for \(p=19\) the roles interchange. The remaining factors, including the branch difference, are units. Thus the special fibres are not merely two isolated samples: they are exactly the simple zeroes of the source-separation signal in the declared p-adic neighbourhood, with an arbitrarily high but explicitly computable precision loss near each zero. The generic target primes have a unit separation at every \(t\) in the neighbourhood.

**BRC/source consequence.** For the declared union of two deformable source balls, full \((t,j)\) readout is not a sufficient recovery state at \(p=13,19\). The pair \((t,J,\text{source-ball label})\) is sufficient, since \(t\) is invertible on each ball. A two-valued branch selector is necessary at the exact double-fibre witnesses; increasing numerical precision in the two original readouts alone does not remove the ambiguity. For **only the two frozen points at \(t=t_0\)**, (2) still shows \(j\bmod p^2\) separates them. The deformation and fixed-fibre domains are distinct; this theorem does not assert that the original fixed CM points have equal \(j\) at infinite precision.

## 4. Executed exact certificate and precision

`d25_joint_t_j_collision_checker_20261027.py` uses only Python standard-library integer/Fraction arithmetic. It evaluates formal \(\mathbb Z/p^5\mathbb Z[s]/(s^2-2)\) arithmetic, Hensel-lifts both source roots with unit derivative, verifies their distinct source residues and product \(x_+x_-=1\), exactly equal mod-\(p^5\) values of \(t,J\), predicted rational \(j\) values, and the fixed-pair nonzero order-one \(j\) difference. Tested primes: 13 and 19 at five digits. Exact rational regressions: 5 points. Nine additional nonexceptional target-prime controls check the exceptional residue condition. For each exceptional prime, four independent nearby fibres \(t=t_*+p^k\), \(1\le k\le4\), verify the exact valuation law \(v_p(D(t))=k\) in precision \(p^5\). **All assertions passed.** Full all-prime claim is justified by (1) and the Hensel proof, **not** by the finite sampling.

The certificate's first-order source changes, in the \(x=a+bs\) basis, are
\[
 (x_+(1/8)-x_+^0)/13\equiv5+7s\pmod{13},\quad
 (x_+(1/64)-x_+^0)/19\equiv9+2s\pmod{19}.
\]
The original \(t_0\) moves by one full \(p\)-adic digit: \((1/8-t_0)/13\equiv10\pmod{13}\), and \((1/64-t_0)/19\equiv18\pmod{19}\). These exact ring calculations agree with the analytic linearization of \(x+x^{-1}=S(t)\). Detailed roots and outputs are stored in `d25_joint_t_j_collision_author_check_20261027.json`.

## 5. Scope, authority, and exact next step

This is an **external rational modular-curve / finite-ring compatibility lemma**, not an embedding of a two-dimensional scheme into the locked six-axis P000 discrete Cell space. Its source population is labeled \(x_+\)/\(x_-\), its observer is a **joint** \((t,j)\), its future operation is local \(p\)-adic deformation and reconstruction, and its signed difference is retained; positive-mass compression is not applied. `BRC_REUSE_APPLIED` at the exact fiber-observer criterion: equation (4) explicitly detects when the quotient is information-lossy.

An actual inert CM \(q\)-Frobenius / native H0/B0 proof must preserve the **frozen** original CM point and derive its real Frobenius/derivative operator. The deformed collision points in (3) are **not** the original CM fibre, so this theorem neither proves nor refutes \(W_p\equiv p\pmod{p^3}\), LIFT or JT2. Source-native bridge, same-original-class [X]U/p², p=373 diagnostic, sign, rank, \(\kappa\), and \(\Delta_p-R_p\) remain assigned to the legitimately authorized native task owner; see pre-existing support issue #1559, **not** a new Task or CLAIM.

On this turn, direct Gateway's `ordinary_chat_recovery.recovery_status` is advertised but no callable tool is exposed; original read request `r40_20261027_0934_cont_read_a` returned `CONTROL_REQUEST_NOT_FOUND` under result lookup, direct continuation `r40_20261027_1042_cont_read_11a` returned `CONTROL_QUOTA`, own checkpoint list returned `ACCESS_DENIED`. Gateway status is 0.6.11 with `research_authority_granted=false`, `executor_binding_configured=false`; Sites reports `static_machine_readonly`, `write_relay_enabled=false`. No native session, winning claim, open, Source result/checkpoint, or mutation is asserted. The `CURRENT_TASK_INPUTS_WITH_NO_RECORDED_OWNER_PROGRESS` seed was **not received**; predecessor completed units are therefore **not invented** (empty array in portable continuation). No denied mutation was retransmitted through another channel.

Original UR V2 bundle (4 files, reported 94,687 bytes, expected SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`) remains an exact-source/provenance recovery obligation. Search of existing conversation/Library index and exact current GitHub digest did not locate byte-identical content; an indexed miss is not proof of nonexistence. Existing UR mathematical proofs remain unchanged.

**Next native authorized action:** recover an exact self-subject session/continuation under the published schema, reconcile original pending write requests without resending, fully read canonical continuation input artifacts if a current-input-only seed is returned, confirm winner CAS, OPEN/RESUME, then publish legitimate evidence/checkpoint with exact frozen source pin. **Next mathematical action:** supply a real same-original-class p-adic Frobenius H0/B0 bridge to \(\Delta_p-R_p\), not another unconnected cusp or deformed \(j\)-collision census.

No scheduler, notification, Worldview, P000, taskbook, GitHub or Site authorization mutations were performed.
