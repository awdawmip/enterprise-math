# D25 LIFT — lawful fixed-p terminal-band cutoff and universal curvature-defect no-go

Status: PROVED_STRICT_REDUCTION_NO_GO_UNIT / LIFT_NOT_YET_CLOSED / NOT_A_RESULT / UNREVIEWED
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT
Publication: TP2-B6F4FC938FF94941C1B7
Date: 2026-09-24
Source pin consumed: awdawmip/enterprise-math@621bd918cfe4eea9f0c0ae20aa82def82fbc87bc

## 0. Consumed frontier and de-duplication

Consume the canonical D25 checkpoint through the universal prefix factor chain and the exact prior-art audit. Do not reopen D24 UR/JT0, the shell/global-jet/Clausen/Green/symmetric-mass/adjoint units, or the universal prefix factorization.

The canonical universal comparison chain is

    R_s = sum_{j=1}^s c_j P_j,
    U_s = R_s-R_{s-1},
    V_s = U_{s+1}-lambda_s U_s,
    V_{s+1}=mu_s V_s,

with

    lambda_s = s^2(6s+1)/[(s+1)(2s+1)(3s+2)],

    mu_s =
      (2s+1)(3s+1)(3s+2)(6s+7)^2
      / [36(s+1)(6s+1)(s+2)(2s+3)(3s+5)].

The current unresolved instruction is to construct a legitimate source-derived adjacent-cutoff p-adic extension Q_s and inspect its labelled curvature before quotienting. This unit does that for the most literal fixed-p terminal p^2 band. It also consumes the concurrent Driver endpoint-Green notes on issue #1516 only to avoid duplicating their general Green theorem; no Driver authority or task admission is imported.

## 1. A lawful fixed-p source cutoff

Fix one target prime

    p=6m+1,    p == 13 or 19 (mod 24),

and retain the accepted half-series source

    B_k = (1/6)_k (1/3)_k / [(k!)^2 2^k],
    g = sum_{k=0}^{p-1} B_k,
    h = sum_{k=0}^{p-1} (12k+1)B_k.

The accepted first digit gives p|g and, with G=g/p,

    G h == 1 (mod p),

so h mod p is a unit.

For 1<=r<=m the top ports B_{p-r} have valuation exactly two. Put

    y_r := B_{p-r}/p^2  (mod p).

The already-proved source reflection gives

    y_1=1/10,
    y_{r+1}/y_r = kappa_r
                := 36r^2/[(6r+5)(3r+2)].

Now define, for 0<=s<=m,

    g_s := g - sum_{r=s+1}^m B_{p-r},

    h_s := h - sum_{r=s+1}^m (12(p-r)+1)B_{p-r},

and

    Q_s := [ (g_s/p) h_s - 1 ] / p  (mod p).

This is a genuine fixed-p source construction. Since g-g_s is p^2-divisible, p|g_s; moreover g_s/p == g/p (mod p) and h_s == h (mod p), so the accepted UR digit implies the numerator defining Q_s is p-divisible. No moving modulus, fitted recurrence, or definition by R_s is used.

At the terminal cutoff,

    BOXED: Q_m = Delta_p := (G h-1)/p  (mod p).

Thus Q_0,...,Q_m is a lawful adjacent-cutoff extension of the actual D25 source residual.

## 2. Exact first difference

Passing from s-1 to s inserts exactly the source port B_{p-s}. Modulo p^3,

    g_s-g_{s-1} = p^2 y_s,

while h_s-h_{s-1} is also p^2-divisible. Therefore, after forming (g_s/p)h_s and dividing its difference by p, the h-increment is p-invisible and

    BOXED:
    U^Q_s := Q_s-Q_{s-1} = hbar y_s  (mod p),

where hbar:=h mod p.

This is a safe observer quotient: the dropped term is explicitly p times a p-integral source quantity after the final division; the top-port label s and normalized p^2 residue y_s are retained.

## 3. Canonical gauged curvature and its exact defect

Use the canonical lambda_s on this source extension:

    V^Q_s := U^Q_{s+1}-lambda_s U^Q_s.

Since y_{s+1}=kappa_s y_s,

    V^Q_s = hbar y_s F_s,

with

    BOXED:
    F_s = kappa_s-lambda_s
        = s^2(36s^2+72s+31)
          / [(s+1)(2s+1)(3s+2)(6s+5)].

Define the local canonical-curvature defect

    delta_s := V^Q_{s+1}-mu_s V^Q_s,
    1<=s<=m-2.

Then

    BOXED:
    delta_s = hbar y_s D_s,

where the compact exact form is

    D_s =
      kappa_s (kappa_{s+1}-lambda_{s+1})
      - mu_s (kappa_s-lambda_s),

and expansion gives

    D_s =
      s^2 N(s)
      / [36(s+1)^2(s+2)(2s+3)(3s+2)(3s+5)
         (6s+1)(6s+5)(6s+11)],

    N(s)=
      209952 s^7 + 1784592 s^6 + 6127488 s^5
      +11019240 s^4 +11136258 s^3 +6207741 s^2
      +1684551 s +146726.

