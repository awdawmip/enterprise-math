# Frozen independent zero-seed second-digit carrier

Status: PRE_EXECUTION_CANDIDATE_DEFINITION / NO_NEW_NUMERICAL_COMPARISON.
This definition was fixed before running the new exact checker. It does not
read g_p, an evaluated Gauss/Hesse discrepancy, a desired UR/LIFT answer,
a fitted scalar, or a period normalization. Inputs are only p and the frozen
exact coordinate x_±. The existing unit16 inputs and preparation provenance
are retained separately; this freeze is not a native execution or Result.

For every prime p=6m+1 define I_p(x)=sum[j=0..p-2]i_j x^j over F_p by

    i_0=0,
    i_(j+1)=((j+1/3)(j+2/3)i_j-2/9)/(j+1)^2,
    j=0,...,p-3.

Every denominator is a unit. This is a fixed nonhomogeneous Hesse
particular solution candidate, not a normalized period. At the exact
x_±=(2±sqrt(2))/4 and target p mod24 in {13,19}, the bounded claim is

    g_p/p = L_p(x_±)/p + p*σ(x_±)*I_p(x_±)  (mod p²).

Only the correction term is evaluated over F_p; L_p(x_±) is evaluated at
the exact algebraic lift through p³. In this term σ(x_±)=x_∓ modulo p.
No assertion equates literal powering with lifted Frobenius modulo p².

The intended proof is that the full polynomial correction J_p differs
from I_p by B_p*H_p, where H_p=L_p modulo p has degree 2m. Unit16 and
inherited CM0 give H_p(x_±)=0. Hence the seed ambiguity cancels for this
value observer and this precision. This is an exact observer-scoped
certificate. It does not drop B_p from the complete carrier, since
J'_p(x_±)-I'_p(x_±)=B_p*H'_p(x_±), which need not vanish.
Ordinary points and derivative observers therefore keep B_p.

For the complete coefficientwise comparison, an independently defined
boundary carrier is fixed as well. Set

    q_2=(2^(p-1)-1)/p,
    S_2=sum[k=0..m-1]1/(6k+2),
    T_r=sum[k=0..m-1]1/(6k+r)^2, r=2,3,6,
    B_p=(2/9)*[(-3S_2-q_2)/p+q_2²/2-3T_6+12T_3+(33/2)T_2] mod p.

Compute S_2,q_2 modulo p², T_r modulo p, and divide the canonical
p-divisible residue -3S_2-q_2 modulo p² by p. All denominators are units.
Set J_p(0)=B_p and use the same recurrence. The full bounded claim is

    f_p(4x(1-x))=L_p(x)+p²x^pJ_p(x)  (mod p³),

with the corresponding differentiated observer requiring full J_p.
The uniform formula, harmonic boundary, CM0 cancellation, and derivative
boundary each receive their own checks; a success in one does not imply
an unproved period calibration, UR, LIFT or parent completion.

Initial discriminating finite comparisons, once own binding is active:
p=7,13,19,31,37,43; all polynomial coefficients with full J_p; exact target
half branches and second digits at 13/19/37/43 with zero-seed I_p;
factor-entry j=2m,4m and last coefficient; the uncorrected half failure at13;
zero-seed polynomial and derivative counterexamples where B_p≠0. The
independent reviewer will not execute the author's checker or merely
compare its own expressions copied from the implementation.

The method is a finite task-local arithmetic supplement. Retain all branch
labels, signed divided values, Jacobians, h/omega^r source marks, and exact
lift precision. Heartbeat World native X6/time and joint-preservation
semantics remain as loaded. No lower-dimensional native model or full-X6
propagation is inferred from these external arithmetic readouts.
