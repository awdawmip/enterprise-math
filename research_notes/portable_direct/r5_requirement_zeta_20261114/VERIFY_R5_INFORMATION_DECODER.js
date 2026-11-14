// Verify R5 observer-class partition from pinned integer cohort data.
// Usage: node VERIFY_R5_INFORMATION_DECODER.js
// Requires only a standard Node.js runtime and the adjacent pinned JSON.
"use strict";
const fs=require("node:fs");
const path=require("node:path");
const data=JSON.parse(fs.readFileSync(path.join(__dirname,"EXACT_R5_REQUIREMENT_ZETA.json"),"utf8"));
function classify(data){
  if(data.frozen_events!==954||data.frozen_cuts!==28||data.frozen_science_pin!=="435e77af0d180eac32bd1f9c4c464bc4010b7551")throw Error("Wrong frozen instance");
  const rows=data.coefficients; if(rows.length!==24)throw Error("Expected 24 budget rows");
  const out=[], maskFactor=1n<<26n,total=1n<<28n;
  for(let k=292;k<=315;k++){
    const w=rows[k-292];if(w.K!==k||w.J!==1620-3*k||w.N_both_equals_N_all!==true)throw Error("Budget/source mismatch "+k);
    const a=BigInt(w.a_empty),b=BigInt(w.a_15),c=BigInt(w.a_17),d=BigInt(w.a_15_17);
    if(a<=0n||b<0n||c<0n||d<0n)throw Error("Invalid cohort "+k);
    const values=[a,a+b,a+c,a+b+c+d], frequency=new Map();
    for(const v of values){const s=v.toString();frequency.set(s,(frequency.get(s)||0)+1);}
    const distinct=frequency.size;
    const kind=k===292||k===315?"invariant":k===293||k===314?"single-cut-tie":"strict-order";
    if(kind==="invariant" && !(b===0n&&c===0n&&d===0n&&distinct===1))throw Error("Invariant failure "+k);
    if(kind==="single-cut-tie" && !(b===c&&b>0n&&d===0n&&distinct===3))throw Error("Boundary tie failure "+k);
    if(kind==="strict-order" && !(c>b&&b>0n&&d>0n&&distinct===4&&values[0]<values[1]&&values[1]<values[2]&&values[2]<values[3]))throw Error("Strict decoder failure "+k);
    const parts=[...frequency.values()].sort((x,y)=>x-y);
    const closureClassSizes=parts.map(x=>(BigInt(x)*maskFactor).toString());
    if(closureClassSizes.reduce((s,x)=>s+BigInt(x),0n)!==total)throw Error("Partition failure "+k);
    const familyClasses=kind==="invariant"?1:4;
    const informationHalfBits=kind==="invariant"?0:kind==="single-cut-tie"?3:4;
    out.push({K:k,J:w.J,kind,count_classes:distinct,count_class_sizes:closureClassSizes,optimizer_family_classes:familyClasses,uniform_count_information_half_bits:informationHalfBits,uniform_family_information_half_bits:kind==="invariant"?0:4,cut_17_count_greater_than_cut_15: c>b});
  }
  return {schema:"R5_EXACT_OPTIMIZER_OBSERVER_INFORMATION_V1",status:"PASS_EXACT_R5_INFORMATION_DECODER",model:"derived_radius2_index_center",frozen_science_pin:data.frozen_science_pin,input_commit:"69b0fa35b6c0f191190c66f8d857a175b289370c",input_file:"research_notes/portable_direct/r5_requirement_zeta_20261114/EXACT_R5_REQUIREMENT_ZETA.json",input_blob:"2c6d2ec1e966384d1befd01b5b48825452d5d320",cut_count:28,ignored_cut_count_for_K_ge_292:26,full_mask_count:total.toString(),class_sizes_units:"number_of_distinct_full_28-bit_closure_masks",entropy_units:"half_bits_exact_under_uniform_independent_closures",rows:out,summary:{invariant_budget_values:[292,315],strict_order_budgets:[294,313],single_cut_ties:[293,314],classes_1:out.filter(w=>w.count_classes===1).length,classes_3:out.filter(w=>w.count_classes===3).length,classes_4:out.filter(w=>w.count_classes===4).length}};
}
const result=classify(data);
if(result.status!=="PASS_EXACT_R5_INFORMATION_DECODER")throw Error("Unexpected status");
console.log(JSON.stringify(result,null,2));
