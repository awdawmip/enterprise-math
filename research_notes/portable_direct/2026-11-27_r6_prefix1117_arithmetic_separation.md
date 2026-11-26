# PREFIX-1117 — curvature spacing and the all-scale separation information barrier

Date 2026-11-27 Asia/Shanghai. EM-DIRECT-780BBE / TASK_RESEARCH; own RA-0ABD84561C86E53067DB0322. Author proof, NOT_REVIEWED. Parent PREFIX-1116 3c84968cbc80871053b2335d25155174dc851cf0:research_notes/portable_direct/2026-11-27_r6_prefix1116_convergent_lattice.md; PREFIX-1115 ddf71410e78ccd4f8eee59e8d96d8bab94ce03e5. Preserve P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d, joint relation observer preservation and native X6 time. Same Stage46 X6 chart O, incoming -e1, signed reversal -5 (phase cover 5q), all other weights 1, next incoming -d, both orientations Link{O,e1} blocked without renormalization, exactly two negatives. Retain native cell, port, signed phase, ordered branch multiplicity. Arithmetic below is an auxiliary observer on the inherited signed BRC certificate, not a new native propagation or independent native spatial plane.

Assume PREFIX-1107 strict sign rule with E=400000, m>=10^8 and E/m^2<=|j-f(m)|<=2, f(m)=rho*m+c+d/m; PREFIX-1097 global last-negative monotonicity; inherited joint density and anchor correspondence. The new analytic arithmetic theorems below do not require these native premises, but the Stage46 sign conclusions do. The inherited 8400 root command exit is unconfirmed. The 8800 command in this turn also produced a complete parseable JSON and final coefficient log but the outer command timed out, so its normal exit is unconfirmed. The exact downstream verifier completed normally; it checks nesting, thresholds and finite arithmetic, not independent validity of the analytic anchor construction.

## 1. Curvature spacing of true near-integer candidates on a lattice line

For real rho,c, d>0, E>0, coprime p,q with q>0, fix integer h=q*j-p*m. Let m in [L,H], 0<L<=H, and u(m)=(rho-p/q)*m+c-h/q+d/m. True near-integer candidates satisfy |u(m)|<=E/m^2. Every such m is in the one residue class -p^{-1}h mod q (q=1 has residue 0). For any three distinct candidates a<b<z on this line, u''(m)=2d/m^3>=2d/H^3. The function v(m)=u(m)-(d/H^3)*m^2 is convex, so its value at b is bounded above by the chord between a,z. Rearrangement yields

 chord(u;a,z)(b)-u(b) >= (d/H^3)*(b-a)*(z-b).

The same chord gap is at most 2E/L^2 because its three sampled values are in [-E/L^2,E/L^2]. Consequently

 (b-a)*(z-b) <= 2E*H^3/(d*L^2).

For N>=3 ordered true candidates, choose the first and last and a middle candidate of index floor((N-1)/2) counting from zero. Their product of gaps is at least q^2*floor((N-1)^2/4). Hence q^2*floor((N-1)^2/4) <= 2E*H^3/(d*L^2), and in particular if q^2>2E*H^3/(d*L^2), at most two true ambiguous points can occur per line. On a doubling window H<2L, the sufficient threshold is q^2>16E*L/d. This separates true analytic ambiguity from artificial uncertainty in a finite coefficient box. It does not assert the same spacing for the entire uncertain-box candidate set (which can be larger). It may help at a large continued-fraction denominator, but the number of lines and arbitrarily small denominators remain separate issues.

## 2. Uniform arithmetic separation cannot follow from a finite open parameter box alone

Fix any real c, any d>0, any E>0. For real rho define A_m={rho: dist(rho*m+c+d/m,Z)<E/m^2}. Each A_m is the union, over integers j, of open intervals centered at (j-c-d/m)/m, radius E/m^3. The set of slopes with infinitely many strict near-integer hits is S=intersection_{M>=1} union_{m>=M} A_m.

Every tail union is open dense: in any nonempty open interval I choose m>=M so large that the center mesh 1/m is smaller than the length of I; a center lies in I. More directly construct an irrational in any I by recursively taking a nonempty closed subinterval inside the previous interior intersect A_{m_k}, with m_k increasing, length <=2^-k and excluding the k-th rational (in a fixed enumeration). Such a subinterval exists by the mesh property and openness. The nested intervals have a unique common point avoiding every enumerated rational and satisfying infinitely many strict hits. Thus S is a dense G_delta; the construction proves density and irrational witnesses directly, without assuming anything about Stage46 rho.

On a bounded interval I=[a,b] of length ell, the number of A_m component intervals intersecting I is at most ell*m+2E/m^2+1. Each has length 2E/m^3, so for M>=2 the measure of I intersect union_{m>=M} A_m is at most

 2E*ell/(M-1) + E/(M-1)^2 + E^2/(M-1)^4.

Proof: sum the bounds 2E*ell/m^2+2E/m^3+4E^2/m^5 and compare each decreasing tail to its integral from M-1. The bound tends to zero, hence S is null. Almost every slope has only finitely many strict hits, whereas a dense G_delta set has infinitely many. The same null result holds for non-strict hits (use closed intervals of the same lengths).

