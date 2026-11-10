# R44 exact executed evidence (2026-11-10)

Scientific pin: 43ec6098b1330ae86d0a7863be336c5d97f6ef34. Auxiliary labelled irrational-circle observer only. Predecessor R43: PR #1987 / 25876fa923a88c6d64e9be703b3d3bd42c204bf6.

Extended local command: python VERIFY_R44.py. Exact Python Fraction, arbitrary precision integers, integer isqrt; all 1,414 full source vectors compared with a separately constructed 40-decimal enclosing rational parameter using Euclidean Floor Sum rank/select. Cases with N<=160 are also checked by literal full-window enumeration. Actual extended program SHA256: 6f79075c82dfbbdf829e003dc2c73d02cd07756e9712d8895356517ca73870cc. Full JSON certificate SHA256: 77899d1eef2acd5e9b575192f953f7f3702c3311899db71b683ffb202b759206. Run log SHA256: fe2b89e0d6ef39a6badb97faa214071d5ffd2a74ad98cd4e7e956a2b24085503.

| Family | m | J | N | K shifts | Minimum initial dyadic bits | Final bits | Precision upgrades | One-label expiry repairs | Vectors |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| J100 | 16 | 100 | 120 | 512 | 14 | 19 | 5 | 0 | 513 |
| J1000 | 16 | 1000 | 500 | 512 | 22 | 22 | 0 | 0 | 513 |
| J1e6 | 16 | 1000000 | 10000 | 64 | 27 | 30 | 3 | 0 | 65 |
| J1e9 | 16 | 1000000000 | 100000000 | 32 | 36 | 41 | 5 | 0 | 33 |
| short_N5 | 16 | 100 | 5 | 160 | 13 | 17 | 4 | 155 | 161 |
| negative | 16 | -30 | 24 | 128 | 11 | 14 | 3 | 16 | 129 |

Totals: 1,414 vectors (22,624 historically labelled entries); 1,408 shifts; 5,632 sparse extinction-rank checks; 20 adaptive precision upgrades; 171 exact one-label repairs; 26 phase initializations or precision-reset products; 1,402 ordinary modular additions. The full program performs no full-window replay upon refinement. The program uses exact R42/R43 dependencies from the frozen R43 research bundle, not rewritten pseudocode.

Executed stdout:

PASS J100 initial 14 end 19 refine 5 repairs 0 vectors 513
PASS J1000 initial 22 end 22 refine 0 repairs 0 vectors 513
PASS J1e6 initial 27 end 30 refine 3 repairs 0 vectors 65
PASS J1e9 initial 36 end 41 refine 5 repairs 0 vectors 33
PASS short_N5 initial 13 end 17 refine 4 repairs 155 vectors 161
PASS negative initial 11 end 14 refine 3 repairs 16 vectors 129
PASS_R44_ADAPTIVE_NESTED_DYADIC_STREAM_AND_INDEPENDENT_ORACLE 1414

Standalone small smoke test (VERIFY_R44_COMPACT.py, in this GitHub directory): exact checks at (m,J,N,K) = (8,35,30,80), (8,200,60,80), (10,-25,20,80), all passed. Exact evidence and proof have not yet undergone independent mathematical review. The full million/trillion S23 risk compiler was not executed this round.
