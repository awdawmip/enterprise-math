# X6 R278 — sixth-pencil continuation and future-safe row-envelope reduction

2026-11-27. Independent informed TASK_RESEARCH, author proof and computation, NOT_REVIEWED. Topic read r2-20261127-2208-x6-read SUCCEEDED at 14:08:59.303211 UTC, Source af81386070eb9079f70af7e52183936a68e5f920, NO_CANONICAL_PUBLICATION_DIRECTORY (not native owner projection). Own researcher binding unconfirmed; no CLAIM or shared-state mutation. P000 V5, joint-relation and residual fidelity preserved. Auxiliary weight-coefficient algebra, not native spatial plane or temporal claim.

## Frozen input and scope

R277@a1df3c1aa315909d8c109ef8551f24a460a44b1f:research_notes/portable_direct/2026-11-27_r2_x6_r277_incremental_slope_projection_sixth_prefix.md, with R247@7e54892a45579bdc497c27e061399339d1fb3512, R275@001076e59298e45715cb58c87ab3395c53d005a8, R276@33fba542db5f810e803d770b7046b5e26ac1ebb9. Same exact frozen Port 10, 1935 directions, 47 supports, 51 endpoints, 98 germs, 2225 suffix partitions. Capacity exclusions inherit necessary-wall and complete suffix premises. Strict words c=1 only. Continue R277 from [1000,0]; do not rerun the closed prefix or the five-line search.

## New lemma: interval-relative dominance is safe under all future intersections

Let R277's exact strict feasibility state be (P,M,I), where I is the open projected f interval and the rows in P,M have respectively positive and negative e coefficients. For each row r=(A,B,C), A nonzero, define g_r(f)=(-Bf-C)/A. P requires e>g_r(f); M requires e<g_r(f). For a nonempty I the complete joint feasible set is f in I and max_{r in P} g_r(f)<e<min_{r in M} g_r(f), with empty bounds interpreted as infinities.

Suppose p,r belong to P and g_p(f)>=g_r(f) for every f in I. Then discard r, retaining I and p. For M the sufficient condition is g_p(f)<=g_r(f). Proof: within I the inequality of p implies the inequality of r, including equality of boundary functions since e is strictly on the required side. Outside I neither old state nor compressed state allows any point. Thus the joint feasible set, not merely the f projection, is unchanged. Intersecting equal sets with an arbitrary future conjunction of rows preserves equality; every later projected f interval is therefore also unchanged. This proves a future-context lease for the specific operation of adding rows, not for deleting historical constraints, reweighting rows, or recovering their provenance. Keep original endpoint words and germ masks; they are not compressed by this lemma.

Exact dominance test: write D(f)=g_p(f)-g_r(f) for lower bounds (reverse for upper). It is rational affine. On a finite nonempty open I=(l,u), D>=0 everywhere iff D(l)>=0 and D(u)>=0 by continuity and affinity. For an infinite endpoint use the sign of the slope (nonpositive toward -infinity, nonnegative toward +infinity); finite endpoint still tested. On R require zero slope and nonnegative constant. All comparisons are exact cross multiplications. In particular parallel rows with equal B/A can be reduced to the strongest intercept: for A>0 retain largest -C/A, for A<0 retain smallest -C/A. This latter special case works on R. Compression requires retaining I itself; dropping it could resurrect points previously ruled out by removed rows. Example: e>0 and e>f, I=(-1,0), e>f can be dropped under the retained interval; allowing f>0 later by dropping I would invalidate that reduction. Pruning by current active projected endpoints alone without joint-set dominance is not justified.

This lemma is a proved mathematical optimization; the new batch below used the unchanged R277 incremental algorithm, not an implementation of the envelope optimization. No wall-time or row-count improvement is asserted. For the next implementation measure dominance overhead and cross-pair count, and verify exact joint feasibility against the uncompressed R277 state.

## Actual continuation computation

Executed the exact R277 reproduction algorithm, start=1000, size=800, ceiling=25000000. All 63200 extensions classified; first 100 algebra-tested extensions compared with R275 full elimination and agreed. Packed support count self-checks rerun. No cutoff. Results:

```json
{"direct":20168,"alg":34996,"recursive":7519,"surv":517,"visits":63200,"checkedAgainstOld":100,"checks":22237932,"next":[1800,0],"partial":false}
```

