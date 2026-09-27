# Three aggregate moments on the HBW marked section

Status: PURE_SYMBOLIC_DERIVATION / NOT_EXECUTED / NOT_ADMITTED.
Researcher EM-DIRECT-C6438C; activity RA-CAAAC604CB513AEA8BBC1DFC.

This is a composition of the already derived marked-section conjugacy and degree-two BRC transport, for a new factor-certificate probe. It is not a preserved first-hit histogram or a completed native Shor algorithm. The current user objective remains completion of Shor through native BRC and Enterprise geometric tools.

## 1. A dual section that closes under transport

Use exactly the regular setup of HBW_MARKED_SECTION_CONJUGACY.md:

    R = Z/NZ, ab=1, delta=a-b, gcd(delta,N)=1,
    M = [[0,1],[-1,a+b]], ell=(-b,1),
    x=P(u,v)=(u+v,au+bv), uv=1.

All displayed matrix/section identities here are in R unless explicitly stated otherwise. Direct multiplication gives

    ell M = (-1,a) = a ell,
    ell M^e = a^e ell,
    L(x) = ell x-delta = delta(u-1).

Thus the linear row ell is an eigen-covector of the companion action. The affine marked readout L is not itself an eigen-observer: its translated value L+delta=ell x is. A positive schedule step c=a^(2^j) acts on L by

    L -> c L + delta(c-1).

The inverse step acts by the same formula with c^-1. The same fixed a,b,delta and marked row are retained for every power; they are not reset to the multiplier at each layer. This is a residue-observer interface of the integer X6 macro-program, not a claim that modular reduction preserves every raw Cell endpoint.

## 2. Exact three-statistic closure for the UNSTOPPED branch population

At each step retain four microscopic branches with multipliers [1,1,c,c^-1]. Count microscopic histories with integer multiplicity, without normalization and without absorption on a gcd event. Let

    h0 = sum 1, h1 = sum L, h2 = sum L^2,
    A1 = 2+c+c^-1, A2 = 2+c^2+c^-2.

Linearity and the binomial formula give the division-free updates

    h0' = 4 h0,
    h1' = A1 h1 + delta(A1-4) h0,
    h2' = A2 h2 + 2 delta(A2-A1) h1
                   + delta^2(A2-2 A1+4) h0.

Initial values are (h0,h1,h2)=(1,0,0). Integer lifts satisfy polynomial identities, so reduction modulo N commutes with this recursion. The coordinates are aggregate residues; recovering the exponentially large exact integer totals is not part of this observer contract. No division by 4 or by 2, no hidden prime, no period and no branch enumeration is needed for these particular residues. The number of layers and every arithmetic operation still have to be paid for.

In the translated analysis frame

    r0=h0,
    r1=h1+delta h0 = delta sum u,
    r2=h2+2 delta h1+delta^2 h0 = delta^2 sum u^2,

the update diagonalizes:

    r0'=4r0, r1'=A1r1, r2'=A2r2.

This is an observer-level use of an affine analysis frame. It removes redundant mixed terms in the recursion; it does not erase unobserved state while claiming to preserve an arbitrary future observer. In particular, a full stopped histogram with per-path gcd/depth events cannot be reconstructed from these three residues.

## 3. Geometric area determinant and certified factor readout

Form the symmetric aggregate matrix

    H_L = [[h0,h1],[h1,h2]], D_L=det(H_L)=h0 h2-h1^2.

For the unshifted unit moments m_j=sum u^j, j=0,1,2, write C=m0 m2-m1^2. Substitution gives the exact polynomial identity

    D_L = delta^2 C.

More generally, for any affine scalar readout f=alpha u+beta,

    det(sum (1,f)^T(1,f)) = alpha^2 C.

The translation beta cancels. If alpha is a certified unit modulo N, the exact positive gcd with N is unchanged, including prime powers and endpoint values 1 and N. This shows explicitly that the candidate factor does not depend on an arbitrary affine shift of the chosen marked chart. A nonunit alpha is a separate setup outcome and cannot be silently divided away.

There is also the division-free pairwise identity

    C = sum_(i<j) (u_i-u_j)^2,

where indices include all microscopic multiplicities. It motivates an area/Gram interpretation, but over a finite field a zero sum of squares need not imply that every term vanishes. Therefore D_L=0 modulo a prime is NOT, by itself, a witness that all occupied sections coincide there, that an orbit has returned, or that its order has been recovered. This includes finite-characteristic cancellation and h0 vanishing modulo a prime. No Euclidean positivity argument is used.

A typed computation of d=gcd(D_L,N), followed by exact typed division when 1<d<N, is nevertheless a sound factor certificate. Soundness is separate from the chance of a useful gcd. d=1 is an unsuccessful probe; d=N is saturation, with no proper factor unless an additional charged refinement is supplied. This signed determinant is an algebraic post-processing observer, not negative probability mass or a QFT amplitude claim.

## 4. What this contributes, and what remains open

The generic degree-two transport pattern becomes a concrete HBW marked-section aggregate with three modular coordinates. Its geometry explains why an affine frame change can simplify the recurrence without changing the final proper-factor certificate. This is COMPOSE/DOMAIN_OPERATOR_CANDIDATE, not a new top-level classical theorem or a Foundation revision.

The companion/section proof supplies the exact bridge to the native program; existing rational T0 moment APIs do not automatically execute modular typed arithmetic. A bounded typed-ring implementation still has to bind its sources and separately charge unit admission, schedule construction, moment transport, determinant formation, gcd, and factor verification. Running both the expanded affine recurrence and the diagonal recurrence for a validation case must charge the extra route separately. It must not claim that the diagonal form independently certifies every omitted raw HBW coordinate.

The separate AGGREGATE_WITNESS_PROBE_AUDIT.md analyzes what algebraic factors this determinant can detect. Neither note establishes a useful uniform success probability for unknown large factors, an efficient repetition/refinement strategy, period reconstruction, or a general classical replacement for Shor. Those are the scientific targets. A successful constructed example would validate the interface, not close them.

Any continuation conversation can verify these symbolic identities and develop the missing success argument without the original runner or author. A local typed execution is an additional evidence unit, not an environmental prerequisite for advancing the mathematics.

Dependencies: HBW_MARKED_SECTION_CONJUGACY.md SHA256 fbec0b42234fe7a126e5bf03b14842ee0935d7801836b4dce99e5b6167346ce1; brc_transport.py immutable source blob be1debe367263931bd5e93fd750be3ed54624fe1 at EM 2e81851d62c869a20b47ae083a24dde1a4c0420c, as audited in the marked-section note.

Global-Knowledge-Sync: main@7a63984 / GLOBAL_KNOWLEDGE_V1.
