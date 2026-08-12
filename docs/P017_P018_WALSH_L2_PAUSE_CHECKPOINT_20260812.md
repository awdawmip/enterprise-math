# P017×P018 Walsh even-conductor L² pause checkpoint

Status: `PROVED_WIP + EXECUTABLE_CHECKED_CORE + ANALYTIC_ENVELOPE_PROVED_WIP + RESEARCH_PAUSED`  
Captured: `2026-08-12T17:05+08:00`  
Owner line: `bridge/p017-p018-hard-core-v2`  
Checkpoint branch: `checkpoint/p017-p018-walsh-l2-pause-20260812`  
Baseline owner head before this checkpoint: `90251d026b4d422a98de007f76de2a1e3de9337e`  
Existing exact L² artifact origin: `dc14b551531c1e300dca05af9652ba508def2f9b`  
Prior Relay checkpoint: Issue #82 comment `5252221650`  
Legendre status: `NOT PROVED`.

This document freezes the current P017×P018 Walsh cutoff/smooth-shadow/L² frontier so that research can stop without losing the exact resume point. It does not promote branch/WIP mathematics to `CANONICAL_MAIN`.

## 1. Exact even-conductor L² pair kernel already implemented

Let

\[
M=k(k+1),
\]

and for every surviving odd radius `r` and odd transverse prime `p` define

\[
\sigma_p(r)=
\begin{cases}
+1,&p\mid M-r,\\
-1,&p\mid M+r,\\
0,&\text{otherwise}.
\end{cases}
\]

For squarefree nontrivial even conductors `q` in the conductor budget,

\[
A_q=\sum_r\prod_{p\mid q}\sigma_p(r).
\]

The executable module

`src/enterprise_math/p017_p018_walsh_even_l2_kernel.py`

proves/checks the exact second-moment expansion

\[
\sum_q A_q^2=\sum_{r,s}K_C(r,s).
\]

For a pair `(r,s)`, split the common active transverse primes into

- `D_+(r,s)`: same-orientation collision radical;
- `D_-(r,s)`: opposite-orientation collision radical.

Then

\[
(D_+,D_-)=1,
\]

and every contributing conductor factors uniquely as `q=de` with `d|D_+`, `e|D_-`. Projecting to even total support yields the exact truncated Möbius hyperbola identity

\[
\boxed{
K_C(r,s)+1
=
\frac12
\sum_{\substack{d\mid D_+,\ e\mid D_-\\de\le C}}
\bigl(\mu(d)+\mu(e)\bigr).
}
\]

Equivalently, with

\[
\mathfrak M_D(y)=\sum_{\substack{e\mid D\\e\le y}}\mu(e),
\]

one has

\[
\boxed{
K_C+1
=
\frac12\sum_{d\mid D_+}\mathfrak M_{D_-}(C/d)
+
\frac12\sum_{e\mid D_-}\mathfrak M_{D_+}(C/e).
}
\]

Thus the nontrivial second-order object is a finite truncated divisor hyperbola, not a free `k^2`-scale prime-distribution problem.

## 2. Exact radius-pair scale collapse

Put

\[
x=\frac{r+s}{2},\qquad y=\frac{r-s}{2}.
\]

Because surviving radii are odd, `x,y` are integers. Same-orientation and opposite-orientation collisions satisfy

\[
\boxed{
D_+\mid y,
\qquad
x^2\equiv M^2\pmod{D_+},
}
\]

and

\[
\boxed{
D_-\mid x,
\qquad
y^2\equiv M^2\pmod{D_-}.
}
\]

Moreover

\[
0<x<k,\qquad |y|<\min(x,k-x)<k/2.
\]

Hence the pair kernel lives on an `O(k)` midpoint/difference triangle with crossed divisor/root conditions. This is the precise form of the observed scale collapse from the ambient `k^2` square-basin arithmetic to radius-sum/radius-difference factor geometry.

## 3. New unconditional analytic energy envelope

Let `A` denote the effective odd anchor product. The surviving radii are odd and satisfy `(r,A)=1`. Expand anchor survival by Möbius inversion:

\[
1_{(r,A)=1}=\sum_{\substack{a\mid A\\a\mid r}}\mu(a).
\]

Fix a nontrivial conductor `q` and an orientation vector

\[
\varepsilon=(\varepsilon_p)_{p\mid q}\in\{\pm1\}^{\omega(q)}.
\]

For fixed `a|A` and `\varepsilon`, the conditions

- `r` odd;
- `a|r`;
- `r\equiv \varepsilon_p M \pmod p` for every `p|q`

form one CRT residue class modulo `2aq`, because `A`, `q`, and `2` are pairwise coprime on the transverse odd support. In the interval `1\le r<k`, its cardinality is

\[
\frac{k}{2aq}+O(1).
\]

The bulk term is independent of `\varepsilon`, while the Walsh sign is `\prod_{p|q}\varepsilon_p`. Therefore, since `q>1`,

\[
\sum_{\varepsilon}\prod_{p\mid q}\varepsilon_p=0,
\]

so the full bulk cancels exactly. Only endpoint discrepancies remain. Summing the `O(1)` discrepancy over `2^{\omega(q)}` orientation vectors and `2^{\omega(A)}` squarefree anchor divisors gives

\[
\boxed{
|A_q|\le 2^{\omega(A)+\omega(q)}.
}
\]

