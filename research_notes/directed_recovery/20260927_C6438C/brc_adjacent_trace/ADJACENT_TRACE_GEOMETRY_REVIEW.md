# Adjacent-trace HBW geometry review

Status: **SYMBOLIC PASS / SHARED CONTEXT / NO SCIENTIFIC EXECUTION / NOT ADMITTED**.

Reviewed the complete `ADJACENT_TRACE_HBW_GEOMETRY.md`, SHA-256 `3b8083eb0ecddc1c12406cd64113ce3e2bb88ee676a0e7b8fd3f7c6289511e14`. The three referenced frozen proof files were located and their actual bytes matched the stated `fbec0b42...`, `a3562a0b...` and `2294c283...` pins. No scientific source was imported and no numerical oracle or external query was used.

No material defect was found. Literal matrix multiplication gives both TM and MT as `[[-2,k],[-k,k^2-2]]`; T maps the cyclic initial vector to `(2,k)` and has determinant `4-k^2`. With the paid discriminant-unit hypothesis this is an invertible residue-ring chart, including at prime powers. It need not be an integer-unimodular rechart, and the note correctly distinguishes these contracts. The conic value at the new initial point is `4-k^2`; M preserves that form. A common norm alone is not an observation-safe quotient.

The trace recurrence and the initial values establish `t_n=M^n(2,k)` and the displayed D0/D1 updates on the coherent orbit. The signed translated residual is exactly T times the original residual, so their generated ideals and common gcds agree. This proves a primitive-depth observation without computing T inverse or a square root. It does not make the nonlinear bit update a single original HBW move.

For the inversion, S fixes the first trace and replaces the second by the previous trace, hence sends `t_n` to `t_-n`. The signed return matrices satisfy `M^(-n)-epsilon I = -epsilon M^(-n)(M^n-epsilon I)`, which proves ideal invariance. Extending this to a quotient of a process requires the separately stated symmetric step language and correct microscopic multiplicities. In particular, invariance of the current joint readout alone does not license folding an arbitrary future asymmetric bit program.

The forward single-section observer joins the n and n+2 clocks, while its inverted version joins n and n-2. For a regular local component with order r>4, the purely symbolic index n=r-2 makes n+2 a return and neither n nor n-2 a return. The two-clock theorem then gives different local supports. The counterexample uses the order only to state a conditional mathematical witness, not as a free algorithm input. Thus the extra output invalidates the old inversion-fold lease. The note correctly requires retaining orientation or proving a different symmetrized output contract; averaging cannot preserve the exact gcd-valued output.

This is a valid bridge to the existing marked HBW conic interface and a precise boundary on its quotient. It supplies neither an advantageous input selector nor an end-to-end complexity or Shor-completion claim. The current ordered-pair implementation and its native costs still require their own source and saved-record checks.

Global-Knowledge-Sync: shared-author reuse of already read canonical context; no fresh independent handshake is claimed by this static review.
