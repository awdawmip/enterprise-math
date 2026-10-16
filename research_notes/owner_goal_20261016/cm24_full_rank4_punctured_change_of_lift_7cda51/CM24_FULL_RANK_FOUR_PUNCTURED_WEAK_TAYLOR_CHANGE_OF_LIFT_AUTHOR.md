# A positive full-rank-four change of lift on the fixed punctured weak ring

Author EM-PUBLIC-7CDA51. NEW AUTHOR PAPER, FROZEN UNREVIEWED. This is separate from my completed nonauthor CM24/P11 reviews; none of their PASS verdicts reviews this proof. Root directed the positive-arrow scope. No other actor supplied this construction or repair. This paper composes ordinary Taylor transport with the existing weak degree/valuation mechanism, not a new general Tool or a historical-novelty claim. No scientific program is used.

## 1. Exact full carrier, ring and claimed arrow

Fix an original allowed prime p congruent to 13 or 19 modulo 24. Retain the unramified complete p-adic DVR O, its coefficient Witt map σ with σ(p)=p and σ(O)⊂O, an integral chosen g, and σ0=1−2g. The symbol σ0 is not the endomorphism σ; σ(g)=g is not assumed. Put m=(p−1)/2 and retain the exact lift

    H_b(x)=g(1+x^m)+(4σ0/5)x+(σ0/5)x^(m−1).

Let f=1−r², q=4r²−1, u=f^-1, v=q^-1, and

    A=O[r,u,v],     A† its existing weak p-adic completion,
    S=4r³−3r,      w=(8r^p−4r)/f,
    D=S'(r)/(6(S²−1)) * [[−(2S−1),−1],[−(4S−5),2S−1]].

The fixed solution-column connection is the ENTIRE matrix

    Ncal=[[D11,D12,0,0],
          [D21,D22,0,0],
          [0,0,0,0],
          [w,0,−w H_b(r²),0]],        X'=Ncal X,

in the original order (y1,y2,z,V). No proper component, source baseline, g lift or H_b term is dropped. This is the exact carrier from the old 13743-byte formal paper and its inherited V2 inputs; the ring is the one explicitly defined in the 14956-byte Kummer paper.

Use the two ring lifts, with the SAME σ on coefficients,

    φ(r)=r^p,       θ(r)=1+(r−1)^p,       Δ=φ(r)−θ(r).

Write Qcal=σ(Ncal), meaning coefficient action only, and

    Nφ=φ'(r) Qcal(φ(r)),       Nθ=θ'(r) Qcal(θ(r)).

The theorem proved below is an explicit T∈GL4(A†), from the θ-pullback solution connection to the φ-pullback one, satisfying

    T'=Nφ T−T Nθ,       T≡I (mod p),       det T=1,       T(0)=I.

It preserves the original filtration and has identity graded maps on z and V. If an actual full comparison Fφ is independently supplied, Fθ=Fφ T transports it in the correct direction and preserves determinant and origin. No such full Fφ is supplied by this theorem. The removed points r=±1 and q=0 are outside the ring: no regular-boundary or full geometric/functional conclusion is claimed.

## 2. Explicit integral presentation bounds

Presentation degree refers to total polynomial degree in r,u,v, using an exhibited representative in O[R,U,V]. It is an upper bound, not an assertion that this representation is unique. The ordinary derivation ∂=d/dr acts by

    ∂r=1,       ∂u=2r u²,       ∂v=−8r v².

It preserves A and increases presentation degree by at most two. It does not lower coefficient p-valuations. The same statements hold after applying σ to coefficients.

The identity S²−1=(r²−1)q² and S'=3q express D as −(1/2)uv times a polynomial matrix of r-degree at most three. Thus D has presentation degree at most five. The w entry has degree at most p+1; H_b(r²) has r-degree at most p−1; the whole bottom row therefore has presentation degree at most 2p. Since 2,3,5 are p-units, every entry of Ncal and Qcal is integral in A and has an exhibited presentation of degree at most 2p. This bound retains all source terms and permits every integral g, including permitted zero cases.

For either ψ=φ or θ, reduction gives ψ(r)=r^p modulo p. Consequently

    f(ψ)=f^p+p aψ,       q(ψ)=q^p+p bψ,

with aψ,bψ∈O[r] of degree at most 2p. These identities imply that the inverted defining polynomials have inverses in A†. More precisely, for any exponent b≥1,

    f(ψ)^(-b)=f^(-pb) sum_(j≥0) (−1)^j binom(b+j−1,j)
                                      p^j aψ^j f^(-pj),

