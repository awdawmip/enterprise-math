# R205 — Additive affine-orbit dimension lower bound for independent provenance and complete event tails

Date: 2026-11-16 (Asia/Shanghai). Status: **AUTHOR_PROVED / EXACT_BINARY_WITNESS_CHECKED / NOT_REVIEWED**.

**Frozen scientific input:** \`awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34\`. Dependencies: R195 (field-uniform exact source-order affine minimum), R200 (independent source–direction joint observer), R201 (binary affine upper construction), and R204 (nilpotent suffix argument). This is a scoped observer-quotient theorem, not a change to P000 or the physical BRC carrier.

## Model and result

Let there be \`m>=1\` event directions (the native X6 case has **12 signed directions, not 12 spatial axes**), \`k>=1\` selected provenance labels, and a further neutral label \`⊥\`. Each event is an independently chosen pair \`(direction, provenance)\`, giving an alphabet \`A\` of size \`a=m(k+1)\`. The R200 quotient \`J_{m,k,L}\` retains the selected-source last-occurrence order \`s(w)\` and the final \`L>=1\` **full paired events** \`tail_L(w)\`; its product is chronological concatenation followed by these observation maps.

Let \`d_orbit(q,m,k,L)\` be the minimum dimension of an affine action of this finite quotient over a finite field \`F_q\` with a **single orbit point distinguishing every element** of the quotient. Cross-couplings between source/tail coordinates are unrestricted.

**R205-A (new additive lower bound):**

\`\`\`
d_orbit(q,m,k,L) >= k(k+1)/2 + L*ceil(log_q(2m)).
\`\`\`

Together with the explicit R195 source registers and an R204 nonzero-coded full paired-event suffix shift, there is also the constructive upper bound

\`\`\`
k(k+1)/2 + L*ceil(log_q(2m))
 <= d_orbit(q,m,k,L)
 <= k(k+1)/2 + L*ceil(log_q(m(k+1)+1)).
\`\`\`

For \`q=2,m=12,k=6,L=2\`:

\`\`\`
source-order affine minimum = 21
full paired-event suffix affine upper block = 14
new mandatory source-preserving tail kernel >= 10
31 <= complete joint affine-orbit dimension <= 35.
\`\`\`

The previously separate lower bounds only implied \`max(21,14)=21\`. This proof forces the source-order and a separate nilpotent tail contribution to coexist even with arbitrary affine cross-couplings. It does **not** establish that 31 is attained.

## Proof of R205-A

Let \`rho:J→Aff(F_q^D)\` have an injective orbit map at a point \`p\`. Let \`O={rho(j)p:j∈J}\`; work in the invariant affine span \`W=AffSpan(O)\`, with translation space \`V\` and \`dim V<=D\`. Choose one **neutral-provenance** event \`z=(d_0,⊥)\`, write \`f=rho(z)\` and let \`M\` denote its linear part on \`V\`.

**1. Idempotent source retraction.** Appending \`z^L\` leaves every selected-source order unchanged and sets the final full-event tail to \`z^L\`. Consequently \`E=f^L\` is idempotent on every point of \`O\` and therefore on its affine span \`W\`. Its linear part \`P=M^L\` is a projection. Decompose \`V=U⊕K_0\`, where \`U=im(P)\` and \`K_0=ker(P)\`.

The image \`E(O)\` consists of exactly one point for each selected-source last-occurrence order; these points are distinct because \`rho\` has an injective orbit. On \`E(W)\` define, for every source \`i\`, the affine generator \`G_i=E∘rho((d_0,i))|_{E(W)}\`. Its action on the affine-spanning set \`E(O)\` appends source \`i\` and re-erases the tail. Therefore all source-monoid relations hold as affine-map equalities on \`E(W)\`. The action factors through \`S_k\` and has an injective orbit starting at \`E(p)\`, so is faithful. R195-A, whose proof applies to **all fields**, gives:

\`\`\`
dim U = dim E(W) >= k(k+1)/2.
\`\`\`

This argument does not require the raw generator \`rho((d_0,i))\` to preserve \`U\`.

**2. A source-preserving family of 2m events.** Choose a prefix \`h\` visiting all \`k\` selected sources exactly once, and call the last source \`j\`. There are exactly \`2m\` different event letters \`x\` whose provenance is in \`{⊥,j}\`: every direction with either neutral provenance or the current last source. Every \`hx\` has the same source order \`s(h)\`. Put \`v_x=rho(hx)p\`. The retraction \`E\` sends all \`v_x\` to the same point. Hence the differences \`v_x-v_y\` lie in \`K_0\`.

After appending \`z^{L-1}\`, these histories have the distinct final **complete paired tails** \`xz^{L-1}\`. Their full joint states remain pairwise distinct, so the injective orbit gives \`2m\` distinct points \`f^{L-1}(v_x)\`. Their differences are exactly \`M^{L-1}(v_x-v_y)\`. Since \`P=M^L\`, the invariant subspace \`K_0\` carries the nilpotent operator \`B=M|_{K_0}\` with \`B^L=0\`. Distinct images of the \`2m\` differences force

\`\`\`
q^rank(B^(L-1)) >= 2m,
rank(B^(L-1)) >= ceil(log_q(2m)).
\`\`\`

**3. Nilpotent rank is additive.** If \`B^L=0\` and \`rank(B^(L-1))=r\`, choose \`u_1,...,u_r\` with independent \`B^(L-1)u_i\`. The \`Lr\` vectors \`B^j u_i\` (\`0<=j<L\`) are linearly independent: in any dependence, apply \`B^(L-1-j)\` at the smallest nonzero exponent \`j\`; all later terms vanish, while the remaining top images are independent. Therefore \`dim K_0 >= Lr >= L ceil(log_q(2m))\`.

Adding \`dim U\` and \`dim K_0\` proves the theorem. QED.

## Exact upper construction and representation boundary

The \`k(k+1)/2\` source coordinates are R195's singleton and pairwise 0/1 resets, initialized to ones. Choose \`c=ceil(log_q(a+1))\` and an injection from the \`a\` full paired-event letters into the \`q^c-1\` **nonzero** vectors of \`F_q^c\`; store the final \`L\` codes in shift-and-append registers initialized to zero. The direct sum is affine; the source registers recover the complete selected-source order, while zero padding and nonzero codes recover the complete paired tail, yielding a single separating orbit. This proves the upper bound.

This result is about **affine actions over finite fields** for the R200 *selected observation quotient*. It is not a measured runtime result and does not claim to compress native six-axis paths, physical affine actions, signed branches, weights, multiplicities, or provenance/conditional ports not covered by this quotient. The installed \`enterprise_math.brc_transport.Affine\` uses exact rational coefficients; its F2 representation-class lower bound must not be quoted as a rational-dimensional lower bound.

## Reproducible finite check

Run \`python R205_affine_joint_lower_bound_check.py\`. This pure-standard-library, exact F2 bitwise checker instantiates R201's 35-bit binary source+tail affine orbit for \`m=12,k=6,L=2\`, checks all 24 source-preserving letter witnesses before and after appending a neutral event, verifies they share the same source base but retain 24 distinct full paired tails, and checks two-step nilpotence of the tail subspace with rank seven after one step. See \`R205_verification.json\`. This is a check of the **explicit upper construction and lower-bound witnesses**; it is not an exhaustive search over 31–34-dimensional representations. Universal validity rests on the algebraic proof above.

Native installed-package \`EffectHistogram\` integration remains **NOT_EXECUTED**; independent mathematical review is **NOT_REVIEWED**.

## Next exact open unit

Determine if 31–34 dimensions can achieve the full binary joint observer for \`m=12,k=6,L=2\`, or prove one or more impossible by combining constraints from neutral/source-labeled nilpotent generators. Separately execute the existing R201 native \`enterprise_math.brc_transport\` probe under its pinned package and extend to R203 joint cross-moment transport, with full conversion, composition, storage and bit-complexity accounting.

**Control/evidence scope:** independent portable scientific work; no CLAIM, Result, Review, P000 change, release or deployment claimed.
