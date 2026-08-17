# R059D Stage AH — Proof of the autonomous N Motzkin boundary-word generator

Researcher-ID: `EM-R059D-AH-7B1EFD`

Task: `RS-R059D-STAGE-AH-N-MOTZKIN-WORD-AUTONOMOUS-GROWTH-LAW`

## Theorem

For every integer radius `r>=0`, the canonical first-sector N boundary word `W_N(r)` is generated exactly by the following integer-only recurrence.

For `r=0`, return the empty word. For `r>0`, initialize

`a=r, b=0, rho=-4, H=empty`.

While `a-b>1`:

- if `rho>=0`, append `1` to `H` and update
  `rho <- rho - 3(a+2b+3)`, `b <- b+1`;
- if `rho<0`, append `2` to `H` and update
  `rho <- rho + 3(a-b-3)`, `a <- a-1`, `b <- b+1`.

When the loop stops, let `center=2` iff `a-b=1`, otherwise empty. Let `mirror(H)` mean reverse `H` while mapping `1->3` and `2->2`. Then

`W_N(r)=H + center + mirror(H)`.

The runtime uses only integer arithmetic and comparison and never queries source occupancy, source `Q`, a word table, a jump table, floating point, square root, trigonometry or pi.

## AH-L1 — frozen N support on the left half

Stage AG proves that a first-sector dual vertex `(a,b)` is selected by N exactly when

`3(a^2+ab+b^2)-3 max(a,b)+1 <= 3r^2`.

On the left half `a>=b`, write

`L(a,b)=3(a^2+ab+b^2)-3a+1`.

Then selection is `L(a,b)<=3r^2`.

For fixed `a`,

`L(a,b+1)-L(a,b)=3(a+2b+1)>0`.

Hence the selected vertices in every left-half column form an initial interval in `b`.

If `a-b>=2`, then

`L(a-1,b+1)-L(a,b)=3(b-a+2)<=0`.

Therefore every selected left-half point with `a-b>=2` has its diagonal successor `(a-1,b+1)` selected.

These two facts make the canonical outer boundary greedy and unique: from a current selected boundary vertex `(a,b)` with `a-b>1`, take the vertical step `(0,1)` exactly when `(a,b+1)` is selected; otherwise the vertical candidate is outside and the selected diagonal `(-1,1)` is the unique next outer-boundary step.

Thus the left-half boundary alphabet is exactly `{1,2}`.

## AH-L2 — residual invariant and exact decision law

Define the slack of the next vertical candidate by

`rho = 3r^2 - L(a,b+1)`.

At the initial state `(a,b)=(r,0)`,

`L(r,1)=3r^2+4`,

so `rho=-4`, independent of `r`.

The boundary decision is therefore exactly:

`rho>=0 <=> (a,b+1) is selected <=> emit 1`.

If `rho<0`, emit `2` by AH-L1.

The residual can be updated without evaluating `L` again.

After a `1` step, the new vertical candidate is `(a,b+2)` and

`L(a,b+2)-L(a,b+1)=3(a+2b+3)`,

so

`rho' = rho - 3(a+2b+3)`.

After a `2` step, the new state is `(a-1,b+1)` and its next vertical candidate is `(a-1,b+2)`. Direct subtraction gives

`L(a-1,b+2)-L(a,b+1)=3(b-a+3)`,

hence

`rho' = rho + 3(a-b-3)`.

This proves the stated integer recurrence and proves that the runtime recurrence is exactly equivalent to the frozen N boundary semantics while containing no per-cell support oracle.

## AH-L3 — termination and center rule

Let `d=a-b`. A symbol `1` reduces `d` by one; a symbol `2` reduces `d` by two. Therefore the left recurrence terminates after finitely many steps with `d in {0,1}`.

If `d=0`, the path reaches the reflection axis and no central edge is needed.

If `d=1`, the unique edge crossing the reflection axis is the diagonal symbol `2`; it is fixed by reflection-plus-reversal, so it is the unique center symbol.

## AH-L4 — reflection closes the word

The frozen N support predicate is invariant under `(a,b)<->(b,a)`. Reflection maps the oriented first-sector path to the same boundary traversed in the opposite direction. Under reflection followed by traversal reversal,

- symbol `1=(0,1)` maps to `3=(-1,0)`;
- symbol `2=(-1,1)` maps to itself;
- symbol `3=(-1,0)` maps to `1=(0,1)`.

Therefore the right half is exactly `mirror(H)`, proving

`W_N(r)=H+center+mirror(H)`

for every `r`.

This proves the all-radius word theorem.

## AH-L5 — Motzkin and AG count compatibility

With AF height `h=a+b-r`, the left half uses only symbols `1` and `2`, so height is nondecreasing and never negative. The center `2` preserves height. The reflected half reverses the rises as `3` descents, so the path returns to height zero and remains nonnegative.

Because the generated word is exactly the canonical N word, the accepted AG theorem applies:

`#1=#3=J_N(r)=floor(alpha*r+1/3)`,

`#2=r-J_N(r)`,

`|W_N(r)|=r+J_N(r)`.

The AH generator does not need to evaluate this floor law at runtime; the equality is a theorem-level compatibility statement.

## AH-L6 — AF B functional and count readouts

Read the generated word from `(r,0)` and maintain AF height `h`. Immediately before every `a`-decreasing step (`2` or `3`), add the current `h` to `B`. This is exactly the AF functional because the generated word equals the frozen canonical word.

Hence

`D=2r+1`,

`C=6r+6J`,

`V=1+3r(r+1)+6B`.

The full N count chain is therefore autonomous once `W` is emitted.

## AH-L7 — D6 full-boundary closure

Let `R(a,b)=(-b,a+b)`. The generated sector path begins at `(r,0)` and ends at `(0,r)=R(r,0)`. For `k=0..5`, rotate the sector path by `R^k` and concatenate the six copies, deleting duplicated sector-start vertices at joins.

Each rotated copy lies in one closed adjacent-axis sector. Their interiors are disjoint and adjacent copies meet only at the frozen axis endpoint. Since `R^6=id`, the sixth copy returns to `(r,0)`. Local adjacency is preserved by `R`.

Thus the D6 completion is one closed D6-compatible boundary cycle/state with exactly

`6|W| = 6r+6J = C`

boundary edges.

## AH-L8 — state size and minimality boundary

The auxiliary runtime state is a constant number of integers `(a,b,rho)` plus the output prefix being emitted. It stores no two-dimensional occupancy geometry.

No claim of true information-theoretic minimality is made. AF's binding lower bound remains: scalar `J` alone is insufficient to determine `B` or the word. The correct AH status is therefore

`CONSTANT_SIZE_SUFFICIENT_AUXILIARY_STATE_PROVED__MINIMALITY_OPEN`.

## Conclusion

All theorem gates for the N word close:

- word autonomy: proved;
- all-radius equivalence: proved;
- AG counts: proved compatible;
- AF B functional: proved compatible;
- D/C/V readouts: closed;
- D6 closure: proved;
- runtime source/occupancy lookup: absent.

Primary disposition:

`FULL_N_MOTZKIN_WORD_FORWARD_GENERATOR_PROVED`.
