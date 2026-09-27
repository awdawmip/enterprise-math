# Segmented strict program views with an exact compatibility fallback

Status: design and source inspection only. No implementation, metadata experiment, native arithmetic, benchmark or new scientific activity was executed for this directory. Existing trace/boundary files remain frozen. The proposed optimization changes representation of a binding comparison; it does not change scientific words, trace bounds, error budgets or Gram propagation.

## 1. Inspected frozen boundary

The relevant source chain is:

- `sep27-qft-uniform/word_certificates/word_certificates.py`, SHA-256 `c3e8156b5c7573778cd1e781f23e82394c83842a9f4655b59c9659035dc62ce3`: `strict_bytes` and `_program_view`, lines 28–73.
- `sep27-qft-trace/trace_bank/so_trace_certificates.py`, SHA-256 `e2f7f839a8b6826ee3edff7b06070dd91f3e90e7f29278d56e1682d608c6b18d`: `program_view`, lines 53–58; complete admission and immutable `_view_bytes`; `check`, lines 235–237.
- `sep27-qft-trace/policy_execution/so_trace_feedback.py`, SHA-256 `62121d7c1e1a7eafff452990b991ddfe027e65ada5e980881aa4d716de92bd20`: actual SO-bank type, identity and public-boundary checks.
- `sep27-qft-boundary/boundary_execution/boundary_uniform.py`, SHA-256 `875133020ba713af755d19b121f416938193835c3e2c9b7e6ab228c19b814c83`: synchronous outer-entry guard with nested Adaptive snapshot/ledger checks.

Let `S` denote the frozen `strict_bytes` JSON encoder and `J` its ordinary JSON decoder. The existing old helper returns

    raw = (full_dim, dim, codec_view, native_rows, P, C),
    P = S(program.phase_bindings), C = S(program.codec_binding).

It still checks the actual program/word/codec types and all phase keys, and visits every native row field: dimension, denominator, ordered word, complete stored forward/inverse columns, operation counts, column hashes and sparse native caches. No proposed fast path skips this helper or removes a field.

The current SO view is

    V(raw) = S({"native_fields": raw[:-2],
                "phase_bindings": J(P), "codec_binding": J(C)}).

Every full public-boundary check therefore serializes phase/codec metadata in `_program_view`, decodes those byte strings, then reserializes their contents inside the wrapper. The completed timing unit observed slower warm queries despite unchanged native counters. Redundant metadata processing is a plausible optimization target, not a proven causal allocation of those timings.

## 2. Safe implication and the domain of two-way equality

Define the ordered three-byte-string representation

    F(raw) = (S(raw[:-2]), P, C).

For all ordinary inputs on which the frozen functions are defined,

    F(raw_1) = F(raw_2)  implies  V(raw_1) = V(raw_2).        (1)

This follows componentwise. Native-field JSON text is identical; the same phase/codec bytes decode identically; fixed distinct wrapper keys then encode identically. The tuple stores three separately delimited byte strings, not an ambiguous concatenation and not only their hash.

On the admitted canonical metadata domain where `S(J(P))=P` and `S(J(C))=C`, the converse also holds. The wrapper has three distinct fixed fields, so equal wrapper JSON yields equal canonical component encodings. Generated ordinary metadata with recursively string-keyed objects lies in this domain. JSON arrays, booleans, integers, finite floats, strings and null retain the same encoder-level distinctions as before. This is equality of frozen JSON representations, not a new promise to distinguish Python tuples from lists or every Python subclass.

In particular, cached native column `0` versus `False`, or `1` versus `True`, remains distinguishable because `S(raw[:-2])` is bytes. Replacing it by raw Python tuple equality is invalid. Likewise integer `1` and float `1.0` remain distinct in the frozen JSON encoding. The proposal must not use `str`, lossy coercion, an unordered collection or host numerical equality in place of these bytes.

## 3. Why unconditional direct replacement is not fully equivalent

The legacy helper does not recursively require string keys in metadata. Consider these pure symbolic JSON examples:

    p = {2: 0, 10: 0}
    q = {"2": 0, "10": 0}.

Because `sort_keys=True` sorts original integer keys numerically, `S(p)` emits the key order `"2","10"`. `S(q)` sorts strings and emits `"10","2"`. Thus `S(p) != S(q)`, but `S(J(S(p))) = S(J(S(q)))`. The old whole-view function identifies these two encodings after decoding and sorting; direct comparison of raw metadata bytes does not.

For example, at a sufficiently large phase width, replacing all outer phase-binding keys by integers can change numeric versus lexical order while the old SO check normalizes them back to the same string keys. Initial bank construction still indexes string keys and would not admit that replacement as a new bank; the issue is a later in-process check against an already admitted bank. The native bank keys are independently strict integers and are not this metadata field.

Consequently a direct segmented replacement is never weaker by (1), but can be stricter on anomalous metadata. It is incorrect to claim a globally identical acceptance relation without either declaring a new stricter metadata schema or handling these cases. No executed counterexample is claimed here; this is a statement about the specified encoder/decoder semantics.

## 4. Recommended exact compatibility design

Retain the frozen exact-type `SOTraceBank` unchanged. Add a separately versioned boundary adapter with an immutable segmented admission token. Do not monkeypatch the bank, pretend to be a new bank type, or modify its scientific evidence.

At adapter construction:

1. Run the existing constructor/admission and actual `SOTraceBank.check(program)`; require the exact bank type and frozen source pins.
2. Decode the bank's immutable, already admitted `_view_bytes` **once**. Require its fixed three-key wrapper schema. Let its components be `native_fields`, `phase_bindings`, `codec_binding`.
3. Store the immutable tuple `E=(S(native_fields), S(phase_bindings), S(codec_binding))`, along with the exact bank identity/hash, view-profile name and pinned source hashes. It is derived from the admitted bank bytes, never from an unchecked current program. Private field access is a source-pinned adapter dependency and must be documented.

