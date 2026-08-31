# P000 six-axis P11 collision locus and conditional selector return

Status: `SUCCESS / EXACT_COLLISION_LOCUS_WITH_ONE_BIT_CONDITIONAL_SELECTOR / DERIVED-ONLY / DRIVER_REVIEW_PENDING`

- Task: `RS-P000-SIX-AXIS-P11-COLLISION-LOCUS-CONDITIONAL-SELECTOR`
- Publication: `TP2-3DEA87F0F4ED366BEE03`
- Researcher: `EM-P000P11C1-4A91D2`
- Claim: `chatgpt-p000p11c1-20260831-1255-4a91d2`
- Execution record: `ER-4A91D2C7F08E3B5619AA`
- Result: `RR-C3E71A9D4B6052F88E21`
- Parent accepted Result: `RR-B96585874709743F94BC`
- Taskbook: `research_tasks/P000_SIX_AXIS_P11_COLLISION_LOCUS_CONDITIONAL_SELECTOR_20260831.md` / `sha1:179c541b37f7853ba1ac1d871a86ec9108dfaa77`

Hard target:
`P000_P11_COLLISION_LOCUS_AND_CONDITIONAL_SELECTOR_EXACTLY_CLASSIFIED_OR_FROZEN_RESOLVENT_GRAMMAR_INSUFFICIENT`.

Terminal disposition:
`EXACT_COLLISION_LOCUS_WITH_ONE_BIT_CONDITIONAL_SELECTOR`.

## 1. Main theorem

Let the already-known derived marginals be

`H={h0,h1,h2}`, `T={t0,t1,t2}`

and for an alignment `sigma in S3` define

`P11(sigma)=sum_i h_i t_{sigma(i)}`,
`P21(sigma)=sum_i h_i^2 t_{sigma(i)}`,
`P12(sigma)=sum_i h_i t_{sigma(i)}^2`.

Alignments are identified exactly when they give the same multiset
`K=multiset{(h_i,t_{sigma(i)})}`, i.e. the same `K/Gamma` state under the already-frozen `Gamma=C2 wr S3` quotient.

The exact classification is:

1. If either marginal has a repeated value, `P11` is injective on the distinct `K/Gamma` alignment orbits. Hence every valid `P11` fibre has size one.
2. If both marginals are distinct, sort them increasingly and put

   `A=h1-h0>0`, `B=h2-h1>0`,
   `C=t1-t0>0`, `D=t2-t1>0`.

   Then the only possible two-orbit `P11` collisions are

   - `C1`: assignments `132` and `213`, exactly when `A*C=B*D`;
   - `C2`: assignments `231` and `312`, exactly when `A*D=B*C`.

   No transposition-relative pair can collide.
3. Both equations hold simultaneously iff `A=B` and `C=D`. In that arithmetic-progression case there are two different doubled `P11` levels, not one triple level. Their separation is exactly `2*A*C>0` after the harmless translation normalization below.
4. Consequently every `P11` fibre has cardinality `1` or `2`, and the collision flag itself is computable from the already-known `H,T,P11` packet.
5. On every two-orbit fibre there is a symmetric quadratic resolvent whose two roots are exactly the two candidate `P21` values; dually there is a symmetric quadratic resolvent whose roots are exactly the two candidate `P12` values.
6. Therefore the minimum additional lossless information is exactly one conditional bit on the collision locus and zero bits off it. No second full integer moment needs to be carried on the generic one-orbit locus.

This theorem is entirely inside the frozen derived arithmetic facade. It does not infer a native orientation, a Pfaffian negative slot, a native six-axis signed carrier, factorization, dimension reduction, or Full-Cell dynamics.

## 2. Repeated-marginal strata are collision-free

Suppose first

`H={h,h,k}`, `k!=h`.

Modulo exchange of the two equal `h` slots, an alignment orbit is determined only by the value `t_* in distinct(T)` placed on the `k` slot. Then

`P11 = h*sum(T) + (k-h)*t_*`.

Since `k-h!=0`, distinct admissible values of `t_*` give distinct `P11`. Thus there is no two-orbit collision. Triple `H` gives only one orbit.

Dually, if

`T={t,t,u}`, `u!=t`,

an orbit is determined by the `h_*` placed on the unique `u` slot and

`P11 = t*sum(H) + (u-t)*h_*`,

which is again injective. Triple `T` is unique.

Hence a two-orbit fibre is possible only on the fully distinct `H` and fully distinct `T` stratum.

## 3. Exact distinct-stratum collision equations

Equality of two assignment values is unchanged if a constant is subtracted from every `h_i` and/or every `t_j`, because the induced change in `P11` is assignment-independent. Thus for comparing the six values we may normalize

