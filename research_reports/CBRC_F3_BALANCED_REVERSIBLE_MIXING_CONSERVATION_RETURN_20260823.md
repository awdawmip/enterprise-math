# CBRC F3 — Balanced Reversible Mixing and Scalar Conservation Return

Researcher-ID: `EM-CBRC-F3-7B31A9`

Task: `RS-CBRC-F3-BALANCED-REVERSIBLE-MIXING-CONSERVATION-FORWARD-CLASSIFICATION`

Owner branch: `research/cbrc-f3-balanced-reversible-mixing-conservation-forward-classification`

Taskbook source commit: `bbdc0ad66c5bde1c712f2fbd80308929cd6159e6`

Blind mathematical input source commit: `19ed5cfdba021cf67be0f059d8e26be1fb5af3b2`

Blind input blob SHA: `82cf1607f6ad87080dba68cd0a12aa8d31dd1882`

Primary verdict:

`F3_CURRENT_CARRIER_BALANCED_MIXING_FAMILY`

Hard target:

`BALANCED_REVERSIBLE_MIXING_SCALAR_CONSERVATION_MINIMAL_EXTENSION_CLASSIFIED`

## 1. Executive result

The accepted current carrier already supports genuine balanced reversible branch mixing. No carrier enlargement is required.

The decisive point is that literal representative commutation with marker swap is too strong: if the free block of a two-slot automorphism commutes with marker swap, its integer determinant condition forces a signed monomial matrix, and exact positive balanced splitting of the elementary coefficient is then impossible. Marker-choice independence must therefore be implemented at the level of the physical operation class, i.e. by closure under marker conjugation, not by requiring one representative to satisfy `MP=PM`.

An exact current-carrier survivor is obtained with

`C1 = Z e ⊕ <tau | 3 tau = 0>`

and the two-slot additive automorphism

`M((n1,a1),(n2,a2)) = ((2 n1 + 3 n2, a1), (3 n1 + 4 n2, a2))`.

Its free matrix is

`A = [[2,3],[3,4]]`, `det(A)=-1`,

so it is reversible with

`A^{-1}=[[-4,3],[3,-2]]`.

The elementary input splits as

`M(e,0) = (2e,3e)`.

A full nonnegative scalar family conserved by this same `M` is

`q_delta(n,a) = f(n) + delta * 1_{3|n and a != 0}`, `delta >= 0`,

where `f` is the six-periodic even function

- `f(0 mod 6)=0`,
- `f(±1 mod 6)=1`,
- `f(±2 mod 6)=1/2`,
- `f(3 mod 6)=1/2`.

Hence

`q_delta(2e)=q_delta(3e)=1/2`

and exact marked conservation gives

`Q(M(e,0)) = 1/2+1/2 = 1 = Q(e,0)`.

The parameter `delta` is not selected by M1–M9. `delta=0` and `delta=1` are inequivalent exact countermodels on the same carrier and the same mixing law. Therefore scalar conservation does not select a unique quantitative law, homogeneous degree, polarization, or positive form.

## 2. Q1 — complete additive-automorphism structure on the current carrier

Let `T=(Z/3)^2` be the torsion subgroup of `C1⊕C1`. It is characteristic. The quotient by `T` is `Z^2`. Since there is no nonzero homomorphism from finite torsion into `Z^2`, every additive endomorphism has the unique block form

`(n,t) -> (A n, B (n mod 3) + D t)`

with

- `A in M_2(Z)`,
- `B in M_2(F3)`,
- `D in M_2(F3)`.

It is an automorphism iff

- `A in GL_2(Z)`, equivalently `det A = ±1`, and
- `D in GL_2(F3)`.

Thus every two-slot additive automorphism is exactly a triple

`(A,B,D) in GL_2(Z) × M_2(F3) × GL_2(F3)`.

For each free block `A`, there are exactly `3^4=81` cross blocks `B` and `|GL_2(F3)|=(3^2-1)(3^2-3)=48` torsion blocks `D`, hence `3888` torsion/cross lifts.

