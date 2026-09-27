# Joint character fibers: author self-review

Status: **AUTHOR_SELF_REVIEW_PASS / PURE_SYMBOLIC / NOT_EXECUTED / NOT_ADMITTED**.
This review binds `JOINT_CHARACTER_FIBERS.md` at SHA-256 `5a60e21262e880797af799b8fd5e23155f6a1cec2a26f8ecc2cbe7375b0a1323` (15,938 bytes). It is the author's own check, not an independent mathematical admission. No scientific module, host numerical oracle, fixture or provider query was run.

## Character and local class boundaries

The proof uses a cyclic eigenvalue group of order L=r-sigma only in the mathematical analysis. The nonsplit character calculation uses lambda^r=lambda^-1 and excludes lambda=-1 before division by lambda+1. Euler's criterion is applied to k+2 in the base field; the extension calculation evaluates that same field element. Inversion preserves exponent parity, so the character descends to the actual trace parameter.

The two excluded eigenvalues have different roles: lambda=1 has eta=+1; lambda=-1 has eta=(-1)^(L/2)=alpha_r*sigma. They are each removed once from their actual parity class. Only after removal is the count divided by two. This prevents the common error of subtracting both exceptions from every class. The four closed forms in (2) sum to r-2 and to the previously proved split/nonsplit counts. Empty classes at r=3 and r=5 are explicitly retained. No conditional probability is assigned to them.

## Signed-root congruence

For E>=0, g=gcd(E,L) and a=L/g are sufficient. Positive solutions are the g multiples of a. If a is odd, g is even, so half have each parity. If a is even, all are even.

The negative congruence is soluble exactly when a is even. Then E/g is invertible and odd modulo a. Its inverse is also odd, so multiplying a/2 by that inverse leaves its parity unchanged. All g solutions therefore lie in the single class eta=(-1)^(a/2). No unstated dependence on the odd part of E/g is needed. If a is odd there is no negative solution; in particular a=1 requires no inverse computation.

The positive exceptional corrections are 1 and the even-E contribution of -1. The negative correction is only the odd-E contribution of -1. This proves integer, nonnegative counts without any numerical spot check. E=0 gives the entire regular class positively, E=1 gives neither return, and the r=3 symbolic boundary agrees with the four-element norm-one group. Positive and negative sets cannot overlap in odd characteristic.

## Global normalization and dependent characters

CRT independence applies to local trace parameters before global filtering. It does not imply independence of the two characters at one prime or of their two global products. The local sums are r-2, -1, -1 and -alpha_r. Expanding the two sign indicators consequently gives

    Z=(R+j+e+alpha*j*e)/4,
    R=(p-2)(q-2), alpha=alpha_p*alpha_q.

The four orientation weights are products of local class sizes, divided by this same Z. Empty orientations have weight zero. The theorem requires Z>0 before forming a conditional law, and allows an empty global class. The covariance (alpha*R-1)/R^2 is nonzero for distinct odd primes, since R>1; the signs are therefore not independent fair bits. A balanced conditional sign for a particular j does not contradict this statement.

The two-prime squarefree promise is essential to the displayed global interpretation and four divisor labels. Jacobi values weight repeated prime factors differently; neither regularity nor the two global signs certifies that promise. The proof does not extend the distribution formulas to prime powers, arbitrary factorizations or a nonuniform proposal law.

## Factor categories and clock selection

For one sign, the four products in (9) form a partition in each orientation and sum to C_p*C_q. The formula is written directly in counts rather than through local conditional divisions, so it remains well-defined when some C is zero. For both signs the categories are positive, negative and neither. Equal categories give no proper main-clock factor; distinct categories give a proper factor. This proves (10) and includes opposite-sign simultaneous hits without treating them as independent trials.

For a fixed sign, E and E+2 are disjoint on the regular local domain because a common return would force lambda^2=1. Opposite signs at the two clocks need not be disjoint. The note explicitly refuses to use a four-disjoint-category model for that enlarged event set.

The public E=N-j corollary only reuses the predecessor's common-gcd identity. The two reduced group orders are coprime, hence cannot both be even. The negative branch remains nonsaturating after further conditioning on eta. This is an impossibility of one failure outcome, not a lower bound on success probability. Mixed public clocks are covered algebraically but their unknown local gcds are analysis parameters, not free algorithm inputs. A k-dependent or adaptive exponent can change the within-class law and needs another argument.

## Execution and continuation boundary

All new content is symbolic. No finite native fixture supplies a rate, and no new typed Jacobi integration has been implemented. The proposed interface keeps the typed Delta/k+2 producers, full character certificates, rejected proposals, chosen exponent, ordered adjacent traces, gcd/division witnesses and every corresponding cost. It does not import the older QFT final-bit contract. Classical character/Lucas ideas are not presented as a new general factoring algorithm.

The exact predecessor paths and hashes, actual policy-read marker and continuation boundary are recorded in the proof. This new directory is separate from the frozen adjacent-trace package. A peer should check (2)-(10), especially parity of negative solutions and zero-weight orientations, before any future numerical integration. The current result is ready for that bounded review.

Global-Knowledge-Sync: main@b304760 / GLOBAL_KNOWLEDGE_V1.
