# Tool coverage and typed reuse

Source snapshot: `108ac80d4af9a1ebe19cc613aaccb7402564100e`. The relevant toolkit, policy and archived ring files are unchanged from the verified local b99 snapshot. Three actual `tools/enterprise_toolbox.py --json coverage` queries are retained with this intake's local receipts.

| Interface | Resolution | Actual use and boundary |
| --- | --- | --- |
| T0_BRC / exact_arithmetic DIV | REUSE_EXECUTED | Nine real BRC calls, including rejection of the nonintegral1/2 type. Degree ratios and residual pair counts retain quotient/remainder/reconstruction traces. No complex coefficient, elliptic point or field square root is numerically evaluated |
| T6_OPERATION_SAFE_QUOTIENT | REUSE_EXECUTED | Existing `operation_quotient.refines` proves that a total-degree/Hurwitz partition does not determine the finer local signature. Only the declared finite observation relation is tested; no unmodeled future operation is certified |
| Task-local integer polynomial ring | REUSE_EXECUTED | Unchanged `check_squareclass_rr.py` primitives check `R U=(R²+t)²` and the nonzero U+1 tamper residual. The old checker main programs and assignment enumeration are not run |
| Existing L(2O+S) basis in the empty-fiber paper | REUSE_APPLIED | Specializing S to a nonzero two-torsion point supplies the missing `t/(R-r)` half-section. The geometric divisor argument remains a paper obligation for separate review |
| T1 scale enumeration, T5 precision, T12 Bellman/path closure and other lexical matches | NOT_APPLICABLE | No scale family, approximate precision, optimization or path-closure problem is being claimed. No new general capability gap or tool family is asserted |

The population consists of labelled local ramification types, not global maps. Alternative labels preserve which Q maps to which special value. The observer retains B occupancy, Q target, local degree, and the sign of a pole valuation. Total12 is a derived coarse readout and cannot replace that data.

The second loss-of-information witness is factorwise valuation: `ord_T(R)=2` can cancel `ord_T(R+t/R)=-1` twice. Product regularity does not imply regularity of a half-section. Signed valuations remain typed integer data; positive branch counts do not stand in for cancellation or divisor descent.

All141 locally admissible labelled placements remain only finite necessary types. The disputed six-block obstruction is not applied to discard its coordinate, and none of the new local counts is added to the archived135 V4 candidates or1980 parameter components.
