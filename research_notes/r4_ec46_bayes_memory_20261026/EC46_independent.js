'use strict';
// Independent BigInt verification of the displayed EC46 source experiment.
const A=[[24n,8n],[12n,4n],[3n,1n]];
const B=[[1n,3n],[4n,12n],[8n,24n]];
function enumTuples(base,length){const out=[];const go=(a)=>{if(a.length===length){out.push(a.slice());return;}
for(let j=0;j<base;j++){a.push(j);go(a);a.pop();}};go([]);return out;}
const result={};
for(let K=1;K<=3;K++){
 let opt=1n<<62n,patterns=0,optimalWitnesses=0;
 for(const enc of enumTuples(K,3))for(const decision of enumTuples(2,2*K)){
  let err=0n;
  for(let h=0;h<3;h++)for(let y=0;y<2;y++){
   const declareP=BigInt(decision[2*enc[h]+y]);
   err+=A[h][y]*(1n-declareP)+B[h][y]*declareP;
  }
  patterns++;
  if(err<opt){opt=err;optimalWitnesses=1;}
  else if(err===opt)optimalWitnesses++;
 }
 result[String(K)]={minNumerator:String(opt),totalDenominator:'52',checkedPolicies:patterns,optimalWitnesses};
}
const D=A.map((row,h)=>row.map((v,y)=>v-B[h][y]));
const conflict=[];
for(let h=0;h<3;h++)for(let k=h+1;k<3;k++){
 if([0,1].some(y=>D[h][y]*D[k][y]<0n))conflict.push([h,k]);
}
if(result['1'].minNumerator!=='26'||result['2'].minNumerator!=='21'||result['3'].minNumerator!=='16'||conflict.length!==3)throw Error('EC46 independent verification FAIL');
process.stdout.write(JSON.stringify({schema:'EM_R4_EC46_JS_CHECK_V1',result,conflicts:conflict,verified:true},null,2)+'\n');
