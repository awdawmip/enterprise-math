# CBRC F1 — Ablation and Countermodel Packet

Status: `PHASE-A REQUIRED ABLATIONS`

Date: `2026-08-22`

Researcher-ID: `EM-CBRCF1-8D27A4`

Task-ID: `RS-CBRC-F1-NONSIGN-RECOALESCENCE-CARRIER-FORWARD-CLASSIFICATION`

Primary carrier under full F1 constraints:

`C_min = Z e ⊕ <tau | 3tau=0>`

with

`R(e)=e+tau`,
`R(tau)=tau`.

Primary verdict:

`F1_UNIQUE_MINIMAL_NONSIGN_CARRIER`.

## 1. Baseline theorem dependencies

The primary classification uses:

- conservative embedding of the old signed layer;
- refinement-compatible forgetful retraction;
- additive reversibility;
- non-sign elementary orbit size `>2`;
- finite-orbit requirement;
- branch-role relabeling covariance;
- orientation reversal;
- path-composition compatibility;
- rank-primary minimality.

The explicit dark-cancellation clause is audited separately and proved redundant once the old signed group embeds and transport is additive.

No torsion-free axiom is used.

---

## 2. Ablation A1 — remove finite-orbit requirement

### Removed condition

The elementary occurrence is no longer required to have a finite orbit.

### Countermodel

Take the torsion-free rank-two additive carrier

`C=Z^2`

and the additive automorphism

`U = [[1,1],[0,1]]`.

Choose the old elementary occurrence

`e=(0,1)`.

Then

`U^k e=(k,1)`.

These are all distinct for `k>=0`.

Thus:

- transport is additive and reversible;
- it is not `±id`;
- the elementary orbit is infinite.

### Effect

The finite local transport alphabet is no longer forced.

The characteristic finite-order classification disappears.

Under the original rank-primary order the torsion rank-one minimum still remains an admissible lower-rank model, so this ablation does not by itself create a smaller carrier. What it destroys is the theorem that every admissible F1 transport belongs to a finite local orbit family.

### Load-bearing conclusion

`FINITE_ORBIT -> FINITE_LOCAL_TRANSPORT_ALPHABET`.

Without it:

`INFINITE_ORDER_TRANSPORT_ADMISSIBLE`.

---

## 3. Ablation A2 — remove conservative F0 embedding

### Removed condition

Do not require an injective copy of the old signed `Z` coefficient layer.

### Countermodel

Take the finite additive carrier

`C=(Z/2)^2`.

Define

`R(a,b)=(b,a+b)` mod `2`.

Then

`(1,0) -> (0,1) -> (1,1) -> (1,0)`.

So `R` has an elementary orbit of size `3`.

The torsion-free rank is `0`.

### Failure relative to F1

No injective homomorphism

`Z -> (Z/2)^2`

exists.

Therefore the old signed layer is lost.

### Effect

The minimum additive rank drops from `1` to `0`.

This proves conservative embedding is load-bearing for the statement that the first non-sign carrier is an extension of F0 rather than a replacement of it.

### Load-bearing conclusion

`CONSERVATIVE_F0_EMBEDDING -> RANK >= 1`.

---

## 4. Ablation A3 — remove exact dark-cancellation preservation

### Removed condition

Delete the explicit statement that the embedded additive inverse must remain available.

### Result

No change.

### Proof

If

`i:Z -> C`

is an additive group embedding, then

`i(-1)=-i(1)`.

Hence

`i(1)+i(-1)=0`.

For additive automorphism `R`,

`R(i(1))+R(i(-1))=R(0)=0`.

So exact signed dark cancellation is already implied by:

- conservative group embedding;
- additive transport.

### Classification

The explicit dark-preservation clause is redundant and can be removed without widening the admissible family.

### Load-bearing conclusion

None independently.

Freeze:

`EXACT_DARK_PRESERVATION_CLAUSE_REDUNDANT = true`.

---

## 5. Ablation A4 — remove branch relabeling covariance

### Removed condition

Serialization/name swap of the two `(1,1)` paths need not preserve the physical transport class.

