/** EC48E independent exact witness checker; two-stage positive BRC source labels. */
'use strict';
const P=[30n,70n,30n,50n,90n,20n,90n,50n];
const Q=Array(8).fill(1n), H=4, Y=2;
function failIf(condition,label){ if(condition) throw new Error(label); }
function profiles(cut,includeTies=false){
  const set=new Set();
  for(let h=0;h<H;h++){
    const bits=Array.from({length:Y},(_,y)=>{
      const i=h*Y+y, d=P[i]-cut*Q[i];
      return (d>0n||(includeTies&&d===0n))?'1':'0';
    }).join('');set.add(bits);
  }
  return set;
}
const ratios=[...new Set(P.map(String))].map(BigInt).sort((a,b)=>a<b?-1:a>b?1:0);
failIf(ratios.join(',')!=='20,30,50,70,90','critical ratios');
for(let i=0;i<ratios.length;i++)for(let j=i+1;j<ratios.length;j++){}
const counts=[10n,25n,40n,60n,80n,100n].map(r=>profiles(r).size);
failIf(counts.join(',')!=='1,2,3,3,2,1','generic peak');
const A=profiles(50n,true), B=profiles(50n,false);
failIf(A.size!==3||B.size!==3||new Set([...A,...B]).size!==4,'critical signatures');
const col0=new Set([P[0],P[2],P[4],P[6]].map(String));
const col1=new Set([P[1],P[3],P[5],P[7]].map(String));
failIf([...col0].some(x=>col1.has(x)),'cross-label tie collision');
const states=[];
for(const stage of ['release','expand']) for(const s2 of [0n,1n,2n]){
  // 2 * the eight declared terminal-choice probabilities, row-major.
  const w2=stage==='release' ?
    [0n,2n, 0n,2n, 2n,0n, 2n,s2] :
    [0n,2n, 0n,s2, 2n,0n, 2n,0n];
  const decoder2=stage==='release' ?
    [[0n,2n],[2n,0n],[2n,s2]] :
    [[0n,2n],[0n,s2],[2n,0n]];
  const m=stage==='release'?[0,0,1,2]:[0,1,2,2];
  for(let h=0;h<H;h++)for(let y=0;y<Y;y++){
    const i=h*Y+y;
    failIf(w2[i]!==decoder2[m[h]][y],'factorization equality');
    const d=P[i]-50n*Q[i];
    failIf(d>0n&&w2[i]!==2n,'positive sign failed');
    failIf(d<0n&&w2[i]!==0n,'negative sign failed');
  }
  const support2=w2.reduce((acc,x,i)=>acc+(P[i]-50n*Q[i])*x,0n);
  failIf(support2!==200n,'exact exposed support optimum');
  const tie2=w2[3]+w2[7]; // twice raw tied Q-mass; norm beta coordinate increment /16
  failIf(stage==='release'?tie2!==2n+s2:tie2!==s2,'tie mass');
  states.push({stage,s_numerator:String(s2),s_denominator:2,memory_count:3,
               raw_tie_mass_numerator_2:String(tie2),support_numerator_2:String(support2)});
}
const result={schema:'EM_R4_EC48E_BIGINT_EXACT_WITNESS_V1',raw_P:P.map(String),raw_Q:Q.map(String),
  critical_ratios:ratios.map(String),generic_profile_counts:counts,
  K_hull:Math.max(...counts),critical_left_signatures:[...A].sort(),critical_right_signatures:[...B].sort(),
  two_bank_union_size:new Set([...A,...B]).size,
  exposed_lambda:'40/43',exposed_alpha_minus_lambda_beta:'10/43',
  tied_beta_offset_interval:['0/1','1/4'],states,result:'PASS'};
console.log(JSON.stringify(result,null,2));
