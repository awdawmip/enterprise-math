# D25/LIFT — original weighted-216 middle band: exact two-digit parameter jet and Wilson quotient

2026-10-27, 12:00+08. Logical Research lane: `chatgpt-research-onhour-enterprise-math-20260923`, **distinct** from maintenance `chatgpt-hourly-enterprise-math-20260921`.

**STATUS: AUTHOR-SIDE / NEW HAND-PROVED ALL-PRIME BAND IDENTITY / EXECUTED 11-PRIME EXACT TERM-CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / NOT_SOURCE_CHECKPOINT / NOT_NATIVE_H0B0 / NOT_LIFT_PROOF.**

Mother objective: `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`. Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific Source pin **`c47e13e4aba0e006366f989d6334d443f6333ae3` unchanged**. Consume D24 first-digit frozen `RR-AC9B3BA5BD277CE043F5` and reviewed `DR-610CB297F3195E8F2D9E`, not re-prove UR.

## Original object, exact theorem

For any prime (p=6m+1>3), in (\mathbb Z_{(p)}) set
[
q_n=rac{(2n)!(3n)!}{(n!)^5,216^n}
=rac{inom{2n}{n}^2inom{3n}{n}}{216^n},quad
w_n=(6n+1)q_n,quad W_p=sum_{n=0}^{p-1}w_n.
]
All divisions by (p) below precede reduction. Put (n_0=2m+1=(p+2)/3). The **two-digit base coefficient**
[
mathcal B_p=rac{q_{n_0}}p
=rac{(2n_0)!,((3n_0)!/p)}{(n_0!)^5,216^{n_0}}pmod{p^2}
]
is p-integral. Define a finite parameterized polynomial
[
mathscr J_p(z,t)=sum_{k=0}^{m-1}
rac{(7/6+t)_k(1+t)_k(4/3+t)_k}{(5/3+t)_k^3}z^k,quad z=1/2.
]
For (0le k<m), define the **p-unit** rational coefficients and their parameter derivative:
[
c_k=2^{-k}rac{(7/6)_k(1)_k(4/3)_k}{(5/3)_k^3}pmod{p^2},quad
d_k=sum_{j=0}^{k-1}left[rac1{j+7/6}+rac1{j+1}+
rac1{j+4/3}-rac3{j+5/3}ight]pmod p
]
with (d_0=0). Define separately the signed weighted and derivative **ports**
[
J_w=sum_{k<m}(6k+5)c_kpmod{p^2},quad
J_0=sum_{k<m}c_kpmod p,quad
J_{t,w}=sum_{k<m}(6k+5)c_kd_kpmod p.
]
Then the **algebraic identity for every prime (pequiv1pmod6), (p>3)** is
[
oxed{sum_{n=2m+1}^{3m}w_nequiv
pmathcal B_pleft[J_w+rac p3(6J_0+J_{t,w})ight]pmod{p^3}.}	ag{M}
]
This preserves the weight derivative (6J_0) separately from (J_{t,w}); the (mathcal B_p) factor cannot be reduced merely modulo p.

There is also an explicit Wilson-quotient version: with
(mathfrak W_p=((p-1)!+1)/pinmathbb Z),
[
oxed{mathcal B_pequiv
-rac{2(4m+2)!}{((2m+1)!)^5,216^{2m+1}}
left[1+pleft(rac32-mathfrak W_pight)ight]pmod{p^2}.}	ag{W}
]

## Proof — genuine original coefficient, not a fitted expression

**Valuation/units.** For (2m+1le nle3m=(p-1)/2), (3nin[p,2p)), (2n<p), (n<p), so (v_p(q_n)=1). The denominators of (mathcal B_p), (c_k,d_k) are p-units for (k<m): the factors (j+7/6), (j+1), (j+4/3), (j+5/3) are nonzero modulo p for (0le jle m-2). No use of a spurious (p^{-1}) in (mathbb F_p).

**Exact ratio.** The original factorial identity is
[
q_{n+1}/q_n=
rac{(2n+1)(2n+2)(3n+1)(3n+2)(3n+3)}{216(n+1)^5}.
]
Insert (n=n_0+k=(p+2)/3+k), cancel factors without division by any weighted term:
[
rac{q_{n_0+k+1}}{q_{n_0+k}}=
rac12rac{(k+7/6+p/3)(k+1+p/3)(k+4/3+p/3)}
{(k+5/3+p/3)^3}.
]
For exactly (k=0,ldots,m-1), this telescopes into the kth coefficient of (mathscr J_p(1/2,p/3)), with initial factor (q_{n_0}).

**Parameter jet.** In the p-local ring, set (t=p/3); Taylor expansion of the finite rational coefficient at (t=0) gives (c_k(1+td_k)pmod{p^2}). Terms quadratic in t vanish modulo p². Meanwhile the *original weight*, exactly, is (6(n_0+k)+1=6k+5+2p=(6k+5)+6t). Thus **termwise**
[
rac{w_{n_0+k}}pequiv
mathcal B_pleft[(6k+5)c_k+rac p3ig(6c_k+(6k+5)c_kd_kig)ight]pmod{p^2}.
]
Summing the (m) equalities proves (M).

**Wilson correction.** Since (3n_0=p+2),
[
rac{(3n_0)!}{p}=(p-1)!(p+1)(p+2).
]
Using the exact integer definition ((p-1)!=-1+pmathfrak W_p), this factor equals (-2+p(2mathfrak W_p-3)pmod{p^2}); (2n_0=4m+2<p) and (n_0<p), hence (W). Neither (M) nor (W) relies on finite numeric induction.

## Composition with **previously proved** high band; exact remaining target

