# EC49FZP — Maximal unsaturated fiber envelope and close-budget pruning

Date 2026-11-25. Portable continuation of EC49FZO, frozen BRC16943, h=14, m=25, 50 support masks and 2393 fourth-level roots. Parent scientific files c5ddb01cfc3637ccac13bafb07f9ad6198e59157:research_notes/portable_direct/EC49FZO_CERTIFICATE_COVERAGE_QUOTIENT_DP.md and 6f7e55ae25f789482e79abaa876bc1788c3252f4:research_artifacts/portable_direct/EC49FZO/fourth_tail_and_costs.json. Historical researcher provenance EM-DIRECT-23537B, current private session/writer binding unconfirmed. Topic read r4-20261125-1230-ec49as-read-v1 SUCCEEDED at Source dbf965b90533581517010bd74ea52281e248f5b3: NO_CANONICAL_PUBLICATION_DIRECTORY (not a native owner projection). Independent unshared research, no CLAIM, no formal Result or review. P000 unchanged.

## Theorem: exact maximum certificate on the maximal unsaturated layer

Consider a genuine binary observation history of W(r,j)=1[r in U]1[j not in H], with at least one positive common anchor. The possible holes outside the globally positive columns form the common universe C. For each active support U the fiber is {H:B_U subset H subset C, |H|<=h}; saturated fibers can equivalently be normalized to their single B_U. Let F_U=C minus B_U, p=|F_U|. Restrict to |B_U|<h. Write H=B_U union Z with Z subset F_U and b=|Z|<=h-1-|B_U|. For every competing V let R_V=U xor V and D_V=B_V minus B_U.

The exact minimum target-specific path certificate is

    c_U(Z)=min_{T: T intersects R_V for all V!=U with D_V subset Z}
                [max(p,b+|T intersect U|)+|T minus U|].

Proof. Each free column is compulsory for this unsaturated target: flipping it gives a compatible state of U (adding one hole stays within h). A live free column must be queried positively and a hole free column must be queried in a row of U, yielding zero; there are p-b and b respectively. The same-hole competitors are exactly those V with B_V subset H, equivalently D_V subset Z, because H is within the common universe C and has legal size. Distinguishing them requires a row difference. On H, a row-difference query must use a live column: positive row features can share the p-b compulsory positive column queries; negative row features require separate queries. Thus the lower bound is b+max(p-b,|T intersect U|)+|T minus U|. Conversely pair selected positive rows and live free columns, using the common positive anchor's row/column for unmatched features, use the anchor row for free holes and its known-live column for negative rows. This achieves that cost. Every competitor with B_V not subset H has a compulsory live free column of U in B_V minus H (B_V subset C), so is eliminated by its positive observation. Every other support is eliminated by a selected differing row feature, and the free-column features uniquely identify H within U. This proves equality. Saturated targets are not included here.

If Z subset Z', both the active constraint family and b are nondecreasing, so c_U(Z)<=c_U(Z'). Every unsaturated Z can be extended to cardinality b*=min(p,h-1-|B_U|), without becoming saturated. Hence

    max_{H in fiber, |H|<h} C_full(U,H)
       = max_{Z subset F_U, |Z|=b*} c_U(Z).

The maximal layer is exact for the worst unsaturated path certificate. In particular, for budget k, let A_k={T:max(p,b*+|T intersect U|)+|T minus U|<=k}. An unsaturated obstruction exists iff some Z of size b* satisfies:
    for every T in A_k, there is V!=U with D_V subset Z and T intersect R_V empty.
Equivalently no eligible row set hits all rivals enabled by Z. For evaluating these predicates it is enough to enumerate T in the union of relevant R_V: other rows can be removed without increasing cost or losing coverage. Rivals with D_V outside F_U or |D_V|>b* cannot participate. This is a direct residual-envelope test, not a sufficient condition for existence of an adaptive strategy. In a general arbitrary union of fibers with distinct potential-hole universes the proof does not apply.

