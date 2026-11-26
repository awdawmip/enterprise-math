# PREFIX-1115 — signed derivative transport and ordered arithmetic thresholds

Date 2026-11-27 Asia/Shanghai. Independent continuation of EM-DIRECT-780BBE / TASK_RESEARCH, RA-0ABD84561C86E53067DB0322. AUTHOR_CONDITIONAL_ANALYTIC_PROOF / EXACT_RATIONAL_AUXILIARY_COMPUTATION / NOT_REVIEWED.

## Scope and frozen source

P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json and joint relation observer preservation unchanged. Stage46 X6 chart O, incoming -e1, signed reversal -5 (phase cover 5q), other weights 1, next incoming -d, both orientations of Link{O,e1} blocked without renormalization, exactly two negatives. Keep Cell, port, signed phase, ordered branch multiplicity of the original BRC joint carrier. This is a certified auxiliary observation of that same signed carrier; no new physical propagation, CT enumeration, classical comparison or native residual attribution. Mother B_fix,odd(32) open.

Parent 1af1b1acc240cb357002faadf8ee6617bc81809e:research_notes/portable_direct/2026-11-27_r6_prefix1114_signed_interval_newton.md; inherited E=400000 for m>=10^8 and strict sign condition (PREFIX-1107), global last-negative monotonicity, density jet identities PREFIX-1096/1113. Actual prior archive PREFIX-1114-execution-evidence.zip (22 manifest entries verified). Parent scripts replay_hi.py, root_7200.py and root_7200_window.py and parent JSONs retained as exact inputs. All calculations are within inherited signed BRC observation correspondence, not new confirmation of that correspondence.

## 1. Signed derivative transport

For F(t)=sum_i a_i P_i(t), let I contain the true root, x in I, r=max(x-inf I,sup I-x). Suppose V_j(x) encloses the complete signed F^(j)(x), and W_(j+1)(I) encloses F^(j+1) on I. Then for all t in I,

 F^(j)(t) in V_j(x)+[-r B_j,r B_j],
 B_j=max(abs(inf W_(j+1)),abs(sup W_(j+1))).

Proof: integrate F^(j+1) over the interval between x and t, or apply the real mean value theorem. Use the joint dual at the fixed point and pay full analytic tails; W is the signed derivative of the entire combination, not the sum of component magnitudes. Intersect this enclosure with the old component interval enclosure. Both contain the true derivative, hence the intersection is rigorous and never wider than the old enclosure. It can be tighter even without improving the root box. The actual 8000 run enclosed derivatives 0 through 5, evaluated derivatives 0 through 4 at an exact rational center and used the next signed derivative for variation. For j=0 the exact root property is used only after the check.

Actual 8000 full vs point+variation widths (rounded display only):
j=0 3.009672807664289e-59 -> 1.6670595451815147e-60
j=1 8.406159137505645e-59 -> 4.315929927133931e-60
j=2 2.8906908605140242e-58 -> 6.287359933915516e-60
j=3 1.0385496505157967e-57 -> 4.532123592916576e-59
j=4 3.830565210267871e-57 -> 1.093183103061917e-58
All five intersections attained the narrower transport bound. Recompute c,d using the unchanged jet identities, not a new fit.

## 2. Arithmetic threshold order theorem

Write f(m)=rho*m+c+d/m. Assume inherited strict sign rule for |j-f(m)|>=E/m^2 and <=2, and inherited last-negative monotonicity. Given an integer candidate (m,j) from a coefficient uncertainty band of width <1, define

 L=(j-c_u-d_u/m-E/m^2)/m,
 U=(j-c_l-d_l/m+E/m^2)/m.

If rho<L, then f(m)<j-E/m^2, so D_m(j)>0. If rho>U, then f(m)>j+E/m^2, so D_m(j)<0. The original candidate band and E/m^2 small ensure the inherited |j-f|<=2 applicability and that adjacent j-1,j+1 have strict signs. Thus K_last is j if D_m(j)<0 and j-1 otherwise (including exact zero). For distinct candidates with ordered pairwise disjoint intervals U_i<L_(i+1), all strict-negative candidates form an initial segment of that order. Indeed a nonnegative outcome at i forces rho<=U_i, so every later interval has rho<L and positive D. A negative outcome at i forces rho>=L_i, so every earlier interval has rho>U and negative D. Therefore at most n+1 possible joint terminal patterns, rather than 2^n independent alternatives. With an exact terminating oracle for negative versus nonnegative at candidate positions, binary search needs at most ceil(log2(n+1)) queries to determine the cut. An undecidable sign or zero does not count as an oracle success. Alternatively one common rho refinement between adjacent thresholds simultaneously determines all outcomes. This is a conditional arithmetic compression theorem; it does not supply an all-scale lower bound, and does not assert an exact-zero oracle.

