# S23 shared-parameter AV observer: all-n Blackwell extremal fiber theorem and the exact n=4 fiber diameter

2026-11-06. Author-side mathematical proof, with exact rational executable checks. Frozen scientific input: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Prior n=2 exact theorem and n=3 exact fiber theorem: Draft PR #1777, commits `a8b13eb9b5f4fad53663f7d93b808ae181bdf547` and `19e92b1ef3f481397437c5d4be9b2c65f153e348`. This concerns the auxiliary conditional AV statistical experiment; original ten-label S23 encoder/decoder bridge is a separate research question.

## Domain, observation and quantity

For real `a,c ∈ [1/2,7/8]`, let `z=(1-a)c` and `P(a,z)=(a,z,1-a-z)` on labeled stops (1,3,4). Its binary third-stop observer is `B(z)=(z,1-z)`. For `n>=1`, the same unknown `(a,c)` governs n conditionally IID trials. Denote the maximal complete-observation fiber diameter

`D_n = sup { TV(P(a,z)^⊗n,P(a',z)^⊗n): both parameters legal and share z }`.

The reconstruction deficiency is

`δ_n = inf_{single parameter-independent stochastic L:{Y,N}^n->{1,3,4}^n} sup_(a,c) TV(P(a,z)^⊗n,B(z)^⊗n L)`.

## New theorem: a fixed experiment dominates every fiber for every n

**Theorem.** For every integer `n>=1`,

`D_n = TV(P0^⊗n,P1^⊗n)`, with `P0=(1/2,1/4,1/4)` and `P1=(5/7,1/4,1/28)`.

More strongly, for **every** legal shared-z pair with its first-stop masses ordered, there exists one three-to-three Markov kernel sending the pair of experiment laws `(P0,P1)` to that selected pair. It follows, for all n, from tensoring this same kernel n times and TV data processing that the displayed pair globally maximizes the fiber distance. Both reference parameters are legal: `(a,c)=(1/2,1/2)` and `(5/7,7/8)`.

### Proof, step 1: exact legal fibers

`1/16<=z<=7/16`. At fixed z, the first-stop mass lies in the closed interval

`L(z)=max(1/2,1-2z) <= a <= H(z)=min(7/8,1-8z/7)`.

These inequalities are equivalent to `c=z/(1-a)∈[1/2,7/8]` and `a∈[1/2,7/8]`. Put `E_L(z)=P(L(z),z)`, `E_H(z)=P(H(z),z)`, `z_0=7/64`, `z_*=1/4`, `z_min=1/16`, `z_max=7/16`.

### Proof, step 2: every pair of endpoint laws is a common garbling of (P0,P1)

We use a common Markov operation `M_{t,R}` that sends any distribution P to `t P+(1-t)R`, where `t∈[0,1]` and R is fixed independently of which of the two hypotheses generated P. The operation is row-stochastic: output the input symbol with probability t, otherwise sample R.

On `z∈[z_0,z_*]`, both endpoint laws obey the **exact affine identity**

`E_i(z)=4z P_i+(1-4z)(1,0,0)`, `i∈{L,H}` with `P_L=P0,P_H=P1`.

On `z∈[z_min,z_0]`, set `t=(z-z_min)/(z_0-z_min)`, and `R_min=(7/8,1/16,1/16)`. Both endpoints satisfy

`E_i(z)=t E_i(z_0)+(1-t)R_min`.

On `z∈[z_*,z_max]`, set `t=(z_max-z)/(z_max-z_*)`, and `R_max=(1/2,7/16,1/16)`. Both endpoints satisfy

`E_i(z)=t P_i+(1-t)R_max`.

All three formulas are exact coordinatewise identities of affine rational functions. Their mixing coefficients belong to [0,1]. In the low-z interval compose the first and second common channels. Consequently the two endpoint distributions at every z are jointly obtained from (P0,P1) by one Markov kernel.

### Proof, step 3: every ordered interior pair is a common garbling of its endpoints

At fixed z, put `N=1-z`, `L=L(z)`, `H=H(z)`. If L=H there is only one law and the assertion is immediate. Otherwise choose `L<=x<=y<=H` and define

