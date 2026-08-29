# P000 FCC 六线旋转代数与 Rubik-word calculus — Research Return

Status: `RESEARCH_RETURN_FROZEN / SUCCESS_WITH_TYPED_NATIVE_BOUNDARY / AWAITING_DRIVER_REVIEW`

Task: `RS-P000-6D-AXIS-MIXING-ROTATION-GROUPOID`
Publication: `TP2-040D3DF614D42C696220`
Researcher: `EM-P06DRA-4C91B7`
Claim: `chatgpt-p06dra-20260829-1246-4c91b7`
Execution branch: `research/p000-6d-axis-mixing-rotation-algebra-em-p06dra-4c91b7`
Taskbook blob: `sha1:d0b041291dace564c264ab393db5c84df7f2006f`

Hard target:

`P000_FCC_SIX_LINE_ROTATION_ALGEBRA_AND_RUBIK_WORD_CALCULUS_EXACTLY_CLASSIFIED`

## 1. Frozen atlas and exact K4 identification

Use the frozen relabeling

`L_AB=L1, L_AC=L3, L_AD=L6, L_BC=L5, L_BD=L4, L_CD=L2`.

Then the four slices are exactly the four vertex-stars of `K4`:

- `S_A={AB,AC,AD}`
- `S_B={AB,BC,BD}`
- `S_C={AC,BC,CD}`
- `S_D={AD,BD,CD}`.

Each line occurs in exactly two slices and `S_i ∩ S_j={ij}`. Hence the atlas incidence structure is exactly `K4`, so `Aut(atlas)=Aut(K4)=S4`.

This is an incidence statement only; the physical FCC carrier realization is checked separately.

## 2. Exact FCC carrier rotation skeleton

Let `O_FCC` be the determinant-`+1` signed `3x3` permutation matrices. There are exactly `3!*2^2=24`.

Exact integer enumeration shows that every `Q∈O_FCC` permutes the six frozen unoriented `[110]` line families and the four slice types, and that the 24 induced slice permutations are pairwise distinct and exhaust `S4`.

Thus

`O_FCC ≅ S4`

on the frozen carrier atlas, and for `σ∈S4`

`R_σ(L_ij)=L_{σ(i)σ(j)}`.

The six-edge action is faithful. This is the orientation-preserving cubic/FCC carrier skeleton; it is not a claim that `S4` is the full native P000 rotation group.

## 3. Six-slot formula and minimal generators

For slot order

`x=(x_AB,x_AC,x_AD,x_BC,x_BD,x_CD)`

the exact coordinate rule is

`(R_σ x)_ij = x_{σ^{-1}(i)σ^{-1}(j)}`.

Therefore

`R_σR_τ=R_{στ}`, `R_σ^{-1}=R_{σ^{-1}}`, `R_e=I`.

Choose

`a=(BCD)`, `b=(AB)`.

Then `ord(a)=3`, `ord(b)=2`, `ord(ab)=4`, and `<a,b>=S4`. Two generators are minimal because `S4` is not cyclic.

On the six lines:

`ρ(a)=(AB AC AD)(BC CD BD)`

`ρ(b)=(AC BC)(AD BD)`.

In slot order `(AB,AC,AD,BC,BD,CD)`,

`P_a=`

```text
[0 0 1 0 0 0]
[1 0 0 0 0 0]
[0 1 0 0 0 0]
[0 0 0 0 1 0]
[0 0 0 0 0 1]
[0 0 0 1 0 0]
```

and

`P_b=`

```text
[1 0 0 0 0 0]
[0 0 0 1 0 0]
[0 0 0 0 1 0]
[0 1 0 0 0 0]
[0 0 1 0 0 0]
[0 0 0 0 0 1]
```

One exact `3x3` carrier realization is

```text
Q_a = [[ 0,-1, 0],
       [ 0, 0, 1],
       [-1, 0, 0]]

Q_b = [[ 0,-1, 0],
       [-1, 0, 0],
       [ 0, 0,-1]]
```

with determinant `+1`.

## 4. Slice action, stabilizers, chart orientation

Because slices are vertex-stars,

`R_σ(S_i)=S_{σ(i)}`.

Representative stabilizers:

- `Stab(S_A)≅S3`, order 6;
- `Stab(L_AB)={e,(AB),(CD),(AB)(CD)}≅C2×C2`, order 4;
- `Stab(S_A,L_AB)={e,(CD)}≅C2`, order 2;
- with a chosen cyclic chart orientation, the orientation-preserving chart stabilizer is `<(BCD)>≅C3`.

Choose chart-local representatives satisfying zero-sum:

- `S_A: -L_AB+L_AC+L_AD=0`
- `S_B:  L_AB-L_BC-L_BD=0`
- `S_C: -L_AC+L_BC+L_CD=0`
- `S_D:  L_AD-L_BD+L_CD=0`.

For every carrier rotation and source slice, all three chosen representatives transport with one common sign `ε(σ,i)∈{±1}`. Exact enumeration verifies the cocycle law

`ε(στ,i)=ε(σ,τ(i))ε(τ,i)`.

This sign is chart/readout orientation data only, never a primitive native negative axis.

## 5. Supported move theorem: exact group/groupoid boundary

Let a finite address set `X` carry the permutation `ρ(σ)`. For support `Ω⊆X`, define the naive identity-outside truncation

`M~[Ω,σ](x)=ρ(σ)x` for `x∈Ω`, and `x` otherwise.

### Theorem

`M~[Ω,σ]` is an ambient permutation of `X` iff `ρ(σ)(Ω)=Ω`.

If `Ω` is invariant, the restriction permutes `Ω` and fixes its complement.

If `ρ(σ)(Ω)≠Ω`, choose `y∈ρ(σ)(Ω)\Ω` and `x∈Ω` with `ρ(σ)x=y`. Then the truncation maps both `x` and the outside point `y` to `y`, so it is not injective.

Hence the correct object for a non-invariant support is the transformation-groupoid arrow

`m[Ω,σ]: Ω → ρ(σ)(Ω)`.

Its inverse is

`m[Ω,σ]^{-1}=m[ρ(σ)(Ω),σ^{-1}]`

and composable arrows satisfy the exact action law. Ambient supported moves are precisely isotropy arrows. The checker exhausts all `24×64` `(σ,Ω)` cases on the six slots.

## 6. Conjugation / setup transport

For a legal ambient supported move,

`R_τ M[Ω,σ] R_τ^{-1}
 = M[R_τ(Ω), τστ^{-1}]`.

At groupoid level the same formula holds with source/codomain transported explicitly.

This is the exact carrier analogue of a Rubik setup move: a known local algorithm can be moved to another support by conjugation without confusing support transport with frame relabeling.

## 7. General commutator localization theorem

For finite permutations `A,B`, put

`S_A=supp(A)`, `S_B=supp(B)`, `Δ=S_A∩S_B`

and use `[A,B]=ABA^{-1}B^{-1}`.

Then

`supp([A,B]) ⊆ Δ ∪ A(Δ) ∪ B(Δ)`,

so

`|supp([A,B])| ≤ 3|Δ|`.

Proof: outside the displayed union, a point moved by only one of `A,B` cannot be carried by the inverse of that move into the other support, because that would place the original point in `A(Δ)` or `B(Δ)`; hence the second move fixes the intermediate point and the first move cancels. Points outside both supports are fixed trivially.

The deterministic checker verifies this for all `720^2=518400` pairs in `Sym(6)`.

## 8. Sharp FCC overlap localizer

Define

`U_A=M[S_A,(BCD)]=(AB AC AD)`.

Conjugating the label by `b=(AB)` gives `(ACD)` fixing `B`; define

`U_B=M[S_B,(ACD)]=(AB BC BD)`.

Their supports meet only at `AB`. Exact calculation gives

`[U_A,U_B]=(AB AC BC)`.

Thus two three-slot star turns sharing one slot localize to the three edges of face `ABC`, fixing `AD,BD,CD`.

Moreover

`Δ∪U_A(Δ)∪U_B(Δ)={AB,AC,BC}`,

so the general support bound is sharp here.

Bounded exhaustive search over freely reduced words in
`{U_A^{±1},U_B^{±1}}` finds no nonidentity word of length `<4` supported inside that face; the commutator has length 4. It is locally shortest in this alphabet.