## 3. Actual exact computation

Parent recurrence and elimination matrix retained; increase Frobenius order N=200 to N=260 (261 terms); inherited bound factor=(pbound+(N+1+2)*qbound)/(N+1-2) verified <1, rather than using old N-specific equality. All original resonance and elimination hash checks pass. Anchor integer grid H=10^100 and outward integration grid 10^220 unchanged; center coefficient rounding 10^100 with full dr payment; interval arithmetic 10^140, report outward 10^85. First actual anchor [6800,7200,7600,8000] completed normally, followed by exact adaptive floor-sum sieve. Second anchor [7200,7600,8000,8400] produced complete parseable result JSON and final c,d output; the outer container command timed out (exit not confirmed). A separate successful exact threshold verifier subsequently read the JSON, checked nested boxes and all candidate outcomes. This second computed certificate is explicitly recorded with that execution limitation, not a clean command-exit receipt. Actual raw data and original code/logs are included in local evidence archive. No independent review.

8000 boxes (integers divided by 10^85):
rho 214400367204046439832747905320189591538351105920951930768238591471336985753828331576226 .. 214400367204046439832747905320189591538351105920951930768238591471337016618243377672837
c 991410104376806546245006442360370506919542722555360711737697284896267798454119146866295 .. 991410104376806546245006442360370506919542722555360711737697284896271170423247861515800
d 96908626596415488199625924806903600960651737707918479478269855624901489595100026049591 .. 96908626596415488199625924806903600960651737707918479478269855625221421002362182677574
Widths 3.0864415046096607e-69, 3.371969128714649e-67, 3.199314072621566e-65. All nested within parent. All 16 old candidates closed, minimum gap 4.329211176651565e-31. 90 doubling windows [10^8,123794003928538027489912422400000000), 5170 nodes, 22 candidate pairs, compact ordered candidate JSON SHA256 c000cf55b3d47848c40c44c1054616a8de93606fb5033268f57bcc2d19ee96e5. First pair (30614983299972440557741525569009913,656386366145984069336387628154657777).
Thresholds sorted by increasing L, using one-based index in lexicographic (m,j) list: [13,1,11,9,7,21,6,19,2,5,17,4,3,15,14,22,12,20,10,18,8,16]. All 22 intervals strictly inside common rho box, minimum consecutive gap 1.7452380626161474e-71, maximum width 2.7890701927217045e-98. Thus at most 23 possible sign patterns and at most 5 exact oracle decisions if available. The actual candidates also lie on three parallel integer lines q*j-p*m=constant: q=6711868895915652573356270627256609, p=143902715590973366560782416004716377, gcd=1. Classes [1,2,3,4,5,6,7,9,11,13], [8,10,12,14,15,17,19,21], [16,18,20,22]. No claim of universal three-line property.

8400 output (integers divided by 10^85):
rho 214400367204046439832747905320189591538351105920951930768238591471337001196109386645552 .. 214400367204046439832747905320189591538351105920951930768238591471337001196656728356815
c 991410104376806546245006442360370506919542722555360711737697284896269484458469127177428 .. 991410104376806546245006442360370506919542722555360711737697284896269484518264379180719
d 96908626596415488199625924806903600960651737707918479478269855625061452448312226656203 .. 96908626596415488199625924806903600960651737707918479478269855625061458121669367665141
Widths 5.4734171126218125e-74, 5.979525200328942e-72, 5.673357141008938e-70 (display). Independent-of-root-script finite verifier: nested boxes checked for all three parameters; all 22 candidate bands exclude j, minimum gap 7.357099805411848e-36. First 14 ordered thresholds negative, last 8 positive. No 8000 midpoint formula corrections among the 22. Hence conditional on inherited correspondence/sign lemmas and the produced root certificate, continuous range [10^8,123794003928538027489912422400000000) is now certified without exception, count 123794003928538027489912422300000000. Midpoint integers on 10^85:
r=214400367204046439832747905320189591538351105920951930768238591471337001196383057501183
s=991410104376806546245006442360370506919542722555360711737697284896269484488366753179073
t=96908626596415488199625924806903600960651737707918479478269855625061455284990797160672
K_last=floor((r*m+s+t/m)/10^85). Since final boxes nested in earlier boxes, all noncandidates retain floor and strict signs. No new sweep of the already certified range is needed.

## 4. Reproduction delta

