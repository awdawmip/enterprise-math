# 心跳世界代数：六轴整数环、余数进位与带时间的 BRC

Researcher-ID: `EM-DIRECT-AD0416`
Research-Activity-ID: `RA-37C0A30C7B1F5A338F03D186`
Progress-Event-ID: `heartbeat-world-algebra-naming-20260919-AD0416`
Session: `chat-local-reciprocal-ceec8bd1559acdf8c10ebc9b` (reused local identifier, not platform-authenticated).
Read pins: GLOBAL_KNOWLEDGE `37f93f9bc0b7349550d506709eb8de90e27f9dad`; EM `5d3b1302f67e988ee46485aed3cfa2e1df3c58f8`.
Naming status: `DIRECT_CURRENT_USER_CONSTRAINT`.
Mathematics/tool status: `RESEARCH_CONSTRUCTION / SCOPED_PROOFS / EXACT_CHECKS / NOT_FOUNDATION`.
No formal CLAIM, independent review, physical clock calibration, whole-project test result or Nollm deployment is asserted.

## 1. Definition versus the chosen model

The user names the entire native six-space-plus-one-time world 心跳世界 / HEARTBEAT_WORLD. This is not a name solely for b=2, a twelve-tick program, or a visualization. The binding human/machine contracts are `definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.md` and `.json`, linked by P000. Native X6 signed displacements, final six-field nonnegative Cell addresses, temporal events and decorated branch states remain distinct.

For the research below choose a raw relative Cell chart, an ordered cyclic six-axis frame, and integer b>=2. Write A_b(z)=(b*z6,z1,z2,z3,z4,z5), with A_b^6=bI. These choices induce an algebra; P000's six-axis metric alone does not choose this multiplication. Changing the anchor/frame requires transporting the operation, rather than asserting coordinate-independent multiplication of arbitrary Cells. Time t is the separately typed update order; the formal algebraic symbol lambda below is NOT elapsed time.

## 2. A faithful integer polynomial representation

Associate z=(z1,...,z6) with f_z(lambda)=z1+z2*lambda+...+z6*lambda^5 in

R_b = Z[lambda]/(lambda^6-b).

Then f_(A_b z)=lambda*f_z. The six vectors e1,A_b e1,...,A_b^5 e1 are exactly e1,...,e6, so no nonzero polynomial of degree<6 kills A_b. As A_b^6=bI, the minimal polynomial is exactly X^6-b for every b; the representation is faithful even when this polynomial factors.

For zero-based coefficient indices k=0,...,5 define the product
(z*w)_k = sum_(i+j=k) z_i*w_j + b*sum_(i+j=k+6) z_i*w_j.

This is ordinary polynomial multiplication followed by the monic relation lambda^6=b. Hence addition/subtraction and this product obey the commutative ring laws; e1 is the unit. Naturals embed as (n,0,...,0) and act by nI. No prime-only projection or deletion of composite objects occurs. This is not a claim that all natural numbers automatically spread over all six axes.

Examples: lambda^3*lambda^3=b; lambda^5*lambda=b; (1+lambda)(1-lambda)=1-lambda^2. Computation needs only six integer coefficients and integer folded convolution; no numerical value of b^(1/6) is materialized.

For b=2, X^6-2 is Eisenstein at2, so R_2 is an integral domain and Q[lambda]/(lambda^6-2) is a degree-six field. An elementary proof: a nontrivial monic integral factorization would reduce mod2 to two powers of X, making both constant coefficients divisible by2 and their product divisible by4, contradicting constant term -2 (using the primitive/monic Gauss lemma). The same proof applies to prime b. R_2 is an order; no assertion that it is the full ring of integers is made.

In contrast, b=4 has (lambda^3-2)(lambda^3+2)=0 with two nonzero coefficient vectors. The same sixbeat identity therefore does NOT imply a domain or field for every radix. The inverse interface rejects singular multiplication matrices. This is a counterexample to an overstrong algebraic extension, not to the world's name or native dimension.

## 3. Division distinguishes units, residues and rational readouts

Let L_z be the six-by-six integer multiplication matrix for z, and N(z)=det L_z. This arithmetic norm is not the native spatial length L_E or its square.

L_(z*w)=L_z L_w, hence N(z*w)=N(z)N(w). If N(z)!=0, the integer quotient Z^6/L_z Z^6 has cardinality |N(z)|. A lattice inverse exists on all integer inputs exactly when |N(z)|=1, by the determinant/adjugate criterion. This counts residue types, not the number of inverse images of an injective multiplication map. On L_z Z^6 the inverse is unique; arbitrary input needs a coset representative to define quotient plus residue.

At b=2:
- N(lambda)=-2: two residue classes;
- N(2)=64: 64 residue classes;
- N(1+lambda)=-1: an integer automorphism, no coset ambiguity.

