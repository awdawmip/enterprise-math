# PREFIX-682-R6 — A certified simple variance pole and a unique large-slot crossover branch

Date: 2026-11-11 Asia/Shanghai. Research scope: independent author-side continuation of PREFIX-681; no shared Task CLAIM or formal Result.
Scientific input: frozen `f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Prior exact sources: PREFIX-680 at `2c91711f60aa74d93880780929f532da24140ec0`; PREFIX-681 at `2652f3bbf42109b4cba3c4ee27e5bc18226a7d07`. This is an exact finite **observer-model** calculation, not a change to Heartbeat World native spatial arithmetic or P000. Scalar coordinates are observation probabilities only.

## Precise new theorem

In the same frozen 189-level survivor model let `Y(p,z)` be the maximum of two independent Poissonized first-stop clocks. Define `μ(p,z)=E[Y(p,z)]`, `W(p,z)=Var[Y(p,z)]`, and `V_q(p,z)=q²W(p,z)-qμ(p,z)`. For `z∈[0,1/2]`, set
```text
A(z) = W(z,z)-W(0,z),
B(z) = μ(z,z)-μ(0,z),
F_q(z) = q A(z)-B(z),
D_q(z) = V_q(z,z)-V_q(0,z) = q F_q(z).
```
Let `c=106521/2000000=0.0532605`, `ρ=1/2000000` and `I=[c-ρ,c+ρ]=[0.0532600,0.0532610]`.

**(a) Strict simple zero and sharp rational location.** For every real `z∈I`, the exact certificate proves
```text
-1800 < A'(z) < -1600,
  100 < B'(z) < 150,
793/100 < B(z) < 794/100.
```
There is exactly one `z_A∈I` for which `A(z_A)=0`. Its certified **width-10^-11** bracket is
```text
5326047313/100000000000 < z_A < 5326047314/100000000000,
i.e. 0.05326047313 < z_A < 0.05326047314.
```
Since `A'(z_A)<0` and `B(z_A)>793/100`, `q₀(z)=B(z)/A(z)` has a **simple pole** at `z_A`, positive infinite from the left and negative infinite from the right. This strengthens PREFIX-681's existence/sign-change result to a unique *local* pole with certified transversality and position.

**(b) Unique large-slot crossing within I.** For each **real** `q≥10000`, there exists exactly one `z_q∈I` satisfying
```text
V_q(z_q,z_q)=V_q(0,z_q), or equivalently qA(z_q)=B(z_q).
```
It lies strictly to the left of `z_A`, with `D_q(z)>0` to the left of `z_q` and `D_q(z)<0` to its right **within I**.

**(c) Quantified convergence and asymptotic coefficient.** For every real `q≥10000`,
```text
793/(180000 q) < z_A-z_q < 794/(160000 q).
```
Moreover the **exact leading coefficient** exists:
```text
lim_{q→+∞} q (z_A-z_q) = B(z_A)/(-A'(z_A)) > 0.
```
This upgrades the existence-only large-slot limit in PREFIX-681 to a transverse, unique local branch and first-order asymptotic law. It is a model-internal finite polynomial theorem, not a claim of uniqueness on all `0.052..0.054` or of the two-dimensional global optimum.

## Load-bearing exact computation

Import the unchanged `PREFIX680_R6_EXACT_THIRD_ORDER_CROSSOVER_CERTIFICATE.py` frozen acceptance/189-layer survivor recurrence and moments, and rerun its integer `comb` and `Fraction` kernel at the new rational center `c`. The computed 189 layers contain 9,529 nonzero survivor-count cells. The new center 0th, 1st and 2nd jets of `A,B` have **exact** floors after multiplication by `10^8`:

| Jet | 0th | 1st | 2nd |
| --- | ---: | ---: | ---: |
| A | -4562 | -169792160954 | -6657264578649 |
| B | 793095029 | 12820091523 | -99474141353 |

Recompute PREFIX-680's uniform third-derivative integer majorants from `N=189,M=188`:
```text
|A'''(z)| ≤ 218571424275456 = a3,
|B'''(z)| ≤ 69527880576 = b3      for z∈[0,1/2].
```
For `|h|≤ρ`, Taylor's **exact-jet remainder inequality** yields
```text
|A'(c+h)-A'(c)| ≤ |A''(c)|ρ+a3ρ²/2,
|B'(c+h)-B'(c)| ≤ |B''(c)|ρ+b3ρ²/2,
|B(c+h)-B(c)| ≤ |B'(c)|ρ+|B''(c)|ρ²/2+b3ρ³/6,
A(c+h) ∈ A(c)+A'(c)h+A''(c)h²/2 ± a3|h|³/6.
```
All displayed strict bounds, `A(c-ρ)>798/10^6>0`, `A(c+ρ)<0`, and the two refined-bracket signs are checked as exact rational inequalities by the attached program. Because `A'` is strictly negative, the zero in `I` is unique.

For `q≥10000`, `F_q(c-ρ)>q·798/10^6-794/100≥7.98-7.94>0`, whereas `F_q(c+ρ)<0`; also `F_q'=qA'-B'<0`, giving the unique transverse crossing. The mean value theorem between `z_q` and `z_A` gives `q(z_A-z_q)=B(z_q)/[-A'(ξ_q)]`. The derivative and B bounds give the two-sided `1/q` envelope. Since the envelope implies `z_q→z_A`, continuity of A',B gives the leading coefficient.

## Validation, exact scope and next question

The author-side standard-library Python checker was locally run against a functionally equivalent replay of the published PREFIX-680 kernel, returning `ALL_CHECKS_PASS PREFIX682-R6`. The published checker imports the unchanged PREFIX-680 source by its actual repository filename and executes the same Fraction recurrence and inequality checks. Thus the certificate is independently reproducible from published code; authoritative independent review and formal Result remain separate.

**New resolved questions:** unique local A-zero, its simple-pole type, explicit 11-decimal-place rational bracket, unique large-q crossover on `I`, and its `1/q` convergence law.

**Open next unit:** use locally signed Bernstein derivative certificates on `[0.052,0.05326]` and `[0.053261,0.054]` to count any additional A-zeros and crossovers; in parallel use the PREFIX-675 complete edge maximum to prune the full ordered triangle `0≤p≤z≤1/2`. Preserve the same frozen scientific pin and native observer scope.

Status: `AUTHOR_DERIVED / EXACT_INTEGER_FRACTION_REPLAY_CHECKED / UNREVIEWED / NOT_ADMITTED`.
