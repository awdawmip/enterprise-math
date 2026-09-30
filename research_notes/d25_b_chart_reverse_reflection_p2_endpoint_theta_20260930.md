# D25 portable research: p^2 reverse reflection and the second endpoint digit

Status: AUTHOR_PORTABLE_PROOF / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT

This unit continues only the portable upper-B-chart lane. It does not claim a native session, CLAIM, run, Result, review, or theorem admission, and it does not reopen the canonical Research1 normal-Dixon / Gauss-Manin lane.

## Source boundary

- GLOBAL_KNOWLEDGE_V1 canonical main: 688f64b4be0b0594f5a3774bbf88171080ea322e.
- Enterprise Math canonical main: 912b49c89d29d36b1f5cfe1ed18bc7cb94a3a410.
- Canonical D25 local-progress blob: 51dd15a8142f3dda0506a306f9c0693a036f5891.
- Portable branch head immediately before this write: bb72581e731f994102e34666383dcb98504b15fc.
- Durable predecessor used: d25_b_chart_q_endpoint_lift_20260929.md, blob ab117820a707ad17b10088510b44a16ef69ab491.
- Current control recovery remains Issue #2578: session_state=ABSENT, no pending/run/claim/upload/staging, execution_authorized=false. This portable proof does not change that control state.

## 1. Definitions

Let p=6m+1 be prime and n=2m.

Define the forward reverse-prefix carrier

t_r = 2^r (2/3)_r / (1/2)_r,  0 <= r <= n,

and the durable Q-carrier

Q_j = - (5/6)_j / (2/3)_j * 2^(-j).

Write Fermat quotients as q_p(a)=(a^(p-1)-1)/p mod p, and q34=q_p(3)-2 q_p(2).

The durable Q-endpoint lift gives

Q_(n-1) = -8/3 + p delta_p  (mod p^2),

delta_p = 8/3 q_p(2) - 4/3 q_p(3) - 4/9  (mod p).

## 2. Lift the next Q endpoint

Exactly,

Q_n / Q_(n-1) = (2p-3)/(4(p-2)).

Hence

Q_n = -1 + p(1/6 + 3 delta_p/8)  (mod p^2).

Substituting the durable formula for delta_p gives

Q_n = -1 - (p/2) q34  (mod p^2).

Therefore

- Q_n = 1 + (p/2) q34  (mod p^2).

## 3. Rowwise p^2 reverse reflection

For s >= 0 define

rho_s = Q_(n-s-1) / Q_(n-s).

Using n=(p-1)/3,

rho_s = 4(p-3s-2)/(2p-6s-3).

The t-carrier ratio is

t_(s+1)/t_s = 4(3s+2)/(3(2s+1)).

Their quotient has the first-order expansion

rho_s / (t_(s+1)/t_s)
= 1 + p e_s  (mod p^2),

where

e_s = 1 / [3(3s+2)(2s+1)]
    = -1/(3s+2) + 2/[3(2s+1)].

All displayed denominators are p-units for 0 <= s <= n-1.

Set

E_r = sum_(s=0)^(r-1) e_s,  E_0=0.

Multiplying the ratios from s=0 to r-1 and using the lifted endpoint -Q_n above gives the all-row reflection

- Q_(n-r)
= t_r [ 1 + p( q34/2 + E_r ) ]  (mod p^2),

for every 0 <= r <= n.

Modulo p this reduces to the previously used reflection -Q_(n-r)=t_r.

## 4. Endpoint holonomy and the new digit

At r=n, the left side is -Q_0=1 exactly. Therefore

1 = t_n [ 1 + p( q34/2 + E_n ) ]  (mod p^2).

Now

E_n
= - sum_(s=0)^(n-1) 1/(3s+2)
  + (2/3) sum_(s=0)^(n-1) 1/(2s+1).

The first sum vanishes modulo p: the set {3s+2 : 0<=s<n} is closed under x -> p-x, so reciprocal terms cancel pairwise.

For the second sum,

sum_(s=0)^(n-1) 1/(2s+1)
= H_(4m) - (1/2)H_(2m)
= (1/2)H_(2m)  (mod p),

because H_(4m)=H_(2m) mod p by reflection.

Hence

E_n = H_(2m)/3 = - q_p(3)/2  (mod p).

Therefore

(t_n-1)/p
= - q34/2 - E_n
= q_p(2)  (mod p).

Equivalently, the new endpoint lift is

t_(2m) = 1 + p q_p(2) = 2^(p-1)  (mod p^2).

Define the second endpoint digit

theta_p := (t_(2m)-1)/p mod p.

Then

theta_p = q_p(2).

## 5. BRC consequence

The durable Q digit delta_p alone carries only q_p(3/4)=q_p(3)-2q_p(2).

The new reverse-prefix endpoint digit theta_p carries q_p(2). Together they recover q_p(3), hence H_(2m):

q_p(3) = 2 theta_p - 3 delta_p/4 - 1/3,

H_(2m) = -3 theta_p + 9 delta_p/8 + 1/2  (mod p).

Thus any future regularized m-transport that appeared to require an extra H_(2m) / q_p(3) repair direction can represent that direction canonically by the pair of endpoint digits (delta_p, theta_p). This is an observer-safe coordinate replacement, not a proof that the full transported bulk closes.

The rowwise defect E_r is also important provenance: reducing the reflection only modulo p erases the accumulated p-layer connection. The endpoint value E_n is its holonomy and is exactly the missing q_p(3) contribution needed to turn delta_p plus theta_p into H_(2m).

BRC disposition: COMPOSE_APPLIED / P2_REVERSE_REFLECTION / SECOND_ENDPOINT_DIGIT / OPERATION_SAFE_REPAIR_COORDINATE.

## 6. Independent regression

A dependency-free modular checker was run for every prime p<10000 with p=1 mod 6, 611 primes total.

For every prime and every row 0<=r<=2m it checked

- Q_(2m-r)
= t_r [1 + p(q34/2 + E_r)]  (mod p^2),

and also checked

(t_(2m)-1)/p = q_p(2)  (mod p).

Result: 611/611 primes, zero failures. The target residue classes p=13 or 19 mod 24 contribute 312 of these primes, also with zero failures.

The finite run is regression only. The theorem is the exact endpoint lift plus the finite product expansion above.

## 7. Next exact unit

Do not add H_(2m) as an unrelated free harmonic state. Carry theta_p as the natural endpoint digit of the reversed t-carrier.

The next smallest unit is to lift the already-used mod-p identity connecting the c=1/3 reversed logarithmic prefix to the Q-shell one p-adic order deeper. Substitute the rowwise defect E_r explicitly and test whether the complete divided reflection defect factors through (delta_p, theta_p) plus the existing logarithmic prefix J_m. If a further weighted E_r moment survives, retain that moment as the next repair coordinate; do not collapse it into endpoint data without proving fiber constancy.
