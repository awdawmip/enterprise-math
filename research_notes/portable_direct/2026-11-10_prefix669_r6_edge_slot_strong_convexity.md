# PREFIX-669-R6 — Quantitative slot-parameter convexity of the moving BRC boundary maximum

Date: 2026-11-10 (Asia/Shanghai). Scientific input pin: `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Type: independent direct TASK_RESEARCH increment; author-derived mathematical implication of existing frozen-model certificates. Status: `AUTHOR_DERIVED / EXACT_FRACTION_IMPLICATION_CHECKED / UNREVIEWED / NOT_ADMITTED`.

## Question, scope and sources

For the frozen 189-layer two-direction BRC first-stop *statistical observer*, determine how its **already certified boundary-strip maximum** changes with the continuous sampling-slot parameter. Write `mu(p,z)=E[Y(p,z)]`, `W(p,z)=Var(Y(p,z))` and `V_q(p,z)=q^2 W(p,z)-q mu(p,z)`. On the boundary `p=0`, put

`I=[607/4096,609/4096]`, `Q=19/128`, `M(q)=max_{z in I}V_q(0,z)=V_q(0,z_*(q))`, `12<=q<=24`.

Theorem PREFIX-660 establishes a unique interior maximizer `z_*(q)`, differentiable and increasing, as well as exact edge `z`-curvature and derivative envelopes. PREFIX-659 certifies `86048.098<V_12(0,Q)<86048.099` and `346339.323<V_24(0,Q)<346339.324`. PREFIX-668 independently recomputes the center mean `89.455<mu(0,Q)<89.456`. These three prior *author certificates* are the stated hypotheses of the present implication proof. Relevant immutable history: PREFIX-659 at `65536b12a268b619e0e1e89f685de3fb2162bea3`, PREFIX-668 at `f6288695a77bd13ee55752fd73cf177083e7c8db`; PREFIX-660 file `research_notes/portable_direct/2026-11-10_prefix660_r6_moving_edge_maximum.md` (blob SHA `892b2ec2cab13acbd17b606ea4667f0bb9a47f9a`). Frozen probability observer variables are **not** native Enterprise X6 spatial axes.

## Theorem 669.1 — strict slot monotonicity and strong-convexity enclosure

For every real `q` in `[12,24]`, the boundary envelope `M` is twice differentiable and

```
M'(q) > 14282,
1208 < M''(q) < 1213.
```

Its unique optimal edge probability also obeys the explicit uniform motion bound

```
12*19/52000000 < z_*'(q) < 24*66/12800000.
```

In particular, for `12<=a<b<=24`, `0<theta<1` and `q=(1-theta)*a+theta*b`, the exact two-sided chord deficit is

```
604*theta*(1-theta)*(b-a)^2
  < (1-theta)*M(a)+theta*M(b)-M(q)
  < (1213/2)*theta*(1-theta)*(b-a)^2.
```

For the midpoint `q=18`, this gives

```
21744 < (M(12)+M(24))/2 - M(18) < 21834.
```

This is a theorem for the certified boundary interval `I`, with exact dependence on the unchanged observer probability model; the full-square global maximum remains open.

## Proof

PREFIX-660 gives `42<W_z(0,Q)<43` and `-92000<W_zz(0,z)<-88000` throughout `I`. As `|z-Q|<=1/4096`, integration yields `19<W_z(0,z)<66` on `I`. From the center variance and mean certificates,

```
(86048.098+12*89.455)/144 < W(0,Q)
  < (86048.099+12*89.456)/144.
```

Integration with `|W_z|<66` shows `604<W(0,z)<606` throughout `I`. On the boundary, the PREFIX-660 finite Gamma-clock representation reads

```
mu(0,z)=25+sum_{m=0}^{188} a_m s_m(z),
0<=a_m<=1, 0<=s_m(z)<=1,
```

hence `mu(0,z)<=214`. The strict concavity theorem of PREFIX-660 gives

```
-52000000<V_{q,zz}(0,z)<-12800000
```

on `I` for every `12<=q<=24`: it follows from its two endpoint-slot bounds by the affine identity `V_{q,zz}/q=q W_zz-mu_zz` together with `W_zz<0`.

At the unique interior critical point `z=z_*(q)`, the first-order relation is `mu_z=q W_z`. Implicit differentiation gives

```
z_*'(q) = -q W_z(0,z_*(q))/V_{q,zz}(0,z_*(q)) > 0.
```

The displayed `z_*'` bounds follow from `19<W_z<66` and the curvature bounds. By the envelope theorem and another differentiation,

```
M'(q) = 2q W(0,z_*)-mu(0,z_*),
M''(q) = 2W(0,z_*)
         + q^2 W_z(0,z_*)^2/(-V_{q,zz}(0,z_*)).
```

The first formula gives `M'>2*12*604-214=14282`. The second gives `M''>2*604=1208`, while

```
M'' < 2*606 + (24*66)^2/12800000 < 1213.
```

Integrating the strict second-derivative inequalities twice against the affine chord between `a` and `b` proves the two-sided chord-deficit inequality. This completes the theorem.

## Corollary 669.2 — new certified slot-18 bound and edge separation

The Gamma-clock polynomial gives the *exact identity at every fixed observer parameter point*

```
V_18 = (3/4) V_12 + (3/8) V_24.
```

At `Q`, the PREFIX-659 strict lower certificates therefore imply

```
M(18) >= V_18(0,Q)
      > (3/4)*86048.098+(3/8)*346339.323
      = 1555306557/8000 = 194413.319625.
```

Combining the midpoint chord deficit with the PREFIX-660 upper edge maxima gives

```
M(18) < [86048.1065484353+346340.5678394320]/2-21744
      = 3889006743878673/20000000000
      < 194450.33719393365.
```

Thus `194413.319625<M(18)<194450.33719393365` is an exact rational implication for the modeled edge optimum. The two PREFIX-660 dyadic maximizer brackets also imply

```
4265/16777216 < z_*(24)-z_*(12) < 4267/16777216.
```

## Verification and next discriminating unit

Run `python PREFIX669_R6_EDGE_SLOT_ENVELOPE_CERTIFICATE.py` in this directory, standard library only. It checks **19 exact integer/Fraction implications** of the published strict source bounds; `PREFIX669_R6_RESULTS.json` contains precise rational diagnostics. It reuses rather than recomputes PREFIX-659/660/668's 189-layer survivor source; this is a new derived theorem, not an independent verification of those certificates. Status remains unreviewed and not admitted.

Next: use slot-parameter curvature and strengthened slot-specific linear normal penalties for interval exclusion rules uniform in `q`, then perform exact Bernstein pruning of `0<=p<=z<=1/2` against the best known `p=0` competitor. Independently, test `p in [1/64,1/32]` curvature using a coupled bivariate Bernstein bound; sampled centers suggest additional negative curvature without yet certifying that entire rectangle.
