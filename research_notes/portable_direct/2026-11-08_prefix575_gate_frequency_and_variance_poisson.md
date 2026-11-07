# PREFIX-575 — 原生 X6-BRC 门控计数的全长度 Poisson 恒等式与方差增长率

**Date:** 2026-11-08 · **Status:** AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED  
**Frozen science pin:** `f42f2906d77f24085c123f3ccfe9667d41caa96d`.  
**Dependencies:** PREFIX-565/566 original native 96-port / 37-class gate-preserving observer, PREFIX-572/573/574 spectral frontier. Underlying six-axis native state, ordered actions and gate bit remain unchanged. The observer deliberately sets `q1=q2=q3=q4=q5=q6=1` while retaining the gate counter. Nine frozen root inputs share this exact observer kernel.

## Exact theorem A: gate-event expectation, every path length

Start at any of the 96 native ports `i`. Let `X_d` be the native port after `d` independent uniform choices among its six labeled actions; `K_d` counts their original gate-bit events. Let `c(i)` be the exact PREFIX-566 class (0..36), and put `h(i)=H[c(i)]/768`, where

```text
H = [0,2,-6,-5,123,2,-1,8,2,-1,18,2,3,2,-4,124,-5,123,-4,
     17,2,-1,18,2,-3,12,5,-4,-1,17,3,6,5,14,17,17,-3]
```

For every native starting port and every integer `d>=0`,

```text
E_i[K_d] = d/192 + h(i) - E_i[h(X_d)].
|E_i[K_d] - d/192| <= 65/384.
```

The stationary gate-event rate is exactly **1/192 event per original action**. The absolute finite-depth correction is bounded independently of `i,d`.

## Exact theorem B: compensated martingale and variance rate

Write `G_t` for the gate bit of action `t` and set

```text
eta_t = G_t - 1/192 + h(X_(t+1)) - h(X_t)
M_d   = sum_(t=0)^(d-1) eta_t
```

The increments `eta_t` have zero conditional expectation given the current port. Put `w(i)=W[c(i)]/1769472`, where

```text
W = [0,4448,-13464,-11245,236819,4424,-2197,17888,4544,-2197,
     40032,4544,6723,4448,-9000,238296,-11245,236819,-8968,
     37871,4544,-2197,40032,4544,-6777,26712,11351,-8968,
     -2197,37871,6723,13536,11351,31424,37871,37871,-6777]
```

Then, for every native initial port `i` and every `d>=0`,

```text
E_i[M_d^2] = (1127/221184)*d + w(i) - E_i[w(X_d)].
lim_(d -> infinity) Var_i(K_d)/d = 1127/221184.
```

These are full-length, exact statements about the stochastic observer obtained by choosing original labeled BRC actions equiprobably. The variable `d` counts ordered native actions, not physical time.

## Finite certificate and full-length proof

Construct `A_ij` by summing original labeled six-action multiplicities in the exact PREFIX-566 37-class gate observer; `sum_j A_ij=6`. The original native 96-port directed graph has exactly six incoming and six outgoing actions per port, and exactly three marked edges `7 -> 9`, `29 -> 9`, `31 -> 9`. The weighted class quotient is strongly lumpable for future gate observations. Its graph is strongly connected, bipartite (17/20), and contains a 2-cycle `0->7->0`. The pushforward of uniform 96-port counting is therefore stationary. Its gate rate is `3/(96*6)=1/192`.

Let `g_i` count marked actions leaving class `i`; `g_i=1` precisely for `i=4,15,17` and zero otherwise. The following **37 independent integer equalities** are directly checked by the published certificate:

```text
6*H_i - sum_j A_ij H_j = 768*g_i - 24.
```

For `P=A/6`, this is the exact Poisson equation `(I-P)h=g/6-1/192`. Sum conditional expectations over `t=0..d-1` to obtain theorem A. Since `min(H)=-6` and `max(H)=124`, `h(i)-E h(X_d)` has absolute value at most `130/768=65/384`.

On an original transition `i -> j` with gate bit `b∈{0,1}`, define integer

```text
m(i,j,b) = 768*b - 4 + H[c(j)] - H[c(i)].
```

The first Poisson equation implies `E[m | current port]=0` and `eta=m/768`. Define the class quadratic count

```text
V_i = sum_(six actions from class i) m(i,j,b)^2.
```

The exact sum of `m^2` over all `96*6=576` native labeled actions is `1731072`. With uniform stationary ports, the stationary conditional quadratic rate is

```text
sigma^2 = 1731072/(576*768^2) = 1127/221184.
```

A second finite integer check covers all 37 classes:

```text
6*W_i - sum_j A_ij W_j = 3*V_i - 54096.
```

Using `1769472=3*768^2`, this says `(I-P)w=E[eta^2|current]-sigma^2`. Orthogonality of martingale differences yields `E[M_d^2]=sum_{t<d}E[eta_t^2]`; telescoping the second Poisson equation proves theorem B's exact identity. The `w` correction is bounded, whence `E[M_d^2]=sigma^2*d+O(1)`. Since `K_d-d/192=M_d+h(X_0)-h(X_d)` with bounded h, Cauchy–Schwarz gives `Var(K_d)=sigma^2*d+O(sqrt(d))`; divide by `d` to get the exact limit.

## Evidence and reproduction

Run `PREFIX575_gate_count_poisson_certificate.py` with unmodified `PREFIX565_positive_marginal_certificate.py` (Git blob `7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41`) and `PREFIX566_gate_quotient_certificate.py` (Git blob `7b6613193847e4123cd0ac11107eb9b9c70290c8`) in the same directory. Python 3 standard library and exact integers suffice. The code asserts 96-port indegree/outdegree, nine-root observer equality, exact weighted quotient, both 37-equation Poisson certificates, stationary counts, connectivity/period and two independent 96-port integer dynamic-programming moment identities at all depths 0..128. There are `96*129=12384` checks **per moment identity**; the printed JSON result states `ALL_CHECKS_PASS`. The finite run validates the implementation; the algebraic Poisson/martingale proof establishes all-depth quantifiers.

**Next unit:** reintroduce `u=q5+q6`, `v=q5*q6` into the gate-sensitive Poisson method, explicitly retaining the original native source; seek a coefficientwise positive lifted potential, a minimal finite witness if that positivity fails, or higher gate cumulants by rank-one perturbation. Keep P000 and frozen science pins unchanged. Live control service read during this author run returned `BACKEND_IDENTITY_OR_VERSION_MISMATCH / STATUS_DATABASE_UNAVAILABLE`, `operation_sent=false`; current native Owner/Researcher-ID and formal CLAIM/Result/Review were unavailable.
