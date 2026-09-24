# D25 LIFT — projection-compatible finite Green closure and skew-flux recurrence

Status: PROVED_STRICT_REDUCTION_UNIT / LIFT_NOT_YET_CLOSED / NOT_A_RESULT / UNREVIEWED
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT
Publication: TP2-B6F4FC938FF94941C1B7
Date: 2026-09-24

## 0. Consumed frontier
Consume the authenticated Green/Wronskian checkpoint. In F_p, p=6m+1,
A(z)=sum_{j=0}^m a_j z^j, L_m A=0,
L_m=2 theta^2-z(m-theta)(2m-theta),
y_1=1/10, 2r^2 y_r=(r+m+1)(r+2m+1)y_{r+1},
and
C_m=[(6 theta+1)[A(z)G(z)]_{>=0}]_{z=1}.
The live LIFT certificate remains
W_p == S_p^2+12S_pD_p-2p^2 C_m (mod p^3).
Do not reopen D24 UR/JT0 or earlier D25 shell/jet/Clausen units.

## 1. Positive projection only sees a finite Green branch
Set
G_m(z)=sum_{r=1}^m y_r z^{-r}.
Since deg A=m, every r>m contributes only negative powers to A(z)z^{-r}. Hence

BOXED: C_m=[(6theta+1)[A(z)G_m(z)]_{>=0}]_{z=1}.

Thus the LIFT observer never needs the infinite continuation of the reflected branch. This quotient is exact for C_m and preserves every labelled pair 1<=r<=j<=m.

## 2. Finite truncation creates exactly one terminal source
Coefficientwise application of L_m gives

BOXED: L_m G_m=-1/18+2m^2 y_m z^{-m}.

For z^{-r}, 1<=r<m, the recurrence cancels exactly. The constant splice is -(m+1)(2m+1)y_1=-1/18 in F_p. The only additional defect is the missing r=m+1 transition, leaving 2m^2y_m z^{-m}.

This terminal source is mandatory: the previous infinite-branch equation L_mG=-1/18 cannot be substituted after taking the finite positive-projection quotient without restoring this endpoint.

## 3. Exact finite Wronskian with both sources
Define the Euler Wronskian
J(z)=A theta G_m-(theta A)G_m=z(A G_m'-A'G_m).
The Lagrange identity for L_m gives

BOXED: (2-z)theta J+3mzJ=A(z)(-1/18+2m^2y_m z^{-m}).

Equivalently,

BOXED: d/dz{J(z)/(2-z)^(3m)}
 = A(z)(-1/18+2m^2y_m z^{-m})/[z(2-z)^(3m+1)].

This is the projection-compatible replacement for the infinite Green Wronskian. It has exactly two source ports: the splice at 0 and the terminal reflected endpoint.

## 4. The skew flux is completely first-order
Write J(z)=sum_h J_h z^h. Then coefficient extraction yields

BOXED: 2h J_h+(3m-h+1)J_{h-1}
 = [z^h] A(z)(-1/18+2m^2y_m z^{-m}).

In particular, for 1<=h<=m, the terminal source is absent and

2hJ_h+(3m-h+1)J_{h-1}=-a_h/18,

with J_m=0. Thus every nonnegative skew-flux coordinate is determined backwards from the low Gauss coefficients alone. At h=0 the terminal source gives the exact adjacent-diagonal identity

BOXED: sum_{j=0}^{m-1}(2j+1)a_j y_{j+1}
 = 1/9-4m^2 a_m y_m   (mod p).

No finite scan enters this proof.

## 5. BRC information-loss audit: Wronskian is not C_m
For each Laurent diagonal h>=0 define
H_h=[z^h](A G_m)=sum_r a_{h+r}y_r.
Then
C_m=sum_{h=0}^{m-1}(6h+1)H_h,
while
J_h=-sum_r(2r+h)a_{h+r}y_r.

Therefore the Wronskian transports the oriented/skew first moment, not the symmetric diagonal mass H_h. Whenever a diagonal contains at least two labelled pairs, the linear map from pair contributions to J_h has a nontrivial kernel on which H_h changes. Hence replacing the positive-part carrier by J alone is an unsafe BRC quotient.

The exact new reduction is instead:
- all skew-flux coordinates J_h are no longer independent live data; the source recurrence above determines them;
- the unresolved LIFT information is precisely the symmetric positive-diagonal mass sequence H_0,...,H_{m-1}, or any proved equivalent carrier.

This identifies the smallest missing observer behind the prior Green route and prevents a false Wronskian-only closure.

BRC_REUSE_RESOLUTION=COMPOSE_APPLIED.
Preserved: h, labelled low/high pairs, orientation, splice source, terminal source, and positive diagonal mass.
Safe quotient: infinite reflected tail -> G_m for C_m.
Forbidden quotient: G_m -> Wronskian J alone.

## 6. Exact regression
A deterministic modular checker over all 166 target primes p<5000 verifies: the finite Green equation including the terminal source; the full coefficient recurrence for J; the adjacent-diagonal flux identity; and equality of the finite projection with the original C_m double sum. Failures: 0. This is falsification/regression only.

## 7. Narrow next action
Do not rederive the Green source/Wronskian. Derive a closed recurrence or telescoper for the remaining symmetric diagonal masses H_h, preferably by the symmetric-square/creative-telescoping operator of the same Gauss equation, and sum (6h+1)H_h. The target is still to identify C_m with the second p-adic digits of S_p,D_p and prove W_p==p mod p^3, or produce an exact obstruction.
