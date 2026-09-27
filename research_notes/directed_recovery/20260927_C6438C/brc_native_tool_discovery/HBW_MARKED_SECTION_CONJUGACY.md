# HBW marked-section conjugacy: repairing the factor observer

Status: PURE_SYMBOLIC_AND_SOURCE_AUDIT / SHARED_CONTEXT / NOT_EXECUTED / NOT_ADMITTED. This is a COMPOSE domain interface using existing integer-X6 transport, exact BRC histograms and typed modular/gcd readouts. The companion recurrence, conjugacy and inversion symmetry are standard algebra, not new classical theorems under new names. No scientific module import, host numerical experiment, external provider query or remote write was performed for this note.

## 1. Finding

The two-coordinate companion carrier can preserve the **original** factor observer `gcd(u-1,N)` over arbitrary composite N, including prime powers. Replace the saturated trace observer `gcd(z-2,N)` by an explicitly marked affine-section readout. On the regular setup branch the new readout needs no division by the discriminant difference and no inverse reconstruction at each state.

The construction also has a direct integer formula for conjugated inversion. Therefore the original symmetric square schedule, its microscopic branch multiplicities, and its first-hit factor/depth histograms transfer to this representation. Neither the state dimension nor the reachable support is compressed by this conjugacy. Computational advantage requires a charged implementation comparison.

## 2. Setup, ring and integer types

Fix `N >= 2` and a certified unit a in `R = Z/NZ`. Pay for a certified inverse b with `ab = 1` in R. Choose integer representatives a,b and put

```
delta = a-b,       k = a+b,
P = [[1, 1],      D = [[a, 0],      M = [[ 0, 1],
     [a, b]],          [0, b]],          [-1, k]].
```

The integer matrix M is unimodular, with

`M^-1 = [[k,-1],[1,0]]`.

There is an important type distinction:

`MP - PD = (ab-1) [[0,0],[1,1]]`                            (1)

as an integer identity. Consequently `PD = MP` in R, but generally not on the unreduced integer lattice. Also `det(P)=-delta`. A unit determinant modulo N makes P invertible over R; it does not make P unimodular over Z or a lossless native Cell basis change.

Compute the positive gcd `g0 = gcd(delta,N)` using the actual typed arithmetic route:

* `g0=1`: the regular conjugacy branch of this note applies.
* `1<g0<N`: setup already supplies a proper factor, with its own typed divisibility receipt. An algorithm may stop with a distinctly labeled SETUP_FACTOR event. This changes the original first-hit law; it must not be reported as a law-preserving conjugacy run.
* `g0=N`: `a=b` in R, hence `a^2=1`. P is singular and the marked observer below vanishes on its image. Use the original certified unit/pair route or a separately charged at-most-two-state treatment of the powers of a. There is no general promise of a proper factor in this branch. In the binary-power schedule every exponent `2^j` with `j>=1` gives the identity multiplier.

These cases include `delta=0`, N=2, and even N. No division by two or field assumption occurs. For even N, the inverse of an odd unit is odd, so the regular branch cannot occur; the gcd branches above remain valid. Unit admission for a is a prerequisite, not a free factorization/order oracle.

## 3. Exact marked-section observer

On the unit conic `uv=1` in R, define the correlated image

`(z,w) = P(u,v) = (u+v, au+bv)`.

The initial unit u=v=1 maps to the marked point `(2,k)`. Use the affine form

`L(z,w) = w-bz-delta`.

Direct cancellation gives

`L(P(u,v)) = delta(u-1)` in R.                             (2)

If `g0=1`, multiplication by delta preserves the ideal generated with N. Explicitly, a Bezout identity `s delta+tN=1` gives both inclusions between `<N,delta f>` and `<N,f>`. Therefore

`gcd(L(z,w),N) = gcd(u-1,N)`                               (3)

as the exact positive divisor, including the endpoint values 1 and N. Equality of residues is enough: adding a multiple of N to L does not change its gcd with N. Prime-power valuations are not doubled. This repairs the former observer because `z-2 = (u-1)^2/u` would instead square the vanishing order.

