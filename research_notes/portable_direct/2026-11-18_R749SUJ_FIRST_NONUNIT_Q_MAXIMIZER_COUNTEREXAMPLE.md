# R749SUJ — First exact counterexample to the unit-defect maximal Port-threshold conjecture

Date: 2026-11-18 (Asia/Shanghai). Status: **AUTHOR_EXACT_NOT_REVIEWED**.

## Provenance and precise scientific scope

Continuation of R749SUI, immutable scientific predecessor `awdawmip/enterprise-math@7836316b174a1182703fd3595244d88460f68438:research_notes/portable_direct/2026-11-18_R749SUI_UNIFORM_FIRST_INTRUSION_AND_MODULAR_INVERSE_OPTIMIZER.md`. Frozen scientific family: WBRC-T30–T32 at `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`. P000 and ACTIVE X6/triadic/temporal/residual axioms remain untouched. This is a **labeled, auxiliary two-Port positive-rational feedback-bin observer** result, not an assertion that the auxiliary integer matrices are admissible native Cell/Link/Port events.

For each integer M >= 2 set

`U_M = {(a,u,v,d) in {1,...,M}^4 : ad - uv = 1}`.

Set `tau(a,u,v,d) = max(u,v)*a*d`, and call `(a,u,v,d)` **canonical adjacent-diagonal** if `a=d` and `{u,v}={a-1,a+1}`. Let `T*(M)` be the maximum tau over noncanonical members and `Q(a,u,v,d)=u+v-a-d`. R749SUI recorded the open proposal: all maximizers have `|Q|=1`.

## Theorem A (finite exact falsification; first occurrence)

At **M=58**, the noncanonical maximum is exactly

`T*(58)=127890 = 58*45*49`.

Its **four labeled maximizers**, written as `(a,u,v,d)`, are

- `(45,58,38,49)`, `(45,38,58,49)`,
- `(49,58,38,45)`, `(49,38,58,45)`.

Every one satisfies `Q=2`, and `45*49-58*38=2205-2204=1`. The next-largest *distinct* tau is 124080, leaving a strict gap of 3810. The complete bounded domain contains **3882 noncanonical labeled configurations**.

The independently enumerated ranges `2 <= M <= 57` have only `|Q|=1` among their noncanonical maximizers. Hence **58 is the first counterexample over all integer M>=2**.

At **M=93** a second exact counterexample occurs: `T*(93)=579576=93*76*82`, with four labeled maximizers obtained from `(76,93,67,82)` by independently interchanging a/d and u/v; each has `Q=2` and determinant one. Here the runner-up is 575190, and the noncanonical domain has 10254 configurations.

**Proof and exhaustive certificate.** For any fixed M, enumerate every integer triple `(a,d,u)` with `1<=a,d,u<=M`. The equation `ad-uv=1` uniquely forces `v=(ad-1)/u`. Retain the triple exactly if `ad-1>0`, `u | (ad-1)`, `1<=v<=M`, and the canonical predicate is false. Thus the loop in `R749SUJ_FINITE_Q_COUNTEREXAMPLE_CERT.py:exhaustive` is a *complete, injective enumeration* of the exact finite set `U_M\setminus canonical`, without a heuristic search. Integer maxima and sorted lists of every equal-score labeled winner are returned; this proves all finite-domain assertions above when the printed certificate is executed. In addition, an independently organized modular-inverse implementation of the R749SUI optimizer agrees on both the maximum and the full winning list at **every M=2,...,120**.

The inverse implementation also scans **every M=2,...,600**, finding exactly M=58 and M=93 as sizes with a non-unit winner defect in that finite range. This latter claim is bounded computational evidence, not a theorem about all M. The finite first-occurrence theorem uses only the certified finite domain `2,...,58`.

## Theorem B (exact defect/imbalance identity, all determinant-one tuples)

Every integer quadruple with `ad-uv=1` satisfies

`(u-v)^2 - (a-d)^2 = Q(a,u,v,d)*(u+v+a+d) + 4.`

**Proof.** Expanding the left side gives `(u+v)^2-(a+d)^2+4(ad-uv)`; factor the difference of squares and use `ad-uv=1`. In particular the M=58 winner has `(u-v)^2-(a-d)^2=20^2-4^2=384=2*(58+38+45+49)+4`. This gives a direct arithmetic diagnostic for the defect, without identifying it with a physical energy or a native-coordinate dimension.

## Verification, exact inputs, reproducibility

Companion executable: `R749SUJ_FINITE_Q_COUNTEREXAMPLE_CERT.py` (Python 3, only `math` and `json` from the standard library; arbitrary-precision integer arithmetic; no floating point). Companion JSON: `R749SUJ_Q_COUNTEREXAMPLE_RESULTS.json`.

Run:

```sh
python3 R749SUJ_FINITE_Q_COUNTEREXAMPLE_CERT.py > R749SUJ_Q_COUNTEREXAMPLE_RESULTS.json
```

The script independently calculates finite maxima, all labeled winners, the runner-up, and precise finite scanning coverage. This run passed locally on 2026-11-18. The two independent enumeration methods agree for 2..120; the separate optimized 2..600 search has the finite exception set `{58,93}`.

## Research consequences and next open problems

The conjecture `maximizer => |Q|=1` is **false**. Any proposed global parametrization or shortcut restricted to `|Q|=1` omits the proven maximal configurations at M=58 and 93. Preserve Q as a genuine joint-relational observer rather than quotienting the offdiagonal sum to a unit defect.

Next: classify possible maximizing Q values, establish an infinite family of non-unit maximizing Q if one exists, or prove a global eventually-unit theorem if evidence warrants; examine prime-valuation and congruence conditions on `ad=uv+1` near the top threshold. Independently seek a source-pinned admissible X6 Cell/Link/Port event with a triadic lift, explicit resource/time guard and preservation map for this feedback-bin observer. No shared CLAIM, Result/Review, Foundation promotion or native event mapping is asserted.

Source role: continued independent portable research; historical contributor provenance `EM-DIRECT-7A5B40` is not treated as a fresh authenticated session capability.