`t=(y-x)/(H-L), v=(x-t L)/N, u=v+t`.

The channel keeps stop 3 unchanged, sends an input 1 to 1 with probability u (otherwise 4), and sends an input 4 to 1 with probability v (otherwise 4). Its output first-stop mass from input P(a,z) equals

`u a+v(N-a)=t a+v N`, hence maps E_L to P(x,z) and E_H to P(y,z). It is stochastic: `t∈[0,1]` and `v>=0`. To check `u<=1`, write `x=L+α(H-L)`, `y=L+β(H-L)`, with `0<=α<=β<=1`. The formula for u is affine on this triangle, and at vertices (0,0),(0,1),(1,1) it equals L/N,1,H/N, respectively, all in [0,1]. Then `0<=v<=u<=1`. This completes the channel construction.

Composition gives a **single common channel** mapping (P0,P1) to any such ordered pair. Tensor power preserves its hypothesis independence. The data-processing inequality for TV proves `D_n<=TV(P0^⊗n,P1^⊗n)`; equality is obtained from the reference pair itself. QED.

## Exact formula, explicit n=4 value, and the n=7 regime change

For `i+j+k=n`, the ordered outcome type contributes multinomial weight `n!/(i!j!k!)`. The finite exact formula is

`D_n = (1/2) Σ_(i+j+k=n) [n!/(i!j!k!)] |(1/2)^i(1/4)^(j+k)-(5/7)^i(1/4)^j(1/28)^k|`.

The likelihood ratio of reference law P1 to P0 on this outcome type is `(10/7)^i (1/7)^k`. For `1<=n<=6`, this exceeds one precisely when `k=0,i>=1`: for any k>=1, it is at most `(10/7)^(n-1)/7 <= 10^5/7^6 < 1`. Thus summing positive differences yields the particularly simple exact identity

`D_n=(27/28)^n-(3/4)^n` for `1<=n<=6`.

In particular, **`D_4=5265/9604`**, while `D_3=5211/10976` agrees with the earlier derivation. At n=7 the type (i,j,k)=(6,0,1) changes sign; the extra positive likelihood mass is exactly `176457/30118144`, so the n<=6 formula must not be extrapolated. The exact value is `D_7=4369158699/6746464256`.

## Deficiency corollaries and information meaning

For every n the pair P0,P1 produces the same binary experiment B(1/4)^⊗n. Any common reconstruction therefore outputs the same Q under the two hypotheses. The TV triangle inequality yields `δ_n>=D_n/2`. At n=4,

`5265/19208 <= δ_4 <= 801/2401`.

The upper bound uses the previously source-published fixed two-trial kernel L2 with uniform error `9/49`, applied independently to two blocks: `L4=L2⊗L2`, with `TV<=1-(1-9/49)^2=801/2401`. This is a constructive bound inherited from the author-side n=2 exact certificate and is not asserted sharp for n=4.

The Bhattacharyya affinity `ρ=√(5/14)+1/4+1/√112<1` obeys `1-TV(P0^⊗n,P1^⊗n)<=ρ^n` by the coordinatewise inequality min(p,q)<=√(pq). Thus `D_n>=1-ρ^n` and `lim_(n→∞) D_n=1`. Consequently `liminf δ_n>=1/2`. This describes the retained hidden first/fourth split at arbitrarily many trials, in an explicitly scoped positive-measure BRC observer fiber.

## Validation, scope and next question

`VERIFY.py` runs only exact `fractions.Fraction` arithmetic and checks the n=1..8 formula, the n=4 and n=7 constants, 99 legal rational z mixtures, and a family of interior-pair channels (978 exact checks). Its real-domain general theorem is proved above by Markov composition, not inferred from finite tests. Actual program stdout: `RUN_EVIDENCE.txt`. This is author mathematical evidence, awaiting independent review. The open next unit is to construct and certify a joint 16×81 reconstruction kernel for n=4 or strengthen its minimax lower bound beyond the fiber radius, and separately study the lawful ten-label S23 bridge to `R_beh(k,10)`.