Consequently

\[
E_C:=\sum_q A_q^2
\le
4^{\omega(A)}\sum_{q\le C}4^{\omega(q)}.
\]

Since `4^{\omega(n)}\le d_4(n)` and

\[
\sum_{n\le C}d_4(n)\ll C(\log(2C))^3,
\]

we obtain

\[
\boxed{
E_C\ll 4^{\omega(A)}C(\log(2C))^3.
}
\]

Here `A|k(k+1)` and its prime factors are distinct odd primes, hence

\[
\omega(A)=O\!\left(\frac{\log k}{\log\log k}\right),
\qquad
4^{\omega(A)}=k^{o(1)}.
\]

For `C\ll k`, this gives the unconditional envelope

\[
\boxed{
\sum_qA_q^2\le k^{1+o(1)}.
}
\]

No fixed-power improvement `k^{1-\delta}` is claimed here.

## 4. Finite diagnostics retained only as observations

The existing discovery calculations give approximately/exactly the following even-conductor energies at the stated exploratory cutoffs:

- `k=862`, `z=29`: energy `23` against about `430` surviving radii;
- `k=8191`, `z=90`: energy `121` against about `4095` surviving radii.

These are finite diagnostics, not an asymptotic theorem. In particular they do not justify asserting `E_C\ll k^{1-\delta}`.

A further finite decomposition at `k=8191` indicates that the two-prime conductor sector already supplies a substantial fraction of the total energy. This is retained only as route-selection evidence: squaring the columns may discard too much of the signed terminal structure to make raw sublinear energy the right primary target.

## 5. Route correction: move from raw energy to the weighted dual boundary

The current smooth-shadow resource theorem gives, for a power cutoff `z=k^{\alpha+o(1)}`,

\[
\Psi_A(C,z)\ge k^{\alpha-o(1)}.
\]

The most useful next representation is therefore not a standalone bound on `E_C`, but an exact terminal-boundary decomposition

\[
\boxed{
B(k,z)=\sum_q\lambda_q(k,z)A_q.
}
\]

Once this is obtained, Cauchy together with the unconditional energy envelope yields

\[
|B(k,z)|
\le
\left(\sum_qA_q^2\right)^{1/2}
\left(\sum_q|\lambda_q|^2\right)^{1/2}
\le
k^{1/2+o(1)}\|\lambda\|_2.
\]

Thus a sufficient coefficient-norm target is

\[
\boxed{
\|\lambda\|_2\le k^{\alpha-1/2-\eta}
}
\]

for some fixed `\eta>0`. Then

\[
|B(k,z)|\le k^{\alpha-\eta+o(1)}<\Psi_A(C,z)
\]

for sufficiently large `k`.

Important specializations:

- half cutoff `\alpha=1`: it is enough to prove `\|\lambda\|_2\le k^{1/2-\eta}`;
- exact-zone shallow end `\alpha=2/3`: it is enough to prove `\|\lambda\|_2\le k^{1/6-\eta}`;
- fourth-root / parity-knee scale `\alpha=1/2`: the crude one-shot Cauchy bound is critical and needs additional cancellation or direct weighted-kernel use.

This interacts directly with the already proved cutoff reuse-width Pareto: at the half cutoff every terminal high prime has reuse width at most `2`. Therefore the highest-value resume target is to derive the exact coefficient vector `\lambda_q` from the terminal deletion/floor remainder mechanism and exploit this sparse matching geometry before asking for stronger cancellation in the raw `A_q` energy.

## 6. Frozen route status at pause

The following are considered closed or deprioritized until new evidence appears:

- generic positive classical linear-sieve cutoff tuning;
- dimension-two positive double-rough lower-sieve tuning;
- attempts to close the problem merely by moving the power cutoff;
- treating repeated factors as the order-`k` obstruction after the Generation-4 exact repair;
- treating `\sum_qA_q^2\ll k^{1-\delta}` as the mandatory first analytic target.

The unresolved difficulty remains squarefree/signed boundary correlation.

When research resumes, the preferred order is:

1. derive the exact half/deep-cutoff terminal dual coefficients `\lambda_q`;
2. prove sparsity/collision/`L^2` control for `\lambda` using reuse width `\le2`;
3. if that alone is insufficient, estimate the weighted pair form using the exact truncated Möbius hyperbola and crossed divisor-root diamond;
4. compare the resulting boundary exponent with the exact smooth-shadow resource exponent.

## 7. Source map retained for continuation

Key source commits already present on the owner line include:

- cutoff Pareto / monotone refinement: `ba9dd97`, `798170f`, tests `db9a604`;
- exact smooth-shadow main: `53755b5`, tests `5f04b75`;
- smooth-shadow power resource: `3e22169`, tests `179f9a1`;
- classical linear-extremal negative theorem: `e504f9d`, tests `a376d9d`;
- cutoff-mixture BRC compiler: `21c3cb6`, tests `c9d66c6`;
- Generation-4 bridge: `68e7fe7`, tests `8aa9357`;
- exact even-conductor L² kernel: `dc14b551531c1e300dca05af9652ba508def2f9b`;
- prior cross-route summary: Research Relay Issue #82 comment `5252221650`.

Research is intentionally paused at this checkpoint. Do not infer a Legendre proof from any item above.