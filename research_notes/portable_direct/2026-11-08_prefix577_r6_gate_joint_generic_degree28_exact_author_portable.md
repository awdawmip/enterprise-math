# PREFIX-577 R6 — exact generic degree 28 of first-gate joint generating function

**2026-11-08 / author-only / UNREVIEWED / NOT_ADMITTED.** Scientific input pin `f42f2906d77f24085c123f3ccfe9667d41caa96d` unchanged.

## Result

Retain the original 96 ports with all 576 original tagged actions and six native spatial reward axes. Consider only the declared *passive* first gate return readout from port 9, root zero: `T` is the first gated step, `U,V` the cumulative fifth and sixth axis rewards. Each original action is independently selected with probability 1/6. Let `C(x,y)` count nongated original actions with weight `x^R5 y^R6`, `g` the original gated action-weight vector, and `s_n(x,y)=e_9^T C(x,y)^n g(x,y)`. Then

```
F(z,x,y) = E[z^T x^U y^V] = (z/6) * sum_{n>=0} s_n(x,y) * (z/6)^n.
```

**Theorem:** Over `Q(x,y)`, the reduced denominator of `F(z,x,y)` with respect to `z` has **degree exactly 28**. This closes the earlier interval `28 <= degree <= 34` (author note `0d6ca30199b4716c5e2e0409e4eefcf6881e4fa7`).

An explicit polynomial denominator `Q(t,x,y)=sum_{k=0}^{28} Q_k(x,y)*t^k`, with `Q_0=1` and every odd `Q_k=0`, satisfies `Q(t,x,y)*sum(s_n*t^n)=P(t,x,y)` with `deg_t P<=27`. All even coefficients are completely specified below: for each key `k`, each triple `[a,b,c]` contributes `c*x^a*y^b` to `Q_k(x,y)`.

```json
{"0":[[0,0,1]],"2":[[0,0,-8]],"4":[[0,0,4],[0,1,-152],[1,0,-152],[1,1,-336]],"6":[[0,0,96],[0,1,832],[0,2,-2480],[1,0,832],[1,1,-7008],[2,0,-2480]],"8":[[0,0,-192],[0,1,256],[0,2,2176],[1,0,256],[1,1,20928],[1,2,-78336],[2,0,2176],[2,1,-78336],[2,2,35328]],"10":[[0,1,-4608],[0,2,6400],[0,3,-23040],[1,0,-4608],[1,1,49152],[1,2,115200],[1,3,182528],[2,0,6400],[2,1,115200],[2,2,-274944],[3,0,-23040],[3,1,182528]],"12":[[0,2,73728],[0,3,-178176],[0,4,552960],[1,1,-46080],[1,2,104448],[1,3,260096],[2,0,73728],[2,1,104448],[2,2,2660352],[2,3,3534848],[3,0,-178176],[3,1,260096],[3,2,3534848],[3,3,-1220608],[4,0,552960]],"14":[[0,3,983040],[0,4,2408448],[1,2,2064384],[1,3,-3764224],[1,4,10764288],[2,1,2064384],[2,2,-909312],[2,3,5292032],[2,4,-7999488],[3,0,983040],[3,1,-3764224],[3,2,5292032],[3,3,17801216],[4,0,2408448],[4,1,10764288],[4,2,-7999488]],"16":[[0,4,-16515072],[0,5,-15335424],[1,3,1179648],[1,4,21037056],[1,5,-8847360],[2,2,-25657344],[2,3,24707072],[2,4,-61636608],[3,1,1179648],[3,2,24707072],[3,3,-21987328],[3,4,14548992],[4,0,-16515072],[4,1,21037056],[4,2,-61636608],[4,3,14548992],[4,4,17104896],[5,0,-15335424],[5,1,-8847360]],"18":[[0,5,56623104],[1,4,-226492416],[1,5,-243007488],[2,3,-346816512],[2,4,-902627328],[2,5,-53084160],[3,2,-346816512],[3,3,-326762496],[3,4,-1115553792],[3,5,91422720],[4,1,-226492416],[4,2,-902627328],[4,3,-1115553792],[4,4,-631111680],[5,0,56623104],[5,1,-243007488],[5,2,-53084160],[5,3,91422720]],"20":[[1,5,1019215872],[2,4,4586471424],[2,5,3515351040],[3,3,806879232],[3,4,-3194486784],[3,5,-1807220736],[4,2,4586471424],[4,3,-3194486784],[4,4,2437152768],[4,5,-806879232],[5,1,1019215872],[5,2,3515351040],[5,3,-1807220736],[5,4,-806879232],[5,5,-84934656]],"22":[[2,5,-12230590464],[3,4,26499612672],[3,5,38532022272],[4,3,26499612672],[4,4,137027911680],[4,5,43146805248],[5,2,-12230590464],[5,3,38532022272],[5,4,43146805248],[5,5,7134511104]],"24":[[3,5,-122305904640],[4,4,-510627151872],[4,5,-566684024832],[5,3,-122305904640],[5,4,-566684024832],[5,5,-190593368064]],"26":[[4,5,1541054398464],[5,4,1541054398464],[5,5,1687821484032]],"28":[[5,5,-3962711310336]]}
```

