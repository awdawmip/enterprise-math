// PREFIX-507: independent exact checks of native observer / five-color Parikh supports.
// Run: node prefix507_V_interval_moment_certificate.js
"use strict";
const colors=[0,4,1,2,3,3,4,4,4,4], gates=[[0,0,1],[0,1,0]];
function* parts(n,k){if(k===1){yield[n];return;}for(let a=0;a<=n;a++)for(const t of parts(n-a,k-1))yield[a,...t];}
const endings=[[[]]];for(let n=1;n<=3;n++)endings[n]=endings[n-1].flatMap(s=>[0,1,2,3,4].map(x=>[...s,x]));
function suffixSupport(k,gate){
 const L=Math.min(3,k.reduce((a,b)=>a+b,0)),result=new Set();
 for(const s of endings[L]){
  const used=[0,0,0,0,0];for(const x of s)used[x]++;
  if(used.some((x,i)=>x>k[i]))continue;
  const rem=k.map((x,i)=>x-used[i]);let q=0;
  for(let j=1;j<=L;j++)if(gate.slice(0,j).every((v,i)=>v===s[L-j+i]))q=j;
  if(rem[1]+rem[2])result.add(q+",B");
  if(rem[3])result.add(q+",C");
  if(rem[1]+rem[2]+rem[3]===0){
   let t="N";for(const x of s)if(x===1||x===2||x===3){t=x===3?"C":"B";break;}
   result.add(q+","+t);
  }
 }
 return result;
}
function observe(cnt){
 const y=[],p=[];for(let i=0;i<5;i++){y.push(cnt[i*2]-cnt[i*2+1]);p.push(Math.min(cnt[i*2],cnt[i*2+1]));}
 return {y,V:p[1]+2*p[3]+p[4],W:p[2]+p[4]};
}
function obsKey(o){return o.y.join(",")+"|"+o.W+"|"+o.V;}
function liftedMap(n,gate){
 const m=new Map(),cached=new Map();
 for(const c of parts(n,10)){
  const o=observe(c),k=[c[0],c[2],c[3],c[4]+c[5],c[1]+c[6]+c[7]+c[8]+c[9]];
  const ck=k.join(",");if(!cached.has(ck))cached.set(ck,suffixSupport(k,gate));
  const key=obsKey(o);if(!m.has(key))m.set(key,new Set());
  for(const s of cached.get(ck))m.get(key).add(s);
 }
 return m;
}
function wordMap(n,gate){
 const m=new Map(),counts=Array(10).fill(0),w=[];
 function walk(j){
  if(j===n){
   const o=observe(counts),key=obsKey(o),s=w.map(x=>colors[x]);let q=0,t="N";
   for(let z=1;z<=3&&z<=n;z++)if(gate.slice(0,z).every((v,i)=>v===s[n-z+i]))q=z;
   for(const x of s)if(x===1||x===2||x===3){t=x===3?"C":"B";break;}
   if(!m.has(key))m.set(key,new Set());m.get(key).add(q+","+t);return;
  }
  for(let x=0;x<10;x++){counts[x]++;w.push(x);walk(j+1);w.pop();counts[x]--;}
 }
 walk(0);return m;
}
function same(a,b){return a.size===b.size&&[...a].every(x=>b.has(x));}
function rows(m,n){
 const t=new Map();
 for(const [key,states]of m){
  const pos=key.lastIndexOf("|"),base=key.slice(0,pos),v=Number(key.slice(pos+1));
  if(!t.has(base))t.set(base,Array(n+1).fill(0));t.get(base)[v]=states.size;
 }
 return t;
}
function rangeMoment(z,l,h){
 let sum=0,first=0;
 for(let v=l;v<=h;v++){sum+=z[v];first+=(v+1)*z[v];}
 return [sum,first];
}
function main(){
 const out={certificate:"PREFIX507_PRESBURGER_V_INTERVAL_MOMENTS",status:"ALL_CHECKS_PASS",
  scope:"All ten-direction ordered words length n<=6 compared to independent native occupancy/five-color suffix lifting; each V interval and first moment checked independently. Lengths 7..9: occupancy/suffix construction only. No quantifier-elimination compiler executed.",
  gates:{},counterexample:null};
 for(let gi=0;gi<2;gi++){
  const gate=gates[gi],key=gi===0?"aab":"aba";let result=[];
  for(let n=0;n<=9;n++){
   const viaOccupancy=liftedMap(n,gate);let intervals=0,orderedWords=null;
   if(n<=6){
    const direct=wordMap(n,gate);orderedWords=Math.pow(10,n);
    if(direct.size!==viaOccupancy.size)throw Error("fiber size mismatch: "+key+" "+n);
    for(const [k,states]of direct)if(!viaOccupancy.has(k)||!same(states,viaOccupancy.get(k)))throw Error("fiber support mismatch: "+key+" "+n+" "+k);
    const a=rows(direct,n),b=rows(viaOccupancy,n);
    if(a.size!==b.size)throw Error("row size mismatch");
    for(const [row,z]of a){const w=b.get(row);if(!w)throw Error("row missing");
     for(let l=0;l<=n;l++)for(let h=l;h<=n;h++){
      const f=rangeMoment(z,l,h),g=rangeMoment(w,l,h);
      if(f[0]!==g[0]||f[1]!==g[1])throw Error("interval moment mismatch: "+key+" "+n+" "+row+" "+l+" "+h);
      intervals++;
     }
    }
   }
   result.push({n,raw_ordered_words:orderedWords,observation_fibers:viaOccupancy.size,
                V_interval_count_and_first_moment_comparisons:intervals});
  }
  out.gates[key]=result;
 }
 const m=liftedMap(2,gates[0]);
 out.counterexample={
  n:2,y:[0,0,0,0,0],W:0,state:"q=0,t=N",
  reachable_V:[0,2],
  V0:[...m.get("0,0,0,0,0|0|0")].sort(),
  V1:m.has("0,0,0,0,0|0|1")?[...m.get("0,0,0,0,0|0|1")].sort():[],
  V2:[...m.get("0,0,0,0,0|0|2")].sort()
 };
 if(!out.counterexample.V0.includes("0,N")||out.counterexample.V1.includes("0,N")||
    !out.counterexample.V2.includes("0,N"))throw Error("periodic hole witness invalid");
 return out;
}
if(typeof module!=="undefined"&&require.main===module)console.log(JSON.stringify(main()));