Indeed 1/lambda=lambda^5/2 is a rational readout, whereas

(1+lambda)^(-1)=-1+lambda-lambda^2+lambda^3-lambda^4+lambda^5

has integer coefficients, since the product is lambda^6-1=1. Thus a mixed-axis algebraic element may be invertible over integer coordinates even though a scalar2 is not. An inverse here does not certify one primitive physical move, low fine-step cost, probability cancellation or time reversal.

The reference `divide_readout` reuses exact matrix inversion from current BRC transport and returns a primitive integer numerator vector and a positive denominator. Denominator>1 is explicitly outside raw integer Cell coordinates. This is neither an integer factorization algorithm nor a field-generic complexity improvement.

## 4. Carry is an explicit spatial correction

The existing one-beat contraction is exactly division with remainder by lambda:

z=lambda*q+r,  q=(z2,...,z6,floor(z1/b)), 0<=r<b.

Here r is a scalar multiple of e1. For w=lambda*p+s, define c=floor((r+s)/b) and r'=(r+s) mod b. Because b=lambda^6,

z+w=lambda*(q+p+c*lambda^5)+r'.

So the microbeat carry enters the SIXTH coordinate of the coarse state, not its first. Subtraction uses c=floor((r-s)/b) and the Euclidean remainder. Both statements include negative original inputs.

For multiplication, c=floor(rs/b), r'=rs mod b, and

z*w=lambda*[lambda*q*p+s*q+r*p+c*lambda^5]+r'.

This yields exact arithmetic on the retained pair (q,r). Coarse coordinates alone lose carry and cross terms. Example at b=2: analyze(1)=q0,r1, so adding two such values requires coarse carry lambda^5; discarding the residue would return zero instead of2. This is not a failure of distributivity in the full algebra, but a failure to preserve the operation after an information-losing observation.

One-step parity does not suffice for arbitrary later contractions: original T6 on states0..63, parity output and floor(n/2) future action gives block counts2,4,8,16,32,64,64. Longer obligations reveal finer digits. The previously proved conditional-moment repair remains one-step scoped.

## 5. Timing changes action order, not scalar multiplication

At one common chart/time, algebraic multiplication above commutes. Timed update words generally do not. Put H(z)=A_b z and T_u(z)=z+u. Exact covariance is

H o T_u = T_(A_b u) o H.

For tick updates F_u(z)=A_b z+u,
F_v o F_u(z)=A_b^2 z+A_b u+v,
F_u o F_v(z)=A_b^2 z+A_b v+u.

Their difference is (A_b-I)(u-v). With b=2,u=e1,v=e2, start0, the endpoints are2e2 versus e1+e3. The two words have the same two tick counts and the same injected unit-step counts. A heartbeat's own global physical compute/transport cost is not claimed zero.

General forward words z->A_b^k z+u combine chronologically by

(k,u) star (l,v)=(k+l,A_b^l u+v).

Associativity follows because either triple association gives (k+l+m,A_b^(l+m)u+A_b^m v+w). This is standard semidirect action algebra, not a new number-multiplication law. At complete sixbeats, the one-axis dilation/translation relation matches the standard affine Baumslag-Solitar relation; that comparison lives in an algebraic extension where inverses are admitted, not in the positive-time physical evolution category.

The heartbeat respects addition, but is not a unital ring automorphism:
(A_b z)*(A_b w)=A_b^2(z*w), not generally A_b(z*w).

This is the familiar degree-two scaling of multiplication. It does NOT mean that physical time ran twice as fast. To express the same material product in a moving chart F_t, transport the law as m_t(x,y)=F_t(m_0(F_t^-1 x,F_t^-1 y)) on its valid image, or retain the actual integer residual lift; do not silently apply a raw rational inverse to arbitrary Cells.

## 6. Temporal BRC ports and identity

A timed affine arrow is (start t,duration k,effect F). It maps an event (z,t) to (F(z),t+k). Composition requires the first target time to match the next source time. Parallel alternatives in the minimal `TimedPacket` interface have the same source and target times. Variable-duration branches need an explicit family of different target ports, not untyped merging.

Use the existing positive EffectHistogram at each such port. Serial and alternative composition retain its laws when the time ports match. This is a T0 domain adapter, not a replacement for existing scalar/multiplicity/provenance carriers. Equal timed effects still need not preserve full labeled history under history-sensitive observations. Hidden state/phase/resources used later require additional typed ports.

An identity arrow has duration0 and spatial identity. A forward heartbeat followed by a spatial inverse with positive duration returns the coordinate but ends at a later time. Similarly H^6 and scalar2 have the same spatial linear map, but they are equal timed arrows only with matched temporal ports; full path-formal identity is stronger still. No periodic spatial/phase return equates two absolute-time events by default.

