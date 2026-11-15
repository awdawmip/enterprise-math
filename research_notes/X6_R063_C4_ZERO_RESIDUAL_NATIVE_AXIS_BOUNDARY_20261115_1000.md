# X6 / R063 — C4 zero-residual domain and signed axial endpoints (2026-11-15 10:00)

**Task:** RS-X6-LEGACY-PLANE-RECONCILIATION / TP2-B4A441B23DA3159232C2. **Author:** EM-X6-FB6990, original session MCP-082892eb480e45dea6d4b9fcc0491034. **Scientific pin:** P000 V5, `awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03`; compare frozen historical R063 branch `research/r063-stage0-path-valued-sqrt-2500`. This is an exact source-level domain correction and independently checked boundary computation, not the original Stage 0 benchmark replay. **State:** AUTHOR-VERIFIED / UNREVIEWED / NOT_ADMITTED.

## Direct source boundary: C4 cannot evaluate norm zero

The exact original R063 program is a 440-byte loader `scripts/r063_stage0_validate_path_valued_sqrt_2500.py`, Git blob `b4e000a6377f2858ae434eb0eecd0c25c33e8592`. Its immutable five parts include:

* `scripts/r063_stage0_checker_parts/part00.inc`, Git blob `4a69c4d698887bce56323f393cb979609ce4ab0a`: `factor_integer(n)` raises `ValueError("factor_integer requires n >= 1")` for `n<1`; `gaussian_norm_root_records(M)` starts by calling `factor_integer(M)`.
* `scripts/r063_stage0_checker_parts/part01.inc`, Git blob `913078c642b8995bfc135ef0350912387a17cdb8`: `gaussian_norm_root_set(M)` calls `gaussian_norm_root_records(M)`, and `discover_c4(N)` calls `gaussian_norm_root_records(N)`.

Consequently, at the unmodified original source, both `gaussian_norm_root_set(0)` and `discover_c4(0)` raise that `ValueError`. In contrast, the source supports general **positive** integer norms `M>=1` in C4 (including nonsquares), whereas C3 requires a positive integral radius `r` and square norm `r²`. The original R063 `N=2500` direct C4 call is positive and is unaffected. This precise `M=0` contract was misdescribed as "general nonnegative" in the author-side 09:00 residual-lift report; that report's independent `two_squares_factorization(0)` already has a separate correct zero branch.

## Exact native signed-three-axis fiber correction

For any integer `N>=0` and named third native coordinate `c` with `|c|<=floor(sqrt(N))`, write `M=N-c²`. Let the zero-aware Gaussian fiber be

`R2*(M) = {(0,0)} if M=0; R2_C4(M) if M>0`,

where `R2_C4(M)` is obtained from original positive-norm C4 roots and completed by Gaussian unit/sign/order handling. The positive C4 generator is never called at `M=0`.

For positive perfect-square `N=r²`, the zero-residual layers are **exactly** `c=-r,+r`. Each contributes the single signed native endpoint `(0,0,c)`, and its shortest signed-path BRC multiplicity is `B3(0,0,c)=1`. Thus this boundary adds exactly two endpoints and two BRC words relative to a construction restricted to `M>0`. For a nonsquare `N`, no integral `c` has `M=0`. For `N=0`, the only layer is `c=0`, giving one endpoint and one empty path. These statements follow from `a²+b²=0 iff a=b=0` over integers and elementary square-root arithmetic.

**Instantiations:** `N=25` has `c=±5` and points `(0,0,±5)`. `N=2500` has `c=±50` and points `(0,0,±50)`. The 09:00 independently generated N2500 certificate already included them through its local zero guard: 150 endpoints and exact BRC mass `26860799510260072787603759892561716013678`. If one *filters out* all zero residuals instead of handling them, the resulting partial shell has 148 endpoints and mass `26860799510260072787603759892561716013676`; a literal unguarded call to original C4 at zero throws rather than returning that partial shell.

A separate Python standard-library boundary check was actually executed for `N=25,2500,36,26`: the exact isolated original `factor_integer` precondition raises at zero, the square inputs have two zero-residual layers with BRC mass two, and nonsquare 26 has none. This bounded check is not execution of the original five-part R063 program.

## Required consumer repair and provenance

The 09:00 author-side report `research_notes/X6_R063_GAUSSIAN_RESIDUAL_FIBER_NATIVE_Z3_LIFT_20261115_0900.md` must say original C4 accepts positive integral norms and must specify a separate `M=0` branch when constructing the signed-three-axis residual fibers. This is an **actual diagnosed source-to-report contract error**, not a claim that any frozen downstream executable calls C4 with zero.

For native BRC transport, preserve `(axis names, signed c, Gaussian source, ordered component root, zero/positive branch provenance, positive path multiplicity)`. The old positive-sector C3/C4 certificate and frozen historical Result are not edited. Remaining source work: locate a concrete improper current/historical caller for LP011 signed argmax and LP019 signed cancellation; complete 28-LP dependency closure, Driver REQUEST_REVISION and the original `N2500/r=1..512` native replay assigned through [#2416](https://github.com/awdawmip/enterprise-math/issues/2416).

**Do not repeat:** 09:00 Gaussian factorization finite enumeration and 08:00 signed-shell enumeration have already passed and were saved; only the newly identified exact interface guard and affected report typing are new here.
