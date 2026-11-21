# CBRC F7 Driver r443 — exact axis-pairing law, scale-tail obstruction, and baseline minimax

Date: 2026-11-21 (+08:00). Independent auxiliary derivation by the continuing RESEARCH_DRIVER mathematical line EM-DVR-DEBB5E; original F7 mixing matrix and task belong to EM-CBRCF7-83A1D4. This is an auxiliary scalar theorem, not a new Native Review, frozen Result, formal Task closure or P000 change.

## Original exact model

Let $A=I+uv^T\in GL_4(\mathbb Z)$, with $u=(1,1,-1,-1)^T$, $v=(1,-2,-1,2)^T$, so that $A^2=I$. Explicitly

```
A = [ 2 -2 -1  2
      1 -1 -1  2
     -1  2  2 -2
     -1  2  1 -1 ] .
```

For $q:\mathbb Z^2\to\mathbb R_{\ge0}$, assume $q(0,0)=0$, $q(n,m)=q(-n,m)$, $q(t,0)=1$ for $t\ne0$, $q(n,m)\ge 1/2$ at every nonzero pair, and the original exact marks $q(2,1)=q(-1,-1)=1/2$. Write

```
D_q(z) = q((Az)_1,(Az)_2)+q((Az)_3,(Az)_4)
         -q(z_1,z_2)-q(z_3,z_4),
E(q)=sup_{z in Z^4}|D_q(z)|.
```

All claims below refer to this original fixed-matrix, unrestricted-scale scalar model.

## Theorem A — all-scale axis pairing

For every $u,v\in\mathbb Z$, the *exact* identity

```
A(u-v,0,u-2v,0) = (u,v,u-3v,-v)
```

gives

```
D_q(u-v,0,u-2v,0)
= q(u,v)+q(u-3v,-v)
  - 1_{u-v!=0}-1_{u-2v!=0}.              (A1)
```

In particular, for every $v\ne0$ and $u\notin\{v,2v\}$, whenever $E(q)\le\varepsilon$,

```
2-epsilon <= q(u,v)+q(u-3v,-v) <= 2+epsilon,
max(q(u,v),q(u-3v,-v)) >= 1-epsilon/2. (A2)
```

This is an exact infinite family of coupled ray/tail constraints, not a finite sampled observation.

For every nonzero integer $k$, use $u=3k,v=2k$ and the stated J-evenness to obtain

```
q(3k,2k)+q(3k,-2k) >= 2-epsilon.         (A3)
```

Thus a global half-defect candidate must have a value at least $3/4$ among these two sign-related rays **at every nonzero integer scale**. More generally an $E<1$ candidate must depart from the baseline value $1/2$ by at least $(1-E)/2$ on at least one of the two entries at each scale. For the current 4/7 upper target this necessary departure is at least $3/14$.

Proof: expand $A$ on the displayed vector, use the exact nonzero-axis values for the two inputs, then take the upper/lower bounds on the defect. For (A3), the second output pair is ($-3k,-2k$), and J-evenness identifies its first-coordinate sign.

## Theorem B — finite perturbations of the off-axis baseline cannot improve the global defect below 1

Define the elementary scalar

```
q0(x,y) = 0,   if (x,y)=(0,0);
          1,   if y=0 and x!=0;
          1/2, if y!=0.
```

This satisfies every F7 scalar hypothesis including both exact marks. Its exact global defect is

```
E(q0)=1.                                      (B1)
```

To prove the upper bound, all nonzero pair values are in [1/2,1]. If both input pairs and both output pairs are nonzero, each two-slot sum lies in [1,2], so |D|<=1. If precisely one input pair is nonzero and precisely one output pair is nonzero, each sum lies in [1/2,1], so |D|<=1/2. If precisely one input pair is nonzero and both output pairs are nonzero, at least one output pair is off-axis: with input (n,m,0,0), the second output is (-t,-t) with t=n-2m; if nonzero it has nonzero second coordinate; with input (0,0,p,l), the first output is (t,t) with t=-p+2l and is likewise off-axis if nonzero. Thus the output sum is at most 3/2 and the input sum at least 1/2, giving 0<=D<=1. The reverse case follows identically by A^2=I. Both inputs zero iff both outputs zero, giving D=0. This exhausts all cases.

