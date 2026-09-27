# A concrete next geometric tool: certified projective elliptic arithmetic

Status: **SYMBOLIC_TOOL_DESIGN / SOURCE_AUDIT / NOT_IMPLEMENTED / NOT_ADMITTED**. No scientific module was imported, no arithmetic fixture or grid was run, and no remote file was written. This is a shared-context research proposal. Its classical content is Montgomery elliptic arithmetic and the ECM factoring mechanism; the proposed addition is an explicit native arithmetic and observer contract, not a new name for ECM or a claim to complete Shor.

## 1. What changing the free trace can and cannot do

For `M_k=[[0,1],[-1,k]]` over an odd prime field, assume `Delta=k^2-4 != 0`. Its eigenvalues are lambda and lambda inverse. In the split case they belong to `F_p^*`, so `M_k^(p-1)=I`. In the nonsplit case Frobenius exchanges them, giving `lambda^p=lambda^-1` and `M_k^(p+1)=I`. Thus varying k changes the split type and the actual divisor occurring as the element order, but every **regular** companion remains in a torus controlled by p-1 or p+1. A new cyclic mark or invertible coordinate system does not change this fact or the complete-return ideal at fixed k,E.

The regularity qualification matters. At k=2, a nonzero nilpotent J with J squared zero gives `M=I+J`, of order p. At k=-2 the corresponding order is 2p. These are the discriminant-zero unipotent cases, not additional regular torus sizes or a genus-one family. An actual gcd of Delta with N must classify a proper setup factor, unit discriminant, or degenerate/saturated setup; scanning k does not make this classification free.

Consequently, a geometric extension intended to change the local group-order mechanism must change the curve/group, rather than only its trace presentation or cyclic mark. This is a scope theorem, not a lower bound for every possible observer of the companion orbit.

## 2. Existing native source: useful pieces and a real gap

The previously read canonical registry at EM `2e81851d62c869a20b47ae083a24dde1a4c0420c`, Git blob `3889506451091ebcfbf7a58cda6517c4af8c3597`, was read from the exact local cached file. Its SHA-256 is `2d12bc746e36ce0e005a17fa8e07d468c2102ce0ec826c1417c580c19f513dde`. T0 provides fixed-weight affine transport and degree-at-most-two moments. T6 supplies operation/observation safety contracts; T7 explicit action/quotient tools; T8 relation-observer composition. None of those descriptions supplies an arbitrary nonlinear curve group law.

The bounded source search for elliptic/genus-1/Montgomery/Weierstrass and their Chinese terms found no matching implementation in the cached registry/source collection and the two exact local source snapshots searched. This is **not** a claim that every current repository file has been searched or that no elliptic code exists anywhere. The concrete interfaces read give the following narrower, usable conclusions:

| Local source and reading scope | Git blob / SHA-256 | Relevant boundary |
| --- | --- | --- |
| `sep26-local-takeover/activity_closeout/src/enterprise_math/brc_residue_port.py`, module contract and residue-layout/packet interfaces | `9b0314b272843431af9f170897c95be608ccef16` / `a15b06ab0f81834f8f9cd49d1090456b45c2c58729558473516038663e474729` | Integer affine fiber maps and fixed conditioned degree-2 observers; arbitrary nonlinear maps are expressly outside its contract. |
| Same source directory, `euler_cayley_spinor.py`, module and normalization/product interfaces | `17155fb6c73ddf9fb8da3e79c9e55f4ea3d0b00b` / `641ded9e39d574b15ab8f7e81e17c3a6adb3c18d5a164ec8fdc3e73225a0ff2f` | Rational/integer spinor normalization divides common content. This is not modular elliptic arithmetic; dividing nonunit content would erase the factor information needed below. |
| Same source directory, `heartbeat_projective_frames.py`, frame/normalization contract | `78e1b765f2355156d9e529835ced7527bb5cd46e` / `6ba7cfa3d6afc49efdc7951bb5be1177d3f497ef006c866657e26f08adb0e018` | Known-prime p-lattice finite congruence frames, not unknown-composite curve points or native fractional Cell moves. |
| `t6-exact-remote-result-audit-4lv27l1h/snapshot/src/enterprise_math/prime_method_inventory.json`, method inventory/targeted entries, not an untruncated full-text read | `3576d5a228e18bd3cf3ce9b248c1df638555cf71` / `509a77fcfa93aed7628d483fda6c60524ffcba01166ab5585fe959c04d76b838` | Existing classical and native prime/factor observers do not certify the proposed genus-one API. |
| Same snapshot, `prime_toolkit.py`, public API names and routing search | `2c1797f084bde6a9d05e538c8bac20e1a054017a` / `13e79a70ea6bf4e1677b4fe3de9a747fa9e90fed9db040f9c2c9801da34f2fa7` | No matched elliptic interface in this bounded audit. No full-body execution claim. |

