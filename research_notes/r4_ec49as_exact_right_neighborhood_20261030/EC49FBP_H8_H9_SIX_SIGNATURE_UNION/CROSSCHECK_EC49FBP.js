'use strict';
// Independent exact DP crosscheck: integer native-prefix trie, 64 states (no Python imports).
const OP='acdefg', DELTA=[[-1,-1],[1,2,-1,-2],[2,1,-2,-1],[3,1,1,-3],[1,-1],[2,-2]];
const TRANS=[[1,2,3,1,4,5],[1,6,7,1,1,1],[2,2,8,2,2,2],[3,8,3,3,3,3],[4,2,7,4,4,4],[5,6,3,5,5,5],[6,6,8,6,6,6],[7,8,7,7,7,7],[8,8,8,8,8,8]];
const OBS=[0,0,4,1,16,32,8,2,0],colors={1:0,2:1,4:2,8:3,16:4,32:5};
function evaluate(x,y,z){
 let nodes=[{ch:new Map(), sig:0}], counts=Array(6).fill(0), accepted=Array(6).fill(0);
 const insert=(ops,signature)=>{
   let u=0;
   for(const op of ops) for(const axis of DELTA[op]){
      let v=nodes[u].ch.get(axis);
      if(v===undefined){v=nodes.length;nodes[u].ch.set(axis,v);nodes.push({ch:new Map(),sig:0})}
      u=v;
   }
   nodes[u].sig|=1<<colors[signature];
   accepted[colors[signature]]++;
 };
 function words(state,left,seq,wanted){
   if(left===0){const sig=OBS[state];if(wanted.has(sig))insert(seq,sig);return}
   for(let i=0;i<6;i++)if(counts[i]>0){let nxt=TRANS[state][i];if(nxt===8)continue;counts[i]--;seq.push(i);words(nxt,left-1,seq,wanted);seq.pop();counts[i]++}
 }
 const apply=(h,cd,wanted)=>{
   counts=[z-1,cd==='c'?1:0,cd==='d'?1:0,z,h+1-y-2*z,h+1-x];
   words(0,h,[],wanted);
 };
 for(const c of ['c','d'])apply(8,c,new Set([1,2,4,8]));
 apply(9,'',new Set([16,32]));
 const missing=accepted.some(v=>v===0);if(missing)throw Error('missing'+[x,y,z]);
 const D=new Array(nodes.length);const INF=9999;
 for(let i=nodes.length-1;i>=0;i--){
   let dp=new Int16Array(64).fill(INF);dp[0]=0;
   if(nodes[i].sig)dp[nodes[i].sig]=0;
   for(const child of nodes[i].ch.values()){
     const cdp=D[child], next=new Int16Array(dp);
     for(let m=0;m<64;m++){
       const a=dp[m];if(a===INF)continue;
       for(let n=1;n<64;n++){
         const b=cdp[n];if(b===INF)continue;
         const join=m|n,val=a+b+1;
         if(val<next[join])next[join]=val;
       }
     }
     dp=next;
     D[child]=null;
   }
   D[i]=dp;
 }
 return {key:[x,y,z], optimum:D[0][63], accepted, nodes:nodes.length};
}
const all=[];for(let z=1;z<=4;z++)for(let x=2*z+1;x<=9;x++)all.push(evaluate(x,10-x,z));
process.stdout.write(JSON.stringify(all,null,2)+'\n');
