# X6 R277 — exact incremental strict slope projection and sixth-pencil prefix

2026-11-27. Independent informed TASK_RESEARCH, author proof and computation, NOT_REVIEWED. Native topic read r2-20261127-r277-topic-read SUCCEEDED at 13:06:27.343600 UTC, Source 5b0b3c43f941ce04f80d46754acaacf31e7a8fd1, NO_CANONICAL_PUBLICATION_DIRECTORY, not an owner projection. Own researcher binding not confirmed; no CLAIM, formal Result, Review or shared-state change. Activity association pending. P000 V5, ACTIVE worldview and joint-relation/residual fidelity retained. Auxiliary weight-coefficient algebra only; not a native spatial plane or temporal claim.

## Inputs and inherited scope
R247@7e54892a45579bdc497c27e061399339d1fb3512 (fdbef2ee6e6c32573f3a1ccd171cb5337de520fa), R275@001076e59298e45715cb58c87ab3395c53d005a8 (9732c23573cf3071a782d0b84d511494ebb1c745), R276@33fba542db5f810e803d770b7046b5e26ac1ebb9 (597a62f00fb89d9624e301bbca97f0073b37a040); paths are research_notes/portable_direct/2026-11-27_r2_x6_r followed by 247_two_anchor_signed_primary_faces, 275_monic_block_compression_and_strict_prefix, 276_strict_fifth_pencil_packed_frontier and .md respectively. Same frozen Port 10, 1935 directions, 47 support labels, 51 endpoints, 98 germs, 2225 linear suffix partitions. Capacity exclusions inherit R247 necessary-wall and complete pure-linear suffix premises. Strict words c=1 only. All 8453 five-line survivors retained by R276; do not repeat five-line search.

## Incremental projection lemma
For strict rows A e+B f+C>0, keep distinct rows with A>0 in P and A<0 in M. The exact f projection is the intersection I of all A=0 strict half-lines and every (A_p B_m-A_m B_p) f+(A_p C_m-A_m C_p)>0, p in P,m in M. Proof: for fixed f every positive row gives a strict lower bound on e and every negative row an upper bound. A real e exists iff every lower bound is below every upper bound; if one side empty choose e beyond the other finite extreme. Thus each projected constraint is necessary and sufficient jointly, including unbounded and empty cases. I is an open interval (possibly all R or empty); keep rational lower/upper bounds by cross multiplication. When a new positive row arrives, intersect I with constraints pairing it with every old negative row, then append it. Symmetrically for a new negative row; flat rows directly intersect I. Induction: every opposite-sign pair appears exactly once at arrival of its later row. Positive rescaling and exact dedup preserve the same inequalities. Empty I permits immediate rejection; otherwise the saved P,M,I must all be retained, since a future row may interact with an old bound not currently active in I. This gives an exact reusable incremental state, not a lossy projection onto the f interval alone. For old p,m and new u,v rows of each sign, updating all pairs requires at most p*v+m*u+u*v new pair comparisons, versus (p+u)*(m+v) from scratch. No measured wall-clock speedup is asserted. Copies used to branch are included in implementation cost. Old row state constructed once per five-line word; each sixth extension clones it, adds only new circuit and local rows. Strictness and unbounded intervals handled exactly. All branch masks and distinct endpoint words retained.

## Exact computation and continuation
Sixth direction B=0 has 12 finite samples, hence 79 strict words; total 8453*79=667787 possible extensions. Deterministic word order: R276 text bank line order, then ascending fifth-pattern set bit, and R275 l-major/h-major sixth pattern order (0 all positive). All indices zero-based. First batch [0,150) and second starting 150, requested end 1000, disjoint. Full new classified visits and next index below; if partial, the interrupted candidate at next is unclassified and all preceding classified survivors are retained. First batch used a 20m ceiling, second 25m, both BigInt; first batch completed without cutoff. In each run first 100 algebra-tested extensions compared incremental feasibility with original R275 full Fourier–Motzkin exactly; all agreed. R276 count projection self-checks rerun. No repeated five-line capacity decisions. All survivors are necessary-condition survivors, not valid decision trees. Remaining 11 singleton directions and zero words not searched here.

