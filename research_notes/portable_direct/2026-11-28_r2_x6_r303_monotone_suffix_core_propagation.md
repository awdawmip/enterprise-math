# X6 R303 — hereditary suffix failure and root-core propagation

2026-11-28. Independent informed TASK_RESEARCH, author proof and exact computation, NOT_REVIEWED. R302 exact predecessor 82ea8671084d55cfd1306608ed2440995623a441:research_notes/portable_direct/2026-11-28_r2_x6_r302_full_suffix_first.md, blob a9252f53c14f6bd8c1b15fd33700010be3a150fc. Current native read r2-20261128-1909-x6-observe SUCCEEDED, 2026-11-28T11:09:32.739584Z, Source 35b35ea07ebfb12e57110564d6a79efd92a05e8b, NO_CANONICAL_PUBLICATION_DIRECTORY; native owner projection not evaluated, own identity unconfirmed. No shared state mutation. Global canonical rules read at 5d73bfa6caa9dd6b23abe069f21c0daaef487183, P000 V4/V5 and ACTIVE worldview, joint/residual fidelity. Auxiliary finite BRC observer only, not native dynamics.

## Hereditary optimistic suffix failure

Let G be the frozen 98-germ carrier, c(S) the number of incident support labels, L the complete 2225 split bank, W its subset of necessary-wall splits (R247/R302), and C_d(S) the R302 optimistic recursion. It fails if c(S)>2^d-1, succeeds if c(S)<=d, and otherwise accepts iff some split (U,V) in W when saturated or L otherwise has both C_{d-1}(S∩U), C_{d-1}(S∩V). Zero germs retain the original split semantics. At depth 1 the cardinality cases exhaust all S.

**Lemma:** for X⊆Y, C_d(Y) implies C_d(X). Proof by induction. If C_d(Y) is accepted by base case, c(X)<=c(Y)<=d. If X is in the base case, done. Otherwise c(X)<=c(Y)<=2^d-1; if X is saturated, Y must also be saturated, so the witness split for Y belongs to W; if X is unsaturated, its bank L includes both possible banks for Y. The same split restricts to X, and induction applies to both child intersections. Thus failure of C_d(X) implies failure for every superset at equal depth. This is exact for the inherited optimistic predicate; no converse to actual tree feasibility asserted. Germs remain distinct; support count is only its declared observer.

A failing depth-five branch can now serve as a certificate core for all residual strict root words whose A or B includes it. Greedy deletion shrinks a core only after a completed exact false return; any ceiling preserves the last certified core. A core need not be inclusion-minimal. Remove superseded active cores by subset inclusion; retain their provenance in history. As with R302, no cutoff implies rejection. Reuse R298–R302 exclusion masks exactly and do not count them again. Once the check ceiling is hit, complete a full residual pass for existing core containment only. The firstUnknown tuple is informational; because propagation can remove later words, resume by masks, not by blindly skipping a contiguous interval.

## Frozen inputs
```json
{"s247":"fdbef2ee6e6c32573f3a1ccd171cb5337de520fa","s296":"8e8d8cf7a3a642da52992eedba1f205991d8a874","s298":"13a256b7dc24d83f8e1f56b8f363016928da2d19","s299":"faf4de0953220d3a4122117a3a0c4feacc335674","s300":"95adc01b2f8cd86eec92cbc4e572a466a8c4c73f","s301":"75918d86ade1e8e74f1022ca0c9afc8255e2f0ef","s302":"a9252f53c14f6bd8c1b15fd33700010be3a150fc"}
```

## Actual output
```json
{"stats":{"bank":4327,"linearPartitions":2225,"zeroContainingSplits":47,"direct":645285,"priorR298":219776,"priorR299":237386,"priorR300":54,"priorR301":118573,"residual":63649,"residualPrefixes":1839,"completed":107,"rejected":107,"survived":0,"unprocessed":63542,"checks":5000000,"spotChecks":412,"cacheHits":100104,"fullyRejectedPrefixes":2,"countMiss":277555,"memoEntries":[0,0,712,2162,5532,1193],"priorR302":5847,"directSolves":40,"propagated":67,"coreTests":2289127,"minChecks":4909269,"unknownPrefixes":1837,"coreCount":40,"activeCores":36},"frontier":[166,138,30,1113],"hist":{}}
```

