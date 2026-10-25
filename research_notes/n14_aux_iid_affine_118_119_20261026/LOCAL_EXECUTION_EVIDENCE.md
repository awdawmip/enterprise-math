# Executed author-side evidence — N14 auxiliary iid Stage118 and Stage119

Observation date: 2026-10-26 (Asia/Shanghai).
Role: local direct author research only. This is not an independently reviewed computation and not a native task Result. This record is extracted from exact local program output; uploading code to GitHub is NOT executing it there.

## Local execution and coverage

Executed in the local Python runtime:
- python VERIFY_STAGE118_119.py (standard-library exact Fraction Bellman/conditional moments, plus literal ordered-history DFS using integer numerator weights)
- python independent_ordered_stage118.py (separately authored integer-history DFS; imports neither the main checker nor the other stage's DFS)
- python independent_ordered_stage119.py (same independence property)

All three runs produced PASS. This source folder's VERIFY_STAGE118_119.py is a runnable portable derivative of the executed local primary script, with the same substantive fraction recurrences and assertions, independently remote-read-back as source; publication alone has not rerun that remote file. The two separate locally executed DFS scripts, their exact sidecar JSON comparison inputs and outputs are included in the user-facing ZIP archive, not presented as remote-executed GitHub code.

The exact finite domain consists of 680 count states (sum binom(n+2,2) from n=0 to14), with complete 1240 alternative-action gaps. At each of the two stage dual points: 1238 strictly positive gaps, exactly two tied states, zero negative gaps. Native owner verification was unavailable.

## Recorded Stage118 full results

K=254421/296, L=90232/111, root=3609077962245944299849/6080637848103419904, min positive gap 837575281/15909322752.
D=(9,1,2), G=(13,6,4), first-hit ordered counts 172 and 15234.
First-hit P mass D=671875/53747712; G=317375/3131031158784.
First-hit Q mass D=671875/20155392; G=317375/2229025112064.

At tied-action continue baseline M00=(eP,eQ,tP,tQ):
- 608646098809500173/1752976676930715648
- 55734695409295/160489808068608
- 2803541503230308399/219122084616339456
- 54211857203227/4458050224128

Exact D-Q-stop gradient:
(593265625/5283615080448, -430671875/5015306502144, -34607609375/1981355655168, -17355203125/417942208512).

Exact G-Q-stop gradient:
(317375/25048249270272, -317375/26748301344768, -317375/3131031158784, -317375/2229025112064).

Error-balanced endpoint D-Q-stop weights 376073711298041/1042086080000000 and 376202743278041/1042086080000000. Opposite G Q-stop endpoints z=1 and z=0. Error growth eta=11742875/9527238592561152. At both endpoints eP=eQ, tP>tQ. tP-tQ margins:
- 1333116856006035527645/2074346604281154502656
- 1333122950341609217645/2074346604281154502656

Literal integer DFS visited 898165, 852463, 890425, 844723 ordered prefixes at (w,z) corners 00,01,10,11 respectively; each of four M values matched exact Bellman conditional moment results exactly.

## Recorded Stage119 full results

K=14079159385935/17413198588, L=272890577165656/352617271407, root=2715351325492390545950322492769/4829139473901711838949670912; minimum positive gap 76168651372577/5483903804921664.
D=(9,1,2), J=(6,5,1), first-hit ordered counts 172 and 4. First-hit J masses P=1/196608,Q=1/746496, D unchanged.

Same rational M00 and D gradient as Stage118. Exact J-P-stop gradient:
(-287489051/10820843684757504, 5340805/160489808068608, -2860972883/450868486864896, -27244717/13374150672384).

Error-balanced endpoint D-Q-stop weights 376202743278041/1042086080000000 and 376517470455067/1042086080000000, opposite J P-stop weights y=0 and y=1. Error increment eta=4353299647/592805956870471680. At both endpoints eP=eQ, tP>tQ. tP-tQ margins:
- 1333122950341609217645/2074346604281154502656
- 1333129085804580517835/2074346604281154502656

Literal integer DFS visited 898165, 893725, 890425, 885985 ordered prefixes at (w,y) corners 00,01,10,11 respectively; moment equality with independent DFS passed at all corners.

The affine formulas for all real parameters follow from proved disjoint first-hit cones and the finite support structure, not a finite real-grid test. Right-edge sharpness follows from the full Bellman tie classification and equality conditions for positive K,L.

## Local immutable content fingerprints and full archive

Executed local source SHA-256:
- VERIFY_STAGE118_119.py: 27edca58bd382e604f1e378cf6be9925ea4e943959c9928c624fb49f25d385d6
- independent_ordered_stage118.py: 7fec2fd1eeffc084483774c4775da8a8361446e792a5b49cb0ba9ba1485dc0c2
- independent_ordered_stage119.py: 8bd42662106cb332fe9c6c70cf610c92be234b75e79c2ed495f671e4c704a775
- local exact primary JSON output verification118119.json: 944f56df71115dbfa5dbabcc39cf997bd7d34f50c5dc775dd098cf4f809616a9
- separate Stage118 DFS output: 4e6bcff48ebcb97ea22d20be203b1690f4b9553dd8dd655574aab612652fc939
- separate Stage119 DFS output: f326b91654528590896e1de420ebc6d2aabbcbf298fffb42038ae6ee2bbafb00
- local full proof draft SHA-256: bde39852ca7bb1f3f674391e887e031aa8c134c1679b45d5b4fc024752d163eb

User-facing archive: EnterpriseMath_N14_Stages118_119_20261026.zip, SHA-256 c4d6cc4a68385a424e04b7252cd522bea2cf94f7e2d781129c0a4674a9440ba4. The locally archived proof draft and source run are not claimed byte-identical to their GitHub portable derivatives. Archive ZIP testzip and all 10 member names passed.

GitHub immutably published proof, portable primary code, main exact certificate and Stage120 packet at commit cf692926028dfecc9c448975440435a9334828a2; readback matched emitted source exactly.
