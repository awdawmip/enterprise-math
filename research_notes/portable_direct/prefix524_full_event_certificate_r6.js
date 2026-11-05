// PREFIX-524: exact aAc-event distribution certificate for the symbolic four-STAR graph.
// Run with Node.js. No physical time or trigonometric operation is used.
"use strict";
const S=[[0,2,5],[0,3,4],[1,2,4],[1,3,5]];
const edge=[[0,1],[2,3],[0,2],[1,3],[1,2],[0,3]];
const key=x=>x.join(","), eq=(a,b)=>a.size===b.size&&[...a].every(([k,v])=>b.get(k)===v);
const n=(j,c)=>S[j].filter(a=>a!==Math.abs(c)-1).map(a=>-Math.sign(c)*(a+1));
const ST=[];
for(let j=0;j<4;j++)for(let a of S[j])for(let v of [-1,1])for(let p of n(j,v*(a+1)))ST.push([j,p,v*(a+1)]);
if(ST.length!==48||new Set(ST.map(key)).size!==48)throw Error("48 distinct states");
const ix=new Map(ST.map((s,i)=>[key(s),i]));
const D=ST.map(([j,p,c])=>{
 let other=S.findIndex((x,k)=>k!==j&&x.includes(Math.abs(c)-1));
 return [...n(j,c).filter(t=>t!==p).map(t=>[j,c,t]),...n(other,c).map(t=>[other,c,t])].map(x=>ix.get(key(x)));
});
const indeg=Array(48).fill(0);
D.forEach(a=>a.forEach(x=>indeg[x]++));
if(!D.every(a=>a.length===3)||!indeg.every(x=>x===3))throw Error("phase degree");
const perm=a=>a.length?a.flatMap((v,i)=>perm(a.filter((_,j)=>i!==j)).map(z=>[v,...z])):[[]];
const charts=perm([0,1,2,3]).map(v=>edge.map(e=>edge.findIndex(f=>key(f)===key(e.map(x=>v[x]).sort((a,b)=>a-b)))));
function target(chart){let a=chart.indexOf(0)+1,c=chart.indexOf(2)+1,j=S.findIndex(v=>v.includes(a-1)&&v.includes(c-1));return ix.get(key([j,a,-c]));}
function hist(d,T){
 let x=new Map();for(let s=0;s<48;s++)x.set(s+",2,0",1n);
 for(let k=1;k<=d;k++){
  let y=new Map();for(let [z,val] of x){let [s,b,h]=z.split(",").map(Number);
   for(let t of D[s])for(let c of [0,1]){let hh=h+(k>1&&b===0&&c===0&&t===T?1:0),w=t+","+c+","+hh;y.set(w,(y.get(w)||0n)+val);}}
  x=y;
 }
 let H=new Map();for(let [z,val] of x){let h=+z.split(",")[2];H.set(h,(H.get(h)||0n)+val)}return H;
}
const T=target(charts[0]),A=[1n];let x=new Map([[T,1n]]);
for(let d=1;d<=32;d++){let y=new Map();for(let [s,val] of x)for(let t of D[s])y.set(t,(y.get(t)||0n)+val);x=y;if(d%2===0)A.push(x.get(T)||0n);}
if(A.slice(0,5).join(",")!=="1,0,5,28,297")throw Error("return coefficients");
for(let i=0;i+5<A.length;i++)if(A[i+5]!==5n*A[i+4]+26n*A[i+3]+78n*A[i+2]+135n*A[i+1]-243n*A[i])throw Error("return recurrence");
const N=15,F=Array.from({length:6},()=>Array(N+1).fill(0n)),R=Array(N+1).fill(0n);
for(let m=2;2*m<=N;m++)R[2*m]=4n**BigInt(m-1)*A[m];
for(let d=2;d<=N;d++)F[1][d]=9n*BigInt(d-1)*6n**BigInt(d-2);
for(let k=2;k<6;k++)for(let d=0;d<=N;d++)for(let i=0;i<=d;i++)F[k][d]+=F[k-1][d-i]*R[i];
function binom(n,k){if(k>n)return 0n;let v=1n;for(let j=1;j<=k;j++)v=v*BigInt(n-j+1)/BigInt(j);return v;}
const out=[];
for(let d=0;d<=N;d++){let H=hist(d,T);
 if([...H.values()].reduce((a,b)=>a+b,0n)!==48n*6n**BigInt(d))throw Error("total "+d);
 for(let k=1;k<6;k++)if([...H].reduce((a,[h,v])=>a+binom(h,k)*v,0n)!==F[k][d])throw Error("factorial "+d+","+k);
 for(let [h,v] of H){let actual=h===0?48n*6n**BigInt(d):0n;
  for(let k=Math.max(h,1);k<6;k++)actual+=(k-h)%2?-binom(k,h)*F[k][d]:binom(k,h)*F[k][d];
  if(actual!==v)throw Error("inversion "+d+","+h);
 }
 out.push({d,H:Object.fromEntries([...H].sort((a,b)=>a[0]-b[0]).map(([h,v])=>[h,String(v)])),F1:String(F[1][d]),F2:String(F[2][d]),F3:String(F[3][d])});
}
let chart_checks=0;for(let m of charts)for(let d=0;d<=9;d++){if(!eq(hist(d,target(m)),hist(d,T)))throw Error("S4 chart "+d);chart_checks++;}
function native(d,m){let H=new Map();function go(s,w,k){if(k===d){let c=w.map(v=>{let a=m[Math.abs(v)-1];return a===0?(v>0?"a":"A"):a===2?"c":"_"}).join(""),hit=0;for(let j=0;j+2<c.length;j++)if(c.slice(j,j+3)==="aAc")hit++;H.set(hit,(H.get(hit)||0n)+1n);return;}
 for(let t of D[s])for(let b of [0,1]){let ss=b===0?[-ST[s][2],ST[t][2]]:[ST[t][2],-ST[s][2]];go(t,w.concat(ss),k+1);}}
 for(let s=0;s<48;s++)go(s,[],0);return H;}
for(let d=0;d<=4;d++)if(!eq(native(d,charts[0]),hist(d,T)))throw Error("native scan "+d);
const q=[1,-12,16,240,-1136,4992,-19968,59904,-214272,414720,-995328,-2985984,8957952];
for(let d=13;d<=N;d++)if(q.reduce((a,b,j)=>a+BigInt(b)*F[2][d-j],0n)!==0n)throw Error("order-12 recurrence "+d);
const report={verdict:"ALL_CHECKS_PASS",scope:"symbolic four-STAR signed-X6 graph; author executable check",states:48,frames:charts.length,frame_depth_checks:chart_checks,native_histories_scanned:74640,depth_max:N,pair_order:12,q_coefficients_ascending:q,selected:[out[6],out[10],out[15]],exact_histograms:out};
console.log(JSON.stringify(report,null,2));
