// R4-EC45 exact source-multiplicity enumeration (no dependencies; Node.js)
const P=[20,10,1],Q=[1,10,20],A=['P','Q','C'];
function words(n,alphabet){if(!n)return [[]];return words(n-1,alphabet).flatMap(w=>alphabet.map(x=>[...w,x]));}
function run(K){
 let best=Infinity,seen=0,ties=0,witness=null;
 for(const mem of words(3,[...Array(K).keys()]))
 for(const stage2 of words(K,A))
 for(const terminal of words(2*K,['P','Q'])){
  seen++;let score=124;
  for(let i=0;i<3;i++){
   const m=mem[i],action=stage2[m];
   if(action==='P')score+=10*Q[i];
   else if(action==='Q')score+=10*P[i];
   else {
    score+=P[i]+Q[i];
    for(let z=0;z<2;z++) score+=terminal[2*m+z]==='P'?Q[i]*(z?9:1):P[i]*(z?1:9);
   }
  }
  if(score<best){best=score;ties=1;witness={mem,stage2,terminal}}
  else if(score===best)ties++;
 }
 return {K,enumerated:seen,optimal_plans:ties,best_numerator_over_310:best,witness};
}
const rows=[1,2,3].map(run);
if(rows.map(x=>x.best_numerator_over_310).join(',')!=='248,216,184') throw Error('wrong minima');
if(rows.map(x=>x.enumerated).join(',')!=='12,1152,46656')throw Error('wrong enumeration');
console.log(JSON.stringify({schema:'EM_R4_EC45_JS_V1',passed:true,total:rows.reduce((s,x)=>s+x.enumerated,0),rows}));
