# RH full-integer composite road: Vinogradov–Korobov near-field extension

Date: 2026-11-15
Status: SCOPED MATHEMATICAL DRIVER DERIVATION; no independent native Result admission, no all-scale escape-tail bound, no RH proof.
Derivative author: RESEARCH_DRIVER EM-DVR-DEBB5E.
Original program/contribution: EM-FREE-C4A91D, formal task RH-ROAD-TAIL-20260909 / TP2-DCE65A0EFCE8151C39BD. Preserve the independent researcher/owner and the distinct review boundary.

## Setup and exact inherited arithmetic input

For a>0 and positive integer N let

```
R_a(1)=1;
R_a(n)=prod_{p|n} (1-p^{-a})   (n>=2);
S_a(N)=sum_{n<=N} R_a(n);
c_a=1/zeta(1+a);
B_{a,N}=S_a(N)-1-(N+1/2)c_a;
E_a(L)=sum_{1<=N<=L} B_{a,N}^2/N^2;
psi(N)=sum_{p^k<=N} log p.
```

All positive integers, including products of distinct primes, remain in the road. The inherited exact elementary expansion from
`research_notes/driver/2026-11-15_rh_road_small_a_primecount_firstorder_pnt_nearfield.md` (commit `049192c481c7f5c9e838772ab08e2afa95a354e9`) states, for **all** a>0,N>=1,

```
B_{a,N}=a(psi(N)-N-1/2)+e_{a,N},
|e_{a,N}| <= a^2 N [(3/4)(log N)^2+1+1/(2N)].
```

The previous quantitative-PNT note (commit `23e8a6256a91316e38a949d317156085aabc49ce`) used the weaker de la Vallée Poussin error `exp(-c sqrt(log N))`, obtaining an `o(a)` window up to `a^{-1} exp(delta sqrt(log(1/a)))`.

## Imported classical input, not a new prime number theorem

The unconditional Vinogradov–Korobov prime number theorem provides some absolute constants `c>0`, `C>0`, `x_0>e^e` with

```
|psi(x)-x| <= C x exp(-c Phi(log x)),     x>=x_0,
Phi(u)=u^(3/5) (log u)^(-1/5)            (u>e).
```

This is a previously established external theorem, not proved here. The constants are existential; no explicit numerical c or finite-size threshold is claimed. References: Daniel R. Johnston, "Zero-density estimates and the optimality of the error term in the prime number theorem", arXiv:2411.13791 (2024), https://arxiv.org/abs/2411.13791 ; Chiara Bellotti, "A new zero-density estimate for zeta(s) and the error term in the Prime Number Theorem", arXiv:2508.02041 (2025), https://arxiv.org/abs/2508.02041 . Both discuss the known Vinogradov–Korobov scale for the error in psi(x). Only the existence of a positive constant c is used.

## Summability lemma (preserves the full exponent)

**Lemma.** For any fixed c>0, choose an integer N_0>exp(e) so large that 2c Phi'(log x)<=1/2 for all x>=N_0. There exists C_c>0 such that, for every integer L>=N_0,

```
sum_{N_0<=n<=L} exp(-2c Phi(log n)) <= C_c [1+L exp(-2c Phi(log L))].
```

Only integers n>=N_0 occur in this expression, so Phi(log n) is defined. The finitely many smaller indices of the eventual q_N sum are handled separately.

**Proof.** For u>e,
```
Phi'(u)=u^(-2/5) (log u)^(-1/5) [3/5-1/(5 log u)] -> 0.
```
For x>=N_0, set f(x)=exp(-2c Phi(log x)). Then f is positive and decreasing, and
```
d[x f(x)]/dx=f(x)[1-2c Phi'(log x)] >= f(x)/2.
```
Thus `integral_{N_0}^L f(x) dx <= 2L f(L)+O_c(1)`. Integral comparison for decreasing positive f yields the displayed bound (enlarging C_c for the initial endpoint). QED.

## Theorem: expanded uniform o(a) moving window

Let `t=log(1/a)` and `G(t)=t^(3/5) (log t)^(-1/5)`. For the c supplied by the imported Vinogradov–Korobov estimate, and **every fixed** real delta with `0<delta<2c`, define

```
L_delta(a)=floor(a^(-1) exp(delta G(t))).
```

Then, as a->0+,

```
E_a(L_delta(a)) = o(a).
```

In particular `E_a(floor(a^(-1) exp(h(a))))=o(a)` whenever `h(a)>=0` and `h(a)=o(G(log(1/a)))`.

**Proof.** Define `q_N=(psi(N)-N-1/2)/N`. The imported PNT bound, plus `1/N <= C exp(-c Phi(log N))` for all N>=N_0 after enlarging N_0, yields

```
|q_N| <= C' exp(-c Phi(log N)).
```

By the lemma and a finite bound on the omitted indices N<N_0, `sum_{N<=L}q_N^2 <= C''[1+L exp(-2c Phi(log L))]` for L>=N_0. Use the inherited exact first-order decomposition and `(u+v)^2<=2u^2+2v^2`:

```
E_a(L) <= C_1 a^2 [1+L exp(-2c Phi(log L))]
           + C_1 a^4 L (1+log L)^4,    L>=N_0.          (1)
```

Take `L=floor(a^(-1) exp(h))` where `0<=h<=delta G(t)`. Because `G(t)=o(t)`, we have

```
log L=t+h+o(1),
Phi(log L)=G(t)(1+o(1)),
aL=exp(h)(1+o(1)).
```

Dividing (1) by a gives the three upper-bound terms

```
O(a),
O(exp(h-2c G(t)(1+o(1)))),
O(a^2 exp(h)(1+t+h)^4).
```

The first and third tend to zero, since `h=O(G(t))=o(t)`. The middle tends to zero uniformly when `h<=delta G(t)` and `delta<2c`. For `h=o(G(t))`, choose any such fixed delta eventually. This proves both statements. QED.

## Exact advance, non-advance, and next obligation

The previous `exp(delta sqrt(log(1/a)))` near-field horizon is strictly improved to a Vinogradov–Korobov horizon `exp(delta (log(1/a))^(3/5)/(log log(1/a))^(1/5))`. The unsquared external PNT exponent c is preserved with multiplier 2c in the energy window by the summability lemma (rather than lost in an arbitrary square-root split). This is a **derived implication of established unconditional prime-number-theorem estimates**, not a newly proved PNT improvement. No statement is made at the boundary delta=2c.

The open RH-ROAD-TAIL task still requires a genuinely uniform control of the escaping infinite tail `N>L_delta(a)` as a->0+. The proof provides neither that control nor RH, parent completion, an independent reviewer finding, or native Result acceptance. A future native review must inspect this exact statement and all dependencies; authorship is not independent of this Driver note. No CLAIM or researcher ownership has been transferred.

## Provenance and verification

Arithmetic expansion: original full-integer note commit `049192c481c7f5c9e838772ab08e2afa95a354e9`.
Predecessor quantitative near-field: commit `23e8a6256a91316e38a949d317156085aabc49ce`.
External theorem: cited Vinogradov–Korobov-scale references above.
Validation: line-by-line symbolic derivative, integration and asymptotic argument; no Python/Lean build asserted. Existing saved Result status unchanged.