Global conjugation transports this construction to every triangular face of the `K4` atlas.

## 9. Three algorithm classes

### SLICE_TRANSPORT_WORD

`b=(AB)` sends `S_A→S_B`; length 1 is trivially shortest for this pair.

### AXIS_TARGETING_WORD

The edge action of `b` contains `(AC BC)`. Since `Ω={AC,BC}` is invariant,

`M[Ω,b]=(AC BC)`

changes the target carrier slot `AC` with exactly one partner and fixes the other four. A nonidentity permutation cannot have support 1, so support 2 is optimal. Conjugates cover all six target slots.

### OVERLAP_LOCALIZER_WORD

`[U_A,U_B]` is the exact length-4 face localizer above.

These are carrier-slot actions. They do not rewrite the immutable K4 incidence and do not by themselves prove native state-space realizability.

## 10. Word calculus

Use alphabet `{a,a^{-1},b}` with `a^3=e`, `b^2=e`.

Immediate inverse/order reductions are exact. Word equality is decided by exact evaluation in the faithful finite `S4` representation.

A BFS shortlex table gives exactly 24 normal representatives with length distribution

`0:1, 1:3, 2:4, 3:6, 4:6, 5:3, 6:1`.

Hence maximum shortlex length is 6 for this alphabet.

Supported words additionally carry a support/domain trace; support-changing steps remain groupoid arrows and are never silently coerced to whole-domain permutations.

## 11. Native bridge interface and hard boundary

The result exports:

- faithful line-label action `ρ_6:S4→Sym(6)`;
- faithful slice-label action `ρ_4:S4→Sym(4)`;
- exact physical carrier realization `S4≅O_FCC`;
- chart orientation cocycle `ε`;
- support/domain action groupoid;
- exact word evaluation and canonical equality.

At carrier level the actions are faithful.

At native level **no kernel claim is made** because the map

`NATIVE_6D_STATE → FCC_CARRIER_READOUT`

has not been proved injective/equivariant at the needed strength.

Freeze:

`CARRIER_FAITHFULNESS != NATIVE_STATE_IDENTITY`.

Therefore this return does not claim:

- `S4` is the full native P000 rotation group;
- every supported carrier word lifts to native motion;
- chart signs are native negative axes;
- FCC classical linear relations reduce native dimension.

## 12. Regressions

- The accepted C2 whole-block exchange remains a separate exact involution regression, not the full rotation answer.
- HCP first-shell non-central-symmetry remains a guard against deriving six native axes from `12/2`.
- The old A3 partial-support warning is enforced structurally: support/domain transport is explicit, and non-invariant restrictions are groupoid arrows rather than fake global rotations.

## 13. Deterministic checker

Path:

`research_checks/P000_6D_AXIS_MIXING_ROTATION_ALGEBRA_CHECK_20260829.py`

It uses integer/permutation arithmetic only. Local run:

```text
PASS
physical_rotations=24
S4_edge_representation=faithful
generator_orders=a:3,b:2,ab:4
normal_forms=24,max_shortlex_length=6
supported_extension_iff_invariant=exhaustive_24x64
conjugation=exhaustive
commutator_support_lemma=exhaustive_Sym6_pairs
localizer=[U_A,U_B]=(AB AC BC),shortest_local_word_length=4
axis_targeting_min_support=2
chart_orientation_transport=cocycle_verified
typed_regressions=C2,HCP
```

## 14. Disposition

Carrier-level hard target: `SUCCESS`.

Exact strength:

`P000_FCC_SIX_LINE_ROTATION_ALGEBRA_AND_RUBIK_WORD_CALCULUS_EXACTLY_CLASSIFIED / CARRIER_LEVEL`

Unresolved residue:

`NATIVE_TO_FCC_EQUIVARIANT_LIFT_NOT_PROVED`.

Recommended Driver disposition:

`ACCEPT_CARRIER_ALGEBRA_INTERFACE_WITH_NATIVE_BOUNDARY`.

A successor should consume this `S4`/action-groupoid interface and either construct an equivariant native-state lift for selected generators/support arrows or prove the exact extra native orientation/incidence state required. It should not redo `K4/S4`.

Method harvest: `RESULT_ONLY`; no new shared tool family and no external novelty claim.
