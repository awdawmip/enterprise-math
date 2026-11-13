// R710s positive source-labelled BRC exact counter / four-phase simulation.
"use strict";
const PACK={A:["012","013","023"],a:["012","023","013"],
 B:["012","023","123"],b:["012","123","023"]};
function ok(x,m){if(!x)throw Error(m);}
function adj(x,y){let n=0;for(const z of x)if(y.includes(z))n++;return n===2;}
function words(k,l){const have={A:k,a:k,B:l,b:l},out=[],p=[];
 function visit(){if(p.length===2*(k+l)){out.push(p.join(""));return;}
 for(const x of ["A","a","B","b"])if(have[x]>0){have[x]--;p.push(x);visit();p.pop();have[x]++;}}
 visit();return out;}
function states(w){let a=[];for(const z of w)a.push(...PACK[z]);
 for(let i=0;i<a.length;i++)ok(adj(a[i],a[(i+1)%a.length]),"adj");return a;}
function hol(w){let h=[0,1,2],a=[0,2,1],b=[1,0,2];
 for(const x of w){const p=(x==="A"||x==="a")?a:b;const old=h;h=p.map(j=>old[j]);}
 return h.join("");}
function init(S,P,N){const m=S.length,z=()=>Array(m).fill(0);return {
 X:S.slice(),P:P.slice(),N:N.slice(),ip:z(),op:z(),im:z(),om:z(),ep:z(),em:z()};}
function tick(o){const m=o.X.length;ok(m>=4&&m%2===0,"even");
 const old={};for(const key of Object.keys(o))old[key]=o[key].slice();
 const f=Array.from({length:m},(_,i)=>Number(adj(old.X[i],old.X[(i+1)%m])
     &&old.P[(i+1)%m]>0&&old.N[i]>0));
 const target={};for(const key of Object.keys(o))target[key]=o[key].slice();
 for(let i=0;i<m;i++){let a=f[i],b=f[(i+m-1)%m];
  target.P[i]+=a-b;target.N[i]+=b-a;
  target.ip[i]+=a;target.op[i]+=b;target.im[i]+=b;target.om[i]+=a;
  target.ep[i]+=a;target.em[i]+=a;
  target.X[i]=a?old.X[(i+1)%m]:old.X[i];}
 for(const [par,typ] of [[0,"P"],[0,"N"],[1,"P"],[1,"N"]]){
  const seen=new Set();
  for(let i=par;i<m;i+=2){if(!f[i])continue;const j=(i+1)%m;
   ok(!seen.has(i)&&!seen.has(j),"port conflict");seen.add(i);seen.add(j);
   if(typ==="P"){ok(o.P[j]>0,"plus overdraft");o.P[j]--;o.P[i]++;
    o.op[j]++;o.ip[i]++;o.ep[i]++;}
   else{ok(o.N[i]>0,"minus overdraft");o.N[i]--;o.N[j]++;
    o.om[i]++;o.im[j]++;o.em[i]++;}}}
 o.X=target.X;
 for(const key of Object.keys(o))ok(JSON.stringify(o[key])===JSON.stringify(target[key]),"atomic "+key);
 for(let i=0;i<m;i++){ok(o.P[i]>=0&&o.N[i]>=0,"negative");
  ok(o.P[i]+o.N[i]===old.P[i]+old.N[i],"local stock");}
 for(const key of ["P","N"])ok(o[key].reduce((a,b)=>a+b,0)===
  old[key].reduce((a,b)=>a+b,0),"global stock");
 return f.reduce((a,b)=>a+b,0);}
function main(){
 let branches=0,layers=0,events=0,partial=0;const cases=[];
 const targets={"1,1":[16,4,4],"1,2":[108,36,36],
  "2,1":[108,36,36],"2,2":[1296,612,612]};
 for(const [k,l] of [[1,1],[1,2],[2,1],[2,2]]){
  const W=words(k,l),m=6*(k+l),hist={"012":0,"120":0,"201":0};
  for(const w of W){const S=states(w),o=init(S,Array(m).fill(1),Array(m).fill(1));
   for(let t=0;t<m;t++){ok(tick(o)===m,"full fire");
    for(let i=0;i<m;i++){ok(o.X[i]===S[(i+t+1)%m],"copy");
     ok(o.P[i]===1&&o.N[i]===1,"stocks");}}
   ok(JSON.stringify(o.X)===JSON.stringify(S),"return");
   for(const a of [o.ip,o.op,o.im,o.om,o.ep,o.em])for(const v of a)ok(v===m,"ledger");
   const h=hol(w);ok(h in hist,"h");hist[h]++;branches++;layers+=m;events+=2*m*m;}
  ok(JSON.stringify([hist["012"],hist["120"],hist["201"]])===
   JSON.stringify(targets[k+","+l]),"hist");
  cases.push({k,l,cells:m,branches:W.length,layers:W.length*m,
    events:W.length*2*m*m,holonomy_histogram:hist});
  const S=states(W[0]),P=Array.from({length:m},(_,i)=>1+(i%3===0?2:0)),
   N=Array.from({length:m},(_,i)=>1+(i%4===0?3:0)),s=init(S,P,N);
  for(let t=0;t<m;t++)ok(tick(s)===m,"nonuniform full");
  ok(JSON.stringify(s.P)===JSON.stringify(P)&&JSON.stringify(s.N)===JSON.stringify(N),"slack");
  for(let p=0;p<3;p++)for(let n=0;n<3;n++)
   for(let p1=0;p1<3;p1++)for(let n1=0;n1<3;n1++){
    let a=Array(m).fill(1),b=Array(m).fill(1);
    a[0]=p;b[0]=n;a[1]=p1;b[1]=n1;
    const q=init(S,a,b);for(let t=0;t<3;t++){tick(q);partial++;}}
 }
 ok(branches===2904&&layers===67248&&events===3143232&&partial===972,"coverage");
 return {verdict:"R710S_FOUR_PHASE_BRC_SERIALIZABILITY_PASS",
  scientific_pin:"a72226e2430ffa4786321ac86e7f0c599d5f0389",
  cases,total_branches:branches,total_macro_layers:layers,
  serialized_typed_transfer_events:events,perturbed_macro_layers:partial,
  substeps:["even edge plus","even edge minus","odd edge plus","odd edge minus"],
  exact_raw_slack_fiber_m12_plus1_minus1:144,
  observation_scope:"committed boundaries; substep current may be nonzero",
  arithmetic:"positive source-labelled BRC words and exact integer native event counts"};
}
if(typeof module!=="undefined"&&require.main===module)console.log(JSON.stringify(main(),null,2));
