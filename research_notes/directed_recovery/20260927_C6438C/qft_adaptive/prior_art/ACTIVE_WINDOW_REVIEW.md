# Source-specific review of active-window floor moments

Reviewed file: `../nonzero_structure/ACTIVE_WINDOW_FLOOR_MOMENTS.md`.
SHA256: `20a93f15f241f9c3220c031032cc2af697e4d4a448669f5b637396c1a05529d4`.
Status: SHARED_CONTEXT_SYMBOLIC_REVIEW / NOT_INDEPENDENT_ADMISSION.
No scientific computation, matrix experiment, new query or modification of the author's source was performed.

No substantive mathematical defect was found in the stated sufficient-condition theorem. The following checks are algebraic, not empirical tests.

1. The address difference for n=VPA+Vx+y is VP(A'-A)+V(x'-x)+(y'-y). Fixing Delta=A'-A and d=x'-x leaves exactly H-|Delta| choices of A,A' and the stated Count of y,y'. Pulling out the window coefficient contributes 4^ell; with raw 4^-i this leaves 4^{-(K+B)}, without another normalization.
2. In the first modular-triangle identity, k-k_minus is either zero or one. In the one case the difference of k(k+1) is 2k, leaving u-x+Rk=u-rho. For the second identity, k_plus-k=1 gives a quadratic difference 2k, leaving x+u-R-Rk=rho+u-R. Zero differences and equality boundaries contribute zero. Euclidean floor, including negative x, is essential.
3. The symmetric j-sum counts Delta=0 twice; subtracting H Count(t_d) once is correct. Summing its constant component gives H^2 times that component. This check retains the original raw mass scale.
4. For normalized 0<a<m, 0<=b<m, threshold y occurs precisely from J_y=ceil((my-b)/a). The layer-cake expansion therefore gives formula (12). For positive exponent e, the two polynomial factors have degrees e-1 and p+1. Their total is p+e<=3, so the ten moments close. The new modulus is a; the next normalization produces the Euclidean remainder. The O(log m) claim requires the stated shared-geometry evaluation or memoization, not ten separately branching recursive trees. The n=0, e=0, a=0 and Y=0 cases are stated separately.
5. Signed normalization changes coefficients but not total degree. Fixed degree and polynomial-bit inputs give polynomial-bit intermediate integers under this recurrence; no enumeration up to H or R is implicit in a power sum.
6. Noncommuting active words are retained in chronological order inside C_win(d). Identity blocks are removed only under a full-carrier equality, not by ideal-angle similarity or small residual norm. The source explicitly prevents transferring a fixed-tail identity to an untruncated direct-word bank.
7. K=0, B=0, R=1, even R, negative affine shifts and an empty active window are consistent with the formulas. No modular inverse of V is needed. Order discovery, target address acquisition and output/native arithmetic costs remain explicit.

Useful counterexample to an overbroad interpretation: a zero output bit after an earlier one does not imply O_j=I, because the earlier one can still activate a nonidentity feedback word. Thus a visually sparse history does not by itself meet the theorem. Similarly, replacing a fixed chronological pair A then B with B then A inside a coefficient changes U whenever AB differs from BA; scalar free-coordinate counts cannot justify that reorder. The reviewed draft makes neither substitution.

The source's proposed next tests are meaningful: signed floor boundaries; R=1 and even R; K=0/B=0; failed identity premises; and all signed matrix entries for a noncommuting active window with residuals. They remain future execution requirements, not checks performed in this review.

The cost is exponential only in the proved active width, after paid order/address information. It is not a general poly(log N) simulation result and does not establish that most reached histories have a short active window.

Global-Knowledge-Sync: main@06788df / GLOBAL_KNOWLEDGE_V1
