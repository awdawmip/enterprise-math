'use strict';
// Unit265 exact sample-coupling check; input is immutable Unit264 result JSON.
// Run: node X6_TIME_UNIT265_OPTIMAL_C24_CONTEXT_COUPLING_CHECK_20261122_1655.js <unit264-json>
const fs=require('fs');
const z=JSON.parse(fs.readFileSync(process.argv[2],'utf8'));
if(z.schema!=='X6_TIME_UNIT264_BRC_OPTIMAL_OBSERVER_SEPARATOR_CERT_V1'||z.total_optimal_histories!==5664||z.minimum_steps!==28) throw Error('pinned domain mismatch');
const A=z.observer_support.t3.port60,B=z.observer_support.t3.port82;
const key=a=>a.state.join(',');
const a=new Map(A.map(x=>[key(x),x.count])); const b=new Map(B.map(x=>[key(x),x.count]));
const ks=[...new Set([...a.keys(),...b.keys()])].sort();
if(ks.length!==4||A.reduce((v,x)=>v+x.count,0)!==2832||B.reduce((v,x)=>v+x.count,0)!==2832) throw Error('multiplicity mismatch');
const rows=ks.map(k=>({state:k.split(',').map(Number),port60:a.get(k)||0,port82:b.get(k)||0,matched:Math.min(a.get(k)||0,b.get(k)||0)}));
const l1=rows.reduce((s,x)=>s+Math.abs(x.port60-x.port82),0);
const matched=rows.reduce((s,x)=>s+x.matched,0);
if(l1!==4416||matched!==624||l1+2*matched!==5664) throw Error('coupling mismatch');
const v7=z.observer_support.t7;
const a7=new Set(v7.port60.map(key)),b7=new Set(v7.port82.map(key));
if([...a7].some(k=>b7.has(k)))throw Error('event7 state overlap');
const out={domain:'UNIFORM_2832_OPTIMAL_PATHS_PER_PORT',event3:{rows,l1,denominator:5664,tv:'46/59',max_equal_state_pairs:matched,max_coupling:'13/59'},event7:{overlap:0,tv:'1'},original_native_sensors_executed:false};
console.log(JSON.stringify(out,null,2));
