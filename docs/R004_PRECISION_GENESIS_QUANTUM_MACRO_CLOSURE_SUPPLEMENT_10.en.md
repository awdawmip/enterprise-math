# R004 precision genesis — Supplement 10: automatic congruence-to-relation module extraction

Status: `PROVED_WIP + EXECUTABLE_CHECKED + PRIOR_ART_SPECIALIZATION + FOUNDATION_FEEDBACK_CANDIDATE`  
Parent: `R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_09.en.md`  
Owner branch: `research/r004-precision-genesis-closure-20260810`

Supplement 09 proved that a declared linear relation matrix can be a sufficient future state. This supplement removes the need to guess that matrix in one important regime.

Starting only from the future-safe kernel itself, the compiler asks whether that kernel is an additive translation congruence. If yes, the opaque partition canonically becomes a finite quotient module, and its prime-exponent shape can be recovered by exact integer torsion counts.

## 1. Translation-congruence gate

Fix

`X=(Z/p^K Z)^d`

and let

`E=ker(Sigma)`

be a future-safe equivalence relation obtained from the declared future signature.

Ask whether

`x E y -> (x+z) E (y+z)`

for every `x,y,z in X`.

If this translation invariance holds, let

`H=[0]_E`.

Then `H` is an additive subgroup and

`x E y iff x-y in H`.

Therefore every `E`-class is a coset of `H`, and the safe state is the quotient group/module

`Q=X/H`.

This is the standard correspondence between group congruences and normal subgroups; in the abelian case every subgroup is normal. R004 does not claim this algebra as new.

The executable gate is fail-closed: if the zero block is not a subgroup or the partition is not exactly the coset partition of that block, the relation-module compiler refuses to assign a quotient exponent profile.

## 2. Exact quotient torsion counts

Assume the congruence gate passes.

For `j=0,...,K`, define

`T_j = #{q in Q : p^j q = 0}`.

Because `Q` is a finite abelian p-group, every `T_j` is an exact power of `p`.

Instead of a real logarithm, define `alpha_j` by repeated exact division:

`T_j=p^(alpha_j)`.

Thus `alpha_j` is an integer exponent already present in the finite state count.

If

`Q ~= direct_sum_i Z/p^(e_i) Z`,

then

`alpha_j = sum_i min(j,e_i)`.

Therefore the first finite differences

`beta_j = alpha_j-alpha_(j-1)`

satisfy

`beta_j = #{i : e_i >= j}`.

Finally, the number of invariant axes with exponent exactly `j` is

`beta_j-beta_(j+1)`.

Hence the complete invariant exponent multiset `(e_i)` is recovered from the finite torsion-count sequence alone.

The structure theorem for finite abelian groups and Smith-normal-form-style decompositions are established prior mathematics; Mathlib documents finite abelian groups as direct sums of prime-power cyclic groups and finite free PID quotients through Smith normal form [SRC-MATHLIB-FINITE-ABELIAN; SRC-MATHLIB-SMITH-NORMAL-FORM].

## 3. R004-COMP-T07 — quotient exponent profile compiler

For a translation-congruence future kernel on `(Z/p^K)^d`, define the compiled **quotient exponent profile** as the descending tuple

`E_Q=(e_1,...,e_r)`

recovered by the torsion-count finite differences above.

This profile is canonical up to the ordinary ordering of invariant factors.

It records more structure than quotient cardinality alone. Two quotients can have the same number of classes but different profiles, for example

`Z/p^3 x Z/p`

versus

`Z/p^2 x Z/p^2`.

Both have `p^4` elements, but the profiles `(3,1)` and `(2,2)` distinguish their future-relevant module shapes.

## 4. Representation exponent mass and codimension

Define

`M_Q=sum_i e_i`.

Then

`|Q|=p^(M_Q)`.

Again this is not a real logarithmic definition: the profile is already an integer prime-exponent decomposition of the exact quotient size.

The ambient state has exponent mass

`M_X=K d`.

Define the generalized representation exponent codimension

`Gamma = Kd-M_Q`.