Use exact parent archive (see parent paper for proof and compact reproduction). replay_8000.py is replay_hi.py with N=200 -> 260, assertion factor==F(5025203,5349120)<1 -> factor<1, scale=10**85 -> scale=10**100. All other bytes unchanged. root_8000.py is root_7200.py with import replay_8000, anchor [6800,7200,7600,8000], output grid 10^85, original jet_result slope grid D0=10^65 preserved, starting rho from root_7200_result.json divided by 10^65, derivative tail arrays increased from 5 to 6 (j=0..5). Use same polynomial and derivative construction, same interval Newton. Replace old derivative estimation section with:
```python
def joint(j,interval):
    vals=[horner(dp(p,j),interval) for p in pp]
    mids=[(v.a+v.b)/2 for v in vals]; widths=[(v.b-v.a)/2 for v in vals]
    center=sum(a*v for a,v in zip(cc,mids));ar=dual(mids)
    tw=sum((abs(a)+r)*w for a,r,w in zip(cc,rad,widths))
    tail=sum((abs(a)+r)*sum(comb(j,k)*rowbound[k]*tr[j-k] for k in range(j+1)) for a,r,tr in zip(cc,rad,tails))
    total=ar+tw+tail
    return I(center-total,center+total),(ar,tw,tail)
Fs=[];payments=[];comparisons=[]
full=[joint(j,t)[0] for j in range(6)]
x=F(floor((t.a+t.b)*G/2),G);radius=max(x-t.a,t.b-x)
for j in range(5):
    point,pay=joint(j,I(x)); shift=full[j+1].mag()*radius
    improved=I(point.a-shift,point.b+shift)
    out=I(max(full[j].a,improved.a),min(full[j].b,improved.b));Fs.append(out)
    payments.append([str(ceil(y*10**85)) for y in (*pay,shift)])
    comparisons.append(dict(j=j,full=float(full[j].b-full[j].a),point_shift=float(improved.b-improved.a),intersection=float(out.b-out.a),slope=float(full[j+1].mag())))
    print('Fjet',comparisons[-1],flush=True)
```
Continue original root property check and jet composition; add comparisons to result dict. 8400 script differs by anchor list, parent rho box from 8000 output on 10^85, and output filename. No claim that compact transcription separately executed. Exact original local scripts and results retained. root_8000_window.py is root_7200_window.py changing G=10**65 to 10**85, input/output filenames to root_8000, loop while l<10**35. Threshold verifier uses actual JSON endpoints and candidate list with Fraction.

Actual local SHA256:
replay_8000.py ef7609277d1cbaa80b99689a1965a1d80ecd33da5ff6bbec1d929f2ba4510cfb
root_8000.py cd957ab68e1c3a3d2d2e95a763e82259bc2e63c33dd10c472ddce0c69c64278c
root_8000_result.json 11e9c6b31913cce05749d258fbd20eaabdfc0be5d7de742bae2ea41c02b06bbd
root_8000_window.py 0b7b261dcf16124ba1ba49a3c9712377c397343aebc84aa9e36bd294faf8aaaf
root_8000_window_result.json c63652a3c38287c58d45277d54358a96c4b988e0dafd441a314ca510abe71abc
root_8000.log cbaeff5e3112b9cbb004a4a466926d0ceee7217315279b2f078f9d6841c7a437
root_8000_window.log 20e804ceba45e5328908f81f95d9cba4711a20a06a478b125e1e14c03672ffaa
root_8400.py f8172069096d5cb06d178730a21b75ae92dc125a9af954ba50bd685f9650b2ac
root_8400_result.json 5f99a39ec9e70b5c853197d865cb15486d8075f19170acc8dd5da1ed4adcd332
root_8400.log c1e05523a825362b60976dab84acb0670699b521f51a867528d45e6382956741
threshold_check.py 1202e18a48a701dd1599fec5e43cac1b1e70a0bd5b3793f1d9064a0ec5aa2628
threshold_result.json f23c744ed1f7c46757243c8effd3a95bcd14e96ce57d11530110703f5ac2b191
threshold_check.log 5767e380353ce982496bffd65f7a6990f6675358767f81e60842a2cd49b5848c

Control: original own session registration r6-20261123-2358-session-start-own-v1 SUCCEEDED, no live claim granted. Current owner read r6-20261127-0151-leased-read-v1 SUCCEEDED/error=null, as_of 2026-11-26T17:51:15.345016Z, Source c47d2367c4bc6039953742a97babaecdc7703eab, LEASED empty, next_cursor null; no new claim or shared state change. Next: confirm 8400 clean rerun if useful (preserve existing certificate); use threshold-order structure and homogeneous rational approximants to study uniform arithmetic separation or build exact zero decision. All-scale separation, remaining spectrum and mother target open.
