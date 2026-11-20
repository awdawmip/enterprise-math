'use strict';
// Stage434-B: exact native-X6 one-defect fiber, future quotient, and indexed reader.
const DIR=[];for(let k=1;k<=6;k++){DIR.push('+'+k,'-'+k)}
const A='+1',B='-1',C='+2';
function check(x,s){if(!x)throw Error(s)}
function defect(m,b){return Array.from({length:m},(_,i)=>i+1===b?B:A)}
function endpoint(w){const x=[0,0,0,0,0,0];for(const d of w)x[Number(d.slice(1))-1]+=d[0]==='+'?1:-1;return x}
function adj(w){const j={};for(let i=1;i<w.length;i++){const k=w[i-1]+'>'+w[i];j[k]=(j[k]||0)+1;}return Object.fromEntries(Object.entries(j).sort())}
function eq(a,b){return JSON.stringify(a)===JSON.stringify(b)}
function obs(P,Q){return {m:P.length,n:Q.length,xP:endpoint(P),xQ:endpoint(Q),JP:adj(P),JQ:adj(Q),K:Q.reduce((s,d,i)=>s+(i<P.length&&d===P[i]?1:0),0)}}
function trace(P,Q,ops){const out=[obs(P,Q)];let q=Q.slice();for(const o of ops){if(o==='POP'){check(q.length>0,'invalid pop');q.pop()}else q.push(o);out.push(obs(P,q))}return out}
function words(n,p,r){const out=[[]];function walk(q,pc,rc,w){if(pc<p&&q>0){const nxt=w.concat('POP');out.push(nxt);walk(q-1,pc+1,rc,nxt)}if(rc<r){for(const d of DIR){const nxt=w.concat(d);out.push(nxt);walk(q+1,pc,rc+1,nxt)}}}walk(n,0,0,[]);return out}
function key(b,n,p,r){const a=n-p+1,z=n+r;return b>=a&&b<=z?b-a+1:0}
function reconstruct(m,n,p,r,k){const a=n-p+1;const b=k===0?n+r+1:a+k-1;return defect(m,b)}
function witness(n,j){if(j<=n){return Array.from({length:n-j+1},()=> 'POP').concat([B])};return Array.from({length:j-n-1},()=>C).concat([B])}
// Independent quotient reader updates Q endpoint, J and exact K from only class ID.
function readerTrace(m,n,p,r,k,ops){
 const a=n-p+1,z=n+r,b=k===0?-1:a+k-1;
 const P=defect(m,2),xp=endpoint(P),jp=adj(P);
 const q=Array(n).fill(C),xq=endpoint(q),jq=adj(q);
 const match=(j,d)=>j<a||j>z?0:(d===(j===b?B:A)?1:0);
 let K=0;
 const snap=()=>({m,n:q.length,xP:xp.slice(),xQ:xq.slice(),JP:{...jp},JQ:Object.fromEntries(Object.entries(jq).sort()),K});
 const out=[snap()];
 for(const op of ops){
  if(op==='POP'){
   check(q.length>0,'reader illegal POP');const j=q.length,d=q.pop();K-=match(j,d);
   xq[Number(d.slice(1))-1]-=d[0]==='+'?1:-1;
   if(q.length){const edge=q[q.length-1]+'>'+d;jq[edge]--;if(!jq[edge])delete jq[edge]}
  }else{
   const j=q.length+1,d=op;if(q.length){const edge=q[q.length-1]+'>'+d;jq[edge]=(jq[edge]||0)+1}
   q.push(d);xq[Number(d.slice(1))-1]+=d[0]==='+'?1:-1;K+=match(j,d);
  }
  out.push(snap());
 }
 return out;
}
function runCase(m,n,p,r){check(n>=2&&p>=0&&p<=n-1&&r>=1&&m>=n+r+2,'theorem domain');
 const N=m-2,a=n-p+1,z=n+r,ws=words(n,p,r),Q=Array(n).fill(C);
 const ps=Array.from({length:N},(_,i)=>defect(m,i+2)),base=obs(ps[0],Q);
 for(const P of ps)check(eq(obs(P,Q),base),'initial observer fiber');
 const sig=ps.map(P=>JSON.stringify(ws.map(w=>trace(P,Q,w))));
 let pairTests=0;for(let i=0;i<N;i++)for(let j=i+1;j<N;j++){pairTests++;check((sig[i]===sig[j])===(key(i+2,n,p,r)===key(j+2,n,p,r)),'future equivalence mismatch')}
 const masses=Array(p+r+1).fill(0);for(let b=2;b<m;b++)masses[key(b,n,p,r)]++;
 check(masses[0]===m-2-p-r&&masses.slice(1).every(x=>x===1),'class masses');
 for(let k=0;k<=p+r;k++){const rep=reconstruct(m,n,p,r,k);check(key(rep.indexOf(B)+1,n,p,r)===k,'reader representative')}
 let readerTraceChecks=0;for(let k=0;k<=p+r;k++){const rep=reconstruct(m,n,p,r,k);for(const w of ws){check(eq(readerTrace(m,n,p,r,k,w),trace(rep,Q,w)),'incremental reader disagreement');readerTraceChecks++}}
 let witnessChecks=0;for(let j=a;j<=z;j++){const ops=witness(n,j);check(ops.filter(x=>x==='POP').length<=p&&ops.filter(x=>x!=='POP').length<=r,'illegal witness');for(let b=2;b<m;b++){const K=trace(defect(m,b),Q,ops).at(-1).K;check(K===(b===j?1:0),'position witness wrong');witnessChecks++}}
 return {m,n,p,r,fiber:N,classes:p+r+1,masses,actionWords:ws.length,historyPairsChecked:pairTests,readerTraceChecks,witnessChecks,visible:[a,z],rawIndexBits:Math.ceil(Math.log2(N)),classBits:Math.ceil(Math.log2(p+r+1))};
}
function main(){const params=[[8,3,0,1],[9,3,1,1],[10,3,1,2],[11,4,2,2],[13,5,3,2]];const cases=params.map(x=>runCase(...x));
 const total=f=>cases.reduce((a,x)=>a+x[f],0);
 return {marker:'STAGE434B_PARAMETRIC_FIBER_QUOTIENT_PASS',nativeDirections:DIR.length,cases,totals:{histories:total('fiber'),legalActionWordsEnumerated:total('actionWords'),historyPairsChecked:total('historyPairsChecked'),exactWitnessesChecked:total('witnessChecks'),readerTraceChecks:total('readerTraceChecks')},generalTheorem:'For integers n>=2, 0<=p<=n-1, r>=1, m>=n+r+2: a single-B native-X6 observer fiber has m-2 histories and exactly p+r+1 future classes, of masses (m-2-p-r,1,...,1).'};
}
const result=main();if(typeof process!=='undefined'&&process.stdout)process.stdout.write(JSON.stringify(result,null,2)+'\n');
