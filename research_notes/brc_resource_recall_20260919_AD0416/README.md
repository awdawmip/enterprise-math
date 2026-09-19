# BRC resource-conditioned recall — reproducible research snapshot

In the standalone bundle, run `python verify_resource_recall.py` with Python 3.11+ from this directory. In the GitHub research directory, supply the two source-checkout options shown below; vendored dependency files are packaged in the standalone bundle rather than duplicated in the project. No network or third-party Python package is required. The fixture executes pinned Nollm source functions, not a reimplementation of its recall merge rule. It uses a sparse module namespace to avoid importing unrelated package startup code.

The source run reads only synthetic state. Nothing installs, replaces, clears or writes an actual Nollm memory store. The default-profile lateral template data are instantiated from the checked canonical compiler law; the complete compiled artifact and inter-layer dynamic coverage are not used. Source slices are marked in their headers. `vendor/NOLLM_LICENSE` preserves upstream MIT attribution.

The adapter is a research candidate. It preserves bounded no-beam maximum-score observations; `mode='paths'` additionally preserves tie-selected kernel words under its declared resource guard. A missing score and a reached score zero differ. Finite beam and changing runtime state are not certified.

For already available project checkouts:

```text
python verify_resource_recall.py --nollm-src /path/to/Nollm/packages/nollm-core/src --em-src /path/to/enterprise-math/src
```

Pinned full-file hashes must match. A newer source revision requires a deliberate rebase, not disabling the identity assertions.

`RESEARCH_NOTE.md` contains the proof, witness, evidence boundary and next frontier. `verification_results.json` records the executed 10 check groups. This standalone bundle is a small research snapshot, not a full clone of either project.