Marker relabeling acts by conjugation:

`(A,B,D) ~ (PAP, PBP, PDP)`.

This conjugacy-orbit statement is the part actually forced by naming independence. Equality of representatives is not forced.

### 2.1 Literal commuting is an exact no-go

If a free block commutes with marker swap `P`, then

`A=[[u,v],[v,u]]`.

The unimodularity condition is

`u^2-v^2=±1`,

so

`(u-v)(u+v)=±1`.

Over integers this forces either `v=0, u=±1` or `u=0, v=±1`. Therefore the free block is a signed monomial matrix.

For an elementary input `(e,0)`, a signed monomial free block leaves exactly one output branch with free coefficient `±1`; the other has free coefficient zero. The first output is in the accepted `R,J,S` orbit of `e`, so M1–M2 force its scalar to be `1`. Exact conservation then forces the other branch scalar to be `0`, contradicting M5 strict positive two-branch balance.

Therefore:

`MP=PM` cannot be imposed on any genuine current-carrier balanced survivor.

This is why M4 must be a class-level covariance/conjugacy condition rather than representative commutation.

### 2.2 Torsion-assisted mixing alone is insufficient

More generally, if the first column of `A` has a zero entry, primitivity of a column of `GL_2(Z)` forces the other entry to be `±1`. The same scalar argument gives one branch scalar `1` and the other `0`. Thus no amount of free-to-torsion cross coupling `B` can turn a free-monomial split into a positive balanced split.

Hence any genuine current-carrier survivor must mix the torsion-free rank-one contents of the two slots nontrivially. Torsion may decorate a survivor, but cannot by itself produce M5+M6.

Deliverable:

`CURRENT_OBSERVABLE_CARRIER_BALANCED_MIXING_CAPABILITY_CLASSIFIED = CURRENT_CARRIER_SUPPORTS_NONTRIVIAL_FREE_PART_MIXING; PURE_TORSION_ASSISTANCE_NO_GO`.

## 3. Exact current-carrier survivor

Choose

`A=[[2,3],[3,4]]`, `B=0`, `D=I`.

Then `det A=-1`, so `M` is an additive bijection. It is not independent per-slot transport, a global sign, or marker swap.

The elementary split is

`M(e,0)=(2e,3e)`.

Both outputs are nonzero.

### 3.1 Exact marker-choice relation

The accepted operations `J` and `S` imply the unary scalar-invariant free-sign map

`K=J S`, `K(n,a)=(-n,a)`.

Let

`K_L=diag(id,K)`, `K_R=diag(K,id)`

on the two marked slots. Direct integer calculation gives

`P A P = [[4,3],[3,2]] = diag(1,-1) A^{-1} diag(-1,1)`.

Therefore on the full carrier

`P M P = K_L M^{-1} K_R`.

So swapping marker names does not require the same matrix representative. It produces an exactly equivalent inverse-oriented representative up to already accepted absolute transports. This is target-independent and derives only from the admitted operations.

This establishes M4 for the physical mixing class.

## 4. Q2/Q4 — exact scalar-conservation family for the canonical survivor

### 4.1 Accepted transport orbits

M2 implies:

- `q(-n,a)=q(n,a)` because `J S` flips the free sign while fixing torsion;
- if `n` is not divisible by `3`, `R` cycles all torsion labels, so `q(n,a)` is independent of `a`;
- if `3|n`, `R` is torsion-trivial and `S` identifies `a=1` with `a=2`.

Thus the only possible torsion sensitivity occurs on free coefficients divisible by `3`.

### 4.2 Free restriction is forced to period six for this `M`

Write `f(n)=q(n,0)`. Because the free-sign map on the first slot is an isometry, conservation under `M` is equivalent to conservation under

`U = diag(-1,1) A = [[-2,-3],[3,4]]`.

For `(x,y)` with `s=x+y`,

