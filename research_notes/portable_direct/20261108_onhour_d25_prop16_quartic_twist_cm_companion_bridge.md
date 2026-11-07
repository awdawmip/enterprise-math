# D25 — Original E3 Proposition-16 / quartic-twist CM companion bridge

Date: 2026-11-08  
Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`  
Publication: `TP2-B6F4FC938FF94941C1B7`  
Scientific input pin: `enterprise-math@c47e13e4aba0e006366f989d6334d443f6333ae3`  
Logical Research lane: `chatgpt-research-onhour-enterprise-math-20260923`  
Excluded lane: `chatgpt-hourly-enterprise-math-20260921`  
Status: `AUTHOR_SIDE_PROVED / EXACT_FINITE_CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE`

## 1. New result

For every prime \\(p\ge13\\) with \\(p\equiv13,19\pmod{24}\\), put \\(T^2=2\\) in the unramified quadratic coefficient field and use the fixed original-E3 identity-branch conventions from the D25 source notes. Let

- \\(a_{p-1}\in\mathbb F_{p^2}\\) be the coefficient of the invariant differential at the \\(\xi^{p-1}d\xi\\) port;
- \\(b_{p-1}\in\mathbb F_{p^2}\\) be the regular coefficient of the original second-kind differential after its exact principal part is retained in provenance and removed only in the formal de Rham quotient;
- \\(A_p=a_{p-1}/p\pmod p\\);
- (\beta=(4-T)/72\).

Then the original-coordinate coefficient identity is

\[
\boxed{A_p\,b_{p-1}\equiv\beta\pmod p.}
\]

Equivalently, the coefficient of the normalized CM companion \\(\nu/\beta\\) is

\[
b^{\rm CM}_{p-1}
=a_{p-1}+\beta^{-1}b_{p-1}
\equiv\beta^{-1}b_{p-1}\pmod p,
\]

and

\[
\boxed{A_p\,b^{\rm CM}_{p-1}\equiv1\pmod p.}
\]

This is an all-target-prime corollary of the d=3 supersingular formal-cohomology result of Chisholm–Deines–Long–Nebe–Swisher, Proposition 16, after transporting the exact D25 CM eigenbasis and the quartic coordinate twist. It is not a claim that the native H0/B0 `[X]U` benchmark has run.

## 2. Exact curve and CM eigenbasis

The task's original curve is the d=3 family

\[
E_3(t):\quad y^2+xy+(t/27)y=x^3,
\qquad
t=\frac{2-T}{4},\quad T^2=2.
\]

Directly,

\[
4t(1-t)=\frac12,
\]

so \\(\lambda_3=1/2\\), and the original formal parameter is \\(\xi=-x/y\\). The original-E3 isogeny calculation gives, in the fixed basis (\\(\omega,\eta\\)), the CM generator matrix

\[
M_\vartheta=
\begin{pmatrix}
-su & u(2s-1)/18\\
0 & su
\end{pmatrix},
\qquad s=T,\quad u^2=-3.
\]

Its (+su) eigenline is

\[
\nu=\eta+\beta\omega,
\qquad
\beta=\frac{2T-1}{36T}=\frac{4-T}{72}.
\]

The identity-branch repair gives

\[
\eta_O=\xi^{-2}d\xi-\eta_Q.
\]

The pole is retained as a source feature; its principal part is exact in the local formal de Rham quotient. The regular coefficient stream of \\(-\eta_Q\\) is precisely (b_n). Since \\(\omega_O\\) has leading coefficient 1 and the regular part of \\(\eta_O\\) has leading coefficient 0, the normalized eigenline \\(\nu/\beta\\) has coefficient stream

\[
a_n+\beta^{-1}b_n.
\]

In particular, its (p-1) coefficient is \\(a_{p-1}+\beta^{-1}b_{p-1}\\). Supersingularity gives \\(p\mid a_{p-1}\\).

The coefficient formulas used in the exact checker are

\[
a_n=\sum_{j=0}^{\lfloor n/3\rfloor}
\binom{2j}{j}\binom{n-j}{2j}c^j,
\]

\[
b_n=\frac12\sum_{j=1}^{\lfloor(n+2)/3\rfloor}
\binom{2j}{j}\binom{n-j+1}{2j-1}c^j,
\qquad c=\frac{2-T}{108}.
\]

All coefficients are evaluated in (\\(\mathbb Z/p^3\mathbb Z\\)[T]/(T^2-2)) before the exact division of (a_{p-1}) by (p).

## 3. The quartic twist is the missing coordinate factor

For d=3, the source paper's quartic twist uses

\[
\alpha^4=1-\lambda_3=\frac12,
\qquad
\widetilde\xi=\alpha\xi
\]

(up to the equivalent inverse-pullback convention). Each normalized (p-1) differential coefficient acquires the same factor (\alpha^{\pm(p-1)}), so their product acquires

\[
\alpha^{\pm2(p-1)}.
\]

For the target prime classes, (\\((2/p)=-1\\)), hence the Frobenius conjugation satisfies (T^p=-T). Since \\(\alpha^2=\pm T/2\\),

\[
\alpha^{2(p-1)}
=\left\\(\frac{T}{2}\right\\)^{p-1}
=\frac{(T/2)^p}{T/2}
=-1.
\]

The inverse has the same value. Thus the quartic coordinate change flips the product sign exactly; it is not an optional normalization.

The paper's d=3 construction supplies the required degree-(p^2) supersingular Frobenius lift from the multiplication-by-(-p) map on (t=-x/y), after this same quartic twist. This lift commutes with the CM ring because multiplication by (-p) is central. In the paper's convention this gives (b_2=p); Proposition 16 has supersingular sign (-1), so the twisted normalized eigenfunction product is \\(-p\pmod{p^2}\\).

Translating back to the original coordinate multiplies the product by (-1), hence

\[
a_{p-1}\left\\(a_{p-1}+\beta^{-1}b_{p-1}\right\\)
\equiv p\pmod{p^2}.
\]

The (a_{p-1}^2) term is divisible by (p^2). Removing it and dividing by (p) gives

\[
\frac{a_{p-1}}p\,\beta^{-1}b_{p-1}\equiv1\pmod p,
\]

which is the claimed \\(A_pb_{p-1}=\beta\\\) identity.

### Correction to the earlier negative control

The earlier `B_required=-A^{-1}` comparison applied the twisted Proposition-16 product to an unscaled (A_p). That mixed two coordinate frames. The actual twisted pair is

\[
\widetilde A_p=\alpha^{\pm(p-1)}A_p,
\qquad
\widetilde B_p=\alpha^{\pm(p-1)}b^{\rm CM}_{p-1},
\]

so

\[
\widetilde A_p\widetilde B_p
=\alpha^{\pm2(p-1)}\\(A_pb^{\rm CM}_{p-1}\\)
=-1.
\]

The original-coordinate product is (+1), while the quartic-twisted product is (-1), exactly as Proposition 16 requires. The statement that (b_{p-1}) alone is not the normalized CM companion remains correct; the correct original-coordinate normalization is \\(\beta^{-1}b_{p-1}\\) modulo (p). The earlier mismatch is therefore a coordinate-frame error, not a counterexample to the E3 formal-cohomology bridge.

## 4. BRC paired middle-band observer

The D25 middle coefficient has the normalized form

\[
u_{m+r}=\frac{q_m}{50}K_r,
\qquad
q_m=2^{-m}\binom{2m}{m},
\qquad
K_1=1,
\qquad
K_{r+1}=\frac{3r(6r+1)}{(6r+5)^2}K_r.
\]

Let

\[
H_i^{\rm tail}=\sum_{a=1}^{i}(1+6(i-a))c_a,
\]

and let the middle Taylor-jet weight be

\[
f_{m+r}
=\frac{H_{r-1}-H_m}{6}
-\frac{H_{2m}-H_{m-r}}{3},
\]

where the (H_j) on the right are ordinary harmonic numbers. The same (u_{m+r}) carrier is observed in two different ways:

\[
L_2^{\rm mid}=\sum_{r=1}^{m}u_{m+r}f_{m+r}
=\frac{q_m}{50}\sum_{r=1}^{m}K_rf_{m+r},
\]

\[
S_{\rm mid}=2\sum_{r=1}^{m}u_{m+r}H_{m+r}^{\rm tail}
=\frac{q_m}{25}\sum_{r=1}^{m}K_rH_{m+r}^{\rm tail}.
\]

Therefore

\[
\boxed{
\begin{pmatrix}L_2^{\rm mid}\\S_{\rm mid}\end{pmatrix}
=
\frac{q_m}{50}\sum_{r=1}^{m}K_r
\begin{pmatrix}f_{m+r}\\2H_{m+r}^{\rm tail}\end{pmatrix}.
}
\]

This is a genuine same-carrier/two-observer factorization. It does **not** identify the signed cutoff observer \\(S_{\rm mid}\\) with the formal E3 coefficient (b_{p-1}).

The three-band Taylor identity remains

\[
\frac{\Phi_{xx}}{72}
\equiv L_2^{\rm low}+L_2^{\rm mid}+V_{4m}\pmod p,
\]

while the second-reflection cutoff identity is

\[
\frac{Q_p}{p^2}
\equiv \mathcal R_m+p\\(S_{\rm low}+S_{\rm mid}\\)\pmod{p^2}.
\]

Together with the original signed source-port identity,

\[
\Delta_p-\mathcal R_m
\equiv \frac{W_p-p}{p^2}+p\\(S_{\rm low}+S_{\rm mid}\\)\pmod{p^2}.
\]

The low-high correction remains separately typed:

\[
S_{\rm low}
=2\sum_{i=1}^{m}\sum_{a=1}^{i}
\left[(1+6(i-a))(d_ic_a+q_iv_a)+6q_ic_a\right].
\]

No positive-mass, total-only or prime-only projection is used; the signed cutoff, the middle carrier, the low/high reflected coefficients and the original E3 coefficient field remain distinct.

## 5. Exact discriminating checks

All entries below are residues in the indicated field/ring. \\(T^2=2\\).

| Observer | (p=19) | (p=373) |
|---|---:|---:|
| (A_p=a_{p-1}/p) | (11+16T) | (349+48T) |
| (b_{p-1}) (regular second-kind) | (16T) | (49T) |
| (\beta=(4-T)/72) | (18+5T) | (228+316T) |
| \\(b^{CM}_{p-1}=\beta^{-1}b_{p-1}\\) | (18+17T) | (131+262T) |
| (A_pb_{p-1}) | \\(18+5T=\beta\\) | \\(228+316T=\beta\\) |
| (A_pb^{CM}_{p-1}) | (1) | (1) |
| quartic product factor | (-1) | (-1) |
| \\(\Phi_{xx}\pmod p\\) | (9) | (221) |
| \\(\Phi_{xx}/72\pmod p\\) | (12) | (288) |
| \\(L_2^{\rm low}\\) | (3) | (197) |
| \\(L_2^{\rm mid}\\) | (18) | (212) |
| (V_{4m}) | (10) | (252) |
| (q_m) | (12) | (13) |
| \\(\sum K_rH_{m+r}^{\rm tail}\\) | (1) | (15) |
| \\(S_{\rm mid}\\) | (2) | (157) |
| \\(S_{\rm low}\\) | (18) | (252) |
| \\(S_{\rm low}+S_{\rm mid}\pmod p\\) | (1) | (36) |
| \\(\mathcal R_m\pmod{p^2}\\) | \\(202\pmod{361}\\) | \\(52416\pmod{139129}\\) |
| \\(Q_p/p^2\pmod{p^2}\\) | \\(221\pmod{361}\\) | \\(65844\pmod{139129}\\) |
| \\(\Delta_p\pmod{p^2}\\) | \\(88\pmod{361}\\) | \\(11759\pmod{139129}\\) |
| (\\(\Delta_p-\mathcal R_m\\)/p\pmod p) | (13) | (264) |
| ((W_p-p)/p^3\pmod p) | (12) | (228) |

The final two rows satisfy

\[
13=12+1\pmod{19},
\qquad
264=228+36\pmod{373},
\]

as required by the second-reflection identity. Also \\(3+18+10=12\pmod{19}\\) and \\(197+212+252=288\pmod{373}\\), matching \\(\Phi_{xx}/72\\).

The executable checker verifies the E3 coefficient identity at (p=13,19,37,43,61,67,211,373), and independently recomputes the \\(\Phi_{xx}\\)/middle dual-observer values at (p=19,373). The existing D25 second-reflection checker remains the evidence for the low/high (d_i,v_a) port and its 77-prime finite window.

## 6. BRC / P000 observer audit

- Population/carrier: the original E3 identity and opposite branches, the CM eigenbasis, the full low/middle/high coefficient bands, and the signed cutoff terms.
- Readouts kept separate: (A_pb_{p-1}) in (mathbb F_{p^2}); the normalized CM companion coefficient; the quartic-twisted Proposition-16 product; \\(L_2^{\rm mid}\\); \\(S_{\rm mid}\\); \\(S_{\rm low}\\); \\(\Phi_{xx}\\); and \\(\Delta_p-\mathcal R_m\\).
- Future operations: quartic coordinate transport, Frobenius/Cartier action, formal de Rham quotient, and the native H0/B0 divided-power observer.
- Information not erased: the \\(T\mapsto-T\\) conjugation, branch identity, Laurent principal part, CM eigenline normalizer \\(\beta\\), twist factor, signed cutoff, and the distinct low/middle/high valuation sources.
- No identification of \\(S_{\rm mid}\\) with the E3 second-kind coefficient is claimed. Such a map needs its own exact observer-factorization certificate.

The external coefficient field is not reinterpreted as a native X6 spatial plane; this is an arithmetic/formal-cohomology calculation. P000 and the active Heartbeat worldview are unchanged.

## 7. Exact remaining frontier

The new all-prime E3 coefficient identity and the paired middle-band observer are complete as author-side mathematics. The mother target remains open:

\[
\Delta_p-\mathcal R_m\equiv0\pmod p,
\qquad
W_p\equiv p\pmod{p^3}.
\]

Next exact action: derive the **two individual off-diagonal entries**, not only their product, of the quartic-twisted ([-p]) semilinear CM exchange in the original E3 eigenbasis at (p=373), then cross-check at (p=19). Compare that matrix's actual divided-power coefficient port with the fixed native H0/B0 `[X]U` observer. Do not substitute the formal E3 coefficient product or the K-H scalar for the native benchmark.

The native support request `#1559` remains open. The task publication owner remains unassigned. No claim, Source session, Source checkpoint, Result admission, freeze, or native H0/B0 execution was created in this run.

