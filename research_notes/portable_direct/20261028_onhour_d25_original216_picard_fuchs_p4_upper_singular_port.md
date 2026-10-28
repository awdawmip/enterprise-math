# D25 — original 216 finite Picard–Fuchs cutoff anomaly and fourth-digit upper-band singular port

Date: 2026-10-28 Asia/Hong_Kong. Lane: `chatgpt-research-onhour-enterprise-math-20260923` (separate from control maintenance). Classification: **AUTHOR-SIDE / EXACT ALL-PRIME LEMMAS / 27 EXECUTED FINITE CHECKS / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING**. Mother objective: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3` **unchanged**.

## Exact source and target

Preserve the original weighted finite sum and every index/valuation:
[
t_n=rac{(2n)!(3n)!}{216^n(n!)^5}
=rac{(1/2)_n(1/3)_n(2/3)_n}{2^n(n!)^3},qquad
w_n=(6n+1)t_n,qquad W_p=sum_{n=0}^{p-1}w_n.
]
The frozen D25 target remains (W_pequiv ppmod{p^3}) for (pequiv13,19pmod{24}), with the separately pinned original (Delta_p-R_p) interface. The new results are source-faithful *auxiliary scalar* lemmas about the same 216 summands; the D25 proof obligation and native #1559 experiment remain open.

## Theorem 1: sharp finite Picard–Fuchs endpoint, all primes p>3

Let (	heta=z,d/dz), (F_p(z)=sum_{n=0}^{p-1}t_nz^n) in (mathbb Z_{(p)}[z]), and
[
mathcal L=	heta^3-rac z2(	heta+	frac12)(	heta+	frac13)(	heta+	frac23).
]
Then the **exact rational polynomial identity** is
[
oxed{ mathcal L F_p(z)=-	frac12(p-	frac12)(p-	frac23)(p-	frac13)t_{p-1}z^p. }	ag{P1}
]
Moreover, for every prime (p>3),
[
oxed{quad t_{p-1}/p^3equiv-1pmod p,qquad
mathcal L F_p(z)equiv-rac{p^3}{18}z^ppmod{p^4}.quad}	ag{P2}
]
In particular (mathcal L F_p=0pmod{p^3}) **coefficientwise**, whereas the (z^p) obstruction modulo (p^4) has exact valuation 3. The truncated solution of degree at most (p-1) with constant term 1 is the unique such formal solution modulo (p^3) (recurrence coefficient (n^3) is a unit for (1le n<p)). No degree-(<p), constant-1 polynomial satisfies the same homogeneous equation modulo (p^4).

Proof: the adjacent-term recurrence is
[
(n+1)^3t_{n+1}=	frac12(n+	frac12)(n+	frac13)(n+	frac23)t_n.
]
It cancels coefficients of (z^0,dots,z^{p-1}) in (mathcal LF_p), leaving precisely the indicated (z^p) boundary. For (q=1,2) and (0le r<p), Wilson's block congruence is ((qp+r)!/p^qequiv(-1)^q q!,r!pmod p). Thus
[
(2p-2)!/pequiv-1,qquad
(3p-3)!/p^2equiv-1,qquad
((p-1)!)^5equiv-1,quad216^{p-1}equiv1pmod p,
]
giving (t_{p-1}/p^3equiv-1). Substitution in P1 gives (-p^3/18) exactly modulo (p^4). Because (18) is a (p)-unit, this obstruction is nonzero. Uniqueness follows successively from the recurrence; no (z^p) term is permitted in degree (<p). This is independent of the conjectural LIFT.

The weighted final source term has the universal nonzero digit
[
oxed{w_{p-1}/p^3equiv5pmod p.}	ag{P3}
]
Thus the PF approach is boundary-free through the **third** p-adic digit but requires an explicit nonzero boundary coordinate at the **fourth**.

## Theorem 2: fourth-digit exact original upper-band reconstruction, p=6m+1

For every prime (p=6m+1>3), the entire upper band (4m+1le nle p-1=6m) has (v_p(t_n)=v_p(w_n)=3). Set
[
sigma_r=rac{w_{4m+1+r}}{p^3}mod p,quad 0le r<2m,qquad
Omega_p=sum_{r=0}^{2m-1}sigma_rpmod p.
]
Factoring the exact original (2n) and (3n) factorials into Wilson blocks gives
[
oxed{sigma_requiv
-6(2r+1)rac{(2m+1+2r)!(3r+1)!}
{216^{4m+1+r}((4m+1+r)!)^5}pmod p.}	ag{P4}
]
Consequently the **original finite sum**, with no changed cutoff, obeys
[
oxed{W_pequivsum_{n=0}^{4m}w_n+p^3Omega_ppmod{p^4}.}	ag{P5}
]

There is also a reversible *unweighted* lower-to-upper mirror. For (1leellle2m) put (u_ell=t_ellmod pinmathbb F_p^	imes) and (
u_ell=w_{p-ell}/p^3mod p). Apply the previously proved original paired-unit theorem **R2** at the low index (ell), for which (lfloor2ell/pfloor=lfloor3ell/pfloor=0). It yields
[
rac{t_ell t_{p-ell}}{p^3}equiv-rac1{18ell^3}pmod p,
]
and therefore
[
oxed{
u_ellequiv-rac{1-6ell}{18ell^3u_ell}pmod p,qquad
Omega_p=sum_{ell=1}^{2m}
u_ell.}	ag{P6}
]
This actually **consumes** R2, instead of re-proving or replacing it. The low *weighted* digit (ar w_ell) cannot be inverted everywhere: at (ell=m), (6m+1=p) and (ar w_m=0) although (u_m) is a unit. The lost branch is nonzero and has a simple repair:
[
oxed{rac{w_m}{p}equiv u_m,qquad

u_m=rac{w_{p-m}}{p^3}equiv24u_m^{-1}
e0pmod p.}	ag{P7}
]
A weighted-only mirror that discards this particular source label incorrectly loses an actual fourth-digit contribution. This is a concrete BRC joint-observer fiber failure; retaining (u_m) (or (w_m/p)) repairs it. P4 and P6 independently compute each upper digit.

## Executed exact certificate

Companion: `research_notes/portable_direct/d25_216_picard_fuchs_cutoff_p4_guard_20261028.py`. Python standard library integer and modular-unit arithmetic (no floats) was actually run, checking **27 primes** including (5,7,11,13,19,37,211,373). Checks cover every internal Picard–Fuchs polynomial coefficient, the exact nonzero endpoint, independent original binomial terms at selected indices, every (pequiv1pmod6) upper factorial digit, R2 low-to-upper inverse, the singular branch, and original full-sum reconstruction. Actual terminal marker:

`PASS_D25_EXACT_PF_CUTOFF_AND_ORIGINAL_P4_UPPER_PORT`

At (p=373) ((m=62, p^3=51895117, p^4=19356878641)):
[
egin{aligned}
mathcal LF_{373}ert_{z^{373}}&equiv7524791965equiv-373^3/18pmod{373^4},\
u_{62}&=122,quad ar w_{62}=0,quad w_{62}/373=122pmod{373},\

u_{62}&=43=24cdot122^{-1}pmod{373},\
Omega_{373}&=278=235+43pmod{373},\
sum_{n=0}^{248}w_n&equiv16762123164,qquad
W_{373}equiv11832087049pmod{373^4}.
end{aligned}
]
Discarding the singular branch would drop (43cdot373^3=2231490031) modulo (373^4). This is an **exact information-loss witness**, not an inference of universal LIFT.

## BRC / native X6 / continuation boundary

Carrier: ((p,n,6n+1,t_n,w_n,v_p(t_n),v_p(w_n),nleftrightarrow p-n,	ext{upper digit},	ext{special }ell=m,	ext{cutoff})). Declared observer: original scalar (W_pmod p^4); permitted operations are signed addition, unit inversion only on (u_ell), original factorial valuation and PF differential action. The unweighted repair retains the otherwise lost zero-weight branch. The external scalar model is only a restricted auxiliary observer; native Heartbeat X6 is six-dimensional Cell space with separately typed time, and no full-X6 or native Frobenius assertion is made.

Research lane has **no verified current winning Source CLAIM/run**. This turn's Site status (2026-10-28) reports `research_authority_granted=false`, `write_relay_enabled=false`; exact historical #6575/#6576 lookup in this Site returns `CONTROL_REQUEST_NOT_FOUND` (different transport namespace), so neither request is reissued. No Source Result, Research-Activity, freeze, or other role-bound mutation is claimed. The three historical staging sources remain independent. Correct state: `AUTHOR-SIDE / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING / UNREVIEWED / NOT_ADMITTED`.

**NEXT SCIENTIFIC P3 FRONTIER:** original (p^3) cancellation remains R9, i.e. proving or falsifying the full bulk-quotient versus middle/high reciprocal sum for both (pequiv13,19pmod{24}). P1 supplies a homogeneous finite PF equation through this precision; a candidate certificate must actually evaluate ((1+6	heta)F_p(1)), not just solve the operator. **NATIVE PRIORITY:** existing issue #1559 awaits an authorized native (p=373) H0/B0 divided-power run with ([X]Umod139129), rank, semilinear Frobenius/eta, signed odd Green/Hesse, (kappa) and (Delta_p-R_p). No owner or run is claimed by this note. Do not replace the native benchmark with P1–P7. Preserve source pin and mother objective; no scheduler/Actions changes.