This extends Supplement 09's full-row-rank matrix formula `Gamma=K(d-r)`.

If every quotient axis has full depth `K`, then `M_Q=Kr` and the two definitions coincide. If the quotient has mixed depths, `Gamma` records the exact p-digit mass removed by the future-safe kernel.

## 5. Examples recovered automatically

The executable compiler recovers, without being told the answer:

- exact `Z/8 x Z/8` state -> profile `(3,3)`;
- quotient after killing one full axis -> `(3)`;
- quotient `Z/8 x Z/2` -> `(3,1)`;
- 3-adic quotient `Z/9 x Z/3` -> `(2,1)`;
- kernel of the rank-two relation matrix from Supplement 09 -> `(2,2)` at cap `K=2`.

The torsion sequences distinguish these shapes even when raw class counts alone are insufficient.

## 6. Noncongruence boundary

The coupled-AND future-safe partitions from Supplement 08 fail the translation-congruence gate.

For the diagonal action language, the partition is

`{{00},{01,10},{11}}`.

For the cross action language, it is

`{{00,11},{01},{10}}`.

Neither is the coset partition of its zero block. Therefore neither can honestly be represented as an additive quotient module.

This gives a strong fail-closed rule:

`future kernel not translation-congruent -> do not force quotient-exponent coordinates`.

Such a kernel must remain in a richer relation/witness representation unless another independently proved structure applies.

## 7. Compiler ladder after Supplement 10

R004 now has the following structured compilation ladder.

### Layer A — axiswise arithmetic

`one p-power axis + arbitrary translations -> p-adic trie compiler`.

### Layer B — full product observation

`product state + componentwise dynamics + arbitrary correlated actions -> product of marginal compilers`.

### Layer C — declared relation factorization

`coupled future factors through a proven linear relation matrix -> relation-rank compiler`.

### Layer D — relation state discovered from the kernel

`future kernel is additive translation congruence -> quotient module -> invariant exponent profile`.

### Layer E — genuinely noncongruent coupling

If none of the preceding gates pass, the compiler must retain a general structured relation/witness state; forcing exponent or quotient coordinates would be unsound.

This is the point where A3/A4 ownership becomes essential.

## 8. Validation

New executable module:

`src/enterprise_math/precision_congruence_relation_compiler.py`

with matching regression coverage.

Independent checks recovered the profiles `(3,3)`, `(3)`, `(3,1)`, and `(2,1)` from coset partitions using only exact subgroup/coset/torsion arithmetic. The coupled-AND partitions correctly fail the congruence gate.

Supplement 09's relation-rank oracle was also strengthened during this continuation: compiler construction may deduplicate equal induced relation actions, but regression now compares compiled tokens against the literal original joint-action future signature. An independent bounded sweep of **1,313** partition cases found no mismatch after this correction.

No Lean status or fresh full-repository CI status is claimed.

## 9. Prior-art and ownership boundary

The following are prior mathematics and are not claimed by R004:

- congruences of groups as cosets of normal subgroups;
- finite abelian group decomposition into prime-power cyclic factors;
- Smith normal form and invariant factors over PIDs;
- torsion subgroup counts as invariants of finite abelian p-groups.

Mathlib's official documentation explicitly exposes finite abelian groups as direct sums of `ZMod(p^e)` components and Smith-normal-form decomposition for finite free modules/submodules over PIDs [SRC-MATHLIB-FINITE-ABELIAN; SRC-MATHLIB-SMITH-NORMAL-FORM].

R004's project-specific addition is architectural and executable: use these established invariants as a middle compiler stage between a generic future-safe partition and A3/A4 relation/witness state.

## 10. Revised frontier

The strongest remaining compiler question is now narrower than before:

> **When a future-safe kernel is not a product kernel and not an additive congruence, what weakest structured relation/witness object can represent it without falling back to an opaque class label?**

Candidate destinations include A3 weighted relation state, A4 witness/correspondence state, or a new verified bridge between them. The answer must be discovered by the appropriate owner/Foundation route; R004 should only provide counterexamples, sufficient special cases and compiler pressure tests.