BRC alternative addition is not addition of spatial coordinates or arithmetic coefficients. Two positive branches at the same location still have multiplicity2; coefficients of an algebraic inverse can be signed without becoming negative branch masses. The six normalized binary refinement packets were matched against all64 explicit alternatives with mass1.

## 7. Modular observation produces two genuinely different regimes

For M>=2 and gcd(b,M)=1, A_b is an invertible matrix on (Z/MZ)^6. Its exact matrix order is

ord(A_b mod M)=6*ord_M(b).

Proof: A_b^k e1=b^floor(k/6)e_(1+k mod6); to return e1 first requires k divisible by6, then b^(k/6)=1 modM. Conversely this condition makes the full matrix identity. This is a matrix order / test-orbit period, not every vector's least period or an absolute event return.

For b=2 modulo2^k, A_2 is not invertible; its nilpotency index is exactly6k: A_2^(6k)=2^k I=0 mod2^k, while A_2^(6k-1)e1=2^(k-1)e6 is nonzero. This erases a finite low-bit observer under expansion, not the full integer point. Retaining quotient/high digits recovers the information; time does not reverse. At M=3,5,7 the matrix orders are12,24,18 respectively.

## 8. Reuse, verification and limits

Reused exact pinned current `brc_transport.py`, `brc_histogram.py`, and `predictive_quotient.py`; all three full files match their Git blob hashes and are executed. The already supplied prime-valuation dependency is a clearly labeled minimal excerpt. Reuse classifications: T0 affine/histogram `REUSE_EXECUTED`; T5 mixed radix `REUSE_EXECUTED` through existing euclidean_digits; T6 `REUSE_EXECUTED`; cyclic-ring arithmetic and explicit temporal-port wrapper `EXTEND_EXISTING_TOOL / RESEARCH_DOMAIN_OPERATOR`. No claim is made that generic polynomial quotient arithmetic is absent from every other project module.

15 check groups PASS:180 basis products over radices2,3,4,5,7;2400 exact ring-law triples;120 matrix/norm/division comparisons;729 exhaustive integer-unit inverse examples;5000 residue arithmetic pairs;300 temporal composition triples;64 literal BRC branches;10 odd-modulus matrix orders;8 power-of-two nilpotency boundaries;6 invalid contract mutations;7 bad input rejections. The first run completed mathematical assertions but failed JSON serialization of a Fraction; the serializer was corrected and the whole suite rerun. This implementation fault is not represented as a mathematical finding.

Proofs supply all-scale claims. No full project test suite, independent referee, Lean proof, minimal polynomial-multiplication hardware bound, semantic recall benchmark or physical time law. The ring construction is scoped; the world's name/native coordinate constraint is user-authoritative. Existing P000 fields are byte-verified before an additive naming/companion-contract change; no old axiom or address gate is weakened.

Primary comparison sources consulted (abstract/metadata unless stated): Guelman–Liousse, arXiv:1010.4133, affine dilation/translation relation; Garcia Garcia et al., arXiv:1603.03330, polyphase/perfect reconstruction; Jena–Sahoo, arXiv:1612.06700, Eisenstein-type irreducibility. The elementary formulas above are proved here; no global novelty audit is claimed.

## 9. Axis-symmetry boundary (new verification, not a world change)

The fixed-frame ring does not preserve the entire native positive-axis S6 as ring automorphisms. Any unital positive-axis permutation must fix e1=1 and send lambda to lambda^j for some j=1,...,5. Applying the relation gives b=(lambda^j)^6=b^j, so j=1 and every basis power is fixed. Only the identity survives. Among all signed-axis permutations the same argument gives lambda -> +/-lambda, hence exactly two automorphisms (identity and alternating coefficient signs). All46080 signed permutations were checked against basis-product preservation; this agrees with the proof.

This does NOT reduce geometric native S6. It shows that selecting this multiplication is additional structure. Under a native relabeling P, transport the ring as x *_P y=P(P^-1 x * P^-1 y) and the heartbeat as A'_b=P A_b P^-1. The ring remains isomorphic but its coordinate formula/unit change. Phase-aware transported products, not a frozen static product mislabeled universal, are the next useful interface.

## 10. Next exact unit

Implement the phase-aware transported-product interface over a declared heartbeat program, then test one nonlinear state-dependent interaction while preserving time/resource ports. The signed-axis permutation classification above is complete only in its stated monomial class; do not inflate it to all lattice automorphisms. For finite-horizon BRC, preserve phase/resource ports before simplifying the new timed algebra. Do not restart the established reciprocal/gcd, 5/7, Bridge-budget or velocity-census probes.
