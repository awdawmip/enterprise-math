function prefix480_certificate(){
"use strict";
const ORD=[..."aAbBcCdDeE"],LAM=[6n,1n,12n,1n,18n,1n,24n,1n,36n,1n];
const V=[0,1,0,2,1],W=[0,0,1,0,1];
const check=(x,msg)=>{if(!x)throw Error(msg)};
function next(o,i){
 const t=o.slice();if(i===10){t[0]++;return t}
 const ax=Math.floor(i/2),plus=i%2===0,y=o[ax+1],d=plus?(y<0?1:0):(y>0?1:0);
 t[ax+1]+=plus?1:-1;t[6]+=d*V[ax];t[7]+=d*W[ax];return t
}
function trans(w,q,c){
 const t=w.slice(0,q)+c;for(let j=w.length;j>=0;j--)if(t.endsWith(w.slice(0,j)))return j;
 throw Error("kmp")
}
function add(m,key,v){
 const old=m.get(key);if(old)m.set(key,[old[0]+v[0],old[1]+v[1],old[2]+v[2]]);else m.set(key,v)
}
const info={},logs=[];
for(const w of ["aab","aba"]){
 let states=new Map([[JSON.stringify([Array(8).fill(0),0]),[1n,1n,1n]]]), rows=[];
 for(let n=0;n<=8;n++){
  const base=new Set();let C=0n,M=0n,M2=0n;
  for(const [key,v] of states){base.add(JSON.stringify(JSON.parse(key)[0]));C+=v[0];M+=v[1];M2+=v[2]}
  rows.push({n,B:base.size,F:states.size,C,M,M2});
  logs.push(`PASS word=${w} n=${n} B=${base.size} F=${states.size} C=${C} W=${M} M2=${M2}`);
  if(n===4){
   const key=JSON.stringify([Array(8).fill(0),1]); const z=states.get(key)||[0n,0n,0n];
   info[w+"_witness"]=z;
   logs.push(`FIBER word=${w} n=4 O=(0,0,0,0,0,0,0,0) q=1 C=${z[0]} W=${z[1]} M2=${z[2]}`)
  }
  if(n===8)break;
  const out=new Map();
  for(const [key,v] of states){
    const [o,q]=JSON.parse(key);
    for(let i=0;i<10;i++){
      const L=LAM[i];
      add(out,JSON.stringify([next(o,i),trans(w,q,ORD[i])]),[v[0],v[1]*L,v[2]*L*L])
    }
    if(n===0||q===w.length)add(out,JSON.stringify([next(o,10),0]),v)
  }
  states=out
 }
 info[w]=rows
}
for(let n=0;n<=8;n++){
 const a=info.aab[n],b=info.aba[n];check(a.B===b.B&&a.C===b.C&&a.M===b.M&&a.M2===b.M2,"anagram globals n="+n)
}
check(info.aab[8].B===33295&&info.aab[8].F===58496,"aab n8");
check(info.aba[8].B===33295&&info.aba[8].F===58498,"aba n8");
check(info.aab[8].C===110054001n&&info.aab[8].M===10936007142504414n,"n8 total");
check(info.aab[8].M2===1033374017182766350949291334n,"n8 second moment");
check(info.aab_witness.join()===[2n,72n,2592n].join(),"aab q1");
check(info.aba_witness.join()===[3n,108n,3888n].join(),"aba q1");
logs.push("ANAGRAM_ALL_GLOBAL_TOTALS_EQUAL_N0_TO_N8; FIBER_MASS_CONTRAST_VERIFIED");
logs.push("ALL_CHECKS_PASS");
return logs.join("\n")+"\n";
}
if (typeof module !== 'undefined' && require.main === module) console.log(prefix480_certificate());
