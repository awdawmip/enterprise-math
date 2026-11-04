"use strict";
// PREFIX-493 exact certificate: X6 with one native axis held unused.
// 10 ordered signed symbols, raw direction occupancies, KMP, first-source.
// The theorem holds at all lengths; this code covers exactly n=0..8.
const symbols="aAbBcCdDeE";
function choose(n,k){if(n<k||k<0)return 0;let x=1;for(let j=1;j<=k;j++)x=x*(n-j+1)/j;return Math.round(x);}
function coeff(poly,k,n){let s=0;for(let j=0;j<poly.length;j++)s+=poly[j]*choose(n-j+k-1,k-1);return s;}
function G(n){
 const f=(p,k)=>coeff(p,k,n), a=Array(8).fill(0);
 a[1]=f([1,1,1,1,-1,-1],5);
 a[2]=f([0,0,1,1],5)+f([0,2,2,4,4],6);
 a[4]=f([0,0,1,1,1,1],5)+f([0,2,2,4,4],6);
 a[3]=f([0,0,0,0,1,1],5);
 a[6]=f([0,0,0,0,1,0,1],6)+f([0,0,0,4,0,8],7)+f([0,0,4,0,8],8);
 a[7]=f([0,0,0,0,1],6);return a;
}
function phi(a){let v=Array(8).fill(0);v[2]=a[1]+a[2]+a[3];v[4]=a[4];v[6]=a[6]+a[7];return v;}
function prediction(g,n){
 let q0=G(n),q1=G(n-1),q2=g==="aab"?G(n-2):phi(G(n-2)),q3=phi(G(n-3));
 if(n>=1)q0[1]--;
 if(n>=(g==="aab"?3:2))q0[2]--;
 if(g==="aab"&&n>=2)q1[1]--;
 return [q0,q1,q2,q3];
}
function kmp(q,s,g){let tail=g.slice(0,q)+s;for(let k=g.length;k>=0;k--)if(tail.endsWith(g.slice(0,k)))return k;return 0;}
function observer(c){let y=[],p=[];for(let i=0;i<10;i+=2){y.push(c[i]-c[i+1]);p.push(Math.min(c[i],c[i+1]));}
 return [y,p[1]+2*p[3]+p[4],p[2]+p[4]];
}
function appendObserver(c,j){
 let [y,V,W]=observer(c),i=Math.floor(j/2),sign=j%2===0?1:-1;
 let dp=(sign>0?y[i]<0:y[i]>0)?1:0;
 y[i]+=sign;V+=[0,1,0,2,1][i]*dp;W+=[0,0,1,0,1][i]*dp;
 return [y,V,W];
}
function serialize(x){return x[0].join(",")+";"+x[1]+";"+x[2];}
function countMasks(m){let a=Array(8).fill(0);for(let v of m.values())a[v]++;return a;}
function analyze(g,limit){
 let states=new Set(["0000000000|0|0"]),lines=[],checks=0;
 for(let n=0;n<=limit;n++){
  let byQ=Array.from({length:4},()=>new Map);
  for(let key of states){
   let [s,q,t]=key.split("|"),c=[...s].map(Number),f=serialize(observer(c));
   let m=byQ[+q];m.set(f,(m.get(f)||0)|(1<<(+t)));
  }
  let got=byQ.map(countMasks),want=prediction(g,n);
  for(let q=0;q<4;q++)for(let m=0;m<8;m++){
   if(got[q][m]!==want[q][m])throw Error(JSON.stringify({g,n,q,m,got:got[q][m],want:want[q][m]}));
  }
  let qc=got.map(v=>v.reduce((a,b)=>a+b,0));
  lines.push({n,reachable_raw_states:states.size,observer_fibers:qc.reduce((a,b)=>a+b,0),q_fibers:qc,q2_N_masks:got[2][1]+got[2][3]+got[2][7]});
  if(n===limit)break;
  let next=new Set;
  for(let key of states){
   let [s,q,t]=key.split("|"),c=[...s].map(Number);
   for(let j=0;j<10;j++){
    let predicted=serialize(appendObserver(c,j));
    c[j]++;
    let obtained=serialize(observer(c));
    if(predicted!==obtained)throw Error("BRC append failure: "+g+" "+key+" "+symbols[j]);
    checks++;
    let nextTag=(+t)===0?((j===2||j===3)?1:((j===4||j===5)?2:0)):+t;
    next.add(c.join("")+"|"+kmp(+q,symbols[j],g)+"|"+nextTag);
    c[j]--;
   }
  }
  states=next;
 }
 return {rows:lines,brc_append_checks:checks};
}
function verify(limit=8){
 if(limit>8)throw Error("single-digit occupancy key scoped to n<=8");
 let aab=analyze("aab",limit),aba=analyze("aba",limit);
 for(let n=0;n<=limit;n++){
  if(aba.rows[n].observer_fibers-aab.rows[n].observer_fibers!==(n>=3?1:0))throw Error("whole KMP difference failed at "+n);
  for(let q=2;q<=3;q++)if(aab.rows[n].q_fibers[q]!==aba.rows[n].q_fibers[q])throw Error("terminal totals differ");
 }
 return {project:"Enterprise Math",unit:"PREFIX-493",coverage:"All reachable raw signed occupancies x KMP x first-source tags, n=0.."+limit,
 statement:"Exact per-mask rational transfer and BRC append law",gates:{aab,aba},status:"ALL_CHECKS_PASS"};
}
if(typeof module!=="undefined"&&require.main===module)console.log(JSON.stringify(verify(8),null,2));
