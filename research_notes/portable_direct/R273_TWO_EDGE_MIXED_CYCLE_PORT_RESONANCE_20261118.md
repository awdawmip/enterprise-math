# R273 — Exact two-edge mixed-cycle BRC Port resonance and sharp conditional precision

2026-11-18 · AUTHOR_PROVED / EXACT_RATIONAL_CHECK / NOT_REVIEWED.

**Scientific lineage.** Follow R271–R272 at commit `bafca0cfdb4a7814cc5d74534ff9ade753029b4a`, frozen science pin `43ec6098b1330ae86d0a7863be336c5d97f6ef34`; exact typed Port interface WBRC-T30/T31/T32, `definitions/ENTERPRISE_BRC_RECURRENT_PORT_FOUNDATION_20260903.md` (blob `e7823e69fe8112663af2feeb3fc3207b73b2fabe`). Object: finite positive-rational stable BRC effective-Port modules, retained visible Port labels, and permitted nonnegative rational Port edges. P000/Heartbeat-X6, signed branch provenance and observer-fidelity constraints remain separate.

## Theorem A — exact two-edge response

Let `A=I-W`, `S=A^(-1)` for a stable visible labeled-Port system, and let `u!=v` be visible labels. Insert two edges, `u->v` of weight `a>=0` and `v->u` of weight `b>=0`, assuming the resulting system is also stable. Define

```
U = [a e_u, b e_v],     V = [e_v, e_u],
M = I_2 - V^T S U
  = [[1-a*S_vu, -b*S_vv],
     [-a*S_uu,  1-b*S_uv]].
```

Then `det M != 0` and the exact identity is

```
S' - S = S U M^(-1) V^T S,
det M = (1-a*S_vu)(1-b*S_uv)-ab*S_vv*S_uu.
```

**Proof.** The updated inverse problem is `A'=A-U V^T`. Multiplying `A'` with `S+S U (I-V^T S U)^(-1) V^T S` yields the identity. The matrix determinant lemma gives `det A'=det A det M`, so stability/invertibility makes `M` nonsingular. This is the classical Woodbury identity, here applied to the *actual permitted labeled-Port edge interface*.

For each entry put `F_ij=(S U adj(M) V^T S)_ij`, `d=det M`. Then `S'_ij-S_ij=F_ij/d`; if `F_ij != 0`, its 13-adic valuation is exactly `v13(F_ij)-v13(d)`. Numerator terms must be combined before taking valuations: a linearized or independent-edge estimate can miss mixed paths and cancellation.

## Theorem B — individually invisible, jointly resonant edges

Use precisely two visible labeled Ports with empty hidden module and baseline `W=0`, hence `S=I_2`. Adding the edges produces

```
W(a,b)=[[0,a],[b,0]],
S(a,b)=(1/(1-ab))*[[1,a],[b,1]],       0<=ab<1,
S(a,b)_11-1=ab/(1-ab).
```

If either edge alone is inserted (`a=0` or `b=0`), the *selected diagonal observer* `S_11` stays **exactly 1**, for every allowed weight. For both edges, the joint cycle changes `S_11`; the complete one-edge matrices still reveal their edge weights, so this result is precisely scoped to the named observer.

For every `t>=1`, take `P=13^t`, `a=b=1/(1+P)`. Both contexts are strictly stable and

```
1-ab = P(P+2)/(1+P)^2,        v13(1-ab)=t,
v13(S(a,b)_11-1)=-t.
```

Thus a mixed two-edge cycle produces an **arbitrarily deep 13-adic resonance** even though either edge's individual contribution to this observer is identically zero. The cycle is a concrete joint-relation residual. There is also a stability distinction: with `a=b=2`, either single directed edge is nilpotent and stable, but their simultaneous pair has spectral radius 2 and is unstable. Single-edge stability outcomes do not determine the joint outcome.

## Theorem C — sharp conditional precision of the normalized joint observer

Let `t,m>=1`, and compare two strictly stable two-edge systems `(a_0,b_0)` and `(a_1,b_1)`, with all four weights in the localized ring `Z_(13)`. Assume the **certified** depths `v13(d_0)=v13(d_1)=t`, where `d_i=1-a_i b_i`. If

```
a_0 = a_1 (mod 13^(t+m)),  b_0 = b_1 (mod 13^(t+m)),
```

then

```
13^t / d_0 = 13^t / d_1 (mod 13^m).
```

**Proof.** Subtraction gives `13^t (a_0b_0-a_1b_1)/(d_0d_1)`. The product difference has valuation at least `t+m`, and the denominator has valuation `2t`. Therefore the normalized selected star difference has valuation at least `m`.

**Sharp for every t,m even with b fixed.** Put `P=13^t`, `Q=13^(t+m-1)` and choose

```
b = a_0 = 1/(1+P),
a_1 = 3/((1+P)(3+Q)).
```

These are positive, have `a_0b<1` and `a_1b<1`, and

```
a_0-a_1=Q/((1+P)(3+Q)),  v13(a_0-a_1)=t+m-1,
d_0=P(P+2)/(1+P)^2,
d_1=[3P(P+2)+Q(1+P)^2]/[(3+Q)(1+P)^2].
```

Both denominator valuations equal `t`. For `m=1`, the numerator of `d_1` divided by `P` is `7 (mod 13)`; for `m>=2`, it is `6 (mod 13)`. The exact normalized difference

```
13^t*(1/d_0-1/d_1)
 = Q(1+P)^2 / [(P+2)*(3P(P+2)+Q(1+P)^2)]
```

has valuation **exactly `m-1`**. So `t+m-1` input digits are insufficient for this restricted observer and these admissible stable contexts; the `t+m` bound above is sharp. For this family the full inverse has Smith pole depth `t`, consistent with R271; R272's cheap single-edge rule cannot be composed without the feedback determinant.

## Verification and scope

Standalone Python `fractions.Fraction` checker tests all 48 exact pairs `1<=t<=8`, `1<=m<=6`: strict stability, zero effect of either single edge, inverse entries, exact determinant valuations, the input perturbation valuation and the sharp output difference. Three additional positive-rational nonzero-baseline two-Port examples verify the full Woodbury matrix identity exactly. It also checks the separate-vs-joint stability example. Result `PASS 48 WOODBURY 3`. Generated complete JSON SHA-256: `a8db8beb33f971971ecb00598123451dfae2c5fa4bd53dfd379aa564d36d3499`. Arbitrary `t,m` is proved symbolically above; the finite computation verifies an explicit bounded range.

This Port-specific auxiliary reduction preserves the labeled edges and their joint cycle. A future quotient of native branches, ports, source provenance or joint-composite directions requires an exact observer/future-operation descent proof. WBRC-T32 retains exact `W_eff` for unrestricted permitted contexts. Independent peer review and Result/Foundation adoption remain pending.

## Next questions

1. For a fixed sparse edge family on an interacting nonzero module, classify `v13(F_ij)` and `v13(det M)`, including cancellation strata and locally sharp precision witnesses.
2. For a declared horizon of sequential Port insertions, construct and prove a minimal retained mixed-cycle residual coordinate through exact fiber constancy; use full `W_eff` outside the certified horizon.
3. Continue testing an actual provenance-preserving mapping from R269 auxiliary source orbit sequences into native WBRC Ports.

**Artifacts:** this MD theorem/proof, `R273_two_edge_port_resonance_checker.py`, and `R273_verification_digest.json`. Full machine JSON is regenerable by the checker, with the SHA-256 above.
