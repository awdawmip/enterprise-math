# R749SUM — Uniform 16 bound for optimal labeled two-Port determinant-one feedback defects

Date: 2026-11-18 (Asia/Shanghai). Status: AUTHOR_EXACT_NOT_REVIEWED. Scope: auxiliary positive-rational WBRC-T30–T32 *labeled* two-Port feedback observer only.

## Precise source / frozen inputs

The scientific input is frozen at `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389` (WBRC-T30–T32). Reuse the exact former results:
- R749SUK main note at `@0b292a4181f3729b2bda282cf35e6df2166531e5:research_notes/portable_direct/2026-11-18_R749SUK_UNIFORM_MAXIMIZER_DEFECT_AND_DIVISOR_FIBERS.md`, including its complete C++17 finite certificate `R749SUK_Q_FIBER_UNIFORM_BOUND_CERT.cpp` and saved `R749SUK_Q_FIBER_RESULTS.json`.
- R749SUI construction at `@7836316b174a1182703fd3595244d88460f68438`.
- R749SUL is contemporaneous complementary work on positive-unit windows (PR #2710); this note strengthens the global absolute defect bound instead.

The P000 six-native-axis, one-time world, typed three-dimensional slice, triadic force closure, source/resource guards and typed time retain their own scope. This is an auxiliary two-coordinate/Port observer, with no claim of an admitted native X6 event. The model and observer are unchanged from R749SUK.

## Definitions

For integer `M >= 2`, let

```
U_M = { (a,u,v,d) in {1,...,M}^4 : ad - uv = 1 }.
tau(a,u,v,d) = max(u,v) ad.
Q(a,u,v,d)   = u+v-a-d.
```

The canonical family is `a=d, {u,v}={a-1,a+1}`. By R749SUK Theorem 1, `Q=0` exactly for canonical configurations. Let `Opt(M)` be **all labeled maximizers of tau among noncanonical members**; in particular ties are retained. The previous universal statement was `|Q|<=20`.

## Theorem A — improved universal bound (all M)

**For every integer M >= 2 and every A in Opt(M),**

```
                         |Q(A)| <= 16.                      (A)
```

This is a complete finite-plus-analytic proof, using the previously published and executed exact finite certificate for `2<=M<=10000`. The *new analytical part* alone proves (A) for every `M>=9800`, replacing the earlier analytic threshold `M>=249999` for a 16-bound. The finite and infinite ranges overlap.

### Lemma 1 — integer deficit control without cube-root evaluation

Let `t=floor(sqrt(M+1))>=3`, `m=t^2-1`, `delta=M-m` (so `0<=delta<=2t`), and

```
W=m(m-t)^2.
```

The legitimate noncanonical competitor
`(a,u,v,d)=(m-t,m,t(t-2),m-t)` has determinant 1, has `Q=1`, and has threshold `W`. Thus any member of `Opt(M)`, oriented so `u=max(u,v)`, satisfies

```
u a d >= W.
```

Put `h=M-u, r=M-a, s=M-d, S=h+r+s`. All are nonnegative integers. By AM-GM,

```
       W <= (M-h)(M-r)(M-s) <= (M-S/3)^3,
       S <= 3M-3W^(1/3) = 3delta+3m-3W^(1/3).
```

For all integers `t>=3`, the exact polynomial identity

```
27m(m-t)^2-(3m-2t-1)^3
     = 18t^4-28t^3-42t^2+42t+37 > 0                     (1)
```

holds: `18t^2-28t-42 > 0` for `t>=3`, and the other summands `42t+37` are positive. Since `3m-2t-1>0`, (1) implies
`3m-3W^(1/3)<2t+1`. As `S` is integral,

```
                         S <= 3delta+2t <= 8t.            (2)
```

### Lemma 2 — defect-controlled fiber

Use R749SUK's determinant identity
`uQ=(u-a)(u-d)-1` and write `x=u-a=r-h`, `y=u-d=s-h`.
For `u>=2`, neither `x` nor `y` is zero, since otherwise `uQ=-1`. Both cannot be negative: then `xy>=1` implies `Q>=0` by the identity, while `Q=x+y+(v-u)<0` because `v<=u`. Thus either both are positive or their signs differ. In the first case `xy<=rs<=S^2/4`; in the second `|xy|<=rh` or `sh<=S^2/4`. Consequently

```
                       |uQ| <= S^2/4+1.                  (3)
```

Because `a,d<=M`, `u>=W/M^2`. For `t>=3`, the competitor has `W>2`, so a maximizing orientation must have `u>=2`. Combining (2)–(3),

```
 |Q| <= (((3delta+2t)^2)/4+1) M^2/W
     <= (16t^2+1) (t^2+2t-1)^2 / [(t^2-1)(t^2-t-1)^2].  (4)
```

The first inequality of (4) is a stronger, **instance-sensitive exact rational defect certificate** depending on `t,delta`.

### Lemma 3 — the right side of (4) is strictly below 17 for t>=99

Clearing positive denominators, the required inequality is exactly

```
 17(t^2-1)(t^2-t-1)^2
      -(16t^2+1)(t^2+2t-1)^2
   = t^6-98t^5-67t^4+128t^3+16t^2-30t-18
   = t^4(t^2-98t-67)+(128t^3+16t^2-30t-18)>0.        (5)
```

For `t>=99`, `t^2-98t-67>=32>0`, and the second bracket is positive for positive integers `t`. Thus `|Q|<17`, hence the integer `|Q|<=16`, for every `t>=99`, equivalently every `M>=9800`.

For `2<=M<9800`, the complete saved R749SUK C++17 certificate covers all noncanonical determinant-one labeled candidates and determines every tie. Its reported global maximizing defects are only `{-1,1,2}` for the larger range `2<=M<=10000`, so this finite range satisfies (A). This is a reuse of the existing author-executed finite certificate, **not a newly rerun 60-million-candidate calculation in R749SUM**. Combining the disjoint proof obligations establishes (A). QED.

## Corollary B — a sharp-in-form integer-grid window and square subsequence

For any `t>=3`, `M=t^2-1+delta`, `0<=delta<=2t`, and any `A in Opt(M)`, the stronger computable bound is

```
 |Q(A)| <= floor( ((3delta+2t)^2+4)*M^2 / (4(t^2-1)(t^2-t-1)^2) ).   (6)
```

In particular, if `delta=0` and `t>=5`, (6) yields `|Q(A)|<=1`. Indeed the required inequality reduces to

```
2(t^2-t-1)^2-(t^2+1)(t^2-1)
       = t^4-4t^3-2t^2+4t+3 > 0                            (7)
```

for all `t>=5`; write its first terms as `t^3(t-4)-2t^2+4t+3`, increasing and positive from t=5 (or check the derivative of the explicit polynomial). Since noncanonical configurations have `Q!=0`, all such optimal configurations have `Q=+1` or `Q=-1`. This is an absolute-defect claim; R749SUL supplies a separate positive-sign result in its stated windows.

## Reproducibility, scope and next question

The companion `R749SUM_DEFECT16_POLYNOMIAL_CERT.py` is a standard-library-only exact integer polynomial identity checker for (1), (5), (7), with a bounded regression of the strict rational inequalities. Its JSON output is saved in `R749SUM_DEFECT16_RESULTS.json`. Infinite positivity follows from the displayed coefficient arguments, *not* from testing finitely many t. The finite `M<=10000` dependency remains exactly the old immutable R749SUK C++17 certificate and result JSON; no duplicate scan or newly claimed independent review.

This is a global improvement of the proven numerical constant from 20 to 16 for labeled optimum threshold defects. It does not show sharpness of 16; the verified historical finite optimum defects through M=10000 are still in {-1,1,2}. The next worthwhile question is to find a strengthened construction / modular inverse obstruction that reduces the universal bound to 2, or to exhibit a genuine Q>=3 maximizing witness. For native-X6 transfer, require an exact Cell/Link/Port event, triadic lift, resource/time source guard, and observer preservation certificate separately.
