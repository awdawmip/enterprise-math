# Nondecisive mathematical review: discrete coupled moment cuts

Reviewer: EM-REVIEW-58D6A2. Activity: RA-BALANCE-REVIEW-20261028-58D6A2.
Date: 2026-10-28, Asia/Shanghai.
Finding: the 21 necessary coupled cuts, their sharp unit-cost caps and
budget-specific refinements are valid on the explicitly stated 13-smooth
integer dictionary. No unresolved mathematical defect was found.

Reviewed file: `analysis/T6_COUPLED_MOMENT_COMPLETION_CUTS_AUTHOR.md`.
SHA256: `038487aba02c1b5a812a499628f88cfc3cd3d08331b6711128c310815951b478`.
The exact inherited moment/budget interface is stated in the new manuscript;
this review does not reopen the earlier q1-q4 classifications or certify a
new actual p17 survivor.

## Independent checks

Discrete positivity is correct: each integer a from 2 through h+1 supplies
an exact zero factor, while all factors are positive for a>=h+2. It would
be incorrect to replace this with positivity on an entire real interval,
which the author explicitly avoids.

The moment equations imply sum_a t_a f(1/a)=-L(M). Separating positive
and negative t_a yields -CB_-<=-L<=CB_+, and reversing signs gives the
stated CUT orientation. Sharpness is exactly the unit-cost sense: a
maximizing atom with integer multiplicity supplies an attaining budget
multiple. It is not incorrectly asserted for arbitrary fixed small budgets.

For x>h+1, the displayed logarithmic derivative is bounded strictly above
by h/(x-h-1)-(h+k+1)/x, whose numerator is
(h+k+1)(h+1)-(k+1)x. Thus the function decreases strictly after the stated
ceiling A. Every one of the 21 A values is itself admissible and A>=h+2;
an allowed maximum at or below A therefore dominates the entire infinite
tail. This is a proof of a finite reduction, not a heuristic truncation.

I independently recomputed the rational caps and all maximizers on those
proved finite domains in `review/second_round_checks.py`. All 21 table rows
match exactly. In particular excluded unrestricted maximizers 17 and 31
must not enter the dictionary; admissible composite maximizers 18 and 32
are retained. The run is in `second_round_checks_result.json` and is not a
completion census or an old scientific rerun.

For a one-sided integer budget B, a used atom necessarily satisfies a-1<=B.
If B+1<A the bounded atom set is exhaustive; otherwise the included allowed
endpoint dominates all further atoms. This proves BCUT including B=0 and
the annihilated-small-budget cases. The explicit M_1=1,M_2=-1/2 witness
with B_+=B_-=2 satisfies all coordinate bounds but violates the coupled
bound. It establishes strict relaxation improvement only, as correctly
stated, rather than occurrence as an actual affine p17 branch.

## Scope and harvest

Validation grade: independent paper derivation plus exact small rational
table verification, not Lean/kernel proof. The inequalities are necessary,
not sufficient, and no authorized unresolved class was actually filtered.
LOCAL_FEASIBLE and FULL_COMPLETION_EXCLUDED remain distinct from local
affine EMPTY. Global T6 and prior finite classification status are unchanged.

Reuse resolution: EXTEND_EXISTING_TOOL at the old completion interface,
using standard polynomial dual-budget inequalities; no global family is
created. Composite integer directions are retained. This is external
arithmetic, not a replacement of the project's signed native X6 substrate.
Shared control/source context is disclosed; the reviewer is nonauthor but
not clean-blind and has no Driver disposition authority for this report.

Researcher-ID: EM-REVIEW-58D6A2 / TASK_RESEARCH