### Baseline equivalence

With covariance, the two raw presentations

`R_+(e)=e+tau`

and

`R_-(e)=e-tau`

are identified by

`S(tau)=-tau`.

### After ablation

There is no reason to identify `R_+` and `R_-`.

They become two distinct oriented/presentation-labeled models on the same additive carrier.

Further path-specific naming choices can remain as physical-looking parameters even though they originate only from serialization.

### Effect

Strict uniqueness of the transport class is lost.

The carrier remains the same.

### Load-bearing conclusion

`BRANCH_RELABELING_COVARIANCE -> GENERATOR_SIGN_CHOICE_IS_GAUGE`.

---

## 6. Ablation A5 — remove orientation-reversal compatibility

### Removed condition

No native reversal operation is required to transport `R` to `R^{-1}`.

### Baseline

The unique involution fixing `e` and reversing the minimal transport is

`S(e)=e`,
`S(tau)=-tau`.

It satisfies

`SRS^{-1}=R^{-1}`.

### After ablation

`S` is no longer forced.

An oriented model may select `R` without supplying any equivalence to `R^{-1}`.

### Effect

The derived two-orientation comparison structure disappears.

This does not change the additive carrier, but it changes the physical equivalence relation on transport presentations.

### Load-bearing conclusion

`ORIENTATION_REVERSAL -> {R,R^{-1}} IS ONE UNORIENTED CLASS`.

---

## 7. Ablation A6 — remove composition compatibility

### Removed condition

Path transport need not be functorial under typed concatenation.

### Countermodel

Assign:

`T(X_i)=id`,
`T(X_j)=id`,

but declare independently

`T(X_i X_j)=R`.

Then

`T(X_i X_j) != T(X_j)T(X_i)`.

This is reversible path-by-path but does not compose.

The same defect can be inserted at any depth.

### Effect

Depth-three associativity and depth-four diamond consistency cease to be forced.

Edge data no longer determine path transport.

### Load-bearing conclusion

`COMPOSITION_COMPATIBILITY -> PATH TRANSPORT IS OPERATOR FUNCTOR`.

---

## 8. Ablation A7 — torsion-free requirement

### Status

`NOT USED`.

The primary F1 classification does not assume torsion-free coefficients.

Therefore there is no "remove torsion-free" ablation to run.

### Opposite control: add torsion-free

Adding the new axiom

`tors(C)=0`

kills the primary rank-one torsion carrier.

Rank one then reduces to `Z`, whose automorphisms are only `±1`.

The minimum free rank becomes `2`.

For a primitive orbit-generated rank-two carrier, finite order `>2` yields exactly the three integral companion families with traces

`-1,0,1`

and orders

`3,4,6`.

Thus the common rank-two answer is a **counterfactual extra-axiom route**, not the issued F1 result.

Freeze:

`TORSION_FREE_IS_NOT_AN_F1_PREMISE`.

---

## 9. Ablation A8 — remove minimal-rank requirement

### Removed condition

Do not minimize additive rank.

### Countermodel family

From the primary minimum form

`C_min`

construct

`C' = C_min ⊕ Z f`

with

`R'(c,nf)=(R(c),nf)`.

The old signed layer still embeds.

The elementary old occurrence still has orbit size `3`.

All reversal and sign operations extend trivially on `f`.

One may add arbitrarily many inert free or finite summands.

### Effect

Infinitely many larger carriers satisfy the operational conditions.

Uniqueness is lost immediately.

### Load-bearing conclusion

`MINIMAL_RANK -> EXCLUDES INERT ENLARGEMENTS`.

---

## 10. Extra ablation — remove refinement-compatible retraction

This is included because the proof makes the refinement/forgetting operation explicit.

### Removed condition

Keep only an injective map

`i:Z->C`

and do not require a retraction

`pi:C->Z`.

### Countermodel shape

Take a rank-one free group generated by `f` and embed the old generator non-primitively:

`i(1)=d f`

for `d>1`.

The embedding is injective but there is no additive retraction sending `d f` back to `1`.

