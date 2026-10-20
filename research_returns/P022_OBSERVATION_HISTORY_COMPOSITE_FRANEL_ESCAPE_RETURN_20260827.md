# P022 Observation-History Composite Franel Escape — Recovery Return

Status: `PASS / MINIMAL_EXACT_EXCEPTION_FROZEN / ALL_M_NONVANISHING_OPEN`

Task: `RS-P022-OBSERVATION-HISTORY`  
Publication: `TP2-2346F5D3E731ED56DB0A`  
Claim: `chatgpt-p022obs-20260828-2241-recover`  
Researcher: `EM-P022OBS-919781`  
Execution: `ER-6A63C0F7D2E9B18451A0`

## Result

This recovery did not replay the old P022 arithmetic chain. It consumed the accepted Hahn diagonal

\[p\mid F_{2n}\iff Q_n(n;-3n,n-1,3n)=0\pmod p,\qquad p=6n-1,\]

and the expired live checkpoint whose scalar dual-Hasse route had already been proved redundant.

The requested independent matrix/second-order object is now exact. With

\[Y_s=Q_n(n+s;-3n,n-1,3n)\]

the standard Hahn x-difference equation collapses modulo `p=6n-1` to the parameter-free recurrence

\[(s-\tfrac13)(s+\tfrac23)Y_{s+1}+(\tfrac13-2s^2)Y_s+(s-\tfrac12)(s+\tfrac16)Y_{s-1}=0.\]

Writing `V_s=(Y_s,Y_(s-1))^T` gives a universal `2 x 2` transfer `M_s`. The initial values are fixed: `Q_n(0)=1` and `Q_n(1)=10/9 (mod p)`. Hence, for `T_n=M_-1 ... M_(1-n)`,

\[\boxed{T_n(10,9)^T=9(Q_n(n),Q_n(n-1))^T.}\]

Therefore the surviving P022 exception is exactly

\[\boxed{e_1^T T_{3m}(10,9)^T=0}\]

under the admissible gate `18m-1,12m-1,12m+1` prime. Every transfer matrix is invertible on the relevant interval. If a zero occurs, its local crossing is universal:

\[Q(n-2)/Q(n-1)=4/3,\quad Q(n+1)/Q(n-1)=-3/8,\quad Q(n+2)/Q(n+1)=3/2.\]

This removes the moving Hahn parameters from the residue entirely: only the admissible transfer length remains.

## Killed route

The obvious scalar-Hasse second-jet Casoratian is not independent. The two Picard-Fuchs equations plus the already-proved adjoint first-jet condition give `theta^2 P/P=5/243` and `theta^2 D/D=4/243`, hence

\[\theta P\,\theta^2D-\theta^2P\,\theta D=0\]

on the boundary-obstruction locus. This route should not be retried.

## Conductor-18 contact

The fixed transfer has

\[\det M_s=\frac{(s-\tfrac12)(s+\tfrac16)}{(s-\tfrac13)(s+\tfrac23)}.\]

At `s=3t+a`, `a=0,1,2`, this becomes

\[\frac{(t+a/3-1/6)(t+a/3+1/18)}{(t+a/3-1/9)(t+a/3+2/9)},\]

so mod-3 blocking raises the transfer arithmetic to denominator 18. This is a determinant-level bridge to the previous conductor-18 three-section route; it does not yet identify the full rank-nine Frobenius system.

## Validation

New task-local files:

- `src/enterprise_math/p022_barlow_hahn_centered_transfer.py`
- `tests/test_p022_barlow_hahn_centered_transfer.py`
- `docs/P022_BARLOW_HAHN_CENTERED_TRANSFER.en.md`

An isolated replay of the committed module/tests passed: `4 passed`. The known unrestricted zero `(n,p)=(25,149)` is detected exactly. Among the 13 admissible boundaries with `n<=500` there were zero transfer/Hahn mismatches and zero zeros. A research-time scan through `n<=5000` covered 64 admissible boundaries with zero mismatches and zero admissible zeros. These scans are regression/falsification evidence only.

## Hard target disposition

`P022_COMPOSITE_FRANEL_ESCAPE_CLOSED_OR_MINIMAL_EXACT_EXCEPTION_FROZEN`

Disposition: `MINIMAL_EXACT_EXCEPTION_FROZEN / MET`.

Universal all-`m` nonvanishing is **not** claimed. The exact remaining frontier is

\[e_1^T T_{3m}(10,9)^T\ne0\]

for every admissible prime triple.

Recommended next action: compute the full three-step transfer `M_(3t+2) M_(3t+1) M_(3t)` and couple its projective orbit to the accepted conductor-18 Frobenius/Hahn data, or construct an equivalent Cartier/Hasse-Witt off-diagonal block determinant. Do not enlarge the finite census as proof.