The complementary eventual strict separation property also has dense witnesses even with c,d fixed: take any rational rho=p/q. The values rho*m+c modulo integers form a finite set. If any residues are nonzero their distance to the nearest integer has a positive minimum delta. For sufficiently large m, d/m<delta/2 and d/m<1/2. A nonzero residue then gives distance >=delta/2, and a zero residue gives distance d/m. Both are strictly greater than E/m^2 for sufficiently large m (the second when m>E/d). If there are no nonzero residues use just the second argument. Rationals are dense. This proves that every positive-width slope interval, even with fixed exact c,d, contains slopes with eventual strict separation and irrational slopes with infinitely many strict near hits. Arbitrarily precise finite boxes and finite prefix certification alone do not establish the all-scale result for the true Stage46 coefficients. This is a limitation of that information class, not an impossibility of proving separation via the actual BRC spectrum. Near hits also do not prove a wrong floor formula or exact zero: the strict analytic sign rule is merely inconclusive inside the band.

## 3. Exact finite computation, nested 8800 output and seven old candidates

Verified the parent archive manifest (6 listed entries), and the PREFIX-1115 archive manifest (22 entries). Reused the original signed density code replay_8000.py unchanged (N=260, 261 terms). The only changes to root_8400.py were [7200,7600,8000,8400] -> [7600,8000,8400,8800] in the anchor call and result metadata, parent input root_8000_result.json -> root_8400_result.json, and output filename root_8400_result.json -> root_8800_result.json (write occurrence only). This invokes the existing signed BRC auxiliary carrier and exact dual, no classical comparison. Actual command timed out at the outer execution boundary after the complete JSON and final c,d log appeared; no clean exit receipt. Parent fixed grid denominator 10^85 retained. Independent downstream exact verifier ran normally.

8800 rational box endpoints, all divided by 10^85:
rho 214400367204046439832747905320189591538351105920951930768238591471337001196383226040275 .. 214400367204046439832747905320189591538351105920951930768238591471337001196383235591606
c 991410104376806546245006442360370506919542722555360711737697284896269484488367063573850 .. 991410104376806546245006442360370506919542722555360711737697284896269484488368106987111
d 96908626596415488199625924806903600960651737707918479478269855625061455284941067578033 .. 96908626596415488199625924806903600960651737707918479478269855625061455285040066368357
Outward-rounded box widths 9.551331e-79, 1.043413261e-76, 9.8998790324e-75. Each lies strictly within the corresponding previous 8400 box.

The seven old candidate pairs are exactly those in PREFIX-1116 section 4, indexed there in ascending m order. Thresholds computed with the old 8400 box sort as [3,7,2,6,5,1,4]; minimum consecutive gap 3.9624349848815014e-76, maximum width 1.7144199221828455e-105 (rounded display). All thresholds disjoint and interior to old rho box. The 8800 box lies strictly after the fourth and before the fifth threshold. Hence the seven are closed under the inherited sign rule and computed anchor premises: indices 3,7,2,6 negative; indices 5,1,4 positive. Minimum integer-to-new-band gap 6.298545648437197e-38. All seven agree with the old 8400 midpoint floor prediction; no corrections. The new midpoint also agrees.

## 4. New finite window

Using nested 8800 box, reuse all previously noncandidate certificates. Exact new lattice sweep over 10 doubling windows starting at 15845632502852867518708790067200000000 and ending (exclusive) 16225927682921336339157801028812800000000. Window counts [0,0,0,0,0,0,0,0,26,96], 102 lines, 647 rational function evaluations, 122 remaining pairs in 62 progressions (19+43). All remaining candidates are uncertainty-band positions, not established true near hits or zeros. Maximum band width <1 on total covered interval checked. First remaining pair:
m=4265326180744162387203315935318273935179
j=91448749939658137083024518781782759561722.
Under the above inherited and anchor premises, continuous [10^8,m) is certified, count 4265326180744162387203315935318173935179. Total covered excluding 122 is 16225927682921336339157801028812699999878. All certified scales have K_last=floor((r*m+s+t/m)/10^85) for exact midpoint integers:
r=214400367204046439832747905320189591538351105920951930768238591471337001196383230815940
s=991410104376806546245006442360370506919542722555360711737697284896269484488367585280480
t=96908626596415488199625924806903600960651737707918479478269855625061455284990566973195.
The midpoint lies in the new box; nesting preserves previous certificates and newly excluded integers have strict signs by PREFIX-1107. No per-scale native CT enumeration.

## 5. Reproduction, evidence and next unit

