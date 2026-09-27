# A computable character of the HBW doubling cover

Status: PURE_SYMBOLIC_TOOL_CANDIDATE / SHARED_CONTEXT / NOT_EXECUTED / NOT_ADMITTED. This is a separate proof after the adjacent-trace run. It changes no frozen source, experimental grid or recorded cost. It reuses quadratic characters and Lucas/Chebyshev structure; it does not claim those classical ideas as new.

## 1. The local character is the same in both tori

Let p be an odd prime, k a regular trace, Delta=k^2-4 nonzero, and sigma=(Delta|p). The root lambda of X^2-kX+1 belongs to the cyclic torus T of order L=p-sigma: F_p^* in the split case, or the norm-one subgroup of F_(p^2)^* in the nonsplit case. The choice lambda versus lambda^-1 will not affect any statement below. Regularity excludes lambda=1,-1 and makes k+2 and lambda+1 nonzero.

Define the torus square-class character chi_T(lambda)=lambda^(L/2), a value in {1,-1}. Then

    (k+2 | p) = chi_T(lambda).                                      (1)

For the split torus, k+2=(lambda+1)^2/lambda, and Euler's criterion gives the equality directly, since lambda^((p-1)/2) is its own inverse.

For the nonsplit torus, lambda^p=lambda^-1. Therefore

    (lambda+1)^(p-1)=lambda^-1,
    k+2=(lambda+1)^(p+1).

Raising the second identity to (p-1)/2 gives lambda^(-(p+1)/2), which equals lambda^((p+1)/2) because its square is one. This proves (1) without choosing a square root in the nonsplit extension. These are symbolic field identities, not an algorithm permitted to know p or lambda.

Thus this second character describes the element within its torus, while (Delta|p) describes which torus it occupies. Merely renaming the conic norm does not give this information: all coherent states have the same conic norm. The character refers to the double-cover fiber of the trace parameter.

## 2. Exact double-cover fiber and its branch boundary

The trace of lambda squared is k^2-2. Conversely a half-trace h for k must satisfy

    h^2-2=k, or h^2=k+2.                                           (2)

If (k+2|p)=-1 there is no half-trace over F_p and lambda is not a square in T. If it equals +1, (2) has exactly two roots h and -h. They are nonzero because k is regular. They are also regular traces: h=±2 would imply k=2. Their discriminant is h^2-4=k-2, and

    (k-2|p)=(Delta|p)(k+2|p)=sigma.

Hence both roots describe the same torus type as lambda. Each lifts to a torus element mu with mu^2 equal to lambda or lambda^-1. The two half-traces correspond to the two sign choices mu and -mu after quotienting by inversion. Choosing one h is extra branch information; a character only counts its existence and does not recover the branch.

On the inverse-pair carrier this is a two-to-one map onto the square-class fiber, not an invertible rechart. A current character alone therefore does not license arbitrary future halving, branch deletion or orientation folding. The existing E+2 versus E-2 observer distinction continues to apply.

For the forward doubling map, the next trace k'=k^2-2 satisfies k'+2=k^2. Whenever k is nonzero the next character is +1. If k=0, the next trace is the excluded value -2. Consequently repeated forward squaring cannot create a fresh independent square-class bit: the later +1 values follow algebraically. The useful bit concerns a declared preimage layer; it is not an unlimited supply of factor information.

## 3. Exactly what it says about order, including the odd part

Write L=2^t*m with t>=1 and m odd. If lambda=g^j for a generator g of T, then chi_T(lambda)=(-1)^j. Therefore

    chi_T(lambda)=-1  iff  v_2(ord(lambda))=t.                       (3)

The +1 class only implies a smaller 2-primary order. It does not reveal its exact depth without further information. Neither class alone identifies the odd component of the order.

This limitation has an exact useful form. Consider a mathematically uniform regular trace within this fixed torus and its nonsquare class. Let B be a positive odd public integer and E=2^s*B, s>=0. Conditional on this class being nonempty, the probability of either signed return lambda^E=±1 is zero if s+1<t. Otherwise it is

    [2^(t-1)*gcd(B,m)-indicator(t=1)]
    ------------------------------------------------------------. (4)
    [2^(t-1)*m       -indicator(t=1)]

Proof: CRT identifies the cyclic group with its 2-primary and odd components. Nonsquareness forces an odd exponent in the 2-primary component, giving 2^(t-1) choices, and leaves all m odd components available. The condition lambda^(2E)=1 requires the odd component to have order dividing B, giving gcd(B,m) choices. The element 1 is never nonsquare. The exceptional regularity exclusion -1 belongs to this class exactly when t=1 and must be removed once from numerator and denominator. Inverse pairing divides both counts by two. If the denominator is zero the admitted class is empty, and no conditional probability is asserted.

