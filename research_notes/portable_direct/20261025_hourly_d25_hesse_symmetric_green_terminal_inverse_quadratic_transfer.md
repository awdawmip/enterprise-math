# D25/LIFT — exact symmetric Hesse Green inverse, terminal resonance and mod-p quadratic transfer

2026-10-25 · TASK_RESEARCH / PORTABLE AUTHOR PROOF · UNREVIEWED / NOT_ADMITTED. Target Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`; parent D25/LIFT OPEN. Original frozen scientific Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3` unchanged. This note does **not** assert a native CM/divided-power calculation, authenticated Task owner, mathematical acceptance or independent review.

## Exact inherited input and the new subproblem

For any prime `p=6m+1>=13` write `n=2m=(p-1)/3`, `c_k=(3k)!/(27^k(k!)^3)`, `A_p(X)=sum_{k=0}^n c_k X^k`, `B_p(X)=A_p(1-X)`, `Y=X(1-X)`, `t=1-2X`, and `C=(p+1)c_n/9`. From the previously proved reflection factorization, `A-B=p t Phi(Y)`, `deg(Phi)<=m-1`. From the immediately preceding symmetric-descent result, `G_p(Y)=(A+B)/2` lies in `Z_(p)[Y]`, has degree <=m, and obeys the **exact rational** equation

```
N G_p = -(p C/2) S_n(Y),
N = Y(1-4Y) d_Y^2+(1-6Y)d_Y-2/9,
S_0=2, S_1=1, S_r=S_(r-1)-Y*S_(r-2),
S_n(Y)=X^n+(1-X)^n.
```

Those formulas, and the earlier odd Green inverse for Phi, are consumed as established auxiliary inputs, not recredited. **New task here:** solve the symmetric equation by a completely explicit `p`-integral terminal inverse and derive its normalized mod-`p` polynomial.

## Theorem 1 — symmetric Green terminal inverse (exact over Q)

Write `S_n(Y)=sum_{j=0}^m s_j Y^j`, `G_p(Y)=sum_{j=0}^m g_j Y^j`, and

```
mu_j = (6j+1)(6j+2)/9.
g_m = (-1)^m c_n;
g_j = ((j+1)^2 g_(j+1) + (p C/2)*s_j)/mu_j,
       j=m-1,m-2,...,0.
```

This gives **all** coefficients of the original symmetric source polynomial `G_p` by a finite downward recurrence, with no division by `p`. Every denominator `mu_j` for `j<m` is a `p`-adic unit, hence the reconstruction is `p`-integral.

Proof. The coefficient of `Y^j` in `NG` is precisely `(j+1)^2*g_(j+1)-mu_j*g_j` (with `g_(m+1)=0`). The terminal right-hand coefficient is `s_m=2(-1)^m`. At `j=m`, `mu_m=p(p+1)/9`, so the exact equation says `mu_m*g_m=p*C*(-1)^m`. Cancel the **exact rational common p**, *before* reducing modulo p, giving `g_m=(-1)^m c_n`. All lower equations yield the stated inverse. For `0<=j<m`, neither factor `6j+1` nor `6j+2` equals a multiple of `p=6m+1`, and `9` is a unit. Thus no illegal modular inverse or singular top-row division is made. Uniqueness follows from descending coefficient comparison. QED.

The singular mod-p top row is therefore a **terminal resonance**, not an obstruction to the exact p-integral source solution. Deleting that row or dividing by `mu_m mod p` would lose its actual boundary normalization.

## Theorem 2 — canonical finite quadratic transfer modulo p

There is the explicit universal congruence

```
G_p(Y) ≡ H_m(4Y) (mod p),
H_m(Z) = sum_(j=0)^m [(1/6)_j*(1/3)_j/(j!)^2] Z^j.
```

Equivalently, in the original labeled `X` port,

```
sum_(k=0)^(2m) [(3k)!/(27^k (k!)^3)] X^k
 ≡ sum_(j=0)^m [(1/6)_j*(1/3)_j/(j!)^2] (4X(1-X))^j  (mod p).
```

