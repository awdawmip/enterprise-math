# C91: six-weak BRC spectrum and seventh-order bound (author draft)

Model: C88/C90 fixed 156-edge, 142-face classical positive BRC auxiliary; 48 core characters; free ports 86,111; strong faces 8,11,44,61; anchor faces 89,118. This is not an X6-native theorem.

For the 68 other weak faces, exhaustive 3+3 and separately implemented raw-edge 2+4 character enumerators agreed on all six-face surviving records and exact weights: A=448 (2415/16), B=418 (297/2), C=418 (297/2), D=448 (2415/16). The 1732 records were each checked against original 156-bit edge XOR.

Using C90's exact lower-degree table, set U_P(e)=sum_{k=2..6} W_{k,P} e^k + (81/4)sum_{k=7..68} C(68,k)e^k. At e=1/39, an independent integer proof verifies (15/16-U_A)(15/64-U_D)-U_B U_C > 1/100. Therefore, for anchor couplings 1/2<=a,b<1 and all independently varying 0<=r_f<=1/39, the sign of AD-BC is (-1)^(c18+c19) for every feasible 48-bit core.

This extends the C90 bound e<=1/50 by factor 50/39. At e=1/38 the sufficient bound fails, not the model theorem.

Exact portable archive SHA256: 0b20c849fc2dda7ee181a8b9f31f418c7def82ae894bb2134ca231cab662c174. Clean-extract reproduction and two independent enumerators passed.

Status: author verified; no formal CLAIM, native Result, or Driver admission. Native session failed STATIC_READONLY_SCOPE_DENIED; owner inventory failed CONTROL_QUOTA. Parent snapshots: GLOBAL_KNOWLEDGE_V1 main@6f655732470397df513f23f209290f35295eb8b0; Enterprise Math main@826aa3075754e007637ce84ff68d9156fdefdb7b.

Next C92: exact seven-weak spectrum or genuine determinant zero/sign-flip witness, preserving joint face relations.