The actual reusable numerical substrate is the already source-certified typed integer/modular arithmetic and gcd/divisibility receipt chain, plus safe composition and provenance. A quartic homogeneous map requires a new certified register program over that substrate. It is not automatically an affine BRC transport, an X6 automorphism, a closed degree-2 moment update, or a constant-size representation of all paths.

## 3. Minimal curve and point admission, without unknown factors or square roots

Work over `R=Z/NZ`, N odd, with Montgomery equation

`E_(alpha,beta): beta*Y^2*Z = X^3 + alpha*X^2*Z + X*Z^2`.

Require `gcd(2*beta*(alpha^2-4),N)=1`. This ensures smoothness over each residue prime: the affine cubic `f(x)=x(x^2+alpha*x+1)` has distinct roots, beta is a unit, and the point at infinity `[0:1:0]` is nonsingular. These are primewise statements proving the ring interface; factors of N are not required as algorithm input.

A proper setup gcd already certifies a factor. A saturated setup gcd does not admit the curve and is not itself a proper factor. Individual setup expressions may be tested separately at additional cost, or the attempt can end with an explicit degenerate status.

Admit an initial full point by checking its homogeneous curve equation and `gcd(X,Y,Z,N)=1`. One factor-blind affine construction is to choose public alpha and x0, set `beta=f(x0)` and `y0=1`, then perform the same paid setup tests. This makes membership an identity without an inverse or square-root oracle. It supplies no uniform curve distribution, rejection bound, or favorable smooth-order guarantee.

For the x-only representation use `[U:W]`, meaning x=U/W and identifying P with -P. Infinity has x-only representative `[1:0]`; do not confuse it with the full curve triple `[0:1:0]`. A pair is admissible only when `gcd(U,W,N)=1`. In particular, merely being a nonzero pair as ordinary integers is insufficient.

Unit rescalings preserve the pair and its gcd readout. Nonunit rescalings do not. Original integer representatives, modular reduction receipts and any scaling operations must remain explicit. If a pair has nonunit common content, a proper content gcd is a factor; content gcd N is an invalid all-zero residue pair. Neither may be discarded by rational projective normalization and then passed off as a lossless point.

## 4. Two exact homogeneous transitions and their domains

For doubling, propose the literal polynomial program

`D_U=(U^2-W^2)^2`,

`D_W=4*U*W*(U^2+alpha*U*W+W^2)`.

The tangent identity establishing the formula is

`(3x^2+2alpha*x+1)^2 - 4*f(x)*(alpha+2x) = (x^2-1)^2`.

Homogenization gives the displayed map without division by 4 or an alpha24 parameter. It is homogeneous of degree four: rescaling by a unit lambda rescales its output by lambda to the fourth power.

**There is no doubling base point on an admitted regular pair.** This can be proved primewise, not assumed from a numeric test. If U or W is zero over a residue field, D_U is nonzero. Otherwise D_U=0 forces U=+W or -W. The remaining quadratic is then `(2+alpha)W^2` or `(2-alpha)W^2`, both nonzero when `alpha^2-4` is a unit. Thus D_U,D_W cannot both vanish. This preserves admissibility over every component of R. Output validation remains a useful paid implementation check, not an unproved assumption.

For differential addition, take admitted x-only P,Q,D with a certified group relation `D=P-Q` on the same curve. Propose

`S_U=W_D*(U_P*U_Q-W_P*W_Q)^2`,

`S_W=U_D*(U_P*W_Q-W_P*U_Q)^2`.

The corresponding generic affine identity is

`x(P+Q)*x(P-Q) = (x(P)*x(Q)-1)^2/(x(P)-x(Q))^2`.

For a direct polynomial check, put rho=x*u and s=x+u. Subtracting `(alpha+x+u)(u-x)^2` from `f(x)+f(u)` gives `(rho+1)s+2alpha*rho`; its square minus `4*f(x)*f(u)` is `(rho-1)^2(u-x)^2`. The chord formulas for P+Q and P-Q yield the identity. This derivation needs only odd characteristic and the admitted smooth curve, not an ideal numerical propagator.

The differential formula is **not a complete arbitrary addition API**. A triple of valid curve points is not a certificate that D=P-Q. It also has exceptional inputs: P=Q and D=infinity produce the all-zero pair in this displayed formula, so a doubling branch or another certified chart is required. Cross-multiplied identities alone do not turn an all-zero output into a valid point. Over composite N, a chart can fail in only some components; the resulting content gcd may itself reveal a factor, but a globally invalid output must end in a defined failure/repair status.

