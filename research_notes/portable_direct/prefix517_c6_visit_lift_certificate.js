"use strict";
// PREFIX-517: exact integer BRC branch-visit counterexample and observer certificate.
// Run in Node.js: node research_notes/portable_direct/prefix517_c6_visit_lift_certificate.js
const ALPH="aAbBcCdDeE",COLOR=[0,4,1,2,3,3,4,4,4,4],GATES={aab:[0,0,1],aba:[0,1,0]};
const PHASE=[[0,1],[4,-1],[3,1],[0,-1],[4,1],[3,-1]];
const IJ=[];for(let i=0;i<6;i++)for(let j=i+1;j<6;j++)IJ.push([i,j]);
const eq=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
const assert=(b,m)=>{if(!b)throw Error("CERTIFICATE_FAILURE:"+m)};
const letter=([i,s])=>ALPH[2*i+(s<0?1:0)];
const EDGES=PHASE.map((a,r)=>[letter([a[0],-a[1]])+letter(PHASE[(r+1)%6]),letter(PHASE[(r+1)%6])+letter([a[0],-a[1]])]);
const word=bits=>bits.map((b,r)=>EDGES[r%6][b]).join("");
function kstep(g,q,c){const p=GATES[g],t=p.slice(0,q).concat(COLOR[ALPH.indexOf(c)]);
 for(let k=3;k>0;k--)if(t.length>=k&&t.slice(-k).every((v,i)=>v===p[i]))return k;
 return 0;}
function T(g,w){return [0,1,2,3].map(q=>{for(const c of w)q=kstep(g,q,c);return q})}
function sig(g,w){let y=Array(6).fill(0),A=Array(15).fill(0),V=0,W=0,first="N",last="N";
 for(const c of w){let j=ALPH.indexOf(c);assert(j>=0,"letter");let i=j>>1,s=j%2?-1:1;
  IJ.forEach(([a,b],k)=>{A[k]+=y[a]*(b===i?s:0)-y[b]*(a===i?s:0)});
  if(y[i]*s<0){V+=[0,1,0,2,1,0][i];W+=[0,0,1,0,1,0][i]}y[i]+=s;
  if(i===1||i===2){last=i===1?"B":"C";if(first==="N")first=last}}
 return {n:w.length,y,V,W,T:T(g,w),R:T(g,[...w].reverse().join("")),first,last,A};}
function midpoints(bits){let pos=Array(6).fill(0);pos[PHASE[0][0]]=PHASE[0][1];const out=[];
 for(let r=0;r<bits.length;r++){const w=EDGES[r%6][bits[r]];
  let j=ALPH.indexOf(w[0]),i=j>>1,s=j%2?-1:1;pos[i]+=s;out.push(pos.slice());
  j=ALPH.indexOf(w[1]);i=j>>1;s=j%2?-1:1;pos[i]+=s;
  let a=PHASE[(r+1)%6],exp=Array(6).fill(0);exp[a[0]]=a[1];
  assert(eq(pos,exp),"phase endpoint "+r)}
 return out;}
function signatureKey(g,bits){return JSON.stringify(sig(g,word(bits)))}
function supportSet(mid){const o=new Set(mid.map(v=>v.join(",")));return [...o].sort();}
function relativeVisitSet(givenWords){let y=Array(6).fill(0),M=[];for(let k=0;k<givenWords.length;k++){
 const w=givenWords[k];assert(w.length===2,"two-step macroedge");const j=ALPH.indexOf(w[0]),i=j>>1,s=j%2?-1:1;
 y[i]+=s;M.push(y.slice());const t=ALPH.indexOf(w[1]),i2=t>>1,s2=t%2?-1:1;y[i2]+=s2;
 }return {y,M};}
