"use strict";
const fs=require('fs'), {verifyR1}=require('./verify_portable.js');
const input=JSON.parse(fs.readFileSync('portable_input.json','utf8'));
const original=JSON.parse(fs.readFileSync('certificate.json','utf8'));
const clone=x=>JSON.parse(JSON.stringify(x));
let checked=0;
for(const change of [x=>x.nodes[0].options.pop(),x=>x.nodes[0].floor_witness.remainder='1',x=>x.nodes[0].options[0].partial_after=['0','1'],x=>x.nodes.push(clone(x.nodes[0])),x=>x.nodes[0].options.reverse()]){
  const altered=clone(original);change(altered);let rejected=false;
  try{verifyR1(input,altered);}catch(e){rejected=true;}
  if(!rejected)throw Error('Mutated proof accepted');checked++;
}
console.log(JSON.stringify({status:'AUTHOR_PORTABLE_TAMPER_CHECK_PASS',rejected_mutations:checked}));