With input unit scales lambda,mu,nu for P,Q,D, the output scale is `nu*lambda^2*mu^2`; this is still a unit. This is the relevant scaling theorem. Uncontrolled content cancellation is not needed or allowed.

### A useful positive closure: a fixed unit difference makes the ladder chart complete

There is a stronger sufficient domain than a generic differential-addition request. Fix an admitted difference D with **both U_D and W_D units**. Suppose P,Q are certified lifts to the same curve and D=P-Q, with that relation carried by the computation. Then the displayed differential formula has no all-zero residue-prime output.

To prove this, suppose both factors `U_P*U_Q-W_P*W_Q` and `U_P*W_Q-W_P*U_Q` vanish over one residue field. Neither input can be infinity: if W_P=0, admissibility forces U_P nonzero; the second equality then gives W_Q=0, but the first product cannot vanish. Thus both are finite. Their affine x values satisfy x_P=x_Q and x_P*x_Q=1, hence x_P=x_Q=+1 or -1. In odd characteristic, two points at the same x are equal or negatives. Equality gives D=O, contradicting W_D a unit. If Q=-P, D=2P. The doubling numerator is zero at x_P=+1 or -1, while its denominator is nonzero by the regular discriminant; consequently x_D=0, contradicting U_D a unit. This also covers characteristic 3: only oddness and the stated smoothness units were used.

Together with the doubling theorem, this proves an x-only scalar ladder can stay in these polynomial charts for **all** scalar bits, provided its fixed-difference relation and actual curve lifts are established. Starting at `(O,P0)`, the difference is -P0, which has the same x-only coordinates as P0. Both bit updates preserve the adjacent-multiple relation, hence that same fixed x-only difference. No fresh inverse, square root or per-step content gcd is necessary to establish admissibility in this restricted, certified domain. Those gcds may be retained as paid debug checks; they are not a mathematical prerequisite once the complete contract is implemented correctly.

A concrete factor-blind admission satisfying the unit-difference condition chooses x0=2, y0=1 and `beta=10+4*alpha`, then checks the usual smoothness gcd with odd N. The x-only point is `[2:1]`, both coordinates are units. This changes no distribution or success guarantee. It does make the new transition/observer tool obligation narrower and useful: certify one fixed-difference ladder, rather than a complete arbitrary group-addition API. Multiplying both displayed xADD outputs by 4 is an equivalent unit scaling for odd N, not a different geometric operation.

## 5. The factor observer and exactly what its valuation means

After a certified transition and admissibility check, evaluate `d_Z=gcd(W,N)` through the actual typed gcd interface. If `1<d_Z<N`, verify `N=d_Z*h` by an exact division receipt and return the factor. If d_Z=1, there is no infinity hit in any residue-prime component. If d_Z=N with an admissible pair, every component is at infinity; this is a saturated return, not a proper factor.

For a certified scalar chain from P, divisibility of W by a prime p is precisely `[E]P=O` in that residue elliptic curve. Hence a primewise order dividing E at one component and no infinity return at another is a sufficient factor-separation condition. Neither the point order nor a factor is supplied to the algorithm for free.

The gcd keeps the exact prime-power divisibility of **this certified Kummer coordinate W**, invariant under unit scaling. It need not equal a primitive full-elliptic-point return ideal. More precisely, near O use the full curve chart `u=X/Y`, `v=Z/Y`. The curve equation is

`v*(beta-alpha*u^2-u*v)=u^3`.

The parenthesized factor h is a unit near O. The x-only map has regular representation `[U:W]=[h:u^2]`, as is seen from `v/u=u^2/h` on the ordinary finite overlap and then by regular extension. This is not an algorithm that divides a residue tuple by the potentially nonunit u. Its infinity coordinate has twice the valuation of the primitive parameter u, capped by the modulus precision. The quotient by P versus -P is ramified at O; primitive x-only coordinates do not remove that effect. Squarefree prime support is correct, and every proper observed gcd remains a legal factor, but prime-power saturation can hide depth. A primitive-depth observer would require a full-point or other suitable unramified observation interface. This proposal does not silently take square roots of gcds or claim saturation can always be repaired.

Before using d_Z geometrically, admissibility must follow either from the fixed-unit-difference closure certificate above or from an actual common-content check `c=gcd(U,W,N)`. For a general unchecked chart, a proper c is independently a valid factor with its own source label. If c=N, the output is invalid; returning d_Z=N as an elliptic return would be false. Do not normalize away c. The same rule applies to invalid full projective triples.

