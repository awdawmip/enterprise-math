# D25: reflected outer-source spectral jet and the p=5113 carry cancellation

Date: 2026-11-06. Type: TASK_RESEARCH portable author-side mathematics. Status: **AUTHOR-PROVED ALGEBRA / EXACT PRIME-SPECIFIC CERTIFICATE / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CHECKPOINT**.

Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; frozen scientific source pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. These are preserved, not reissued. Research lane `chatgpt-research-hourly-enterprise-math-20260923` is configured, **not independently attested as a platform identity**; no new authenticated native Researcher session, claim, authorized run, result or checkpoint is asserted here. The maintenance conversation is excluded.

## General finite-field theorem: spectral recurrence (all prime p=6m+1)

Work in `F_p[t]`, with `p=6m+1>=7` prime, `a=2m, b=3m, c=4m`, and `0<=j<p`. Define labelled outer-source perturbations

```
U_j(z1,z2,z3)=(-1/2)^j binom(a+z1,j) binom(b+z2,j) binom(c+z3,j),
F_p(t)=sum_{j=0}^{p-1}(6j+1)*U_j(t,0,t).
```

Since `binom(b,j)=0` for `j>b`, this is a degree-at-most `2b` polynomial. Since `c=4m=p-1-a` and `j! != 0 mod p`, we have the exact polynomial reflection

```
binom(c+t,j) = (-1)^j binom(a+j-t,j) in F_p[t].
```

Thus, defining `G_j(t)=binom(a+t,j)binom(a+j-t,j)` and `w_j=(6j+1)2^(-j)binom(b,j)`,

```
F_p(t) = sum_{j=0}^b w_j G_j(t)   in F_p[t].
(j+1)^2 G_{j+1}(t) = [a(a+1)-j(j+1)+(2j+1)t-t^2]*G_j(t).
```

Write `g[j,r]=[t^r]G_j(t)`, set `g[0,0]=1`, all `g[0,r>0]=0` and `g[j,-1]=g[j,-2]=0`. The **all-order singularity-free jet recurrence** is

```
(j+1)^2*g[j+1,r]
   = (a(a+1)-j(j+1))*g[j,r]
      + (2j+1)*g[j,r-1] - g[j,r-2]      (mod p).
```

Every denominator `(j+1)^2`, `1<=j+1<=3m<p`, is a unit. Crucially the recurrence crosses the first carry wall `j=a`, where `g[j,0]` becomes zero, without dividing by a vanishing binomial. The weight may vanish at `j=m` without ever being divided by. It calculates any fixed jet order `r` in `O(br)` field operations and `O(r)` state; the original complete labelled data remains separately available when needed.

**Proof:** all identities follow by polynomial binomial reflection and the factorial ratio
`G_{j+1}/G_j=[(a-j+t)(a+j+1-t)]/(j+1)^2`, interpreted as a polynomial recurrence without division by `G_j`. Coefficient extraction gives the displayed formula. No analytic continuation or unproved supercongruence is used.

## Exact second-order head/carry-tail expression

Write `H_n=sum_{k=1}^n 1/k`, `H_n^(2)=sum_{k=1}^n 1/k^2` in `F_p`; `H_0=H_0^(2)=0`. All harmonic indices below are at most `5m<p`. Let `C_p=[t^2]F_p(t)`; this is `(H_11+2H_13+H_33)/2` in the previous labelled Hessian notation (here H_ij denotes Hessian entries, not harmonic numbers).

For `0<=j<=a`, put

```
A_j = binom(a,j)binom(a+j,j),
D_j = 2H_a - H_(a-j) - H_(a+j),
E_j = H_(a+j)^(2)-H_(a-j)^(2).
[t^2]G_j = A_j*(D_j^2-E_j)/2.
```

For `a<j<=b`, put

```
P_j = (-1)^(j-a-1)*a!*(j-a-1)!/j! * binom(a+j,j),
D'_j = 2H_a - H_(j-a-1) - H_(a+j),
[t]G_j = P_j,       [t^2]G_j = P_j*D'_j.
```

The last case has one binomial zero (the outer first source) and one surviving source: it must not be dropped. Summing gives an exact source-labelled decomposition

