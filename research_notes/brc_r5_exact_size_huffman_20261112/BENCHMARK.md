# R5 exact-size Huffman: first whole-query time/space experiment

2026-11-12. Same **frozen** R5 corpus of 1,065 words, 2,880 trie nodes and 20 exact rational parameters; each benchmark computes 57,600 prefix-count queries, with identical aggregate checksum 62,728. Local independent Python 3.13.5 on Linux x86_64; each row is a single in-process observation, not a statistical timing distribution. The original four-class and new 78-symbol exact-size decoders each access their own packed index and decode actual subtree sizes at query time (not pre-expanded arrays). Wavelet-rank queries are shared.

## Direct bit-at-a-time decoding

| Stride B | Four-class packed bytes | Four-class query wall s | Exact-size packed bytes | Exact-size query wall s | Saved packed bytes |
|---:|---:|---:|---:|---:|---:|
| 16 | 5,406 | 1.0140 | 5,209 | 1.3226 | 197 |
| 32 | 5,226 | 1.1892 | 5,029 | 2.0101 | 197 |
| 64 | 5,136 | 1.4331 | 4,939 | 2.8815 | 197 |

Full-query timings include repeated nearest-offset size decoding, terminal rank and wavelet-range count; they exclude encoder construction and one-off experimental setup. Both decoders recovered the exact size at every one of 2,880 nodes before timing. Timing order was four-class then exact-size at each stride, so measurement noise and warmup should not be ignored.

## Exact-size canonical Huffman with table-aided prefix decoding

The exact-size code has maximum length 12. Construct an in-memory table indexed by the next 8 or 12 bits. Table entries pack decoded exact subtree size and codeword length into a 16-bit unsigned integer. With 8-bit lookup, short codes decode in one table access, and long codes use the ordinary exact prefix fallback. With 12-bit lookup, all existing codewords decode by table. The exact B-bit decoding rule remains the same, and each query advances by the decoded codeword length, so the original 39,512-bit B=64 serialized index is unchanged.

**Lookup table value-array payload only:** 2^8 * 2 = 512 bytes or 2^12 * 2 = 8,192 bytes. These are *additional runtime* bytes beyond the packed index, excluding dictionary/inverse maps, Python object overhead, intermediate arrays and process memory. The table is constructed from the verified canonical codebook and is not a separate persisted byte stream.

| B | 8-bit LUT table | 8-bit LUT wall s | 12-bit LUT table | 12-bit LUT wall s |
|---:|---:|---:|---:|---:|
| 16 | 512 bytes | 1.0669 | 8,192 bytes | 1.0449 |
| 32 | 512 bytes | 1.4445 | 8,192 bytes | 1.1063 |
| 64 | 512 bytes | 1.6300 | 8,192 bytes | 1.3877 |

Each row passed the **same 57,600 exact prefix queries** and checksum 62,728. A 12-bit runtime lookup restores approximate parity at B=64 with four-class direct decoding in these one-run observations (1.3877s vs 1.4331s), with 8 KiB auxiliary table overhead. A much smaller 512-byte table reduces the B=64 first-run time to 1.6300s vs 2.8815s bit-by-bit.

Measured process maximum resident memory was 155,532 KiB for the direct-codec process and 154,120 KiB for the LUT process; these numbers include the entire Python interpreter, fraction-based corpus construction, masks and wavelet model, and are not isolated decoder peak allocations.

## Verification, exact scope and next work

The local scripts executed successfully with `PASS_R5_HUFFMAN_CODECS_IDENTICAL_FULL_QUERY_WORKLOAD` and `PASS_R5_EXACT_SIZE_HUFFMAN_LUT_QUERY`. Their original stdout is preserved in `LOCAL_QUERY_BENCHMARK_OUTPUT.txt` and `LOCAL_LUT_BENCHMARK_OUTPUT.txt`. Independent corpus/source verification and proof are described in `RESEARCH.md` and `VERIFY_EXACT_SIZE_HUFFMAN.py`. This is a repeatable workload definition and actual local observation, with follow-up work to publish a clean repository-only benchmark harness, rerun across fresh isolated processes with randomized order, include encode/init and allocation costs, and test additional exact-size codebooks.
