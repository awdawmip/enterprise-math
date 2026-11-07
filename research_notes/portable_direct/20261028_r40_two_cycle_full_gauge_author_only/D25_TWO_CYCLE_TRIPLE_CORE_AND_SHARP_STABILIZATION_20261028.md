# D25/LIFT — complete two-cycle gauge orbit coding, minimal active core, and sharp stabilization

**2026-10-28 · Portable author theorem and exact finite certificate.** Classification: `AUTHOR_DERIVED / AUTHOR_EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE`. Source-native Task ownership, CLAIM/OPEN, Result and Source checkpoint have not been established by this Site-bound caller. This is an ordinary finite-field auxiliary model, **not** a representation of the original CM/H0/B0 class unless a separate, source-checked interface proves the identification.

## Question and reused frontier

Prior author-only results on Draft PR #1566 classify the full-centralizer gauge orbits for two scalar-eigenvalue blocks of sizes `(m+1)` and `(m+2)`. Instead of extending one block size at a time, this unit asks for **one exact coordinate classification covering every `(m+n)`**, plus the exact first dimension where orbit counts stabilize. The reusable mathematical input is the block commutator interface: with `A=diag(a I_m,b I_n)` and `a != b`, the full image of `B -> [B,A]` consists of the ordered off-diagonal pairs

\[
X:W\longrightarrow V,\qquad Y:V\longrightarrow W,
\quad \dim V=m,\ \dim W=n,
\]

with gauge action

\[
(g,h):(X,Y)\longmapsto(gXh^{-1},\;hYg^{-1}),
\quad (g,h)\in\mathrm{GL}(V)\times\mathrm{GL}(W).
\]

Since `a != b`, each ordered `(X,Y)` really arises from a source `B`; the source matrix `B` is *not* reconstructed by the gauge quotient. All field arithmetic in the proof is exact. No requirement that the field have odd characteristic is needed for this auxiliary theorem.

## Theorem A — complete triple classification for arbitrary `m,n`

Let `k` be any field and `n,m >= 0`. Define, in the **same W-port**,

\[
S=\ker X\le W,\qquad D=\operatorname{im}Y\le W,\qquad T=YX\in\operatorname{End}_k(W).
\]

The triple satisfies `S <= ker T` and `im T <= D`. Define its **minimal active V-dimension**

\[
\boxed{d(S,D,T)=(n-\dim S)+\dim D-\operatorname{rank}T.}
\]

**Claim.** Gauge equivalence classes of `(X,Y)` with fixed `(m,n)` are in natural bijection with simultaneous `GL(W)`-orbits of triples `(S,D,T)` satisfying

\[
S\le\ker T,\quad\operatorname{im}T\le D,\quad d(S,D,T)\le m.
\]

The action on triples is `h.(S,D,T)=(hS,hD,hTh^{-1})`. No additional invariant on the V-port is needed **for this precise full two-sided gauge action**. This does not assert that the triple retains a source-marked basis, coefficients of `B`, an odd Hesse/Green port, or arbitrary future operations.

### Proof: necessity and construction

For a given pair, `kerX` and `imY` are transported by `h`, while `YX` changes by conjugation. Put `r=rank X=n-dim S`, `s=rankY=dim D`, `t=rank(YX)`. Since `Y|imX` has rank `t`,

\[
\dim(\ker Y\cap\operatorname{im}X)=r-t.
\]

Therefore the dimension of a complement to `kerY cap imX` in `kerY` is

\[
(m-s)-(r-t)=m-(r+s-t)=m-d\ge0.
\]

Conversely, take any admissible triple and write `C=W/S`. Since `S <= ker T`, `T` induces a well-defined map `\bar T:C -> D`, with image `im T`. Choose a linear complement `L` of `im T` in `D` (`D=im T direct_sum L`) and define

\[
V_0=C\oplus L,\quad
X_0(w)=(w+S,0),\quad
Y_0(c,\ell)=\bar T(c)+\ell.
\]