`U(x,y)=(x-3s, y+3s)`.

Hence

`f(x-3s)+f(y+3s)=f(x)+f(y)`.

Taking `s=1`, i.e. `y=1-x`, shows that

`E_1(x)=f(x)+f(1-x)`

is `3`-periodic. Equivalently,

`f(x+3)+f(x+2)=f(x)+f(x-1)`.

With evenness, `f(0)=0`, and `f(1)=1`, this recurrence forces

`f(0)=0`, `f(1)=1`, `f(2)=t`, `f(3)=1-t`, `f(4)=t`, `f(5)=1`, `f(6)=0`,

and then repeats with period `6`.

The full two-variable conservation equation is satisfied for every real `t` by this six-periodic family; exact residue enumeration on `(Z/6)^2` verifies sufficiency. Nonnegativity requires `0<=t<=1`.

M5 balance of the split `(2e,3e)` forces

`t=1-t`, hence `t=1/2`.

Thus the free restriction is uniquely selected within this mixing representative, but the full torsion-sensitive law is not.

### 4.3 Full torsion-sensitive family

Because

`A mod 3 = diag(-1,1)`,

whether the first free output is divisible by `3` is exactly whether the first free input is divisible by `3`, and similarly for the second slot. With `D=I`, the indicator

`1_{3|n and a!=0}`

is conserved slotwise.

The full solution of the resulting finite orbit/conservation system is therefore

`q_delta(n,a)=f(n)+delta*1_{3|n and a!=0}`, `delta>=0`,

with the balanced `f` above.

This is not only a pair of examples: it is the complete nonnegative scalar family for the canonical `(A,B=0,D=I)` representative after M1, M2, M5 and M6 are imposed.

Two inequivalent exact countermodels are:

- `delta=0`: pure torsion has marked scalar `0`;
- `delta=1`: pure torsion has marked scalar `1`.

Both conserve exactly under `M` and `M^{-1}` and both split `e` as `1/2+1/2`.

For `delta=0`, because `q` ignores torsion entirely, every one of the `3888` torsion/cross lifts `(B,D)` over the same free `A` preserves `q`. For `delta=1`, exact finite enumeration leaves `36` lifts, including `B=0,D=I`.

Thus the current carrier supports a large mixing family, not a unique operation.

Deliverables:

`CURRENT_CARRIER_MARKED_SCALAR_CONSERVATION_CLASSIFIED = NONUNIQUE_EXACT_FAMILY`.

`BALANCED_MIXING_SCALAR_LAW_CLASSIFIED = UNDERDETERMINED_AFTER_CONSERVATION`.

### 4.4 What is not forced

No homogeneous degree is forced. In the exact survivor,

`q(e)=1`, `q(2e)=1/2`, `q(3e)=1/2`, `q(6e)=0`.

So neither positive homogeneity nor strict positivity on all nonzero coefficients follows.

No positive form is forced because the nonzero coefficient `6e` can have scalar `0`.

No bilinear or polarization object is forced: `delta` remains free and the scalar is periodic/orbit-valued rather than generated by an additive bilinear law.

The blind-input torsion-sensitive relative readout remains compatible in two separate senses:

1. the unmarked recoalescence discriminator is a separate object and the carrier is unchanged;
2. if a torsion-sensitive marked scalar is desired, any `delta>0` provides one, while `delta=0` keeps pure torsion dark at the marked level.

Conservation selects neither choice.

## 5. Q3 — carrier enlargement

Not triggered.

Under any conservative extension order in which the old carrier must embed/retract before added rank, generators, relations, torsion changes, or extra ordered coefficient structure are counted, the least successful carrier is already `C1` itself.

Therefore:

`MINIMAL_BALANCED_MIXING_CARRIER_EXTENSION_CLASSIFIED = NO_EXTENSION_REQUIRED; CURRENT_CARRIER_IS_LEAST`.

No torsion removal, torsion-free rank increase, new coefficient generator, coefficient multiplication, or divisible scalar coefficient domain is required for existence.

