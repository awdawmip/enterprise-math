# Exact parameter fibers and the value of resolving two return branches

Status: PURE_SYMBOLIC_COUNTING_RESULT / SHARED_CONTEXT / NOT_EXECUTED / NOT_ADMITTED.

This unit computes the actual size of the regular free-trace return fibers. It replaces an unspecified hit-rate intuition with exact conditional formulas. The unknown factors appear only in the mathematical analysis, never as inputs to the proposed native program. No numerical table, random sampler or scientific reference run was used.

## 1. The two geometric parameter families

Fix an odd prime p and a positive public integer E. A regular parameter is k in F_p with k^2-4 nonzero; there are p-2 such parameters. The roots lambda,lambda^-1 of X^2-kX+1 lie either in F_p^*, of order p-1, or in the norm-one subgroup of F_(p^2)^*, of order p+1. Both groups are cyclic. Their intersection consists of 1 and -1, which give the excluded parameters 2 and -2.

Every remaining inverse pair gives one k. A split trace and a nonsplit trace cannot coincide, since the quadratic polynomial determined by k already specifies its roots. Thus counting regular traces is exactly counting inverse pairs in these two cyclic groups with the two exceptional roots removed separately from each group. In particular the split and nonsplit parameter counts are (p-3)/2 and (p-1)/2; their sum is p-2.

The finite-field facts used here are standard. Actual primary teaching sources read for this unit were Andrew Sutherland's MIT 18.782 Lecture 3, theorem 3.3 and its finite-field discussion (https://math.mit.edu/classes/18.782/2023sp/LectureNotes3.pdf), and the Rutgers finite-field notes, sections 2.11 and 2.13 (https://sites.math.rutgers.edu/~sk1233/courses/finitefields-F19/intro.pdf). They supply cyclicity and the norm map; the trace-fiber and branch-resolution formulas below are derived here. No current computational-complexity claims from those older notes are adopted.

## 2. Exact signed return counts

Let A_p(E) be the number of regular k with M(k)^E=I, and B_p(E) the number with M(k)^E=-I. Define

    c_plus(E) = 1 + indicator(E even),
    c_minus(E) = indicator(E odd),
    d_L(E) = gcd(E,L),
    h_L(E) = d_L(E) if L/d_L(E) is even, and 0 otherwise.

Then

    A_p(E) = [d_(p-1)(E)+d_(p+1)(E)-2*c_plus(E)]/2,
    B_p(E) = [h_(p-1)(E)+h_(p+1)(E)-2*c_minus(E)]/2.

In a cyclic group of order L the equation lambda^E=1 has exactly d_L(E) solutions. Among the exceptional roots it contains 1, and also -1 precisely when E is even. Removing those roots in both groups and pairing inverses gives the A formula.

For lambda^E=-1, write a cyclic generator as g and solve E*j=L/2 modulo L. This congruence has d_L(E) solutions exactly when d_L(E) divides L/2, equivalently when L/d_L(E) is even. Among the exceptional roots only -1 can solve it, and only for odd E. Removing and pairing again gives B. Distinctness of the eigenvalues makes these scalar conditions equivalent to the stated companion matrix equalities.

As a useful check in symbolic form, the two signed sets are disjoint and their union is the return set for exponent 2E. Therefore

    A_p(E)+B_p(E)
       = [gcd(2E,p-1)+gcd(2E,p+1)-4]/2.

For a uniform admitted k, divide A or B by p-2 to obtain its exact local signed-return probability. A distribution induced by choosing a uniform eigenvalue, a preselected k, or an adaptive parameter rule is different and must not reuse this probability without a proof.

## 3. The two-clock fiber is a disjoint union

Fix either sign epsilon. Put C_p(E)=A_p(E) for the positive sign or B_p(E) for the negative sign. The regular return sets at E and E+2 are disjoint. Simultaneous signed return would imply M^2=I and lambda^2=1, contrary to regularity.

By the reviewed two-clock section theorem, the scalar condition

    V_(E+1)-epsilon*k=0

therefore has exactly C_p(E)+C_p(E+2) admitted roots. Define

    a_p=C_p(E)/(p-2),
    b_p=C_p(E+2)/(p-2),
    c_p=1-a_p-b_p.

These are the probabilities of the mutually exclusive labels E-return, E+2-return, and neither. This records branch identity, rather than replacing the two return fibers by their Boolean union.

## 4. An exact separation gain from keeping the branch label

Let N=pq for distinct odd primes, and condition a uniform k modulo N on gcd(k^2-4,N)=1. CRT gives independent uniform admitted local parameters. Setup/rejection work and possible setup factors are outside this conditional experiment and remain charged by any full algorithm.

If only the union gcd gcd(N,V_(E+1)-epsilon*k) is retained, its proper-factor probability is

    P_union=(a_p+b_p)*c_q + c_p*(a_q+b_q).

If the two primitive branch divisors are retained separately, via the marked common gcd and an actually paid exact quotient, a proper factor is obtained precisely when the two local labels differ. Hence

    P_resolved=1-(a_p*a_q+b_p*b_q+c_p*c_q),
    P_resolved-P_union=a_p*b_q+b_p*a_q.

The extra term is exactly the case where the scalar union gcd saturates but the two different return clocks separate the components. This is a positive mathematical use of the BRC branch/provenance requirement: preserving the two labels can increase the success of this specified readout even over a squarefree modulus. It is distinct from unsquaring a single primitive return depth, which by itself adds no squarefree support.

These formulas concern one fixed sign and exactly the declared conditional law. Trying both signs has additional correlations and must not be assigned independent success probabilities. Prime-power depth distributions, adaptive schedules and complete multi-step first-hit laws also require separate analysis. No such sampler or branch-quotient experiment was executed for this note.

## 5. What remains hard about choosing the clocks

For small numerical E the counts are bounded by its size: A_p(E) is at most E-c_plus(E), and B_p(E) at most E-c_minus(E). Thus the two-clock count for either fixed sign is at most 2E+2, before capping by p-2. A fixed collection of small numerical clocks has a small large-prime fiber by the union bound. This is not a bound in log(E), and does not rule out a large exponent encoded with few bits.

For large E the exact formulas identify the useful condition: substantial divisors shared by E (or its signed variant) and one or both of p-1,p+1. Choosing E without knowing p, while keeping its bit length, construction, attempts and native evaluation inexpensive, is still an unsolved part of this research. Renaming those gcds as geometric resonance does not supply the selector. Neither does the conditional probability calculation allow p or q to be queried for free.

The concrete new result is an exact fiber count and an exact branch-resolution benefit under a stated distribution. The forthcoming native experiment can verify its local observer and readout implementation on the predeclared fixtures. It cannot establish these probability laws empirically from four selected small inputs, nor turn them into a generic Shor completion.

Dependencies: the regular free-trace torus, primitive signed-return, translated-trace and two-clock proofs already frozen in the preceding source milestones. This note does not change their source, run or cost records.

Global-Knowledge-Sync: main@8c23cca / GLOBAL_KNOWLEDGE_V1
