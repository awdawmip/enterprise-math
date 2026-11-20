"use strict";
// Stage497-B independent exact directed matrix-tree/BEST recount ranking.
// Pure BigInt; this is not the Stage495 one-linear-solve optimization.
function run(){
const A="ABCDEFGHIJKL";
function empty(){return Array.from({length:12},()=>Array(12).fill(0))}
function copy(M){return M.map(row=>row.slice())}
function inventory(w){let M=empty();for(let i=1;i<w.length;i++)M[A.indexOf(w[i-1])][A.indexOf(w[i])]++;return M}
function fact(n){let p=1n;for(let k=2;k<=n;k++)p*=BigInt(k);return p}
function det(X){
 let n=X.length;if(!n)return 1n;
 let B=X.map(row=>row.slice()),den=1n,sign=1n;
 for(let j=0;j<n-1;j++){
  if(B[j][j]===0n){let r=j+1;while(r<n&&B[r][j]===0n)r++;if(r===n)return 0n;[B[j],B[r]]=[B[r],B[j]];sign=-sign;}
  let p=B[j][j];
  for(let a=j+1;a<n;a++){
   for(let b=j+1;b<n;b++){
    let num=B[a][b]*p-B[a][j]*B[j][b];
    if(num%den!==0n)throw Error("nonintegral Bareiss");
    B[a][b]=num/den;
   }
   B[a][j]=0n;
  }
  den=p;
 }
 return sign*B[n-1][n-1];
}
function count(M,s,t){
 let n=M.flat().reduce((a,b)=>a+b,0);
 if(!n)return s===t?1n:0n;
 let o=M.map(row=>row.reduce((a,b)=>a+b,0)),ind=Array(12).fill(0);
 for(let u=0;u<12;u++)for(let v=0;v<12;v++)ind[v]+=M[u][v];
 let vertices=[];for(let v=0;v<12;v++)if(o[v]+ind[v])vertices.push(v);
 if(!vertices.includes(s)||!vertices.includes(t))return 0n;
 for(let v of vertices)if(o[v]-ind[v]!==Number(v===s)-Number(v===t) || (v!==t && o[v]===0))return 0n;
 let R=vertices.filter(v=>v!==t);
 let L=R.map(u=>R.map(v=>BigInt(u===v?o[u]-M[u][u]:-M[u][v])));
 let tau=det(L);if(tau===0n)return 0n;if(tau<0n)throw Error("negative arborescence");
 let numerator=tau*fact(o[t]),denominator=1n;
 for(let v of R)numerator*=fact(o[v]-1);
 for(let row of M)for(let k of row)denominator*=fact(k);
 if(numerator%denominator)throw Error("nonintegral count");
 return numerator/denominator;
}
function options(M,s,t){
 let out=[];
 for(let v=0;v<12;v++)if(M[s][v]>0){M[s][v]--;let n=count(M,v,t);M[s][v]++;out.push([v,n]);}
 return out;
}
function unrank(M0,s,t,r){
 let M=copy(M0),w=A[s],drops=0;
 let edges=M.flat().reduce((a,b)=>a+b,0);
 for(let step=0;step<edges;step++){
  let found=false;
  for(let [v,n] of options(M,s,t)){
   if(r>=n){r-=n;continue}
   let support0=M.reduce((a,row,i)=>a+(row.some(z=>z)||M.some(r=>r[i])) ,0);
   M[s][v]--;let support1=M.reduce((a,row,i)=>a+(row.some(z=>z)||M.some(r=>r[i])),0);
   if(support1<support0)drops++;
   w+=A[v];s=v;found=true;break;
  }
  if(!found)throw Error("no successor");
 }
 if(s!==t||r!==0n)throw Error("nonterminal");
 return {word:w,support_drop_levels:drops};
}
function rank(M0,s,t,w){
 let M=copy(M0),result=0n;
 for(let c of w.slice(1)){
  let v=A.indexOf(c),found=false;
  for(let [b,n] of options(M,s,t)){if(b===v){found=true;break;}result+=n;}
  if(!found)throw Error("rank word not Euler");
  M[s][v]--;s=v;
 }
 if(s!==t || M.flat().some(x=>x))throw Error("wrong inventory");
 return result;
}
let groups=new Map(),strings=0;
for(let n=1;n<=5;n++)for(let k=0;k<3**n;k++){
 let j=k,w="";for(let i=0;i<n;i++){w="ABC"[j%3]+w;j=Math.floor(j/3)}
 let s=A.indexOf(w[0]),t=A.indexOf(w[w.length-1]),M=inventory(w);
 let key=s+"|"+t+"|"+JSON.stringify(M);
 let old=groups.get(key);
 if(!old)groups.set(key,{M,s,t,n:1});else old.n++;
 strings++;
}
for(let {M,s,t,n} of groups.values())if(count(M,s,t)!==BigInt(n))throw Error("small exhaustive mismatch");
let samples=[];
for(let [name,word] of [["sparse_cycle","ABCABCABC"],["support_drop","ABACADAEA"]]){
 let M=inventory(word),s=A.indexOf(word[0]),t=A.indexOf(word[word.length-1]),N=count(M,s,t),r=N/2n;
 let a=unrank(M,s,t,r);if(rank(M,s,t,a.word)!==r)throw Error("small rank");
 samples.push({case:name,edges:word.length-1,N:N.toString(),bits:N.toString(2).length,
   selected_rank:r.toString(),word:a.word,support_drop_levels:a.support_drop_levels});
}
let base=empty();for(let a=0;a<12;a++)for(let b=0;b<12;b++)base[a][b]=1;
let skew=copy(base);skew[0][0]+=70;skew[1][1]+=23;skew[2][3]+=17;skew[3][2]+=17;
for(let [name,M] of [["complete_144",base],["skew_271",skew]]){
 let t0=Date.now(),N=count(M,0,0),countMs=Date.now()-t0,r=N/2n;
 t0=Date.now();let a=unrank(M,0,0,r),unrankMs=Date.now()-t0;
 t0=Date.now();let back=rank(M,0,0,a.word),rankMs=Date.now()-t0;
 if(back!==r)throw Error("large rank");
 let rec=inventory(a.word);
 if(JSON.stringify(rec)!==JSON.stringify(M))throw Error("inventory mismatch");
 samples.push({case:name,edges:M.flat().reduce((x,y)=>x+y,0),N:N.toString(),
 bits:N.toString(2).length,selected_rank:r.toString(),word:a.word,
 word_bytes:a.word.length,support_drop_levels:a.support_drop_levels,
 count_ms:countMs,unrank_ms:unrankMs,rank_ms:rankMs});
}
return {small_independent_full_exhaustion:{strings,inventory_endpoint_cases:groups.size},
 arithmetic:"exact_JavaScript_BigInt",reference_not_optimized:true,cases:samples};
}
if(typeof module!=='undefined'&&require.main===module)console.log(JSON.stringify(run(),null,2));