## 6. M7 — composition/refinement consistency

The selected `M` is a global additive automorphism of `C1⊕C1`, so all integer powers and the inverse are defined exactly. The checker verifies conservation and exact inverse recovery through depth four.

For more markers, use the canonical direct-sum extension `M_ij` that acts as `M` on the selected pair and identity on the other slots.

- operations on disjoint pairs commute;
- `M_ij^{-1} M_ij=id` exactly;
- a temporary refinement tree followed by the declared inverses in reverse order returns the exact prior marked state;
- associativity of finite direct sum removes parenthesization as bookkeeping;
- overlapping, noninverse operations on different pairs may fail to commute, but then they represent different operation sequences rather than marker-name ambiguity.

No new primitive three-slot or four-slot operation is required for the F3 local law.

## 7. M8 — sign-dark and relative non-sign compatibility

The carrier is not changed, so exact signed cancellation remains:

`e+Je=0`.

The blind-input relative discriminator also remains:

`e+JRe=-tau !=0`.

Since the selected `M` is bijective, it does not quotient or identify `tau` with zero. Therefore the accepted relative non-sign discriminator is preserved.

## 8. Q5 — smallest exact recoalescence discriminator after mixing

Use the two marked relative presentations

`v0=(e,Je)`

and

`v1=(e,JRe)`.

Their branch scalar data are identical for every `delta>=0`:

`(q(e),q(Je))=(1,1)=(q(e),q(JRe))`,

so both have marked total `Q=2`.

Apply the same derived F3 mixing representative:

`M(v0)=((-e),(-e))`,

`M(v1)=((-e),(-e-tau))`.

Again the branch scalar data are `(1,1)` and the marked total remains `2` in both cases.

After marker erasure and additive same-terminal recoalescence,

`Agg(M(v0))=-2e`,

`Agg(M(v1))=-2e-tau`.

The two unmarked aggregate classes differ by `-tau` while all marked scalar data agree.

Therefore:

`BALANCED_MIXING_RELATIVE_RECOALESCENCE_DISCRIMINATOR = EXACT_TWO_PATH_SURVIVOR`.

No continuum fit or external target law is used.

## 9. Q6 — coefficient multiplication / algebra boundary

Composition of the selected mixing operator yields the exact relation

`M^2 - 6 M - I = 0`

as an additive endomorphism of `C1⊕C1`.

On the free block this is the direct integer identity

`A^2 = 6A + I`,

since

`A^2=[[13,18],[18,25]]`.

On the torsion block `M=I`, so the same polynomial evaluates to `-6I=0` because the torsion exponent is `3`.

This is an operator relation on the marked two-slot module. It does **not** force any internal coefficient multiplication on `C1`. Addition plus composition of endomorphisms is sufficient to state and use the relation.

Multiple internal coefficient-algebra choices could be added without changing the F3 observable data, so no unique coefficient multiplication is selected.

Therefore:

`BALANCED_MIXING_COEFFICIENT_ALGEBRA_BOUNDARY_CLASSIFIED = OPERATOR_POLYNOMIAL_DERIVED; INTERNAL_COEFFICIENT_MULTIPLICATION_NOT_FORCED`.

## 10. Mandatory ablations — summary

Detailed countermodels are in `research_reports/CBRC_F3_ABLATION_AND_COUNTERMODEL_PACKET_20260823.md`.