### Effect

There is no canonical additive forgetting of the enrichment back to the exact F0 coefficient.

Nonprimitive embeddings and finite quotient artifacts enter the classification.

### Load-bearing conclusion

`REFINEMENT-COMPATIBLE RETRACTION -> OLD SIGNED LAYER IS A DIRECT SUMMAND`.

The primary minimum satisfies the stronger split condition, so admitting only weak injections is unnecessary for F1.

---

## 11. Torsion candidate stress test

The taskbook explicitly requires torsion to be admitted or killed.

### Candidate

`C_min = Z e ⊕ <tau | 3tau=0>`.

### Conservative embedding

`i(n)=ne` is injective.

### Forgetful retraction

`pi(ne+a tau)=ne`.

### Transport

`R(ne+a tau)=ne+(a+n)tau`.

### Check 1 — old coefficient unchanged after forgetting

`pi R = pi`.

PASS.

### Check 2 — refinement addition

For coefficients `c_j`,

`R(sum c_j)=sum R(c_j)`.

PASS.

### Check 3 — old integer relations unchanged

If

`n e = m e`

in `C_min`, then `n=m`.

PASS.

### Check 4 — new torsion does not kill old multiplicity

`3tau=0`

does not imply

`3e=0`.

PASS.

### Check 5 — exact sign dark

`e+(-e)=0`.

PASS.

### Verdict

`TORSION_CANDIDATE_ADMITTED`.

No issued F1 axiom kills it.

---

## 12. Multiplication countermodels

F1-Q5 asks whether path composition forces coefficient multiplication.

### Baseline

No multiplication is required: path concatenation composes additive transport operators.

### If multiplication is imposed

Exactly two associative bilinear `R`-multiplicative products extend `e*e=e`.

#### Product L

`e*e=e`,
`e*tau=tau`,
`tau*e=0`,
`tau*tau=0`.

#### Product R

`e*e=e`,
`e*tau=0`,
`tau*e=tau`,
`tau*tau=0`.

They are opposite handed versions.

Reversal `S` exchanges them anti-isomorphically.

### No unital survivor

A two-sided unit would require both

`e*tau=tau`

and

`tau*e=tau`.

No `R`-multiplicative associative product satisfies both.

### Effect

Internal multiplication is underdetermined if nonunitality is allowed and impossible if old `e` is required to remain a two-sided unit.

Therefore multiplication cannot be part of the unique minimal F1 carrier.

---

## 13. Checker-backed finite cases

The deterministic checker validates:

- `Aut(Z)` no-go;
- every normal-form automorphism for cyclic kernel sizes `2` and `3`;
- zero non-sign survivor for size `2`;
- two raw orbit-three parameterizations for size `3`;
- one equivalence class under `tau -> -tau`;
- the additional size-three orbit-six raw family, correctly dominated by orbit size;
- reversal uniqueness;
- all transport exponent compositions through depth `4`;
- all `81` edge-exponent assignments around one commuting diamond;
- all `27` bilinear product parameter triples;
- the two multiplication survivors and zero unital survivor;
- all mandatory ablation countermodels.

Checker deterministic digest:

`d3e570e05b76fc4f6d3269ac5fd58f9f833ce537f9121403b09f9c7fad132080`.

Mismatch count:

`0`.

---

## 14. Ablation verdict table

| Condition | Remove it | Primary consequence |
|---|---|---|
| finite orbit | yes | infinite-order transport admitted |
| conservative embedding | yes | rank-zero finite carrier admitted; F0 lost |
| explicit dark preservation | yes | no change; redundant |
| branch relabeling covariance | yes | `R` and `R^-1` split into presentation classes |
| orientation reversal | yes | `S` not forced |
| composition | yes | nonfunctorial path assignments admitted |
| torsion-free | N/A | not an F1 premise |
| minimal rank | yes | infinitely many inert enlargements admitted |
| refinement-compatible retraction | extra | nonprimitive embeddings and no exact F0 forgetting |

Freeze:

`F1_ABLATION_PACKET_COMPLETE = true`.