Neither propagation nor (3) requires computing `delta^-1`. The typed setup receipt `g0=1`, the algebraic induction and the linear readout suffice. An explicit inverse of P is only needed if a separate consumer asks to reconstruct arbitrary u,v from arbitrary z,w. Its existence proves the representation is bijective on the conic; it need not be executed as part of the sampler.

Geometrically the mark is the affine section `w-bz=delta` through `(2,k)`, together with its gcd-valued residue readout, not just a Boolean incidence test. In an affine-torsor chart one records the chosen reference Cell and this marked point; no global ontic origin is introduced. Translating the chart must transport both the action and the marked affine form.

A useful optional invariant is

`Q(z,w)=z^2-kzw+w^2`,     `Q(M(z,w))=Q(z,w)` over Z,

and `Q(P(u,v))=-delta^2 uv` in R. Thus the conic image has `Q=-delta^2`. When delta is a unit, that quadratic condition characterizes the conic image, since P is invertible. It is an optional membership certificate, not a replacement for the full correlated state: every live state shares Q, while its factor observer can differ.

## 4. Conjugated inversion without P inverse

Let `J(u,v)=(v,u)`. Set

`S = [[1,0],[k,-1]]`,     `S(z,w)=(z,kz-w)`.

For the chosen integer `k=a+b`, the following are exact integer identities:

`SP=PJ`,     `S^2=I`,     `SMS=M^-1`.                       (4)

Hence `SM^eS=M^-e` for every integer e. This is stronger than merely writing `S=PJP^-1` over R: the actual formula does not call an inverse of P or delta. If an implementation instead chooses a reduced representative of k, the last two identities remain exact integer identities for that k, while `SP=PJ` is read modulo N.

On the certified conic image, `L(S(z,w))=delta(v-1)` in R. Because v is a unit inverse of u,

`v-1=-v(u-1)` in R,

so the exact gcd observer is S-invariant on the regular branch. This includes fixed points of S; such points do not license dividing branch multiplicities by two.

## 5. Binary-power schedule and complete stopped histogram law

For the original public schedule with multipliers `c_j=a^(2^j)` and inverses `b^(2^j)`, (1) implies

`P diag(a^(2^j),b^(2^j)) = M^(2^j) P` in R.               (5)

It is enough to square a two-by-two matrix successively; no orbit table or order is an input. The setup and every requested square still cost actual arithmetic. A differently ordered public list of these powers uses the corresponding chronological list of matrices. A schedule of unrelated multipliers is not covered without another certified intertwining interface.

At schedule step j use the full microscopic histogram kernel

`2[1/4] I + [1/4] M^(2^j) + [1/4] M^(-2^j)`.

Here `[q]` means one microscopic branch of weight q. The two identity branches remain `2[1/4]`, not a single `[1/2]`. P is a bijection between the certified conic and its image on the regular branch, intertwines each named action, and preserves the actual gcd by (3). By induction, pushing every live-state histogram through P gives the identical LIVE/factor/depth histogram after each step. A proper factor is absorbed with atom `[1]`, retaining its factor value and first-hit depth.

Further quotienting by S is also safe for this declared kernel: (4) swaps the two nonidentity actions, whose **complete weight histograms** agree, and fixes the two identity branches. The factor observer is S-invariant. Thus both representatives of an S-orbit have identical rows into retained orbit/factor classes. This is the same finite first-hit histogram descent theorem used for the inverse-pair representation.

Two boundaries are essential:

1. P conjugacy retains named actions; the additional S quotient generally does not. A future request for only the named positive action, unequal directional histograms, raw orientation, or complete original path provenance may invalidate S-folding.
2. The theorem uses the declared regular setup branch. Stopping on a factor exposed during setup is a sound augmented search procedure with a new earlier event, not preservation of the old distribution after that event.

No state averaging or moment-only propagation appears in the proof. Applying the averaged matrix to one vector cannot replace the branching kernel when the later observer is gcd-valued.

## 6. Integer X6 realization versus residue quotient

Embed the companion arrow as `M direct-sum I_4` on the first two raw native axes, with a declared initial displacement `(2,k,0,0,0,0)` from the chosen reference Cell. The last four zeros describe a fixed invariant slice. They are not unknown fields silently set to zero. The inverse arrow is likewise an integer X6 arrow. The marked row is `(-b,1,0,0,0,0)` with affine constant `-delta`.