Cumulative sixth-line coverage including R277: 142200 / 667787, 1183 necessary-condition survivors, 525587 unclassified. Total classified exclusions 141017. Next index [1800,0]. All 517 new survivors below in R277 prefix:hex mask format. Prefix-row count is 184; validated strictly increasing range and total popcount 517.

```text
1002:6060300000000
1004:6060300000000
1007:400000000000
1008:300000000000000
1009:300000000000000
1010:84180000020000000
1011:300000000
1012:6060380000000
1014:6060380000000
1017:100000000
1080:300000000000000
1081:40200000000
1082:306000000000000
1084:40200000000
1085:40200000000
1089:60200800000
1090:306060300000000
1091:300000000000000
1092:84180000000000000
1093:60300000000
1094:6060300000000
1095:307078380000000
1097:60300c00000
1098:20100000000
1100:60300c00000
1101:60300000000
1102:4060300000000
1103:40200000000
1141:200000000
1143:200000000
1144:40200000000
1146:200000000
1147:200000000
1151:200000000
1152:306060200000000
1153:307000000000000
1154:84180000000000000
1156:300000000
1157:6060300000000
1158:307070380000000
1159:40000000
1160:300c00000
1161:100000000
1163:300c00000
1164:300000000
1165:4040300000000
1166:200000000
1187:200000000
1192:6000000000000
1195:60200000000
1196:60300000000
1197:6070380000000
1198:8040000000
1199:60300c00000
1200:70380e00000
1202:40200000000
1203:40200800000
1204:c204000000000000
1205:c300000000000000
1206:886180000000000000
1207:2000000000000
1216:18c000000000000000
1217:80000000000000000
1222:8000000000000000
1223:8000000000000000
1224:8000000000000000
1230:c0
1232:40
1233:1dc2080000000020040
1234:40
1235:40
1236:600c0
1237:10030
1238:400000000000010030
1239:c0
1241:20
1243:c0
1247:c0
1250:c0
1251:c0
1254:60040
1257:8000000
1259:8000000
1260:8000000
1264:80000000
1266:38020000
1268:80000000
1269:180f8060000
1278:2000000000000000
1279:1c0
1280:180600c0
1281:4010030
1282:4018038
1283:20040
1284:20
1285:10030
1288:600c0
1290:600c0
1291:c0
1292:c0
1294:1c0
1299:8000000
1300:8000000
1304:600c0
1305:8000000
1306:8000000
1308:18000000
1309:8000000
1312:18038020000
1314:8078020000
1315:38020000
1317:8060000
1318:80000000
1319:180f8060000
1321:80200000
1323:200
1324:200
1325:80
1347:10000000
1349:10000000
1350:1000000000000
1352:180300
1353:300
1357:100200
1360:8060000000
1362:40100000
1367:40100000
1368:20000000
1372:80000
1376:808000000000
1377:c0c000000000
1379:80c000000000
1406:1000000000000
1629:400000000000000000
1630:400000000000000000
1634:8
1635:40
1640:40000000000030000
1643:1800000000
1652:2080000000000000
1655:18000000
1666:18020000
1667:18020000
1668:1000000000000
1670:10000000000
1675:400000000000000000
1677:60
1680:80
1682:80
1683:40
1685:40
1689:400000000000000000
1690:400000000000000000
1691:400000000000000000
1700:8000000
1704:c2080000000000000
1706:40000000000000000
1707:8000000
1708:381c000000
1709:8000000
1710:c000000
1711:10000000
1712:40000010180e000000
1715:8000000
1718:18000000
1719:c2081000000000000
1720:8000000
1721:1c000000
1724:100c000000
1725:100e000000
1726:8000000
1727:c000000
1729:18020000
1732:38000000
1733:18020000
1734:18020000
1735:18020000
1736:1008038040000
1737:60000
1762:4000000000
1776:400000000000
1779:20000000000000
1780:20000000000000
1782:20000000000000
```

## Reproduction and next
Reuse R277's exact assembly and four immutable notes. Run with start=1000,size=800. The sixth-direction grouping is [10,15,11,45,49,9,38,42,40,44,47,50]. No code modification in this batch. Continue [1800,0] and preserve R277+R278 banks; test the new interval-relative row dominance before claiming implementation gains. Then singleton directions and zero words. K6 remains 1–2. Independent review and Activity association pending.