Relation to previous tools: reuse the FZI anchored positive pairing cost, FZJ support fibers and FZL minimal-fiber all-row lower bound. The new monotonic maximum principle permits exact worst-unsaturated testing only on the maximal layer, including competitors not present at the minimal fiber. Saturated states still need FZO. The solver implements the envelope test at k<=8, k-p<=2, b*>0; all other nodes retain the parent's solver. This is an exact necessary condition where called, not an exhaustive all-node certificate scan.

## Executed experiment

Input archive EC49FZO_reproduction.zip (conversation artifact), all 28 listed constituent SHA256 checks passed. fourth.json SHA256 228f907796e82fe17b7984123d636a81d6d6a1bc94e357629a6a98071b390923; fullrow.cpp 3d1ae2d75991d5b6cd9a131f38068f27d04a1e2fc2abccf6e6673893e00f9d0b. Parent fullrow.cpp also at 0b8230271b3c981112b138728d8623e4e259d3ad:research_artifacts/portable_direct/EC49FZL/fullrow.cpp (Git blob b14377bbc9b3797a651d6857b7474d33b9c5295d). Keep frozen input and completed results; select only the 783 capped IDs, sorted numerically, no completed root rerun except the explicit controlled comparison within this round.

g++ -O3 -std=c++17 fullrow.cpp -o solver
python build_envelope.py
g++ -O3 -std=c++17 envelope.cpp -o envelope
python retry.py 0 20 50000 | ./solver > retry.csv
python retry.py 20 55 50000 > next.in
./envelope < next.in > next.csv
./solver < next.in > baseline_next.csv
python retry.py 55 105 50000 | ./envelope > next2.csv

Results (status 1 exact feasible with labeled replay, -1 exact impossible, 0 node-cap unknown; final extra column is envelope prune count):
- first 20: 17 feasible, 3 unknown, 659698 nodes, 17462 replayed labeled states.
- next 35 envelope: 31 feasible, 4 unknown, 1162429 nodes, 37177 replayed states, 23529 envelope prunes; measured 13.23 s.
- same 35 baseline: 30 feasible, 5 unknown, 1177804 nodes, 35950 replayed states, 13.57 s. Node count decreased on 28 roots, unchanged on 7, increased on none. Root 1516 (1227 states) baseline reached cap 50001, envelope produced feasible result with 49164 nodes and 1379 extra prunes. Single timing measurement, no general speed claim.
- next 50 envelope: 45 feasible, 5 unknown, 1162418 nodes, 57717 replayed states, 28268 prunes; 12.89 s.

Across 105 distinct previously unresolved roots: 93 new feasible, 12 remain unknown, 0 new impossible; 2,984,545 calls excluding baseline control, 112,356 labeled state replays, 51,797 new-prune calls (not necessarily unique semantic states across roots), 193 additional ordered histories. All successful runs completed actual labeled replay in parent's C++ code. Cumulative 1693 feasible, 10 impossible, 690 unknown among 2393. Ordered histories: 3421 feasible, 18 impossible, 1256 unknown among 4695. M14 still 25..27. The 35-root control adds 1,177,804 calls but no additional independent roots. No all-state saturated optimizer integration this round. Envelope algorithm's correctness follows the theorem, no independent review. Next: resume remaining 690 only, including 12 capped here, integrate FZO saturated certificates at tight nodes; consider union-of-required-hole sets for an obstruction rather than enumerate all maximal sets. Do not treat node cap as impossibility.

## Exact delta files

Each line below is filename, SHA256, gzip+base64 of the actual local bytes (decode with Python gzip.decompress(base64.b64decode(payload)), check digest). Parent inputs remain the immutable FZO reproduction archive; generated envelope.cpp SHA256 b1047b0df52701a4fd0edcf7d7ba43bfb856a45f20ed6efa05585b458894792a. Raw CSV contains each evaluated ID; comparison rows are separately identified. Full local archive contains frozen inputs plus generated source, not binaries.