`H=(0,A,A+B)`, `T=(0,C,C+D)`

with positive gaps `A,B,C,D`.

For the six assignments of the sorted `T` values, the reduced `P11` table is

| assignment | reduced `P11` |
|---|---:|
| `123` | `2AC+AD+BC+BD` |
| `132` | `2AC+AD+BC` |
| `213` | `AC+AD+BC+BD` |
| `231` | `AC+AD` |
| `312` | `AC+BC` |
| `321` | `AC` |

The maximum `123` and minimum `321` are strict. The cross comparisons among the remaining four are also strict except

`P11(132)-P11(213)=AC-BD`,

and

`P11(231)-P11(312)=AD-BC`.

Therefore the full collision locus is exactly the union

`C1: AC=BD`  equivalently `A/B=D/C`,

`C2: AD=BC`  equivalently `A/B=C/D`.

These are precisely the two 3-cycle relative-permutation collision classes. A transposition changes only two slots and would require a factor `(h_i-h_j)(t_r-t_s)=0`, impossible on the distinct stratum.

If both `C1` and `C2` hold, positivity gives

`A/B=D/C=C/D`,

so `A=B` and `C=D`. The two doubled levels are then `4AC` and `2AC` in the normalized table. Thus even the maximally symmetric distinct-gap control has two disjoint double fibres, never a three-state fibre.

This proves the exact necessary-and-sufficient collision criterion and the global bound `|fibre(P11)|<=2` without an empirical extrapolation.

## 4. Symmetric quadratic resolvent for `P21`

Assume we are on the distinct stratum. Define the Vandermonde moment matrix

`V_H = [[1,1,1],[h0,h1,h2],[h0^2,h1^2,h2^2]]`

and its symmetric Gram matrix

`G_H = V_H V_H^T`,

so, with `r_k=sum_i h_i^k`,

`G_H = [[3,r1,r2],[r1,r2,r3],[r2,r3,r4]]`.

Its determinant is the squared Vandermonde

`Delta_H = det(G_H) = prod_{i<j}(h_i-h_j)^2 > 0`.

For an aligned product vector `t=(t_{sigma(0)},t_{sigma(1)},t_{sigma(2)})^T`, put

`S_T=sum(T)`, `p=P11`, `X=P21`.

Then

`m_X=[S_T,p,X]^T = V_H t`.

Hence

`t^T t = m_X^T G_H^{-1} m_X`.

But the left-hand side depends only on the known marginal `T`:

`t^T t = sum_j t_j^2 = S_T^2-2 e2(T)`.

Multiplying by `Delta_H` gives the frozen symmetric quadratic

`Q21(X) = m_X^T adj(G_H) m_X - Delta_H * sum_j t_j^2`.

Every alignment with the prescribed `H,T,p` must satisfy `Q21(X)=0`. Its leading coefficient is

`adj(G_H)_{33} = 3 sum_i h_i^2 - (sum_i h_i)^2`

`= sum_{i<j}(h_i-h_j)^2 > 0`,

so it is genuinely quadratic.

On a two-orbit `P11` fibre, the two `P21` values are distinct (proved directly in Section 6). Therefore these two actual values exhaust the two roots of `Q21`. No third candidate or hidden higher-degree branch remains.

Equivalently, after choosing a root `X`, the aligned `t_i` are reconstructed by the accepted Vandermonde formula

`t_i = [X-(h_j+h_k)p+h_j h_k S_T] / [(h_i-h_j)(h_i-h_k)]`.

Thus each root deterministically recovers one of the two candidate `K/Gamma` packets.

The coefficients of `Q21` use only symmetric power sums of `H`, symmetric data of `T`, and the already-known `P11`; no outcome-dependent higher mixed moment has been introduced.

## 5. Dual quadratic resolvent for `P12`

Swap the roles of `H` and `T`. Let

`V_T = [[1,1,1],[t0,t1,t2],[t0^2,t1^2,t2^2]]`,
`G_T=V_T V_T^T`,
`Delta_T=prod_{i<j}(t_i-t_j)^2`.

For `Y=P12`, set

`m_Y=[S_H,p,Y]^T`, `S_H=sum(H)`.

Because `m_Y=V_T h` for the aligned `h` vector,

`h^T h = m_Y^T G_T^{-1}m_Y = sum_i h_i^2`.

Therefore

`Q12(Y) = m_Y^T adj(G_T)m_Y - Delta_T * sum_i h_i^2`

is a genuine quadratic with leading coefficient