```json
{"direct":40104,"alg":33711,"recursive":4519,"surv":666,"visits":79000,"checkedAgainstOld":200,"checks":11660320,"next":[1000,0],"total":667787,"unknown":588787}
```
First batch stats: {"hist":{"direct":7511,"alg":3235,"recursive":925,"surv":179,"visits":11850,"checkedAgainstOld":100},"checks":2431859,"next":[150,0],"partial":false}
Second batch stats: {"hist":{"direct":32593,"alg":30476,"recursive":3594,"surv":487,"visits":67150,"checkedAgainstOld":100},"checks":9228461,"next":[1000,0],"groups":[[18,2,0,36],[6,5,43],[48,21,29,23,46],[4,14,16,12,3,8],[26,19,34,20,25,28,39,1,37],[10,15,11,45,49,9,38,42,40,44,47,50]],"partial":false}

Surviving sixth-word mask bank (prefix index:hex bitmask), all classified survivors:
```text
2:80
9:40
10:40
12:c0
13:c0
23:180
33:10000000
36:30060080
37:30000000
38:8000000
63:100200
64:80100
65:300600
66:380700
71:40100200
72:100200
74:100200
75:100200
97:300000
99:300000
100:40000000
101:40406038000000
102:100200
103:80600c0000
104:808060000000
105:400000000000
106:c0100200
107:c0100200
108:20000000
109:300600
110:300600
111:180300
118:c060000000
119:c0804030000000
120:20404030000000
121:1c0e0000000
122:4181c0f0000000
123:20404030000000
124:c0100000
125:180c0100000
126:4060000000
131:1e0000000
132:18180e0000000
133:404020000000
134:e0000000
135:18180e0000000
136:404020000000
137:c0100000
138:60180000
140:180c0000000
141:4020000000
143:180c0000000
144:4020000000
154:3c0780
161:10080000000
178:200000
180:200000
181:1e0100000
183:600000
184:180100000
185:81c00000000000
186:600000000000
187:600c00
188:30301e0180000
189:30301f0180300
190:18180f8000000
191:180780c00
192:1803c0700
193:1c03c0780
204:40000000000000
205:10080000000
206:60808000000000
207:1860c0c060000000
208:180c0000000
209:1c0e0000000
210:181e0f0000000
211:30180600000
212:30180600000
213:181c0300000
220:80000000
221:800000000000
222:180000000
223:1808000000000
224:60c0c060000000
225:20000000000000
226:80000000
227:e0000000
228:18180f0000000
229:180000000
230:180600000
231:1c0300000
238:c00000000000
239:400000000000
240:10080000000
241:1c1c0e0000000
242:c1c1c0e0000000
243:180c0300000
245:10000000000
246:1800000000000
248:30000000000
249:3800000000000
282:100000000
284:300000000
285:2020100000000
287:c00000
288:300000000
290:c00800
291:107020100000000
292:103020100000000
293:2060300c01800
294:2020100000000
301:60300000000
303:60300000000
304:6000000000000
305:106000000000000
308:6060300400000
309:6060300400000
310:60300c00000
311:60300400000
315:300000000
317:300000000
318:60300000000
320:106000000000000
323:6060300000000
324:6060300400000
325:300000000
326:300400000
329:300000000
331:300000000
332:306000000000000
335:60300000000
338:60300000000
339:60300400000
343:306060000000000
344:306020000000000
345:4100000000000000
589:3c0780
596:10080000000
672:80000000000000
673:400000000000
675:1000000000000
676:30301e0100000
677:c04038000000
679:180300000
680:30301e01c0380
725:1010080000000
726:806030000000
728:30180400000
729:c060080000
731:30180600000
732:10080000000
760:1010080000000
761:800020000000
763:180400000
764:60180000
767:180600000
768:80000000
784:81000000000000
785:40c04020000000
787:10000000000
788:8040000000
789:30180000000
790:10080000000
795:81800000000000
796:81000000000000
798:2000000000000
799:181800000000000
800:81000000000000
808:18c000000000000000
998:300000000
999:100000000
```

