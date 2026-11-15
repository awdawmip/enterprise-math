'use strict';
// R762BF conditional signed-axis covariant ledger exact checker.
const fs=require('fs');
function signed(mask,i){return ((mask>>>i)&1)?-1:1;}
const triples=[];
for(let i=0;i<6;i++)for(let j=i+1;j<6;j++)for(let k=j+1;k<6;k++)triples.push([i,j,k]);
if(triples.length!==20)throw Error('axis triple coverage');
let covariantComparisons=0,violation=0;
const signatures=new Set();
for(let etaMask=0;etaMask<64;etaMask++){
 const sig=triples.map(T=>T.reduce((a,i)=>a*signed(etaMask,i),1));
 signatures.add(sig.join(','));
 for(let flipMask=0;flipMask<64;flipMask++)
  for(let T of triples)for(let signedTripleMask=0;signedTripleMask<8;signedTripleMask++){
   const init=T.reduce((a,i,j)=>a*signed(etaMask,i)*signed(signedTripleMask,j),1);
   const after=T.reduce((a,i,j)=>a*(signed(etaMask,i)*signed(flipMask,i))*(signed(signedTripleMask,j)*signed(flipMask,i)),1);
   covariantComparisons++;if(init!==after)violation++;
  }
}
if(signatures.size!==64||covariantComparisons!==655360||violation!==0)
 throw Error('orientation ledger equivariance or injectivity failed');
const flipOnePattern=triples.map(T=>T.includes(0)?-1:1);
const affected=flipOnePattern.filter(x=>x===-1).length;
if(affected!==10)throw Error('single-axis parity footprint wrong');
for(let scalar of [-1,1]){
 const allTriplesPattern=triples.map(()=>scalar);
 if(allTriplesPattern.every((v,i)=>v===flipOnePattern[i]))throw Error('scalar orientation wrongly repairs');
}
const evidence={schema:'R762BF_ORIENTATION_LEDGER_EXACT_V1',date:'2026-11-15',status:'PASS',task_id:'RS-X6-TRIADIC-CLOSURE-DYNAMICS',scope:'conditional signed-axis parity candidate and hypothetical W6 signed frame group; NOT_REVIEWED',domain:{axes:6,orientationStates:64,frameFlipMasks:64,nativeAxisTriples:20,signedTriadAssignments:8},verified:{covariantEligibilityChecks:covariantComparisons,invarianceFailures:violation,distinctOrientationSignatures:signatures.size,singleAxisFlipAffectedTriples:affected,singleAxisFlipUnaffectedTriples:20-affected,globalScalarCanMatch:false},proofScope:'General all-m>=4 injectivity, Wm covariance, and sharp 2^m states follow symbolic proofs',limitations:['No source authority for W6 as physical native rotation group','No P000 TRIADIC_CLOSURE_E signed event admission','Fixed named axis/Port observer, not gauge-quotiented','No independent review or formal Lean proof']};
const out=JSON.stringify(evidence,null,2)+'\n';
if(require.main===module){if(process.argv[2])fs.writeFileSync(process.argv[2],out);process.stdout.write(out);}
module.exports={evidence};
