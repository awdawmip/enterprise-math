# Exact trace parameter fibers: shared-context symbolic review

Result: **PASS / FULL_TEXT_PURE_SYMBOLIC_REVIEW / NOT_EXECUTED / NOT_INDEPENDENT_ADMISSION**.

Reviewed the complete EXACT_TRACE_PARAMETER_FIBERS.md at SHA-256 **88bb76916b9d844d5763d4120668ac85531005155cf36e8bb33a44d829894dd9**. The review checked both signed formulas, exceptional-root removal, the disjoint two-clock fibers and the three-label conditional CRT probability. No scientific program, numerical table, sampler, paid professional query or remote write was performed. This is a separate shared-context review for the adjacent-trace successor, outside the already frozen elliptic package.

## Parameter counting and signed fibers

The split/nonsplit classification is exhaustive for regular k. An eigenvalue of the regular quadratic either lies in F_p^* or has Frobenius conjugate lambda^p=lambda^-1 in F_(p^2), so belongs to the norm-one group. Conversely every such group element supplies a trace in F_p. Their intersection is exactly {1,-1}: for an element of F_p^*, the quadratic norm is its square. Removing these two roots removes precisely the repeated-root traces k=2 and k=-2.

The map lambda to lambda+lambda^-1 has fibers of exactly two outside {1,-1}; its roots are already determined by the trace polynomial. Consequently a regular split trace cannot also be nonsplit, and the family sizes (p-3)/2 and (p-1)/2 are correct. A uniform choice of regular k is therefore uniform on the p-2 inverse pairs, not the law produced by choosing uniformly in either eigenvalue group without the proper weighting.

In a cyclic group of even order L, the equation lambda^E=1 has d=gcd(E,L) solutions. Its exceptional roots are 1 always and -1 exactly for even E. Removing those exceptions separately from both groups and dividing by two proves the displayed A_p(E) formula. There is no additional fixed inverse pair after removal.

For the negative sign, writing lambda=g^j reduces the equation to E*j=L/2 modulo L. Its solvability condition d divides L/2 is exactly that L/d be even; when soluble it has d solutions. Only the exceptional root -1 can occur, and only for odd E. This gives precisely the proposed h_L(E), c_minus(E) and B_p(E). Inversion preserves the signed solution set because epsilon^-1=epsilon.

Distinct eigenvalues ensure that these eigenvalue conditions are equivalent to the full matrix equality M(k)^E=epsilon*I. The two signs are disjoint in odd characteristic. Their union consists of lambda^(2E)=1, so the check

    A_p(E)+B_p(E)
      = [gcd(2E,p-1)+gcd(2E,p+1)-4]/2

also follows directly by removing both exceptional roots from each group. The formulas remain meaningful at the smallest allowed odd prime; no unstated p>3 assumption is needed for the count theorem.

## Two clocks and conditional CRT probabilities

For a fixed sign, simultaneous E and E+2 return would give M^2=I after multiplication by the inverse of M^E. Regularity excludes its eigenvalue possibilities lambda=±1. Thus the two signed return fibers are disjoint, and the reviewed translated-section product theorem gives exactly their union as the scalar zero set.

The labels with masses a_p, b_p and c_p are therefore mutually exclusive and exhaustive. Their probabilities are valid specifically for a uniform regular k. For N=pq with distinct odd primes, conditioning uniform k modulo N on regularity gives the Cartesian product of the two local regular sets, hence independent uniform local parameters. This justifies multiplication of the local label masses. It does not justify unconditioned rates, a free rejection sampler, use of unknown p/q as program inputs, or independent rates for the two different signs.

For the union observer, the only proper-factor label pairs are return/neither and neither/return. This yields

    P_union=(a_p+b_p)c_q+c_p(a_q+b_q).

For separately retained branch divisors, equal labels give both components on the same branch or outside both, hence only saturated/unit outputs. Unequal labels give a proper divisor from at least one branch. The complement of the three equal-label events is exactly

    P_resolved=1-a_p*a_q-b_p*b_q-c_p*c_q.

The two unequal-return label pairs were excluded by the union observer because its gcd is N. Adding exactly those events gives

    P_resolved-P_union=a_p*b_q+b_p*a_q.

No double counting or unmentioned independence assumption enters this difference. The gain is nonnegative and can be strictly positive; the note correctly does not claim it is positive for every choice of primes, exponent and sign. It is an exact comparison between the two declared output observations, not merely a valuation change within the same return branch.

The stated exact quotient is appropriate when the output contract explicitly retains the second primitive branch divisor. For the weaker goal of finding any factor, the first branch gcd itself is already proper in the mixed-return event; an implementation could stop there under a separately declared early-stop contract. This is a nonblocking implementation distinction. It neither changes the stated probabilities nor permits deleting costs from the forthcoming already specified two-divisor comparison.

The formulas are limited to squarefree two-prime N and the given conditional law. Prime-power depth, more prime components, adaptive parameter choices, both-sign correlations and multi-step stopping laws need their own analysis, as the note states.

## Clock size and research scope

The bounds follow from gcd(E,L) <= E and h_L(E) <= E, so A_p(E) <= E-c_plus(E) and B_p(E) <= E-c_minus(E). Summing the E and E+2 bounds gives the stated looser maximum 2E+2, capped by the p-2 admitted parameters. A finite collection of small numerical exponents then has the claimed union-bound limitation.

This is a bound in the numerical value E, not a lower bound in its encoding length. It does not exclude large compactly represented exponents with substantial gcd against unknown p-1 or p+1. Choosing and evaluating such exponents cheaply, paying admission and repeated attempts, and proving overall separation remain explicit open obligations. The exact local formulas do not turn the factor p into an available oracle.

The result establishes an exact conditional benefit from preserving return-branch identity. It does not establish a new general factoring algorithm, an advantage over classical Lucas/collision methods, a global sampling theorem or Shor completion. Selected small implementation fixtures can validate the observer wiring but cannot empirically establish the probability law.

## Primary-source check

This reviewer actually opened the two cited teaching sources. Sutherland's theorem 3.3 states the standard cyclicity result for a finite multiplicative subgroup of a field; the surrounding finite-field section supplies the setting used here. The PDF itself is labeled Fall 2013 even though its URL is under a 2023sp directory; the proof does not depend on a contemporary complexity assertion. Source: [Sutherland, 18.782 Lecture 3](https://math.mit.edu/classes/18.782/2023sp/LectureNotes3.pdf).

The Rutgers notes, sections 2.11 and 2.13, supply cyclicity and the norm exponent/surjectivity formula. Specializing the norm from F_(p^2) to F_p gives a cyclic kernel of order p+1, as required. This review uses only those standard facts, not the notes' computational open-problem discussion. Source: [Rutgers, Introduction to finite fields](https://sites.math.rutgers.edu/~sk1233/courses/finitefields-F19/intro.pdf).

No correction is required within the reviewed scope. The exact count theorem, branch-resolution formulas and continuation limits are suitable for the next independent source milestone.

Global-Knowledge-Sync: reviewer actual canonical read lease main@4ae9f3f / GLOBAL_KNOWLEDGE_V1; the reviewed author's historical marker remains unchanged.

