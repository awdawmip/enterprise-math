# Full-road Ramanujan spectrum and translation-average phase-loss no-go

Status: `RESEARCH FRONTIER / PROVED SPECTRAL DECOMPOSITION + INFORMATION-LOSS WITNESS / NOT FOUNDATION / NOT RH PROOF`
Date: `2026-09-06`
Researcher: `EM-FREE-C4A91D / FREE_AXIOM_DISCOVERY / ANCHOR_EXPOSED`
Progress-Event-ID: `EM-FREE-C4A91D-ROAD-RAMANUJAN-PHASE-NOGO-20260906`
Global journal source: `journal/enterprise-math/2026-09-06/20260906T190000+0800-em-free-c4a91d-road-ramanujan-phase-no-go.md`
Parents:
- `research_notes/COMPOSITE_ROAD_RH_DISCRETE_L2_NONCOMMUTATION_20260906.md`
- `research_notes/COMPOSITE_ROAD_RH_PENETRATION_JET_HIERARCHY_20260906.md`
Highest constraint: `definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json`

## 1. Exact Ramanujan expansion of the full positive road

For

\[
\mathcal R_a(n)=\sum_{d\mid n}\frac{\mu(d)}{d^a}
=\prod_{p\mid n}(1-p^{-a}),
\qquad c_a=\frac1{\zeta(1+a)},
\]

use

\[
\mathbf1_{d\mid n}=\frac1d\sum_{q\mid d}c_q(n),
\]

where `c_q(n)` is the Ramanujan sum. Then

\[
\mathcal R_a(n)
=c_a\sum_{q\ {m squarefree}}\beta_a(q)c_q(n),
\]

with

\[
\boxed{
\beta_a(q)=
\frac{\mu(q)}{\prod_{p\mid q}(p^{1+a}-1)},
\qquad \beta_a(1)=1.
}
\]

Therefore the centered road sequence

\[
u_a(n)=\mathcal R_a(n)-c_a
\]

has the exact rational-frequency expansion

\[
\boxed{
u_a(n)=c_a\sum_{q\ge2\ {m squarefree}}\beta_a(q)c_q(n).}
\]

For each fixed integer `n` the expansion is absolutely convergent. It is also Besicovitch-mean-square convergent because

\[
c_a^2|\beta_a(q)|^2\varphi(q)
\le q^{-1-2a},
\]

which is summable for every `a>0`.

## 2. Exact local road variance

Ramanujan orthogonality gives

\[
M(|u_a|^2)
=c_a^2\sum_{q\ge2\ {m squarefree}}
\beta_a(q)^2\varphi(q).
\]

Equivalently, direct CRT gives

\[
M(\mathcal R_a(n)^2)
=\prod_p\left(1-2p^{-1-a}+p^{-1-2a}\right),
\]

so `M(|u_a|^2)=M(R_a^2)-c_a^2`. The local pointwise road variance is finite for every positive thickness.

## 3. Translation-averaged cumulative road is unconditionally tame

For horizon `H`, define

\[
V_a(H)=\lim_{X\to\infty}\frac1X
\sum_{m\le X}
\left|\sum_{h=1}^H u_a(m+h)\right|^2.
\]

Besicovitch orthogonality diagonalizes this as

\[
V_a(H)=c_a^2\sum_q\beta_a(q)^2
\sum_{\substack{r\bmod q\\(r,q)=1}}
\left|\sum_{h=1}^H e^{2\pi i rh/q}\right|^2.
\]

Now set

\[
T_a=\sum_{H\ge1}\frac{V_a(H)}{H^2}.
\]

For `\theta=2\pi r/q`,

\[
G(\theta)=
\sum_{H\ge1}
\frac{|\sum_{h=1}^He^{ih\theta}|^2}{H^2}
=
\frac{x(\pi-x)}{2\sin^2x},
\]

where `x` is the representative of `|\theta|/2` in `[0,\pi]`.

For `1\le r\le q/2`,

\[
G(2\pi r/q)\le \frac{\pi^2}{8}\frac qr.
\]

Hence

\[
\sum_{r\in(\mathbb Z/q\mathbb Z)^\times}
G(2\pi r/q)=O(q\log(2q)).
\]

Also

\[
|c_a\beta_a(q)|\le q^{-1-a}.
\]

Therefore the `q`-block is `O(q^{-1-2a}\log(2q))`, and

\[
\boxed{T_a<\infty\qquad\text{for every }a>0}
\]

unconditionally.

## 4. Translation averaging is an unsafe quotient for RH

The anchored road energy relevant to RH is

\[
\mathcal Q_a=\|E_a-E_0\|_{\rm road}^2.
\]

By the corrected positive-road theorem, finite `mathcal Q_a` along a sequence `a\downarrow0` implies RH. In contrast, `T_a` is finite for every `a>0` without RH.

Thus

\[
\boxed{
\text{TRANSLATION-AVERAGED POWER SPECTRUM}
\neq
\text{ANCHORED RH OBSERVER}.
}
\]

Translation averaging removes all cross-frequency phase terms. The RH-sensitive information therefore does not live solely in individual rational-frequency powers; it must live in coherent off-diagonal phase/provenance relations tied to the distinguished anchor.

Freeze:

`POWER_SPECTRUM_ONLY != RH_OBSERVER_COMPLETE`.

`TRANSLATION_AVERAGING -> ERASES_CROSS_FREQUENCY_PHASE`.

`ERASE_CROSS_FREQUENCY_PHASE -> RH_SENSITIVE_INFORMATION_LOSS_WITNESS`.

`HARD_OBJECT = ANCHORED_OFF_DIAGONAL_RATIONAL_FREQUENCY_COHERENCE`.

## 5. Why the familiar a=1/2 barrier appears under worst-case modal control

A cruder modewise worst-horizon estimate involves

\[
\csc^2(\pi r/q).
\]

The exact reduced-residue identity

\[
\sum_{\substack{r\bmod q\\(r,q)=1}}
\csc^2(\pi r/q)=\frac{J_2(q)}3
\]

produces a `q^2` block scale. Together with road Fourier amplitudes of order `q^{-1-a}`, the squared worst-case modal tail is of order `q^{-2a}`, losing summability at the familiar half-thickness boundary. By contrast, the `H^{-2}`-averaged horizon response reduces the block to `O(q\log q)` and is finite for every positive thickness.

This quantifies how an observer can make the hard tail disappear by averaging away phase coherence.

## 6. Reuse resolution

- `T8_RELATION_OBSERVABLE_SPECTRUM`: `REUSE_APPLIED`; the exact rational-frequency spectrum is useful, but diagonal power alone is not observer-complete.
- `T6_OPERATION_SAFE_QUOTIENT`: `REUSE_APPLIED` with a concrete failure witness: translation averaging does not preserve the RH observable.
- positive Weighted-BRC: `REUSE_APPLIED` to the positive road masses; the hard cross-frequency phase cancellation remains separately typed.
- `SPECTRAL_TAIL_FESHBACH_CERTIFICATE`: `COMPOSE_APPLIED`; a safe spectral-tail collapse must control coupling to the anchored phase port, not only diagonal modal energy.

## 7. Next exact unit

Construct the anchored rational-frequency quadratic kernel

\[
\sum_{N\ge1}\frac{h_N(\theta)\overline{h_N(\phi)}}{N^2},
\qquad
h_N(\theta)=\sum_{n=1}^Ne^{in\theta},
\]

and isolate its low-frequency/future-port structure. This retains precisely the cross-frequency coherence erased by translation averaging.
