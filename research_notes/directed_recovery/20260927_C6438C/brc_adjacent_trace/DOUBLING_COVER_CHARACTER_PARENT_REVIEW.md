# Parent review of the doubling-cover character

Status: PASS / FULL_TEXT_PURE_SYMBOLIC_REVIEW / SHARED_CONTEXT / NOT_EXECUTED / NOT_ADMITTED.

The root coordinator read the complete DOUBLING_COVER_CHARACTER.md at SHA-256 1a1fc07a5e69abc10756538b46bc14be0e74c5c0d2f88af7886f5a4b86d97e94. This is a separate symbolic review. No character calculation, parameter scan, root construction or scientific reference computation was executed.

The character identity is correct in both local tori. In the split group it follows from k+2=(lambda+1)^2/lambda and Euler's criterion. In the nonsplit group, Frobenius gives (lambda+1)^(p-1)=lambda^-1 and Norm(lambda+1)=k+2. The resulting exponent is the inverse of the torus sign, which equals itself. Thus Legendre(k+2) is precisely the torus square-class character and is invariant under lambda inversion.

The half-trace statement correctly restricts to regular target k. Its two candidate roots h and -h are nonzero and regular, and their discriminant has the same type as the target because Legendre(k+2)=+1. The two-to-one statement concerns these regular target fibers; it must not be extended to the h=0 source whose target is the excluded trace -2. Choosing a half-trace remains an extra operation. The global Jacobi sign only multiplies local labels and does not expose an individual local sign or construct a root.

For a cyclic order 2^t*m, nonsquareness is equivalent to maximal 2-primary order. The count in equation (4) correctly retains every odd component and removes -1 exactly for t=1. After the odd-order condition is satisfied, the sign is negative at s=t-1 and positive at s>=t. When the denominator vanishes the class is empty, as stated. The rate therefore still depends on gcd(B,m)/m and cannot silently turn a dyadic cover into an odd-order selector.

Forward doubling gives the next plus-two trace as an actual square, so it does not generate independent new square-class bits. The distinction between local square-class data, the two observable global Jacobi products, and the unknown local factorization is maintained. The third character from k-2 is their product and has no independent information under the admitted unit hypothesis. Even multiplicities in a nonsquarefree N invalidate the two-prime interpretation, and the note explicitly keeps that boundary.

No mathematical correction is required within this scope. The proposed native record can reuse the generic typed Jacobi primitive but has not been integrated or benchmarked. Conditioning on both global characters changes the parameter law; existing unconditional or single-filter probabilities must be recalculated before use. This is a useful observable of the geometric doubling cover, not a root oracle or a closure of the unknown odd-order problem.

Global-Knowledge-Sync: main@8c23cca / GLOBAL_KNOWLEDGE_V1.
