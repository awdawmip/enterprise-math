# D25 LIFT — symmetric diagonal mass obeys the original 3F2 transport

Status: PROVED_STRICT_REDUCTION_UNIT / LIFT_NOT_YET_CLOSED / NOT_A_RESULT / UNREVIEWED
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT
Publication: TP2-B6F4FC938FF94941C1B7
Date: 2026-09-24

## 0. Consumed frontier
Consume the projection-compatible finite Green checkpoint. Thus
A(z)=sum_{j=0}^m a_jz^j,
G_m(z)=sum_{r=1}^m y_rz^{-r},
H(z)=A(z)G_m(z),
H_h=[z^h]H=sum_{r=1}^{m-h}a_{h+r}y_r,
C_m=sum_{h=0}^{m-1}(6h+1)H_h,
and
q(z):=L_mG_m=-1/18+2m^2y_mz^{-m}.
The finite Wronskian controls only the skew flux; this unit solves the missing symmetric-mass transport.

## 1. Symmetric-square equation
Write the second-order Gauss equation in ordinary derivatives as
f''+P f'+Qf=R,
where
P=[2+(3m-1)z]/[z(2-z)],
Q=-2m^2/[z(2-z)],
R=q/[z^2(2-z)].
A has R=0 and G_m has this R. For H=A G_m the standard direct differentiation identity is
H'''+3PH''+(P'+4Q+2P^2)H'+(2Q'+4PQ)H
 = A R'+(3A'+2PA)R.

Now work in F_p with p=6m+1, so 6m+1=0. After clearing the common polynomial denominator and cancelling the common factor z-2, the m-dependence disappears completely:

BOXED:
18z^2(z-2)H''' +27z(3z-4)H'' +2(29z-18)H' +2H
 = -54qA' -18Aq'.

This identity is exact in F_p.

## 2. Terminal source is invisible to every nonnegative mass coefficient
The terminal part of q is 2m^2y_m z^{-m}; hence both q_terminal A' and A q_terminal' have maximal exponent -1 because deg A=m. Therefore for every h>=0 the terminal source contributes zero to [z^h] of the symmetric-square equation. The only nonnegative source is q_0=-1/18, yielding
[z^h](-54qA'-18Aq')=3(h+1)a_{h+1}
for 0<=h<=m-1.

This is a second exact BRC separation: the terminal reflected endpoint is mandatory for the skew-flux equation but provably invisible to the symmetric nonnegative mass transport.

## 3. First-order recurrence for H_h
Extracting [z^h] from the universal third-order operator gives a cancellation to only two adjacent mass coordinates:

BOXED:
(2h+1)(3h+1)(3h+2)H_h
 -36(h+1)^3H_{h+1}
 =3(h+1)a_{h+1},

for 0<=h<=m-1, with H_m=0.

Thus the entire symmetric mass sequence is first-order, not an independent length-m boundary chain.

## 4. The homogeneous transport is exactly the original W_p kernel
Define the original unweighted 3F2 coefficient

t_h=((1/2)_h(1/3)_h(2/3)_h)/(h!)^3 *2^{-h}.

Then
t_{h+1}/t_h=(2h+1)(3h+1)(3h+2)/[36(h+1)^3].
Hence the mass recurrence becomes

BOXED:
H_{h+1}=(t_{h+1}/t_h)H_h-a_{h+1}/[12(h+1)^2].

Dividing by t_{h+1} and using H_m=0 gives the exact closed tail formula

BOXED:
H_h=t_h sum_{s=h+1}^m a_s/[12s^2 t_s].

So the reflected-boundary symmetric mass is transported by the same 3F2 coefficient sequence that defines the original weighted Ramanujan sum W_p. No y_r survives in this carrier.

## 5. C_m becomes a single prefix transform of the original weighted kernel
Substituting the tail formula and interchanging the finite sums gives

BOXED:
C_m=sum_{s=1}^m a_s/[12s^2t_s] * P_s,
where
P_s=sum_{h=0}^{s-1}(6h+1)t_h.

Thus C_m is no longer an arbitrary low/high double sum: it is an exact one-dimensional prefix transform of the same weighted 3F2 kernel whose full p-truncation is W_p. This is the first direct algebraic bridge from the Green boundary correction back to the original W-kernel.

## 6. BRC/provenance statement
Observer: C_m mod p and surviving W_p mod p^3 certificate.
Preserved: h/s index, low Gauss coefficient a_s, original 3F2 coefficient t_s, weighted prefix P_s, and finite-projection provenance.
Eliminated safely: the reflected y_r chain from the symmetric mass observer.
Not eliminated: p-adic second-digit information of the full S_p,D_p/W_p truncations.
No custom axiom and no finite scan is used in the proof.

## 7. Regression
An exact checker over all 166 target primes p<5000 verifies the symmetric-square Laurent identity, the adjacent first-order recurrence, the normalized tail formula, and the prefix-transform formula for C_m with zero failures. The scan is regression/falsification only.

## 8. Narrow next action
Use the exact prefix transform
C_m=sum_{s=1}^m a_s P_s/(12s^2t_s)
to seek a contiguous/WZ identity for P_s or a p-adic comparison of its endpoint data with the second digits of S_p,D_p. Do not return to the two-dimensional (j,r) boundary sum or the y_r chain unless falsifying this reduction. The hard target remains W_p==p mod p^3 for every p congruent 13 or 19 mod 24.
