# Two-bit nesting and aligned progression: shared-context review

Status: `PASS_SYMBOLIC_REVIEW_NO_SUBSTANTIVE_FINDING`. I read the complete `TWO_BIT_PERIOD_NESTING.md`, SHA-256 `9189f01243aa308f516534337b40e6e2c03a7fcf3f79a7dde179a5689bca1d26`, and independently checked the stated finite-sum identities. This is a shared-context symbolic review, not independent admission. No host numerical test, scientific module import, scientific execution or new literature query was performed.

## Nesting and block stretching

The low-bit product `c_d(x)=v(x)v(x+d)` is already `V`-periodic: translation by `V` flips both factors. Consequently it is `U`-periodic. In the low half-period, the high-bit product has signs `+,-,+,-`, yielding the stated full-period `F=4B_d(U-s)-2B_d(U)` and tail `T=3B_d(U-s)-B_d(U)`. In the high half, its signs reverse with the shifted endpoint `e=s-U`; the full-period and tail formulas in (2) follow. The overlap decomposition has nonnegative complete-period count because `d<L`. At `s=0`, the recorded tail is a whole period and gives exactly `H-q` periods; at `s=U`, both formulas agree. No fictitious empty tail or extra period is inserted.

The prefix formula (4) also checks directly: reducing `x` modulo `V`, the product is `(-1)^eta` until the threshold `V-a` and its negative thereafter. Counting complete `V` blocks and the one residual prefix gives exactly the displayed maximum term. The `a=0` negative interval is empty.

For the independent stretching proof, write `x=Vn+u`. There are `V-t` offsets whose displaced block index is `n+z` and `t` offsets whose index is `n+z+1`. Their permissible block counts are `M-z` and `M-z-1`. The compressed lowest-bit factors contribute `(-1)^z` and `(-1)^(z+1)`, respectively. This proves the subtraction in (5), rather than a sum with a missing parity sign. Its boundary `z=M-1` uses only the explicitly extended empty sum `A_one(M)=0`. It does not authorize a nonempty old-formula call at or beyond `M`.

## Aligned progression closure and multiplicities

When `V` divides `R`, the remainder `t` is constant and the compressed index is `z0+jh`, with `h=R/V`. If `h` is even, the sign is constant. If it is odd, separating even and odd `j` gives two canonical progressions of step `2h`, with opposite fixed signs. The counts and omission of empty parity classes are correct.

For each surviving class, shifting its head by one and using the canonical range below `M` removes at most the final `z=M-1` term. It cannot add a term: the next unshifted point was already outside the interval, so its shifted point is outside too. The shifted contribution carries the original sign `(-1)^c` and the explicit negative coefficient from (5). It must not receive an additional sign reversal merely because its argument is `c+1`.

Two displacement orientations, at most two parity classes, and two single-bit sums per class give at most eight progression sums, hence at most sixteen top-level moment tables. This is not sixteen primitive calls; all recursion, typed coefficient/parity work, cache requests and evidence remain paid. The public old `one_negative` method is a complete two-orientation query and cannot be substituted for one of these individual progressions. A separate typed adapter remains necessary.

At `r=0` the negative-orientation magnitude starts at `R`, excluding zero. At a half-modulus residue the equal heads retain multiplicity two. Entirely empty orientations are discarded before compression. The strict distinct-bit domain implies `g>=2`, `0<=ell<k<g`, and compressed bit index `k-ell>=1`; adjacent bits and `k=g-1` are valid. For `ell=0`, `V=1` forces `t=0` and recovers the lowest-bit lift. Raw normalization stays `4^-g`, because the original pair domain has not changed.

## General-modulus missing interface

Equation (9) is correct. In the low half, the algebraic quantity `B` equals `B_d(U-s)` and its coefficient is `4H-4q-1`. In the high half, the true prefix is `B+mu*C`, and substitution gives coefficient `-4H+4q+3` while leaving the same term `-mu*(2H-2q-1)C`. This is precisely the displayed indicator form of `f`.

Expanding `f*((mu-Q+2mu*q)C+E)` gives the fourteen coefficients in (11). In particular, the nonindicator `C` coefficients are `2mu*H`, `mu*(8H-4)`, and `-8mu`; the indicator coefficients are `mu*(4-8H)`, `16mu*(1-H)`, and `16mu`. The `Q*C` and `E` coefficients have the correct signs. Six `C`, four `D`, and four `E` sums suffice; minimality is not asserted.

The two expressions in (13) follow by substituting `z=d-pQ` into the lower and upper pieces and eliminating `Q*eta` with the difference-of-squares identity. Multiplying by `Q` introduces `Q^2*eta`, which the displayed difference-of-cubes identity removes exactly. Thus `C` has lower-floor total degree at most two, `Q*C` at most three, and `E` at most two, with at most one factor of `d`. Independently eliminating `q^a*delta` introduces coarse-floor degree at most `a+1`. The resulting products therefore fit the sufficient bound `u+alpha+beta<=5`, `u<=1`, `alpha,beta<=3` in (12). Each monomial uses only one offset of each floor, although products of coarse and fine floors remain. The fixed divisions are exact integer identities.

This is a sufficient algebraic moment contract, not a completed recurrence. Separate marginal tables do not supply joint products. Some nested floors can be simplified algebraically, so neither the presence of the current mixed products nor the possible `V/gcd(V,R)` residue split proves impossibility or an exponential lower bound. The note correctly states both limits: that explicit split may be exponential, and a new elimination or descending mixed-moment recurrence remains open. Its fixed-dimensional list alone does not prove polynomial cost. Pure single-floor terms are covered by the existing API only when their degree is within that API's bound.

The proved aligned family preserves chronological external matrices and complete residual contracts by staying within a scalar coefficient identity. No history-dependent native-word change, order/address acquisition, arbitrary Walsh mask, general two-bit implementation, or full Shor/QFT simulator follows without additional work. Those boundaries are accurately stated in the reviewed draft.

Global-Knowledge-Sync: main@b98c6e4 / GLOBAL_KNOWLEDGE_V1