and similarly for q with an index k. The binomial coefficients are integral, so the jth term has valuation at least j and degree at most pb+3pj. For exponent zero the expansion has only its identity term. This proves weak convergence, not just a formal inverse in an unrestricted completion.

It also proves that both lifts extend to A†. Indeed a weak presentation sum_(l≥0) p^l P_l(r,u,v), deg P_l≤C(l+1), after σ and ψ-substitution has terms of valuation at least l+j+k and degree at most pC(l+1)+3p(j+k). Those degrees are bounded linearly by the resulting valuation plus one, with finitely many terms below any fixed valuation. Thus substitution respects the defining weak growth condition. This proof uses σ(p)=p and σ(O)⊂O, not an inverse to σ or an unproved geometric map.

## 3. Taylor coefficients and a complete weak-convergence estimate

Define matrices in A by

    C0=I,       C_(n+1)=∂C_n+C_n Qcal.

Their entries are integral and have presentation degree at most 2pn, by induction using §2. The order C_n Qcal is part of the definition; replacing it by Qcal C_n would generally be wrong.

Since Δ∈pO[r] and deg(Δ/p)≤p−1, define

    T=sum_(n≥0) C_n(θ(r)) Δ(r)^n/n!.

Here and below σ acts only once in Qcal; evaluating C_n at θ(r) is ordinary variable substitution. I prove this full matrix series lies in A†.

Expand each presentation monomial of C_n under θ using the two denominator expansions in §2. Let j,k be the corresponding inverse-expansion indices. Write n!=p^s ε_n with ε_n∈Z_p^×. Every resulting term is an integral polynomial in r,u,v times p^a, where

    a=n−v_p(n!)+j+k,
    degree ≤ p(2p+1)n+3p(j+k).

The n contribution includes the numerator Δ^n/p^n; no factorial denominator is omitted. The inverse expansions add no negative valuation, since their binomial coefficients are integral. Legendre's elementary bound v_p(n!)≤n/(p−1) gives, with β=(p−2)/(p−1),

    a≥βn+j+k,       degree≤3p² a.

For the second inequality one uses 3p²β≥p(2p+1) for p≥5 and 3p²≥3p; the allowed primes satisfy this. For n=0 only C0=I occurs. Below any fixed a there are only finitely many n,j,k and finitely many monomials in the relevant C_n. Grouping these terms by their integral powers of p is therefore a weak presentation with an explicit linear degree bound. This proves T∈Mat4(A†), rather than only T∈Mat4(Ahat).

For n≥1, n−v_p(n!)≥1, so T−I∈pMat4(A†). The estimate also justifies termwise differentiation and finite products: ∂ preserves integral valuation and adds at most two to a presentation degree, and Δ' is still divisible by p. All identities below may first be proved formally over K=O[1/p] and then substituted into the p-adically convergent weak series. No analytic evaluation, local-point computation or numerical radius is used.

## 4. Formal endpoint identity fixes the transport direction

Rename the coordinate to s and put A_s=O[s,(1−s²)^−1,(4s²−1)^−1]. Over A_s⊗K introduce an independent formal increment h. Let U(s+h,s) solve

    ∂_h U=Qcal(s+h) U,       U(s,s)=I.

It exists uniquely coefficientwise in h, since nonzero integers are invertible in K and f(s),q(s) are units. The identity

    ∂_s U=∂_h U−U Qcal(s)

follows without commutativity assumptions on matrices: the difference of the two sides solves ∂_h Z=Qcal(s+h)Z with zero initial value, hence is zero. Comparing h coefficients gives exactly C_(n+1)=C_n'+C_n Qcal. Thus U is the Taylor series in §3 with its correct matrix order.

Substitute s=θ(r), h=Δ(r). The weak estimate proves this substitution is legitimate in A†. The rational expansion of Qcal(s+h) also specializes: its denominators are geometric series around the units f(θ),q(θ), with h=Δ divisible by p; the same generator-degree estimates give linear weak growth. Derivatives and the finite matrix products are locally finite below each p-valuation, so their formal identities survive this specialization. The ordinary chain rule gives

    T'=θ'[Qcal(φ)T−T Qcal(θ)]+(φ'−θ')Qcal(φ)T
      =Nφ T−T Nθ.

Hence T sends a θ-pullback solution column to a φ-pullback solution column. It is not a comparison in the reverse direction, nor is it itself an arithmetic Frobenius on the original carrier.

