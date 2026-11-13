# R749SH — Two-time provenance Walsh propagator and a one-coordinate joint-relation repair witness

Date: 2026-11-12 (Asia/Shanghai). Mathematical continuation of R749SG (this branch) and pinned R749SF `awdawmip/enterprise-math@066958c8da10e4d67395f3c9b6942a8d9d26daa7`; original scientific evidence pin remains `a72226e2430ffa4786321ac86e7f0c599d5f0389`. Author-side exact finite signed-Port observer result; independent review and native Cell/Link/Port permission are separate.

## Theorem 1 — Exact historical/current joint Walsh transform

Adopt R749SG's fixed legal unsigned observation word `omega`, conditional eight-lift kernel `K_omega,p`, source-lineage map `h_omega` and attenuation `theta=8p/(1+7p)`. Let `X=(X_0,X_1,X_2)` denote initial signed axes and `Y=(Y_0,Y_1,Y_2)` final signed axes, with their *actual named axis labels* carried by omega. For an initial subset `T` and final subset `S`, write signed Walsh characters `chi_T(X)` and `chi_S(Y)`. For every arbitrary initial distribution mu0 and every allowed `p∈[0,1]`, on a positive-probability omega,

```
E[chi_T(X) chi_S(Y) | omega] =
  0                                            if any x in S is a fresh final sign;
  theta^(sum_{x in S} k_x) *
    mu0hat(T △ { ancestor_x : x in S })       otherwise.
```

Here `mu0hat(U)=E_mu0[chi_U(X)]`; `△` is symmetric difference, so shared initial tags cancel by `X_i^2=1`. At p=0, a forced BSC with zero correlation makes its transferred tag fresh for this formula; at p=1 only forced observer transitions are admissible.

**Proof:** Conditional on the entire initial signed state X, use R749SG's monomial-or-zero Walsh pullback for chi_S(Y). Multiplication by chi_T(X) converts the surviving initial parity into chi_{T△Anc(S)}(X), and averaging under mu0 proves the identity. This is an all-path algebraic identity, not a finite-depth extrapolation.

**Corollary — minimal moment list for a declared two-time query family.** For any finite family `Q={(T,S)}` of joint Walsh queries at a fixed omega, discard those whose final S touches a fresh sign. For each remaining query retain `mu0hat(T△Anc(S))` if its exponent is nonzero. Distinct nonempty subset indices are independent affine expectation coordinates on the open initial probability simplex; their number is necessary and sufficient for answering *that declared family* exactly. The empty subset is the known normalization 1. No general-purpose full-history storage is mandated when the query family is narrower.

## Theorem 2 — A native-source joint-relation difference survives current-observer coalescence

Consider the actual six-axis X6 restricted observer path of two-port unsigned supports:

```
A={0,1}, B={1,2}, C={2,3}.
```

It is an allowed *nonforced* unsigned step because `A△B={0,2}≠C`. The old sign of axis 0 is discarded; axis-1 and axis-2 signs are copied; the new axis-3 sign is independent fair ±1 conditional on this observer step, for every `0≤p<1`.

Define two different initial distributions, with X2 an independent fair sign and X1 fair:

```
mu_plus:  X0 =  X1,    P(each of 4 states)=1/4;
mu_minus: X0 = -X1,    P(each of 4 states)=1/4.
```

Both initial priors have the *same marginal* on surviving (X1,X2). Thus both induce the identical final signed-state law `P(Y1,Y2,Y3)=1/8` for all eight final signs. Nevertheless:

```
E_mu_plus[X0 * Y1 | omega]  = +1,
E_mu_minus[X0 * Y1 | omega] = -1.
```

The distinction is exactly one *joint historical/current source-parity moment*. This proves the current eight-state observer is sufficient for current signed-Port queries on this path but **not** for a declared future query that asks about the old X0-to-current Y1 relational provenance. A one-scalar repair coordinate `R=E[X0(initial) * Y1(current)]` is necessary and sufficient to distinguish this pair for this specific query; for general priors and richer joint queries use Theorem 1's minimal moment list.

This is a concrete scope-typed certificate implementing the P000-adjacent `JOINT_RELATION_OBSERVER_PRESERVATION` rule: raw current signs and surviving marginals alone can erase an interaction direction. It is a mathematical statement about the abstract signed-Port kernel; it does not assert any native event pass or physical calibration.

## Finite independent check

`R749SH_TWO_TIME_WALSH_EXACT_CHECK.py` uses exact `Fraction` arithmetic. For the above real signed graph nonforced-step conditional law, it verifies 8 conditional initial rows × 8 initial Walsh characters × 8 final Walsh characters = 512 exact two-time identities. It separately verifies both priors are normalized, that each yields exactly the same uniform eight-state final distribution, and that the historical/current cross-moment is respectively +1 or −1. Actual program result is `PASS`.

## Next science

Extend the fixed-word formula to the smallest sufficient historical/current *time-window* (three or more times) of BRC signed-branch associations, and test an explicit native V29/V39 closure permission witness before mapping the abstract transition law to native events. For mixed adaptive unsigned observation policies depending only on observed supports, conditioning on the realized word retains these identities; policies depending on hidden signs would require a distinct likelihood treatment.