`3 sum_i t_i^2-(sum_i t_i)^2 = sum_{i<j}(t_i-t_j)^2>0`.

On a two-orbit fibre its two roots are exactly the two candidate `P12` values, and the dual Vandermonde formula reconstructs the corresponding packet.

So both parent sufficient second moments admit a degree-two elimination precisely matching the residual fibre cardinality.

## 6. `P21` and `P12` encode the same bit on `C1` and opposite bits on `C2`

The dual branch relation is not globally constant; it is exactly stratum-dependent.

Use the normalized positive gaps from Section 3.

### Class `C1`: `AC=BD`

For the colliding pair `132` versus `213`, direct subtraction and the collision equation give

`P21(132)-P21(213) = -A*C*(A+B) < 0`,

`P12(132)-P12(213) = -A*C*(C+D) < 0`.

Hence the lower `P21` root and the lower `P12` root describe the same `K/Gamma` packet. The two numeric root orderings encode the **same** binary residue.

### Class `C2`: `AD=BC`

For the colliding pair `231` versus `312`,

`P21(231)-P21(312) = -B*C*(A+B) < 0`,

while

`P12(231)-P12(312) = +C*D*(A+B) > 0`.

Thus the lower `P21` root corresponds to the upper `P12` root. The two root orderings encode **opposite** residues.

When both collision equations hold, the actual `P11` value identifies which of the two disjoint doubled levels is present, so there is no ambiguity: apply the `C1` same-bit rule on the upper doubled level and the `C2` opposite-bit rule on the lower doubled level.

## 7. Exact conditional selector and information cost

The selector can be defined without carrying a redundant collision flag.

Given valid `H,T,P11`:

1. sort the two marginals and compute the distinct `K/Gamma` candidate alignments consistent with `P11` using the exact criterion above;
2. if the fibre has size one, return the unique packet and carry **no branch bit**;
3. if the fibre has size two, form `Q21`, order its two integer roots increasingly as `X_-<X_+`, reconstruct the two packets by the Vandermonde formula, and carry one bit:
   - bit `0`: select `X_-`;
   - bit `1`: select `X_+`.

The receiver already knows `H,T,P11`, so it can determine whether the fibre size is one or two. No separate collision indicator is required.

Thus the exact minimum side-information cardinality is

`|selector alphabet| = |fibre(H,T,P11)|`,

and the exact fixed-instance information cost is

`log2 |fibre| = 0 bits` off the collision locus,

`log2 |fibre| = 1 bit` on the collision locus.

Worst-case extra information is exactly one bit.

This is an information statement, not an arbitrary integer encoding trick. The parent packets `{P11,P21}` and `{P11,P12}` carry an entire second integer everywhere. The present theorem says that, once `H,T,P11` are already retained, their **alignment-disambiguating content** is only one conditional binary choice on the exceptional locus. Computing the resolvent can still involve integers of the original magnitude; no computational-bit-complexity claim is being substituted for the information theorem.

## 8. Integer-pairable collision families and exact minimal witnesses

Pairability remains the frozen gate

`h^2-4t=d^2>=0`, `d congruent h (mod 2)`.

For exact witness minimality, use the parent local-root metric

`R_B={(a+b,ab): a<=b, |a|,|b|<=B}`

and ask for the least `B` for which both packets in a positive collision class are entirely pairable in `R_B`.

The task-local exact checker scans the nested boxes `B=1,...,6` and obtains

`C1 counts = [0,0,0,0,0,1]`,

`C2 counts = [0,0,0,0,0,1]`.

So `B=6` is exact minimal root sup-norm for both classes in this frozen metric, and each class has a unique `(H,T)` witness at that first box.

### Minimal `C1` witness

`H={-1,1,4}`, `T={-30,-12,0}`.

Here `A=2,B=3,C=18,D=12`, so `AC=BD=36`.

The colliding packets are

`132: {(-1,-30),(1,0),(4,-12)}`

with local roots

`{-6,5}, {0,1}, {-2,6}`

and

`(P11,P21,P12)=(-18,-222,-324)`;

and

`213: {(-1,-12),(1,-30),(4,0)}`

with local roots

`{-4,3}, {-5,6}, {0,4}`

and

`(P11,P21,P12)=(-18,-42,756)`.

### Minimal `C2` witness

`H={-4,-1,1}`, `T={-30,-12,0}`.

Here `A=3,B=2,C=18,D=12`, so `AD=BC=36`.

The colliding packets are

`231: {(-4,-12),(-1,0),(1,-30)}`

with local roots

`{-6,2}, {-1,0}, {-5,6}`

and

`(P11,P21,P12)=(18,-222,324)`;

