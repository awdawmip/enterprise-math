# No finite carry-symbol history determines the next S23/AV symbol

Date: 2026-11-09 (Asia/Shanghai). Status: AUTHOR_SIDE / UNREVIEWED / NOT_ADMITTED.
Frozen science: 43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Companion: PROOF.md and VERIFY_EDGE_PREFIX.py in the same directory, source e94a4146c640f7025227bd2cce534eb164ce9d77.
This theorem concerns the auxiliary irrational-rotation carry coding, not the native X6 temporal dynamics.

## Exact theorem

Let alpha be the irrational number from the frozen S23/AV auxiliary model and B=79.
For every k>=1, C_k=floor(B {k alpha}).

For every integer m>=1 there exist infinitely many pairs of indices k,l >=m such that
  (C_(k-m+1),...,C_k)=(C_(l-m+1),...,C_l)
but
  C_(k+1) != C_(l+1).

Thus no fixed finite m and no function f:{0,...,B-1}^m -> {0,...,B-1}
can satisfy C_(k+1)=f(C_(k-m+1),...,C_k) for all k>=m.

## Proof (all integers m>=1)

Work on the unit circle R/Z with x_k={k alpha}. For a prospective current
phase x, the past m symbols (current through m-1 previous) are
  W_m(x)=(floor(B{x-(m-1)alpha}),...,floor(B{x})).
This vector is locally constant away from its finite boundary set
  D_m = union_(j=0)^(m-1) {a/B+j alpha (mod1): a=0,...,B-1}.
The next symbol is V(x)=floor(B{x+alpha}); its boundary set is
  D_next={a/B-alpha (mod1): a=0,...,B-1}.

No member of D_next belongs to D_m. Indeed an equality would give
(a-b)/B=(j+1)alpha (mod1) for some integer j>=0, forcing alpha rational,
contrary to the inherited irrationality theorem.

Pick any x* in D_next. Since D_m is finite and x* is not in it, there
are two open adjacent intervals I_minus,I_plus on opposite sides of x*
that lie in a single atom of W_m, so W_m is identical on both intervals.
The next-symbol readout V changes across x*, hence has different values
on these two intervals.

The forward irrational orbit {k alpha}, k>=m, visits each nonempty open
interval infinitely often (density/minimality of irrational rotation).
Choose arbitrarily late indices k,l with x_k in I_minus and x_l in
I_plus. Then their last m carry symbols agree but their next symbols
differ. Infinitely many such pairs exist. QED.

## Why this extends the 79-state branch result

The earlier two-successor law proves current C_k alone is not a
deterministic next-state carrier. The theorem above eliminates *every
fixed finite window of carry symbols* as a globally sufficient
deterministic state. The exact phase z_k={79k alpha} together with C_k
remains a sufficient one-step representation; there can be other
information-equivalent representations or unbounded-history recoveries.
This is a scoped BRC observation-fiber nonconstancy theorem.

## Executed exact finite witnesses

VERIFY_NO_FINITE_MEMORY.py certifies each C_k up through k=50000
from the same 160-term strict rational interval for alpha and finds:
m=1:  k=4 and 45, next symbols 73/74;
m=2:  k=15 and 85, next 29/28;
m=4:  k=14 and 125, next 61/62;
m=8:  k=14 and 125, next 61/62;
m=16: k=117 and 228, next 7/8;
m=32: k=41 and 777, next 47/46;
m=64: k=1311 and 2047, next 24/23.
The proof establishes all m; the finite examples are independent
program-level checks of the first selected m values.

## Next

The memory obstruction identifies where phase repair is mathematically
essential. Test whether exact phase-aware witness classes can transfer
critical-cell coverage at plateau i=412. This requires checking the
actual interval geometry, not just its transition coding.
