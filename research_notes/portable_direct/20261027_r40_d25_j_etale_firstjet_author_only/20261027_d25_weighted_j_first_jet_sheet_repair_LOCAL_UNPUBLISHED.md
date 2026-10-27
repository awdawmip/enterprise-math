# D25/LIFT — a weighted first-jet repairs the exceptional two-sheet \((t,j)\) source collision

Date: 2026-10-27 UTC.  Research mode: `TASK_RESEARCH`, *portable author-side algebra only*.
Status: `AUTHOR_DERIVED / EXACT_FINITE_RING_AUTHOR_CHECKED / LOCAL_UNPUBLISHED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / NATIVE_SYNC_DEBT`.
This result is **not** an original-H0/B0 benchmark, actual geometric/crystalline Frobenius calculation, admissible Task checkpoint, independent review, or proof of LIFT/JT2.

## Frozen provenance and consumption

- Parent Objective: `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`.
- Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; original publication `TP2-B6F4FC938FF94941C1B7`.
- Frozen *scientific* Source: `awdawmip/enterprise-math@c47e13e4aba0e006366f989d6334d443f6333ae3`; frozen taskbook Git blob `53a3ef039325534e3715add837f0eee332289984`. Neither current project control nor this work changes those pins.
- Direct parent lemma consumed: local 2026-10-27 `20261027_d25_joint_t_j_two_sheet_exceptional_collision_LOCAL_UNPUBLISHED.md`, formula (1), exact two collision fibres and Hensel source balls. Its exact ring helper is imported rather than copied from `d25_joint_t_j_collision_checker_20261027.py` (SHA-256 `0233a63e5473a8a63ac74bd216e0accc4cb3014203becf4d16c9e08734ba17f3`). Reuse is of author-side local mathematics, not of an admitted Result.
- Cross-lane issue `awdawmip/enterprise-math#1559` read on 2026-10-27 UTC: native original-class p=373 [X]U/H0/B0 still classified `PENDING_OWNER / NATIVE_NOT_EXECUTED`. Its on-hour original-E3 signed isogeny, q-Frobenius and second-kind-column work is distinct; this note does not relabel, repeat or adopt those contributions.

## Declared auxiliary model and observer

Let \(p\equiv13,19\pmod{24}\) be prime, let
\[
 \mathcal O_p=\mathbb Z_p[s]/(s^2-2),\quad
 x=27h,\quad t(x)=\frac{x}{27(1+x)^2},\quad
 J(x)=\frac{27(1+x)(1+9x)^3}{x}.
\]
For \(t_0=1/216\), \(x_\pm^0=3\pm2s\), put
\[
\mathcal T=t_0+p\mathcal O_p,\qquad
\mathcal B_\pm=x_\pm^0+p\mathcal O_p.
\]
From the predecessor's simple-root Hensel proof, each \(t\in\mathcal T\) has exactly one \(x_\pm(t)\in\mathcal B_\pm\), with \(x_-(t)=x_+(t)^{-1}\). On these balls \(x\), \(1+x\), \(1-x\), and \(t\) are units. Hence the derivatives along each analytic section
\[
 J_\pm(t)=J(x_\pm(t)),\qquad \theta_t=t\,d/dt
\]
are legitimate. Define the *auxiliary formal weighted j-observer*
\[
 H_\pm(t)=(1+6\theta_t)J_\pm(t).
\]
The source population is two labelled \(X_0(3)\) local balls; allowed operation is same-\(t\) deformations and first-order local differentiation. This is **not** an identification of \(H_\pm\) with the original hypergeometric \(W_p\) or an original Gauss–Manin/Frobenius operator.

## Theorem — a first derivative replaces the otherwise necessary branch bit

For every above target prime and every \(t\in\mathcal T\), the observer
\[
\boxed{\mathcal O_{\rm jet}(x)=(t(x),J(x),(1+6\theta_t)J(x))}
\]
separates the two source balls with just its mod-\(p\) values of the last two components. Precisely:

1. If \(p\notin\{13,19\}\), \(J_+(t)-J_-(t)\) is a \(p\)-adic unit for every \(t\in\mathcal T\).
2. If \(p=13\) or \(p=19\), \(J_+(t)-J_-(t)\equiv0\pmod p\) throughout \(\mathcal T\), but
   \[
   \boxed{\frac{dJ_+}{dt}(t)-\frac{dJ_-}{dt}(t)\equiv10s\pmod p},
   \]
   and the *same* originally specified weight \(1+6\theta_t\) yields
   \[
   \boxed{H_+(t)-H_-(t)\equiv
      \begin{cases}s& (p=13),\\14s&(p=19),\end{cases}\pmod p.}
   \]
   Both differences are units in \(\mathcal O_p\).

Therefore, at both exact collision fibres \((t,J)=(1/8,8000)\) and \((1/64,-32768)\), the zeroth jet is insufficient and the first jet is sufficient. **Jet order one is minimal within the declared 0/1-jet hierarchy** at those fibres. Given the full \(t\) value and the mod-\(p\) pair \((J,H)\), the unique source \(x_+(t)\) or \(x_-(t)\) is determined; an external branch tag is not an independent requirement *when this differentiating observer is available*. If only \((t,J)\) is measured, the predecessor's branch-label obligation remains unchanged.

### Proof

