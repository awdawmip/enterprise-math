# D25 LIFT — synchronized p/p^2 source coupling is affine at the JT2 observer; the first genuine bilinear interaction is one digit deeper

Status: PROVED_STRICT_REDUCTION_UNIT / LIFT_NOT_YET_CLOSED / NOT_A_RESULT / UNREVIEWED
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT
Publication: TP2-B6F4FC938FF94941C1B7
Date: 2026-09-24
Consumed canonical Source frontier: awdawmip/enterprise-math@9ef2da4b524e07610a01406bed75c37227557ce7

## 0. Consumed frontier

Consume the durable D25 checkpoint through the two isolated source-layer negative controls. Do not reopen accepted D24 UR/JT0, the completed D25 shell/global-jet/Clausen/Green/symmetric-mass/adjoint/prefix-factor/prior-art/supersingular-repair units, or either one-band calculation.

For p=6m+1, p == 13 or 19 (mod 24), retain the accepted source

    B_k=(1/6)_k(1/3)_k/[(k!)^2 2^k],
    g=sum_{k=0}^{p-1} B_k,
    h=sum_{k=0}^{p-1}(12k+1)B_k,
    G=g/p.

The accepted first digit gives G h == 1 (mod p). Write Gbar=G mod p and hbar=h mod p. The exact source valuation bands are 0,1,2 on k<=m, m<k<=2m, 2m<k<p respectively.

The current checkpoint already provides the normalized middle and top ports

    x_s=B_{m+s}/p (mod p),
    y_s=B_{p-s}/p^2 (mod p),

with the repaired middle path and terminal path having first differences

    U^M_s=Gbar(12s-1)x_s,
    U^T_s=hbar y_s.

Both isolated paths have nonzero universal terminal curvature defects, but that does not decide whether labelled cross-layer interaction can repair the endpoint. This unit computes the smallest synchronized two-layer source extension exactly.

## 1. Lawful synchronized two-layer path

For 0<=s<=m define the omitted middle and top suffixes

    M^h_s = sum_{r=s+1}^m (12(m+r)+1) B_{m+r},

    T^g_s = sum_{r=s+1}^m B_{p-r},
    T^h_s = sum_{r=s+1}^m (12(p-r)+1) B_{p-r}.

Thus v_p(M^h_s)>=1 and v_p(T^g_s),v_p(T^h_s)>=2. Keep the already-required middle first-digit repair by retaining the full G, while allowing the top g-coordinate to vary. Define

    Q^M_s = [ G (h-M^h_s)-1 ]/p,

    Q^T_s = [ ((g-T^g_s)/p)(h-T^h_s)-1 ]/p,

    Q^C_s = [ ((g-T^g_s)/p)(h-M^h_s-T^h_s)-1 ]/p        (mod p).

Every displayed quotient is p-integral: (g-T^g_s)/p == G (mod p), while h-M^h_s-T^h_s == h (mod p), so the accepted unit relation Gbar*hbar=1 supplies the required first digit. At s=m all suffixes vanish and

    Q^M_m=Q^T_m=Q^C_m=Delta_p:=(Gh-1)/p (mod p).

No fitted recurrence or moving modulus is introduced.

## 2. Exact affine-superposition theorem

Before reducing modulo p, expand the four numerators. All constant terms cancel and one obtains the exact identity

    BOXED:
    Q^C_s-Q^M_s-Q^T_s+Delta_p = T^g_s M^h_s / p^2.       (A)

The right side has valuation at least one because v_p(T^g_s)>=2 and v_p(M^h_s)>=1. Therefore the current second-digit/JT2 observer sees

    BOXED:
    Q^C_s == Q^M_s+Q^T_s-Delta_p                      (mod p).     (A1)

This is the smallest exact two-layer result: the synchronized p-valued/p^2-valued coupling has no bilinear interaction visible at JT2. The apparent product between the layers is not discarded heuristically; its exact valuation proves that it enters only one digit later.

Indeed, modulo p^2 after the final division, the first omitted interaction is

    BOXED:
    Q^C_s-Q^M_s-Q^T_s+Delta_p == p Xi_s               (mod p^2),

    Xi_s := (T^g_s/p^2)(M^h_s/p)                       (mod p).    (A2)