This pair has exactly `ker X0=S`, `imY0=D`, and `Y0 X0=T`, and

\[
\dim V_0=\dim C+\dim L=r+(s-t)=d.
\]

For `m>=d`, add a complementary `(m-d)`-dimensional V-space `U` on which both `X` and `Y` have zero components; that is, `X(W) subset V0` and `Y(U)=0`. This realizes **every** admissible triple.

### Proof: completeness, including singular and nilpotent cases

Now start with any pair having the same exact triple on `W`. Identify `imX` with `C=W/S` via `X`. Choose a complement `L` of `imT` in `D`, and for each `\ell in L` choose a linear lift `j(\ell) in V` with `Y j(\ell)=\ell`. Then

\[
V_0=\operatorname{im}X\oplus j(L)
\]

is a direct sum: if `j(ell)` lies in `imX`, its Y-image lies in both `L` and `imT`, so `ell=0`. Its Y-image is `D`; it has dimension `d`, and the restrictions of `(X,Y)` to `V0` identify exactly with the constructed `(X0,Y0)`.

Choose `U` complementary to `imX cap kerY` inside `kerY`. Since `kerY cap V0=kerY cap imX`, it follows that `V=V0 direct_sum U` with `dim U=m-d` and `Y(U)=0`. Thus every pair with the exact same `(S,D,T)` is gauge-equivalent, even when either map or `T` is singular, nilpotent or zero. If two triples differ by `h in GL(W)`, transport the construction by `h` and apply the corresponding `g in GL(V)`. This proves the stated bijection. No use of Krull–Schmidt or a classification of cyclic-quiver indecomposables is required.

## Theorem B — sharp orbit-count stabilization at `m=2n`

For finite `k=F_q`, let `N_q(m,n)` be the number of orbits of ordered pairs. Adding one zero V-coordinate defines an **injective** map of orbit sets `N_q(m,n) -> N_q(m+1,n)`: by Theorem A, both are exactly the same triples with the latter admitting additional larger-core triples.

As `rank X <= n`, `rankY <= n`, and `rankT >= 0`, every admissible triple has `d <= 2n`. Hence the padding map is **bijective for every `m>=2n`**:

\[
\boxed{N_q(m,n)=N_q(2n,n)\qquad(m\ge2n).}
\]

The threshold is sharp for **every** `n>=1`. For each `1<=d<=2n`, let `V=k^d`, choose `r=min(d,n)` and `s=d-r`, take `X` of rank `r` into the first `r` V-coordinates and `Y` of rank `s` supported on the other `s` coordinates, with `Y X=0`. Then `d(S,D,T)=r+s=d`. Thus for each `0<=m<2n` there exists an orbit in dimension `m+1` not arising from padding a pair of dimension `m`; consequently

\[
\boxed{N_q(m+1,n)>N_q(m,n)\quad(0\le m<2n,\ n\ge1).}
\]

For `n=0` there is one orbit for every `m`, and the stabilization threshold is zero. The theorem is valid for all finite prime-power fields `F_q`. The core construction itself works over arbitrary fields, although `N_q` counts are only asserted where the sets are finite.

An exact counting reduction follows. Put `c_{d,n}(q)` for the number of `GL_n(F_q)`-orbits of triples with core dimension **exactly** `d`. Then

\[
N_q(m,n)=\sum_{d=0}^{\min(m,2n)}c_{d,n}(q),\qquad c_{d,n}(q)>0\ (0\le d\le2n).
\]

The number of **raw, basis-marked triples** at saturation, before dividing by the `GL_n` action, is exactly

\[
\boxed{\sum_{r=0}^{n}\sum_{s=0}^{n}
\binom{n}{r}_{q}\binom{n}{s}_{q}\,q^{rs}.}
\]

Indeed choose `S` of codimension `r`, choose `D` of dimension `s`, then choose any linear map `T:W/S -> D` (`q^(rs)` choices). This is a finite reduction from `GL_m x GL_n` to the **single small W-port** `GL_n`, independent of `m` once `m>=2n`.

