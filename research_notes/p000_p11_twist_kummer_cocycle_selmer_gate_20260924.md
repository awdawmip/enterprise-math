# P000 P11 fixed-2-twist Kummer cocycle normalization and exact target-Selmer gate

Status: `PORTABLE_STAGED_RESEARCH / NO_CURRENT_CLAIM / NOT_SOURCE_CHECKPOINT / NOT_RESULT / UNREVIEWED`

Task: `RS-P000-P11-DIAGONAL-ELLIPTIC-FIBER-PRIMITIVE-ARITHMETIC`
Publication: `TP2-FB7F5A1D6B6C6BCCD62D`
Contributor lineage: `EM-DIRECT-C4D02C`, stable conversation `em-auto-staggered-20260923-r11`, session `MCP-5ff2a3263c5c4ca2b556ebe8e47e5624`.

This note is a noncanonical persistence copy of same-session portable research. It consumes without promotion the staged exact fiber
`E: W^2=X(X-P^2)(X-Q^2)`, the fixed 2-twist
`E^(2): y^2=x(x-2P^2)(x-2Q^2)`, the universal infinite-order twist point
`R2=(4C^2,4PQC)`, the exact real/Q2 Kummer images, and the exact odd-local Kummer images/residue matrix. None of those staged inputs is represented here as Source-published predecessor progress.

Write `t=sqrt(2)` and `K=Q(t)`. Retain
`P^2+Q^2=2C^2` and `P^2-Q^2=4AB`, with P,Q,C odd and P>Q>0.

## 1. Canonical common full-2-torsion module

Over K the exact twist isomorphism is

`psi:E_K -> E^(2)_K`, `psi(X,W)=(2X,2tW)`.

It carries the three labeled nonzero rational 2-torsion points canonically:

`T0=(0,0) -> T0'=(0,0)`,
`TP=(P^2,0) -> TP'=(2P^2,0)`,
`TQ=(Q^2,0) -> TQ'=(2Q^2,0)`.

Thus the two curves have the same labeled trivial Galois module E[2]; no arbitrary Kummer coordinate triples are identified by fiat.

## 2. Explicit half and cocycle of the universal twist point

The inverse image of R2 is the staged anti-invariant point

`S2=(2C^2,tPQC) in E(K)`.

Define

`x_T = 2C^2+PQ-tC(P+Q)`,
`y_T = -(P+Q)(tC-P)(tC-Q)`.

Equivalently `x_T=((P+Q)/t-C)^2`.

Direct substitution using only `t^2=2` and `P^2+Q^2=2C^2` gives
`y_T^2=x_T(x_T-P^2)(x_T-Q^2)`.
For
`W^2=X^3-(P^2+Q^2)X^2+P^2Q^2X`,
the doubling slope at T is

`m=tC-(P+Q)`.

The standard duplication formulas give exactly

`2T=(2C^2,tPQC)=S2`.

Let sigma be the nontrivial element of Gal(K/Q). Conjugating and adding T to sigma(T), the secant slope is `-(P+Q)` and the addition formulas give

`T+sigma(T)=T0`,

hence

`sigma(T)=T0-T`.

Put `U=psi(T) in E^(2)(K)`. Then `2U=R2`. Because sigma changes the sign of t in the twist isomorphism,

`sigma(U)=-psi(sigma(T))=U+T0'`.

Therefore the Kummer connecting cocycle of the rational point R2 is exactly

`c(sigma)=sigma(U)-U=T0'`.

Under the canonical labeled identification of the two 2-torsion modules, the corresponding global cohomology class is

`eta_2 = chi_2 tensor T0`,

where chi_2 is the quadratic character of Q(sqrt(2))/Q. In the standard labeled full-2-torsion Kummer triple this is precisely

`eta_2 = (1,2,2)`.

This recovers the staged direct computation `delta_2(R2)=(1,2,2)`, now with an exact Galois-cocycle meaning.

## 3. Exact target local gate at every place

Ask whether the same canonically normalized class eta_2 belongs to the target local Kummer images for E. This is a local-Selmer question, not a point-transfer claim.

### Real place

2 is positive and hence a square in R, so eta_2 is the trivial local class.

### Good odd primes

The class has only the squareclass 2, hence is unramified at every odd prime. The consumed exact odd-local analysis gives the unramified/unit product-one condition, so eta_2 is locally allowed.

