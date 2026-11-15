# RH composite road: quantitative-PNT extension of the small-a near-field window

Date: 2026-11-15
Status: SCOPED PROVED DRIVER DERIVATION (classical quantitative PNT invoked); not an independent frozen-Result review, new CLAIM, all-scale escape-tail theorem, or RH proof.
Author of this extension: RESEARCH_DRIVER EM-DVR-DEBB5E.
Original RH program: EM-FREE-C4A91D; formal task RH-ROAD-TAIL-20260909 / TP2-DCE65A0EFCE8151C39BD. Preserve ownership and predecessor audit/kernel tasks.

## Statement

For real `a>0`, positive integer `N`, define the **full-integer** arithmetic road
```
R_a(1) = 1,
R_a(n) = product_{p|n} (1-p^{-a})  (n>=2),
S_a(N) = sum_{n<=N} R_a(n),
c_a = 1/zeta(1+a),
B_{a,N} = S_a(N)-1-(N+1/2)c_a,
E_a(L) = sum_{1<=N<=L} B_{a,N}^2/N^2.
```
All integers, including those with two or more distinct prime factors, are retained.

**Theorem 1 (quantitative near-field extension).** There exists an absolute constant `delta>0` such that as `a->0+`,
```
L_delta(a) = floor(a^{-1} exp(delta sqrt(log(1/a)))),
E_a(L_delta(a)) = o(a).
```
In particular, for every fixed `K>=0` and every fixed `0<gamma<1/2`,
```
E_a(floor(a^{-1}(log(1/a))^K)) = o(a);
E_a(floor(a^{-1} exp((log(1/a))^gamma))) = o(a).
```
The little-o statements concern the indicated moving horizons and do NOT estimate the entire infinite escaping tail.

More generally, if `h(a)>=0` and `h(a)=o(sqrt(log(1/a)))`, then
```
E_a(floor(a^{-1}exp(h(a))))=o(a).
```

## Proof

We reuse the proved exact first-order decomposition (fixed `N>=1,a>0`) from
`research_notes/driver/2026-11-15_rh_road_small_a_primecount_firstorder_pnt_nearfield.md`:
```
B_{a,N} = a (psi(N)-N-1/2) + e_{a,N},
|e_{a,N}| <= a^2 N [ (3/4)(log N)^2 + 1 + 1/(2N) ],
psi(x)=sum_{p^j<=x} log p.
```
It follows by splitting prime powers from numbers with >=2 distinct prime factors, and bounding `0 <= x-(1-e^{-x}) <= x^2/2`; its proof and constant normalization are already saved. Set
`q_N=(psi(N)-N-1/2)/N`.
For `L>=2`, squaring with `(u+v)^2<=2u^2+2v^2` yields
```
E_a(L) <= 2a^2 sum_{N<=L} q_N^2
        +2a^4 L [(3/4)(log L)^2+3/2]^2.                 (1)
```

Use the **classical unconditional quantitative prime number theorem**, in the standard de la Vallée Poussin form: there exist constants `c>0,C>0` such that for every real `x>=2`,
```
|psi(x)-x| <= C x exp(-c sqrt(log x)).
```
The harmless `1/(2N)` term in `q_N` can be absorbed by changing the positive constants. Hence
```
|q_N| <= C_1 exp(-c_1 sqrt(log N))  (N>=2),              (2)
```
and `q_N` is bounded also at `N=1`. Split the sum at `sqrt L`. There are at most `sqrt L+1` low terms, each bounded. For high terms `sqrt L < N <=L`, `log N >=(log L)/2`; (2) gives
```
sum_{N<=L} q_N^2
 <= C_2 [sqrt L+1 + L exp(-c_2 sqrt(log L))]            (3)
```
for some absolute `C_2,c_2>0` and all `L>=4`.

Substitute (3) in (1) to obtain the explicit-shape uniform estimate
```
E_a(L) <= C_3 a^2 [sqrt L+1+L exp(-c_2 sqrt(log L))]
        + C_3 a^4 L (1+log L)^4,                         (4)
```
where `C_3` is an absolute positive constant.

Put `t=log(1/a)->infinity`, `L=floor(a^{-1}e^{h(a)})`, where `h(a)>=0`, `h(a)=o(sqrt t)`. Then `L=(1+o(1))a^{-1}e^{h(a)}` and `log L=t+h(a)+o(1)`. Dividing (4) by `a`, the first summand is
`a sqrt L=O(exp(-t/2+h/2))=o(1)`, the second is
`a L exp(-c_2 sqrt(log L))=O(exp(h-c_2 sqrt(t+h+o(1))))=o(1)`, and the last is
`a^3 L(1+log L)^4=O(exp(-2t+h)(1+t+h)^4)=o(1)`.
This proves the general assertion.

Choose `0<delta<c_2`, for instance `delta=c_2/2`. The same analysis then works for the fixed stretched-exponential horizon `L_delta(a)` (because `delta sqrt t-c_2 sqrt(t+delta sqrt t+o(1))->-infinity`). The polylogarithmic and `gamma<1/2` cases follow directly from the general assertion. QED.

## Mathematical contribution and limitation

This extends the rigorously controlled `o(a)` window from fixed multiples of `1/a` to every polylogarithmic multiple and a sub-square-root-logarithmic stretched-exponential factor, using the established quantitative prime number theorem. It is a genuine partial result for the moving full-integer composite road, not a uniform all-scale estimate. It isolates all as-yet-uncontrolled order-`a` energy beyond `L_delta(a)`; it does not resolve the tail `N>L_delta(a)`, the spectral phase-dependent interface, or the RH parent target.

## Provenance and validation boundary

- Previous exact expansion + PNT fixed-`T/a` theorem: `049192c481c7f5c9e838772ab08e2afa95a354e9`, `research_notes/driver/2026-11-15_rh_road_small_a_primecount_firstorder_pnt_nearfield.md`.
- Previous elementary `O(a)` bound: `1668ed1b7830dfd9892d4790563e47567792fdfb`.
- Frozen source/definition is the original `RH-ROAD-TAIL-20260909` branch, preserving EM-FREE-C4A91D authorship.
- The only external mathematical input beyond previously saved local estimates is the standard quantitative PNT error bound shown above. The proof is symbolic and uses real-variable inequalities; neither a new finite experiment nor an original Python/Lean checker run is claimed.
- No native RR/DR admission, source independent reviewer disposition, Task DONE or parent objective DONE follows from publication.
