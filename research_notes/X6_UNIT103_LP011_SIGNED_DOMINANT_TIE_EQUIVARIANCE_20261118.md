# X6 Unit103 — LP011 dominant native axis: exact tie and equivariance boundary

**2026-11-18 | Task** `RS-X6-LEGACY-PLANE-RECONCILIATION` / publication `TP2-B4A441B23DA3159232C2`.

**Status:** AUTHOR-PROVED / FINITE-INTEGER-EXECUTED / UNREVIEWED / NOT_ADMITTED. This is the exact native signed-coordinate selector boundary suggested by the historical LP011 correction, not proof of any previously alleged wrong runtime caller.

## Exact source and model

Frozen P000 V5: `59538f585d037d09ef687b28715c4bc1a3f9fe03`. At that pin, `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md` lines 227–236 gives the six-axis `S6` permutation skeleton. The selected three-axis foundation `definitions/ENTERPRISE_X6_CENTERED_THREE_AXIS_SLICE_REBASE_20260905.md` lines 12–32 and 385–401 uses raw signed `Z^3` displacements and types support-two motion as composite, not one primitive straight direction.

The original author ledger, source `research_artifacts/X6_LEGACY_PLANE_RECONCILIATION/claim_ledger.json` at immutable author commit `5870a14d5ec3b1c639bdef155a7019b1c91a5a58`, blob `5881055c0801ca5bb0970756d500daa0114d36b0`, LP011 lines 76–79, says `Dominant native axis is argmax_i |delta_i|; orientation sign(delta_i) is separate`. The conventional mathematical `argmax` can denote the *entire maximizing set*; if so the formula is valid. A **single index** cannot be inferred without a tie rule, and no such rule is specified in that four-field entry. This is a precise unresolved interface boundary, not a finding that the ledger is false.

## Theorem: S3-covariant maximizer set and no global equivariant single selector

Let `d=(d_0,d_1,d_2) in Z^3`, `M(d)=max_i |d_i|`. Define the signed native candidate set

`D(d) = { (i, sgn(d_i)) : |d_i|=M(d)>0 }`.

For `d=0` define `D(0)=empty` (no direction). Permutations `p in S3` act on the named axes and on vector coordinates. Then

1. `D(p d) = p D(d)` exactly, including ties; reversal gives `D(-d) = { (i,-s) : (i,s) in D(d) }`.
2. A unique signed maximizer exists exactly if exactly one coordinate has maximal positive absolute value. On that subdomain the unique selector is `S3`-equivariant.
3. There is **no** deterministic `S3`-equivariant function choosing one member of `D(d)` for *every* nonzero signed triple. Proof: choose `d=(1,1,0)`, for which `D(d)={(0,+1),(1,+1)}`. The transposition `p=(0\;1)` fixes `d` but exchanges its two allowed candidates. If equivariant `f` were single-valued, then `f(d)=f(pd)=pf(d)`, impossible because neither candidate is fixed by `p`. This is a complete obstruction, not merely finite evidence.
4. For a tie such as `(1,1,0)`, the displacement is a two-axis composite with two shortest primitive signed step words and N-BRC multiplicity `2`; choosing a dominant *display* axis does not select or erase a native step word. A deterministic index-priority tiebreak is possible **only with that additional external priority declared**, and it cannot satisfy full unlabeled axis-permutation covariance.

The same obstruction embeds in the full six-axis `S6` skeleton by swapping any two equally signed nonzero tied axes and fixing the other four. No new primitive axis is added, no P000/worldview alteration follows, and no observer reduction discards the named directions or BRC provenance.

## Independent exact finite execution

A new standalone Python standard-library checker was executed on all signed triples `[-2,2]^3`, all six selected-axis permutations, and exact sign reversal. Normal Python, `-O` and `-OO` produced byte-identical result JSON.

- 125 triples: 1 zero, 60 unique-max, 48 two-way ties, 16 three-way ties.
- 750 exact signed-set permutation identities and 125 reversal identities, all passed.
- The stabilizer witness `d=(1,1,0)` has two tied positive candidates and `2` shortest words.

GitHub source and actual executed local source have the same Git blob SHA1 `6fbfd53982d9d2e872bb3f71e7333c463c3e120e`, SHA256 `54d370fc0a3f80f1b455b68c4ce3a8d46fb096d3f754232bf06c3427a00ae4f7`. Result blob SHA1 `96cf3a2ccd18e90715bacb62fd55000816d7d043`, SHA256 `c55eb6f25edb771ce4cddefd87516f3ba1e12157e2a16d06b3ab09958ae187bb`.

## LP011 integration decision

**Precise correction criterion:** any actual theorem-facing function claiming an intrinsic deterministic `native_dominant_axis` must either restrict to the unique-max subdomain, return the typed set of maximizers with all signed directions preserved, or explicitly declare external tie priority and abandon full `S3` equivariance. The `argmax |delta|` ledger can be retained as a *set-valued* mathematical formula; do not rewrite preserved historical Result or existing author ledger merely to add this distinction.

This result addresses the independent Driver's October 14 request to assess the *dominant-axis sign/tie rule* at the abstract interface. Locating the historical alleged wrong executable signed-argmax caller remains `UNRESOLVED_PROVENANCE`. The original LP019 positive N-BRC cancellation allegation also remains without an exact wrong caller; Unit102 gives the bounded R062 noncancellation source assessment. The full 28-LP consumer coverage and independent Driver review remain open.

No original R063/Helly or other native benchmark was rerun. Evidence is an independent theorem/proof and its own finite checker, not an executed downstream native consumer regression.
