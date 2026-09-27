# What character stratification and exact packets actually save

Status: AUTHOR_SYMBOLIC_DERIVATION / SHARED_CONTEXT / NOT_ADMITTED.
Activity RA-CAAAC604CB513AEA8BBC1DFC. No new scientific execution.
All transformations below retain the complete native D-vector and their
chronological matrix order. No hidden order, factor or ideal phase is an
input. This note refines the parent's random-path variance calculation;
it does not claim that conditional means can be queried for free.

## 1. A fixed-prefix stratification identity

Fix a measured prefix at depth k, with complete raw field v of mass
M=||v||^2. For one fixed descendant measured history of length ell, let
X_s=U_s v be the field obtained from a uniform preparation address
s in {0,1}^ell. Each U_s is the actual ordered product of permutation/
orthogonal native arms with the fixed history's signs. Therefore ||X_s||^2=M
and the descendant field is mu=E X_s.

Partition addresses into classes c with exact probabilities p_c>0. Denote
their conditional means by mu_c. Independently sample m_c addresses inside
each class and estimate mu by sum_c p_c times its sample mean. Then

    E||mu_hat-mu||^2 = sum_c (p_c^2/m_c)(M-||mu_c||^2).       (1)

This follows by independence of centered sample means and the Hilbert-space
variance identity. It needs no commutation of U_s. If all class variances
were already known, the real-valued optimal allocation at total sample
budget m would be proportional to p_c sqrt(M-||mu_c||^2). Computing these
conditional energies is itself an oracle problem; integer allocations and
their certificate cost cannot be omitted.

## 2. Equal disjoint character classes

Suppose there are c equally likely classes, their conditional mean fields
have disjoint work support, and m is divisible by c. Allocating m/c samples
to each gives

    ||mu||^2 = c^-2 sum_c ||mu_c||^2,
    E||mu_hat-mu||^2 = (M-c||mu||^2)/m.                      (2)

For comparison, unstratified sampling gives (M-||mu||^2)/m. Thus this
particular stratification subtracts (c-1)||mu||^2/m; it does not divide the
large M/m term by c. The assumptions can occur when a known multiplicative
character separates the output of the address classes and the parent field
is supported in one character class. They must be proved, not inferred
from a label histogram. Conditional address sampling must be supplied and
charged; parity characters can use a fixed bit equation without rejection.

If the same c-class condition holds for every ell-bit descendant, sum (2)
over those descendants. The exact complete adaptive instrument satisfies
sum_h ||v_h||^2=M. Therefore

    sum_h E||mu_hat_h-v_h||^2 = (2^ell-c) M/m.                (3)

Summing over an earlier normalized ensemble replaces M by 1. Jacobi gives
at most c=2 in the existing final-bit witness, so the aggregate factor is
2^ell-2, not a polynomial replacement for 2^ell. This does not diminish its
separate exact final-bit shortcut: that shortcut avoids the problematic
row approximation entirely. No higher-order character is assumed available.

## 3. Exact suffix packets: variance improves, arithmetic may not

Instead estimate raw fields only up to ell-b additional rounds, and apply
the final b rounds exactly to each of those estimates with the same actual
adaptive instrument. It is an isometry into all b-bit descendants. Thus
the sum of squared errors over those descendants is exactly the squared
error before that final block. In the parent's equal-m independent
random-path model this gives

    aggregate expected squared error = (2^(ell-b)-1) M/m.    (4)

The deterministic exact block must really act on the signed complete field.
For an explicit sample-supported representation, a single block can create
2^b different work labels. Paying this factor per sample cancels the apparent
2^b saving in the sample count. Complete-word action, signed aggregation,
queries and certificates must all be charged. Equation (4) alone is not a
runtime improvement or a representation theorem.

There is a concrete checkable exception: a run of work multipliers equal
to the identity. Each native branch then acts on a row as
(I+sigma T_h)/2 and causes no work-label expansion. These equalities are
directly testable from the actual typed multipliers, without an order input.
The block can be computed in O(b) complete-vector actions per occupied row,
retaining native noncommutation. More generally, a cheaply certified small
closed work set bounds packet growth; its construction/proof is charged.
These are conditional gains on inputs with verified block structure, not
assertions that the general Shor schedule has many such blocks.

Exact early blocks also allow the baseline checkpoint depth to advance
cheaply on such certified inputs. There is no need to enumerate all measured
histories merely to construct the one queried branch; completeness is used
only in the proof of the global error identity. This recovers an explicit
cost criterion for Rao--Blackwellization without hiding block contraction.

## 4. Why a coarse control variate does not finish the job

For any pathwise control variate Y_s whose exact mean nu is supplied,
the unbiased estimator nu+average(X_s-Y_s) has variance

    [E||X_s-Y_s||^2 - ||mu-nu||^2]/m.                       (5)

This is a useful certificate target: the residual second moment, the mean
nu, and their actual construction cost must be small. A coarse character
summary is not a complete work field nu. Lifting its values back to every
label can reintroduce the original coherent fibre-sum problem. Assuming
that lift or the required conditional means is polynomial would simply
rename the missing row oracle. The work-marginal pruning note supplies one
honest testable lift and an exact sparse-work obstruction; it does not
assume a general low-width representation.

No new random-path, approximate phase, ideal-QFT or reference-state execution
is asserted by these identities. They are algebraic scope and cost results,
available for a later bounded actual comparison if warranted.
