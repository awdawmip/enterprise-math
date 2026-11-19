"use strict";
// Deterministic Boolean BRC exact future-word signature verifier for R26.
// Node: node x6_pairwise_link_graph_brc_verify_r26.js
const verify = function verify(){
 const assert=(v,msg)=>{if(!v)throw Error(msg)};
 const allEdges=n=>{let r=[];for(let i=0;i<n;i++)for(let j=i+1;j<n;j++)r.push([i,j]);return r};
 const edgeMask=(s,E)=>E.reduce((a,[i,j],k)=>a+(((s>>i&1)&&(s>>j&1))?2**k:0),0);
 const validW=(w,n,E)=>{for(let i=0;i<n;i++)if(w>>i&1){let found=false;for(let [a,b] of E)if((a===i&&(w>>b&1))||(b===i&&(w>>a&1)))found=true;if(!found)return false}return true};
 const exampleEdges=(n,name)=>name==="empty"?[]:name==="star"?Array.from({length:n-1},(_,i)=>[0,i+1]):name==="path"?Array.from({length:n-1},(_,i)=>[i,i+1]):allEdges(n);
 let pairComparisons=0;
 const test=(n,E)=>{
   const stateMemo=new Map(),intern=new Map();let next=1;
   function sig(h,theta,phase,done,used){
    if(h===0)return 0;
    const key=[h,theta,phase,done,used].join(",");
    if(stateMemo.has(key))return stateMemo.get(key);
    const br=[];
    for(let i=0;i<n;i++){let bit=1<<i,ret=(phase&bit)!==0;let t=sig(h-1,theta,phase^bit,ret?(done|bit):done,used);br.push(`B${i}${ret?"-":"+"}:${t}`)}
    for(let k=0;k<E.length;k++){let [i,j]=E[k],b=(1<<i)|(1<<j);
      if(!(used&(1<<k))&&((done&b)===b)&&((theta&b)===b)){
        br.push(`A${k}:${sig(h-1,theta,phase,done,used|(1<<k))}`)
      }
    }
    const canon=br.join("|");
    if(!intern.has(canon))intern.set(canon,next++);
    const id=intern.get(canon);stateMemo.set(key,id);return id;
   }
   let checked=0;
   const size=1<<n;
   for(let h=0;h<=5;h++){
     const ids=Array.from({length:size},(_,s)=>sig(h,s,0,0,0));
     for(let s=0;s<size;s++)for(let t=s+1;t<size;t++){
       const eqObs=ids[s]===ids[t],eqTheory=h<5||edgeMask(s,E)===edgeMask(t,E);
       assert(eqObs===eqTheory,`language mismatch n=${n} edges=${JSON.stringify(E)} h=${h} s=${s} t=${t}`);
       pairComparisons++;
     }
     checked+=size;
   }
   const byW=new Map(),byEdges=new Map();
   for(let S=0;S<size;S++){
      let em=edgeMask(S,E),W=0;
      E.forEach(([i,j],k)=>{if(em&(1<<k))W|=(1<<i)|(1<<j)});
      byW.set(W,(byW.get(W)||0)+1);
      byEdges.set(em,(byEdges.get(em)||0)+1);
   }
   const classCount=Array.from({length:size},(_,w)=>w).filter(w=>validW(w,n,E)).length;
   assert(classCount===byW.size&&classCount===byEdges.size,"class count");
   for(let [W,count] of byW){
       let allowed=0;
       for(let v=0;v<n;v++){
           if(W>>v&1)continue;
           let adjacent=E.some(([i,j])=>(i===v&&(W>>j&1))||(j===v&&(W>>i&1)));
           if(!adjacent)allowed|=1<<v;
       }
       let independentCount=0;
       for(let I=allowed;;I=(I-1)&allowed){
           if(!E.some(([i,j])=>(I>>i&1)&&(I>>j&1)))independentCount++;
           if(I===0)break;
       }
       assert(independentCount===count,`class size W=${W} count=${count} actual=${independentCount}`);
   }
   return {classCount,checked};
 };
 let graphCount=0,signatures=0;const fiveVertexCases=[],referenceTable=[];
 for(let n=1;n<=4;n++){
   const pool=allEdges(n);
   for(let g=0;g<(1<<pool.length);g++){
     const E=pool.filter((_,k)=>g>>k&1),res=test(n,E);
     graphCount++;signatures+=res.checked;
   }
 }
 for(let name of ["empty","star","path","complete"]){
    const n=5,E=exampleEdges(n,name),res=test(n,E);
    graphCount++;signatures+=res.checked;fiveVertexCases.push({graph:name,edge_count:E.length,classes:res.classCount});
 }
 for(let n=2;n<=7;n++){
   let row={vertices:n};
   for(let name of ["empty","star","path","complete"]){
     const E=exampleEdges(n,name);
     row[name]=new Set(Array.from({length:1<<n},(_,S)=>edgeMask(S,E))).size;
   }
   referenceTable.push(row);
 }
 assert(graphCount===79&&signatures===7356&&pairComparisons===59406,"scope count");
 return {schema:"X6_LINK_PAIR_GUARD_BRC_R26_V1",date:"2026-11-19",model:"conditional six-axis signed-port intact-triad two-cell lanes, pairwise Link guards",scope:"all 75 labeled simple graphs n=1..4 and empty/star/path/complete graphs on n=5; exact deterministic Boolean successful-word language signatures for horizons 0..5; all fiber-size independence-polynomial identities checked",graphs_checked:graphCount,initial_state_horizon_signatures:signatures,pairwise_language_equivalence_comparisons:pairComparisons,comparison_status:"PASS",five_vertex_cases:fiveVertexCases,reference_table:referenceTable,admission:"CONDITIONAL_NOT_NATIVE_EVENT_ADMISSION",review:"NOT_REVIEWED"};
};
const result = verify();
if (typeof module !== "undefined" && require.main === module) console.log(JSON.stringify(result,null,2));
if (typeof module !== "undefined") module.exports=verify;