Every coefficient of N is positive. Hence D_s>0 as a rational number for every integer s>=1. In particular, this lawful source cutoff does not satisfy the canonical mu-transport as a universal rational identity. The failure is not numerical noise; its exact residual is delta_s.

This is precisely the residual-faithful outcome required by the current research contract: retain the defect rather than rejecting the source construction or fitting it away.

## 4. The terminal curvature defect is nonzero for every nontrivial target

The strongest statement occurs at the final defect site s=m-2. Because p=6m+1,

    m == -1/6 (mod p).

Direct specialization of the exact rational factors gives

    D_{m-2} == -1363661/21168  (mod p),

and the reflected source recurrence gives

    y_{m-2}/y_m == 108/8281  (mod p).

Multiplying and reducing yields the source-normalized terminal identity

    BOXED:
    delta_{m-2}
      = -(8069/9604) hbar y_m       (mod p).              (T1)

For every target prime p>13:
- 9604=2^2*7^4 is a p-unit;
- 8069 == 5 (mod 24), so p cannot equal 8069;
- hbar is a unit by accepted UR;
- y_m is a unit by the explicit reflected product formula.

Therefore

    BOXED:
    delta_{m-2} != 0                 (mod p)

for every target prime p≡13,19 (mod 24) for which the defect site exists (p>=19). The exceptional smallest target p=13 has m=2 and no local-curvature index 1<=s<=m-2.

So the strongest/local factor-chain route delta_s=0 for all s is uniformly impossible for this natural lawful terminal-band extension.

## 5. Even the final two Green-visible defects cannot cancel by themselves

For the canonical endpoint observer, the final curvature defect has Green weight

    Gamma_{m-2,m}=1.

One step earlier, direct substitution in the canonical factor chain gives

    Gamma_{m-3,m}
      = 1+(1+rho_{m-2})lambda_{m-1}
      == 1209/28                         (mod p).

For the present source cutoff,

    delta_{m-3}/(hbar y_m)
      == 440673/48982115                 (mod p).

Combining it with (T1),

    BOXED:
    Gamma_{m-3,m} delta_{m-3}
      + Gamma_{m-2,m} delta_{m-2}

      = -(11913844/26374985) hbar y_m    (mod p).          (T2)

Here

    11913844 = 4*1487*2003,

with 1487==23 and 2003==11 (mod 24), while

    26374985 = 5*7^4*13^3.

Hence for every target prime p>13 for which both sites exist, the right side of (T2) is nonzero. The final two curvature defects therefore cannot mutually compensate at the endpoint.

This does not refute LIFT. It proves a sharper routing fact: any successful use of this Q_s must obtain endpoint cancellation from defects at least three layers earlier and/or from the explicit initial mismatch coordinates. A terminal-local repair is impossible.

## 6. BRC / information audit

Population:
the fixed-p top valuation-two source ports B_{p-r}, 1<=r<=m, embedded in the full accepted g,h source.

Observer:
Q_s in F_p and the terminal Q_m=Delta_p.

Preserved:
target prime, cutoff s, original top source index p-s, normalized p^2 residue y_s, the unit hbar, first difference U^Q_s, gauged curvature V^Q_s, local defect delta_s, and endpoint orientation.

Safe quotient:
the h_s top-port increment disappears from U^Q only after its exact p^2 valuation is propagated through the product and the final division by p.

Forbidden quotient:
do not set delta_s to zero; do not replace this construction by the canonical R_s; do not infer failure of LIFT from failure of local transport; do not use finite regression as proof.

BRC_REUSE_RESOLUTION = COMPOSE_APPLIED.

## 7. Deterministic regression

A companion exact modular checker independently reconstructs B_k modulo p^3, g_s,h_s,Q_s, the reflected y_s, U^Q,V^Q,delta, and the two terminal identities.

For all 166 target primes p<5000 (83 in each residue class 13 and 19 mod 24), it verifies:
- every Q_s is p-integral and Q_m equals the direct Delta_p;
- Q_s-Q_{s-1}=hbar y_s;
- the exact delta_s formula;
- (T1) whenever the final defect site exists;
- (T2) whenever the final two sites exist;
- the claimed terminal and two-layer quantities are nonzero in their stated ranges.

Failures: 0.

This finite check is falsification/regression only. The proof is the fixed-p source insertion calculation plus exact rational specialization above.

## 8. Narrow next action

Do not discard the present Q_s; it is now a useful negative control for source-derived cutoff design. It proves that varying only the terminal p^2 band is too weak for the strong local curvature route and too local for a two-layer endpoint repair.

The next source construction should therefore expose at least one lower-valuation source layer (a p-valued or unit-valued port) or a genuine parameter/Frobenius deformation, while keeping fixed p. For any such candidate:
1. compute U^Q and V^Q from source before comparison;
2. test local mu-transport;
3. if it fails, retain delta and use the endpoint Green pairing rather than rejecting the candidate;
4. preserve all initial mismatch coordinates.

LIFT/JT2 remains open.