```
C_p = HEAD_p + TAIL_p
HEAD_p = (1/2)*sum_{j=0}^a w_j A_j*(D_j^2-E_j),
TAIL_p = sum_{j=a+1}^b w_j P_j*D'_j      (mod p).
```

**Proof:** for `j<=a`, logarithmic differentiation of two nonzero binomials gives first derivative `D_j` and second logarithmic derivative `-E_j`. For `j>a`, factor the unique zero `t` from `binom(a+t,j)`; differentiating the remaining nonzero factors gives `P_j` and `D'_j`. No division by `G_j(0)=0` occurs. This resolves the prior local question of how the second-order outer curvature crosses the carry wall.

## Distinguishing prime p=5113: two nonzero bands cancel and the residue polynomial has an exact triple root

The all-order recurrence and an independent **unreflected** `binom(a+t,j)binom(c+t,j)` recurrence produce

```
p=5113, m=852, a=1704, b=2556:
[t^0,t^1,t^2,t^3] F_5113(t) = [0,0,0,3783] in F_5113.
HEAD_5113=3519, TAIL_5113=1594; 3519+1594=5113=0 mod p.
```

The root at `t=0` of this *mod-p polynomial* therefore has **exact multiplicity 3**, not 4: `3783 != 0`. Neither the head nor the carried tail is zero individually. This is an exact finite-field certificate for one prime, not a classification of all curvature-zero primes.

**Important observer scale:** this mod-p triple root does **not** assert a three-digit collision for the original p-adic perturbations `z=p(v+lambda d)`. The prior source-bound `p^3` result at `p=5113` has `D(lambda)=3118 lambda`, which remains bijective. The first two statements concern distinct observers/normalizations and coexist.

## Reproducible checks and remaining questions

The accompanying program `d25_outer_curvature_spectral_20261106.py` was actually run locally. For **all 330 primes `7<=p<=5000, p=1 mod 6`**, independent reflected and unreflected coefficient recurrences agree through cubic order, and the harmonic head/tail formula matches the second coefficient. Every one also had `[t]F_p=0` in this *finite range*; its general proof remains open. For `p=7,13,19,109,211,229,373,1093,3511,5113`, a separate full sum at `t=0,p,-p` modulo `p^3` reproduces the curvature by exact symmetric finite difference. Sample triples `(HEAD,TAIL,C)`:

```
13    3       2       5
19    7       3      10
373  158     282      67
1093 309     452     761
5113 3519   1594       0
```

The finite checks are not universal proofs of `[t]F_p=0`, `k_p=-3q_p(2)`, curvature nondegeneracy outside the checked range, or the original frozen mother target.

**BRC:** state = three labelled source parameters with p-adic valuation and exact coefficients; observer = weighted sum plus source ports; operation = simultaneous outer-source shift and reduction to `F_p[t]`; the HEAD/TAIL split records carried provenance and the cubic jet retains the future distinguishability hidden by the second derivative. This is an observer-specific readout, not permission to erase original source labels.

**Mother objective:** `Delta_p-R_p=0 mod p`, `p=13,19 mod 24`. The `p=5113` example belongs to the adjacent `1 mod 24` class. Next: use the coefficient recurrence to derive a finite telescoping/WZ certificate for `[t]F_p=0`; test whether `C_p=0` has a source-theoretic characterization for target primes, then return to `p=373` H0/B0, Frobenius, eta/kappa and independent review. Do not rescan completed `p<=100000` data without a genuinely new hypothesis.

**Control continuation, no native write:** Original requests `em-h20-20261106-1324-d25-task-r13` and `em-h20-20261106-1324-d25-cont-r13` were reconciled by exact IDs this run; both became `QUEUED`, not terminal. The native connector exposes no callable `recovery_status`/staging-preservation method here. Previous claim/session/staging ownership has not been independently verified anew, so no session_close, session_start, CLAIM, OPEN, native checkpoint, freeze, review or release was issued. Old IDs remain with support issue #1558; this portable author evidence is separate from native Source and cannot be substituted for its durable checkpoint.