This is a legitimate declared integer-linear macro-program in the current HBW carrier. It does not make a large shear or a power `M^(2^j)` one primitive Cell adjacency. Spatial raw displacement, component-length readout, primitive path length, macro-operation count, and time labels remain different types. No metric-preserving rotation claim is made for P, M or S.

Reduction modulo N commutes with every integer matrix arrow and preserves the marked gcd observation. It is therefore an exact quotient for **this** modular observer and integer-linear future language. It is not a same-Cell rechart preserving arbitrary raw endpoints, metric or common depth.

For a one-step raw state `x=r+Nq`, with r a chosen residue representative, write

`Mr = r' + N kappa`; then `x' = r' + N(Mq+kappa)`.

This displays the omitted carry fiber. If a later observer asks for x rather than its residue, the carry q or an exact reconstructible history must be retained and paid for. For a macro-arrow the same formula holds with that integer macro-matrix, but reconstructing its large entries and carries is not free.

This distinction affects complexity materially. Repeated squaring modulo N needs only a constant-size matrix with O(log N)-bit entries at each stage. By contrast, the unreduced integer entries of `M^(2^j)` can have order `2^j log|k|` bits when the companion has an expanding eigenvalue. A short exponent or operation word does not make its full raw endpoint cheap. The proposed efficient representation is the observer-scoped residue quotient, or a deferred raw program whose future reconstruction cost is explicit; it is not an undocumented deletion of native residual state.

## 7. Optional moving analysis frame

A moving frame is unnecessary for (2)-(5). If one is useful, it must transform the observer at the same time as the state. For explicitly supplied integer-unimodular six-by-six analysis frames `F_j`, write `y_j=F_j x_j`. An arrow `A_j` becomes

`y_(j+1)=F_(j+1) A_j F_j^-1 y_j`.

The marked row at time j becomes `ell F_j^-1`, retaining the same affine constant, and the exchange becomes `F_j S F_j^-1`. The marked point and other coordinate-frame data move consistently. This is a proof of an analysis-coordinate conversion; whether a frame is also a physical/native rotation is a separate contract. Merely invertible-modulo-N frames give only residue charts.

The full first-hit depth is retained even if a frame has a periodic phase. Replacing time by that phase requires its own preservation theorem. Matrix/frame setup, applying the observer row and carrying any raw fibers are charged; no Heartbeat clock speed is inferred from a change of basis.

## 8. Actual source audit and tool match

The following current files were actually read through the authorized connector at immutable EM commit `2e81851d62c869a20b47ae083a24dde1a4c0420c`. Git blob IDs below identify repository blobs, not SHA-256 file hashes.