## 6. Small concrete interface and costs still owed

A successor can implement the following bounded contract; none of these new functions exists merely because this document names it:

1. `admit_curve_point(N,alpha,beta,point)` returns ADMITTED, SETUP_FACTOR, or INVALID/DEGENERATE, with source bindings, full typed smoothness/membership/content evidence and any exact factor division.
2. `projective_double(point_certificate)` evaluates the literal degree-four program, retaining integer/modular operation links and an output pair with the doubling/admissibility proof identifier.
3. `projective_dadd(P,Q,D,relation_certificate)` checks the declared difference relation provenance, evaluates the homogeneous program, and returns ADMITTED, FACTOR_FROM_CONTENT, or EXCEPTIONAL. It never accepts a relation from three coordinate tuples alone.
4. `observe_infinity(point_certificate)` returns NO_HIT, PROPER_FACTOR, or SATURATED with actual gcd and division receipts. A signed/other observation needs a separate contract.

A scalar ladder maintains `R0=[n]P`, `R1=[n+1]P`. A zero exponent bit updates `(2R0,R0+R1)` and a one bit `(R0+R1,2R1)`. With the fixed unit difference, the preceding proof supplies chart closure and the compositional relation certificate for O(log E) intended operations. The native implementation must still verify setup, literal polynomial execution, branch routing and proof/source binding. A caller outside that domain cannot borrow the closure theorem; its exceptional output must remain explicitly classified rather than normalized into a point.

Every executed modular multiplication/reduction, sign-aware addition, setup gcd, content check, final gcd, curve/point generation attempt and rejected chart is charged. The fixed-difference proof can eliminate per-step content checks, but their elimination is an explicit proved optimization, not deletion of an obligation without replacement. Source admission, proof/replay work, retained coordinate/carry information and certificate storage are also charged. Affine field operation counts are not native digit counts. A constant number of active projective registers does not imply constant evidence size or a free nonlinear moment closure. A finite retry wrapper must expose its failure probability or return a resumable/explicit failure status; silently retrying until a favorable curve appears would hide work.

The expected useful change in mechanism is genuine but classical. For a smooth admitted curve over F_p,

`#E(F_p)=p+1+sum_(x in F_p) chi(beta^-1*f(x))`,

because each x has `1+chi(beta^-1*f(x))` possible y values and there is one infinity point. The controlling point order is now a divisor of this elliptic group size, rather than an eigenvalue in the regular companion's p-1/p+1 torus. No point-counting oracle, enumeration of this sum, uniform group-order distribution, or costed smoothness probability is implied. A public exponent schedule only succeeds when the necessary local point-order divisibility and component separation actually hold.

This leaves a precise new tool obligation: provide a native certified nonlinear projective register interface with legal base-locus handling and valuation-aware factor observation. Existing T6/T7 ideas help specify the safe x-only quotient and allowed future language; existing typed arithmetic can supply the primitive receipts. They do not already discharge the curve law, difference-relation or totality proofs. No additional HBW-specific invariant giving a success or complexity advantage was found in this bounded audit. This candidate is therefore **REUSE of classical Montgomery/ECM mathematics, plus an unimplemented native composition/observation interface**, with factor-blind success-rate and total-cost analysis still open. It is not Shor closure.

## Reading and authority provenance

Formula attribution was checked by directly opening the author's Explicit-Formulas Database, [Montgomery x/z formulas](https://www.hyperelliptic.org/EFD/g1p/auto-montgom-xz.html), specifically `dbl-1987-m` and `dadd-1987-m`, and its [Montgomery curve page](https://www.hyperelliptic.org/EFD/g1p/auto-montgom.html). EFD attributes those formula variants to Montgomery's 1987 paper. This review read those web formula sections and the curve definition, not that original paper in full and not an ECM complexity proof. No new professional-provider query was submitted. The domain, scaling, invalid-tuple and observer arguments above are explicit symbolic reasoning; they were not numerical experiments.

Related frozen local proofs: `FREE_TRACE_TORUS_WITNESS.md` SHA-256 `6ad4bbf2db92ffbec7fc57c8da3e16aca9f43a6fb05b89a73aa396aca6f1730c`; `TRACE_SQUARE_VALUATION_LEMMA.md` `35a8259080ccfb7b608eab922a1562c20836e718b9dff09f2af6209937bcb3d5`; `CYCLIC_MARK_INVARIANCE.md` `40ccff0e850bafa9079fc6a4a7a3356b4ed4c106529849e5e03fc543629c882c`.

Global-Knowledge-Sync: main@7a63984 / GLOBAL_KNOWLEDGE_V1.
