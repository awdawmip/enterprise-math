# D25 CM(−24): Hasse first-jet Frobenius eigenline

Date: 2026-11-05. Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific input pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Status: AUTHOR-DERIVED / EXACT FINITE-FIELD PROOF / FINITE-EXACT CHECKED / UNREVIEWED / NOT_ADMITTED. This is a Legendre/CM observer, NOT the native H0/B0 crystalline experiment.

## Theorem

For every prime `p>=5, p=5 (mod 8)`, set `m=(p-1)/2`, `Q=t^4-140t^3+294t^2-140t+1`, `A=F_p[t]/(Q)`, `H=sum_{j=0}^m binom(m,j)^2 t^j`. Use the previously established exact CM Frobenius branch

- `f=t^p=(7-5t)/(5-7t)` when `p=5 (mod 24)`;
- `f=t^p=(5-7t)/(7-5t)` when `p=13 (mod 24)`.

Define `s=-(1+f)/(2(1+t))`; the existing 2-isogeny establishes `s^2(1-t)^2=f`, `s*s^p=1/4`, `H(f)=s^m H(t)`. Define

```
C=16t(1-t^2)H'(t)+(1+2t-7t^2)H(t),
h=(1+2t-7t^2)/(16t(1-t^2)),  V=H'+hH,
D=-4f(1+f)/((1-t^2)(1-f)),  B=s^m.
```

Then, **unconditionally in A**,

```
D*D^p=1,    D*V^p=B*V,
C^p=Gamma*C,  Gamma=-4*s^(m+2),  Gamma*Gamma^p=1.
```

The theorem covers the split and inert CM classes. `C=0` for all split primes remains a separate open assertion; the first-jet eigenline identity is proved without assuming it.

## Proof

Before specializing to `Q=0`, take a global Legendre Landen branch over `F_p(u)`:
`t=u^2`, `f_L=((1-u)/(1+u))^2`, `s_L=-1/(1+u)^2`. The normalized separable 2-isogeny with kernel `(0,0)` gives the Hasse relation `H(f_L)=s_L^m H(t)`; for this even `m` it can also be verified as the exact finite polynomial identity

```
sum_{j=0}^m binom(m,j)^2 (1-u)^(2j) (1+u)^(2(m-j))
  = H(u^2)  (mod p).
```

Differentiate this global identity **before** imposing the CM polynomial. For the global branch derivative `D_L=df_L/dt=-4f_L(1+f_L)/((1-t^2)(1-f_L))` one obtains
`D_L H'(f_L)=s_L^m(H'+beta_L H)`, where `beta_L=m d(log s_L)/dt`.

On `Q=0`, the choice `u=(1+t)(1-f)/(2(1+f))` obeys `u^2=t`, `f_L=f=t^p`, `s_L=s`, and, because `m=-1/2 (mod p)`,

```
beta = -(1/2)*(D/(1+f)-1/(1+t)).
D*(H')^p = B*(H'+beta*H).
```

A direct **rational identity over Q(t)**, valid for both displayed Möbius branches, is

```
D*h(f)-h(t)+beta = Q(t)/(16*t*(t-1)*(t+1)^3).
```

It vanishes in A. Adding the correction `hH` to the differentiated Hasse relation, and using `H(f)=H(t)^p=B H(t)`, yields `D V^p=B V`.

Since `C=16t(1-t^2)V`, we obtain `C^p=-B*(1-f)^2/(4t)*C`. For `L=5-7t` (split) or `L=7-5t` (inert), another **rational identity over Q(t)** is

```
(1-f)^2/(4t) - 4*s^2 = Q(t)/(t*(1+t)^2*L(t)^2).
```

Thus `C^p=-4s^(m+2)C`. Since `s s^p=1/4` and `4^m=1` in F_p, `Gamma Gamma^p=16*4^(-m-2)=1`. The identity `D D^p=1` follows from `D D^p-1=-Q(t)/((t-1)^2(t+1)^2)`, again an exact rational identity. All denominators are units: `Res(Q,t)=1`, `Res(Q,1-t)=16`, and `Res(Q,1+t)=Res(Q,5-7t)=Res(Q,7-5t)=576`. Q is separable since `Disc(Q)=2^32*3^6`. Q has no linear root because the resultants of Q with `f(t)-t` numerators are `2^18*3^4` and `2^16*3^4`. Hence `A=F_{p^2} x F_{p^2}`. QED.

## New scalar frontier

In each of the two quadratic components, `Gamma` has norm one. The solution set `X^p=Gamma X` is exactly a 1-dimensional F_p-line (Hilbert 90). When `Gamma != -1`, a nonzero basis is `v=1+Gamma^(-1)`; in the `Gamma=-1` case use any nonzero trace-zero element, e.g. `sqrt(2)`, since 2 is nonsquare for p=5 (mod 8). Our actual `C` is on this line. Therefore a normalized single F_p coordinate *per quadratic orbit* suffices to decide whether C vanishes. This scalar is not fixed by the Hasse scale equation alone; computing it from an independent CM/quasi-period or finite coefficient functional is the next exact research unit. It retains the separate Frob orbits and derivative/branch provenance instead of collapsing them to a norm-only Boolean.

## Evidence and continuation

The attached stdlib exact quotient-ring checker executes for every prime 5<=p<=5000 with p=5 (mod8). Actual run: **168 PASS (85 split, 83 inert)** for `t^p=f`, `s s^p=1/4`, `H^p=s^mH`, `D D^p=1`, `D V^p=B V`, `C^p=Gamma C` and `Gamma Gamma^p=1`. At p=29, `C=(0,0,0,0)`; at p=373, `C=(349,260,82,367)` and `Gamma=(99,177,87,117)` in the ordered basis `(1,t,t^2,t^3)`. Exact checks corroborate the algebraic proof but are not used as proof of the split-class vanishing.

BRC usage resolution: COMPOSE_APPLIED to the existing Legendre/CM semilinear source/first-jet observer, retaining signed C and full four-coordinate provenance; positive-mass BRC is not a substitute for this finite-field cancellation. Task parent OPEN. Next: construct the missing one-coordinate-per-orbit readout and prove its split vanishing; then use earlier Jacobi–Green–Wronskian p² correction. Separately obtain authenticated original-class p=373 H0/B0 divided-power, [X]U mod p², semilinear η, κ and Δ−R. Existing Source checkpoint and contributors are preserved; native CLAIM/OPEN/checkpoint/Result/review/admission are not asserted.
