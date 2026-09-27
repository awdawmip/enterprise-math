# Exact regular-trace fibers under two quadratic characters

Status: **PURE_SYMBOLIC_RESULT / SHARED_CONTEXT / NOT_EXECUTED / NOT_ADMITTED**.
Author context: EM-DIRECT-C6438C, activity RA-CAAAC604CB513AEA8BBC1DFC. This is a new, separate proof unit. It changes no adjacent-trace source, experiment or publication package. There was no scientific execution, numerical table, provider query or new factoring experiment.

The result is a probability contract for a proposed joint filter. It gives the sizes of all four local character classes and the exact signed-return counts within each. It then mixes the classes under two observable global Jacobi signs. Neither an unknown factor nor an unknown order is an algorithm input. Those quantities occur only in the analysis of a declared sampling law.

## 1. Domain and character coordinates

Fix an odd prime r. A regular trace k in F_r satisfies k^2-4 != 0. Define

    sigma = (k^2-4 | r),   eta = (k+2 | r),   alpha_r = (-1 | r).

Both sigma and eta are in {+1,-1}. In particular regularity excludes k=2,-2 and makes both k+2 and k-2 nonzero. The local companion is

    M(k) = [[0,1],[-1,k]].

For a fixed type sigma, its eigenvalue lambda lies in a cyclic group of even order

    L = r-sigma:
    sigma=+1: F_r^*;
    sigma=-1: the norm-one subgroup of F_(r^2)^*.

The regular traces of this type are precisely the inverse pairs of lambda in this group with lambda=1,-1 removed. Each remaining pair has size two. Let lambda=g^i for a generator g, with i taken modulo L. The second character is

    eta = lambda^(L/2) = (-1)^i.                         (1)

For completeness, k+2=(lambda+1)^2/lambda. In the split case Euler's criterion proves (1) directly. In the nonsplit case lambda^r=lambda^-1 and (lambda+1)^(r-1)=lambda^-1. Raising the displayed expression for k+2 to (r-1)/2 gives lambda^(-(r+1)/2), which equals lambda^((r+1)/2). This also proves (1). Inversion preserves exponent parity because L is even. No choice of eigenvalue orientation affects either character.

These are proof coordinates only. The implemented observer would retain its actual ordered adjacent traces; neither lambda, g, r nor a root of the discriminant is supplied to it.

## 2. Four exact local class sizes

Put h_L=(-1)^(L/2), and use [condition] for the indicator of a statement. The number of regular trace parameters in class (sigma,eta) is

    C_r(sigma,eta)
       = (L/2 - [eta=+1] - [eta=h_L])/2
       = (r-2-sigma-eta-alpha_r*sigma*eta)/4.            (2)

There are L/2 exponents of each parity. The removed eigenvalue 1 has character +1; the removed eigenvalue -1 has character h_L. Removing them and then dividing by two for inversion gives the first expression. The identity h_L=alpha_r*sigma gives the second expression. Thus the apparently fractional expressions are nonnegative integers, by an explicit inverse-pair count.

An equivalent table is:

| Prime class | C(+,+) | C(+,-) | C(-,+) | C(-,-) |
|---|---:|---:|---:|---:|
| r = 1 mod 4 | (r-5)/4 | (r-1)/4 | (r-1)/4 | (r-1)/4 |
| r = 3 mod 4 | (r-3)/4 | (r-3)/4 | (r-3)/4 | (r+1)/4 |

The row sums are r-2. Summing eta recovers (r-3)/2 split traces and (r-1)/2 nonsplit traces. A class of size zero is an empty class, not a distribution with a zero denominator. In particular at r=3 the only class is (sigma,eta)=(-1,-1), of size one. At r=5 the (+,+) class is empty. These are symbolic boundary consequences of (2), not scientific test fixtures.

## 3. Arbitrary public exponent and both signed returns

Let E be any fixed nonnegative integer. Positive exponents are the intended clock domain; allowing E=0 makes the boundary explicit. Define gcd(0,L)=L and put

    g_E = gcd(E,L),     a_E = L/g_E.