| Source | Blob | Reused scope and limit |
|---|---|---|
| [HEARTBEAT_WORLD_NATIVE_X6_TIME.en.md](https://github.com/awdawmip/enterprise-math/blob/2e81851d62c869a20b47ae083a24dde1a4c0420c/definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.en.md) | `bc5f22de9dd625c36612a3533f7bba61c30fe01b` | Raw X6 affine torsor, six native axes, separately typed time and observer-relative residual fidelity. It does not make one endpoint the complete world state. |
| [brc_transport.py](https://github.com/awdawmip/enterprise-math/blob/2e81851d62c869a20b47ae083a24dde1a4c0420c/src/enterprise_math/brc_transport.py) | `be1debe367263931bd5e93fd750be3ed54624fe1` | `Affine`, `EffectHistogram`, ordered serial composition and weight/action multiplicities can express declared integer macro-effects. Degree-two moments do not include the gcd observer. |
| [brc_control_port.py](https://github.com/awdawmip/enterprise-math/blob/2e81851d62c869a20b47ae083a24dde1a4c0420c/src/enterprise_math/brc_control_port.py) | `44def6b8ac787e798d3cc2c6be16f873f91b9db8` | Time/control ports and exact effect-valued transitions. Its generic partition checker does not silently substitute a modular-observer equivalence for equality of rational affine effects. |
| [finite_symmetry.py](https://github.com/awdawmip/enterprise-math/blob/2e81851d62c869a20b47ae083a24dde1a4c0420c/src/enterprise_math/finite_symmetry.py) | `ae96a32cb6b6fdd974bd9f44fb28a1b643c9b8a2` | Standard finite action/equivariance interfaces; (4) gives a compact algebraic certificate rather than acquiring all modular orbits for that finite API. |
| [heartbeat_projective_frames.py](https://github.com/awdawmip/enterprise-math/blob/2e81851d62c869a20b47ae083a24dde1a4c0420c/src/enterprise_math/heartbeat_projective_frames.py) | `78e1b765f2355156d9e529835ced7527bb5cd46e` | Explicitly scoped analysis frames for known-prime carry-peak observations. Its projective quotient is not a certificate for the new marked-section gcd observer or a native rotation theorem. |
| [coordinate_address_contract.json](https://github.com/awdawmip/enterprise-math/blob/2e81851d62c869a20b47ae083a24dde1a4c0420c/coordinate_address_contract.json) | `186895a2545b9c5f31de6dc0944aef157f4b35d1` | Registered lossless final-address codecs; the full-X6 codec is not registered. This note publishes no new public Cell address or modulo-wrapping spatial codec. |

The current carry-peak quotient erases precisely the new observer data: every integer-unimodular M product preserves `Z_p^6`, so its linear p-Smith spread is zero for every prime. A marked-section gcd can nevertheless differ among endpoints. The present repair adds an explicit observer interface; it does not discover a factor detector inside the old peak color. Supplying a hidden prime factor as the prime input would also be target leakage.

The prior `HBW_BRIDGE_AUDIT.md` identified the companion candidate and the saturation problem. This note repairs that observer without rewriting the frozen prior note. It does not revive the old fixed six-jet/nilpotent entrance as a generic solution.

Local proof dependencies read for this extension:

* `HBW_BRIDGE_AUDIT.md`: SHA-256 `30b9bfbac68e4ddf79d9d59e9ac9c67d1d7b787a47e6a1cce0bd456dc4ec12c9`.
* `TRACE_OR_FACTOR_CANDIDATE.md`: SHA-256 `fa489d763a78ae9a07abf70a04e9f957f5fb8f3b11db10d8ffcbc59c82aa570f`.
* `GEOMETRY_CONIC_INTERFACE.md`: SHA-256 `1d1a316d191010eb6d8721d9e14c8d81e7f413cfd1da13d99e1633d73d8949bc`.

## 9. Next bounded certificate and accounting target

A future typed implementation can certify a,b,k,delta and `g0`; build the companion and its explicit inverse/exchange; construct the requested modular matrix powers by actual typed multiplication; propagate full microscopic histograms; and evaluate L through typed signed arithmetic followed by gcd and factor division. It can compare against already saved inverse-pair histograms without regenerating an ideal or classical numerical reference.

Useful checks are: full first-hit histograms on the regular branch; positive and negative matrix actions with their chronology; S-folding including fixed points; a prime-power-derived observer fixture; proper-gcd and degenerate setup branches; serialized source/certificate tampering; and a retained failed/partial receipt. These are suggestions for a later authorized finite execution, not results of this note.

Charge all setup gcd/inverse work, P/mark construction, companion squares, matrix-vector actions, linear readout, gcd/factor checks, histogram merges, invariant validation and any replay/raw-carry reconstruction. No repeated `delta^-1` call is needed. However, the companion action may cost more modular products than the correlated inverse-pair route, and the marker requires arithmetic that the original direct `u-1` readout does not. Full support and output histograms can still grow. There is no proven runtime improvement, polynomial factoring bound, support compression, full-Shor closure or new formal admission.

The mathematical progress is specific: the same first-factor witness law now has a nonsaturating marked affine-section readout on an integer-X6 companion program, with an explicit modular conjugacy and symmetry certificate. This makes a fair native-interface cost comparison possible without changing the factor observable.

Shared-context symbolic cross-check: the other author independently confirmed (1)-(5), the setup branches and the raw-carry cost boundary; no additional execution or independent admission was performed.

Global-Knowledge-Sync: main@7a63984 / GLOBAL_KNOWLEDGE_V1.