## Reproduction
Fetch exact three pinned notes. Take first JS block of R247 up to but excluding ' function actual('; replace its single-line const cc/count implementation with first JS block of R276, replace experiment(data) function signature by experiment(data,bank,start,size). Append first JS block of R275 up to but excluding 'let states=', with [1n,17n]] replaced by [1n,17n],[1n,0n]]. Then append the following tail and close the function; pass R247 data literal and R276 first text block (trimmed), start=0,size=150 (ceiling=20000000) or start=150,size=850. The first batch used equivalent tail without partial-prefix serialization (no cutoff). The second tail below serializes a partial mask if necessary. Next starts from summary.next; if nonzero local index, continue from that j only (modify the loop start for that first prefix, do not reclassify earlier visits). Do not repeat any closed prefix. For later work on singleton directions reconstruct six words by decoding this mask bank, preserving each distinct word.

```javascript

const alphabet="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
const pats=dirs.map((_,k)=>patterns(k));
let words=[];for(let line of bank.split("\n")){let [k,v]=line.split(":");let w=[...k].map(c=>alphabet.indexOf(c)),mask=BigInt("0x"+v);for(let j=0;j<pats[4].length;j++)if(mask&(1n<<BigInt(j)))words.push([...w,j])}
if(words.length!==8453||pats[5].length!==79)throw Error("bank dimensions");
function grow(st,rows){let o={pos:st.pos.slice(),neg:st.neg.slice(),seen:new Set(st.seen),lo:st.lo,hi:st.hi};function cut(b,c){if(!b)return c>0n;let q=b>0n?[-c,b]:[c,-b];if(b>0n){if(!o.lo||q[0]*o.lo[1]>o.lo[0]*q[1])o.lo=q}else if(!o.hi||q[0]*o.hi[1]<o.hi[0]*q[1])o.hi=q;return !o.lo||!o.hi||o.lo[0]*o.hi[1]<o.hi[0]*o.lo[1]}function pair(p,m){return cut(p[0]*m[1]-m[0]*p[1],p[0]*m[2]-m[0]*p[2])}
for(let r of rows){let a=norm(r.slice(0,3)),key=a.join();if(o.seen.has(key))continue;o.seen.add(key);if(a[0]>0n){for(let m of o.neg)if(!pair(a,m))return null;o.pos.push(a)}else if(a[0]<0n){for(let p of o.pos)if(!pair(p,a))return null;o.neg.push(a)}else if(!cut(a[1],a[2]))return null}return o}
const empty={pos:[],neg:[],seen:new Set(),lo:null,hi:null};let hist={direct:0,alg:0,recursive:0,surv:0,visits:0,checkedAgainstOld:0},out=[],end=Math.min(start+size,words.length);ceiling=25000000;
let next=[start,0],bits=0n;try{for(let i=start;i<end;i++){let ps=words[i].map((j,k)=>pats[k][j]),a=E[24],b=0n,R=[];for(let k=0;k<5;k++){a|=ps[k].a;b|=ps[k].b;R.push(...ps[k].R);extendCircuit(ps,R,k)}let st=grow(empty,R);if(!st)throw Error("old bank infeasible");bits=0n;for(let j=0;j<pats[5].length;j++){next=[i,j];let p=pats[5][j],x=a|p.a,y=b|p.b;if(count(x)>31||count(y)>31){hist.direct++;hist.visits++;continue}let N=p.R.slice();extendCircuit(ps.concat(p),N,5);let good=!!grow(st,N);if(hist.checkedAgainstOld<100){if(good!==feasible(R.concat(N)))throw Error("incremental mismatch");hist.checkedAgainstOld++}if(!good){hist.alg++;hist.visits++;continue}if(!can(x,5)||!can(y,5)){hist.recursive++;hist.visits++;continue}hist.surv++;hist.visits++;bits|=1n<<BigInt(j)}if(bits)out.push([i,bits.toString(16)]);next=[i+1,0]}}catch(err){if(err!==CUT)throw err;if(bits)out.push([next[0],bits.toString(16)]);return {hist,checks,next,out,partial:true}}return {hist,checks,next,out,groups,partial:false};
}
```

## Next
Finish the remaining 588787 unclassified sixth extensions from [1000,0]; preserve all classified survivors and then join singleton pencils. Explore row-envelope compression only with a proof that future pair constraints are preserved. K6 remains 1–2. Independent mathematical review and Activity association pending.
