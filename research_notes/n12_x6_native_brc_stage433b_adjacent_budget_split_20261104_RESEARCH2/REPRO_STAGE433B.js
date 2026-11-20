'use strict';
const D='ABCDEFGHIJKL'.split('');
function check(ok,message){if(!ok)throw Error(message);}
function same(a,b){return JSON.stringify(a)===JSON.stringify(b);}
function vec(w){const z=[0,0,0,0,0,0];for(const c of w){const i=D.indexOf(c);check(i>=0,'invalid native direction');z[i>>1]+=(i%2===0?1:-1);}return z;}
function J(w){const z={};for(let i=1;i<w.length;i++){const e=w[i-1]+w[i];z[e]=(z[e]||0)+1;}return Object.entries(z).sort((a,b)=>a[0].localeCompare(b[0]));}
function K(P,Q){let k=0;for(let i=0;i<Math.min(P.length,Q.length);i++)if(P[i]===Q[i])k++;return k;}
function observer(P,Q){return {lengths:[P.length,Q.length],xP:vec(P),xQ:vec(Q),JP:J(P),JQ:J(Q),K:K(P,Q)};}
function firstFromResidual(E,x){const target=x.slice();for(const [e,count] of E){const i=D.indexOf(e[1]);target[i>>1]-=(i%2===0?1:-1)*count;}return D.find(d=>same(vec(d),target))||null;}
function euler(E,x){const L=1+E.reduce((s,row)=>s+row[1],0),first=firstFromResidual(E,x);check(first!==null,'invalid starting residual');const used=E.map(row=>row[1]),out=[];function dfs(w){if(w.length===L){out.push(w);return;}for(let i=0;i<E.length;i++)if(used[i]&&E[i][0][0]===w[w.length-1]){used[i]--;dfs(w+E[i][0][1]);used[i]++;}}dfs(first);return out.sort();}
function brute(E,x,L){const out=[];function walk(w){if(w.length===L){if(same(J(w),E)&&same(vec(w),x))out.push(w);return;}for(const d of D)walk(w+d);}walk('');return out.sort();}
function T(P,Q,p,r){const n=Q.length;return Q.slice(n-p-1)+'|'+P.slice(n-p,n+r);}
function actionWords(p,r){const out=[];function go(np,na,word){out.push(word);if(np<p)go(np+1,na,[...word,'POP']);if(na<r)for(const d of D)go(np,na+1,[...word,'APPEND:'+d]);}go(0,0,[]);return out;}
function trace(P,Q,actions){let q=Q;const out=[{Q:q,O:observer(P,q)}];for(const a of actions){if(a==='POP'){check(q.length>0,'invalid POP');q=q.slice(0,-1);}else q+=a.split(':')[1];out.push({Q:q,O:observer(P,q)});}return out;}
function bits(q){let b=0;while(2**b<q)b++;return b;}
function main(){
 const P='AAABA',Q='CC',base=observer(P,Q),a=euler(base.JP,base.xP),b=euler(base.JQ,base.xQ);
 check(same(a,brute(base.JP,base.xP,P.length))&&same(b,brute(base.JQ,base.xQ,Q.length)),'Euler vs 12-symbol brute mismatch');
 const fiber=[];for(const p of a)for(const q of b)if(same(observer(p,q),base))fiber.push({P:p,Q:q});
 check(same(fiber.map(x=>x.P),['AAABA','AABAA','ABAAA']),'unexpected full fiber');
 let checked=0;const rows=[];
 for(const [p,r] of [[0,1],[1,1],[0,2],[1,2]]){
  const ws=actionWords(p,r),map=new Map();for(const x of fiber){const t=T(x.P,x.Q,p,r);map.set(t,(map.get(t)||0)+1);}
  let equalHistoryPairs=0,distinguishableHistoryPairs=0;
  for(let i=0;i<fiber.length;i++)for(let j=i+1;j<fiber.length;j++){
   let eq=true;for(const word of ws){checked++;if(!same(trace(fiber[i].P,Q,word),trace(fiber[j].P,Q,word))){eq=false;break;}}
   check(eq===(T(fiber[i].P,Q,p,r)===T(fiber[j].P,Q,p,r)),'boundary/future equivalence discrepancy');
   if(eq)equalHistoryPairs++;else distinguishableHistoryPairs++;
  }
  check(map.size===((p===0&&r===1)?2:3),'incorrect budget class count');
  rows.push({p,r,actionWords:ws.length,q:map.size,fixedBits:bits(map.size),classes:[...map].sort((u,v)=>u[0].localeCompare(v[0])).map(([t,n])=>({boundary:t,mass:n})),equalHistoryPairs,distinguishableHistoryPairs});
 }
 const w0='AAABA',w1='ABAAA',pop=['POP','APPEND:A'],app=['APPEND:A','APPEND:B'];
 check(same(observer(w0,Q),observer(w1,Q)),'base observers differ');
 const trPop=[trace(w0,Q,pop),trace(w1,Q,pop)],trApp=[trace(w0,Q,app),trace(w1,Q,app)];
 check(same(trPop[0].map(x=>x.O.K),[0,0,1])&&same(trPop[1].map(x=>x.O.K),[0,0,0]),'pop witness invalid');
 check(same(trApp[0].map(x=>x.O.K),[0,1,2])&&same(trApp[1].map(x=>x.O.K),[0,1,1]),'append witness invalid');
 return {marker:'STAGE433B_ADJACENT_BUDGET_SPLIT_EXACT_PASS',date:'2026-11-04',nativeDirections:12,independentBruteP:12**5,independentBruteQ:12**2,verifiedFullObserverFiber:fiber,initialObserver:base,rows,comparedPairActionWords:checked,strictWitnesses:{expandedPop:{actions:pop,first:trPop[0],second:trPop[1]},expandedAppend:{actions:app,first:trApp[0],second:trApp[1]}},proofScope:'complete three-history native-X6 observer fiber and bounded future words; general refinement is proved separately'};
}
const ANSWER=main();
if(typeof process!=='undefined'&&process.stdout)process.stdout.write(JSON.stringify(ANSWER,null,2)+'\n');
ANSWER;