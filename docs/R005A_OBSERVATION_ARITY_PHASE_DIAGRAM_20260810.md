# R005-A — Observation-Arity × Collapse-Dimension Phase Diagram

Status: `PROVED R005 STRUCTURE / ASYMPTOTIC COROLLARY FROM PRIOR-ART BHP / NOT CANONICAL / LEAN PENDING`  
Date: `2026-08-10`

## 1. Two independent indices

R005 now has two integer indices that must not be conflated: `p>=2` is the collapse exponent defining `k^p<n<(k+1)^p`; `m>=2` is the observation-root depth specifying how much of the divisor witness language is forced, `q<=U^(1/m)`.

The second index is not a second physical dimension. Its role is: m=2 forces the entire square-root candidate language; m=3 forces the cube-root residual core and is enough for unique least basis; m>=4, by T-A21, bounds any surviving residual by `Omega(n)<=m-1`.

## 2. T-A22 — universal short-interval exponent

At the hardest m-root core witness, `q~k^(p/m)`, so `x=A/q~k^(p(m-1)/m)`. The available cofactor interval has length `(U-A)/q~k^(p(m-1)/m-1)~x/k`. Hence

`k~x^(m/[p(m-1)])`

and the required short-prime scale is

`lambda(p,m)=1-m/[p(m-1)]`.

Special cases:

- m=2: `lambda=1-2/p` — full forcing;
- m=3: `lambda=1-3/(2p)` — unique least basis;
- m=4: `lambda=1-4/(3p)` — residual arity at most 3.

## 3. BHP admissible region

Baker–Harman–Pintz supply the established exponent `theta=21/40=0.525` for sufficiently large x. The m-root core is asymptotically controlled whenever

`lambda(p,m)>21/40`,

equivalently

`p>40m/[19(m-1)]`.

This curve is the current R005 observation-arity / collapse-dimension phase boundary induced by BHP. No novelty is claimed for BHP itself.

## 4. Integer phase regions

### p=2

For every finite m,

`lambda(2,m)=(m-2)/(2(m-1))<1/2<0.525`.

Even as m tends to infinity, lambda approaches 1/2 from below. Thus this BHP route controls no finite m-root observation core for p=2.

### p=3

`lambda(3,2)=1/3`, `lambda(3,3)=1/2`, but `lambda(3,4)=5/9>0.525`. Hence every m>=4 core is asymptotically BHP-controlled. In particular, sufficiently large cubic basins have the fourth-root core forced, so T-A21 gives `Omega(n)<=3` for every residual. Generic R005 structure gives `Omega(n)>=3`; therefore any sufficiently large p=3 residual, if one exists, must have exactly `Omega=3`.

The least-basis layer m=3 remains exactly square-gap critical.

### p=4

`lambda(4,2)=1/2`, while `lambda(4,3)=5/8>0.525`. Therefore every m>=3 core is asymptotically controlled; unique least basis follows, but full forcing remains square-gap critical.

### p>=5

Already `lambda(p,2)=1-2/p>0.525`, so the complete candidate language is asymptotically forced.

## 5. Phase table

| collapse p | m=2: full forcing | m=3: least basis | m=4: residual Ω≤3 | BHP picture |
|---:|---:|---:|---:|---|
| 2 | λ=0 | λ=1/4 | λ=1/3 | no finite m controlled |
| 3 | λ=1/3 | λ=1/2 | λ=5/9 | m≥4 controlled |
| 4 | λ=1/2 | λ=5/8 | λ=2/3 | m≥3 controlled |
| 5 | λ=3/5 | λ=7/10 | λ=11/15 | all m≥2 controlled |
| ≥6 | >3/5 | >7/10 | >11/15 | all layers controlled |

Rows describe collapse geometry; columns describe required observation precision.

## 6. Finite evidence and hierarchy

The exact p=2 certificate family has the fourth-root core fully forced while 50 residual composites remain, all with `Omega=3`; this makes the m=4 arity bound sharp on an explicit finite family.

For p=3, finite Oppermann transport proves unique least basis through `k=2,150,153,225`. Independently, the (3,4) BHP cell says that sufficiently far out, even a hypothetical least-basis failure cannot recover higher multiplicative complexity: the residual fiber is confined to three-factor composites.

For p=4, finite verified Legendre/Oppermann information gives full forcing through `k=9,985,091`, while the phase diagram separately gives asymptotic least-basis control.

## 7. Candidate foundational interpretation

The pair `(p,m)` is a natural precision coordinate: p controls basin scale; m controls the depth of mandatory factor observation; lambda(p,m) tells how strong a prime-gap theorem is required to make that observation layer sufficient for the declared residual question.

The Prime Toolkit therefore has a stratified state rather than a binary enough/not-enough witness flag:

`full separation ⊃ least-basis separation ⊃ residual arity 3 ⊃ residual arity 4 ⊃ ...`

This is a candidate A2/A4 bridge: A2 asks how much observation state is sufficient for a declared future truth question; A4 records what support multiplicity remains unresolved after that precision.

## 8. Foundation feedback candidate

`FF-R005A-10 — Observation-arity × collapse-dimension phase law`

Payload: T-A21 residual arity filtration; T-A22 lambda formula; BHP phase curve; integer phase boundaries; and the p=3 asymptotic residual-if-any `Omega=3` theorem.

Status: `PROVED R005 STRUCTURE / PRIOR-ART PRIME-GAP INPUT / NOVELTY UNVERIFIED`.

Do not canonicalize before Lean validation and prior-art audit.

## 9. Next

- p=2: direct arithmetic classification of three-factor square-basin residuals; BHP 0.525 cannot resolve any fixed m-root layer by this route.
- p=3: the remaining least-basis obstruction is the m=3 square-gap layer; classify hypothetical Omega=3 residuals.
- p=4: least basis is asymptotically settled by BHP; the interesting frontier is m=2 full forcing.
- p>=5: focus on quantitative thresholds and toolkit efficiency rather than existence of the structure.