Thus Xi_s is a genuine labelled cross-layer coordinate, but it belongs to the next digit beyond the present JT2 observer. It must be retained if the research later advances one p-adic digit deeper.

## 3. Consequence for the canonical first-order factor chain

Because Delta_p is constant in s, (A1) immediately gives

    BOXED: U^C_s=U^M_s+U^T_s
                 =Gbar(12s-1)x_s+hbar y_s.             (U)

The canonical lambda/mu transforms are linear, hence without any additional hypothesis

    BOXED: V^C_s=V^M_s+V^T_s,

    BOXED: delta^C_s=delta^M_s+delta^T_s.               (D)

Therefore the natural synchronized two-layer extension creates no new nonlinear local repair mechanism at the current observer. Any success on this route must come from additive cancellation of the two provenance-labelled defect streams together with the already-required initial mismatch/endpoint coordinates, or from a genuinely different deformation that changes the retained first-digit repair data.

At the final local-curvature site s=m-2, consuming the two already-proved one-band formulas yields

    BOXED:
    delta^C_{m-2}
      = -(42062/343) Gbar x_m
        -(8069/9604) hbar y_m                            (mod p).   (T)

This formula is a superposition identity, not a claim that the sum is universally nonzero.

## 4. Strict separation witness: local no-go is not stable under coupling

The exact checker finds a useful finite separation witness at p=163, m=27. Direct source reconstruction gives

    Gbar=154, hbar=18, x_m=150, y_m=22  (mod 163),

and the two labelled terminal defects are

    delta^M_{m-2}=60,
    delta^T_{m-2}=103,

so

    BOXED: delta^C_{m-2}=60+103=0 (mod 163).

Thus the isolated facts delta^M_{m-2}!=0 and delta^T_{m-2}!=0 cannot be combined into a universal two-layer terminal obstruction. The p=163 witness is finite evidence of logical separation only; it is not promoted into an all-prime cancellation law.

This makes the BRC provenance requirement mathematically active: the two source streams must remain labelled until the endpoint observer is evaluated. Declaring each stream bad before allowing their signed sum would erase a real cancellation channel.

## 5. Endpoint regression and what it does not prove

A companion exact modular checker reconstructs the full source modulo p^3 for every target prime p<5000 (166 primes, 83 in each residue class). It verifies with zero failures:

- p-integrality and the common endpoint Q^M_m=Q^T_m=Q^C_m=Delta_p;
- the exact affine identity (A) at the p^2 quotient precision and (A1) modulo p;
- U, V and delta linearity in (U),(D);
- the terminal formula (T);
- the p=163 separation witness;
- independently, the already-defined universal-prefix endpoint R_m equals the directly reconstructed Delta_p for all 166 tested targets.

The last item is only regression/falsification evidence for the surviving LIFT endpoint identity. It is not an all-prime proof and does not close LIFT/JT2.

## 6. BRC audit

Population: two source layers at fixed p, the middle ports B_{m+s} of valuation one and reflected top ports B_{p-s} of valuation two.
Observer: the divided second digit Delta_p modulo p together with adjacent synchronized cutoff operations and canonical lambda/mu/Green endpoint operations.
Preserved: p, cutoff s, layer label, original source index, valuation, x_s,y_s, first-digit repair coordinate, Q^M,Q^T,Q^C,U,V,delta and the deeper interaction Xi_s.
Safe compression: Q^C -> Q^M+Q^T-Delta only after (A) and the valuation bound prove the cross term p-invisible at JT2.
Forbidden compression: erase layer labels before signed endpoint cancellation; discard Xi_s if advancing to the next p-adic digit; infer an all-prime identity from p=163 or the 166-prime regression.
BRC_REUSE_RESOLUTION=COMPOSE_APPLIED.

## 7. Narrow next action

Do not search for another synchronized scalar two-band cutoff: theorem (A) proves that this whole construction class linearizes at the current JT2 observer. The next proof-level unit should do one of two things:

1. keep the two labelled defect streams and derive the complete finite Green endpoint pairing, including the initial Q/U/V mismatch coordinates, seeking an exact symbolic cancellation to R_m; or
2. construct a genuine parameter/Frobenius deformation that changes the retained first-digit repair coordinate so that a JT2-visible interaction can occur.

If the full additive Green pairing has a nonzero exact residual, persist that residual as the next strict reduction. LIFT/JT2 remains open.
