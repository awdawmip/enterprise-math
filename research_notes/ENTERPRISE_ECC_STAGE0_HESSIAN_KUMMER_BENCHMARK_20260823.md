# Enterprise ECC Stage 0 — Hessian / Kummer benchmark

Status: `FREE_RESEARCH / PHASE_B / EXPERIMENTAL`
Date: `2026-08-23`
Researcher-ID: `EM-FREE-ACE4FF`

## 1. Scope

Question: can the current three-positive-axis Enterprise geometry support an ECC implementation with a genuine arithmetic or scheduling advantage, rather than merely redrawing a classical elliptic curve?

Important type boundary:

- geometric ellipse != elliptic curve;
- Enterprise native address `(a,b,c), min(a,b,c)=0` != projective elliptic-curve coordinate `(X:Y:Z)`;
- a first-generation implementation may use the three Enterprise axes as execution lanes without identifying the two coordinate semantics.

## 2. Baseline models

Arithmetic comparison uses verified explicit-formula counts from the Explicit-Formulas Database (EFD):

- Montgomery XZ mixed ladder step: `5M + 4S + 1*a24`;
- twisted Edwards extended, `a=-1`: addition `8M`, doubling `4M + 4S`;
- Hessian projective: addition `12M`; a symmetric doubling variant `6M + 3S` (serial-best alternatives also exist, e.g. `7M+1S`);
- complete short-Weierstrass projective, `a=-3`, Renes–Costello–Batina: addition `12M + 2*b`, doubling `8M + 3S + 2*b`.

Sources:

- https://www.hyperelliptic.org/EFD/g1p/auto-montgom-xz.html
- https://www.hyperelliptic.org/EFD/g1p/auto-twisted-extended-1.html
- https://www.hyperelliptic.org/EFD/g1p/auto-hessian-standard.html
- https://www.hyperelliptic.org/EFD/g1p/auto-shortw-projective-3.html

## 3. Constant-flow per-bit work comparison

For a simple constant-flow binary ladder-style comparison, use one addition plus one doubling per scalar bit, except Montgomery which has a fused differential-addition-and-doubling primitive.

Using the standard rough model `S = 0.8M` and treating parameter multiplication separately:

| model | per-bit core work | M-equivalent (parameter multipliers omitted) |
|---|---:|---:|
| Montgomery XZ | `5M+4S` | `8.2M` |
| Edwards ext a=-1 | `12M+4S` | `15.2M` |
| Hessian projective symmetric | `18M+3S` | `20.4M` |
| complete Weierstrass a=-3 | `20M+3S + 4*b` | `22.4M + 4*b` |

Immediate result: Hessian does not win merely because it has three symmetric coordinates.

## 4. Same three-multiplier budget

Give every model the same budget of three parallel field multipliers/squarers. The relevant metric is then work/span rather than visual coordinate count.

A hand-scheduled dependency audit gives approximate multiplication-layer depths for one constant-flow bit step:

- Montgomery mixed ladder: about 4 layers;
- Edwards addition+doubling: about 6 layers;
- Hessian symmetric addition+doubling: about 7 layers;
- complete Weierstrass: at least about 9 layers when full-cost curve-parameter multiplications are included.

Therefore the hypothesis

`THREE HESSIAN COORDINATES -> AUTOMATIC THREE-LANE SPEEDUP`

is rejected under a fair equal-hardware budget.

The remaining possible engineering gap is a *fused Hessian/Kummer ladder primitive*, analogous to Montgomery `xDBLADD`, not ordinary full-coordinate Hessian addition.

## 5. Interpreter microbenchmark (diagnostic only)

A current-runtime CPython modular-arithmetic microbenchmark over `p = 2^255-19` used the above arithmetic kernels. Median of 7 runs:

| kernel per bit step | median microseconds |
|---|---:|
| Montgomery | 4.80 us |
| Edwards | 8.84 us |
| Hessian | 9.28 us |
| complete Weierstrass | 15.96 us |

