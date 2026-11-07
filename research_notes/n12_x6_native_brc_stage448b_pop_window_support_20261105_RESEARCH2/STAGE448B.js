"use strict";
const A=0,B=6;
const fail=(msg)=>{throw Error(msg)};
const add=(map,key,val)=>map.set(key,(map.get(key)||0n)+val);
function valid(n,k){
 const out=[];const rec=(a,b)=>{if(a.length===n){if(b===k&&a[n-1]===0)out.push(a.slice());return;}
 for(const x of [0,1]){if((a.length===0||a.length===n-1)&&x===1)continue;
 if(x===1&&(b===k||a[a.length-1]===1))continue;
 a.push(x);rec(a,b+x);a.pop();}};
 rec([],0);return out;
}
function histories(m,n,kp,kq,d){
 const P=valid(m,kp),Q=valid(n,kq),out=[];
 for(const p of P)for(const q of Q){let h=0;for(let i=0;i<m;i++)h+=(p[i]!==q[i]);if(h===d)out.push({p,q});}
 return out;
}
function key(h,r){const m=h.p.length,n=h.q.length,ell=Math.min(r,n-m);return h.p[m-2]+":"+h.q.slice(m-1,m+ell).join("");}
function outputWordStates(ell){
 let st=new Map([["0,-1,-1",1n]]);
 for(let i=0;i<ell;i++){const nx=new Map();for(const [label,c] of st){
 const [s,f,v]=label.split(",").map(Number);
 for(const x of [0,1]){if(v===1&&x===1)continue;add(nx,[s+x,f===-1?x:f,x].join(","),c);}
 }st=nx;}return st;
}
function dp(m,n,kp,kq,d,r){
 const ell=Math.min(r,n-m),t=n-m-ell,T=new Map();
 let states=new Map([["0,0,0,0,0",1n]]),transitions=0;
 for(let i=1;i<=m;i++){
  const next=new Map();
  for(const [state,count] of states){
   const [a,b,h,u,v]=state.split(",").map(Number);
   for(const x of (i===1||i===m?[0]:[0,1]))for(const y of (i===1?[0]:[0,1])){
    if((x&&u)||(y&&v))continue;
    const aa=a+x,bb=b+y,hh=h+(x!==y);
    if(aa>kp||bb>kq||hh>d)continue;
    transitions++;
    if(i===m){if(aa===kp&&hh===d)add(T,[u,y,bb].join(","),count);}
    else add(next,[aa,bb,hh,x,y].join(","),count);
   }
  }states=next;
 }
 const tailMemo=new Map();
 function tail(length,prev,rem){
  const k=[length,prev,rem].join(",");if(tailMemo.has(k))return tailMemo.get(k);
  if(rem<0)return 0n;
  let result=0n;
  if(length===0)result=rem===0&&prev===0?1n:0n;
  else if(length===1)result=rem===0?1n:0n;
  else {result=tail(length-1,0,rem);if(prev===0)result+=tail(length-1,1,rem-1);}
  tailMemo.set(k,result);return result;
 }
 const words=outputWordStates(ell),pop=new Map();let q=0n,total=0n;
 for(const [meta,wordCount] of words){
 const [s,f,v]=meta.split(",").map(Number);
 for(let bp=0;bp<=1;bp++)for(let qm=0;qm<=1;qm++){
  if(qm===1&&f===1)continue;
  let mass=0n;
  for(let b=0;b<=kq;b++)mass+=(T.get([bp,qm,b].join(","))||0n)*tail(t,v,kq-b-s);
  if(mass>0n){pop.set([bp,qm,s,f,v].join(","),mass);q+=wordCount;total+=wordCount*mass;}
 }
 }
 return {ell,q,total,transitions,pop,words,prefix:T};
}
function direct(m,n,kp,kq,d,r){
 const hist=histories(m,n,kp,kq,d),mass=new Map();
 for(const h of hist)add(mass,key(h,r),1n);
 return {hist,mass};
}
function populationForKey(word,table){
 const [bp,prefix]=word.split(":");const qm=Number(prefix[0]);const window=prefix.slice(1);
 const s=[...window].filter(x=>x==="1").length;
 const f=Number(window[0]),v=Number(window[window.length-1]);
 return table.pop.get([bp,qm,s,f,v].join(","))||0n;
}
function dirPath(binary){return binary.map(x=>x?B:A);}
function fullObserver(p,q){
 const end=a=>{const v=Array(6).fill(0);for(const x of a)v[x%6]+=x<6?1:-1;return v.join(",");};
 const jj=a=>{const m=new Map();for(let i=0;i<a.length-1;i++)add(m,a[i]*12+a[i+1],1n);return Array.from(m.entries()).sort((x,y)=>Number(x[0])-Number(y[0])).map(x=>x[0]+"="+x[1]).join(";");};
 let k=0;for(let i=0;i<Math.min(p.length,q.length);i++)k+=p[i]===q[i]?1:0;
 return [p.length,q.length,end(p),end(q),jj(p),jj(q),k].join("|");
}
function traces(m,r){
 const out=[];
 function rec(a,pops,adds){if(a.length)out.push(a.slice());
  if(adds<r){for(let d=0;d<12;d++){a.push(d);rec(a,pops,adds+1);a.pop();}}
  if(!pops && m+adds>0){a.push(-1);rec(a,1,adds);a.pop();}
 }
 rec([],0,0);out.sort((a,b)=>a.length-b.length||a.join(",").localeCompare(b.join(",")));return out;
}
function futureSignature(h,act){
 const start=dirPath(h.p),q=dirPath(h.q);let all=[];
 for(const tr of act){
  const p=start.slice(),pre=[];
  for(const op of tr){if(op===-1)p.pop();else p.push(op);pre.push(fullObserver(p,q));}
  all.push(pre.join("#"));
 }return all;
}
function main(){
 let families=0,nonempty=0,raw=0,popchecks=0,alltraces=0,futurepairs=0,examples=[],distinguish={};
 for(let m=4;m<=8;m++)for(let n=m+1;n<=Math.min(m+3,10);n++)for(let kp=0;kp<=Math.min(2,Math.floor((m-2)/2));kp++)for(let kq=0;kq<=Math.min(2,Math.floor((n-2)/2));kq++)for(let d=0;d<=Math.min(3,m);d++){
  const r=2;families++;
  const x=direct(m,n,kp,kq,d,r);if(!x.hist.length)continue;nonempty++;raw+=x.hist.length;
  const calc=dp(m,n,kp,kq,d,r);
  if(calc.total!==BigInt(x.hist.length)||calc.q!==BigInt(x.mass.size))fail("total/q mismatch "+JSON.stringify({m,n,kp,kq,d,q:String(calc.q),expected:x.mass.size,total:String(calc.total),raw:x.hist.length}));
  for(const [k,v] of x.mass){popchecks++;if(populationForKey(k,calc)!==v)fail("mass mismatch "+k);}
  if(m<=6&&n<=8&&x.hist.length<=30){
   const actions=traces(m,r),seen=new Map(),groups=new Map();
   for(const h of x.hist){
    const fullKey=key(h,r),sig=futureSignature(h,actions).join("~");
    if(seen.has(sig)&&seen.get(sig)!==fullKey)fail("different key same future signature");
    seen.set(sig,fullKey);
    if(groups.has(fullKey)&&groups.get(fullKey)!==sig)fail("same key different future signature");
    groups.set(fullKey,sig);
   }
   futurepairs+=x.hist.length*(x.hist.length-1)/2;
   alltraces+=actions.length*x.hist.length;
  }
  if(examples.length<5&&x.mass.size>=3)examples.push({m,n,kp,kq,d,r,q:String(calc.q),population:[...x.mass.values()].map(String).sort(),raw:x.hist.length});
  const byOld=new Map();for(const h of x.hist){const old=h.q.slice(m,m+calc.ell).join("");if(!byOld.has(old))byOld.set(old,[]);byOld.get(old).push(h);}
  for(const hh of byOld.values())for(let i=0;i<hh.length;i++)for(let j=i+1;j<hh.length;j++){
   const x=hh[i],y=hh[j],bpDiff=x.p[m-2]!==y.p[m-2],qmDiff=x.q[m-1]!==y.q[m-1];
   if(!bpDiff&&!qmDiff)continue;
   const which=bpDiff&&!qmDiff?"p_suffix":!bpDiff&&qmDiff?"q_boundary":"both";
   if(!distinguish[which]){const actions=traces(m,r);let witness=null;
    for(const tr of actions){const sim=h=>{const p=dirPath(h.p),q=dirPath(h.q),obs=[];for(const z of tr){if(z===-1)p.pop();else p.push(z);obs.push(fullObserver(p,q));}return obs.join("#");};
    if(sim(x)!==sim(y)){witness=tr.map(z=>z===-1?"POP":("APPEND("+z+")"));break;}}
    distinguish[which]={m,n,kp,kq,d,P1:x.p.join(""),Q1:x.q.join(""),P2:y.p.join(""),Q2:y.q.join(""),keys:[key(x,r),key(y,r)],witness};
   }
  }
 }
 const large=dp(64,80,15,17,1,12);
 return {pass:true,tag:"STAGE448B_ONE_POP_WINDOW_DP_PASS",families,nonempty,raw,popchecks,full_future_tree_evaluations:alltraces,full_future_pairs:futurepairs,examples,distinguish,large:{params:[64,80,15,17,1,12],q:String(large.q),total:String(large.total),prefix_states:large.prefix.size,mass_summary_states:large.pop.size,transitions:large.transitions}};
}

const RESULT = main();
if (typeof console !== 'undefined' && console.log) console.log(JSON.stringify(RESULT,null,2));