## 8. Provenance and status

Prior exact inputs consumed:

- D25 original-E3 CM 3-isogeny/eigenbasis note;
- D25 identity-branch/principal-part repair;
- D25 original second-kind coefficient note;
- D25 three-band local-jet theorem;
- D25 second-reflection mixed-band theorem and its 77-prime checker;
- frozen taskbook at `c47e13e4aba0e006366f989d6334d443f6333ae3`.

External source: Chisholm, Deines, Long, Nebe and Swisher, “p-Adic Analogues of Ramanujan Type Formulas for 1/π” (2013), Proposition 16 and the d=3 quartic-twist/Frobenius-lift discussion in §4.3. The paper's d=3 model is (E_3(t):y^2+xy+(t/27)y=x^3); its quartic twist and ([-p]) lift are the hypotheses used here.

- Proof status: `AUTHOR_SIDE_PROVED`, conditional only on the cited published Proposition-16 d=3 lift and the exact D25 CM/branch identities.
- Finite arithmetic: `EXACT_8_PRIME_E3_CHECKED`; `EXACT_P19_P373_DUAL_OBSERVER_CHECKED`.
- Review/admission: `UNREVIEWED / NOT_ADMITTED`.
- Native benchmark: `NOT_EXECUTED`.
- Researcher identity: `NOT_VERIFIED`; logical lane key is the stable conversation ID above, not a server-issued Researcher-ID.
- Activity registration: `PENDING` because the Source backend did not return a verified session/Researcher authority.
- Source request: `onhour11-20261106-1400-exact-research-lane-continuation` was read/reconciled once; Source returned `BACKEND_IDENTITY_OR_VERSION_MISMATCH / STATUS_DATABASE_UNAVAILABLE`, `operation_sent=false`. Site status remains `CONFIGURED_NOT_LIVE_VERIFIED`, with `research_authority_granted=false`.