## Theorem C — exact finite new certificate for `n=3, q=2`

The executable checker exhaustively enumerated all sixteen subspaces of `F_2^3`, all 512 linear endomorphisms `T`, and retained exactly the **2,825** admissible triples `(S,D,T)`. It enumerated all **168** invertible `3x3` matrices, conjugated every admissible triple, and partitioned the triples into orbits using exact integer bit arithmetic. The orbit numbers by minimal core dimension `d=0,1,...,6` are

\[
\boxed{(c_{d,3}(2))_{d=0}^{6}=(1,4,15,32,15,4,1).}
\]

A separate Burnside total of fixed triples was `12,096`; division by `|GL_3(F_2)|=168` gives exactly `72`, matching the explicit orbit partition. Therefore the fully enumerated **finite** orbit counts are

| `m` | 0 | 1 | 2 | 3 | 4 | 5 | 6 | any `m>=7` |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `N_2(m,3)` | 1 | 5 | 20 | 52 | 67 | 71 | 72 | 72 |

This `n=3, q=2` count is an **exact finite computation with supplied source**, not a symbolic formula for every `q`, an independent check, or an original native H0/B0 measurement.

## Verification and falsification boundaries

`d25_two_cycle_core_stabilization_checker_20261028.py` uses exact modular row elimination and construction of `U`/`V0`. It checks 76,724 fully enumerated `(X,Y)` configurations across fifteen prime-field `(q,n,m)` cases, 900 deterministic larger random pairs, and twelve explicit sharpness constructions (including `q=373`, `n<=4`). It independently groups 76,569 small-field pairs by their `GL_n`-triple canonical keys across eleven `(q,n,m)` cases, comparing with prior full-group orbit totals. It then performs the full `F_2^3` triple enumeration, 474,600 finite gauge-action applications and the Burnside fixed-point crosscheck. The exact output is `d25_two_cycle_core_stabilization_author_check_20261028.json`. Finite checks do not substitute for the universal proof above.

This auxiliary theorem is **not** a compression authorization for the source-marked CM/Frobenius system. Its carrier is `(V,W,X,Y)` with all directed ports and provenance; its observer is full two-sided gauge orbit. The triple `(S,D,T)` is a complete coordinate **for this observer**, and only future maps proven equivariant with this gauge/padding are safe to evaluate after the quotient. The dimension `m` must remain available as a typed parameter when a future operation can examine unused V-directions. In particular a native smaller gauge group, a fixed source basis, Green/Hesse phase, or `Delta_p-R_p` may distinguish states merged by the full gauge, so their preservation requires a separate exact fiber-constancy/descent check. BRC reuse is a precise full-gauge information-fiber theorem, **not** a new BRC primitive or an X6-to-vector-space ontology bridge.

## Exact next gates

1. **Native scientific interface**: Issue `awdawmip/enterprise-math#1559` must supply the original same-class `p=373` Frobenius and normalization, actual rank, admissible gauge group, signed observer and `Delta_p-R_p`. Determine whether it has a legitimate two-block decomposition; if not, retain the original native structure and treat this work as an auxiliary finite-field theorem only.
2. **Source authority/provenance**: the current Site identity has read-only scope and no research executor binding. Consume the original request receipt and exact Source continuation through a future *actually authorized* identity, without copying another conversation's session/claim. If a current-input-only seed is returned, fully read its pinned `input_artifacts` and set `frontier_notes.completed_units=[]`; put this portable work in staged evidence / do-not-repeat, not predecessor-completed Source units.
3. **UR V2**: recover the original four-file bundle, verify **94,687 bytes** and SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`, and supply only missing legitimate writer/provenance/checkpoint. Do not re-prove UR or reconstruct bytes as original.

Frozen scientific Source pin remains `c47e13e4aba0e006366f989d6334d443f6333ae3`. P000 and ACTIVE Heartbeat X6 remain unchanged. No canonical Task publication, Source claimant, Result, review or admission is inferred from this author artifact.
