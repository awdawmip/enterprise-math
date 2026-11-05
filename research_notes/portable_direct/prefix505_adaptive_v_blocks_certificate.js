"use strict";
// PREFIX-505: exact adaptive V blocks, native BRC+KMP+first-source observer.
// Standalone: node prefix505_adaptive_v_blocks_certificate.js
const AL="aAbBcCdDeE", CV=[0,1,0,2,1], CW=[0,0,1,0,1];
function advance(x,ch,g){
 const y=x.slice(0,5),i=Math.floor(AL.indexOf(ch)/2),s=ch===ch.toLowerCase()?1:-1;
 const cancel=s*y[i]<0?1:0;y[i]+=s;
 let q=0,word=g.slice(0,x[7])+ch;
 for(let j=0;j<=3;j++)if(word.endsWith(g.slice(0,j)))q=j;
 let t=x[8];if(t==="N"){if(ch==="b"||ch==="B")t="B";else if(ch==="c"||ch==="C")t="C";}
 return [...y,x[5]+CV[i]*cancel,x[6]+CW[i]*cancel,q,t];
}
function stateRows(states,n){
 const rs=new Map();
 for(const x of states.values()){
 const [u,v,c,d,e,V,W,q,t]=x,cc=Math.abs(c),s=Math.abs(d)+Math.abs(e);
 const m=(n-Math.abs(u)-Math.abs(v)-cc-s)/2;
 if(m<0||!Number.isInteger(m))throw Error("parity");
 const key=[u,v,cc,s,W].join(",");
 if(!rs.has(key))rs.set(key,{key,sets:Array.from({length:2*m+1},()=>new Set())});
 rs.get(key).sets[V].add(q+":"+t);
 }
 for(const r of rs.values()){r.controls=r.sets.map(s=>[...s].sort());r.k=r.controls.map(v=>v.length);delete r.sets;}
 return rs;
}
function makePrefix(k){const a=[0],b=[0];for(let v=0;v<k.length;v++){a.push(a[v]+k[v]);b.push(b[v]+(v+1)*k[v]);}return {a,b};}
function cost(p,i,j){return p.b[j]-p.b[i]-i*(p.a[j]-p.a[i]);}
function score(cuts,p){let t=0;for(let j=0;j<cuts.length-1;j++)t+=cost(p,cuts[j],cuts[j+1]);return t;}
function optimize(k,b){
 const L=k.length,B=Math.ceil(L/b),p=makePrefix(k);
 const dp=Array.from({length:B+1},()=>Array(L+1).fill(Infinity));
 const back=Array.from({length:B+1},()=>Array(L+1).fill(-1));dp[0][0]=0;
 for(let z=1;z<=B;z++)for(let j=z;j<=L;j++)for(let i=Math.max(z-1,j-b);i<j;i++){
   let val=dp[z-1][i]+cost(p,i,j);
   if(val<dp[z][j]){dp[z][j]=val;back[z][j]=i;}
 }
 let cuts=[L],j=L;
 for(let z=B;z>0;z--){j=back[z][j];cuts.unshift(j);}
 if(j!==0)throw Error("no backtrack");
 let regular=[0];for(let v=b;v<L;v+=b)regular.push(v);regular.push(L);
 return {cuts,regular,optimalCost:score(cuts,p),regularCost:score(regular,p),B};
}
function exhaustive(k,b){
 let L=k.length,B=Math.ceil(L/b),p=makePrefix(k),best=Infinity,count=0;
 function scan(i,z,total){
  if(z===B){if(i===L){count++;best=Math.min(best,total);}return;}
  for(let j=i+1;j<=Math.min(i+b,L);j++){
   if(L-j<B-z-1||L-j>(B-z-1)*b)continue;
   scan(j,z+1,total+cost(p,i,j));
  }
 }
 scan(0,0,0);return {best,count};
}
function checkRow(row,cuts){
 const k=row.k,P=[0];
 for(let j=0;j<cuts.length-1;j++){
  let v=P[j];for(let h=cuts[j];h<cuts[j+1];h++)v+=k[h];P.push(v);
 }
 let checked=0;
 for(let v=0;v<k.length;v++)for(let q=0;q<k[v];q++){
  let i=0;while(cuts[i+1]<=v)i++;
  let rank=P[i]+q;for(let h=cuts[i];h<v;h++)rank+=k[h];
  if(rank!==checked)throw Error("rank");
  let j=0;while(j<P.length-1&&P[j+1]<=rank)j++;
  if(j>=P.length-1)throw Error("prefix sentinel");
  let rem=rank-P[j],vv=-1,qq=-1;
  for(let h=cuts[j];h<cuts[j+1];h++){
   if(rem<k[h]){vv=h;qq=rem;break;}rem-=k[h];
  }
  if(vv!==v||qq!==q)throw Error("inverse");
  checked++;
 }
 if(checked!==P[P.length-1])throw Error("row tally");
 return checked;
}
function verify(maxN=8){
 const out={research:"PREFIX-505",status:"ALL_CHECKS_PASS",
 frozen_input:"f42f2906d77f24085c123f3ccfe9667d41caa96d",scope:"native X6 five signed axes; BRC V,W; KMP q; first B/C source t",
 arithmetic:"exact safe integer (all tested values below 2^53)",gates:{}};
 for(const g of ["aab","aba"]){
  let states;const series=[];
  for(let n=0;n<=maxN;n++){
   if(n===0)states=new Map([["0,0,0,0,0,0,0,0,N",[0,0,0,0,0,0,0,0,"N"]]]);
   else{let next=new Map();for(const x of states.values())for(const ch of AL){let y=advance(x,ch,g);next.set(y.join(","),y);}states=next;}
   let rows=stateRows(states,n),checks=0,bruteCount=0,witness=null;
   const byWidth={};for(const b of [2,3,4])byWidth[b]={rows:0,improved:0,uniform_calls:0,optimal_calls:0,extra_boundary_words:0};
   for(const row of rows.values()){
    for(const b of [2,3,4]){
     let x=optimize(row.k,b),br=exhaustive(row.k,b);
     if(br.count===0||x.optimalCost!==br.best||x.optimalCost>x.regularCost)throw Error("optimality");
     if(x.cuts.length!==x.regular.length)throw Error("block count");
     for(let i=1;i<x.cuts.length;i++)if(x.cuts[i]-x.cuts[i-1]>b)throw Error("max width");
     if(b===2)checks+=checkRow(row,x.cuts);
     const m=byWidth[b];m.rows++;m.uniform_calls+=x.regularCost;m.optimal_calls+=x.optimalCost;m.extra_boundary_words+=x.B-1;
     if(x.optimalCost<x.regularCost){
       m.improved++;
       if(!witness||x.regularCost-x.optimalCost>witness.gain)
       witness={gate:g,n,row:row.key,k:row.k,b,regular:x.regular,adaptive:x.cuts,uniform:x.regularCost,optimal:x.optimalCost,gain:x.regularCost-x.optimalCost};
     }
     bruteCount+=br.count;
    }
   }
   const total=[...rows.values()].reduce((a,row)=>a+row.k.reduce((x,v)=>x+v,0),0);
   if(checks!==total)throw Error("coverage");
   series.push({n,native_states:states.size,rows:rows.size,row_control_states:total,rank_inverse_checked:checks,brute_partitions:bruteCount,widths:byWidth,witness});
  }
  out.gates[g]=series;
 }
 return out;
}
if(typeof module!=="undefined"&&typeof require!=="undefined"&&require.main===module)console.log(JSON.stringify(verify(Number(process.argv[2]||8)),null,2));
