# Exact executed evidence (gzip Git blobs)

All files in this directory are author research evidence, not native Enterprise Math Result/Review/Working Truth. Date: 2026-10-26.

Human-readable complete mathematical proof: PROOF.md.
Portable code to recompute the finite suffix classification: PORTABLE_VERIFY.py (saved, not claimed to have been executed remotely).
RESULT_SUMMARY.json is compact, with pinned input references.

The following four compressed binary files carry the **exact bytes actually executed or generated locally**. Decompress with Python gzip.open or `gzip -dk` before running. Their immutable Git blob IDs were computed independently on the local compressed bytes and matched GitHub create/read receipts.

| file | original filename | original SHA-256 | original size |
|---|---|---|---:|
| VERIFY.py.gz | VERIFY.py | 80a9524e83499f354b04d61ed03e2b45c9aba2a28290315f5eb911abcf76105c | 5311 |
| VERIFY_BRC.py.gz | VERIFY_BRC.py | 52352fd29b674cb199cd64e7c9971967247fe0af1525366b8f59c75d4f5b420e | 3445 |
| RESULT.json.gz | RESULT.json | a5ec75dca1be1c5f9cc2b15268e31b3ba28596f01d84f69501771c4c57b44037 | 65586 |
| BRC_RESULT.json.gz | BRC_RESULT.json | 061343eb92b6339a860b9b85c34890483b98db40c2b64f45c388dce927ad1574 | 597 |

Run VERIFY.py first, then VERIFY_BRC.py from the same directory using Python 3 standard library. The complete result JSON reconstructs all 34 monitor classes, 78 quotient transitions, 150 distinct-state suffix certificates and the count-aware per-fiber quotient. The BRC flow checker tests a distinct rational policy and all its indexed two-law terminal probabilities.

Local full collection includes the longer PROOF.md, NEXT_TASK.md, stdout, SHA256SUMS.txt, and the four files above. Local ZIP SHA-256: 0bca98ac203a80133fc9731674c35ddedc3bb7cdd7c761117afc6a014fafa8fd.

No GitHub remote execution is claimed. Mathematical acceptance pending independent Driver review, and P000 native-X6 bridge absent.
