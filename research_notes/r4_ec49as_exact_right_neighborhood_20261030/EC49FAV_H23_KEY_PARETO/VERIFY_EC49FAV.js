#!/usr/bin/env node
// Exact EC49FAV native signed-X6 two-horizon key/edge proof; frozen pin fc0f038e7bfd12c886b4d37f900bfb770c0f61ab
function run(){
 const OP={a:[-1,-1],b:[-2,-2],c:[1,2,-1,-2],d:[2,1,-2,-1],e:[3,1,1,-3],f:[1,-1],g:[2,-2]};
 const START=[["N",0],["N",1],["N",2],["A",0],["A",2],["B",0],["B",1],["AB",0],["BA",0]];
 const SNAMES=["de","ed","ce","ec","feg","gef"],BUCKET=["N","A","B","AB","BA"];
 const steps=w=>[...w].flatMap(c=>OP[c]);
 function endpoint(w){let v=[0,0,0,0,0,0];for(const s of steps(w))v[Math.abs(s)-1]+=s>0?1:-1;return v.join(",");}
 function key(w){let v=[0,0,0,0,0,0];for(const s of steps(w))if(s>0)v[s-1]++;return v.join(",");}
 function observer(w){let out=[];for(let [state0,prev0] of START){let state=state0,prev=prev0;
   for(const s of steps(w)){if(prev===1&&s===2){if(state==="N")state="A";else if(state==="B")state="BA";}
     else if(prev===2&&s===1){if(state==="N")state="B";else if(state==="A")state="AB";}prev=s;}
   out.push(BUCKET.indexOf(state));}return out.join(",");}
 const SIG=new Map(SNAMES.map((w,i)=>[observer(w),1<<i]));
 if(SIG.size!==6)throw Error("signature collision");
 const mask=w=>SIG.get(observer(w))||0,rank9=m=>Boolean((m&(2|16))&&(m&(4|16))&&(m&(1|32))&&(m&(8|32)));
 function pref(ws){let s=new Set();for(const w of ws){let p="";for(const v of steps(w)){p+=v+",";s.add(p);}}return s;}
 const WS={2:[],3:[]};
 for(const h of [2,3]){function recur(w){if(w.length===h){if(endpoint(w)==="2,0,0,0,0,0"&&mask(w))WS[h].push(w);return;}
  for(const c of "acdefg")recur(w+c);}recur("");}
 if(WS[2].length!==6||WS[3].length!==38)throw Error("candidate census");
 const KEYS=[...new Set([...WS[2],...WS[3]].map(key))].sort(),KI=new Map(KEYS.map((k,i)=>[k,i]));
 if(KEYS.length!==8)throw Error("key census");
 function trie(words,free){let root={ch:new Map(),w:null,m:0,k:0,free:true};for(const w of words){let n=root,p="";
  for(const s of steps(w)){p+=s+",";if(!n.ch.has(s))n.ch.set(s,{ch:new Map(),w:null,m:0,k:0,free:free.has(p)});n=n.ch.get(s);}
  if(n.w!==null)throw Error("nonunique native steps");n.w=w;n.m=mask(w);n.k=1<<KI.get(key(w));}return root;}
 function bits(v){let n=0;while(v){n+=(v&1);v>>>=1;}return n;}
 function dp(n){let d=new Map([["0,0",{c:0,ws:[]}]]);
  if(n.w!==null)d.set(n.m+","+n.k,{c:0,ws:[n.w]});
  for(const child of n.ch.values()){let nd=new Map(),x=dp(child);
   for(const [sa,a] of d){let [m,k]=sa.split(",").map(Number);
    for(const [sb,b] of x){let [mm,kk]=sb.split(",").map(Number),kb=k|kk;if(bits(kb)>5)continue;
     let state=(m|mm)+","+kb,c=a.c+b.c,old=nd.get(state);
     if(!old||c<old.c)nd.set(state,{c,ws:a.ws.concat(b.ws)});}}
   d=nd;}
  if(!n.free)for(const [state,a] of d)if(+state.split(",")[0])a.c++;
  return d;}
 let best={1:null,2:null,3:null,4:null,5:null},nH2=0;
 for(let subset=1;subset<(1<<WS[2].length);subset++){
  const w2=WS[2].filter((w,i)=>subset&(1<<i)),m2=w2.reduce((m,w)=>m|mask(w),0);
  if(!rank9(m2))continue;nH2++;
  let free=pref(w2),k2=new Set(w2.map(key)),d=dp(trie(WS[3],free));
  for(const [state,a] of d){let [m,k]=state.split(",").map(Number);if(!rank9(m))continue;
   const allK=new Set([...k2,...KEYS.filter((_,i)=>k&(1<<i))]),nk=allK.size,E=free.size+a.c;
   for(let cap=nk;cap<=5;cap++)if(!best[cap]||E<best[cap].edges)best[cap]={edges:E,H2:w2,H3:a.ws,keys:[...allK].sort().map(s=>s.split(",").map(Number)),keys_used:nk,early_edges:free.size,added_H3:a.c};}}
 if(nH2!==25||[1,2,3,4,5].map(k=>best[k].edges).join(",")!=="42,31,16,16,16")throw Error("Pareto check");
 for(let k=1;k<=5;k++){const z=best[k];if(pref([...z.H2,...z.H3]).size!==z.edges)throw Error("witness bad");}
 const W={2:["fe","ge"],3:["feg","gef"],4:["fegc","fegd","gefc","gefd"],
  5:["feggf","gefgf"],6:["fegccc","fegddd","gefccc","gefddd"],
  7:["fegccfg","fegddgf","gefccfg","gefddgf"],
  8:["feggfgfc","feggfgfd","gefgfgfc","gefgfgfd"],9:["feggfgfgf","gefgfgfgf"]};
 let all=[],byH={},allSig=new Set();
 for(let h=2;h<=9;h++){let M=0,K=new Set();for(const w of W[h]){if(w.length!==h||endpoint(w)!=="2,0,0,0,0,0"||!mask(w))throw Error("wrong full witness word");M|=mask(w);K.add(key(w));allSig.add(mask(w));}
  if(!rank9(M))throw Error("wrong horizon rank "+h);all.push(...W[h]);byH[h]={words:W[h],keys:[...K].sort().map(s=>s.split(",").map(Number)),signature_mask:M,total_prefix_edges:pref(all).size};}
 const allKeys=[...new Set(all.map(key))].sort().map(s=>s.split(",").map(Number));
 if(allKeys.length!==5||allSig.size!==6||pref(all).size!==112)throw Error("full witness resources");
 return {status:"PASS_AUTHOR_SIDE_EXACT_INTEGER",study:"EC49FAV",date:"2026-11-05",frozen_science_pin:"fc0f038e7bfd12c886b4d37f900bfb770c0f61ab",H2_legal_words:6,H3_legal_words:38,H2_rank9_subsets:nH2,key_classes:KEYS.length,at_most_key_optima:best,whole_H2_H9_witness:{edge_count:112,keys:allKeys,signature_count:6,by_horizon:byH},rank_criterion:"(E or F) and (C or F) and (D or G) and (J or G)",method:"Exhaustive H2/H3 complete seven-operation native-X6 words, exact 2-window native primitive-prefix OR-mask DP with full six-coordinate key masks, plus independent full-horizon literal witness audit"};
}
console.log(JSON.stringify(run(),null,2));
