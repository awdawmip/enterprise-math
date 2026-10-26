# D25/LIFT auxiliary Ward: all finite-field geometric-weight seam resonances are simple

Date: 2026-10-26. Status: **SOURCE-NEUTRAL PORTABLE AUTHOR MATHEMATICS / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / NATIVE_SYNC_DEBT**. This is not a canonical Source task checkpoint, active CLAIM, authorized OPEN, Result, independent review, native H0/B0/CM Frobenius experiment or proof of the original LIFT/JT2 target.

Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, immutable publication `TP2-B6F4FC938FF94941C1B7`, unchanged frozen scientific Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Original objective: `Delta_p ≡ R_p (mod p)` for all primes `p ≡ 13,19 (mod24)`, or a valid strict reduction / exact counterexample.

## Existing evidence consumed, without recredit

* `research_notes/portable_direct/20261026_hourly_d25_ward_seam_resonance_binomial_r11.md`: authentic corrected-Clausen auxiliary Ward source law, geometric weight `2^n`, original p=733 seam resonance.
* `research_notes/portable_direct/20261026_offphase_d25_ward_observer_cokernel_hensel_source_neutral.md`: all-weight Ward cokernel; p=733 rank-moment value 211; exact unique Hensel root in residue class 2, `z≡155810880 (mod733³)`.
* `research_notes/portable_direct/20261026_offphase_d25_rank_jet_universal_seam_source_neutral.md`: earlier **special weight** `z=2` scalar/rank-jet identity. Reproducing this specialization is NOT claimed as new work.
* Original Source-verified D25 progress, UR/JT0 and labelled J/E/infinity/high-high sectors remain distinct, without new credit. Shared author/control context is disclosed; no independent referee pass is claimed.

## New theorem — squarefree resonance for every geometric weight

Let `p=6m+1≥7` be prime, `M=2m−1`, `k=F_p`, and for `0≤t≤M` put
[
c_t=inom{2t}{t}4^{-t}in k^	imes,qquad
P_M(x)=sum_{t=0}^{M}c_t x^t,qquad
A_p(z)=P_M(z^{-1}).
]
For the inherited Ward cokernel functional
[
chi_p(w)=w_0+sum_{t=1}^{M}c_t w_{-t},
]
the geometric and first rank-moment observers are
[
chi_p(z^n)=A_p(z),qquad
chi_p(nz^n)=zA'_p(z).
]