This is **not** a cryptographic implementation benchmark: Python is not constant-time; values are not optimized assembly; parameter multiplication costs differ; inputs were arithmetic-kernel states rather than standardized secure-curve test vectors. It is only a sanity check that the EFD work-count ordering appears in an independent executable arithmetic kernel.

## 6. New Hessian quotient coordinate

For the affine Hessian curve

`H_d: x^3 + y^3 + 1 = 3 d x y`, `d^3 != 1`,

negation is

`-(x,y) = (y,x)`.

Hence

`s(P) := x(P) + y(P)`

satisfies

`s(P)=s(-P)`.

So `s` is a natural coordinate on the Kummer quotient `H_d/{+-1}`.

Write `p0=xy`. From the Hessian equation,

`p0 = (s^3+1)/(3(s+d))`.

The standard Hessian-to-Weierstrass birational map has Weierstrass x-coordinate

`u = 12(d^3-1)/(d+s) - 9d^2`.

Therefore the Hessian quotient coordinate `s` and the Weierstrass x-coordinate `u` are related by a Mobius transformation. This is an exact algebraic bridge, not a visual analogy.

## 7. Exact one-coordinate doubling law

Starting from the affine Hessian doubling formulas and eliminating `x,y` through `s=x+y` and `xy=(s^3+1)/(3(s+d))` gives

`s(2P) = -(s^4 + 4s + 3d)/(2s^3 + 3d s^2 - 1)`.

For projective Kummer coordinate `s=S/Z`, one homogeneous realization is

`S' = -(S^4 + 4 S Z^3 + 3d Z^4)`,

`Z' = 2 S^3 Z + 3d S^2 Z^2 - Z^4`.

A square-heavy schedule can evaluate this in approximately `2M + 6S + 2D` (`D` = multiplication by fixed parameter/constant), before any final scaling.

With three parallel arithmetic lanes, its multiplication/squaring dependency span is about three layers when fixed-constant multiplies are cheap.

## 8. Exhaustive finite verification

Pressure test:

- field: `F_239`;
- Hessian parameter: `d=5`;
- curve: `x^3+y^3+1=15xy (mod 239)`.

The curve has 248 affine points plus one point at infinity, total group order 249.

The derived one-coordinate doubling identity was exhaustively checked on all 248 affine points. Result:

`248 / 248 PASS`, `0 mismatches`, `0 denominator exceptions in this test set`.

Example using the earlier subgroup point `(3,91)`:

- direct Hessian doubling gives `(53,229)`;
- direct quotient readout gives `53+229 = 43 mod 239`;
- the new formula at `s=3+91=94` also gives `43 mod 239`.

## 9. Relation to known prior art

Hessian arithmetic, unified Hessian addition/doubling, side-channel use, and ternary scalar algorithms are classical prior art. In particular:

- Joye–Quisquater (CHES 2001) already exploited Hessian symmetry for unified addition/doubling/subtraction;
- EFD records modern operation counts and shows Montgomery/Edwards arithmetic is generally cheaper in large prime characteristic;
- signed-ternary Hessian scalar algorithms exist especially in characteristic three.

Therefore novelty cannot be claimed from `Hessian + three coordinates` or from ternary scalar recoding alone.

The current Enterprise-specific research gap is narrower:

1. derive a low-cost `s`-coordinate differential addition law directly on the Hessian Kummer quotient;
2. fuse it with the new `s`-doubling map into an Enterprise `sDBLADD` primitive;
3. compare its work/span under exactly three arithmetic lanes against Montgomery `xDBLADD` on the same large prime field;
4. only if that survives, investigate whether the three Enterprise axes provide a useful fixed scheduling/placement semantics.

## 10. Stage 0 verdict

`FULL_COORDINATE_HESSIAN_THREE_LANE_AUTOMATIC_SPEEDUP = REFUTED`.

`HESSIAN_KUMMER_SINGLE_COORDINATE_ROUTE = SURVIVES`.

Next executable action:

`DERIVE / SEARCH / VERIFY HESSIAN-s DIFFERENTIAL ADDITION -> FUSED sDBLADD -> THREE-LANE WORK/SPAN BENCHMARK`.
