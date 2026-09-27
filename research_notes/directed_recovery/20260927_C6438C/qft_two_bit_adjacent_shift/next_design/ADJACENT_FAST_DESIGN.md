# Adjacent-bit point evaluation, balanced modulus, and setup reuse

Status: SYMBOLIC / STATIC_SOURCE_REVIEW / NOT_EXECUTED / NOT_ADMITTED.
This is a new version proposal. No scientific module was imported or run,
no numerical reference was computed, and no frozen source or evidence changed.
The only new executed script reads and counts already saved record metadata.
The coordinator can implement and run a separately reviewed bounded successor
under the existing research authorization; this document is portable mathematical
work and does not require a particular environment for further derivation.

## 1. Contract and exact dependencies

Keep strict integer inputs g>=2, 0<=ell, k=ell+1<g, R>=1, 0<=r<R,
and stride=1. Put V=2^ell, U=2V, P=4V, H=2^(g-k-1), L=HP=2^g.
The scalar sign is s(x)=(-1)^(bit_ell(x)+bit_k(x)) and

    A_s(d)=sum_(0<=x<L-d) s(x)s(x+d), 0<=d<L,
    K(r)=sum_(0<=x,y<L; y-x congruent r mod R) s(x)s(y).

The two positive-magnitude progressions have heads r and R-r, step R,
exclusive limit L. Keep both when their heads coincide; only the first has
d=0 when r=0. Preserve the raw denominator exponent 2g, supplied-order/address
scope, signed outputs, and all external matrix weights unchanged.

Read sources (all SHA-256):

- `../sep27-qft-two-bit-adjacent-shift/ADJACENT_SHIFT_REDUCTION.md`:
  `96757c3624c69bf3ec1e313504f56bb6099d1a79e47032813084b19340c272ad`.
- Its `adjacent_shift.py`:
  `bee8a702062dfb16a75139a63b6c52b9451a02834a5b3033f5d52fcaebff9c6e`.
- `../sep27-qft-gap-direct/DIFFERENCE_AUTOCORRELATION.md`:
  `c0c3765fce7d07f383f1ebfcb514dd8483485944bfeb202d024dd21e69205cbf`.
- Its `direct_gap/direct_signed_gap.py`:
  `3ab2515c1b9df35d01c9605f21d8f8fe56bd044effe489063192c0a5c56a8521`.
- Static setup/point/replay reference `../sep27-qft-two-bit-top-fast/top_bit_fast.py`:
  `8c73aa1ad2f195b9d8f440112dac7b08cacbc1e544e65850a754dc38f2fa48e8`.
- Frozen degree-three runner `../sep27-qft-adaptive/nonzero_structure/typed_floor_moments.py`:
  `633502c9b484e60e5dc5fcf6edd0420f12d52c33c43e88851b9e1e6465ea94a2`.

The setup and terminal-failure design below borrows the top-fast architecture,
not its highest-bit-only mathematical formula. Adjacent non-top inputs remain
valid. No degree-five dependency is added.

## 2. A single displacement needs no floor-moment table

Let d=qP+z, 0<=z<P, 0<=q<H, and h=H-q. The frozen one-bit formula for
f(x)=(-1)^bit_k(x) is

    A_f(d)=h(P-4z)+z,                 0<=z<=2V,
            h(4z-3P)-3z+2P,          2V<=z<P.

The frozen adjacent correction A_s(d)-A_f(d) is -2z on [0,V],
2z-4V on [V,3V], and 8V-2z on [3V,P]. Therefore

    A_s(d)=h(P-4z)-z,                0<=z<V,
            h(P-4z)+3z-4V,           V<=z<2V,
            h(4z-3P)-z+4V,           2V<=z<3V,
            h(4z-3P)-5z+4P,          3V<=z<P.                 (1)

This is obtained by adding exact expressions; it introduces no propagation,
normalization, floating point, trigonometry, or period enumeration. Junctions
agree: z=V gives -V; z=2V gives -hP+2V; z=3V gives V. At z=0 the
answer is hP=L-d. As z reaches P the fourth expression gives (h-1)P,
which is the next period's z=0 value. The displacement d=L is outside the
point routine: it is an empty progression, not a point to evaluate with q=H.
These are symbolic identities, not newly executed numeric fixtures.

