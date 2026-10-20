# R063 Stage 3 — Interaction Count Collapse Theorem

Status: `PROVED / EXACT_FINITE_COMBINATORICS`
Researcher-ID: `EM-R063S3-F1CF9D`

Let source path words `p=w_1...w_m` and `q=v_1...v_n` have component counts `(a,b)` and `(c,d)`. Define the interaction rectangle

`I(p,q)={(r,s):1<=r<=m, 1<=s<=n}`

with the unique local table from Stage 3. Retain each cell's row position, column position, source letters and signed output label.

## Exact count collapse

The four source-letter pair types occur exactly

- `X_i x X_i`: `ac` cells, each `+X_i`;
- `X_i x X_j`: `ad` cells, each `+X_j`;
- `X_j x X_i`: `bc` cells, each `+X_j`;
- `X_j x X_j`: `bd` cells, each `-X_i`.

Therefore forgetting row/column order but retaining signed counts gives

`(#(+X_i)-#(-X_i), #(+X_j)-#(-X_j))`

`=(ac-bd, ad+bc)`, exactly the frozen Stage 2 raw root product.

Equivalently encode `+X_i,+X_j,-X_i,-X_j` by `1,J,-1,-J`. For any finite `C4`-labelled interaction process `P`, define

`Eval(P)=sum_x J^(label(x))`.

For Cartesian interaction product `P box Q`, with labels added mod 4,

`Eval(P box Q)=Eval(P) Eval(Q)`

by finite distributivity. No continuum phase, metric, optimization or target-path choice appears.

## Verified domain

The checker exhaustively audited every nonempty binary source word of length at most six: `126` words and `15,876` ordered word pairs, every rectangle having at most `36` cells. Row certificate SHA-256:

`8eb68b77c48a81b27ba764362db5aee20f512cd7f31010edb1bad51f975d47df`.

`INTERACTION_RECTANGLE_COUNT_COLLAPSE_EQUALS_RAW_ROOT_PRODUCT = true`.