## Reproducer
Load exact blob text into src keyed as above. Run this function; output includes full delta and provenance. Counts compare R302 prior disjointness and baseline.
```javascript
function sweep(src,ceiling=5000000){
 const block=(s,h)=>JSON.parse(s.split(h)[1].match(/\x60\x60\x60json\n([\s\S]*?)\n\x60\x60\x60/)[1]);
 const data=JSON.parse(src.s247.match(/const data=(\[.*\]);/)[1]);
 const bank=[...src.s296.matchAll(/^([0-9]+):([0-9]+):([0-9,]+):([0-9a-f]+):([0-9a-f]+):([0-9]+)$/gm)].map(m=>m.slice(1,7));
 const old=block(src.s298,"## Complete nonempty rejection masks"), newer=block(src.s299,"## Exact new rejection mask delta"), suffix=block(src.s300,"## Full output"), latest=block(src.s301,"## New suffix exclusion masks");
 const dot=(a,b)=>a[0]*b[0]+a[1]*b[1]+a[2]*b[2],cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]],abs=x=>x<0n?-x:x,gcd=(a,b)=>b?gcd(b,a%b):abs(a),nz=a=>a.some(Boolean),sg=x=>x>0n?1:x<0n?-1:0,scale=(a,c)=>a.map(x=>x*c),norm=(a,un=false)=>{let g=a.reduce(gcd,0n);return g?a.map(x=>x/(un&&a.find(Boolean)<0n?-g:g)):a},sub=(a,b)=>a.map((x,i)=>x-b[i]);
 const N=data.map(e=>e.normal.map(BigInt)),parts=data.map(e=>e.normal.join()==="51,2,-1"?[[["1","9","69"],["3","17","187"]],[["2","5","112"],["1","0","51"]]]:e.normal.join()==="17,-1,0"?[[["0","0","1"],["1","17","391"]],[["1","17","69"],["1","17","22"]]]:[e.endpoints]).map(s=>s.map(pair=>pair.map(p=>p.map(BigInt))));
 let P=[],idx=new Map(),G=[],tag=Array(47).fill(0n),gTag=[];
 function id(p){p=norm(p);let k=p.join();if(!idx.has(k)){idx.set(k,P.length);P.push(p)}return idx.get(k)}
 for(let k=0;k<parts.length;k++)for(let [a,b] of parts[k]){if(dot(N[k],a)||dot(N[k],b))throw Error("endpoint");let u=id(a),v=id(b);for(let [i,j] of [[u,v],[v,u]]){let bit=1n<<BigInt(G.length);G.push([i,j,bit]);gTag.push(k);tag[k]|=bit}}
 if(P.length!==51||G.length!==98||P[24].join()!=="0,0,1")throw Error("dimensions");
 const ALL=(1n<<98n)-1n,canon=(a,b)=>a<b?[a,b]:[b,a];
 function signJet(rows,vs){for(let r of rows)for(let v of vs){let z=sg(dot(r,v));if(z)return z}return 0}
 function mask(rows,vs){let a=0n,b=0n;for(let i=0;i<rows.length;i++){let z=signJet(rows[i],vs);if(z>0)a|=G[i][2];else if(z<0)b|=G[i][2]}return canon(a,b)}
 function uniqueRays(xs){let m=new Map();for(let x of xs)if(nz(x)){let v=norm(x,true);m.set(v.join(),v)}return [...m.values()]}
 function partitions(rows){
  const first=rows.map(rs=>rs.find(nz)||[0n,0n,0n]),prim=uniqueRays(first),raw=[];
  if(!prim.some(a=>prim.some(b=>prim.some(c=>dot(cross(a,b),c)))))throw Error("rank");
  for(let i=0;i<prim.length;i++)for(let j=i+1;j<prim.length;j++)raw.push(cross(prim[i],prim[j]));
  const rays=uniqueRays(raw),out=new Map();
  function add(rs,vs){let [a,b]=mask(rs,vs);out.set(a+","+b,[a,b])}
  for(let v of rays)for(let r of prim)if(!dot(v,r)){let w=cross(v,r);for(let e of [-1n,1n])for(let f of [-1n,1n])add(first.map(x=>[x]),[v,scale(w,e),scale(r,f)])}
  for(let r of prim){let cuts=uniqueRays(rows.map(rs=>{let s=rs.find(x=>nz(cross(r,x)));return s?cross(r,s):[0n,0n,0n]}));if(!cuts.length){let v=[[1n,0n,0n],[0n,1n,0n],[0n,0n,1n]].map(x=>cross(r,x)).find(nz);add(rows,[v]);continue}for(let v of cuts){let w=cross(r,v);add(rows,[v]);add(rows,[v,w]);add(rows,[v,scale(w,-1n)])}}
  return [...out.values()]
 }
 const linrows=G.map(([u,v])=>[P[u],sub(P[v],P[u])]),Q=partitions(linrows),S=N.map(n=>mask(linrows,[n])),ordered=[...new Map([...S,...Q].map(([a,b])=>[a+","+b,[a,b]])).values()];
 if(Q.length!==2225||ordered.length!==2225||ordered.some(([a,b])=>a&b))throw Error("partition dimensions "+Q.length+","+ordered.length);
 const pc32=x=>{x=x-((x>>>1)&0x55555555);x=(x&0x33333333)+((x>>>2)&0x33333333);return (((x+(x>>>4))&0x0f0f0f0f)*0x01010101)>>>24};
 const L=[],H=[];
 for(let k=0;k<7;k++){let l=new Uint32Array(16384),h=new Uint32Array(16384);for(let x=1;x<16384;x++){let b=x&-x,j=31-Math.clz32(b),t=gTag[14*k+j],y=x^b;l[x]=l[y]|(t<32?1<<t:0);h[x]=h[y]|(t>=32?1<<(t-32):0)}L.push(l);H.push(h)}
 function label(s){let l=0,h=0;for(let k=0;k<7;k++){let x=Number(s&16383n);l|=L[k][x];h|=H[k][x];s>>=14n}return [l,h]}
 const cc=new Map();let countMiss=0;
 function count(s){let n=cc.get(s);if(n!==undefined)return n;let [l,h]=label(s);n=pc32(l)+pc32(h);countMiss++;if(cc.size<500000)cc.set(s,n);return n}
 const brute=s=>tag.filter(t=>t&s).length;
 const E=P.map((_,i)=>G.filter(g=>g[0]===i).reduce((m,g)=>m|g[2],0n)),singles=[7,13,17,22,27,30,31,32,33,35,41],AX=[],BY=[],X=[],Y=[],bit=Array.from({length:2048},(_,v)=>1n<<BigInt(v));
 for(let v=0;v<2048;v++){let a=0n,b=0n;for(let k=0;k<11;k++)if(v>>k&1)b|=E[singles[k]];else a|=E[singles[k]];AX.push(a);BY.push(b);X.push(label(a));Y.push(label(b))}
 const pop=x=>{let n=0;while(x){x&=x-1n;n++}return n},key=(i,j)=>i+":"+j,hex=x=>BigInt("0x"+x),om=new Map(old.map(z=>[key(z[0],z[1]),hex(z[4])])),nm=new Map(newer.map(z=>[key(z[0],z[1]),hex(z[3])])),lm=new Map(latest.map(z=>[key(z[0],z[1]),hex(z[3])])),fm=new Map();
 for(let z of suffix){if(z.status!=="rejected")throw Error("prior suffix");let k=key(z.i,z.j);fm.set(k,(fm.get(k)||0n)|bit[z.v])}
 const previous=block(src.s302,"## New rejection masks"), pm=new Map(previous.map(z=>[key(z[0],z[1]),hex(z[3])]));
 const cores=[],history=[],coreIds=new Map();let directSolves=0,propagated=0,coreTests=0,minChecks=0,priorR302=0,firstUnknown=null,unknownPrefixes=0,verifiedPropagation=0;
 const memo=Array.from({length:6},()=>new Map()),CUT={},stats={bank:bank.length,linearPartitions:Q.length,zeroContainingSplits:ordered.filter(([a,b])=>(a|b)!==ALL).length,direct:0,priorR298:0,priorR299:0,priorR300:0,priorR301:0,residual:0,residualPrefixes:0,completed:0,rejected:0,survived:0,unprocessed:0,checks:0,spotChecks:0,cacheHits:0,fullyRejectedPrefixes:0};
 function can(s,d){if(!s)return true;let c=count(s);if(c>2**d-1)return false;if(c<=d)return true;if(memo[d].has(s)){stats.cacheHits++;return memo[d].get(s)}let bank=c===2**d-1?S:ordered,cap=2**(d-1)-1;for(let [a,b] of bank){if(stats.checks>=ceiling)throw CUT;stats.checks++;let x=a&s,y=b&s,cx=count(x);if(cx>cap)continue;let cy=count(y);if(cy>cap)continue;if(cx<cy)[x,y]=[y,x];if(can(x,d-1)&&can(y,d-1)){memo[d].set(s,true);return true}}memo[d].set(s,false);return false}
 let stopped=false,frontier=null,delta=[],survivors=[],hist={};
 for(let k=0;k<bank.length;k++){let [is,js,w,ah,bh,ns]=bank[k],i=Number(is),j=Number(js),n=Number(ns),a=hex(ah),b=hex(bh),K=key(i,j),[al,ahh]=label(a),[bl,bhh]=label(b);
 let o=om.get(K)||0n,m=nm.get(K)||0n,f=fm.get(K)||0n,l=lm.get(K)||0n;
 let p=pm.get(K)||0n;if((p&(o|m|f|l))|| (o&m)||(o&f)||(o&l)||(m&f)||(m&l)||(f&l))throw Error("overlap");
 let direct=0n,ct=0;for(let v=0;v<2048;v++)if(pc32(al|X[v][0])+pc32(ahh|X[v][1])<=31&&pc32(bl|Y[v][0])+pc32(bhh|Y[v][1])<=31){direct|=bit[v];ct++}
 if(ct!==n||((o|m|f|l|p)&direct)!==(o|m|f|l|p))throw Error("baseline");
 stats.direct+=ct;stats.priorR298+=pop(o);stats.priorR299+=pop(m);stats.priorR300+=pop(f);stats.priorR301+=pop(l);
 priorR302+=pop(p);let rem=direct&~(o|m|f|l|p),nrem=pop(rem);stats.residual+=nrem;if(!rem)continue;stats.residualPrefixes++;
 
 let reject=0n,keep=0n,done=0,unknown=0;
 for(let rr=rem;rr;rr&=rr-1n){let z=rr&-rr,v=z.toString(2).length-1,A=a|AX[v],B=b|BY[v];if(A&B||(A|B)!==ALL)throw Error("branch");
 if(k%97===0){if(count(A)!==brute(A)||count(B)!==brute(B))throw Error("label count");for(let q=0;q<ordered.length;q+=211){let [u,vv]=ordered[q];for(let s of [A&u,A&vv,B&u,B&vv])if(count(s)!==brute(s))throw Error("conditioned count")}stats.spotChecks++}
 let hit=null;for(let C of cores){coreTests++;if((C&A)===C||(C&B)===C){hit=C;break}}
 if(hit!==null){reject|=z;stats.rejected++;stats.completed++;done++;propagated++;continue}
 if(stopped){unknown++;if(!firstUnknown)firstUnknown=[k,i,j,v];continue}
 try{
 let ca=count(A),cb=count(B),first=ca>=cb?A:B,second=ca>=cb?B:A,failed=null;
 if(!can(first,5))failed=first;else if(!can(second,5))failed=second;
 directSolves++;
 if(failed===null){keep|=z;stats.survived++;let h=ca+","+cb;hist[h]=(hist[h]||0)+1}
 else{
   reject|=z;stats.rejected++;
   let core=failed, minStart=stats.checks;
   // Only successful false tests shrink the core. A cutoff never establishes a rejection.
   if(cores.length<100){
    for(let g=0;g<98;g++){let b=1n<<BigInt(g);if(!(core&b))continue;if(stats.checks-minStart>=120000||stats.checks>=ceiling)break;
     let trial=core^b;try{if(!can(trial,5))core=trial}catch(err){if(err!==CUT)throw err;stopped=true;break}}
   }
   minChecks+=stats.checks-minStart;
   if(!coreIds.has(core)){coreIds.set(core,history.length);history.push({origin:[i,j,v],branch:failed.toString(16),core:core.toString(16),germs:pop(core),labels:count(core)});for(let j=cores.length-1;j>=0;j--)if((cores[j]&core)===core)cores.splice(j,1);cores.push(core)}
 }
 done++;stats.completed++;
 }catch(err){if(err!==CUT)throw err;stopped=true;unknown++;if(!firstUnknown)firstUnknown=[k,i,j,v]}

 }
 stats.unprocessed+=nrem-done;if(unknown)unknownPrefixes++;if(unknown!==nrem-done)throw Error('unknown accounting');if(reject){delta.push([i,j,pop(reject),reject.toString(16)]);if(reject===rem)stats.fullyRejectedPrefixes++}if(keep)survivors.push([i,j,pop(keep),keep.toString(16)])
 }
 if(stats.direct!==645285||stats.priorR298!==219776||stats.priorR299!==237386||stats.priorR300!==54||stats.priorR301!==118573||priorR302!==5847||stats.residual!==63649||stats.residualPrefixes!==1839||stats.completed+stats.unprocessed!==stats.residual||stats.rejected+stats.survived!==stats.completed)throw Error("totals");
 return {stats:{...stats,countMiss,memoEntries:memo.map(m=>m.size),priorR302,directSolves,propagated,coreTests,minChecks,unknownPrefixes,coreCount:history.length,activeCores:cores.length},frontier:firstUnknown,delta,survivors,hist,history}
}

const result=sweep(src);
```

