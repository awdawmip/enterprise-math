# Complete exclusion of cost9865

All190 exact cost profiles with0,1,2 cores have completed zero-solution receipts.
The complete cost spectrum is regenerated from the unchanged native census.
Together with the preceding complete exclusion through9864 and the existing
three-or-more-core bounds, this proves9866 <= R12 <=9996.

## Counts and scope

- Profiles:190/190; profile SHA256:93e21ef7cd5fb0dcee631c48407e6f336ba3329c441f8be39c14a32282340ca2.
- Cover nodes:1,473,371,875; geometric nodes:20,787,134.
- Exactly189 selected receipts use the unchanged original native source.
- One receipt is the complete173-batch union of5528 outer prefixes, contributing
  60,478,750 cover nodes. Every interval and source transformation is included
  in sharded/. Splitting changes only outer dispatch; no pruning predicate,
  recursion, candidate order, or same-type convention changes.
- Duplicate terminal receipts discarded:20. No interrupted or
  currently running profile contributes to these totals.

A core means a complete13-point class or its center-deleted12-point class;
outer-deleted12-point classes are not cores. The unchanged predecessor bounds
exclude cost9865 with exactly3 cores (bound9881), exactly4 cores (bound9871),
or at least5 cores (bound9996). The prior geometric bound excludes the omitted
profiles having at least7 selected12/13 classes. These reductions are the same
ones used by the already frozen lower/ and lower_9862..lower_9864 packages.

## Portable verification

Place this directory beside the unchanged lower/, lower_9862/, lower_9863/ and
lower_9864/ packages. Supply the complete original predecessor as --previous.

    python replay.py --previous /path/to/predecessor --mode audit --output /tmp/audit9865

The audit verifies the source, headers, native input digests, prior complete
layers, all190 selected receipts, and the173-batch certificate. It independently
regenerates the exact cost profile list. An audit does not rerun native searches.

    python replay.py --previous /path/to/predecessor --mode full --jobs 2 --output /tmp/full9865

Full mode reconstructs the
complete bank and anchors from the original observations, compiles the bound
original native source and headers, records the actual executed binary hash and
compiler command, and runs all190 profiles. In full mode even the formerly split
profile uses the original unsplit native engine; the aggregate node totals must
agree exactly. No prebuilt executable is trusted as a substitute for compilation.

The retained execution binary used by the original native workers was also
recompiled and compared byte for byte; see native_binary_binding.json.
The independent within-team source cross-check is not a formal Review.
Review status remains NOT_REVIEWED.
