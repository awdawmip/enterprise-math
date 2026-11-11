# X6 diagonal quotient: exact least-native-gauge lift and recovery ambiguity

Status: DRIVER_MATHEMATICAL_AUDIT / PROVED_AUXILIARY_LEMMA / NOT_NATIVE_RESULT_ADMISSION
Date: 2026-11-12 (Asia/Shanghai)
Scope: centered signed three-axis slice $d\in\mathbb Z^3$; diagonal translation quotient $\mathbb Z^3/\mathbb Z(1,1,1)$. No Foundation or native metric redefinition.
Associated task: RS-X6-LEGACY-PLANE-RECONCILIATION, TP2-B4A441B23DA3159232C2; historical Result RR-943A793DB1F7B8012A85, HRI-1A48B2D7F0E242FCC2C57D7E (REQUEST_REVISION).

Context/attribution: preserves original X6 legacy-plane work by EM-X6P-40B5BD, the retyped quotient and gauge definitions stewarded in existing Source, and the previous Driver LP-011 audit. This is a shared-context follow-on, not a blind independent review, CLAIM, formal Result or change of the historical disposition.

## Typed setup and theorem

Let $r=\rho(d)=d-\min_i(d_i)\mathbf 1$, so $r\in\mathbb Z_{\ge0}^3$ and $\min_i r_i=0$. Every signed native lift of this observer address is $d_\mu=r+\mu\mathbf1$, where $\mu\in\mathbb Z$. Define $S=r_1+r_2+r_3$, $N=\sum_i r_i^2$, and the existing diagonal-invariant *carrier* quadratic

$$
Q_{\mathrm{car}}(r)=r_1^2+r_2^2+r_3^2-r_1r_2-r_2r_3-r_3r_1.
$$

Let $G(d)=\sum_i d_i^2$ be the native signed-slice squared gauge.

**1. Observer-fiber native gauge.** Exactly,

$$
G(d_\mu)=N+2S\mu+3\mu^2.
$$

**2. Unique least-gauge lift and exact bridge.** Exactly,

$$
\mu_*=-\left\lfloor\frac{S+1}{3}\right\rfloor,\qquad
G_*(r):=\min_{\mu\in\mathbb Z}G(d_\mu)
=N-\left\lfloor\frac{S^2}{3}\right\rfloor
=\left\lceil\frac{2Q_{\mathrm{car}}(r)}3\right\rceil.
$$

The integer minimizer $\mu_*$ is unique. The function $G_*$ is a **derived least-lift functional** on the quotient, not the native gauge $G(d)$ for an arbitrary native displacement, nor an identification of the carrier form with the native metric.

**3. Complete fiber energy spectrum.** Let $t=\mu-\mu_*$ and $\epsilon=S+3\mu_*\in\{-1,0,1\}$. Then

$$
G(d_\mu)=G_*(r)+3t^2+2\epsilon t.
$$

Consequently, the observer chart $r$ plus an exact native squared gauge value $G$ determines the original common level $\mu$ **uniquely if $3\nmid S$**. If $3\mid S$, the minimum gauge has one lift and every admissible nonminimum gauge has exactly two integer lifts $\mu_*\pm t$. This characterizes the exact residual information loss after providing the squared gauge.

**4. Reversal.** If $Q=\max_i r_i$, then

$$
\rho(-d)=Q\mathbf1-r.
$$

This min-zero observer operation is an involution. It preserves $Q_{\mathrm{car}}$ and $G_*$, while native reversal preserves $G(d)$ at the actual signed displacement. The uncorrected positive-section squared sum $N$ may differ under reversal:

$$
N(r)-N(Q\mathbf1-r)=2QS-3Q^2.
$$

## Proof

Expansion of $\|r+\mu\mathbf1\|_2^2$ gives part 1, and completing the square gives

$$
G=N-\frac{S^2}{3}+3\left(\mu+\frac S3\right)^2.
$$

For integer $S$, the nearest integer to $-S/3$ is unique and is $-\lfloor(S+1)/3\rfloor$. The squared correction to the real minimum is $0$ or $1/3$. Using $3N-S^2=2Q_{\mathrm{car}}$ and the integrality of $G$ yields the exact ceiling expression in part 2. Substitution $\mu=\mu_*+t$ yields part 3. Equality between gauges at two levels factors as

$$
G(d_\mu)-G(d_\nu)
=(\mu-\nu)\bigl(3(\mu+\nu)+2S\bigr).
$$

Thus distinct integer levels can share a gauge exactly when $3\mid S$, and then they are symmetric about $-S/3=\mu_*$. Finally $\min(-d)=-\max(d)=-(\mu+Q)$ proves $\rho(-d)=Q\mathbf1-r$. Direct expansion proves the remaining reversal identities. QED.

