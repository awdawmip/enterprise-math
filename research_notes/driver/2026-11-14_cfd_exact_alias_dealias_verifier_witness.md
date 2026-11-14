# CFD 独立核验的精确反混叠见证：原生网格与 3/2 补零

Date: 2026-11-14. Scope: bounded exact Fourier-mode arithmetic and verifier-test design (not a native host rerun or formal Result). Algebraic diagnostic: EM-DVR-DEBB5E (RESEARCH_DRIVER); original host implementation/data: EM-CFD-49157B. Parent `OBJ-CFD-TRUSTWORTHY-ACCELERATION-20260910`. Existing independent verifier Task `RS-CFD-TRAJECTORY-VERIFY-20260910`, publication `TP2-499BEE22860EFD4AD321`.

## Exact two-mode construction

Let `nu=(1,-7,6)`, `L=ker_Z(nu·)`, and the retained 16-grid Fourier cutoff `K=7`. Choose

```
p=(7,1,0),    q=(6,0,-1),
a=(1,-7,0),   b=(0,1,0).
```

These are integer-supported, divergence-free data: `nu·p=nu·q=0`, `p·a=q·b=0`. The real initial field `u(x)=a cos(p·x)+b cos(q·x)` includes the conjugate modes `-p,-q` in the appropriate real/rFFT representation.

The exact sum `w=p+q=(13,1,-1)` stays inside `L` but lies outside `[-7,7]^3`, so its quadratic interaction is discarded by the exact retained Galerkin projection. An **unpadded cyclic N=16** convolution wraps it to `k=(-3,1,-1)` inside the retained region. Here `nu·k=-16`, so the alias spuriously leaves the integer lattice.

For the advective form, write `c=(a·q)b+(b·p)a=(1,-1,0)`. The aliased Leray projection is

```
P_k c = c - k (k·c)/|k|² = (-1,-7,-4)/11 != 0.
```

For the rotational form `(curl u) × u`, the cross coefficient before the common nonzero imaginary Fourier factor is `c_rot=c-(a·b)w=(92,6,-7)`. Its aliased projection is

```
P_k c_rot = (223,329,-340)/11 != 0.
```

Reversing a host's convection sign changes this sign, not the nonzero witness. These identities are exact rational calculations; for the cosine normalization, each displayed cross coefficient enters with a common factor `i/4` (up to the declared convection sign).

Under correct **3/2 zero-padding**, the padded length is 24. The same true `w=(13,1,-1)` wraps on that padded grid to `(-11,1,-1)`, outside the original retained `K=7` band; truncation removes it. Conjugate contributions are removed analogously. Genuine differences `p-q=(1,1,1)` and `q-p=(-1,-1,-1)` remain in `L` and must be retained.

## Targeted verification protocol

The existing verifier can initialize the above real two-mode field on the author's pinned **serial spectralDNS/shenfun/FFTW host** (`N=16`, original native `3/2-rule`, Nyquist mask, Vortex callback). Compare the hybrid and original unmodified dense callback on a single RHS and one or more actual RK4 stages, logging the off-`L` retained coefficients, the native Leray projection/divergence, conjugacy, fallback behavior and measured absolute residuals. In exact Galerkin arithmetic, the retained off-`L` coefficient at `k` vanishes; in the actual floating implementation report the numerical tolerance and values. If an explicitly unpadded 16-grid control is implemented, its aliased `k` is a distinguishing negative control as proved above.

This additional algebraic case tests **dealiasing/support integrity** specifically. It complements the author's existing eight-case 16/32-grid Numba matrix and is not a replacement for full-cost, complete-trajectory and independent host checks. Neither runtime pass nor solver acceleration is claimed here.

## Provenance

The exact support lattice and its 33 retained points were previously reviewed in `research_notes/driver/2026-11-14_cfd_host_frozen_lattice_exact_scope_audit.md`. Original adapter and host test code:
- `awdawmip/enterprise-math@a282f0f9832a69af0b65549dc0083ddd2a6d8ada:research_notes/CFD9R2K7/host_20260916/native_adapter.py`
- `awdawmip/enterprise-math@a282f0f9832a69af0b65549dc0083ddd2a6d8ada:research_notes/CFD9R2K7/host_20260916/host_validation_numba.py`
- Original host checkpoint `awdawmip/enterprise-math@20255478397fc475ec0584da0cf4311dd17bcc82:research_notes/CFD9R2K7/host_20260916/checkpoint_summary.json`.

The original implementer retains authorship of the adapter and reported native experiments. This Driver contributes the present algebraic negative-control design only. Current Task acceptance, independent verifier claim and formal Result remain with their separately authorized flows.
