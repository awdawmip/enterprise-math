# CBRC F7 r489 — B29 default-extension failure and 42 disjoint old-coordinate repair obstructions

Date: 2026-11-22 (Asia/Taipei). Contributor: the existing RESEARCH_DRIVER logical lane EM-DVR-DEBB5E, original SID MCP-9b4714dc46b948afa4875a86c89c713c. Original F7 researcher EM-CBRCF7-83A1D4 and its frozen Result RR-AA38973D56330E59D315 retain their authorship and separate review state.

## Statement and unchanged F7 model

Let (q:\mathbb{Z}^2\to\mathbb{R}) obey the original F7 requirements: (q(-x,y)=q(x,y)), (q(0,0)=0), (q(x,0)=1) for (x\ne0), (q(x,y)\ge1/2) for (y\ne0), and (q(2,1)=q(-1,-1)=1/2). Set (k=a-2b-c+2d) and (D_q=q(a+k,b+k)+q(c-k,d-k)-q(a,b)-q(c,d)).

Let (q_{28}) be **the exact globally defined witness** from r488: (Q_{28}=4q_{28}) is specified by the static 16,294-key B28 array, with (Q_{28}=2) on every unindexed nonaxis/nonmarked coordinate. Original immutable reference:

- [r488 theorem](https://github.com/awdawmip/enterprise-math/blob/2ad4b8fc7f1cf48496d1fbc914163060fc3e2044/research_notes/driver/2026-11-22_f7_r488_B28_exact_quarter_minimax.md)
- [actual fixed encoded byte array](https://github.com/awdawmip/enterprise-math/blob/a8250b8b3155e0dac034e168517f298037fde266/research_artifacts/F7_R488_B28_Exact_Quarter_Witness_20261122.b85), decompressed SHA256 `fa01c131e431a7ff708dbffc9974c44dcb8e2f126349bcbe8ba6ee5bc7a1fd6d`
- [original independent B28 integer checker](https://github.com/awdawmip/enterprise-math/blob/7cafd74d5a6eb7ff8040900d23ec7ca0e48bfe7e/research_checks/CBRC_F7_R488_B28_EXACT_QUARTER_CERT_20261122.py).

**Theorem r489.** The unchanged global r488 witness has (\max_{[-29,29]^4}|4D_{q_{28}}|=4), violating the B29 half-error bound on **18,752** of the (59^4=12,117,361) original integer quadruples. Of these, **18,304** are supported exclusively on preexisting B28 indexed (evenness-reduced) function coordinates. More strongly, every admissible real-valued (\widetilde q) with (\max_{[-29,29]^4}|D_{\widetilde q}|\le1/2) must differ from (q_{28}) at **at least 42 distinct old B28 indexed keys**, and its old-coordinate total change satisfies
\[
\sum_{K\in I_{28}}|\widetilde q(K)-q_{28}(K)|\ge\frac{42}{4}=\frac{21}{2}.
\]
Here (I_{28}) denotes the 16,294 B28 free keys (K=(|x|,y)) with (y\ne0), excluding the original fixed marks. The bound assumes *no* quarter-grid restriction on (\widetilde q), and makes no minimal-repair claim.

## Complete finite-check method and histogram

Use the exact r471 change of variables (r=a-b,t=a-2b,u=c-d,s=c-2d); then (D_q=[h_r(s)-h_u(s)]-[h_r(t)-h_u(t)]), (h_r(v)=q(2r-v,r-v)). For each (r\in[-58,58]), (T_r=[2r-\min(29,r+29),,2r-\max(-29,r-29)]\cap\mathbb Z). Enumerate all (r<u), (t\in T_r), (s\in T_u), and accumulate the exact integer (4D_{q_{28}}=Q(2r-s,r-s)-Q(2u-s,u-s)-Q(2r-t,r-t)+Q(2u-t,u-t)). Restore (r>u) by sign reversal and (r=u) by zero. This enumerates the original full input box bijectively, with no rounding.

| Exact (4D_{q_{28}}) | Original-input count |
|---:|---:|
| -4 | 88 |
| -3 | 9,288 |
| -2 | 379,057 |
| -1 | 2,798,567 |
| 0 | 5,743,361 |
| +1 | 2,798,567 |
| +2 | 379,057 |
| +3 | 9,288 |
| +4 | 88 |

The (r<u) half has 9,376 violating rows, of which 9,152 have all four *editable* evenness-reduced support keys inside (I_{28}). The opposite orientation doubles these figures. The original (r=u) cases total 136,939 and have zero error.

## Independent-support certificate for old-coordinate repair

The following 42 rows are exact ((r,u,t,s,4D_{q_{28}})) witnesses. For each, original input ((a,b,c,d)=(2r-t,r-t,2u-s,u-s)) lies in ([-29,29]^4). Its four support keys
[
(|2r-t|,r-t),quad (|2u-s|,u-s),quad (|2r-s|,r-s),quad (|2u-t|,u-t)
]
are all freely editable, belong to the original (I_{28}), are distinct *within* the row and disjoint across the 42 rows (168 distinct keys total). Values (pm3) below are in units of (Q=4q).

| # | r | u | t | s | 4D |
|---:|---:|---:|---:|---:|---:|
| 1 | -57 | -53 | -86 | -78 | 3 |
| 2 | -12 | 24 | -16 | 53 | 3 |
| 3 | -36 | 9 | -65 | 12 | 3 |
| 4 | -24 | 18 | -53 | 27 | 3 |
| 5 | -11 | 20 | -22 | 49 | 3 |
| 6 | -20 | 17 | -49 | 29 | 3 |
| 7 | -36 | 45 | -46 | 61 | -3 |
| 8 | -13 | 35 | -15 | 41 | -3 |
| 9 | -36 | 41 | -43 | 53 | -3 |
| 10 | -47 | 39 | -66 | 49 | -3 |
| 11 | -44 | 42 | -60 | 55 | -3 |
| 12 | -42 | 45 | -55 | 62 | -3 |
| 13 | -46 | 40 | -64 | 51 | -3 |
| 14 | -38 | 41 | -47 | 56 | -3 |
| 15 | -42 | 48 | -57 | 67 | -3 |
| 16 | -49 | 40 | -69 | 54 | -3 |
| 17 | -48 | 42 | -67 | 57 | -3 |
| 18 | -52 | -38 | -75 | -49 | -3 |
| 19 | -50 | 26 | -71 | 27 | -3 |
| 20 | -9 | 43 | -20 | 57 | -3 |
| 21 | -26 | 49 | -27 | 69 | -3 |
| 22 | -22 | 52 | -27 | 75 | -3 |
| 23 | -55 | 36 | -81 | 46 | -3 |
| 24 | -54 | 38 | -79 | 49 | -3 |
| 25 | -34 | 50 | -45 | 71 | -3 |
| 26 | -22 | 51 | -21 | 73 | -3 |
| 27 | -56 | 22 | -83 | 27 | -3 |
| 28 | -43 | 38 | -60 | 47 | -3 |
| 29 | -32 | 54 | -40 | 79 | -3 |
| 30 | -32 | 55 | -38 | 81 | -3 |
| 31 | 10 | 56 | 11 | 83 | -3 |
| 32 | 34 | 54 | 43 | 83 | -3 |
| 33 | -43 | 8 | -57 | 22 | -3 |
| 34 | -57 | -46 | -85 | -63 | -3 |
| 35 | -41 | 11 | -53 | 16 | -3 |
| 36 | -40 | 10 | -51 | 28 | -3 |
| 37 | -44 | 46 | -59 | 64 | -3 |
| 38 | -44 | 44 | -62 | 59 | -3 |
| 39 | -45 | 46 | -62 | 63 | -3 |
| 40 | -47 | 41 | -65 | 54 | -3 |
| 41 | -46 | 47 | -65 | 65 | -3 |
| 42 | -45 | 39 | -61 | 54 | -3 |

For each witness, passing from (|4D_{q_{28}}|=3) to (|4D_{\widetilde q}|\le2) requires a change of magnitude at least one in its four-term integer-scaled expression. By the triangle inequality, the sum of absolute changes of (q) over those four distinct old keys is at least (1/4). Pairwise disjointness gives both the **42-key** and **21/2 total-variation** lower bounds. These are exact mathematical obstructions to retaining the B28 witness; they do not decide the unrestricted B29 minimax value.

## Reproducibility and remaining scope

The construction consumes the original r488 static SHA256-pinned bytes, applies the published r488 deterministic key-index order, and uses only integer additions/lookup/Counter arithmetic. The new certificate rows were independently checked against the *original* four-input expression, not just the fiber formula; every listed discrepancy equals its signed table value. The 42 witnesses were selected greedily from 7,355 eligible all-old four-distinct support rows; no maximum matching claim is made.

**Proved**: (e_B=1/2) through (B=28) by r488; the specific default B29 extension fails, and any B29 half-error repair must alter at least 42 old keys with aggregate (L_1\ge21/2). **Open**: existence of any B29 (1/2)-error witness; exact (e_{29}); global (e_\infty\in[1/2,4/7]).

Scientific note only; neither Native Review, frozen Result repair, formal Task completion nor Parent Objective closure is claimed. The native integrity/review issue remains [#2874](https://github.com/awdawmip/enterprise-math/issues/2874).
