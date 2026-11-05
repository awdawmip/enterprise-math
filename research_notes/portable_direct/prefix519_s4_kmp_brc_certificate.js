"use strict";
// PREFIX-519: S4 orbit transducer over exact signed X6 BRC words.
const assert=(b,msg)=>{if(!b)throw Error(msg)};
const eq=(x,y)=>JSON.stringify(x)===JSON.stringify(y);
const starEdges=[[0,1],[2,3],[0,2],[1,3],[1,2],[0,3]]; // L1..L6
const perms=(xs)=>xs.length?xs.flatMap((x,i)=>perms(xs.filter((_,j)=>i!==j)).map(z=>[x,...z])):[[]];
const group=perms([0,1,2,3]);
const maps=group.map(g=>starEdges.map(([a,b])=>starEdges.findIndex(([c,d])=>[c,d].join()===[g[a],g[b]].sort((x,y)=>x-y).join())));
assert(group.length===24 && maps.every(p=>eq([...p].sort((a,b)=>a-b),[0,1,2,3,4,5])),"S4 edge map");
const id=maps.findIndex(p=>eq(p,[0,1,2,3,4,5]));
const act=(s,p)=>Math.sign(s)*(p[Math.abs(s)-1]+1);
const color=s=>{const i=Math.abs(s);return i===1?(s>0?0:4):i===2?(s>0?1:2):i===3?3:4};
const source=s=>Math.abs(s)===2?"B":Math.abs(s)===3?"C":"N";
const gateWord={aab:[0,0,1],aba:[0,1,0]};
function delta(p,q,c){const str=p.slice(0,q).concat(c);for(let k=3;k>=0;k--){if(eq(str.slice(-k||str.length).slice(k===0?str.length:0),p.slice(0,k)))return k;}throw Error("delta");}
// Separate direct matcher prevents a zero-length suffix corner case.
function step(pattern,q,c){const s=pattern.slice(0,q).concat(c);for(let k=3;k>=1;k--)if(k<=s.length && eq(s.slice(s.length-k),pattern.slice(0,k)))return k;return 0;}
function sig(w,p,pattern){const colors=w.map(x=>color(act(x,p))),sources=w.map(x=>source(act(x,p)));
 const trans=cs=>[0,1,2,3].map(q=>cs.reduce((r,c)=>step(pattern,r,c),q));
 return {T:trans(colors),R:trans(colors.slice().reverse()),f:sources.find(t=>t!=="N")||"N",l:sources.slice().reverse().find(t=>t!=="N")||"N"};}