**(1) Differential certificate.** Since `2(t+1)c_(t+1)=(2t+1)c_t`, coefficient comparison yields the exact polynomial identity in `k[x]`
[
oxed{2(1-x)P'_M(x)-P_M(x)=-(2M+1)c_Mx^M.}	ag{1}
]
All coefficients below degree `M` cancel, and the displayed last coefficient remains.

**(2) Every resonance is simple.** Here `2M=4m-2<p`, so `c_M` is a p-unit, and `2M+1=4m-1` is not divisible by `p=6m+1`. Moreover `P_M(0)=1` and substitution `x=1` into (1) gives `P_M(1)=(2M+1)c_M≠0`. If `P_M(a)=P'_M(a)=0` in an algebraic closure, (1) forces `a^M=0`, hence `a=0`, a contradiction. Consequently
[
oxed{gcd(P_M,P'_M)=1.}
]
The degree-`M` polynomial has `M` distinct algebraic roots, none at `0` or `1`. Every `A_p` root in an extension of `F_p` is a simple unit root.

**(3) Explicit scalar/moment obstruction for every unit z.** Changing variable `x=z^{-1}` in (1) gives
[
oxed{2(z-1)chi_p(nz^n)+chi_p(z^n)=(2M+1)c_Mz^{-M}.}	ag{2}
]
Therefore, at **every** geometric Ward scalar resonance `z` in any residue extension,
[
oxed{chi_p(z^n)=0 Longrightarrowchi_p(nz^n)=rac{(2M+1)c_M}{2(z-1)z^M}
e0.}	ag{3}
]
The value `z=1` cannot be a resonance. In particular, no scalar-only resonance preserves the rank-moment observer under the declared operation `z∂_z`. For `z=2`, (2) reduces exactly to the **previously established** `χ_p(2^n)+2χ_p(n2^n)=4(M+1)binom(2M+2,M+1)/8^(M+1)`; this specialization is reused, not re-proved as new.

**(4) Hensel classification without assuming roots exist.** Retain the exact p-integral finite-Gauss Ward scalar
[
X_p(z)=1+(p+1)sum_{t=1}^M a_t(p)z^{-t},quad
a_1(p)=rac{1}{p+2},quad
a_t(p)=a_{t-1}(p)rac{p+2t-1}{p+2t}.
]
It reduces to `A_p(z)` modulo `p`. At any `z_0∈F_p×` with `A_p(z_0)=0`, (3) implies `X'_p(z_0)` is a p-unit. The ordinary Hensel lemma therefore gives **exactly one** `z∈Z_p×` with `X_p(z)=0` and `z≡z_0 (mod p)`. The same holds over the unramified Witt lift of any finite residue-field extension. This says nothing about the number of `F_p`-rational roots, nor about actual crystalline Frobenius data.

## Exact author-side arithmetic certificates

An integer-only Python checker independently constructs modular binomial coefficients and tests (2) for **all 36,588 nonzero residues** across the 80 primes `p<1000, p≡1 (mod6)`. It finds 77 `F_p×` scalar roots, each with a nonzero moment and derivative. The universal assertion above rests on the symbolic proof, not on the finite test.

At `p=733`, `M=243`, exhaustive evaluation finds exactly the two roots `{2,649}`. The scalar and rank-jet data are `χ_733(2^n)=0`, `χ_733(n2^n)=211`, `X'_733(2)=472`, and `χ_733(649^n)=0`, `χ_733(n649^n)=330`, `X'_733(649)=572`. The pre-existing class `z≡2` root `155810880 (mod733³)` is preserved, not recredited. **New exact second-branch certificate:**
[
oxed{z_{649}equiv 85677pmod{733^2},quad
z_{649}equiv334816724pmod{733^3},quad
X_{733}(334816724)equiv0pmod{733^3}.}
]
The two Hensel digits for the class `649` are `116,623`. Other modular censuses: `p=13`: no unit roots; `p=19`: `8,13,17`; `p=373`: `311`, moment 24. These are author checks; independent replication is outstanding.

## BRC interface, strict source separation and unfinished work

`T0_BRC/T6_OPERATION_SAFE_QUOTIENT`: **COMPOSE_APPLIED** — the scalar and first moment are different ports; relation (2) gives their exact source-preserving coupling for the specified `z∂_z` future operation. `T1_SCALE_ENUMERATION_VALUATION`: **REUSE_APPLIED** via the factorial p-unit certificate. `n` is an auxiliary signed rank, `z` an observer parameter, neither a primitive Heartbeat World X6 coordinate. No physical conclusion, custom axiom, new BRC family or mathematical acceptance is inferred.

**Still missing:** a valid type- and source-preserving bridge from original labelled Hasse/CM/Frobenius ports to the auxiliary Ward observers, including separate J/E, positive infinity, ordered high-high, original-class H0/B0 divided-power module, `[X]U mod p²`, semilinear direction, `eta`, `kappa` and `Delta_p-R_p`. No direct native CLAIM/OPEN/checkpoint or independent review is claimed here. A current-input continuation seed must retain `frontier_notes.completed_units=[]`; this new author note is never predecessor-completed research.

UR V2 four-file byte bundle (historically 94,687 bytes, SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`) remains unrecovered. Only an authentic matching original can satisfy restoration; no unverified reconstruction should be called recovery. Preserve prior native completed units, actor histories and frozen Source pin.

Next discriminating action: test whether the original signed source-labelled LIFT scalar/rank input factors through (2) without erasing future-sensitive provenance, and obtain actual authenticated H0/B0 module/Frobenius data. Native writer/provenance/checkpoint remain separate lawful operations.
