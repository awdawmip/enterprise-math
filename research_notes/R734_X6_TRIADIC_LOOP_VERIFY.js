function verify(){
 const A=(v,msg)=>{if(!v)throw Error(msg)};
 const p=(a)=>a.length? a.flatMap((x,i)=>p(a.slice(0,i).concat(a.slice(i+1))).map(rest=>[x,...rest])):[[]];
 const steps=[[0,1],[0,-1],[1,1],[1,-1],[2,1],[2,-1]], words=p(steps);
 const first=(w)=>{const z=[0,0,0];for(let i=0;i<w.length;i++){z[w[i][0]]+=w[i][1];if(z.every(x=>x===0))return i+1}return null};
 const nb=(w)=>w.every((x,i)=>i===0||!(x[0]===w[i-1][0]&&x[1]===-w[i-1][1]));
 const sig=(w)=>{const x=[0,0,0];for(const [a,b] of w)if(!x[a])x[a]=b;return x.map(v=>v===1?"+":"-").join("")};
 const ret={2:0,4:0,6:0}, f6={}, fnb={};
 A(words.length===720,"word count");
 for(const w of words){const t=first(w),s=sig(w);A(t===2||t===4||t===6,"return");ret[t]++;if(t===6)f6[s]=(f6[s]||0)+1;if(nb(w)){A(t===6,"NB first return");fnb[s]=(fnb[s]||0)+1}}
 A(ret[2]===144&&ret[4]===96&&ret[6]===480,"return distribution");
 A(Object.keys(fnb).length===8&&Object.values(fnb).every(v=>v===30),"30 each signature");
 A(Object.values(f6).every(v=>v===60),"60 each signature");
 const orbit={};
 for(let bit=0;bit<8;bit++){
  const s=[0,1,2].map(i=>bit&(1<<i)?"-":"+").join("");
  const H=p([0,1,2]).filter(a=>[0,1,2].every(i=>s[i]===s[a[i]]));
  const fiber=new Set(words.filter(w=>nb(w)&&sig(w)===s).map(w=>JSON.stringify(w)));
  let count=0;
  while(fiber.size){const w=JSON.parse(fiber.values().next().value),q=new Set(H.map(h=>JSON.stringify(w.map(([i,v])=>[h[i],v]))));
   A(q.size===H.length,"free action");for(const v of q)A(fiber.delete(v),"invariant fiber");count++;
  }
  A(count*H.length===30,"orbit count");
  orbit[s]={stabilizer_order:H.length,min_equivariant_branch_count:H.length,orbit_count:count};
 }
 return {schema:"R734_X6_TRIADIC_LOOP_BRC_CERT_V1",status:"PASS",date_local:"2026-11-12",source_science:"a72226e2430ffa4786321ac86e7f0c599d5f0389",
 scope:"Signed native X6 pure coordinate adjacency; six-step positive N-BRC branch census with three distinct axes, each + and - once. First occurrence defines source sign. Physical closure predicate and V29/V39 native scheduler are external typed inputs.",
 first_return_counts:ret,nonbacktracking_one_axis_triple:240,nonbacktracking_per_signed_triad:30,first_return_six_per_signed_triad:60,
 totals:{axis_triples:20,signed_triads:160,six_step_words:14400,first_return_six_words:9600,nonbacktracking_words:4800},
 stabilizer_orbits:orbit,physical_force_closure_verified:false,native_V29_V39_verified:false,
 marker:"R734_X6_TRIADIC_LOOP_BRC_EXACT_PASS"};
}
console.log(JSON.stringify(verify(),null,2));