const compose=(a,b)=>a.map(q=>b[q]);
const choose=(a,b)=>a!=="N"?a:b;
function prod(a,b){return {T:compose(a.T,b.T),R:compose(b.R,a.R),f:choose(a.f,b.f),l:choose(b.l,a.l)};}
const z=()=>Array(6).fill(0);
const add=(a,b)=>a.map((x,i)=>x+b[i]);
const vec=s=>Array.from({length:6},(_,i)=>i===Math.abs(s)-1?Math.sign(s):0);
const disp=w=>w.reduce((a,s)=>add(a,vec(s)),z());
const pairs=w=>{let n=z();for(const s of w)n[Math.abs(s)-1]++;return n.map((v,i)=>(v-Math.abs(disp(w)[i]))/2)};
const wedge=(a,b)=>{let x=[];for(let i=0;i<6;i++)for(let j=i+1;j<6;j++)x.push(a[i]*b[j]-a[j]*b[i]);return x};
const area=w=>{let a=Array(15).fill(0),y=z();for(const s of w){const x=vec(s);a=add(a,wedge(y,x));y=add(y,x);}return a};
const cross=(u,v)=>{const x=disp(u),y=disp(v);return x.map((a,i)=>(Math.abs(a)+Math.abs(y[i])-Math.abs(a+y[i]))/2)};
const orbit=w=>({aab:maps.map(p=>sig(w,p,gateWord.aab)),aba:maps.map(p=>sig(w,p,gateWord.aba))});
function list(max,alphabet){let a=[[]],level=[[]];for(let i=1;i<=max;i++){level=level.flatMap(w=>alphabet.map(s=>w.concat(s)));a.push(...level)}return a}
const alpha=Array.from({length:6},(_,i)=>[i+1,-(i+1)]).flat();
const words=list(3,alpha),small=list(2,alpha);
let compositionChecks=0,reversalChecks=0,covarianceChecks=0,brcChecks=0;
for(const w of words){const ow=orbit(w),rw=w.slice().reverse(),orw=orbit(rw);
 for(const name of Object.keys(gateWord))for(let j=0;j<24;j++){
  const a=ow[name][j],b=orw[name][j];
  assert(eq(a.R,b.T)&&eq(a.T,b.R)&&a.f===b.l&&a.l===b.f,"reversal");reversalChecks++;
 }
 // Signed X6 BRC and oriented area composition for every split.
 for(let split=0;split<=w.length;split++){
  const u=w.slice(0,split),v=w.slice(split),ou=orbit(u),ov=orbit(v);
  for(const name of Object.keys(gateWord))for(let j=0;j<24;j++){
   assert(eq(prod(ou[name][j],ov[name][j]),ow[name][j]),"orbit composition");compositionChecks++;
  }
  assert(eq(pairs(w),add(add(pairs(u),pairs(v)),cross(u,v))),"BRC cross-boundary");
  assert(eq(area(w),add(add(area(u),area(v)),wedge(disp(u),disp(v)))),"signed area");brcChecks++;
 }
}
function cmap(p,q){return p.map(i=>q[i]);} // q after p, matching act(act(s,p),q)
const table=new Map(maps.map((p,j)=>[p.join(),j]));
for(const w of small){const ow=orbit(w);
 for(let h=0;h<24;h++){
  const wh=w.map(s=>act(s,maps[h])),oh=orbit(wh);
  assert(eq(pairs(wh),(()=>{const p=pairs(w),out=z();for(let k=0;k<6;k++)out[maps[h][k]]=p[k];return out})()),"S4 BRC covariance");
  for(let g=0;g<24;g++){
   const gh=table.get(cmap(maps[h],maps[g]).join());assert(gh!==undefined,"group closure");
   for(const name of Object.keys(gateWord)){
    assert(eq(oh[name][g],ow[name][gh]),"S4-KMP covariance");covarianceChecks++;
   }
  }
 }
}
const w1=[4,5,5,4],w2=[5,4,4,5],m=[3,0,2,1],target=group.findIndex(g=>eq(g,m));
const shortest1=[4,-4],shortest2=[-4,4];
assert(target>=0&&maps[target][3]===0&&maps[target][4]===2,"counterexample permutation");
assert(eq(disp(w1),disp(w2))&&eq(pairs(w1),pairs(w2))&&eq(area(w1),area(w2)),"counterexample BRC/area");
assert(eq(disp(shortest1),disp(shortest2))&&eq(pairs(shortest1),pairs(shortest2))&&eq(area(shortest1),area(shortest2)),"length 2 BRC/area collision");
for(const name of Object.keys(gateWord)){
 assert(eq(sig(w1,maps[id],gateWord[name]),sig(w2,maps[id],gateWord[name])),"same original Gamma");
 assert(!eq(sig(w1,maps[target],gateWord[name]).T,sig(w2,maps[target],gateWord[name]).T),"recolored difference");
 assert(sig(w1,maps[target],gateWord[name]).T[0]===1&&sig(w2,maps[target],gateWord[name]).T[0]===0,"distinct q0");
 assert(eq(sig(shortest1,maps[id],gateWord[name]),sig(shortest2,maps[id],gateWord[name])),"length2 original Gamma equality");
 assert(sig(shortest1,maps[target],gateWord[name]).T[0]===0&&sig(shortest2,maps[target],gateWord[name]).T[0]===1,"length2 altered q0");
}
const output={status:"ALL_CHECKS_PASS",arithmetic:"exact signed native X6 BRC and integer KMP maps",model:"S4 atlas axis relabeling; five-axis KMP colors extended by filler on L6",gates:Object.keys(gateWord),automorphisms:24,words_checked_length_0_to_3:words.length,words_checked_length_0_to_2:small.length,composition_checks:compositionChecks,reversal_checks:reversalChecks,covariance_checks:covarianceChecks,brc_area_split_checks:brcChecks,shortest_collision:{w1:"dD",w2:"Dd",length:2,lower_bound_reason:"length zero or one is distinguished by length and signed net displacement",y:disp(shortest1),p:pairs(shortest1),A:area(shortest1),recolored_terminal_q0_w1:0,recolored_terminal_q0_w2:1},collision:{w1:"deed",w2:"edde",n:4,y:disp(w1),p:pairs(w1),A:area(w1),frame_vertex_permutation:m,frame_axis_permutation:maps[target],native_original_GammaA_equal_for_both_gates:true,recolored_terminal_q0_w1:1,recolored_terminal_q0_w2:0},claim_scope:"constructive exact transducer and obstruction in symbolic signed-X6 word model; no physical rotation selection asserted"};
console.log(JSON.stringify(output,null,2));
