# R062 Stage 0 — Component-Labeled Native Relation Model

Researcher-ID: `EM-R062-7C4A91`  
Status: `LABELED_NATIVE_TRANSITION_MODEL_EXACT`

## 1. Typed state

Fix a translated native right sector `S_ij(P)`. Let the sector-local cell state be

`c(P,ij;x,y)`, with `x,y in N_0`.

The state type retains the concrete translated start/context; two parallel translated sectors are not identified merely because their local transition tables are isomorphic.

The unique typed incidence is:

`Sigma_P^(ij) : P -> c(P,ij;0,0)`.

## 2. One-step component relations

Define two distinct one-step relations:

`R_i(c(P,ij;x,y), c(P,ij;x+1,y))`

and

`R_j(c(P,ij;x,y), c(P,ij;x,y+1))`.

Their generator labels are semantic data. In the frozen carrier implementation, each step is verified by exact integer coordinates and no floating-point predicate.

For a word `w = X_{k1}...X_{kn}`, its path operator is the left-to-right relational execution of the corresponding generator relations, matching canonical BRC `runWord`:

`Run(w,A) = relImage(R_kn, ... relImage(R_k1,A) ...)`.

Equivalently, the relation of the complete word is the typed relational composite with the same intermediate cell witness at every multiplication.

## 3. Native trace fiber

For component content `(a,b)`, let `Omega(P,ij;a,b)` be all paths beginning after `Sigma_P^(ij)` whose word contains exactly `a` copies of `X_i` and `b` copies of `X_j`.

The checker reconstructs every prefix trajectory. It verifies:

`|Omega(P,ij;a,b)| = binom(a+b,a)`

for every `a+b <= 12`, all three sectors and seven translated starts, with zero duplicate witness and one common typed terminal for each fixed trace.

The trace identity is the quotient

`T_{P;a,b}^{(ij)} = (P,[X_i^a X_j^b])`

under adjacent component-preserving commutation `X_iX_j ~ X_jX_i`.

## 4. Third-family exclusion is typed, not metric

For local `(1,1)`, the carrier has a nearest-center reverse-third step reaching the same carrier endpoint as `X_iX_j` and `X_jX_i`.

The bridge does **not** exclude that shortcut because it is shorter, longer, or has a different jump count. It is excluded because its one-step label belongs to the third carrier family and therefore is not a word in the declared native component language `{X_i,X_j}` for this trace.

Thus `SAME_CARRIER_ENDPOINT != SAME_NATIVE_LINE_IDENTITY` is preserved by component typing alone.

## 5. No carrier promotion

Carrier integer coordinates are checker/implementation data for exact incidence, translation and endpoint equality. No carrier vector equation is promoted to a native line identity. Native membership is decided by the frozen component trace type.
