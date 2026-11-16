# R469 portable research evidence

The frozen scientific formula source is R462 commit 18783e01e3646c72b7aab3b16d3f565e83e6446f; this continuation follows exact author-side R468 commit 1eb6cd74a9337c01464acc0177153c94355bf32e. The current policy snapshot does not modify scientific pins.

Reproduce from the Enterprise Math repository checkout with R468 sibling research directory intact:
```sh
cd research_notes/r469_signed_brc_right_edge_217_224_20261102_emr3/
python R469_REPRODUCE.py 217 224
python R469_ROW_VERIFY.py
```
`R469_REPRODUCE.py` imports R468_EXACT_KERNEL.py and its R462_VERIFY_FROZEN_KERNEL.py (same prior folder); no copied kernel bytes or mathematical substitutions. A separate independent integer row implementation was actually executed and yielded the same coefficient/minor stream hashes, recorded in R469_EVIDENCE_ALL.json and the local downloadable research archive. Optional GMP acceleration is not a proof premise.

Each fixed s=217..224 has full Z[u] positive coefficient proof for all k>=floor((s+2)/2), with 8 separate s records; r=241,243,245,247 each has full finite-row exact Catalan positive-minor check. PF3 interval is conditional on R447/R450. This is author-side only; canonical CLAIM/Result/independent review not obtained.
