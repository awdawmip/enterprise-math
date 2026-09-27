# Carry executor: bounded review plan and a native noncommuting witness

Status: static source/evidence review only; no new scientific arithmetic,
matrix multiplication, kernel execution or external query was performed.
The parent owns implementation and actual tests. This is shared-context
author support, not independent admission.

## Frozen interfaces inspected

- `optimization/collision_analysis/gram_sampler.py`, SHA-256
  `468de944518fbc6afa81a17555676436376da63921a784c810ffe8fab3ca17e9`:
  `_left` applies complete native words to all matrix columns;
  `_right_transpose` uses transpose/left/transpose without reversing the
  gates; `_sum` uses the inherited signed PositivePathObserver; `_combine`
  aligns dyadic denominators and contributes exactly one factor 1/4.
- `optimization/carrier_codec/carrier_codec.py`, SHA-256
  `c25149e0ab4ce92a59d2ca40cb697fe6505cd1dc8d406e9c5a2d92cb2b28c953`:
  restriction freshly reconstructs the full native word, verifies its cached
  fields, checks both forward and inverse blocks, and requires identity on
  the omitted complement. Encoding rejects a nonzero omitted residual.
- `optimization/collision_analysis/check_gram_sampler.py`:
  its bank loader reads the complete direct-word compilation payload with
  SHA-256 `79491e65feec104f2cdc9de510263efef749d8a1174f9cab4c20146a0171615c`
  and re-admits it with `t=4, epsilon=1`.

These optimization sources are pinned at EM commit
`0e6380ff74d31b842ba0b54802c1f0595a7dd60d`, under
`research_notes/directed_recovery/20260926_C6438C/optimization/`.
The phase compilation is at EM commit
`9348fc6abdf45becbd12a8019d93f72d576b9fab`, path
`research_notes/directed_recovery/20260926_C6438C/direct_word_integration/DIRECT_WORD_INTEGRATION_RESULTS.json.gz`.
Its gzip SHA-256 is
`ef981768a20a72a67bfd7d01284d1b946cfc95ded96552a07571c436964d1460`.

## An already reachable noncommuting feedback prefix

Use the prior actual fixture `N=21, a=2, t=4`, prefix `h=(1,0,1)`.
The frozen `GRAM_SAMPLER_RESULTS.json.gz` contains both D=6 and D=61 runs
of the longer history `(1,0,1,0)` with every prefix retained. Its D=6 checks
record the selected mass after the first three bits as

    1011331799 / 4294967296 > 0.

This establishes reachability from existing execution evidence; no new
sampling or ordinary reference propagation was used to choose the fixture.

By the actual `_gates(depth)` source, chronological feedback for these three
rounds is `T0=I, T1=Q=bank[2], T2=R=bank[3]`. The certified bank's
`phase_compilation.phases[m].certificate.actual_columns.complete_basis_columns`
provides the following exact previously executed column entries:

- Q e0 = -e1, and Q fixes coordinate 2;
- coordinate 2 of R e0 is `-1419/4194304`;
- coordinate 2 of R e1 is `-18807/134217728`.

Consequently coordinate 2 of Q R e0 is negative, whereas that of R Q e0
is positive. This is a symbolic consequence of the stored full native
columns and the signed-permutation Q, not a newly computed ordinary matrix
product. The two words genuinely fail to commute on the relevant input.

The signs for h are (-,+,-), so the all-one preparation path has

    U(7) = (-R) Q (-I) e0 = R Q e0.

For i=3,d=7 there is only the pair n=0,m=7. Therefore

    C_h(7) = e0 (R Q e0)^T / 64.

Its (row 0,column 2) entry is positive. A reversed temporal product produces
Q R instead and changes that entry's sign. This is a particularly small,
high-value order/overflow test. In fact the stored columns also give
R[0,1]=94887584/134217728=2965237/4194304=-R[1,0]. Hence RQe0 and QRe0
have the same coordinate 0, so a trace-only C(7) check would miss this
particular order error. The residual matrix entry distinguishes it.

## Exact D6 use is supported by prior evidence

The same prior Gram case records the full-bank codec binding

    01e92cca058b66eb220588d0d29eac23ee8eb9b7d9baa5a572a0f174c2a9c265

