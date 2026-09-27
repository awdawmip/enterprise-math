# An exact lowest-bit lift for signed correlation queries

Status: new symbolic derivation only, not yet peer-reviewed or executed. It introduces no order discovery or actual-program mutation. The existing query domain is ordered pairs in a fixed finite interval, grouped by their difference modulo a supplied positive counting modulus.

For any fixed real scalar weights f(x) on 0<=x<L, define

    K_f(R,r) = sum_{0<=x,y<L, y-x=r (mod R)} f(x)*f(y),
    f_star(x) = (-1)^x*f(x),                0<=r<R.

Because (-1)^(x+y)=(-1)^(y-x), the extra lowest-bit sign depends only on the displacement. If R is even every displacement in the class r has parity r. Hence

    K_f_star(R,r) = (-1)^r * K_f(R,r),      R even.

If R is odd, the class r modulo R partitions into the two classes r and r+R modulo 2R. Their displacement parities are opposite. Consequently

    K_f_star(R,r) = (-1)^r * (K_f(2R,r) - K_f(2R,r+R)),    R odd.

These are disjoint exhaustive pair partitions, so negative displacements and both orientations are included automatically. Both targets are canonical residues modulo 2R. The r=0 case needs no exceptional multiplicity correction. R=1 uses the ordinary classes zero and one modulo two and never calls an inverse-of-one operation. L need not be a power of two for these identities.

For the bit-gap application set L=2^g and f(x)=(-1)^(bit_k(x)), with k>=1. Then f_star is the two-negative-bit mask {0,k}. Its exact signed query reduces to one existing single-bit query for even R or two for odd R. Raw normalization remains 4^(-g), since the finite pair domain is unchanged. The actual single-bit observer accepts arbitrary positive counting moduli, so replacing R by 2R does not silently assume a newly known multiplicative order. If k=0 instead, multiplying the same lowest-bit sign twice yields the unsigned interval query; it must not be labeled a two-distinct-bit mask.

If the underlying single-bit query has polynomial cost in the public integer bit lengths, these one-or-two-call reductions preserve that property, including the extra bit in 2R. This extends a restricted family; it does not solve arbitrary Walsh masks or prove general Shor simulation efficient. No experimental cost saving, literature-first novelty or formal admission is asserted.

For a future typed implementation, derive parity and 2R through the actual integer runner, preserve both signed oracle receipts, bind their unchanged source/proof/input domain, and record the outer subtraction and sign multiplication. A verifier must reconstruct the appropriate even/odd branch and both odd-modulus residues; it cannot trust a claimed lift or a claimed zero. A small independently executed typed pair comparator would be new work for this two-bit family and must not be mislabeled as the previous 31 one-bit cases.

The f array and any outside selected native words are held fixed in this identity. Toggling an actual semiclassical history bit can also change later selected phase words; this proof does not say that those induced changes vanish. Its immediate role is a signed scalar-gap coefficient after the full operator/carry contract has been established.

Global-Knowledge-Sync: main@f8aa9c8 / GLOBAL_KNOWLEDGE_V1
