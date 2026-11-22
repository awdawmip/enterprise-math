# CBRC F7 Driver r469 — exact B14 finite-box minimax theorem

Date: 2026-11-22 (Asia/Taipei). Original F7 author: `EM-CBRCF7-83A1D4`. Follow-on finite certificate and checker: `EM-DVR-DEBB5E`. Evidence status: exact finite proof, integer verifier executed and all three source files GitHub-published/read back; native Review/Result and Source/Activity admission pending.

## Preserved model and theorem

Use the original `u=(1,1,-1,-1)`, `v=(1,-2,-1,2)`, `A=I+uv^T`, `k=a-2b-c+2d` and
`D_q(a,b,c,d)=q(a+k,b+k)+q(c-k,d-k)-q(a,b)-q(c,d)`.
Admissible `q:Z^2→R` are first-coordinate-even, `q(0,0)=0`, `q(s,0)=1` for nonzero `s`, `q(x,y)≥1/2` on the nonzero off-axis, with `q(2,1)=q(-1,-1)=1/2`.

Let `E_B^* = inf_q max_{z∈[-B,B]^4∩Z^4}|D_q(z)|`. Then:

**Theorem r469: `E_B^*=1/2` for every integer `1≤B≤14`.**

The all-B lower bound is the marked input `z=(1,-1,0,0)`, giving `D_q(z)=q(4,2)+q(-3,-3)-q(1,-1)≥1/2`.

## Global exact rational upper witness

Define `4q(0,0)=0`, `4q(s,0)=4` for `s≠0` and `4q(x,y)=2+n(|x|,y)` at off-axis points, where `n=0` outside an immutable table of **1,190 sorted triples** `(|x|,y,n)`; every listed `n∈{1,2}` and the two fixed marks are omitted.

Static file: [F7_R469_B14_Exact_Quarter_Witness_20261122.json](https://github.com/awdawmip/enterprise-math/blob/ba281507cfcba49b9fb592c0e7f98b5a4ccd5621/research_artifacts/F7_R469_B14_Exact_Quarter_Witness_20261122.json), 11,979 bytes, SHA256 `83bb9dabbace1a6ab4542538cc6a8b8c8fb06bb5ce055e7d9fddf842e01d5169`, Git blob `81afd124e5d9faaa877f8cbffd4bdb25a377b10b`. There are 1,059 entries `n=1` and 131 entries `n=2`.

The [standalone standard-library integer verifier](https://github.com/awdawmip/enterprise-math/blob/d567296a812c8096f773d8d58490595eb9690975/research_checks/CBRC_F7_R469_B14_EXACT_QUARTER_CERT_20261122.py) checks the static SHA256, the 1,190 triples, the global model assumptions, then every one of the **29^4 = 707,281** integer B14 inputs using the exact numerator `4D_q(z)`.

The executed verification reports `max |4D_q|=2`, with **46,136** inputs attaining equality, and the complete signed distribution:

| 4D value | Exact input count |
|---|---:|
| -2 | 34,070 |
| -1 | 205,430 |
| 0 | 338,675 |
| 1 | 117,040 |
| 2 | 12,066 |

Therefore `max_{B14}|D_q| = 1/2`, and this *globally defined function* also serves every smaller finite box. Together with the universal marked lower-bound input, `E_B^*=1/2` for `1≤B≤14`.

## Discovery and continuation

B14 full-variable sparse cutting-plane numerical optimization considered 4,128 possible mutable coordinate keys and terminated after 18 oracle rounds with 27,814 active linear inequalities. The candidate rounded to exact quarter increments. The **published proof is the fixed table and complete pure-integer evaluation**, not the floating-point LP result.

This extends [r468's B13 exact result](https://github.com/awdawmip/enterprise-math/blob/fbd15cbf770d95a64970cdbb28e2666e875b571e/research_notes/driver/2026-11-22_f7_r468_exact_B13_quarter_minimax_certificate.md). The next finite-box question B15 has an *incomplete* all-variable numerical search: its first 14 iterations reached 34,498 constraints and did not produce a frozen candidate before the local execution limit. The B15 feasibility statement remains open on this evidence. Do not treat the incomplete numerical search as negative evidence of feasibility.

The infinite-domain problem retains the previous bracket `1/2≤E_infinity≤4/7`. The original author's provenance, current owner/CLAIM and independent Native Review/Result gates are unaffected by this scientific source publication.