The preceding author certificate `research_notes/portable_direct/20261027_onhour_d25_weighted216_high_band_hypergeometric_jet.md` at commit `aa26c73c44f7090fe1d52551b670f8e7f302566f` proves
[
sum_{n=3m+1}^{4m}w_nequivrac{4p^2}{9}left(rac6pight)K_ppmod{p^3},
quad
w_nequiv0pmod{p^3};(n>4m).
]
Combining with (M), **with no change to W's definition**, gives
[
oxed{W_pequiv
sum_{n=0}^{2m}w_n+
pmathcal B_p[J_w+	frac p3(6J_0+J_{t,w})]+
	frac{4p^2}{9}left(rac6pight)K_ppmod{p^3}.}	ag{T}
]
The previously derived original Source-port equality is
(Delta_p-R_pequiv(W_p-p)/p^2mod p) for both target classes (pequiv13,19pmod{24}).
The character ((6/p)) is **−1 for class 13 and +1 for class 19**. UR supplies (W_pequiv ppmod{p^2}), so dividing the whole right side of (T) after subtracting p is legal. **The all-prime vanishing of that quotient has not been proved; no LIFT/JT2 closure is claimed.** This is an exact *direct weighted-216* middle-band complexity reduction, not a new Clausen-positive-mass assertion.

## Reproducible executed exact certificate

Companion code `research_notes/portable_direct/d25_weighted216_middle_parameter_jet_20261027.py` was actually executed, using Python standard library exact integers, on primes `7,13,19,31,37,43,61,67,73,211,373`. For **every** such prime it compares **every individual original weighted middle term** modulo p² after dividing by p with its independent Pochhammer parameter-jet prediction; independently checks base coefficient (W); and recomposes all three original bands with the direct full (W_pmod p^3). No floating point. Finiteness limits the checks; proof above establishes (M) universally.

Last execution marker `D25_WEIGHTED216_MIDDLE_PARAMETER_JET_PASS`; deterministic JSON SHA256:
`b10959246e10f60a230b3e4e9ca020a5829c31ae263023d72ccd578707ca92c5`.

At **p=373**, (m=62), (n_0=125), (p^2=139129), (p^3=51895117):
[
mathcal B_{373}=93197pmod{139129},quad
mathfrak W_{373}=224pmod{373},quad
J_w=11471pmod{139129},quad
J_0=55, J_{t,w}=104pmod{373}.
]
[
sum_{n=125}^{186}w_n/373equiv103721pmod{139129},quad
sum_{n=125}^{186}w_nequivoxed{38,687,933}pmod{51,895,117}.
]
The *original* full series parts are low ([0,124]) (28,094,360), middle ([125,186]) (38,687,933), high ([187,248]) (37,008,314), each modulo (51,895,117); their sum is (373) modulo (51,895,117). Separate target branch regressions: at p=13, (low,mid,high)=(780,1937,1690) mod 2197; at p=19, (5662,4826,3249) mod 6859. These are falsification checks, not native data or universal proof.

## BRC, authority, missing evidence, continuation

**BRC resolution COMPOSE_APPLIED.** Population: original signed weighted-216 term indices, p-adic valuation strata, separately labeled classes 13/19. Exact carrier: (q_n,w_n), index bands, Wilson quotient, parameter derivative, weight derivative, signed Legendre branch, cutoff R. Observer: original ((W_p-p)/p^2mod p) only after p³ composition; future operation: band summation and source-preserving (R)/(Delta) readout. Formula (M) proves a safe quotient for that band at that precision, but dropping derivative/weight jets, residue signs, source ports, or division order is not safe. Auxiliary two-coordinate hypergeometric algebra is **not** a reduction of the ACTIVE P000 native X6/three-dimensional slice.

The immutable accepted UR/JT0 Result is consumed, not re-credited. This new file is merely author-side, independently unreviewed, not a role-bound Source checkpoint or native result. Original experimental **highest-priority missing unit** is the same-class H0/B0 divided-power ([X]Umod139129) at p373 with actual rank, Frobenius semilinear direction/eta normalization, signed Green/Hesse, original κ and Δ−R, tracked by **`awdawmip/enterprise-math#1559` OPEN/PENDING_OWNER/NOT_EXECUTED**. Neither the field jet nor a surrogate Hesse model performs this experiment. Responsible path: verified original Source Task owner / authorized native executor / CodeX native maintainer, **no owner confirmed**; acceptance requires version-pinned raw inputs/outputs and independently reproduced operator normalization.

Research lane's historic successful recovery request `research-onhour-20261027-0501-recovery-r13` (bridge #6575) shows old session pointer `MCP-de3e5bafb24f43f4a5e6285e7601676a`, but does **not** grant Source authority or currently possessed capability. Prior dispatch `research-onhour-20261027-0507-dispatch-r13` (#6576) ended **FAILED/TimeoutExpired**. This turn's read-only exact continuation request `research-onhour-20261027-1200-continuation-r11` failed pre-admission with `CONTROL_QUOTA`. Own CLAIM/OPEN/run: **NONE VERIFIED**; original target_request_id must be used to reconcile any UNKNOWN effects rather than replay. Old three staging pieces are neutral separate-source archives, not accepted research. Current activity: `REGISTER_PENDING`; no session_key, no claimed Source checkpoint, no new dispatch, and no maintenance conversation identity used.

**Next exact actions:** existing #1559 must obtain an actual authorized original H0/B0 executor and run the p373 benchmark; the own Research lane must regain canonical Source continuation/CLAIM/OPEN before submitting formal checkpoint and before independent Driver review; for mathematical proof seek a full finite transform canceling the intact low + Wilson mid + signed high ports **for all** target primes, never cite finite regression as theorem. No scheduler/Actions/new Task or changes to frozen scientific pin, current owner, timer phase/frequency/enabled/notifications. Parent D25/LIFT/JT2 remains OPEN.