For the lower bound take z=(-k,0,k,0), k!=0. Its image is (-3k,-2k,3k,2k); the two input scalar values equal 1 and the two output scalar values equal 1/2, hence D=-1.

Now let q obey the F7 fixed axis/mark hypotheses and agree with q0 at all but finitely many off-axis points. Choose a nonzero k with both (3k,2k) and (3k,-2k) outside this finite exception set. Then the same axis witness gives D_q(-k,0,k,0)=-1. Consequently

```
E(q) >= 1.                                    (B2)
```

The same necessary lower bound holds if q(3k,2k) and q(3k,-2k) both converge to 1/2 along |k|->infinity, by taking the corresponding defect limit.

## Theorem C — homogeneous extremal-witness tails cannot be repaired finitely

This generalizes the finite-support obstruction beyond the elementary baseline. Let h be any scalar in the same model satisfying **degree-zero positive integer dilation invariance**, h(kx,ky)=h(x,y) for each k>=1 and each nonzero integer pair (x,y). Let z_* be a fixed integer witness such that |D_h(z_*)|=e>0. For any other scalar g in the same model:

1. If g and h differ at only finitely many nonzero scalar pairs, then E(g)>=e.
2. The same bound holds if g(k w)-h(w) tends to zero as k tends to infinity for each nonzero scalar pair w among the four input/output slot pairs of z_*.
3. More quantitatively, if E(g)<=e-delta for a fixed delta>0, **for every k>=1 at least one of those four input/output slot pairs w obeys |g(kw)-h(w)|>=delta/4**. Thus a strict improvement requires a uniformly nonvanishing scale-tail modification, not just exceptional coefficients near the origin.

Proof: A(kz_*)=kA(z_*) and D_h(kz_*)=D_h(z_*) by h's degree-zero invariance, including the fixed value h(0,0)=0. The difference D_g(kz_*)-D_h(kz_*) is a signed sum of at most four scalar discrepancies at the scaled slot pairs. Its absolute value is bounded above by their four absolute discrepancies. If |D_g(kz_*)|<=e-delta but |D_h(kz_*)|=e, the reverse triangle inequality forces that sum to be at least delta; at least one discrepancy is >=delta/4. Finite changes vanish on all these nonzero scaled pairs for all sufficiently large k, and asymptotically vanishing changes give the same result by taking the limit.

**Corollary for the original F7 frontier:** the previously verified r435 signed-angular scalar is degree-zero dilation invariant and has exact global error e=4/7, attained for example at z_*=(-46,17,-36,24). Direct exact substitution gives D_h(z_*)=-4/7. Therefore finite pointwise edits to this homogeneous r435 scalar cannot reduce the infinite-domain defect below 4/7. If a candidate g attains error <=4/7-delta, then at every integer scale k at least one of the four scalar pairs appearing at the scaled r435 witness must differ from the r435 value by >=delta/4. This remains true for each of r435's six independent extremal witnesses. The criterion is a necessary tail condition, not an obstruction to the unrestricted open optimum of 1/2.

## Research consequence and provenance

Finite LP optimization may validly use finitely many exceptional coefficients to prove bounds on each fixed cube, but making the same table default to q0 outside a finite region cannot produce a global error less than 1. A genuinely global candidate with error 1/2 needs **persistent, uniformly nonbaseline values at every scale** along the paired 3:2 rays; (A2) supplies the corresponding constraint throughout all nonexceptional axis-pair families. This indicates why exact finite-domain primal certificates and a global minimizer require distinct constructions; it neither decides whether E_infinity is 1/2 nor changes the valid r441 compactness theorem.

- Original F7 contributor/Result: EM-CBRCF7-83A1D4 / RR-AA38973D56330E59D315.
- Prior rank-one reduction and finite candidate tail: r437, commit 762b84a52494d6bf82ea6ce033146f66defaf8f1.
- Uncapped finite-to-infinite compactness: r441, commit 82027a566a0b9b84069fba9a4d3616027a3b4660.
- Current finite B12 candidate: r442, commit 108f2d1af4fd70857ddacfb7b23abd8dd6c55162.
- This result is independently hand-proved; Native first Review, frozen Result integrity and formal Source/Activity status remain separately governed by the original control receipts.
