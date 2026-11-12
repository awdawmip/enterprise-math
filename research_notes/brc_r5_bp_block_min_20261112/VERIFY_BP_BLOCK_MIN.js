#!/usr/bin/env node
'use strict';
/* Standalone rooted-tree BP block-minimum navigation verifier. Node.js 18+. */
const verify = function verify(){
 const counts={exhaustiveRootedTrees:0,exhaustiveNodeQueries:0,largeNodeQueries:0,selectTests:0,rangeMinTests:0,largeCases:[]};
 const assert=(c,m)=>{if(!c)throw Error(m)};
 const cache=new Map();
 function forests(n){
  if(cache.has(n))return cache.get(n);
  if(n===0)return [""];
  const a=[];
  for(let k=0;k<n;k++)for(const x of forests(k))for(const y of forests(n-1-k))a.push("("+x+")"+y);
  cache.set(n,a);return a;
 }
 function build(bp,B){
  const m=bp.length,N=m/2;
  assert(m%2===0,"odd BP");
  let opens=0,depth=0;
  const ranks=[],mins=[],deltas=[],blocks=Math.ceil(m/B);
  for(let j=0;j<blocks;j++){
   const begin=j*B,end=Math.min(begin+B,m);
   ranks.push(opens);
   let local=0,mn=0;
   for(let p=begin;p<end;p++){
    if(bp[p]==="("){opens++;local++;}else{local--;}
    if(local<mn)mn=local;
    depth+=bp[p]==="("?1:-1;
    assert(depth>=0,"unbalanced prefix");
   }
   mins.push(-mn);deltas.push(local);
  }
  assert(depth===0&&opens===N,"not balanced");
  const rankAt=j=>j<blocks?ranks[j]:N;
  function rank(pos){
   assert(pos>=0&&pos<=m,"rank position out of range");
   if(pos===m)return N;
   const j=Math.floor(pos/B);
   let v=ranks[j];
   for(let q=j*B;q<pos;q++)if(bp[q]==="(")v++;
   return v;
  }
  function select(i){
   assert(i>=0&&i<N,"select index out of range");
   let l=0,h=blocks;
   while(l+1<h){const t=Math.floor((l+h)/2);if(ranks[t]<=i)l=t;else h=t;}
   let v=ranks[l];
   for(let p=l*B;p<Math.min(m,(l+1)*B);p++)if(bp[p]==="("){if(v===i)return p;v++;}
   throw Error("select1 missing "+i);
  }
  function match(p){
   assert(bp[p]==="(","not opening");
   const target=2*rank(p)-p;
   let ex=target+1,q=p+1;
   const end0=Math.min(m,(Math.floor(p/B)+1)*B);
   for(;q<end0;q++){ex+=bp[q]==="("?1:-1;if(ex===target)return q;}
   for(let j=Math.floor(end0/B);j<blocks;j++){
    assert(q===j*B,"block alignment");
    if(ex-mins[j]>target){
     const d=2*(rankAt(j+1)-rankAt(j))-(Math.min(m,(j+1)*B)-j*B);
     assert(d===deltas[j],"rank delta");
     ex+=d;q=Math.min(m,(j+1)*B);
    }else{
     const end=Math.min(m,(j+1)*B);
     for(;q<end;q++){ex+=bp[q]==="("?1:-1;if(ex===target)return q;}
    }
   }
   throw Error("unclosed opening "+p);
  }
  const size=i=>(match(select(i))-select(i)+1)/2;
  const childIndices=i=>{
   const p=select(i),end=match(p);
   let c=p+1,ans=[];
   while(c<end){
    assert(bp[c]==="(","child not open");
    ans.push(rank(c));c=match(c)+1;
   }
   assert(c===end,"child extent mismatch");return ans;
  };
  return{N,B,m,ranks,mins,size,rank,select,match,childIndices};
 }
 function check(bp,B){
  const idx=build(bp,B),n=idx.N;
  const opens=[],expected=[],children=Array.from({length:n},()=>[]);
  const stack=[];
  for(let p=0;p<bp.length;p++){
   if(bp[p]==="("){
    const i=opens.length;opens.push(p);
    if(stack.length)children[stack[stack.length-1].i].push(i);
    stack.push({p,i});
   }else{
    assert(stack.length>0,"bad closing");
    const z=stack.pop();
    expected[z.i]=(p-z.p+1)/2;
   }
  }
  assert(stack.length===0,"open stack");
  for(let i=0;i<n;i++){
   assert(idx.select(i)===opens[i],"select mismatch "+i);
   assert(idx.rank(opens[i])===i,"rank mismatch "+i);
   assert(idx.size(i)===expected[i],"subtree mismatch "+i);
   const c=idx.childIndices(i);
   assert(JSON.stringify(c)===JSON.stringify(children[i]),"child mismatch "+i);
   counts.selectTests++;counts.rangeMinTests++;
  }
  return idx;
 }
 for(let n=1;n<=9;n++)for(const f of forests(n-1)){
  check("("+f+")",16);
  counts.exhaustiveRootedTrees++;
  counts.exhaustiveNodeQueries+=n;
 }
 function rooted(n,arity,seed){
  const ch=Array.from({length:n},()=>[]);
  let x=seed>>>0;
  for(let i=1;i<n;i++){
   x=(Math.imul(x,1664525)+1013904223)>>>0;
   const p=arity>0?Math.floor((i-1)/arity):(x%i);
   ch[p].push(i);
  }
  let out="";
  function visit(i){out+="(";for(const c of ch[i])visit(c);out+=")";}
  visit(0);return out;
 }
 const N=2880;
 const big=[
  ["star","("+ "()".repeat(N-1)+")"],
  ["chain","(".repeat(N)+")".repeat(N)],
  ["ternary",rooted(N,3,17)],
  ["random-seeded",rooted(N,0,19092026)]
 ];
 for(const [label,bp] of big){
  const idx=check(bp,64);counts.largeNodeQueries+=N;
  const bins=[0,0,0,0];
  for(let i=0;i<N;i++){const v=idx.size(i);bins[v<=3?0:v<=15?1:v<=255?2:3]++;}
  counts.largeCases.push({label,nodes:N,widthBins:bins});
 }
 const suffixBits=28987,oldHuffmanBits=41087;
 const sizes=[];
 for(const B of [16,32,64,128,256,512]){
  const J=Math.ceil(2*N/B),widthR=Math.ceil(Math.log2(N+1)),widthMin=Math.ceil(Math.log2(B+1));
  const indexBits=J*(widthR+widthMin);
  const bits=2*N+indexBits+suffixBits;
  sizes.push({B,blocks:J,rankBits:widthR,minBits:widthMin,indexBits,totalBits:bits,bytes:Math.ceil(bits/8),savedBytes:Math.ceil(oldHuffmanBits/8)-Math.ceil(bits/8)});
 }
 assert(sizes[2].totalBits===36457,"B=64 budget");
 assert(sizes[2].bytes===4558,"B=64 bytes");
 assert(counts.exhaustiveRootedTrees===2056,"Catalan exhaustiveness");
 return{status:"PASS_BP_BLOCK_MIN_EXACT_NAVIGATION",...counts,sizeBudget:sizes};
};
console.log(JSON.stringify(verify(),null,2));
