# EC49FAZ — Free H4/H5 selection, fixed H2/H3 and two later cache keys: exact 112-edge optimum

Date: 2026-11-05 Asia/Shanghai. Status: AUTHOR_FINITE_DP_CHECKED / PYTHON_PARTIAL_CROSSCHECK / UNREVIEWED / NOT_ADMITTED.
Source science frozen at fc0f038e7bfd12c886b4d37f900bfb770c0f61ab; extends EC49FAY@ccd19ace0a348f769294cf96ad770b986ac5ddeb.

## Exact family theorem

Use the original ordered **signed native X6 primitive** path model and six-signature nine-history observer. Fix only H2={fe,ge} and H3={feg,gef}; their primitive-prefix union has 16 edges. Select arbitrary finite sets of words at H4–H9, with native endpoint (+2,0,0,0,0,0), complete positive six-axis cache keys K4=K5=(4,2,1,0,0,0) and K6=K7=K8=K9=(6,4,1,0,0,0), permitted six signatures, and rational rank nine in each window. Count the union of all signed primitive prefixes with literal path identity.

Then the exact minimum total native primitive-edge count is

**E*(H2/H3 fixed, H4/H5 word selection free, late keys fixed)=112.**

EC49FAY required exact H4/H5 word sets. This result optimizes those word sets as well; H4/H5 prefixes may be freely shared with H6–H9.

## Complete enumeration

For word length h and key (x,y,z,0,0,0), terminal balance forces: #a=z−1, #e=z, #c+#d=x+y−h−1, #f=h+1−y−2z, #g=h+1−x. Enumerate each c/d split and all distinct permutations. Apply the EC49FAX nine-state transition table (included in the verifier). The permitted signature populations are H4: 12 each of D/E/C/J, total 48; H5: 12 each of F/G, total 24; H6: 80 D, 40 E, 80 C, 40 J, total 240; H7: 360 D, 270 E, 360 C, 270 J, total 1260; H8: 560 each D/E/C/J, total 2240; H9: 280 each F/G, total 560.

EC49FAR's four-clause rank-nine criterion forces all four signatures on H4/H6/H7/H8 and both F/G on H5/H9. Thus the coverage target is 4+2+4+4+4+2=20 bits.

## Exhaustive exact min-plus/OR dynamic program

Expand each candidate operation word to the following **ordered signed primitive** steps: a=(-1,-1), c=(1,2,-1,-2), d=(2,1,-2,-1), e=(3,1,1,-3), f=(1,-1), g=(2,-2). The first two primitive symbols uniquely determine each operation, so the six operation codewords are prefix-free. Insert all eligible candidates in one signed-primitive trie. Nodes already in the fixed H2/H3 primitive trie are free, all other non-root primitive-prefix edges cost 1 when selected.

At each node v let D_v[m] be the minimal cost for a selection of terminal words under v whose rank-coverage OR mask is exactly m. Initialize the empty choice m=0 at zero cost; allow any terminal's mask at zero cost; combine child masks by the exact recurrence D_new[m OR n]=min(D_new[m OR n],D_old[m]+D_child[n]). Count the incoming primitive edge once for a nonempty mask if not a fixed early prefix. Induction on the trie proves that every eligible subset is represented and every cost is its exact native signed-prefix-union cost.

The executed Node.js integer verifier counted **26,705 trie nodes**, **1,048,576 root masks**, and **21,972,032 pairwise state merges**; minimum new edges beyond fixed H2/H3 are **96**. The jointly optimized cumulative target costs for requirements through H4,H5,H6,H7,H8,H9 are respectively 16,22,54,66,90,96 *new* edges. Therefore lower bound 16+96=112.

## Explicit attaining witness

H2: fe, ge
H3: feg, gef
H4: fegc, fegd, gefc, gefd
H5: feggf, gefgf
H6: fegccc, fegddd, gefccc, gefddd
H7: fegccfg, fegddgf, gefccfg, gefddgf
H8: feggfgfc, feggfgfd, gefgfgfc, gefgfgfd
H9: feggfgfgf, gefgfgfgf

The independent Python standard-library validator checks each witness word's signed displacement, cache key, rank-nine signature mask and native prefix counts; cumulative H2–H9 edges are **12,16,32,38,70,82,106,112**. It independently confirms H4/H5 candidate signature multiplicities; it does **not** independently implement the full 20-bit lower-bound DP.

## Reproduction, limits and next action

Run: node VERIFY_EC49FAZ.js > EXACT_REPORT_EC49FAZ.json
Run: python CROSSCHECK_EC49FAZ.py > CROSSCHECK_REPORT_EC49FAZ.json

All costs are exact integers; 20-bit DP validates a finite universe justified by the complete multiplicity enumeration. Result is author-side and awaits independent mathematical review and actual authorized Source CLAIM/Result. No alterations of P000, ACTIVE worldview or frozen scientific inputs. The unrestricted H9 mother problem retains the previous author-side interval 80 <= E* <= 94, with a distinct 94-edge witness outside this fixed-key family.

**Next EC49FBA:** vary the H4/H5 cache key schedule or the fixed H2/H3 early choice. Reuse EC49FAW's 124 eligible double-key schedules and EC49FAV's 31-edge/two-key early alternatives; seek E<=93 or a broader exact optimum, keeping literal signed primitive prefix costs.