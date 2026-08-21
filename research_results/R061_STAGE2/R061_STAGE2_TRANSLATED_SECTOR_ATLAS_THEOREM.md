# R061 Stage 2 — Translated Sector Atlas Theorem

Task-ID: `RS-R061-STAGE2-ARBITRARY-POINT-NATIVE-LINE-TRANSLATION-CROSS-SECTOR-GLUING`  
Taskbook source: `8b197776249e0b18850cee8375488de9aa57cbb4`  
Researcher-ID: `EM-R061S2-3CE600`

## Status

`TRANSLATED_SECTOR_ATLAS_EXACT = true`  
`TRANSLATED_START_INCIDENCE_EXACT = true`

This theorem is derived from the frozen R061 Stage 1/1R sector/trace semantics. Translation is typed as a derived operational action; signed carrier coordinates used below are implementation carrier only.

## 1. Frozen native objects retained

The construction preserves exactly:

- `O_E=0` as a triple cell-boundary intersection, not a cell or center;
- three positive native axis families `E1,E2,E3` only;
- the three native right sectors `S12,S23,S31`, each of native angle `120°`;
- nearest center spacing `1`;
- circle-cell radius `1/sqrt(3)`;
- one canonical incident anchor cell in each fixed open sector;
- coordinate-vertex and cell-center typed copies separated by a constant affine offset.

No native negative axis is introduced.

## 2. Canonical global vertex address and implementation carrier map

Let

`A_E = {(A,B,C) in N_0^3 : min(A,B,C)=0}`

be the frozen glued native vertex atlas.

For the proof only, choose the frozen carrier presentation with coefficient pair `(p,q)` relative to `(t1,t2)` and carrier relation `t3=-t1-t2`. Define the implementation map

`kappa(A,B,C)=(A-C,B-C)`.

This does **not** identify native triples under diagonal shift. On the canonical set `min=0`, `kappa` is injective. It is also surjective onto the integer coordinate-vertex carrier lattice: for `(p,q) in Z^2`, with

`m=min(p,q,0)`,

its unique canonical preimage is

`(p-m,q-m,-m)`.

Thus the signed pair is an `I0_IMPLEMENTATION_CARRIER` address for proving translation/incidence; the native vertex ID remains the nonnegative min-zero triple.

## 3. Translation based at an arbitrary coordinate vertex

For a native coordinate vertex `P`, define `tau_P` by carrier translation through the implementation location `kappa(P)`. It acts on the already-frozen labeled axis families, coordinate vertices, cell centers and circle cells.

The three translated positive rays are

`E_i(P)=tau_P(E_i)`.

The translated right sectors are

`S_12(P), S_23(P), S_31(P)`.

Because translation changes no axis-family label or local incidence relation:

1. the three translated rays partition directions around `P` exactly as at `O_E`;
2. each adjacent pair still forms one native right angle of `120°`;
3. no translated ray requires a native negative axis;
4. translated native axis ticks remain coordinate vertices at unit native tick spacing;
5. translated native axes pass through no cell centers.

## 4. Unique translated sector anchor

Let the frozen origin incidence be

`Sigma_O^(ij): O_E -> C_O^(ij)(0,0)`.

Define by translation, not by guessed numeric offset,

`C_P^(ij)(0,0) = tau_P(C_O^(ij)(0,0))`,

`Sigma_P^(ij) = tau_P(Sigma_O^(ij)): P -> C_P^(ij)(0,0)`.

Then every translated open sector contains exactly one cell center incident to `P`.

If `s_ij=ctr(C_O^(ij)(0,0))-O_E` is the frozen affine offset, then

`ctr(C_P^(ij)(a,b)) = P + V_ij(a,b) + s_ij`

in the implementation carrier presentation. The meaningful theorem is the translation covariance of the incidence map; the numerical carrier representative is only a certificate.

## 5. Exact replay certificate

The committed checker exhaustively replayed the translated incidence theorem on the coordinate-vertex patch

`-4 <= p,q <= 4`

containing `81` start vertices.

It performed `243` translated sector-anchor checks (`81 x 3`) and found:

- one and only one incident anchor in every translated open sector;
- exact carrier radius-square certificate `1/3` for each anchor;
- translated axis vertices remain in the coordinate-vertex residue class;
- no translated native axis vertex is a cell center;
- `mismatch_count = 0`.

## 6. Semantic typing

The carrier `(p,q)` coordinates and `t1+t2+t3=0` relation are used only to prove the translated incidence/decomposition facts. They are not promoted to native signed coordinates or a native vector identity.

`TRANSLATED_SECTOR_ATLAS_EXACT = true`.

`TRANSLATED_START_INCIDENCE_EXACT = true`.
