# R4-EC35 — Reproduction and status

**Author-side exact positive-source BRC mathematics; no native X6/Heartbeat computation, live CLAIM, independent Driver review or formal acceptance.**

Research note: EC35_FINITE_HORIZON_OBSERVER_QUOTIENT.md.

Exact executed verifier: EC35_verify.py (local SHA256 91881f869617ebdfefab4ac4c1568da9debb45c469e210de149e8a7226b07c31).

Prerequisites are the unchanged pinned EC33 and EC34 Python scripts stored in the same directory:

- EC33_VERIFY_UPSTREAM_PINNED.py — SHA256 c2c5b183f88e7856c006f6b9ca954d603ac4e2cfd25d65a5558c67c91bc69856; source commit 0f84db42704c6e107adb9fd99d5e64cb77589e9d.
- EC34_GITHUB_VERIFY_PINNED.py — SHA256 6dda5679426771152f3f09fa1327bf7c69dff3c03a9c50214f635532a9bf2862; source commit d90b896f9bdcd61c93d09dd7add5cdbee174b7fa.

Run from this directory:

    python EC35_verify.py --max-H 16 --max-h 18 --max-words 8 --output EC35_REPORT.json

Only the Python standard library is used. Input carrier: positive ordered microscopic BRC branches with retained source alternatives R0/R1 and observed R/B class labels. Terminal observer is unit mass, future operation alphabet is one auxiliary step A with horizon h. All numerical comparisons are exact integer/rational calculations.

The attached local evidence bundle EM_R4_EC35_FINITE_HORIZON_20261026.zip contains the longer paper draft, exact scripts, full report and cold-start receipt; bundle SHA256 409626a74bdc42cb16069c26a4360af729981c3dd4cc717ade4a964a9476e249. The cold-start receipt covers those ZIP bytes and should not be mistaken for a GitHub-host execution log. The GitHub note is a separately edited complete proof, so paper/README archive hashes must not be used as GitHub-blob equality assertions.

The proven scope is the auxiliary EC33/EC34 positive-source model, not the P000-native physical system. All-future equivalence, stronger microscopic labels and compositional approximation remain separate obligations.
