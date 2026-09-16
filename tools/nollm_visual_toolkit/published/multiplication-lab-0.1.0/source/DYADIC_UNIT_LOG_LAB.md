# Dyadic Unit-Log Phase Lab 0.1.0

Additive research observer for Nollm Visual Toolkit 0.3.0. It builds on the published reciprocal-phase page and does **not** rewrite the historical multiplication-lab defaults.

## Exact arithmetic coordinate

For `n>0`, write `n=2^v u`, with `u` odd. At precision `b`, every odd residue modulo `2^(b+2)` is uniquely

`u=(-1)^eps 5^t`, `eps in {0,1}`, `t mod 2^b`.

The exact finite-resolution multiplication state is `(v,eps,t)`. Products add `v`, add `eps mod 2`, and add `t mod 2^b`. The direct evaluator strips powers of two and computes a base-5 unit-group logarithm from the odd residue; it does not factor the odd integer.

For compatibility with the existing 2D multiplication workbench, the page uses the one-circle observer

`Phi=t+eps*2^(b-1)+v*2^(b-3) mod 2^b`.

This sends a factor of 2 to 45 degrees. The browser's prime table is only an adapter to the old UI: tests compare the adapter with direct unit-log evaluation for all 65,536 integers.

## Generate

```sh
python -m nollm_visual_toolkit.unit_log_phase_lab --out unit-log.html --phase-bits 11
python -m nollm_visual_toolkit.unit_log_phase_lab --site unit-log-site --preview
```

The default comparison site includes 11-bit and 16-bit pages. Each page can switch between `unitlog`, reciprocal-prime, golden-rank and the older negative-control modes inherited from the underlying workbench.

## Why 11 bits is the default at 65,536 integers

The display radius is `sqrt(n)`. If `M=2^b` angular positions are available, the outer spoke separation is approximately

`2*pi*sqrt(N)/M`.

For `N=65,536`, 11 bits gives `M=2048` and outer spacing about `0.785`, below one display-cell center spacing. The finite run gives:

| observer | 64-sector CV | occupied 2D cells |
|---|---:|---:|
| unit-log 11 bit | 0.006813 | 58,486 |
| unit-log 16 bit | 0.028287 | 57,520 |
| reciprocal 11 bit | 0.025983 | 57,342 |
| reciprocal 16 bit | 0.029426 | 57,339 |

Thus more angular bits are not automatically a better finite physical projection. The exact source coordinate still refines; the rendered cell observer has an appropriate finite resolution.

## Proved phase-distribution result

For dyadic population `1<=n<2^L` and `L>=b+2`, every phase bin has

`H(a)=2^(L-b)-2+R(a)`, with `R(a)>=0` and `sum R=2^(b+1)-1`.

Therefore

`TV(Phi_b, Uniform) <= (2^(b+1)-1)/(2^L-1)`.

The same bound controls every nontrivial phase Fourier coefficient. At the geometric critical scale `b=L/2+O(1)`, this is `O(N^-1/2)` on the declared dyadic populations.

The proof and independent finite verifier are in `research_notes/nollm_dyadic_unit_log_phase_20260911.md`.

## Resolution refinement

If `t_b` is the exponent modulo `2^b`, then

`t_(b+1)=t_b+eta_b 2^b`, `eta_b in {0,1}`.

Consequently the circle observations satisfy

`w_(b+1)^2=w_b`, where `w_b=exp(2*pi*i*t_b/2^b)`.

The exact infinite refinement coordinate is 2-adic; the visible circles form a square-root branch tower. Old angles cannot all remain numerically fixed while new exact group bits are added. This is a structural reason to preserve refinement state rather than force a single final circle.

## Nollm boundary

The research state `(v,eps,t)` suggests separating:

- `v_2` as an exact dyadic scale/layer component,
- `eps` as a two-sheet unit component,
- `t` as the lateral dyadic unit-log coordinate.

Current Nollm research has 22.5-degree adjacent-layer rotation and `beta=2^(1/4)`, so a factor `2^v` corresponds to `2v` virtual layer intervals, scale `2^(v/2)` and frame rotation `45v` degrees. This note does not change physical Memory Layer semantics or the production Coverage kernel.

Retaining `(eps,v_2)` next to the display cell greatly reduces finite projection collisions, but those collision counts remain floating display evidence, not a native-memory theorem.

Status: `RESEARCH_TOOL / PROVED_DECLARED_PHASE_IDENTITIES / FINITE_GEOMETRIC_OBSERVER / NOT_FOUNDATION`.