Original exact lattice implementation: 2ec540692bf1ba695b60416903db654f797f3e67:research_notes/portable_direct/2026-11-27_r6_prefix1116_convergent_lattice.py. Use the previous archive PREFIX-1115 and PREFIX-1116, the above root script delta, and new verifier. Actual local files:
root_8800.py SHA256 9c2964fd0fec2d266a78284fa4169bff06559d2d5d77d651392ecb9c315b5509
root_8800.log 92931ec3908d89cf76404d77735fdf2d84be252e5be3009b265a7828000159bf
root_8800_result.json 367ed5c982ef92405623cfe6633aa29ce1449bfa2e1cb2e355fd8692d84355a9
prefix1117_verify.py 4b86b71164c92ee0a65bbf65c0bbcdcf3e548968aa6818113a9bd02c2f199c37
prefix1117.log 91c95d9dca2b9746fa42a32089ebb0f39a87cd9e79fec33696e32481a1a4443f
prefix1117_result.json 5204d06289bba9d8155044be15f673e07d63d66b32bb7fc997b088d2ae1821a8
Exact local evidence archive PREFIX-1117-execution-evidence.zip includes raw code, results and input material. The finite verifier is reproduced below; it was executed with the original local files, not merely transcribed. The exact 8800 coefficient boxes above suffice for all downstream arithmetic; no new native attribution is claimed.

Control: own original session registration r6-20261123-2358-session-start-own-v1 SUCCEEDED. Current owner read r6-20261127-0347-leased-read-v1 SUCCEEDED/error=null, snapshot 2026-11-26T19:48:14.485725Z, Source dc57e4797bbdfd3f48b000743d69d63da7d3ac40, LEASED tasks empty, next_cursor null. Independent research, no new CLAIM or shared task state mutation. Next: exploit arithmetic structure of the actual spectral coefficients rather than assume interval width alone proves global separation; characterize the 122 uncertainty candidates in the joint threshold coordinate, and confirm clean anchor execution if useful. Mother B_fix,odd(32), all-scale strict separation for true coefficients, exact-zero decision and remaining spectrum open.

### Actual downstream verifier

```python
from fractions import Fraction as F
from pathlib import Path
from math import floor,ceil
import hashlib,json
from prefix1116_lattice import load,expand,sweep,stats,E,G
old=load('root_8400_result.json');new=load('root_8800_result.json')
assert all(a<=c<=d<=b for (a,b),(c,d) in zip(old,new))
R,C,T=old
prev=json.loads(Path('prefix1116_result.json').read_text())
pairs=sorted(p for w in prev['extension_windows'] for p in expand(w));assert len(pairs)==7
thresholds=sorted(((F(j)-C[1]-T[1]/m-F(E,m*m))/m,(F(j)-C[0]-T[0]/m+F(E,m*m))/m,i+1,m,j) for i,(m,j) in enumerate(pairs))
assert all(R[0]<l<=u<R[1] for l,u,*_ in thresholds)
gap=min(y[0]-x[1] for x,y in zip(thresholds,thresholds[1:]));assert gap>0
width=max(u-l for l,u,*_ in thresholds)
results=[]
for l,u,i,m,j in thresholds:
    lo=new[0][0]*m+new[1][0]+new[2][0]/m-F(E,m*m)
    hi=new[0][1]*m+new[1][1]+new[2][1]/m+F(E,m*m)
    assert hi-lo<1
    sign=-1 if lo>j else 1 if hi<j else 0
    assert sign and (new[0][0]>u if sign==-1 else new[0][1]<l)
    results.append(dict(index=i,m=m,j=j,sign=sign,gap=str(lo-j if sign==-1 else j-hi),threshold=[str(l),str(u)]))
assert [x['sign'] for x in results]==[-1]*4+[1]*3
end=prev['extension_windows'][-1]['H']+1
w=sweep(new,end,end*1024);a=sorted(p for x in w for p in expand(x))
assert len(a)==122 and sum(x['count'] for x in w[:8])==0
mid=[(int(x[0]*G)+int(x[1]*G))//2 for x in new]
# compare previous midpoint floor on the seven; a changed prediction is not a certificate failure.
oldmid=[(int(x[0]*G)+int(x[1]*G))//2 for x in old]
def pred(m,r):return (r[0]*m*m+r[1]*m+r[2])//(G*m)
for x in results:
    m,j=x['m'],x['j'];k=j if x['sign']==-1 else j-1
    assert pred(m,mid)==k
    x['old_midpoint_correct']=pred(m,oldmid)==k
assert new[0][1]*end*1024+new[1][1]+new[2][1]/10**8+F(E,10**16) - (new[0][0]*end*1024+new[1][0]+new[2][0]/10**8-F(E,10**16))<1
out=dict(box_widths=[str(y-x) for x,y in new],threshold_gap=str(gap),threshold_maxwidth=str(width),resolved=results,extension=stats(w),windows=w,remaining=a,first=a[0],end=end*1024,mid=mid,raw_sha256=hashlib.sha256(Path('root_8800_result.json').read_bytes()).hexdigest())
Path('prefix1117_result.json').write_text(json.dumps(out,indent=2))
print('widths',*[float(y-x) for x,y in new]);print('threshold order',[(x['index'],x['sign'],x['old_midpoint_correct']) for x in results]);print('gap',float(gap),'max width',float(width));print('stats',stats(w),'counts',[x['count'] for x in w]);print('first',a[0],'end',end*1024,'mid',mid);print('min sign gap',float(min(F(x['gap']) for x in results)))
print('raw sha256',out['raw_sha256']);print('result sha256',hashlib.sha256(Path('prefix1117_result.json').read_bytes()).hexdigest())
```