The trace of the full Ncal is zero: the two proper diagonal entries cancel and the other diagonal entries vanish. Therefore tr Qcal=0. Jacobi's identity in the formal h-ring gives ∂_h det U=tr(Qcal(s+h))det U=0; det U at h=0 is one. Hence det U=1, and the legitimate substitution gives det T=1 in A†. Its adjugate is an inverse in Mat4(A†). In particular no invertibility of φ, θ or σ is assumed.

The recursion preserves the full block pattern. For n≥1 the z row and V column of C_n vanish and there is no proper/z mixing in the quotient modulo V. Thus

    T=[[T_D,0,0],[0,1,0],[t1,t2,t3,1]]

in block sizes 2,1,1, preserving <V>⊂<z,V>⊂A†4; det T_D=1. This is a statement for the full connection, including the bottom proper entries, not a replacement by its isolated kernel.

At r=0 the generators have values r=0,u=1,v=−1, so weak presentations evaluate p-adically in O. Both φ(0) and θ(0) equal zero, and Δ(0)=0. Every positive-n summand vanishes and T(0)=I. No endpoint or target value has been fitted to obtain this normalization.

## 5. Conditional comparison transport and exact limits

Suppose an independently given full matrix Fφ over A†[1/p] satisfies the solution-transport equation

    Fφ'=Ncal Fφ−Fφ Nφ.

Then Fθ=Fφ T satisfies Fθ'=Ncal Fθ−Fθ Nθ by direct differentiation. Conversely Fθ T^-1 gives Fφ. This is a bijection between the two sets of such matrices, not an existence proof for either set. If Fφ is integral or filtration-preserving, the integral T and its inverse preserve that property. Full and proper-quotient determinants and the origin matrix are unchanged. The kernel graded factors are unchanged because T has identity z,V graded maps.

This supplies a target-independent positive change-of-lift arrow on the actual full punctured weak module. The previous raw/log-base obstruction does not prevent it: t is a unit on this locus and its log structure is trivial. The proof nowhere uses a raw lift of the standard integral log base at t=0.

It is essential not to identify A† with K[[t]] or K((t)) at r=1. The p-small increment used for the dagger substitution need not be small in the singular boundary's t-adic expansion. This paper gives neither a regular boundary matrix nor a Laurent boundary expansion of T. It does not turn the saved θ-formal classification into a raw-τ construction, strengthen the old node representative no-go, or produce a new contradiction to geometric/crystalline Frobenius.

No full arithmetic Fφ, complete geometric realization or source-compatible observation was an input proved here. The old isolated Kummer comparison supplies only its own kernel, not a full Fφ to plug into §5. The actual proper finite-level PD matrix is likewise only a proper object until its other realization identifications are supplied. Thus this theorem selects no μ, c, ξ, η, origin k, original source action, global functional or Y, and proves no cup/generic-frame/Rlim/completed-site bridge. Those remain separate genuine obligations.

## 6. Provenance and review status

The exact reused full-carrier primary is in Source3981c60496c24a3c1567677726c136966522d8bf, research_notes/CM24_LOG_RESIDUE_GRADES_REVIEWED_20261015.json: 13743-byte member SHAe17688c59f6d59f4611cbcd0bb518483fa381b2526d3ee82bec3dd61eb75cf5c. The same Source's research_notes/CM24_KUMMER_KERNEL_REVIEWED_20261015.json contains the 14956-byte primary SHAe364fcaa5b5d49d4e5ab6f97f47d34b554289c043583290e20b25f521e59ae85, its ring and prior weak-growth method. Raw/log-base distinctions are actual Sourcef9d00a18506130c15e042dba01c8a4d9770855e9, primary7948B SHA5350ded219800b1ba409185aa235fde44d809c466bcf652e8a5dfbef1353db3b. All were personally consumed with full Source/member byte custody in the prior review; author/input identities remain attributed to their actual authors.

The new increment is the explicit whole-rank-four positive weak-ring transport with its degree bound and orientation, not a claim to invent Taylor transport. Bounded dedup also retained the prior 9986-byte isolated-kernel/two-germ result; neither it nor the θ-formal classification constructs this full weak transfer. No global registry or literature absence is asserted.

Own actual identity, activity gates, prior contributions, direction timing and immutable dependencies are recorded in the accompanying scope/provenance file. This author direction followed preliminary reasoning; it is not blind preregistration. The designated different reviewer BFF6DC received only already existing Source inputs before freeze and supplied no construction or repair. A genuine new nonauthor check is required; I do not review my own new material. No scientific program, Native vote, new Task/run/Tool or old-budget reset occurred. Mother Goal remains OPEN.