## Core provenance
Each core is an exact germ mask, not a support-label quotient; origin is [i,j,v]. A core's failure is independently reproducible by R302 can(core,5) on the same frozen split bank.
```json
[{"origin":[138,20,1347],"branch":"3cc3000fc57be7cedc7d0c02f","core":"3cc3000fc57be7ced84800000","germs":39,"labels":24},{"origin":[138,20,1351],"branch":"3cc3000fc57be7cedc750c02f","core":"3cc3000fc57be78e984400000","germs":37,"labels":24},{"origin":[138,20,1361],"branch":"3cc3000fc57bc5cedc7d8c02f","core":"3cc3000fc57b4586985980000","germs":36,"labels":26},{"origin":[138,20,1363],"branch":"3cc3000fc57bc5cedc7d0c02f","core":"3cc3000fc57bc58e98480000a","germs":37,"labels":25},{"origin":[138,20,1365],"branch":"3cc3000fc57bc5cedc758c02f","core":"3cc3000fc5794586986580000","germs":35,"labels":26},{"origin":[138,20,1367],"branch":"33cfff03a843a31238af3fd0","core":"33cfff03a843a31238a42000","germs":39,"labels":26},{"origin":[138,20,1379],"branch":"3cc3000fc57b67cedc7d0c02f","core":"3cc3000fc57b67ce584800000","germs":37,"labels":24},{"origin":[138,20,1383],"branch":"3cc3000fc57b67cedc750c02f","core":"3cc3000fc57b678e584400000","germs":36,"labels":24},{"origin":[138,20,1395],"branch":"33cfff03a84ba312382f3fd0","core":"33cfff03a84ba212282a0000","germs":37,"labels":26},{"origin":[138,20,1475],"branch":"3cc3000fc55be7cedc7d0c02f","core":"3cc3000fc55be58e986800000","germs":36,"labels":25},{"origin":[138,20,1479],"branch":"3cc3000fc55be7cedc750c02f","core":"3cc3000fc55be78e582400000","germs":36,"labels":24},{"origin":[138,20,1489],"branch":"3cc3000fc55bc5cedc7d8c02f","core":"3cc3000fc559c586985980000","germs":35,"labels":26},{"origin":[138,20,1491],"branch":"33cfff03aa43a312382f3fd0","core":"33cfa501aa43a212282a0000","germs":32,"labels":26},{"origin":[138,20,1507],"branch":"3cc3000fc55b67cedc7d0c02f","core":"3cc3000fc55b678e586800000","germs":36,"labels":25},{"origin":[138,20,1603],"branch":"1cc3000dc7fbe7cedc7d0c02f","core":"1cc3000dc7fbe686186408000","germs":36,"labels":26},{"origin":[138,20,1611],"branch":"233cfff2b80418392b82f3fd0","core":"233cfff2b80418392a8280000","germs":37,"labels":26},{"origin":[138,20,1617],"branch":"1cc3000dc7fbc5cedc7d8c02f","core":"1cc3000dc7fbc58e984980000","germs":37,"labels":25},{"origin":[138,20,1619],"branch":"1cc3000dc7fbc5cedc7d0c02f","core":"1cc3000dc7fa858e9c6408000","germs":36,"labels":25},{"origin":[138,20,1635],"branch":"1cc3000dc7fb67cedc7d0c02f","core":"1cc3000dc6fa6686186408000","germs":33,"labels":26},{"origin":[138,20,1649],"branch":"1cc3000dc7fb45cedc7d8c02f","core":"1cc3000dc7fb458e984980000","germs":36,"labels":25},{"origin":[138,20,1651],"branch":"233cfff23804ba312382f3fd0","core":"233cfff23804ba30238222000","germs":38,"labels":25},{"origin":[138,20,1731],"branch":"1cc3000dc7dbe7cedc7d0c02f","core":"1cc3000dc6dba686186408000","germs":33,"labels":26},{"origin":[138,20,1745],"branch":"1cc3000dc7dbc5cedc7d8c02f","core":"1cc3000dc7dbc58e984980000","germs":36,"labels":25},{"origin":[138,20,1747],"branch":"233cfff238243a312382f3fd0","core":"233cfff238243a30238222000","germs":38,"labels":25},{"origin":[138,20,1763],"branch":"1cc3000dc7db67cedc7d0c02f","core":"1cc3000dc7da66c6186408000","germs":34,"labels":26},{"origin":[138,20,1859],"branch":"1cc3000dc57be7cedc7d0c02f","core":"1cc3000dc57ba58e946800008","germs":35,"labels":26},{"origin":[138,29,1115],"branch":"3cc3008f47fbc5c6d47f0c02f","core":"3cc3008f47da8586846408000","germs":34,"labels":25},{"origin":[138,29,1139],"branch":"3cc3008fc7fb45cedc7f0c02f","core":"3cc3008ec7ea458a986408000","germs":35,"labels":26},{"origin":[138,29,1147],"branch":"3cc3008f47fb45c6d47f0c02f","core":"3cc3008b47ea4586846408000","germs":33,"labels":25},{"origin":[138,29,1267],"branch":"3cc3008fc7db45cedc7f0c02f","core":"3cc3008fc7d9458a986408000","germs":36,"labels":26},{"origin":[138,29,1367],"branch":"3cc3008fc57bc5cedc770c02f","core":"3cc3008fc57bc5ce9c0400008","germs":38,"labels":24},{"origin":[138,29,1395],"branch":"3cc3008fc57b45cedc7f0c02f","core":"3cc3008fc57b458e984800008","germs":36,"labels":25},{"origin":[138,29,1399],"branch":"3cc3008fc57b45cedc770c02f","core":"3cc3008fc57b45ce9c0400008","germs":37,"labels":24},{"origin":[138,29,1491],"branch":"3cc3008fc55bc5cedc7f0c02f","core":"3cc3008fc55b458a986800008","germs":35,"labels":26},{"origin":[138,29,1495],"branch":"3cc3008fc55bc5cedc770c02f","core":"3cc3008fc55bc54a982400008","germs":35,"labels":25},{"origin":[138,29,1651],"branch":"1cc3008dc7fb45cedc7f0c02f","core":"1c83008947ea458a9c6408000","germs":32,"labels":26},{"origin":[138,29,1747],"branch":"1cc3008dc7dbc5cedc7f0c02f","core":"1cc3008947da858a9c6408000","germs":33,"labels":26},{"origin":[138,29,1779],"branch":"1cc3008dc7db45cedc7f0c02f","core":"1883008945db458a9c6408000","germs":31,"labels":26},{"origin":[138,29,1875],"branch":"1cc3008dc57bc5cedc7f0c02f","core":"18810089c57b858a98680000a","germs":31,"labels":27},{"origin":[138,30,1099],"branch":"3cc3000f47fbe7c6d47f0c02f","core":"3cc3000f47fbe7c6c46408000","germs":40,"labels":25}]
```

## New rejection masks
Each row [i,j,count,hex mask]; disjoint from R298–R302.
```json
[[138,20,32,"8000000000000000000000008000a00880000000000000000000a008800aa0888000000000000000000000008000a00880000000000000000000a008800aa0088000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"],[138,29,27,"8000000000000000000000008000000880000000000000000000000880000008800000000000000000000000800000088000000000000000000000088000000880000000000000000000000880000088800000000000000000000088800008888000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"],[138,30,45,"80000000000000000000000880002008800000000000000000002008800aa008800000000000000000000000800020088000000000000000000220088002a00880000000000000000000000880002008800000000000000000022008800aa888800000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"],[243,20,3,"20000000000000000000000020000000008000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"]]
```

## Surviving optimistic suffix checks
```json
[]
```

## Next
Continue remaining 63542 unknown words using the new masks and certified root cores (can reuse all history, or its subset antichain). Preserve any optimistic survivors separately for exact quadratic feasibility. Mother K6 remains 1–2; general zero/germ cases open. No independent review or Activity association asserted.