function joinRelative(u,v){const U=relativeVisitSet(u),V=relativeVisitSet(v);return {y:U.y.map((x,i)=>x+V.y[i]),M:U.M.concat(V.M.map(z=>z.map((x,i)=>x+U.y[i])))}}
function hamming(a,b){let n=0;for(let i=0;i<a.length;i++)n+=a[i]!==b[i]?1:0;return n;}
function main(){let result={status:"ALL_CHECKS_PASS",input_pin:"f42f2906d77f24085c123f3ccfe9667d41caa96d",
 model:"chosen anchored STAR S_B={L1,L4,L5}; 6 macroedge C6 loops; two native shortest branches per edge",
 edges:EDGES,checks:{}};
 const a=[1,0,0,0,0,0],b=[0,0,0,1,0,0],mA=midpoints(a),mB=midpoints(b);
 assert(!eq(mA,mB)&&hamming(a,b)===2,"two-flip visit contrast");
 for(const g of Object.keys(GATES)){
  const sigA=sig(g,word(a)),sigB=sig(g,word(b));
  assert(eq(sigA,sigB),"GammaA same for witness "+g);
  assert(sigA.V===6&&sigA.W===2&&sigA.y.every(x=>x===0),"BRC witness");
  assert(eq(sigA.T,[1,1,1,1])&&eq(sigA.R,[0,0,0,0]),"KMP full maps");
  let level={witness:{a_bits:a,b_bits:b,a_word:word(a),b_word:word(b),
    a_midpoints:mA,b_midpoints:mB,
    signature:{n:sigA.n,y:sigA.y,V:sigA.V,W:sigA.W,T:sigA.T,R:sigA.R,first:sigA.first,last:sigA.last,A:sigA.A}},
    enumerations:[]};
  for(const m of [1,2]){const N=6*m,fibers=new Map(),area=new Map();let oneFlipTests=0;
   for(let mask=0;mask<2**N;mask++){
    let bits=Array.from({length:N},(_,r)=>(mask>>r)&1),s=sig(g,word(bits)),k=JSON.stringify(s),ak=JSON.stringify(s.A);
    if(!fibers.has(k))fibers.set(k,[]);fibers.get(k).push(bits);
    area.set(ak,(area.get(ak)||0)+1);
    assert(s.y.every(x=>x===0),"closed native X6 loop");
    for(let r=0;r<N;r++){const x=bits.slice();x[r]^=1;const t=sig(g,word(x));
     assert(!eq(s.A,t.A),"single flip must change area");oneFlipTests++;}
    const mid=midpoints(bits),fixed=mid.map((pos,r)=>{
      const A=PHASE[r%6],B=PHASE[(r+1)%6],outer=Array(6).fill(0);
      outer[A[0]]+=A[1];outer[B[0]]+=B[1];return eq(pos,outer)?1:0;});
    assert(eq(fixed,bits),"history recovered by indexed midpoints");
    const pieces=bits.map((bit,r)=>EDGES[r%6][bit]),split=Math.floor(N/2);
    let direct=relativeVisitSet(pieces),merged=joinRelative(pieces.slice(0,split),pieces.slice(split));
    assert(eq(direct,merged),"midpoint-translation concat");}
   let ambiguous=0,largest=0;
   for(const v of fibers.values()){largest=Math.max(largest,v.length);
    if(v.some(x=>!eq(midpoints(x),midpoints(v[0]))))ambiguous++;}
   assert(area.size===(2*m+1)**3,"area-class exact count");
   assert(fibers.size===(m===1?36:200),"GammaA class count");
   assert(ambiguous===(m===1?20:184),"visit-loss classes");
   level.enumerations.push({m,branch_histories:2**N,area_classes:area.size,
      gamma_A_classes:fibers.size,ambiguous_indexed_visit_fibers:ambiguous,
      max_gamma_A_fiber:largest,single_flip_checks:oneFlipTests,
      exact_history_and_compose_checks:2**N});}
  result.checks[g]=level;
 }
 // Reference pair: the two witness histories differ at macroedges 0 and 3.
 // All six midpoints are native cells relative to the chosen STAR pivot.
 // For a single macroedge, inner midpoint=0; outer midpoint=a_r+a_{r+1}.
 return result;}
if(typeof require!=="undefined"&&require.main===module)console.log(JSON.stringify(main(),null,2));