## Exact diagnostic example

For $r=(3,4,0)$, one has $S=7$, $Q_{\mathrm{car}}=13$, $\mu_*=-2$, and $G_*=9$. The actual signed native displacement $d=(3,4,0)$ instead has $G(d)=25$. Its reverse $-d=(-3,-4,0)$ also has native gauge 25, while the reverse observer *representative* $(1,0,4)$ has the naive squared-section sum 17. Both observer addresses have least-lift gauge 9. This explains the historical LP-013 observation without retyping a relative observer quantity as native distance.

## Exact finite regression check

All $7^3-6^3=127$ triples $r\in\{0,\ldots,6\}^3$ with $\min_i r_i=0$ were enumerated in Python 3. The check compared $G_*$ with $\lceil 2Q_{\mathrm{car}}/3\rceil$, checked the spectrum formula for $\mu\in[-8,8]$, checked the minimum against levels $\mu\in[-10,10]$, and checked the equality criterion for all pairs $\mu<\nu$ with $\mu,\nu\in[-7,7]$. There were **zero mismatches** in these finite domains; the 127 charts split into $43$ with $S\equiv0\pmod3$ and $42$ in each of the two other residue classes. The proof above is universal; this is supplementary regression evidence only.


## Sharp one-bit recovery and a signed-BRC counterexample

The fiber classification yields a precise **full native displacement-recovery** result, not merely an axis query. Given a realizable pair $(r,G(d))$, the compatible integer common levels form a singleton except when $3\mid S$ and $G(d)>G_*(r)$, in which case there are exactly two. Thus an additional binary choice of sign of $\mu-\mu_*$ is necessary and sufficient precisely in the exceptional case; zero extra information is needed otherwise. This is an information-theoretic statement **conditioned on the exact native squared gauge already being available**, not a claim that this gauge can be computed from the observer chart alone.

The extra bit can also matter to exact native shortest-path/BRC readouts. Take $r=(3,0,0)$, with $S=3$ and $\mu_*=-1$. The two nonminimal signed lifts

$
d_+=(3,0,0)\quad(\mu=0),\qquad d_-=(1,-2,-2)\quad(\mu=-2)
$

share **exactly the same** observer chart $r$ and squared gauge $G=9$, but their native $L^1$ shortest step counts differ: $T(d_+)=3$ and $T(d_-)=5$. For the stated signed-axis shortest-word convention, with weights $T!/\prod_i|d_i|!$, their path multiplicities are $M(d_+)=1$ and $M(d_-)=30$. These are exact integer calculations in the already established signed-$\mathbb Z^3$ slice; they prove that neither $T$ nor this signed shortest-path multiplicity universally factors through the pair $(\rho(d),G(d))$.

This counterexample closes the immediate factorization discriminator without asserting anything about physical X6 rotation, path-word identity beyond shortest-word counts, or general Weighted-BRC composition laws. The bit recovers the entire signed triple and hence its associated exact shortest-word count, but does **not** by itself identify which of several native paths was traveled, their order/provenance, or a complete dynamical successor rule.

## Existing sources, obligations and next discriminator

This theorem quantitatively links the already-defined quotient carrier form in definitions/ENTERPRISE_DERIVED_DIAGONAL_DISPLACEMENT_QUOTIENT_20260826.md (verified Git blob 175d2c0f00db8e94a263442dbdc77928c0dc9567) to the retyped signed native gauge in definitions/ENTERPRISE_ARBITRARY_POINT_DIRECTED_LINE_GAUGE_20260821.md (blob 875e3b274e5be03c5872f782872065a0b96d14eb), and extends research_notes/driver/2026-11-12_x6_lp011_observer_axis_minimal_side_channel.md (blob 8eb065792d646594d16132626e14e9439fa30878). It establishes neither native rotation dynamics nor BRC path-fiber equivalence.

The X6 historical HRI remains REQUEST_REVISION. Unresolved documentary obligations are the exact pre-rebase original LP-011 wording and the secondary digest mismatch in recomputation_summary.json. The existing frozen custody map reports a declared SHA256 a40e89f66ffa42b684b918780994cdfd86b176eebdd3a71d87b89c815e975839, but byte-custody SHA256 21ac687263bc55283be5e50dcbab8dd3b6024900a323f941b3f703077cebf46f and original primary Git blob c6d42b50e75a9c05e93e922e88ddfd9f1e2eb14a. The mathematical theorem does not resolve this historical integrity discrepancy.

Next discriminating question: determine the minimum state needed to recover operation-safe **individual path identity and composition** from a signed endpoint and step-count or multiplicity data; the one-bit theorem above settles only endpoint displacement recovery once the exact native squared gauge is supplied.