In particular `Q_2=-8`, `Q_4=4-152(x+y)-336xy` and `Q_28=-3962711310336*x^5*y^5`. Every coefficient is symmetric under `x↔y`; maximum individual variable degree is 5.

## Exact proof and reproduction scope

1. Original-port to 37-class passive quotient: each of the 576 native tagged edges is rechecked against its exact class-multiplicity/axis-reward/gate signature. The 37-state quotient preserves the passive finite-horizon readout. The action-conditioned 51-state interface remains distinct.
2. Modular interpolation using `1000000007` and `1000000009` *discovers* the displayed integer coefficient polynomials. That sampling is not the proof.
3. Independently compute the original native **96-port** path generating polynomials `s_n∈Z[x,y]` for `n=0..64`. For every `n=28..64`, multiply the displayed `Q_k` and check the entire integer polynomial identity `sum_{k=0}^{28}Q_k s_{n-k}=0` coefficient-by-coefficient. All **37** consecutive identities vanish exactly. The 37-state quotient implementation independently obtains the same vanishing.
4. For the exact 37×37 polynomial transfer `C37(x,y)`, let `w=sum_{k=0}^{28}Q_k C37^(28-k)g`. The residual sequence is `r_{28+m}=e_[9]^T C37^m w`. Cayley–Hamilton of the **37-state exact quotient** forces a recurrence of order ≤37 for the residual sequence. Its first 37 values are identically zero, so every subsequent residual vanishes. Thus the denominator has degree at most 28 over `Q(x,y)`.
5. **Independent lower bound:** the native 96-state integer weighted-path recurrence at `(x,y)=(2,3)` modulo `1000000007` has nonzero 28×28 Hankel determinant `595325725`. Hence reduced generic degree is at least 28. The two bounds coincide.

**Author verification record:** The native 96-edge comparison, exact polynomial identities `n=28..64`, modular nonzero Hankel witness and two-prime reconstructed coefficient list were locally executed. Certificate `GENERIC_DEGREE28_CERTIFICATE.json` SHA-256 `d7416a802b176c6440b9f24a93638c1e6845fc1f594d4b6ec5260345a55db2d4`. Full reproducible author ZIP SHA-256 `838f1f61f91bc9a45f8253d65016fa8d327f4da9e96d9661fb5509925fc7b860`, separately delivered in the task conversation.

## Durable frontier / authority

The exact scalar passive denominator question is solved at the author-proved level. **Next independent scientific unit:** construct an explicit 28-dimensional realization over `Q(x,y)` and exhibit the port-to-observer readout map, without erasing original tag, other axes, source and branch identities. No native D25 result, independent review, or Source CLAIM is implied.

Last read-only Source continuation: task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`, original request `h40-r11-exact-d25-continuation-20261108t2111-v1` SUCCEEDED with `execution_authorized=false`. Own previously registered session lacks current private execution capability, so native checkpoint remains pending. D25 original H0/B0, Frobenius and CM experiments remain independently pending; D24 Result/review terminal. UR original four-file V2 bundle still requires genuine 94,687-byte SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76` provenance.