- Remove M3 reversibility: a lower-complexity nonbijective balanced conserving map exists with free matrix `[[2,3],[3,2]]`, determinant `-5`.
- Remove M4 branch-choice independence: the exact conserving free scalar family retains the asymmetry parameter `t`; e.g. `t=1/4` gives split scalars `1/4` and `3/4`.
- Remove M5 balanced two-nonzero condition: signed-monomial and torsion-assisted degenerate cases re-enter.
- Remove M6 conservation: arbitrary accepted-orbit labels can make the elementary split look balanced while failing on other states; an exact countermodel is supplied.
- Remove M7: no enlargement of the canonical global-automorphism witness; M7 is automatically satisfied by direct-sum local extension and mainly excludes partial/ambiguous one-shot laws.
- Remove M8: no effect on current-carrier existence because an automorphism cannot kill the existing torsion discriminator; it remains a protection against destructive extensions.
- Remove M9: no new mathematical model once M6 is formalized with one fixed `q`; M9 is an explicit anti-rescaling guard preventing semantic reinterpretation.
- Remove strict positivity on split outputs: no effect under the derived strong balance `q(a)=q(b)` plus M6, because each split scalar is forced to `1/2`. Global strict positivity is nevertheless not forced.
- Remove minimal-extension requirement: no effect here because the current carrier already succeeds.
- Allow arbitrary orbit labels with no M6: the scalar family becomes vastly underdetermined and elementary balance ceases to constrain behavior away from the split.

## 11. Deterministic checker

Required checker:

`scripts/cbrc_f3_validate_balanced_mixing_forward.py`

Deterministic digest:

`aa2b1736c163362b9dbd179d09e85183ab5a46c335db316f46754c95ec37d3a8`

Checker coverage includes:

- exact `C1` operations and accepted `R,J,S` relations;
- `48` torsion automorphisms and `81` cross blocks per free block;
- exact selected `A`, inverse and marker-swap relation;
- exhaustive scalar conservation on the full finite quotient `(Z/6 × Z/3)^2` for multiple `delta` values;
- exact inverse recovery;
- composition through depth four;
- balanced elementary split;
- torsion-lift census (`3888` survivors at `delta=0`, `36` at `delta=1`);
- exact two-path recoalescence discriminator;
- mandatory ablation countermodels;
- derived operator polynomial;
- zero theorem/enumeration mismatches.

Finite enumeration is used only after the infinite-domain recurrence has reduced the scalar law to a six-periodic quotient, so the scalar classification is not inferred from an arbitrary finite window.

## 12. Unresolved assumptions / boundary of the classification

1. `Balanced` is taken in the operationally strong sense demanded by M4+M5: after quotienting marker names, the two elementary output branches are physically exchangeable, hence their local scalar values must be equal. M4 alone does not imply equality.
2. The full infinite set of possible free matrices `A in GL_2(Z)` admitting some pathological nonnegative conserved scalar is naturally an infinite feasibility family. F3 does not need to select a unique `A` because one exact current-carrier family already decides the carrier-extension question negatively. The automorphism group itself is classified exactly, and the canonical survivor family is classified exactly.
3. Global strict positivity `z!=0 => q(z)>0` is not part of the accepted requirements and is false for the canonical exact family. Whether adding that stronger axiom leaves some other current-carrier survivor is a separate strengthened problem, not needed for the present hard target.
4. The scalar `q` is a marked-slot scalar only. No identification with the unmarked aggregate readout is made.

## 13. Secondary tags

`CURRENT_CARRIER_VIABILITY = YES`

`CARRIER_EXTENSION = NONE`

`MIXING_LAW = NONTRIVIAL_ADDITIVE_AUTOMORPHISM_FAMILY`

`MARKER_RELABELING = CONJUGACY_CLASS; LITERAL_COMMUTATION_NO_GO`

`SCALAR_LAW = EXACT_NONUNIQUE_FAMILY`

`RECOALESCENCE_DISCRIMINATOR = SURVIVES`

`MULTIPLICATION_BOUNDARY = INTERNAL_MULTIPLICATION_NOT_FORCED`

`ABLATIONS = COMPLETE`

`TARGET_LEAK_AUDIT = PASS`

## 14. Final verdict

`BALANCED_REVERSIBLE_MIXING_SCALAR_CONSERVATION_MINIMAL_EXTENSION_CLASSIFIED`

with primary verdict

`F3_CURRENT_CARRIER_BALANCED_MIXING_FAMILY`.
