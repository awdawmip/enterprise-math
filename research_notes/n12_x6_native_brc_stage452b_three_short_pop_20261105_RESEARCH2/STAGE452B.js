// Stage452-B: exact finite-fiber verifier, native signed-X6 labels 0..11.
// Pure JavaScript; execute: node STAGE452B.js
"use strict";
const A=0,B=1;
function words(n,k){
 const out=[];function f(s,b){if(s.length===n){if(b===k)out.push(s);return;}
 const i=s.length;for(const x of [A,B]){if(x===B&&(i===0||i===n-1||s[i-1]===B))continue;
 if(b+(x===B)>k)continue;f([...s,x],b+(x===B));}}f([],0);return out;
}
function obs(p,q){
 const v=w=>{const a=Array(6).fill(0);for(const x of w)a[Math.floor(x/2)]+=x%2?-1:1;return a;};
 const j=w=>{const a=Array(144).fill(0);for(let i=1;i<w.length;i++)a[w[i-1]*12+w[i]]++;
 return a.map((x,i)=>x?i+":"+x:"").filter(Boolean);};
 let k=0;for(let i=0;i<Math.min(p.length,q.length);i++)if(p[i]===q[i])k++;
 return JSON.stringify([p.length,q.length,v(p),v(q),j(p),j(q),k]);
}
function key(p,q,rp,pp=3,pq=2){
 const m=p.length,n=q.length,h=Math.min(n-1,m+rp),a=[];
 for(let i=m-pp;i<=m-1;i++)if(i>=1)a.push("P"+i+":"+p[i-1]);
 for(let i=n-pq;i<=n-1;i++)if(i>=1)a.push("Q"+i+":"+q[i-1]);
 for(let i=m-pp+1;i<=h;i++)if(i>=1&&i<=n)a.push("W"+i+":"+q[i-1]);
 return a.join("|");
}
function builder(){
 const cache=new Map(),intern=new Map();let states=0;
 function sig(p,q,pp,pq,rp,rq){
  const state=[p.join(","),q.join(","),pp,pq,rp,rq].join("|");
  if(cache.has(state))return cache.get(state);
  const ch=[];
  if(pp>0&&p.length>0)ch.push(["Ppop",sig(p.slice(0,-1),q,pp-1,pq,rp,rq)]);
  if(pq>0&&q.length>0)ch.push(["Qpop",sig(p,q.slice(0,-1),pp,pq-1,rp,rq)]);
  if(rp>0)for(let x=0;x<12;x++)ch.push(["Papp"+x,sig([...p,x],q,pp,pq,rp-1,rq)]);
  if(rq>0)for(let x=0;x<12;x++)ch.push(["Qapp"+x,sig(p,[...q,x],pp,pq,rp,rq-1)]);
  const z=JSON.stringify([obs(p,q),ch]);
  if(!intern.has(z))intern.set(z,intern.size+1);
  const id=intern.get(z);cache.set(state,id);states++;return id;
 }
 return {sig,stats:()=>({states,interned:intern.size})};
}
function run(){
 const cases=[[5,7,1,1,0,0],[5,7,1,1,1,0],[5,7,1,1,0,1],
 [6,8,1,1,1,0],[6,8,1,1,0,1],[6,8,1,2,1,0],
 [7,9,1,1,0,0],[7,9,1,2,1,0]];
 const verifier=builder();let fibers=0,pairs=0,histories=0,failed=null;
 const caseStats=[];
 for(const [m,n,kp,kq,rp,rq] of cases){
  const groups=new Map();let localh=0,localf=0,localclasses=0;
  for(const p of words(m,kp))for(const q of words(n,kq)){
   const o=obs(p,q);if(!groups.has(o))groups.set(o,[]);
   groups.get(o).push({p,q,k:key(p,q,rp),sig:verifier.sig(p,q,3,2,rp,rq)});
  }
  for(const hs of groups.values()){
   fibers++;localf++;histories+=hs.length;localh+=hs.length;
   localclasses+=new Set(hs.map(x=>x.k)).size;
   for(let i=0;i<hs.length;i++)for(let j=0;j<i;j++){
    pairs++;if((hs[i].k===hs[j].k)!==(hs[i].sig===hs[j].sig))
     failed={case:[m,n,kp,kq,rp,rq],a:hs[i],b:hs[j]};
   }
  }
  caseStats.push({parameters:[m,n,kp,kq,rp,rq],fibers:localf,histories:localh,classes:localclasses});
 }
 const wq=(()=>{const m=6,n=10,p=Array(m).fill(A),q1=Array(n).fill(A),q2=Array(n).fill(A);
  q1[m-3]=B;q2[1]=B;return {current_same:obs(p,q1)===obs(p,q2),
  old_same:key(p,q1,0,2,2)===key(p,q2,0,2,2),new_diff:key(p,q1,0)!==key(p,q2,0),
  K_after_P_POP3:[q1,q2].map(q=>JSON.parse(obs(p.slice(0,-3),q))[6])};})();
 const wp=(()=>{const m=7,n=10,p1=Array(m).fill(A),p2=Array(m).fill(A),q=Array(n).fill(A);
  p1[m-4]=B;p2[1]=B;return {current_same:obs(p1,q)===obs(p2,q),
  old_same:key(p1,q,0,2,2)===key(p2,q,0,2,2),new_diff:key(p1,q,0)!==key(p2,q,0),
  J_after_P_POP3:[p1,p2].map(p=>JSON.parse(obs(p.slice(0,-3),q))[4])};})();
 const result={marker:"STAGE452B_3P2Q_FINITE_FUTURE_EQUIVALENCE_CHECK",cases:caseStats,
  totals:{case_count:cases.length,fibers,histories,pairs,signatures:verifier.stats()},
  witnessQ:wq,witnessP:wp,failed,pass:failed===null&&wq.current_same&&wq.old_same&&wq.new_diff
   &&wp.current_same&&wp.old_same&&wp.new_diff};
 if(!result.pass)throw Error(JSON.stringify(result));return result;
}
const executed=run();
if(typeof console!=="undefined")console.log(JSON.stringify(executed,null,2));
