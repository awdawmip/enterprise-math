# R061 Stage 0 — Native Circle-Cell Admissibility Audit

## Status

`CELL_ADMISSIBILITY_EXACT = false`

`Pi_cell = identity` is **not** validated on the full candidate
scalar-to-native-path formula.

## 1. Conditional local replay

Suppose a start circle cell `C_start` has already been selected and suppose
`X_i,X_j` are interpreted exactly as nearest-center transitions along the two
active positive carrier direction families.

Then every free shuffle word has a well-defined single-cell state sequence:

`C_0 -> C_1 -> ... -> C_(a+b)`.

Each letter moves between nearest centers, hence between overlapping
neighboring circle cells. Under this conditional replay:

- every instantaneous state is one circle cell;
- no transition teleports;
- no simultaneous multi-cell state is introduced;
- the formal relative displacement is `(a,b)`;
- no carrier Euclidean length is used as native length.

Thus the shuffle words are not rejected merely for local step invalidity once
a valid start cell is supplied.

## 2. Why this does not prove Pi_cell=identity

The candidate formula starts from scalar/native origin `O_E=0`, but the
current foundation freezes:

`ORIGIN_IS_TRIPLE_CELL_INTERSECTION`;

`ORIGIN_IS_NOT_CELL_CENTER`;

`ORIGIN_IS_NOT_A_CELL`.

Therefore a word of center-to-center transition generators cannot start at
`O_E`. A type-changing start-incidence choice is required before the first
center transition.

Furthermore, the foundation does not specify the exact map from the three
cells incident to `O_E` to their absolute integer center addresses in each
sector chart. Without that affine anchor, the relative formal count

`(#X,#Y)`

cannot be asserted to equal the absolute endpoint center address used by the
native origin-length law.

So `Pi_cell` is not merely a word-rejection filter. Native realization needs
at least:

1. an origin-incidence/start-cell choice;
2. an affine start-cell/address rule;
3. explicit chart transitions when leaving a local sector;
4. a declared canonical finite path class;
5. completion with third-family realizations if the canonical class requires
   all nearest-center/minimum-jump paths.

## 3. Minimal zero-case counterexample to identity typing

At `N=0`:

`D_0={(0,0)}`;

`Lambda(0,0)={empty word}`.

The formal empty word is well-defined. But there is no native circle-cell
state located at `O_E`: the origin is a coordinate vertex. Therefore
identifying the formal zero word with a native cell trajectory at the origin
violates the frozen object typing.

This already prevents `Pi_cell=identity` on the *full* candidate fiber unless
the zero case receives separate non-cell semantics.

## 4. Third-axis incompleteness is separate

Even after a start cell is supplied, every shuffle word may be locally
admissible while the **fiber** remains incomplete. For `(1,1)`, the full
nearest-center carrier also admits the one-step inverse-third-family
realization `-X_3`, missed by `Lambda(1,1)`.

Thus "each generated word is admissible" does not imply "the generated fiber
is the native path fiber".

## Verdict

`PI_CELL_IDENTITY_FULL_FIBER = false`.

`EXACT_MINIMAL_NATIVE_PROJECTION_DERIVED = false`.

No arbitrary tie-break/filter is introduced. The missing start-incidence and
chart/path-class data are reported to Driver review instead.
