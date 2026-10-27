# D25/LIFT — Universal unit-safe Ward face repair and authentic p=733 rank-jet boundary

Date: 2026-10-26. Requested TASK_RESEARCH lane: `chatgpt-research-hourly-enterprise-math-20260923`, distinct from CONTROL_PLANE_MAINTENANCE. Source task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`. Frozen science pin `c47e13e4aba0e006366f989d6334d443f6333ae3` is **unchanged**.

**Status: AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.** This is an auxiliary corrected-Clausen source calculation, not a native authorized Research checkpoint, source Claim, original-class CM/Frobenius experiment, admitted WZ relation or independent review. No new owner/session/claim identity is inferred.

## Exact inherited inputs and genuine new question

Consume without recrediting:
- `20261026_hourly_d25_ward_torsion_hensel_observer.md`: the Smith invariant and mod-p obstruction of the *free labelled* Ward carrier, including p=733 observer resonance.
- `20261026_hourly_d25_negative_orientation_source_adjoint_r11.md`: geometric-weight **negative-only** Green adjoint.
- `20261026_hourly_d25_diagonal_rank_moment_closed_recurrence_r11.md`: genuinely coupled `k-1,k-2` Hasse source `J_n^{ab}+E_n^{ab}` and both finite endpoint terms.
- `20261026_hourly_d25_ward_factorial_boundary_r11.md`: the actual p-unit (1,2) left Hasse endpoint.

**Unfinished subquestion now resolved:** Construct an *arbitrary-observer, both-orientation*, unit-safe Ward source operator with exactly one explicit face coordinate; prove a constructive source-only criterion, then test whether the known **free** p=733 rank-jet obstruction genuinely acts on a nonzero Hasse endpoint (not just on a formal free vector).

For any prime (p=6m+1ge7), write (M=2m-1, L=-M, R=mathbb Z_{(p)}). The source carrier is (Y_L,ldots,Y_M) with (Y_{M+1}=0), oriented edge
[
S_n=(p-2n)Y_n-(p-2n-1)Y_{n+1},qquad Lle nle M.
]
In the actual corrected-Clausen family, (Y_n^{ab}=M_n^{ab,1}-(p-n)M_n^{ab,0}/2) and (S_n^{ab}=J_n^{ab}+E_n^{ab}). The ordered ((j,ell)) population, six Hasse labels, signed rank, first moment, two cutoff traces and positive/infinity observer are not collapsed.

## Theorem A — all-weight, both-orientation exact face-repair formula

Fix **arbitrary** (w=(w_L,ldots,w_M)in R^{2M+1}), and set (eta_0=0). Define coefficients without ever dividing by p:
[
egin{split}
eta_{n-1}&=rac{(p-2n)eta_n-w_n}{p-2n+1}
quad(n=0,-1,ldots,L+1),\
eta_n&=rac{w_n+(p-2n+1)eta_{n-1}}{p-2n}
quad(n=1,ldots,M),\
delta_w&=w_L-(p-2L)eta_L.
end{split}
]
Every denominator in these recursions is a (p)-unit. The following equality holds **exactly over R**, with all the positive-rank sources present:
[
oxed{displaystyle
sum_{n=L}^{M}w_nY_n
=sum_{n=L}^{M}eta_nS_n+delta_wY_L.}	ag{A}
]

**Proof.** In (sumeta_n S_n), the coefficient of each (Y_n) for (L<nle M) is ((p-2n)eta_n-(p-2n+1)eta_{n-1}); both recurrences make it (w_n), including (n=0) since (eta_0=0). The (Y_{M+1}) term vanishes by the genuine right cutoff, whereas (Y_L) has coefficient ((p-2L)eta_L). Add (delta_wY_L). QED.

This is more general than the earlier (2^n) negative-only adjoint: arbitrary signed/rank-jet weights, both (nle0) and (n>0), exact (p)-unit transport, and one explicitly retained genuine left face.

## Theorem B — exact residue-to-face map and a constructive integrality test

Put (c_t=inom{2t}{t}4^{-t}pmod p), (0le tle M), so (c_M
e0), and
[
Phi_p(w)=sum_{t=0}^{M}c_t w_{-t}pmod p.
]
Then
[
oxed{delta_wc_MequivPhi_p(w)pmod p.}	ag{B}
]
In particular the face is p-divisible if and only if the free-observer obstruction vanishes.

**Proof.** In (A) reduce modulo p and substitute the known Ward kernel vector (v_{-t}=c_t, v_n=0 (n>0)), for which (S(v)=0). The left is (Phi_p(w)); the right is (delta_wc_M). This uses a free-module test vector **only to characterize the adjoint**, not to assert the vector comes from Hasse jets. QED.

There is also an **explicit source-only lift when (Phi_p(w)=0)**, not merely an abstract Smith-form existence claim. Define the unit
[
g_p=prod_{n=L}^{-1}rac{p-2n}{p-2n-1}in R^	imes.
]
If the chosen center is instead (eta_0=tin R), and both recurrences are extended with that center, its face changes exactly as
[
delta_w(t)=delta_w(0)-p,g_p t.
]
When (Phi_p(w)=0), formula (B) shows (delta_w(0)in pR). Thus setting
[
oxed{eta_0=delta_w(0)/(p g_p)}
]
makes the face vanish **as an exact p-local identity**. Conversely, if (Phi_p(w)
e0), the kernel test rules out any p-integral source-only factorization on the free carrier. This proves the all-weight criterion constructively with its one-digit precision cost; it never divides by p before the numerator is proven p-divisible.

## Theorem C — the authentic Hasse endpoint detects rank-jet resonance at p=733

For the actual truncated corrected-Clausen carrier, the leftmost pair is uniquely (j=2m,ell=1), hence
[
Y_L^{ab}=-2m,u_{a,2m}u_{b,p-1}.
]
The inherited factorial proof gives
[
Y_L^{02}=Y_L^{03}=Y_L^{04}=0quad	ext{exactly},qquad
oxed{
Y_L^{12}equiv
rac{4(-1)^m}{inom{2m}{m}(2m+1)(m+1)}
inmathbb F_p^	imes.}	ag{C}
]
Therefore applying (A) to **genuine** (S_n^{12}=J_n^{12}+E_n^{12}) gives a nonzero face precisely when (Phi_p(w)
e0), whereas the a=0 Hasse channels admit the same source formula with zero face *for their actual state* even if the free-module obstruction is nonzero. These are different quantified statements; the Hasse coincidence is not an unrestricted row-lattice identity.

For (p=733), (M=243), exact independent recurrence calculations modulo (p^2) give
[
c_M=20,quad Y_L^{12}=610pmod{733}.
]
For the three Ward-**Y** observers (w_n=2^n, n2^n, (1-6n)2^n), the first-digit figures are:
 
| (p) | observer (w_n) | (Phi_p(w)) | (delta_w) | genuine (delta_wY_L^{12}) |
|---:|---|---:|---:|---:|
| 13 | (2^n) | 9 | 8 | 7 |
| 13 | (n2^n) | 3 | 7 | 11 |
| 13 | ((1-6n)2^n) | 4 | 5 | 6 |
| **733** | (2^n) | **0** | **0** | **0** |
| **733** | (n2^n) | **211** | **487** | **205** |
| **733** | ((1-6n)2^n) | **200** | **10** | **236** |

All entries in their respective rows are modulo (p). For 733, (delta_{mathrm{signed}}c_M=10cdot20=200mod733), and the **authentic** left source face is (10cdot610=236mod733), nonzero. Thus the free rank-jet sensitivity discovered previously **survives on the real (1,2) Hasse boundary**, even though fixed geometric weight (2^n) is resonant and has no first-digit face. This is a **new labelled-source residue certificate**. The geometric face can still reappear at the next digit; the two statements do not conflict.

**Scope:** the signed weight here measures (Y_n^{12}), not the original Clausen mass (M_n^{12,0}). This does **not** prove the six-channel coupled WZ cancellation is impossible; other genuine Hasse relations, positive/infinity sources and ordered high–high terms can still participate. No unproved substitution from Ward-Y to original CM observables is made.

## Exact independent checks

Companion `20261026_hourly_d25_universal_ward_face_repair_rank_jet_r13_check.py` computes Hasse jets through degree 4 modulo (p^2) from the original `k-1,k-2` recurrence, constructs all 25 ordered moment channels, and **separately** reconstructs each genuine (J_n+E_n) including both finite cutoff sources. It then checks equation (A) for six actual Hasse channels and three observers, the exact residue condition (B), the a=0 face vanishing, the p-unit (1,2) boundary, and the constructive central correction when (Phi=0).

**Executed author checks: PASS 23 target primes** (all 22 primes (pequiv1mod6) in (7le ple211), plus (733)); 11,742 separate authentic (J+E) source-cell checks, 414 channel/observer exact modular-(p^2) adjoint checks, and additional endpoint/residue/source-factorization checks. These are mathematical author tests, not a native CM run, independent Driver replication, Lean formalization, original-class bridge or mathematical admission.

BRC **COMPOSE_APPLIED**: preserve the ordered Hasse family, actual (k-1,k-2) source, signed/rank-jet observer, left-face repair, p-valuation and separately oriented infinity/high–high populations. Exact compression is valid only for declared observer and genuine future couplings. These auxiliary ranks are not P000 native spatial coordinates; the locked P000 and ACTIVE residual-fidelity worldview remain unchanged.

## Native control and exact next research unit

A fresh exact continuation read was attempted as `researchhourly-20261026-2021-continuation-r13`. Transport returned `INVALID_ARGUMENT / CONTROL_QUOTA`, and subsequent `em_control_result` for that same request returned `CONTROL_REQUEST_NOT_FOUND`; this does **not** prove a new Source state or permission. Prior Source checkpoint and old session/staging remain historical protected state; no session transition, CLAIM, OPEN, native checkpoint or Result occurred. Existing control owner: `awdawmip/enterprise-math#1558`.

**Next smallest mathematical unit:** In the *fixed original* (z=2) six-channel Clausen scalar, substitute the genuine (J/E) sources and all six mass/moment reconstructions into (A), retaining the p13 non-resonant ((1,2)) face, the p733 rank-jet face (236), both finite cutoff traces, separately computed positive infinity (Z^+) and ordered high–high (H_p). Determine whether the resulting (k-1,k-2) coupled source equations supply a cancellation, or give a labelled nonzero residual. Separately unresolved original-class (H_0/B_0), ([X]Umod p^2), Frobenius (eta), (kappa), (Delta_p-R_p), native experiment and independent review keep D25/LIFT/JT2 **OPEN**. Do not recredit prior completed/native units.