First count eigenvalues before removing 1,-1. For the positive equation lambda^E=1, define

    B_+(L,E,eta) = g_E/2                  if a_E is odd,
                   g_E * [eta=+1]        if a_E is even.           (3)

For the negative equation lambda^E=-1, define

    B_-(L,E,eta) = 0                                      if a_E is odd,
                   g_E * [eta=(-1)^(a_E/2)]               if a_E is even. (4)

The exact regular-trace signed counts in the class are

    T_r^+(sigma,eta;E)
      = (B_+(L,E,eta) - [eta=+1] - [E even]*[eta=h_L])/2,

    T_r^-(sigma,eta;E)
      = (B_-(L,E,eta) - [E odd]*[eta=h_L])/2.             (5)

These are counts of M(k)^E=I and M(k)^E=-I, respectively. They obey

    0 <= T_r^+ + T_r^- <= C_r,
    U_r(sigma,eta;E) = C_r - T_r^+ - T_r^- >= 0.         (6)

Proof of (3): E*i=0 modulo L has i=a_E*t for 0<=t<g_E. If a_E is even all exponents are even. If a_E is odd, g_E is even because L is even, and exactly half the exponents have each parity.

Proof of (4): E*i=L/2 modulo L is soluble exactly when g_E divides L/2, equivalently when a_E is even. Then (E/g_E)*i=a_E/2 modulo a_E. The coefficient E/g_E and its inverse modulo the even modulus a_E are odd, so every solution has parity equal to a_E/2. Adding a_E does not change parity; there are g_E solutions. The a_E=1 boundary is in the insoluble case and needs no modular inverse.

For (5), lambda=1 is always a positive solution and never a negative one. The eigenvalue -1 is positive exactly when E is even and negative exactly when E is odd. Its character is h_L. Remove these exact exceptional solutions in their actual classes, then pair inverses. Regularity makes the matrix diagonalizable over its splitting field, so the scalar and full-matrix signed conditions are equivalent. The two signed sets are disjoint in odd characteristic, proving (6).

There is no conditional probability assigned to C_r=0. If C_r>0, the three probabilities are T_r^+/C_r, T_r^-/C_r and U_r/C_r. A fixed sign uses its own count; trying both signs does not create independent trials.

Boundary checks follow symbolically. At E=0, (3)-(5) give T^+=C and T^-=0. At E=1 both counts are zero because only the excluded eigenvalues could return. For the sole r=3 class, a clock congruent to 0 modulo 4 gives a positive return, one congruent to 2 modulo 4 gives a negative return, and an odd clock gives neither. The formulas apply without special algorithmic cases for these boundaries. Negative integer exponents, if ever needed, have the same signed-return sets as their absolute values, but their execution contract is not introduced here.

## 4. Global filters and their exact dependence

Now suppose mathematically that N=pq for distinct odd primes. This is a theorem-domain promise, not a conclusion inferred by a Jacobi routine. Draw k uniformly modulo N, condition on regularity, and impose two fixed observable signs

    J_D = Jacobi(k^2-4,N) = j,
    J_+ = Jacobi(k+2,N) = e,               j,e in {+1,-1}.

Only after the complete regularity/character certificates are available does this conditional experiment describe an accepted proposal. Set

    R = (p-2)(q-2),       alpha = alpha_p*alpha_q = Jacobi(-1,N).

For each choice (sigma,eta) at p, the only compatible class at q is (j*sigma,e*eta). Its count weight is

    W_(sigma,eta) = C_p(sigma,eta)*C_q(j*sigma,e*eta).

The accepted regular count is

    Z_(j,e) = sum_(sigma,eta) W_(sigma,eta)
            = (R + j + e + alpha*j*e)/4.                 (7)

The four orientation weights are W/Z, restricted to nonzero W. Within such an orientation the local trace parameters are independent and uniform in their specified classes. Zero-weight orientations contribute zero to sums; their conditional laws are not constructed.

