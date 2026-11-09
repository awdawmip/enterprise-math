# PREFIX-630 R2 — Native BRC phase-only fast suffix recovery

Date: 2026-11-09 Asia/Shanghai. **Author-side exact derivation and executable original-native tests; independent mathematical review pending.** Researcher-ID `EM-X6-CF0D65`, activity `RA-D77B57E8C12B452BB18C719D`. Frozen scientific input: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`.

## Original observer and problem

Use the 48 original signed STAR phases, 96 original bit ports, all 576 typed native BRC actions and weights `(1,1,1,1,0,0)`. Initial probe is `d=e4+e11+e14+e32`, with strength `lambda>0` and unknown native nonnegative gates `g1,...,gn`. Let `r_n=A(g_n)...A(g_1)E(lambda*d)`; `v_n=C r_n` is the full terminal 48-phase observable, **not** the original 96-port state. A suffix window has length `L>=1`, `t=n-L>=4`. We wish to recover the **complete source-port/action/ordered-path-labelled** last-L-step tensor.

Reuse the exact sharp phase-only register counts from PREFIX-629 (Draft PR #1884): at `t=4` save `g5,...,gn` (L scalars), and at `t>=5` save `g_t,...,gn` (L+1 scalars). The new result here is a short direct reconstruction procedure, avoiding the O(n) original synthetic prefix replay.

## Constructive result and proof

**Theorem.** For every such nonnegative gate history, terminal `v_n` plus the above sharp saved gates recover the complete original tagged suffix tensor exactly. For `t>=5`, after fixed precomputation the predecessor requires `L` fixed-dimensional rational matrix operations and therefore `O(L)` arithmetic operations, independent of total age n; explicit labelled output requires its output-size work. The boundary `t=4` adds the four-product phase readout, with `O(log n)` repeated-squaring arithmetic work. Exact integer/rational bit lengths remain age-dependent.

**Endpoint decoder.** Take `H={3,14,15}`, `ell=v[3]+v[14]+v[15]-2v[2]`, `delta=(g_n-1)*ell/(3*(g_n+3))`. The original native port decoder of PREFIX-622 (PR #1863) yields `r_n=D_(g_n)(v_n)` by, for each phase `i != 4`,

```
r[2*i]   = (v[i] - (delta if i in H else 0))/2
r[2*i+1] = (v[i] + (delta if i in H else 0))/2
r[8]=r[9]=v[4]                  # original marked-phase exception
```

This is exact on the specified native reachable family, including zero gates.

**Rank-16 predecessor.** Fix the original zero-based port index sets

```
R=[0,2,4,6,8,10,12,14,32,34,36,38,48,50,52,54]
C=[0,4,8,12,16,18,20,22,24,28,42,46,56,60,64,68].
```

With original `A0=A(0)`, `E=A(1)-A0`, `T=A0*A0`, `V=E*A0`, `K=T[R,C]`, `G(g)=T[:,C]+g*V[:,C]`, `N(g)=N0+g*N1` and `N0=K^-1(A0 G(0))[R,:]`, `N1=K^-1(A0 V[:,C])[R,:]`, the exact PREFIX-628 R2 original-matrix identities say

```
det K = -65536;  N1[2,7]=1/2 and all other N1 entries 0
det N(g)=16384*(g+3)
A(c)G(b)=G(c)N(b).
```

Hence each reachable `r_k`, k>=2, has an exact unique predecessor given its last gate:

```
r_k = G(g_k) * N(g_k)^(-1) * K^(-1) * (r_(k+1))[R].
```

Writing `U=N0^(-1)`, the invertible rank-one update is `N(g)^(-1)=U - [g/(1+g/3)]*U*N1*U`. From `D_(g_n)(v_n)`, apply this for `k=n-1,...,t`; all required `g_k` are in the saved buffer if t>=5. The remaining suffix gates `g_(t+1),...,g_n` and the exact reconstructed `r_t` specify every original labelled path mass by multiplying its original action weights.

At t=4, extract the four exact phase products `Pi_r(n)=product_(1<=k<=n, k mod4=r)(g_k+3)` from the PREFIX-626/629 exact four-cycle phase decoder, then calculate

```
g4 = Pi_0(n)/product_(5<=k<=n,k mod4=0)(g_k+3) - 3.
```

This provides the only unsaved gate needed by the same backwards recursion. All denominators `g+3` stay positive. The saved memory remains exactly the sharp L/L+1 counts, as previously proved in PREFIX-629. No new independent minimum-memory proof is asserted here.

**Output complexity.** The inverse reconstruction has `O(L)` bounded 16-dimensional rational arithmetic at t>=5. A fully materialized labelled suffix tensor can have up to `64*6^L` originally live path entries; its writing cost is separately accounted. At t=4 arithmetic powers of age n require an additional `O(log n)` exponentiation operation count, while the exact numeric *bit* cost grows with operand size.

## Executed original-native evidence and measured results

The companion runnable checker on this branch depends on the exact `PREFIX629_phase_only_suffix_checker.py` from its immutable parent PR #1884. It builds all 576 original native actions and the symbolic 96x96 A0/E from those actions; checks the four 96x16 coefficient identities of `A(c)G(b)`, rank-one inverse and `det K=-65536`. Every input is propagated by original native actions using `Fraction`; both algorithms start from the same terminal phase vector and the same minimal saved gate buffer. Both expand the **same complete native tagged L-suffix tensor** with the same action enumeration.

47 exact cases: all-one, bounded rational, periodic-zero and all-zero gate families, `n in {5,7,16,32,64,128,256,512,1024}`, `L=1,3` when allowed. Both algorithms recovered every precursor original 96-port coordinate and every emitted labelled path mass; output digest and exact count agree in all cases. A warmup precedes three full-query wall-clock timings per algorithm. Timings include reconstruction and labelled path emission but exclude reusable SymPy matrix setup; source forward acquisition is reported separately.

Examples from the executed standalone import-based program, milliseconds; same environment and Python Fraction exact arithmetic:

| n | L | Synthetic replay | 16-state pullback | Measured ratio | Terminal max numerator bits |
|---:|---:|---:|---:|---:|---:|
| 5 | 1 | 0.5098 | 0.9029 | 0.5646x | 9 |
| 7 | 3 | 1.2836 | 2.0590 | 0.6234x | 11 |
| 16 | 1 | 1.7659 | 0.6104 | 2.8930x | 20 |
| 64 | 1 | 9.5484 | 0.7149 | 13.3563x | 68 |
| 128 | 1 | 17.3732 | 0.6198 | 28.0303x | 132 |
| 256 | 1 | 35.8018 | 0.8475 | 42.2440x | 260 |
| 512 | 1 | 82.2394 | 0.6785 | 121.2077x | 516 |
| 512 | 3 | 74.4425 | 2.5630 | 29.0451x | 516 |
| 1024 | 1 | 175.0133 | 0.6808 | 257.0701x | 1028 |

For these runs L=1 produced 72 nonzero original labelled path entries and L=3 produced 288. The shorter synthetic replay can win at very small n; for fixed small L at larger n this 16-state pullback wins in these measured runs. Exact bit lengths increase with age (e.g., 1028 numerator bits at n=1024). These are implementation measurements, not machine-independent speed lower bounds.

The local full run emitted `ALL_ASSERTIONS_PASS`. Accompanying result JSON retains all case timings, original output counts, lengths, bit lengths and independent output hashes. Core claims and reused lemmas are **author-side, independent Driver review pending**.

## Next

Benchmark exact bit-operation costs at larger n and with rational inputs whose denominators themselves grow; then implement sparse streaming of original labelled outputs for larger L and measure output-size crossover. The X6 native physical rotation mother question remains open and current source Owner/CLAIM remains governed by the separate task control plane.
