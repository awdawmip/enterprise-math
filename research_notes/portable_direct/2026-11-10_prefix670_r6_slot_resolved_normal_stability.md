# PREFIX-670-R6 — Slot-resolved normal coercivity in the certified BRC boundary strip

Date: 2026-11-10 (Asia/Shanghai). Frozen science `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Status: `AUTHOR_DERIVED / EXACT_RATIONAL_IMPLICATION_CHECKED / UNREVIEWED / NOT_ADMITTED`.

## New exact theorem

For the same frozen 189-layer two-direction BRC first-stop statistical observer, set `V_q(p,z)=q^2 W(p,z)-q mu(p,z)`, where `W=Var(Y)` and `mu=E[Y]`. Let `z_*(q)` be the unique edge optimizer from PREFIX-660 and `M(q)=V_q(0,z_*(q))`. For every real `q in [12,24]`, `p in [0,1/64]` and `z in [607/4096,609/4096]`, define

```
L(q) = q * (76650/12 + 76595*(q-12)/144),
C(q) = (15000*q^2+221*q)/2.
```

Then the entire rectangle has a quantitative slot-resolved stability certificate:

```
M(q)-V_q(p,z) >= L(q)*p + C(q)*p^2 + 6400000*(z-z_*(q))^2.
```

Equality holds precisely at `(p,z)=(0,z_*(q))`; the bound is strict for any other point. In particular,

```
q=12: L=76650,    C=1081326
q=18: L=689685/4, C=2431989
q=24: L=306490,   C=4322652.
```

For `q=24` the certified first-order normal penalty is **306490*p**, rather than the slot-independent **76650*p** used in PREFIX-668. The quadratic term is likewise strengthened by `221*q*p^2/2`.

## Proof, including precise predecessor contracts

PREFIX-661 supplies for every `z` in the stated band:

```
V_{12,p}(0,z)<-76650,  V_{24,p}(0,z)<-306490.
```

For fixed `z`, the quotient `V_{q,p}(0,z)/q=q W_p(0,z)-mu_p(0,z)` is affine in `q`. Its strict endpoint envelopes imply

```
-V_{q,p}(0,z)/q
  > ((24-q)/12)*(76650/12) + ((q-12)/12)*(306490/24)
  = 76650/12 + 76595*(q-12)/144.
```

PREFIX-668 proves throughout the full `p,z` rectangle that `W_{pp}<-15000` and `mu_{pp}>221`. Therefore

```
V_{q,pp}=q^2 W_{pp}-q mu_{pp}<-15000*q^2-221*q.
```

Integrate once in `p` using the strictly negative boundary normal derivative, then integrate again from `0` to `p`:

```
V_q(0,z)-V_q(p,z) >= L(q)*p+C(q)*p^2,
```

with strict inequality for `p>0`. Separately PREFIX-660 gives `M(q)-V_q(0,z)>=6400000*(z-z_*(q))^2`, with strict inequality for `z != z_*`. Add the two independent nonnegative gaps to obtain the theorem. All quantities retain the frozen observer's original meanings.

## Exact verification and research utility

Run `python PREFIX670_R6_SLOT_RESOLVED_NORMAL_STABILITY_CERTIFICATE.py` (Python 3 standard library). It passes **46 exact Fraction/integer checks** including exact interpolation coefficients and three slot instances. This validates implications of predecessor author certificates; it is not an independent rerun of the 189-layer path computation. The completed proof and executable checker may be used as a stronger small-`p` elimination lemma in exact `0<=p<=z<=1/2` interval pruning, where the parent full-domain maximum question remains open.

BRC interface: frozen path multiplicities `A_n(k)`, exact Bernoulli observer probability and Gamma-clock moment-to-variance law. This is a derived, observer-typed lemma, not a native X6 dynamic theorem. Sources: PREFIX-660 `2026-11-10_prefix660_r6_moving_edge_maximum.md`, PREFIX-661 `2026-11-10_prefix661_r6_uniform_edge_strip_stability.md`, PREFIX-668 `2026-11-10_prefix668_r6_coupled_block_quadruple_strip.md`. Latest source-parent immutable ref for PREFIX-668: `f6288695a77bd13ee55752fd73cf177083e7c8db`; exact scientific pin unchanged.

**Next:** make slot-specific rectangle-upper-bound tests that compare against the strongest certified edge competitor, then extend the certified normal curvature beyond `p=1/64` using signed bivariate Bernstein controls.
