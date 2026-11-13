# R5: seven forcing scores have rank six; an exact lawful collision and a minimal two-readout repair

Date: 2026-11-10 (Asia/Shanghai). Author-side exact-mathematics continuation of Draft PR #2002. **Scientific inputs are unchanged:** GLOBAL pin `a01383f825ef9d43b4b754254303298c64041568`; Enterprise Math pin `86149263e38c22292c9def1e0f69092efa1be77e`. Current behavioral rules are read separately.

## Statement, scope and provenance

Work in the original seven-likelihood-ratio P/Q–BRC auxiliary Blackwell model: 14 original physical strategy coordinates, five linear equalities, 26 capacity nonnegativity inequalities, 21 original transport equations and 30 allowed transfer columns. The eight-dimensional physical affine coordinates are `p(z)=p7+P z`; the compressed (reversibly scaled) 15-component transport right side is `q(z)=q7+T z`. The previous exact model definitions, seven-edge seed, six forcing certificates and separating certificate are reproduced in `VERIFY_COLLISION.py`. These are **model-internal finite rational results**; no change is made to native P000 or world dynamics.

Let `Y` contain the existing six forcing rows `y00,y33,y43,y45,y65,y66` and the seventh separating row `ell`; put `s(z)=Y q(z)` and `A=Y T`. The six forcing rows are rechecked against every one of the 30 allowed columns.

**Theorem A — exact rank and score identity.** The rational matrices obey

```text
rank(T)=8,      rank(A)=6,      dim ker(A)=2,
s_ell(z) = (10/23) s_43(z) - (65/138) s_45(z) + (52/69) s_65(z)
```

for **every** point of the eight-dimensional physical affine model (including lawful physical points). The identity uses the actual scores, not merely their variations: its derivative is zero because `A^T (0,0,-10/23,65/138,-52/69,0,1)^T=0`, and its constant is zero at the exact seed `p7`. The left nullspace is exactly the span of this row relation. The seven certificate values therefore retain only six independent affine degrees of freedom.

**Theorem B — physically lawful collision.** There are two *different* physical strategy pairs `pbar` and `pplus`, each satisfying all five physical equalities and all 26 capacities, such that both admit exact nonnegative couplings satisfying all 21 original Blackwell equations but

```text
Y q(pbar) = Y q(pplus),       q(pbar) != q(pplus).
```

One direct construction starts from the earlier lawful seven-edge seed `p7`, and the six-edge diagonal pair `u=(x,x)` with

`x=(1,1/2,1,1/10,1/10,1/10,1/20)`.

Set `pbar=(p7+u)/2` and form `K` from the exact rational nullspace of `A`. Set `dz=K*(1/10000,1/40000)^T` and `pplus=pbar+P dz`. The exact computed displacement is

```text
dz = (
 -2126551/867626168000,
  27401958279/29065476628000000,
  864386951/8676261680000,
 -3/91750,
 -1789/29360000,
  1088083/98356000000,
  1/10000,
  1/40000
)
```

and the first two 15-component observation differences are precisely

```text
q0(pplus)-q0(pbar) = -3/91750,
q1(pplus)-q1(pbar) = 333/2348800.
```

`pbar` has an explicit positive 10-edge coupling obtained by averaging the seven-edge `p7` transport with the six diagonal edges. `pplus` has an exact positive **13-edge** coupling, consisting of

```text
(0,0), (1,1), (0,2), (1,2), (2,2), (3,2), (2,3),
(3,3), (4,3), (4,5), (5,5), (6,5), (6,6)
```

whose minimum exact positive mass is `27/229375`. The verifier solves for all 13 rational weights and checks the original 21-component equation, not only the compressed equations. This establishes a real collision inside the admissible physical/transport domain. The 10-edge and 13-edge numbers are *constructed support sizes*, not claims of minimum support for those two points.

**Theorem C — minimal linear recovery.** Append two additional unscaled target-mass readings `q0,q1` to the seven existing scores. The exact 8-by-8 coefficient matrix built from the first six score rows and the two additional `T` rows has

```text
det = 19799371/65505024 != 0.
```

Consequently the eight physical affine coordinates `z` (and thus `q`) are exactly recovered from these observations by rational linear inversion. Because the existing score matrix has rank six, **two independent added scalar linear readouts are necessary and sufficient for injective recovery over the entire eight-dimensional affine family**.

## Verification and evidence

`VERIFY_COLLISION.py` is a compact stand-alone SymPy/Fraction verifier reconstructing the original five physical equalities and 26 capacities, full 21 transport equations, six 30-column dual checks, the rank and determinant, an explicit kernel, the lawful paired strategy collision, an exact 10-edge source and 13-edge target coupling. The support for the 13-edge coupling was initially found with floating-point LP, but the stated proof and exact verifier solve a *fixed support* rational linear system and assert every resulting mass is strictly positive. No floating-point premise is used in the proof.

The local pre-publication run of the full stand-alone `VERIFY_R5_CERTIFICATE_COLLISION.py` produced `PASS_EXACT_PHYSICALLY_LAWFUL_CERTIFICATE_INVISIBLE_COLLISION_AND_TWO_COORDINATE_RECOVERY`. See `EXACT_OUTPUT.txt`; the shorter published `VERIFY_COLLISION.py` implements the same load-bearing exact assertions, but it has not separately been executed verbatim after transport. Readback verifies the published source content, not an independent mathematical review.

## Meaning and next question

The seven forcing/separation certificates remain valid *decision certificates* for the previous support lower bounds. They are not a lossless summary of the full physical/Blackwell observer state. The two missing coordinates form a concrete residual-fidelity obstruction, and the added target masses are a minimal linear repair within this affine representation.

Next: determine whether two physical states with identical seven scores can have **different true minimum support numbers**; such a pair would distinguish *support-classification sufficiency* from the stricter full-observation reconstruction established here. Independently, investigate smaller task-specific sufficient summaries for merely deciding `N_min <= 6`. No change to the previous frozen pins, task ownership, CLAIM, Result, review or Foundation status is asserted.