At s=t-1 every successful return in (4) is negative; at s>=t it is positive. This follows because the 2-primary component has full order 2^t and B is odd. When s<t-1 there is no signed return. These signs apply after the odd component is actually killed, not merely after identifying the character.

In particular, for a nonsplit Blum-prime component, t=v_2(p+1)>=2 and the regular nonsquare-class rate is exactly gcd(B,m)/m once the public clock contains enough powers of two. With B=1 it is 1/m. The filter gives a precise covering branch and maximal 2-primary order but cannot make a large unknown odd m disappear. This is a conditional counting statement, not an implemented sampler, hidden order input or hardness theorem.

## 4. What a factor-blind global observer actually sees

For an odd N with paid gcd(Delta,N)=1, both k+2 and k-2 are units. The existing typed Jacobi primitive can compute

    J_D=Jacobi(Delta,N),  J_+=Jacobi(k+2,N).

Its numerator must be linked to the actual typed modular producer. Exact addition/reduction, character computation, source admission, any rejected proposals and final factor divisions all remain paid. No new call to this primitive occurred here.

For the explicitly promised squarefree semiprime N=pq, these two signs are

    J_D=sigma_p*sigma_q,
    J_+=chi_(T_p)(lambda_p)*chi_(T_q)(lambda_q).

Thus J_+=-1 proves that exactly one local element admits a half-trace in its own torus. It neither identifies that prime nor constructs its half-trace. J_+=+1 cannot distinguish both square from both nonsquare. Together J_D and J_+ distinguish parity of torus types and parity of covering classes; they are not the four local signs themselves. The additional Jacobi(k-2,N) is their product and supplies no independent bit.

On a prime-power composite, Jacobi weights the local characters by the exponents in N. Even exponent factors disappear from that product. The geometric identities still hold locally at good odd primes, but the two-component interpretation above cannot be extended to repeated primes or arbitrary factorizations without a new theorem.

The global minus sign is also a certificate that (2) has no root modulo the squarefree N: a nonsquare component forbids one. It is not a square-root procedure. If some stronger tool supplied different genuine roots or localized the unsplit covering branch, a gcd might separate components, but that extra operation and its cost must be proved and implemented. It cannot be assumed as a cheap geometric lift.

## 5. A concrete next native interface and the remaining research question

A bounded successor could expose a TorusCoverCharacter record containing the actual typed k, Delta, k+2 residues, their shared producer links, both exact Jacobi certificates, regularity/factor status, and the public exponent/proposal policy. It would compose with the existing ordered adjacent-trace readout. This is reuse of the generic typed_jacobi_trace interface pinned in JACOBI_TORUS_SELECTOR.md, not reuse of that old module's unrelated QFT final-bit theorem. The prototype's double-cover character has not been integrated or benchmarked.

Its meaningful verification target would be a predeclared family-level contract, not another favorable fixed k: all rejected parameters and both character classes must be retained; the output must distinguish observable global signs from unobserved local signs; any success statement must name its input promise and sampling law. The current result supplies exact identities (1)-(4), not such a complete implementation.

The central next tool obligation is a public odd-cofactor schedule or a further observable geometric covering that gives information about the unknown m, with a costed and sound separation certificate. Formula (4) makes this target measurable: a claim of useful rate must explain why gcd(B,m)/m is large often enough, without receiving m or factoring p±1. Adding odd factors to B without paying their construction and bit length, or declaring a cheap inverse cover, does not meet that obligation. Standard Lucas p±1 and elliptic-curve methods remain the appropriate prior-art comparison; no new generic advantage or Shor completion follows here.

This proposal is compatible with the current public-clock and exact-fiber analyses, but does not change their frozen formulas or treat a new character as independent random evidence. In particular, filtering by both Jacobi values changes the conditional law of k and requires recalculating the relevant fiber counts before quoting a hit rate.

Dependencies read: TRANSLATED_TRACE_MARK.md a3562a0b3151c86a7d5c1767af876daafa245ea7426da7dc387c70f0db9f0c6c; ADJACENT_TRACE_HBW_GEOMETRY.md 3b8083eb0ecddc1c12406cd64113ce3e2bb88ee676a0e7b8fd3f7c6289511e14; EXACT_TRACE_PARAMETER_FIBERS.md 88bb76916b9d844d5763d4120668ac85531005155cf36e8bb33a44d829894dd9; JACOBI_TORUS_SELECTOR.md 30fc0de14df7eef7f43c30838fbe1dd47c60db85982ac5d92bfc0c863d2cdf2f. The last note's existing typed Jacobi source pin is a reuse locator, not a new execution or a fresh source audit by this proof unit.

Global-Knowledge-Sync: main@b304760 / GLOBAL_KNOWLEDGE_V1