A typed point routine performs division d by P, subtraction H-q, saved
comparisons of z with V, 2V and 3V, and the selected expression (1). Negative
intermediate/results are legitimate. Every comparison should reference an
actual typed difference/sign observation; host branches select the formula
but must not supply a new scientific value. The same typed quotient and
remainder are shared by the base and correction interpretation; do not call
the old base progression and then a separate point correction.

## 3. Empty and singleton progressions

For head b>=0 and step R>0, first compute a typed t=L-1-b.

- If t<0, route EMPTY, return an actual typed zero, and record no point or
  moment call. The old version already avoids tables here; the new saving is
  avoiding unnecessary coefficient setup and base-helper work.
- Otherwise compute typed (q_len,rem)=divmod(t,R) and n=q_len+1.
  If n=1, route SINGLE_DISPLACEMENT and evaluate (1) at d=b.
- If n>=2, route FLOOR_MOMENTS and retain the frozen two base plus two
  correction tables, their complete outer arithmetic, and full receipts.

This conservative design keeps the existing paid length formula instead of
claiming an unmeasured comparison-based division saving. Do not evaluate the
point formula before proving b<L. Do not erase a complete empty request from
chronological evidence. A schema can mark its omitted table work explicitly
with `table_calls=[]`; it must not fabricate a table result of zero.

No route depends on the resulting correlation value. In particular a zero
point value does not authorize skipping already required typed work.

## 4. R=1 is an exact full-query zero, not an orientation zero

Each period of s consists of four length-V blocks with signs +,-,-,+.
Their sum is zero. Since P divides L, sum_(0<=x<L)s(x)=0. At modulus one
every ordered pair is admitted, hence

    K(0)=(sum_x s(x))^2=0.                                  (2)

The existing input contract enforces r=0 when R=1. Apply all strict input,
source, stride, and terminal-state checks before this shortcut. Record a
typed modulus-unit witness, for example R-1=0, a typed zero output and the
bound proof/domain. This theorem permits omitting even scale construction:
g>=k+1=ell+2 proves symbolically that L contains whole periods. It does not
permit the host to numerically manufacture powers, counts, or correlations.

Use route BALANCED_MODULUS_ONE, with orientation evaluation marked omitted
by this whole-query theorem, not a pair of asserted zero orientation values.
Those two separate sums need not vanish. Preserve the input and denominator
exponent 2g. Other R values continue to both orientations; no unproved wider
zero family or result-dependent dispatcher is introduced.

There is also a broader proved sufficient condition, identified by the
coordinator: R divides U. The identity s(x+U)=-s(x) pairs the first half of
each length-P block with its second half. If R|U these paired labels are in
the same residue class. Thus every class sum S_c=sum_(x congruent c mod R)s(x)
is zero, and K(r)=sum_c S_c*S_(c+r)=0 for every r. This does not require V|R,
factorization, or an order value. A generalized implementation must pay for
construction of U and typed division U by R and preserve its remainder
witness; a failed divisibility test is also charged. The minimal proposed
version selects only R=1 after strict public-input validation and pays the
modulus-unit witness, avoiding an extra divisibility test on every non-hit.
On the six saved fixtures only R=1 meets R|U, so their route census is
unchanged. The general theorem is not represented as an executed predicate.

## 5. Observer-local lazy setup and chronology

Use composition around the frozen DirectSignedGapObserver and its actual
runner, as in top-fast. This avoids repurposing the inherited direct source
hash. The wrapper binds its own source/proof, adjacent source/proof, direct
source/proof and the actual arithmetic dependencies. Keep the generic old
`one_negative` entry unavailable on this new public interface.

After admission and the R=1 test, cache scale setup by `(g,ell,k)`; k is
redundant after validation but explicit. The key also belongs to one fixed
source/profile/domain instance. It may omit R and r because V,U,P,H,L do not
depend on them. Do not treat a mutable process-global dictionary or an
unverified deserialized setup as proof. Cache records include inputs, values,
signed-operation spans, completion flag, and all actual operation references.

Construct the expensive base and correction coefficient bundle only when
the first n>=2 orientation requests it. Cache it under the corresponding
setup index, with complete provenance. Point-only or empty requests should
never force table coefficients. At most one bundle is constructed per setup;
the n>=2 routine must accept the already paid length and setup, rather than
recomputing either through the old public whole-query method. Reuse the
already paid S_d within base/correction as the current source does.