To prove the last equality without an independence assumption for the two characters, (2) gives the local sums over regular k:

    sum 1 = r-2,    sum sigma = -1,    sum eta = -1,
    sum sigma*eta = -alpha_r.

The indicator of the two global sign constraints is

    (1+j*sigma_p*sigma_q)*(1+e*eta_p*eta_q)/4.

Summing this indicator over the regular CRT product gives (7). Thus acceptance conditional on regularity is Z/R, and acceptance from uniform proposals over all N residues is Z/(pq). Costs of nonregular candidates and any factors found during setup remain outside that conditional-return probability and inside the actual algorithm's ledger.

The two global signs are not independent random bits. Under uniform regular k,

    E[J_D]=E[J_+]=1/R,
    E[J_D*J_+]=alpha/R,
    Cov(J_D,J_+)=(alpha*R-1)/R^2.                        (8)

For distinct odd primes R>1, so this covariance is nonzero. Some particular conditional signs can nevertheless be balanced. For example, if alpha=+1 and j=-1, the two values of e have equal conditional weight. That special conditional balance does not establish global independence or reveal the four local signs.

An accepted class can be empty: always test Z>0 before assigning a conditional probability. With p=3, the unique local class forces the compatible q class; a zero q class produces Z=0. No averaging formula silently fills in that empty event.

## 5. Exact factor-output law under the joint filter

Fix an E that is constant on the accepted (j,e) class. It may be an explicitly constructed function of the public N,j,e and public schedule parameters. It may not depend on the unobserved local orientation. For each orientation abbreviate

    C_p=C_p(sigma,eta),  C_q=C_q(j*sigma,e*eta),
    A_p=T_p^+(sigma,eta;E), B_p=T_p^-(sigma,eta;E),
    A_q=T_q^+(j*sigma,e*eta;E), B_q=T_q^-(j*sigma,e*eta;E),
    U_p=C_p-A_p-B_p,     U_q=C_q-A_q-B_q.

Assume Z>0. For a single sign epsilon, put H_p=A_p or B_p and H_q=A_q or B_q as appropriate. The exact four output probabilities of the primitive signed divisor are

    Pr(D_epsilon=1) = sum (C_p-H_p)*(C_q-H_q) / Z,
    Pr(D_epsilon=p) = sum H_p*(C_q-H_q) / Z,
    Pr(D_epsilon=q) = sum (C_p-H_p)*H_q / Z,
    Pr(D_epsilon=N) = sum H_p*H_q / Z,                   (9)

where every sum is over the four orientations. The p and q labels occur only in this analysis; the actual readout is its computed divisor and an exact division certificate. These count formulas use no conditional division by C_p or C_q, so empty local classes are handled automatically.

If both signed main observers are evaluated, the local categories are positive, negative and neither. Their complete joint law in an orientation is the product of the corresponding category counts, then mixed by 1/Z. A proper factor is obtained exactly when the two local categories differ. Consequently

    Pr(at least one proper main-clock factor)
       = 1 - sum (A_p*A_q + B_p*B_q + U_p*U_q)/Z.        (10)

The positive/negative mixed categories yield two proper signed outputs. Simultaneous positive returns or simultaneous negative returns give a saturated divisor and no proper factor from these two main observers. These correlations are why multiplying independent success probabilities is invalid.

For one fixed sign and the two clocks E,E+2, the same formulas also give a branch-aware law. The local counts T_r^epsilon(E) and T_r^epsilon(E+2) are disjoint within every character class: a common regular solution would imply lambda^2=1. Replace A,B above by these two counts and U by their complement. This gives the exact law of the marked first divisor and paid exact second-clock quotient under the joint filter. It does not make all four sign/clock events disjoint: opposite signs at clocks differing by two can overlap at fourth roots, and need a separate joint count if all are combined.

## 6. Public clocks and what remains unknown

The previously proved public clock E=N-j is admissible in this contract because it is fixed on the accepted j class. In each compatible orientation its group orders satisfy

    gcd(E,L_p)=gcd(E,L_q)=gcd(L_p,L_q)=d.