At each outer public entry, after the unchanged Adaptive snapshot and committed-ledger checks:

    require exact SOTraceBank type and original bank identity
    raw = frozen _program_view(program)
    candidate = (S(raw[:-2]), raw[-2], raw[-1])
    if candidate == E:
        accept this complete binding check
    else:
        frozen_bank.check(program)    # exact old compatibility slow path

Do **not** refresh `E` after a slow-path acceptance; otherwise a later view could be chained to an unproven baseline. The scientific records returned by `bank.get(m)` stay the original admitted records.

### Equivalence proof

If the fast branch accepts, (1) shows the current whole view equals the admitted whole view, so the frozen check would accept. If fast comparison does not accept, the exact original method decides. Conversely, whenever the original method accepts, either the fast branch accepts or the slow branch accepts. Thus the acceptance relation is precisely preserved, including metadata normalization exceptions. Invalid types/nonfinite values rejected while building the raw view or JSON components remain rejected; they are not converted to a passing default.

This proof uses the same synchronous trusted-object assumption as the current guard. No external program or bank mutation may occur between view construction and comparison within one outer call. Hostile method replacement, `object.__setattr__` attacks against a frozen bank, and concurrent mutation are outside both contracts. The proposed optimization does not broaden that trust boundary.

The slow path intentionally repeats work for changed or noncanonical metadata. Ordinary unchanged admitted metadata uses the fast path without phase/codec decoding and without the second serialization of those payloads. No performance improvement is proven merely by counting these avoided transformations.

## 5. Guard, provenance and restore invariants

The new adapter must preserve the exact eight covered public methods: `gamma`, `mass`, `probabilities`, `advance`, `prepare_next`, `cursor`, `evidence`, `report`. Reuse the frozen reentrancy/owner/finally semantics; retain inner Adaptive phase-snapshot and ledger checks. An ordinary invalid outer entry must not execute scientific arithmetic before rejection. Exception guard unwinding is not a new `KeyboardInterrupt` ledger-rollback guarantee.

Use a new policy/guard-view profile and cursor schema/source binding, for example a `SEGMENTED_STRICT_SO_VIEW_WITH_FROZEN_FALLBACK_V1` profile. Cross-version cursor bytes deliberately differ. Restore must deterministically reconstruct a fresh adapter/token from a trusted or freshly replayed actual SO bank, replay the committed prefix/pending decision, then compare the complete new strict cursor. An external segmented token or a claimed hash cannot authorize reuse without the original bank admission. Frozen SO bank serialized restoration remains unchanged, including duplicate-key rejection and paid fresh native replay.

Counters need explicit semantics: full logical binding checks, segmented fast accepts, frozen slow checks/accepts/rejects, and constructor admission checks. Do not label every fast comparison as an invocation of the old `SOTraceBank.check` function. Source/identity checks and all native word/column/codec fields remain covered even when no old method is invoked on a fast accept. Any metadata hashes in records are supplementary provenance, not replacements for bytewise comparison.

## 6. Minimal next verification plan

Before scientific execution, compile the independent adapter/checker and obtain source-specific review. Metadata-only tests can compare the two predicates on finite known objects without propagating amplitudes:

- Honest canonical metadata yields a fast accept and the same old verdict.
- Integer/Boolean and integer/float changes in a native column/count are rejected, including cases raw tuple equality would miss.
- Full ordered word, forward/inverse columns, sparse caches, phase metadata and codec changes give the same verdict as the frozen check. Actual object-type and phase-key gates remain strict.
- The numeric-key/string-key counterexample deliberately reaches the compatibility branch and matches the old verdict, instead of being silently called equivalent through a stricter rejection.
- Tuple/list representations that the frozen JSON encoder identifies remain identified; the design must not claim a stronger type schema than it implements.
- Wrong bank type/binding/source and a forged token are rejected; no caller-supplied token substitutes for admission.

For the smallest actual integration check, use the already declared N21 bases 2 and 4, `t=4`, epsilon `1/3`, positive `1000` prefixes. Compare old SO boundary versus new segmented boundary numeric plans/ledger, complete signed matrices, observer streams and native counts. Add new-version strict pending restore, wrong profile/source/token controls, and guard-depth/budget same-bit recovery. The unchanged public-entry wrapper need not gratuitously repeat an entire full-law experiment, but new binding paths must be exercised directly.

Only after correctness should a separately authorized matched experiment reuse the three-fixture/two-order design. Record cold token construction and resident token bytes separately; the tuple duplicates metadata already present in `_view_bytes`, so lower transient serialization may increase persistent storage. Count fast/slow checks, preserve actual full-column admission, and confirm warm factory **and inverse** caches. Wait for concurrent scientific runs and large serialization to finish before starting; if overlap nevertheless occurs, retain and disclose it rather than choosing a replacement run.

## 7. Cost and scientific limit

The normal path still traverses/serializes every complete native-field view, phase binding and codec binding once. Its cost is linear in the encoded metadata size, not constant in word length, dimension or certificate size. It avoids an additional decode and reencoding of the two metadata payloads plus the wrapper construction. The compatibility path can cost more than the old check. Memory, source hashing, object allocation and interpreter overhead must be measured rather than inferred from the algebraic proof.

No new approximation is introduced: accepted word bounds, actual residual coordinates, noncommuting order and Gram query requirements are unchanged. Even a successful host-cost improvement would be a certificate-binding optimization, not a reduction of the large-order correlation/support problem or a general polynomial Shor dequantization.