```text
retry.py 120ceb54784c85a89090a76484967c76fff3de8208df9fd9e86230d91f31a1f9 H4sIAAAAAAAC/2VRXUvEMBB8z6/I2yWylPvwUK/kl5Qi4ZLa1TYp2Zwi4n930/ZEuYcQMjvZmZ3FcYopyzO9wyvFAPRJoktxlC8+SFyKU/9JeLaD6HDwZJpNFy8p98+TTRntUPHnDVzB4D/+A9nicIvsb6HDDLXCma9v0cUki5zEMN90ErJgCOwRzgVmdpW8dT6pOPmgCk1r5l1JZrSTwpBBrYDWtSXyPBLKEHNp4mrXYGvUUhdreeB2ThuzPzwdRIoxkynpVEO0bhFbjVcF3mgt0HEwuFpcu5X+xAF6p1yF2Y+kNIOdJGO2bf1Hi3+z2sPjQQwReoSznX7N80Yqm17em92p1XXR4dMM8dRjW0+JKeraQs+xYdHlJycRQCUYLb1BzL1PGiabewLKNl/IzIPx9DVlc92xamb63cxvYXcPCbb6r1fKbDUIuUiXZPdH2B2LZ73s6AL9PHo+LRx+a/EDE3JcyWkCAAA=
build_envelope.py 28f1bf5df827b40f5b5a10f614850755487967392b9c41912927136296fbe5ab H4sIAAAAAAAC/21US2/bMAy+51eoHRBbiJO2Ow2zFWA7DNuhWIEdi3SQbbpRbEuuHn3k0d8+yrLTZtvBD4nkx48fQVZataTjdt2InIi2U9qSGzxODPOfOKpc02j1tCi6LqILDbz8beHZxnTygfyQBtCfVxY0aYUULW9IJXI85crJknB8cqiUBvLgQL8QkK4Fza1QcjHhslgrzSJirHaFJT93jZL3pH+ZAoOSnDepkJY8pL8IT/L0kEYTbvqkZlFgChsHEMrY1aRQJbAoisjFBbnmzz0bJw23DjNCOTAD+QiN6iAh8Mwxq4QCjOFIrlCyFIGah/jSdc0LURJfVpGiUQbmuSvvAZMjdEMk5jMpMbXoiLJrxO5vyJOwa+Us4heNMwEPNYh9JYJdpiLzv1SUZmHEFmKaitmM7iaEEO/SsUoD3IpV4ti3W/TC31XywOp5l3jLNTc1+4KXd1/xlY5hOcMOxF3yfX4174rY2ygN1iqul5/2+4flx/0+z9glxUqtkA568yMUVums40JnCJTgs1wSLR55Y3r1sf0GaXvfsYwNnjf/lLHBMjCZOGObUE5gJgFK9vV2s5q+Hhn3rGJvmb6ORdH9Hon7O7rMTzkGoFJU1SDJZrW6c2kgueicWf/OeVHHOx+deL8DTT3vPfOHHuMwaDEEQdvZl5j+VwsvAcEWqycoT+q2zIOmqWWxnV/RqT8dS63ilj9jB/IZlmGnjtLw8+poxmo64L1ja+mbFmeW5jhd9RvVMeeWjQKl6ZbFW5/3KNlbbky1xTHIxyuCM6hwHIEbkTfAKix6FPNdQZ8HWnTXu6ua4TBC6u3cWXV7FHT1OQhHR4hAe+jhlk6nZ7H3m1pKdwgT8oWaDicxCmkfafXZBq+jmwcePehuNhtn9kY7iSOnAUdakhZa38WGFxDX8JKgMItKaGPnSwN+mMe8hzeVt6cqHya4L3DXGdxsASjsk8TvktmwW462yCtW8C4pUDQ/ElHy91VyStX7vIvPssdF75hlIMvGx7+7Ok/O/ekUYfSkk7CPR+uwkJ+0sBA2MnbmD4jUjOvOBQAA
retry.csv f892f87a1fa6ae5d9be8d6c556b15359ae90876d08ae1c002847c8fc147c9c58 H4sIAAAAAAAC/02QOxIDMQxC+5xFhf6y7n+xgHdnktLPgDE7LeeYmHhW5sesSraDwGaboF+QawHgCrB5FR5OcF4QU64AUWKqRYnuLEgqyVyTZoA0NX41VTYgB9dKoYROIiesQWr5dkRCE86c1sdVh8RJTFRKVY2EyX376PIL4f2QPw3fYgVJ12ROwKDDJSLM0DmSrrlTFGYAqUtu5zzDnIMDKv6SE2MYFmCOI+PzBRQH7kZiAQAA
next.csv 4653d0bfa95439c1f042e37062181ea7ed5688c42166096924fc93af2fa79b1f H4sIAAAAAAAC/02SN4LDQAwDe7+FBXP4/8eOoByukjWCAZC74jwkok5CbqxNUjEvcVHgfSWVziQ1Aa2lzsQUzCxkzKCwcIGWy5a6LrVcGgVqkUpQeizb38vKTCkSriGg+4lMWpx8ailkUtAaWzJ1+NJi0Lxe7ENTyIJM+rTqE2gHirS+0XL2OQ0tgAyoZuwMWQGKtoMOzsWQFKp1ffBW682+woO4uRLptsZwwLsyA0Z537xTPwabuAYzoLev5hzKWBqQKV9Ute7XTNAFKqcd3ep6WgBVuwIVW2AMVEFvstZIajlqoHEOMrancRS+Wk9arl0J4iQ/2Edyraz2NoReXn/PXXUY+KznDn72uQAU1vbezoq9j2Joq6/Fk2f80FVJx20AVL50N8LrEKBIs74j6u1vvhcicKX0uXx7Qrf2CCzC492gyKNA8X/Pf0NovP4AGBGyLgEDAAA=
next2.csv 103c4297d4ff7d6eff66d46525d13bdc85a431d1b5fc93e2329e9e52035fa4a2 H4sIAAAAAAAC/22TObLjMAwFc5+FAfbl/hcbPKjEP4ESudyCwX4gzO52WJwOHSciPlXyY3d/KB8uYjutBVqgDKqeejwatC/1Jjs0LAhMhgmRzBsStA0B9m0gNp+EtqEvFS3Ro5agKxagRq2ncFasVwFGsZ6oLZ0qibU1VzmxZ+ULRZkTCluLDPHY+hzG5EMTvvA4Jt2JdwwMM3Q/SmaIoaCQiP4bWSNyQgKPwylCRxnCmZ8UEng1fZtphg7YL2TbGxlW9MEYrME6ZqJQKrksA6KwL3jWjqWLZyw714Ln1L/2qjAqeJad7V3TyJbCsza/4Nz07QDR+cHN7/bD1Q/tnXdpz8rsrBoNW9aBph0C4OvD5qm4763ErPGYCJRYOVxM26XWs4geSNb+SfNSp7k1k/WqT4oMbc/A5i6ZLH4ctLp1o0UQ6LjOAqA4ECKaQfVSz1mw8Aa1S9MxUEoH9s/i+KT5UulZGnivRX8Vz/Z8Uf7POOVYoQPfHJo0214MNd4c+6fMljHiLGD7xv5i3dmq6u8fNGfsPUYEAAA=
baseline_next.csv f133d07b071742b21973375743f3d4d732f5be6af758950560ab72ca16e362f4 H4sIAAAAAAAC/02SQXYFQQRF51lLD1AU9r+xuDr5yaiPi4dXrS79qJo/+vgply91NUgNMRMJSA5xeeQJEVEIXa7UqNwccu6QSMiJa0M8hlyDlCQ6oZDBzzE1akhrUnOk6g5JgdxVzqSGtNbWWF+mJ8q1O6cXhEAbYunBPsU+zSw3SZQrf8lM3w0b5d5Z98qBTDBHQ2KkIflHQrerIXt7XRvlIG2yylnsEwSmW9OBh0Fgdn42dIhBdudqX3Ig8XaFQNAxXHU5r859yectwla5/pPV6fVQcTUQtfNe2rxykLbzX+fIS2aWtjVEP2Q+BkH51NaMc0N4Zfv5E6rGsQju8nhdbe4Kuvx+Zn0DyQ8EA3YCAAA=
```
