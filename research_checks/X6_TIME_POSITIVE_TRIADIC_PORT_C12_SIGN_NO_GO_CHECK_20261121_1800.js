"use strict";
// Unit240: compare frozen source-possible X6 C12 microtraces with the later
// positive-port single-triad candidate, then test an explicitly conditional signed extension.
const a=[[1,0,0], [0,1,0], [0,0,1],[-1,0,0],[0,-1,0],[0,0,-1]];
const mod=x=>(x%6+6)%6;
const add=(x,y)=>x.map((v,i)=>v+y[i]);
const neg=x=>x.map(v=>-v);
const eq=(x,y)=>x.every((v,i)=>v===y[i]);
let assertions=0,events=0,negativeEvents=0;
function check(b,msg){assertions++;if(!b)throw Error(msg);}
const tables=[];
for(let W=1;W<=2;W++){
  const L=6*W, choices=2**L, numHist=2*choices;
  let paths=0,closed=0,fullyOuter=0,positiveOnlyFailed=0;
  for(let eps of [-1,1])for(let mask=0;mask<choices;mask++){
    let state=a[0].slice(),r=0,pos=0,negative=0;
    const trace=[state.slice()], orderedSteps=[];
    for(let t=0;t<L;t++){
      let b=a[mod(r+eps)], u=a[r], outer=(mask>>t)&1;
      let micro=outer?[b,neg(u)]:[neg(u),b];
      for(let s of micro){
        let signedSupport=s.filter(v=>v!==0);
        check(signedSupport.length===1 && Math.abs(signedSupport[0])===1,'signed primitive port');
        const axis=s.findIndex(v=>v!==0);
        check(axis>=0 && axis<3,'triad frame contains step axis');
        // Mobile positive triad F=(E1,E2,E3) is carried intact; target is empty
        // because there is exactly one occupied Cell at any stage.
        state=add(state,s);trace.push(state.slice());orderedSteps.push(s.slice());
        if(s[axis]===1)pos++;else negative++;
        events++;
      }
      check(eq(state,b),'macro endpoint');r=mod(r+eps);
    }
    check(r===0 && eq(state,a[0]),'exact Cell and triad return');
    check(pos===6*W && negative===6*W,'exact signed direction balance');
    const counts=[0,0,0],reverseCounts=[0,0,0];
    for(const s of orderedSteps){let axis=s.findIndex(v=>v!==0);if(s[axis]>0)counts[axis]++;else reverseCounts[axis]++;}
    for(let i=0;i<3;i++){check(counts[i]===2*W && reverseCounts[i]===2*W,'two of each signed axis per loop');}
    // Conditional signed-transfer reverse is valid with the same one mobile triad.
    let reversed=state.slice();for(let i=orderedSteps.length-1;i>=0;i--)reversed=add(reversed,neg(orderedSteps[i]));
    check(eq(reversed,a[0]),'reverse path returns');
    paths++;closed++;negativeEvents+=negative;
    if(negative>0)positiveOnlyFailed++;
    if(mask===choices-1)fullyOuter++;
  }
  check(paths===numHist && closed===numHist,'all BRC histories enumerated');
  check(positiveOnlyFailed===numHist,'every closed signed Cell trace fails the positive-only port alphabet');
  check(fullyOuter===2,'unique all-outer word per chirality');
  tables.push({W,full_branch_histories:paths,positive_only_realizable_full_cycles:0,signed_single_mobile_triad_realizable_cycles:closed,positive_port_events_per_cycle:6*W,negative_port_events_per_cycle:6*W,needed_negative_axis_types:3,all_outer_phase_refined_cycles:fullyOuter});
}
console.log(JSON.stringify({schema:'X6_TRIADIC_POSITIVE_PORT_C12_SIGN_OBSTRUCTION_CERT_V1',unit:'Unit240',frozen_source:'a72226e2430ffa4786321ac86e7f0c599d5f0389',separate_later_candidate_source:'f41c2690daba467ecbde99615a1337e67be46ffd:X6_TIME_GUARDED_TRIADIC_RESOURCE_CONFLICT_20261118.md',scope:'one mobile positive ordered triad, positive-only transfer vs explicitly conditional signed bidirectional port extension',tables,primitive_event_instances_checked:events,negative_port_instances:negativeEvents,integer_assertions:assertions,failed_assertions:0,physical_admission:'NOT_CLAIMED; conditional source-model discrimination only'},null,2));