with indices `[0,1,2,3,4,5]`, full dimension 61, encoded dimension 6 and
`all_forward_inverse_blocks_checked=true`. Its bound full-column digests are

    m2: 5aa4e5feafa3cf21278ec916ebd0edbdda7d10ef2ca79d8e86acc7f0271d82f3
    m3: 5f8a9c76671e818401caa74e3879c6e22a497c4a2fc0dc15b0729418eed7317c

Fresh admission of the complete bank and fresh codec validation remain the
parent's execution contract. The D6 matrices are exact word-boundary
coordinates for all reachable residuals; intermediate native letters may
visit other coordinates. Do not restrict those letters or interpret this
as physical truncation. For a correlation, full-carrier recovery is the
two-sided embedding J C6 J^T, not only row-vector decoding.

## Small test set with distinct failure modes

1. **Basis and empty interval.** Empty history, d=0 returns e0e0^T with
   denominator 1, not I or zero. Empty history with d!=0 returns the zero
   matrix. These distinguish the initial pure seed without expensive gates.
2. **One-bit sign/scale and overflow.** With the formal prefix h=(1),
   compare d=0,+1,-1 and +/-2. The first feedback is I, hence the coefficient
   identities are C(0)=e0e0^T/2 and C(+1)=C(-1)=-e0e0^T/4. The two out-of-range
   coefficients are zero. This checks one 1/4 per layer and both carry
   boundaries. A coefficient remains defined even if a modular collision
   makes that history's total mass zero; conditioning must separately reject
   M<=0.
3. **Reachable noncommuting prefix.** At N21/h101/i3 compare d=1 and d=7
   against a bounded explicit sum of the same native preparation paths,
   retaining every matrix entry. d=1 exercises internal carry alternatives;
   d=7 isolates the chronological product above. Also compare negative d
   with the positive matrix transpose and check |d|>=8 yields zero. If budget
   allows, all 15 in-range displacements provide complete bounded coverage
   for only eight preparation paths.
4. **Alias/observer orientation.** At that prefix compare the full assembled
   Gamma(1), Gamma(p_next), and Gamma(b) against the old Gram recurrence and
   an explicit same-word row correlation. Here b is the certified current
   parent multiplier, obtained from actual schedule data. Gamma(p_next) may
   be zero, and Gamma(1) is symmetric; the extra Gamma(b) query is important
   for catching transposition mistakes that trace-only checks miss. Discover
   its aliases with the authorized typed route, not a supplied order.
5. **One D61 boundary check.** For the noncommuting d=7 case, compare the
   entire full D61 correlation with J C6 J^T, including all zero complement
   entries. Together with admitted full-word codec invariance, this gives a
   bounded representation check rather than a trace-only comparison.
6. **Binding/input negatives.** Reject boolean or noninteger d/history bits,
   histories beyond t, and incompatible program dimensions/bank bindings.
   If reuse is supported, ensure a cached (depth,d) answer cannot be returned
   after changing earlier history or a phase word. Bind cached or exported
   results to the actual source, normalized complete word bank, codec and
   exact history. Zero-mass histories must not become conditional samplers.

Tests 1-3 target the new carry recurrence. Tests 4-5 check its use in the
existing actual instrument. These are proposed tests, not claims that they
have run. Any explicit reference must use the same admitted native words
and authorized signed arithmetic, with no ideal-QFT or float replacement.

## Source-review checklist for the forthcoming implementation

- Fresh Y arrays per high-to-low digit; state index meaning switches from
  c_(p+1) to c_p, with both outer endpoints fixed to zero.
- Seed the encoded e0 projector only in the high carry 0 branch.
- Apply O_j on the left/right only when its corresponding path bit is one;
  readout sign appears once per selected arm and is not applied twice.
- `_combine` already divides by four. Do not divide again at return, and
  do not divide once for every alternative term. Empty carry branches need
  an explicit zero correlation rather than `max()` on an empty list.
- `_right_transpose` must retain the source gate order. Reversing the gate
  tuple because it acts on the right would change the intended operator.
- Preserve all matrix entries, raw denominators, negative contributions and
  word-boundary residuals. The identity trace C_h(0)=2^-i does not certify
  the full coefficient or the history mass.
- Distinguish arithmetic calls, native-vector actions, matrix slots,
  numerator/denominator bit lengths, receipts and alias-discovery work.
- Mathematical coefficient evaluation on a fixed history and conditional
  sampling are different entry contracts; keep the M>0 condition explicit.

Global-Knowledge-Sync: main@06788df / GLOBAL_KNOWLEDGE_V1
