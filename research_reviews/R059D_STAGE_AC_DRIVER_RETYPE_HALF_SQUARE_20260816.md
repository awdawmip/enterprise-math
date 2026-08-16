# R059D Stage AC — Driver semantic retype after half-square correction

Date: `2026-08-16`
Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`
Status: `DRIVER_RETYPE_FROZEN`

User correction:

- the canonical triangle `T_n=((0,0,0),(n,0,0),(0,-n,0))` is an **Enterprise half-square**, not an Enterprise square;
- its reflection about the `v` axis forms the complete **Enterprise square**.

Stage AC branch artifacts remain immutable. Their exact combinatorial counts are retained but retyped:

1. `3n` is the typed three-side adjacency-incidence / boundary readout. It is not the native 2D area.
2. `n(n+1)/2` counts one orientation of unit `T_1` triangles.
3. The opposite orientation contributes `n(n-1)/2` unit triangles.
4. Therefore the total unit-triangle cell count inside `T_n` is exactly

   `n(n+1)/2 + n(n-1)/2 = n^2`.

5. The reflected half contributes another `n^2`, so the complete symmetric Enterprise square contains `2n^2` unit half-square cells.
6. Normalize the complete `n=1` symmetric square (two unit triangles) as one Enterprise square-area unit. Then the complete `n` square has area

   `ENTERPRISE_SQUARE_AREA(n)=n^2`.

Thus the geometric square agrees exactly with algebraic self-multiplication:

`ENTERPRISE_SQUARE(n)=n*n`.

Its inverse on the square domain is

`ENTERPRISE_ROOT(n^2)=n` for `n>=0`.

The single triangle is retained as `ENTERPRISE_HALF_SQUARE`; its normalized area is one half of the complete square, while integer-first implementations may store its raw unit-half-square count `n^2` instead of introducing `1/2` into the primitive cell count.

Disposition for old Stage AC semantics:

`COUNTS_VALID__AREA_AND_ROOT_INTERPRETATION_SUPERSEDED`

Do not merge the old claims `A_n=3n` as a 2D area law or `R_n=n(n+1)/2` as an Enterprise root law into current definitions. Preserve them only as their exact retyped combinatorial counts.