The predecessor's exact rational identity is
\[
D(t):=J_+(t)-J_-(t)
 =27\rho(t)(t^{-1}-64)(t^{-1}-8),\qquad
\rho(t)=x_+(t)-x_-(t).
\tag{1}
\]
For all \(t\in\mathcal T\), \(\rho(t)\equiv4s\pmod p\), and \(t^{-1}\equiv216\pmod p\). Consequently
\[
D(t)\equiv27(4s)(216-64)(216-8)
 =27(4s)152\cdot208\pmod p.
\tag{2}
\]
The coefficient is a unit exactly for target primes other than 13 and 19 (since \(152=8\cdot19\), \(208=16\cdot13\)).

For \(p=13\), \(t^{-1}-8\equiv0\) and \(t^{-1}-64\) is a unit. Differentiate the *exact* identity (1). The terms containing \(t^{-1}-8\) vanish modulo 13, leaving
\[
D'(t)\equiv-27(4s)(216-64)216^2\equiv10s\pmod{13}.
\]
For \(p=19\), instead \(t^{-1}-64\equiv0\), so
\[
D'(t)\equiv-27(4s)(216-8)216^2\equiv10s\pmod{19}.
\]
As \(H_+-H_-=D+6tD'\) and \(t\equiv216^{-1}\), reduction gives
\[
(H_+-H_-)\bmod p=6\cdot216^{-1}\cdot10s
=\begin{cases}s&(p=13),\\14s&(p=19).\end{cases}
\]
Because \(s^2=2\) and \(p>3\), these differences are units. Each branch has one \(x\) for each exact \(t\), hence observing \(t\) plus either distinguishing value recovers the source. At the exact fibres from the parent lemma, \(D(t_*)=0\) as an equality in \(\mathcal O_p\), so order zero genuinely fails, while order one succeeds. This proves the theorem. \(\square\)

The chain rule can alternatively be checked directly, without assuming a \(q\)-Frobenius:
\[
\frac{dJ}{dt}=\frac{J'(x)}{t'(x)},\quad
 t'(x)=\frac{1-x}{27(1+x)^3},\quad
 J'(x)=\frac{27(1+9x)^2(27x^2+18x-1)}{x^2},
\]
\[
\boxed{(1+6\theta_t)J(x)=
-\frac{27(1+x)(1+9x)^2(153x^2+116x-5)}{x(x-1)}.}
\tag{3}
\]
All denominators in (3) are units on the declared source balls.

## Executed exact check and limitations

`d25_weighted_j_first_jet_sheet_repair_checker_20261027.py` imports the exact predecessor ring operations and checks equations (1)–(3) in \((\mathbb Z/p^5\mathbb Z)[s]/(s^2-2)\). It Hensel-lifts the two distinct roots of each collision fibre at \(p=13,19\), independently evaluates \((1+6\theta_t)J\) through the rational \(x\)-formula, confirms \(D=0\pmod {p^5}\), \(D'=10s\pmod p\), \(H_+-H_-=s,14s\pmod p\), and tests four nearby precision layers \(t=t_*+p^k\), \(1\le k\le4\). The remaining 164 target primes under 5000 are included only as exact coefficient-divisibility controls. The all-prime result is established by the factorization and derivative proof, not those finite checks.

The original LIFT hard target remains \(\Delta_p-R_p=0\pmod p\) (equivalently, under the inherited bridge, \(W_p\equiv p\pmod{p^3}\)). To use the new theorem there, a genuine original-class H0/B0/q-Frobenius comparison must **prove an interface carrying this first-jet observer or its adequate signed analogue** to the native weighted \(\omega+6\nabla_\lambda\omega\) port. Merely matching the number 6 in both operators does not provide that transfer. This theorem closes an auxiliary source-injectivity issue, not the original second-digit supercongruence.

## Control and exact next action (2026-10-27 UTC)

- Gateway `0.6.11` read-only observations: `em_status` reports `research_authority_granted=false`, `executor_binding_configured=false`; Sites is `static_machine_readonly` / `write_relay_enabled=false`. `recovery_status` is advertised in the service contract but is not a callable tool here. `em_control_continuation` and exact task returned `CONTROL_QUOTA`, own checkpoint list returned `ACCESS_DENIED`, and original receipt request `r40_20261027_0934_cont_read_a` returned `CONTROL_REQUEST_NOT_FOUND`. This does not establish an empty global Task queue or permission to reissue mutations.
- No current winning CLAIM, native run, session key, Source checkpoint, or fresh canonical dispatch was verified. The original continuation seed was not received, so **predecessor `completed_units=[]`**; the material proved here is labelled *current local author work*, not predecessor completion.
- UR V2's precise four-file original remains to be recovered and compared to reported 94,687 bytes / SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`; inherited completed UR mathematics is not restarted.
- Actual responsible native path: authorized Task owner/implementation maintainer on `awdawmip/enterprise-math#1559`. First accepted proof-of-execution must include the **original fixed class** p=373 `[X]U mod139129`, module rank, semilinear Frobenius sign/eta, Green/Hesse observer, original \(\kappa\) and \(\Delta-R\); an auxiliary \(j\)-jet is a discriminating *comparison check* only if its origin and coordinate transfer are explicitly established.
- Next legitimate control action: read own actual recovery status and pending original requests through an authorized read channel; recover Source exact continuation; if a current-input-only seed is supplied, complete every pinned input-artifact readback, keep predecessor completed units empty, and use typed continuation only under verified predecessor CAS; otherwise resume an actually verified winning same-session run. Save/read back checkpoints only with real current authority.

No scheduler, notification settings, external Issue mutation, protected P000/worldview change or frozen-source repinning occurred.
