# R5: exact five-real-parameter maximal-early-flow cone Blackwell lift

Date: 2026-11-07 Asia/Shanghai. Author-side exact theorem; independent review/Source admission pending. Frozen input pins unchanged: GLOBAL `a01383f825ef9d43b4b754254303298c64041568`; EM `86149263e38c22292c9def1e0f69092efa1be77e`.

## Full cone theorem

For EVERY real `0 <= t <= 1` and EVERY real parameters
`0 <= u,w <= 27*t/80`, `0 <= z <= t/10`, `0 <= v-z <= 9*t/40`,
the frozen legal FULL_HIST flow

```
x=(g,a,b,u,v,w,z)=(t,t,t,u,v,w,z)
```

admits a legal seedless LR flow and a fixed seven-key stochastic Blackwell declaration kernel, such that for EVERY real `d in [0,1]^7` all four observers `(e_P,e_Q,T_P,T_Q)` are matched exactly. The statement includes t=0 and all boundary cases. Its history residual is `R(x)=9*t*z-4*t*(v-z)`, which can have either sign.

For t>0, set `X=x/t`; `X` lies in the complete four-dimensional face `g=a=b=1` proved in `RESEARCH_4D.md`. That theorem supplies a legal seedless `Y` and a nonnegative calibrated transport `Q` from `Y` to `X`, with matching stopping times. Define

```
y=t*Y
Q_t=t*Q+(1-t)*E_{3,3},
```

where `E_{3,3}` is the 7x7 unit matrix with its only nonzero mass at likelihood-ratio key index 3, whose likelihood ratio equals 1. For t=0 take `y=0` and `Q_t=E_{3,3}`.

**Proof.** The legal flow constraints are linear and homogeneous (apart from the upper bound g<=1); multiplying a legal Y by t preserves legality. The seedless equation `9*b*z=4*a*(v-z)` is homogeneous of degree 2, so y is seedless. Each Q stopping mass is affine in the seven flow coordinates and satisfies `M(0)=delta_3`; therefore

```
M(t*X) = t*M(X) + (1-t)*delta_3,
M(t*Y) = t*M(Y) + (1-t)*delta_3.
```

Both stopping times equal 1 at zero flow and are affine, hence `T(t*X)=1+t*(T(X)-1)`, and likewise Y, so their two times match. Multiplying the seven row/column calibrated identities for Q by t and adding `(1-t)E_{3,3}` preserves nonnegativity, all row sums, all Q column sums and the likelihood-weighted P column sums because `r_3=1`. Normalize positive-mass rows to stochastic K and assign identity to zero rows. For every d in [0,1]^7, `K*d` remains a legal declaration and both e_Q and 1-e_P agree by the two column identities. This proves the assertion for ALL REAL parameters, including t=0. QED.

### Exact checking

`VERIFY_5D.py` builds the transport by this formula from the published 4D checker; with Python stdlib Fraction it checks 5 rational t values times 81 rational (s,t,p,q) quadruples, each with 128 binary declaration choices, and all row/column/time/legality identities. Its actual executed output is `EXACT_OUTPUT_5D.txt`; the mathematical all-real conclusion follows from the proof above. Terminal result: `PASS_R5_ALL_REAL_FIVE_PARAMETER_MAXIMAL_EARLY_FLOW_CONE_BLACKWELL_LIFT`.

## Continuation

The full frozen R5 target is four-observer pointwise image equality or a certified separation witness. This theorem resolves every legal FULL_HIST flow with `g=a=b` (including g<1). Remaining distinct early-flow regimes have `a<g` or `b<g`, especially `a != b`. Seek rational vertices with exact seedless calibrated transports, common-affine-face interpolation if possible, or a global non-liftability certificate.