Proof. By the factorial/triplication identity, `c_k=(1/3)_k(2/3)_k/(k!)^2`. In `F_p`, `1/3=-2m=-n` and `2/3=-4m=-2n`; for `0<=k<=n<p`, therefore

```
A_p(1) ≡ sum_(k=0)^n binom(n,k)binom(2n,k)
       = binom(3n,n)=binom(p-1,n) ≡ (-1)^n =1 (mod p).
```

The equality in the middle is the finite Vandermonde convolution (no infinite hypergeometric continuation). As `A_p(0)=1`, it follows that `g_0=G_p(0)=(A_p(0)+A_p(1))/2≡1`. Reducing the lower Green coefficient equation modulo p gives `(j+1)^2 g_(j+1)=mu_j*g_j` for `0<=j<m`. Induction yields

```
g_j ≡ product_(r=0)^(j-1) [(6r+1)(6r+2)/(9(r+1)^2)]
    = 4^j*(1/6)_j*(1/3)_j/(j!)^2       (mod p).
```

Finally the inherited **source-labeled** identity `A_p(X)=G_p(Y)+(p/2)*t*Phi_p(Y)` reduces to `A_p(X)≡G_p(Y)` modulo p, proving the finite quadratic transfer. All displayed denominators are p-units in their stated index range. QED.

The finite transform may overlap classical quadratic hypergeometric transformations; **no global priority/novelty claim** is made. The exact terminal-inverse and its source-bounded observer transport are the scoped research increment.

## Corollary — first-digit signed Green observer needs no p-adic lift

For the previously defined ordered source pairing `K_p(Y)=W(X)/p` and `F_(n-1)` from its original X-branch equation, prior work proved

```
K_p(Y) ≡ -C ∫_0^Y F_(n-1)(s)*G_p(s) ds (mod p).
```

Substituting the newly explicit `H_m(4s)` computes this **particular first-digit signed W-pairing** purely over `F_p`, with division only by `j+1<=2m<p`. This is an observer-safe quotient for that specified first digit; it does not recover the original CM `kappa` or a divided-power `[X]U`.

## Exact rational author checks and p=373 witness

Independent paths used (i) the two triangular Green recurrences and (ii) direct original factorial coefficients `c_k` to reconstruct and compare every coefficient of `A_p(X)` over Q, followed by denominator-safe reduction modulo `p^2`. Tested `p=13,19,37,43,61,67,211,373`: exact coefficient equality and mod-p finite quadratic transfer held for every listed p. This is **author regression**, not independent review.

At `p=373` (`m=62`), the new symmetric inverse gives
`G_373(1/8)=112646 (mod 139129)` and `G_373'(1/8)=114 (mod 373)`. The reflected source derivative port is `d=G'(1/8)/2=57 (mod 373)`, consistent with the earlier factorial source witness. Combining with the inherited odd `Phi` recurrence in the exact ordered pairing recovers `K_373(1/8)=99504 (mod 139129)`. These are independent method checks of **ordinary source polynomials only**.

## Typed BRC/Enterprise observer boundary and continuation

BRC `COMPOSE_APPLIED` at the typed carrier `(p,m;X,Y,t;A,B;G,Phi;S,F;K)`. Terminal resonance preserves `p`-valuation and branch/source provenance; mod-p quadratic transport is lossless **only for explicitly designated first-digit polynomial or K observers**. The `p`-level odd correction `Phi`, second-digit K data, fixed CM basis `H0/B0`, semilinear Frobenius and native `kappa` are **not** reconstructed by the mod-p compression.

Native D25/LIFT remains OPEN. Exact next task: obtain or authenticate the same-prime, same-original-class divided-power `H0/B0` representative, semilinear Frobenius direction and source-selected `[X]U mod p^2` normalization, then test whether an explicitly proved source map transports this `(G,Phi,K)` carrier to the native `omega+6 nabla_lambda omega` and `kappa/Delta_p-R_p` observer. Do not repeat the 19 inherited Source native units, earlier odd Green inverse, prior Hesse Green pairing, or large WZ/LOW/HIGH scans. No Result, freeze, audit pass or Source-native CM experiment is claimed by this portable note.
