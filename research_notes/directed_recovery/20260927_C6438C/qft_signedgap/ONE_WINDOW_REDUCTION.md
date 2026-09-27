# One negative bit: one window query and an interval count

Status: SYMBOLIC_AUTHOR_DERIVATION / SHARED_CONTEXT / IMPLEMENTATION_PENDING.

This refines the executed three-window integer observer without changing its inputs or its raw normalization. It concerns a contiguous gap with physical stride one, one negative bit, and an arbitrary positive counting modulus R. It neither discovers a work order nor gives an address logarithm.

Let g>=1, 0<=k<g, U=2^k, H=2^(g-k-1), L=2UH=2^g. Every x in [0,L) has the unique form x=2UA+Ue+v with A in [0,H), e in {0,1}, v in [0,U). The signed coefficient is

    K(r) = sum_{0<=x,y<L; y-x = r mod R} (-1)^(e(x)+e(y)).

Define J0 as the existing window_weight(H,U,2,R,r,0), and Jplus/Jminus as the same function at displacements +1/-1. The two equal-bit blocks (e,e')=(0,0),(1,1) have the same difference multiset, hence each contributes J0. The remaining two blocks contribute Jplus and Jminus. They partition all pairs, without boundary loss, even when R is even, one, or larger than L.

Let T_L(r) count every unsigned pair in the full contiguous interval [0,L). Then

    T_L(r) = 2 J0 + Jplus + Jminus,
    K(r)   = 2 J0 - Jplus - Jminus = 4 J0 - T_L(r).

Thus the production algorithm needs one existing floor-window query, one existing interval_count(L,R,r), and the typed signed combination 4*J0-T_L. This is an algebraic replacement, not dropping negative contributions. K can be negative and the surrounding Gram denominator remains 4^g (recorded exponent 2g).

For completeness, if L=qR+u, 0<=u<R and 0<=r<R, the already implemented interval counter is

    T_L(r) = R q^2 + 2 q u + max(u-r,0) + max(u-(R-r),0).

This follows by writing the residue multiplicities as q plus the indicator of [0,u). It uses a constant number of signed/unsigned typed arithmetic operations after actual Euclidean division. In the implementation, L and every scientific magnitude, sum, product, difference and division still follow the admitted typed arithmetic path; loop indices, routing and signs are host wiring.

The old method makes three degree-three window queries; the new method makes one plus the simple interval count. Both have polynomial bit cost in g+log(R+1) under the pinned fixed-degree Euclidean recurrences. This reduces a query count and may reduce constants, but is not a new asymptotic class and does not guarantee a speed ratio: cross-query memoization, division costs, full evidence retention and serialization matter. New bounded executions must retain and compare actual counts against the frozen three-window results rather than infer wall-clock speed.

The signed sets interpretation also gives a useful limit. With S0={2UA+v}, the two sign classes are translates S0 and S0+U. Their equal-sign autocorrelations coincide; that equality is why one window suffices. For an arbitrary Walsh mask, the two classes need not have a cheap single-window representation. The identity is therefore not a general arbitrary-mask oracle, multiple-gap contraction, or full QFT simulator.

Continuation: implement a separately versioned one-window observer; compare all 31 existing residue results and full fresh typed replay certificates without rerunning the old pair enumeration; retain the complete previous 97,157,549-byte payload as immutable reference and report production, replay and control costs separately. Mathematical dialogue can extend the partition argument or identify other sign-class symmetries directly from this note, independently of local execution availability.