Thus one inserts the common d into (3)-(5), while retaining eta-specific restrictions. The coprime quotients L_p/d and L_q/d cannot both be even. By (4), both components cannot return negatively; further conditioning on e cannot create an event already impossible pointwise. The negative main divisor therefore remains nonsaturating in the squarefree two-prime domain. This reuses the existing public-clock theorem, rather than claiming a new clock construction.

A mixed public exponent, for example E=2^s*B with a specified odd B, is handled by the same formulas with its actual gcd(E,L_r). A joint character constrains parity of the cyclic exponent, but does not reveal or remove its odd-order component. The analysis does not let an algorithm obtain L_p,L_q,d or their factorizations for free. Exact probabilities here may remain numerically unevaluable to a factor-blind program; they are a valid theoretical contract and a target for further bounds, not a rate oracle supplied to production.

If E is chosen adaptively from other observations of k, the conditional distribution can change within a character class. Equations (9)-(10) cannot simply be reused: one must partition by the full selection rule or prove the resulting law. Likewise, repeated proposals, first-hit schedules and retries are not independent merely because each marginal has an exact count.

## 7. Native composition and cost boundary

The proposed production input remains N, a public proposed k, its proposal law and a public clock rule. It contains no factors, local order or cyclic generator. A future integration must bind the actual typed producers of Delta and k+2 to both Jacobi certificates, retain regular/nonregular and rejected outcomes, and then bind the selected E to ordered adjacent-trace propagation and the requested signed/clock observers. Zero/saturated values cannot be silently discarded. Every proper divisor still needs an actual exact division certificate.

All filter construction, Jacobi work, rejected proposals, public-clock arithmetic, propagation, chosen gcds, branch quotient, validation, replay, source checking and retained records remain chargeable. The generic typed Jacobi primitive identified by the predecessor is a reuse locator; this proof has neither invoked it nor audited a new integration. The old QFT final-bit theorem is not part of this torus contract. No new primitive admission, generic factoring speedup or Shor completion is claimed. Classical character and Lucas/torus analysis supplies the mathematics being made explicit here.

## Sources and continuation

The following exact local predecessor files were read in full, without importing their associated scientific modules:

- `../sep27-brc-adjacent-trace/DOUBLING_COVER_CHARACTER.md`, SHA-256 `1a1fc07a5e69abc10756538b46bc14be0e74c5c0d2f88af7886f5a4b86d97e94`.
- `../sep27-brc-adjacent-trace/EXACT_TRACE_PARAMETER_FIBERS.md`, SHA-256 `88bb76916b9d844d5763d4120668ac85531005155cf36e8bb33a44d829894dd9`.
- `../sep27-brc-adjacent-trace/PUBLIC_JACOBI_CLOCK_FIBERS.md`, SHA-256 `d3fbce534cc26e41146242cc97a7527b92054fa67eddae50fd7b15854094c3e9`.
- `../sep27-brc-adjacent-trace/JACOBI_TORUS_SELECTOR.md`, SHA-256 `30fc0de14df7eef7f43c30838fbe1dd47c60db85982ac5d92bfc0c863d2cdf2f`.

The finite-field cyclicity and norm-one facts are the same primary-source-backed facts identified in the exact-fiber predecessor. No new literature query was made, and no novelty claim is attached to these classical facts or to the character method. The new deliverable is the joint count/probability contract, proved above.

Any authorized conversation can continue from (2)-(10), either deriving useful factor-blind bounds for a specified public clock or proposing a bounded typed integration with a complete invoice. Missing a particular execution tool does not prevent this symbolic continuation. Actual scientific computation must preserve the typed BRC source contract. This separate unit is not part of the already frozen adjacent-trace execution package.

Global-Knowledge-Sync: main@b304760 / GLOBAL_KNOWLEDGE_V1. The shipped helper actually returned PASS/LEASE_REUSED at `b3047603607cebcbd3f39e7028bf707f199c3f48`; all three canonical entry files were read at that snapshot. The dirty working tree was preserved. No canonical write was performed.