and

`312: {(-4,0),(-1,-30),(1,-12)}`

with local roots

`{-4,0}, {-6,5}, {-3,4}`

and

`(P11,P21,P12)=(18,-42,-756)`.

### Infinite pairable families

Each minimal witness generates an infinite exact family. For every integer `m>=1`, replace every local root pair `{a,b}` by `{ma,mb}`. Then

`h -> m h`, `t -> m^2 t`,

so pairability is automatic and

`P11 -> m^3 P11`,
`P21 -> m^4 P21`,
`P12 -> m^5 P12`.

Both gap equations are homogeneous of degree three under this scaling, so the corresponding `C1` or `C2` collision persists for every `m`. This gives explicit parametrized integer-pairable collision families in both positive classes.

## 9. Three-state adversarial controls

There is no three-state `P11` fibre.

The symbolic table already proves this: the only equality-capable pairs are the disjoint `C1` pair `{132,213}` and `C2` pair `{231,312}`. The strict maximum `123` and strict minimum `321` never collide, and all remaining cross comparisons have a strictly positive gap.

The strongest algebraic attempt is to impose both collision equations. That forces

`H=(h0,h0+A,h0+2A)`,
`T=(t0,t0+C,t0+2C)`

with `A,C>0`. But then the two double levels remain separated by `2AC`, so the fibre pattern is exactly

`1,1,2,2`,

not `1,1,1,3` or anything larger.

As a deterministic regression, the checker exhausts every sorted three-multiset `H,T` from `[-3,3]`, including every repeated stratum, and obtains maximum fibre `2`. The pairable subset is therefore also bounded by two. This finite census is only a regression guard; the all-domain proof is the positive-gap table above.

## 10. Prior-mathematics boundary and P000 firewalls

The reusable ingredients are classical:

- rearrangement/assignment geometry for the six `S3` matchings;
- Vandermonde interpolation;
- Gram matrices and moment elimination;
- symmetric-polynomial and finite-group invariant theory;
- multisymmetric/polarized power sums, as already documented in the parent result (Vaccarino; Rydh).

No historical novelty claim is made for those ingredients. The task-specific contribution is only the exact specialization to the frozen `H,T,P11` interface with the integer-pairability gate, the two explicit collision equations, the two-root `P21/P12` resolvents, and the conditional one-bit information law.

Preserve all firewalls:

`DERIVED_SIX_COORDINATE_ARITHMETIC_FACADE_ONLY`.

`NO_NATIVE_ORIENTATION`.

`NO_PFAFFIAN_NEGATIVE_SLOT_SELECTION`.

`NO_NATIVE_DIMENSION_REDUCTION`.

`NO_FACTORIZATION_OR_FULL_CELL_PROMOTION`.

Recovering `K/Gamma` plus a collision branch still does not choose the parent's oriented scalar

`Q=S_T-2*t_negative_slot`.

The selector is `Gamma`-invariant alignment information only.

## 11. Exact checker and frozen control boundary

Task-local checker:

`research_checks/P000_SIX_AXIS_P11_COLLISION_LOCUS_CONDITIONAL_SELECTOR_CHECK_20260831.py`.

Certificate:

`research_artifacts/P000_SIX_AXIS_P11_COLLISION_LOCUS_CONDITIONAL_SELECTOR/certificate_20260831.json`.

Deterministic run:

`PASS P000_P11_COLLISION_LOCUS_CONDITIONAL_SELECTOR checks=23620 collision=7056 resolvent=16036 branch=320 scale=144 double_controls=64 rootbox=C1:0,0,0,0,0,1|C2:0,0,0,0,0,1 fibre_max=2 selector_bits=0_or_1`.

Freeze:

`P11_TWO_ORBIT_LOCUS = C1 UNION C2` on the distinct marginal stratum.

`C1: AC=BD / SAME_P21_P12_ROOT_BIT`.

`C2: AD=BC / OPPOSITE_P21_P12_ROOT_BIT`.

`REPEATED_MARGINAL_STRATA_COLLISION_FREE = TRUE`.

`P21_QUADRATIC_RESOLVENT_EXISTS = TRUE`.

`P12_QUADRATIC_RESOLVENT_EXISTS = TRUE`.

`MINIMUM_CONDITIONAL_SELECTOR_BITS = 0_OFF_LOCUS / 1_ON_LOCUS`.

`THREE_STATE_P11_FIBRE = IMPOSSIBLE`.

`ORIENTATION_FIREWALL_PRESERVED = TRUE`.

This is a new immutable Researcher Result for Driver review. The researcher lane makes no downstream publication or promotion decision.