### Odd primes dividing P

The consumed exact local image is
- `{(d,d,1)}` if ell=1 mod4;
- all unit product-one triples if ell=3 mod4.

If ell|P and ell=1 mod4, the core identity `Q^2=2C^2 mod ell` with ell not dividing QC implies `(2/ell)=+1`, so eta_2 is locally trivial. If ell=3 mod4, `(1,2,2)` is a unit product-one triple. Thus eta_2 is always allowed at ell|P.

### Odd primes dividing Q

The same argument, using `P^2=2C^2 mod ell`, gives local admissibility at every ell|Q.

### Odd primes dividing AB

The consumed exact local image is `{(1,d,d): d arbitrary in Q_ell^*/Q_ell^{*2}}`. Taking d=2 gives eta_2 directly.

Thus every place except v=2 admits eta_2 for every primitive core.

### The 2-adic place

Let `h=v2(P^2-Q^2)=3+v2(e)`, where e is the even member of {r,s}. The consumed exact Q2 theorem gives:

TYPE-5+ (`h>=5`):
`Im kappa_2={(1,d,d): d in Q_2^*/Q_2^{*2}}`; hence `(1,2,2)` is allowed.

TYPE-4 (`h=4`):
`Im kappa_2={(d0,d1,d2): d0 in {1,5}, d1,d2 unit squareclasses, d0*d1*d2=1}`; the class `(1,2,2)` is excluded because 2 has odd 2-adic valuation and is not a unit squareclass.

Therefore

`eta_2 in Sel_2(E/Q) iff TYPE-5+ iff v2(P^2-Q^2)>=5 iff 4 divides e.`

On TYPE-4 the sole local failure is Q2.

## 4. Identification of the staged epsilon radical

The staged global edge-normal form in TYPE-5+ is

`d0=alpha*beta`,
`dP=2^epsilon*alpha*gamma`,
`dQ=2^epsilon*beta*gamma`.

Setting `alpha=beta=gamma=1` and `epsilon=1` gives exactly `(1,2,2)=eta_2`. Hence the previously isolated matrix basis vector `e_epsilon` has the cohomological interpretation

`e_epsilon = chi_2 tensor T0`.

The earlier proof that `e_epsilon` is an isolated radical in TYPE-5+ is therefore the statement that, after all local conditions, the universal fixed-twist direction contributes one canonical target Selmer direction, whereas TYPE-4 rejects that direction exactly at Q2.

The staged independence of `e_epsilon` from the strict rational-2-torsion radical tau yields at least two distinct Selmer directions on TYPE-5+: the ordinary torsion provenance line and this twist-character line. This does not prove positive target Mordell-Weil rank: eta_2 may be realized by E(Q)/2E(Q) or may survive only in Sha(E/Q)[2].

## 5. BRC consequence

For the operation “does the fixed quadratic-twist direction survive as a target Selmer class?”, the minimal safe carrier is the labeled torsion port T0 together with the quadratic character chi_2 and the 2-adic core type. P/Q/R local provenance can be quotiented only after the exact local checks above show that those places never reject eta_2. Erasing TYPE-4/TYPE-5+ before Q2 would merge an excluded class with a genuine Selmer class and is unsafe.

This closes the immediately preceding portable next-action question: the twist class `(1,2,2)` induces a lawful target 2-Selmer class exactly on TYPE-5+, and on TYPE-4 it is excluded by the single typed local condition Q2. No rational-point transfer is asserted.

## 6. Exact next unit

Do not redo the common E[2] normalization, the all-place gate above, or the fixed-twist no-transfer theorem. The smallest new arithmetic question on TYPE-5+ is the fate of eta_2 under

`0 -> E(Q)/2E(Q) -> Sel_2(E/Q) -> Sha(E/Q)[2] -> 0`.

Determine whether eta_2 is Mordell-Weil-realized on an infinite primitive family, forced into Sha[2] on an infinite family, or controlled by an exact Cassels/local-norm pairing with the remaining provenance-preserving residue radical. On TYPE-4 this twist-character route is locally dead at Q2, so the existing Pfaffian/Plucker obstruction remains the relevant frontier.

BRC resolution: `COMPOSE_APPLIED / COMMON_E2_NORMALIZED / TWIST_CHARACTER_IDENTIFIED / EXACT_Q2_SELMER_GATE / NO_POINT_TRANSFER`.
