# Which geometric marks change a companion-return witness?

Status: **PURE_SYMBOLIC_DERIVATION / NOT_EXECUTED / NOT_ADMITTED**. Author context `EM-DIRECT-C6438C`, activity `RA-CAAAC604CB513AEA8BBC1DFC`. This is a new symbolic unit; it does not modify the frozen free-trace or trace-valuation notes and contains no numerical execution.

Let R=Z/NZ, M=[[0,1],[-1,k]], and Q_k(r,s)=r^2-krs+s^2. Take an arbitrary public mark w=(r,s). Its cyclic basis has

`C_w=[w,Mw]=[[r,s],[s,-r+ks]]`, `det(C_w)=-Q_k(w)`.

Thus a paid gcd(Q_k(w),N)=1 is exactly a unit-determinant certificate for this cyclic basis. A proper gcd is already a factor, and a saturated gcd is a noncyclic setup case, not permission to invert. This test can be carried out by the same native polynomial/gcd operations as the existing conic interface.

## Full return is independent of every admissible cyclic mark

Let T be any matrix commuting with M, including M^E-I or M^E+I, and put z=T w. Commutation gives

`T C_w=[z,Mz]`.

If Q_k(w) is a unit, right multiplication by C_w is invertible over R. Hence the ideal of all four entries of T equals the ideal of all entries of [z,Mz]. The latter is precisely the ideal of the two coordinates of z: its first column supplies z, and Mz is an R-linear combination of z. Therefore

`ideal(entries T)=ideal(coordinates T w)`.

Lifting the ideals to integer gcds with N yields an exact divisor identity, including prime powers:

`gcd(N,entries T)=gcd(N,(T w)_1,(T w)_2)`.

The proof uses a unit inverse only to establish ideal equality. A production algorithm need not calculate that inverse; it can use the setup certificate and compute the two coordinates directly. If it chooses to compute a basis transformation, that additional native work is still paid.

Consequently changing the cyclic mark cannot alter the complete identity-return or antipodal-return divisor of a fixed k,E. A search over admissible marks is redundant for that observer. This is an exact scope limit, not a general lower bound for factorization or a prohibition on changing k, E, the underlying curve, or the declared observation.

## Coordinate and projective observations have a different scope

A single coordinate or linear form of z can have a proper gcd even when the common ideal is the whole ring. Such a hit is a valid factor witness but is not a complete matrix return. It must be labeled by its own observation contract, with the projection selection and every attempted gcd charged.

For example, over a prime field, if z is nonzero and a row ell is uniform in F_p^2, the linear map ell -> ell z is surjective with a kernel of size p. Its zero probability is exactly 1/p. This statement is only about uniform rows at a fixed nonzero z; it is not a factoring success theorem, does not assume a free uniform sampler, and does not extend to an adaptively selected row without its own proof. It explains why merely adding many unnamed projections is not evidence of high-density factor separation.

An invertible integer or residue change of the two output coordinates also leaves their common gcd unchanged. A nonunit rescaling or singular projection can change valuations, so it cannot be treated as a lossless coordinate change. The earlier trace-square lemma is one concrete example of an observation changing the ideal rather than merely displaying it differently.

## Native-tool consequence

The useful native interface is a two-coordinate ideal witness plus a paid cyclic-basis certificate. It can reuse declared unimodular HBW macros and retain integer/valuation information without storing four matrix entries. This does not make arbitrary affine or nonlinear observers interchangeable. It also provides an implementation pruning rule: do not spend a search budget varying cyclic marks while claiming to improve the same full-return event.

The next choices that can change the event are the companion parameter, exponent schedule, a separately declared projection, or a different geometric group. Existing conic changes retain local orders dividing p-1 or p+1 in the regular case; investigating a different curve requires a new lawful native arithmetic/observer interface, not just a new name for the old mark.

Global-Knowledge-Sync: main@8c23cca / GLOBAL_KNOWLEDGE_V1
