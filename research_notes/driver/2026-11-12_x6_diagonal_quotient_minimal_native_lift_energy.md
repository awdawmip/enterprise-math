# X6 diagonal quotient: exact least-native-gauge lift and recovery ambiguity

Status: DRIVER_MATHEMATICAL_AUDIT / PROVED_AUXILIARY_LEMMA / NOT_NATIVE_RESULT_ADMISSION
Date: 2026-11-12 (Asia/Shanghai)
Scope: raw centered signed three-axis slice (d\in\mathbb Z^3), diagonal translation quotient (\mathbb Z^3/\mathbb Z(1,1,1)). No Foundation or native metric redefinition.
Associated task: RS-X6-LEGACY-PLANE-RECONCILIATION, TP2-B4A441B23DA3159232C2; historical Result RR-943A793DB1F7B8012A85, HRI-1A48B2D7F0E242FCC2C57D7E (REQUEST_REVISION).
Context/attribution: preserves original X6 legacy-plane work by EM-X6P-40B5BD, the retyped quotient and gauge definitions stewarded in the existing Source, and the prior Driver LP-011 audit. This is a shared-context follow-on, not a blind independent review, CLAIM, formal Result or change of the historical disposition.

## Typed setup and exact theorem

Let (r=\rho(d)=d-\min_i(d_i)\mathbf 1\), so (r\in\mathbb Z_{\ge0}^3\) with (\min r=0\), and every native signed lift of the same observer address is (d_\mu=r+\mu\mathbf1\), (\mu\in\mathbb Z\). Put
(S=r_1+r_2+r_3), (N=\sum_i r_i^2),
(Q_{\mathrm{car}}(r)=\sum_i r_i^2-\sum_{i<j}r_ir_j\), the existing diagonal-invariant classical *carrier* quadratic, and (G(d)=\sum_i d_i^2\), the native signed-slice squared gauge.

The following equations hold exactly:

1. **Observer-fiber native gauge:**
   [
     G(d_\mu)=N+2S\mu+3\mu^2.
   ]
2. **Least-gauge representative and exact bridge to the carrier quadratic:**
   [
     \mu_*=-\left\lfloor\frac{S+1}{3}\right\rfloor,qquad
     G_*(r):=\min_{\mu\in\mathbb Z}G(d_\mu)
     =N-\left\lfloor\frac{S^2}{3}\right\rfloor
     =\left\lceil\frac{2Q_{\mathrm{car}}(r)}3\right\rceil.
   ]
   The minimizing integer lift is **unique**. This (G_*) is a derived variational observable of the quotient, **not** the value of (G(d)) for an arbitrary native Cell/path displacement and **not** an identification of (Q_{\mathrm{car}}) with the native metric.
3. **Complete fiber energy spectrum:** with (t=\mu-\mu_*\in\mathbb Z) and (\epsilon=S+3\mu_*\in\{-1,0,1\}),
   [
     G(d_\mu)=G_*(r)+3t^2+2\epsilon t.
   ]
   Thus the observer chart plus an exact native squared gauge (G) determines the native common level (\mu) **uniquely if** (3\nmid S). If (3\mid S), every admissible nonminimum gauge has exactly two lifts (\mu_*\pm t), while (G=G_*) has one. This is an exact description of the remaining information loss after also supplying (G).
4. **Reversal intertwines, but does not equate, observer and native gauge:** if (Q=\max_i r_i),
   [
      \rho(-d)=Q\mathbf1-r,
   ]
   an involution of min-zero charts. It preserves (Q_{\mathrm{car}}) and (G_*) while the native reversal preserves (G(d)). The uncorrected positive-section sum of squares (N(r)) need not be reversal-invariant:
   [
      N(r)-N(Q\mathbf1-r)=2QS-3Q^2.
   ]

## Proof

Expanding \(\|r+\mu\mathbf1\|_2^2\) proves (1). Completing the square gives
\(G=N-S^2/3+3(\mu+S/3)^2\). Because \(S\in\mathbb Z\), the nearest integer to \(-S/3\) is unique and equals \(-\lfloor(S+1)/3\rfloor\); the squared correction is zero or \(1/3\). Since \(3N-S^2=2Q_{\mathrm{car}}\), taking the integer ceiling yields the third expression in (2), and completing the square or direct substitution gives the first two. Set \(\mu=\mu_*+t\) to obtain (3). If \(G(d_\mu)=G(d_\nu)\), then \((\mu-\nu)(3(\mu+\nu)+2S)=0\). Distinct integer lifts can share a squared gauge iff \(3\mid S\), in which case they are symmetric around \(\mu_*=-S/3\). Finally \(\min(-d)=-\max(d)=-\mu-Q\) proves the reversal chart identity; the quadratic and (N) identities follow by expansion. QED.

## Exact diagnostic example

For (r=(3,4,0)), (S=7), (Q_{\mathrm{car}}=13), (\mu_*=-2), (G_*=9). The native displacement (d=(3,4,0)) instead has (G(d)=25). Its native reverse is ((-3,-4,0)), also gauge 25, whereas the reverse *observer representative* is ((1,0,4)), with naive squared section value 17. Both observer addresses have least-lift squared gauge 9. This extends the existing historical LP-013 witness without changing its source semantics.

## Supplementary finite exact verification

In Python 3, enumerate all 127 min-zero triples (r\in\{0,\ldots,6\}^3). For each, compare (G_*) against `ceil(2*Q_car/3)`, test all sampled levels (\mu\in[-8,8]\) against the energy-spectrum formula, verify the global minimizer using (\mu\in[-10,10]\), and test every pair of sampled integer levels (\mu<\nu\) from ([-7,7]) for the collision criterion. Results: **0 discrepancies** across the stated finite domain; 43 charts have (S\equiv0\pmod3), 42 each have residues 1 and 2. The proof above is universal; this computation is a regression check, not its logical basis.

## Relation to current Source and remaining work

This note adds an exact quantitative bridge to the previously defined quotient carrier form in `definitions/ENTERPRISE_DERIVED_DIAGONAL_DISPLACEMENT_QUOTIENT_20260826.md` (verified blob `175d2c0f00db8e94a263442dbdc77928c0dc9567`), native gauge and observer retyping in `definitions/ENTERPRISE_ARBITRARY_POINT_DIRECTED_LINE_GAUGE_20260821.md` (blob `875e3b274e5be03c5872f782872065a0b96d14eb`), and the prior `research_notes/driver/2026-11-12_x6_lp011_observer_axis_minimal_side_channel.md` (blob `8eb065792d646594d16132626e14e9439fa30878`). It does not establish physical rotation, path-fiber equivalence or BRC multiplicity from quotient data. The X6 historical HRI remains REQUEST_REVISION: original LP-011 pre-rebase wording provenance and the `recomputation_summary.json` secondary digest conflict still need source reconciliation. The frozen custody map records declared `a40e89f66ffa42b684b918780994cdfd86b176eebdd3a71d87b89c815e975839` versus byte-custody `21ac687263bc55283be5e50dcbab8dd3b6024900a323f941b3f703077cebf46f`, while the original primary Git blob is `c6d42b50e75a9c05e93e922e88ddfd9f1e2eb14a`; this discrepancy is not resolved by the new mathematics.

Next scientific discriminator: for signed BRC path words, determine which path-fiber properties, if any, factor through (r,G(d)) alone; test explicit double-lift cases when (3\mid S), without conflating native signed displacements with quotient representatives.