Each request records setup index/hit, route, typed length, point piece or
table parameters, source-bound coefficient reference, final addition, and
actual operation spans. Attach an unfinished request/orientation/setup before
starting its typed work. A provisional cache entry is not usable until marked
complete. Any exception after admitted work makes the observer terminal;
further scientific calls/export reject while incomplete_snapshot retains the
available typed/signed/native work. Early invalid inputs before work can
remain recoverable, but must neither modify cache nor consume arithmetic.
Do not promise preservation of semantic objects that were never attached;
the raw operation stream is the fallback evidence.

Fresh verification reconstructs an empty observer and replays all requests
in order, thereby reconstructing cache hits and charged setup exactly. Then
strictly compare the full semantic certificate, excluding only the existing
native runtime-delta field. Changing setup index, hit flag, completion,
piece, length, omitted-table list, source or output must reject. Completed
evidence costs each stream operation once; repeated setup references are
not new arithmetic. A failed replay retains the actual prefix, not a guessed
complete certificate. No cross-process persisted-cache admission is proposed.

## 6. Saved-record applicability and honest cost prediction

The companion stdlib-only metadata reader binds the already executed adjacent
raw and only classifies its saved lengths. Its route census is:

| Existing fixture (g,ell,k,R) | Empty | Singleton | Multiple | Old tables | Proposed tables |
|---|---:|---:|---:|---:|---:|
| (3,0,1,5) | 0 | 5 | 5 | 40 | 20 |
| (4,0,1,5) | 0 | 0 | 10 | 40 | 40 |
| (4,1,2,6) | 0 | 0 | 12 | 48 | 48 |
| (4,1,2,9) | 0 | 5 | 13 | 72 | 52 |
| (3,0,1,11) | 7 | 15 | 0 | 60 | 0 |
| (4,0,1,1) | 0 | 0 | 2 | 8 | 0 |
| Total | 7 | 25 | 42 | 268 | 160 |

Thus the specified routes remove 100 table calls for 25 singleton
orientations and eight for the balanced modulus-one query. This is a proven
counterfactual top-level-call count for the saved inputs, not new execution.
Distinct recursive nodes and internal cache hits need not fall in the same
ratio. Half-modulus orientations remain duplicated, even if an internal
moment cache happens to serve identical parameters.

Keeping the checker's six separate observers, scale setup falls from 37
per-query constructions to five (the R=1 observer needs none), and expensive
coefficient bundles from 37 to four (the R=11 observer is point-only).
There are only three distinct mathematical setup keys across the grid, but
claiming three actual constructions would improperly assume cross-observer
reuse. This proposal does not change that execution layout.

Frozen production was 126950 typed digit steps versus brute 52700. Its
disjoint source-span charges include 33375 base-table and 43616 correction-
table steps, 29503 base outer and 12184 correction outer steps, 543 scale,
5698 base-coefficient, 489 correction-coefficient, 224 empty-base, and 1318
routing/final steps. These numbers identify opportunities; they are not the
savings. Point routing/division, strict replay, snapshots and serialization
remain charged. In particular two fixtures retain all their table calls.
No new digit total, speedup, elapsed-time ratio, or full-Shor improvement is
established. Arbitrary bit length still costs actual typed digit work; setup
power construction is not constant in g. R/order/address discovery is still
external and paid separately.

## 7. Minimum successor validation

Reuse the hash-bound 37 historical values without rerunning their 1152 pair
comparisons. Retain the same six observers/all residues so the route census
is testable, including R>L empties, duplicate half-modulus orientations,
non-top k, negative outputs, and the balanced R=1 query. A new bounded checker
should save complete production, fresh replay, paid/early negatives and
terminal-reuse costs separately. Mutations should cover a point junction or
piece, n/empty route, setup reference/hit, lazy coefficient state, forged R=1
omission, source/schema/output and the preserved two-orientation multiplicity.
Any untested exact junction remains a proof boundary, not an executed fixture.
Protect both successful and failed output paths before starting; preserve
unexpected failures, and do not retry them invisibly.

The result is a concrete scalar-observer optimization design. It does not
close general separated-bit masks, full matrix correlation, hidden order,
or complete Shor simulation complexity.

Global-Knowledge-Sync: main@52978d9 / GLOBAL_KNOWLEDGE_V1
