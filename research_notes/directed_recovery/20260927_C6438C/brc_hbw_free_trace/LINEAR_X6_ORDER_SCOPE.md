# What a fixed linear HBW macro can change modulo an unknown prime

Status: **PURE_SYMBOLIC_SCOPE_LEMMA / NOT_EXECUTED / NOT_ADMITTED**. Shared author context `EM-DIRECT-C6438C`, activity `RA-CAAAC604CB513AEA8BBC1DFC`. This is finite-field linear algebra used to guide native tool selection. It is not a complexity lower bound for BRC, Shor simulation or factoring.

Let L be an integer-unimodular d-by-d matrix and p an unknown prime dividing the target modulus. Reduction gives an invertible matrix over F_p. Factor its characteristic polynomial over F_p into distinct irreducible factors f_i of degrees d_i, with multiplicities. Let s_i be the largest Jordan-block size associated with f_i over a splitting field, and let e be the smallest nonnegative integer for which p^e is at least every s_i. Then

`ord(L mod p) divides p^e * lcm_i(p^(d_i)-1)`.             (1)

The irreducible factors, p and the local order are proof variables, not algorithm inputs. In particular sum_i d_i is at most d, each s_i is at most d, and when p>d the unipotent multiplier p^e is either 1 or p.

## Proof

Over a finite splitting field, a Jordan block can be written lambda*(I+J), where lambda is a nonzero root of an irreducible f_i and J is nilpotent of index at most s_i. Lambda lies in F_(p^(d_i)), so its multiplicative order divides p^(d_i)-1. In characteristic p,

`(I+J)^(p^e)=I+J^(p^e)=I`

whenever p^e is at least s_i. The scalar and unipotent factors commute, so the block order divides their product. Taking the least common multiple over all blocks gives (1). The claim is independent of the chosen splitting-field basis and therefore holds for the original matrix.

One may phrase the same proof through primary cyclic modules instead of explicitly constructing a Jordan form. Neither construction is needed by an actual native matrix-power algorithm. They establish only a local order restriction.

## Consequence for the native six-coordinate geometry

For a fixed linear macro on X6, the possible semisimple order bounds come from irreducible degree patterns within dimension six. Varying integer coefficients can change the pattern and the actual element order. It does not provide arbitrary local group cardinalities: the matrix remains subject to (1). A finite predetermined composition of linear unimodular arrows is another such matrix.

The degree-two regular companion case sharpens (1) using determinant one: its local order divides p-1 in the split case or p+1 in the nonsplit case. Degenerate repeated-root cases have a separate unipotent factor; they must not be silently included in that regular two-case statement.

This helps distinguish changes of coordinates, changes of matrix elements, and changes of geometric group. Similarity by a certified invertible coordinate transformation preserves the exact order. Moving between free trace parameters can change it, but remains within the conic family. Raising the dimension can reach additional cyclotomic types, with correspondingly larger arithmetic and selection obligations; no success-rate advantage follows from dimension alone.

## What the lemma does not constrain

It does not address every possible BRC computation. State-dependent arrow selection, piecewise-affine carry rules, nonlinear maps, arithmetic circuits, branching observers and changing curve families are outside the iteration of one fixed linear macro. Even an affine update requires a correctly charged homogeneous extension before this particular linear statement is applied. The lemma does not imply that those other operations are free, impossible, or equivalent to a fixed matrix.

It also does not prove that useful matrix orders cannot be found efficiently. A factor algorithm need not explicitly obtain the full matrix order, and a proper coordinate gcd can occur before a complete return. The missing useful-section or exponent selector must be analyzed on its own terms. No general factoring hardness is inferred from a list of local group bounds.

## Next tool obligation

An elliptic or another nonlinear projective family is a substantive change because its local group sizes can vary beyond this fixed conic/matrix order pattern. To use it honestly, the native interface must prove its homogeneous polynomial transitions, preserve coordinate ideals and valuations, handle base loci and nonunit setup, and charge selection and all failed attempts. Existing affine transport does not itself supply that nonlinear closure. A standard elliptic-curve factoring mechanism remains reuse even if implemented with native BRC arithmetic.

The immediate design question is therefore concrete: identify a new lawful geometric transition/observer pair that changes the selection problem, rather than spending a search budget on equivalent linear coordinate frames. The existence of such a useful pair and a general native Shor completion remain open.

Global-Knowledge-Sync: main@8c23cca / GLOBAL_KNOWLEDGE_V1
