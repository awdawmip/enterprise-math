"use strict";
// Unit251: exact historical BRC route replay and finite C24 inverse observer check.
// This is conditional mathematics; no physical Cell/Port update or C24 sensor is executed.
const result = (function runCheck() {
  "use strict";
  let assertions=0;
  function ok(cond,msg){assertions++;if(!cond)throw new Error(msg)}
  function mod(x,n){return ((x%n)+n)%n}
  function gcd(a,b){return b?gcd(b,a%b):a}
  function crt(v8,v3){for(let x=0;x<24;x++)if(x%8===v8&&x%3===v3)return x;throw Error("CRT")}
  const ports=[0,2,4,6,8,10], ringG=Array(12).fill(0);ringG[5]=3;ringG[10]=3;
  const sourceRows=[[0,0,1],[0,2,6],[0,4,3],[0,6,2],[0,8,3],[0,10,6],[2,0,6],[2,2,1],[2,4,6],[2,6,3],[2,8,2],[2,10,3],[4,0,3],[4,2,6],[4,4,1],[4,6,6],[4,8,3],[4,10,2],[6,0,2],[6,2,3],[6,4,6],[6,6,1],[6,8,6],[6,10,3],[8,0,3],[8,2,2],[8,4,3],[8,6,6],[8,8,1],[8,10,6],[10,0,6],[10,2,3],[10,4,2],[10,6,3],[10,8,6],[10,10,1]];
  const sourceRoutes=[
    {ingress:0,egress:2,cost:38,route:"MdCBAMCBAMCBAMCBAMCBAMefghijklabcdCBAc",firstExit:3},
    {ingress:2,egress:4,cost:46,route:"BdCMefEDCMEDCMEDCMEDCMEDCMghijklabcdefEDCBAedc",firstExit:7}
  ];
  ok(sourceRows.length===36,"source covers 36 cases");
  for(const [i,j,c] of sourceRows)ok(c===12/gcd(12,mod(j-i,12)),"source count mismatch "+i+"/"+j);
  function replay(item,alpha,beta){
    const pos={A:0,B:2}, winding={A:0,B:0}, ring={A:0,B:0}, precision={A:0,B:0}, visits={A:0,B:0};
    let first=null, lastCentre={A:false,B:false}, signedEvents=0, centreEvents=0;
    for(let n=0;n<item.route.length;n++){
      const z=item.route[n], who=z>="A"&&z<="M"?"A":"B";
      const to=z.charCodeAt(0)-(who==="A"?65:97);
      const from=pos[who],other=who==="A"?"B":"A";
      ok(to>=0&&to<=12,"typed destination at event "+n);
      ok(to!==pos[other],"Cell exclusion at event "+n);
      if(to===12){
        ok(from===item.ingress,"ingress at event "+n);
        lastCentre[who]=true;precision[who]=mod(precision[who]+alpha[item.ingress/2],24);centreEvents++;
      }else if(from===12){
        ok(lastCentre[who]&&to===item.egress,"egress at event "+n);
        lastCentre[who]=false;precision[who]=mod(precision[who]+beta[item.egress/2],24);centreEvents++;
        visits[who]++;
        if(!first)first={event_index:n+1,triad:who,cell:"x"+to,delta_C24:precision[who],ring_delta_C24:ring[who],passages:visits[who]};
      }else{
        ok(to===mod(from+1,12)||to===mod(from-1,12),"signed native ring step "+n);
        const direction=to===mod(from+1,12)?1:-1;
        winding[who]+=direction;
        const delta=direction===1?ringG[from]:-ringG[to];
        ring[who]=mod(ring[who]+delta,24);
        precision[who]=mod(precision[who]+delta,24);
        signedEvents++;
      }
      pos[who]=to;
    }
    ok(item.route.length===item.cost,"original minimal-event route cost");
    ok(pos.A===0&&pos.B===2,"exact return to labelled original Cells");
    ok(winding.A===-12&&winding.B===12,"exact signed BRC windings");
    ok(visits.A===6&&visits.B===0,"six passages by A, none by B");
    ok(first&&first.event_index===item.firstExit&&first.triad==="A","first exit location");
    ok(first.ring_delta_C24===0,"first passage has zero A ring calibration contribution");
    ok(centreEvents===12&&signedEvents===item.cost-12,"12 signed centre events");
    return {ingress:item.ingress,egress:item.egress,route_length:item.cost,first_exit_event:first.event_index,first_triad:first.triad,first_cell:first.cell,first_C24:first.delta_C24,first_ring_C24:first.ring_delta_C24,centre_passages_A:visits.A,terminal_C24:precision,signed_ring_winding:winding};
  }
  const classes=[];
  for(const parity of [0,4])for(let p=0;p<3;p++)for(let q=0;q<3;q++){
    const r=[0,p,q], alpha=ports.map((_,k)=>crt(k%2?parity:0,r[k%3]));
    const beta=alpha.map(x=>mod(-x,24));
    for(const [i,j,c] of sourceRows)ok(mod(c*(alpha[i/2]+beta[j/2]),24)===0,"source terminal indistinguishability");
    classes.push({parity,p,q,alpha,beta});
  }
  ok(classes.length===18,"18 mod-gauge distinct law classes");
  const zero=Array(6).fill(0);
  const base=sourceRoutes.map(r=>replay(r,zero,zero));
  ok(base[0].first_exit_event===3&&base[1].first_exit_event===7,"readout positions 3 and 7");
  const cohort=classes.map(l=>({law:l,reads:sourceRoutes.map(r=>replay(r,l.alpha,l.beta))}));
  for(const row of cohort){
    ok(row.reads.every((r,k)=>r.terminal_C24.A===base[k].terminal_C24.A&&r.terminal_C24.B===base[k].terminal_C24.B),"both terminal readings unchanged within 36-route kernel");
    for(let k=0;k<2;k++)ok(row.reads[k].first_C24===mod(row.law.alpha[sourceRoutes[k].ingress/2]+row.law.beta[sourceRoutes[k].egress/2],24),"first exit reads exact centre weight");
  }
  const afterOne=cohort.filter(r=>r.reads[0].first_C24===base[0].first_C24);
  const afterTwo=afterOne.filter(r=>r.reads[1].first_C24===base[1].first_C24);
  ok(afterOne.length===3&&afterTwo.length===1,"18 -> 3 -> 1 identifiability");
  ok(afterTwo[0].law.alpha.every(x=>x===0),"only global gauge survives");
  const oneScalarMin=Math.min(...ports.flatMap(i=>ports.map(j=>classes.filter(l=>mod(l.alpha[i/2]+l.beta[j/2],24)===0).length)));
  ok(oneScalarMin===3,"one passage scalar leaves at least three law classes");
  const localNonstationaryPassageIncrements=[8,16,0,0,0,0];
  ok(localNonstationaryPassageIncrements.reduce((x,y)=>x+y,0)%24===0,"dynamic residual cancels at endpoint");
  ok(localNonstationaryPassageIncrements[0]!==localNonstationaryPassageIncrements[1],"prefix read detects time-varying residual");
  const result={
    schema:"X6_UNIT251_IN_TRACE_BRC_C24_SENSOR_CERT_V1",date:"2026-11-22",unit:"Unit251",task_id:"RS-X6-NATIVE-TIME-DYNAMICS",
    source_provenance:{
      frozen_p000:"a72226e2430ffa4786321ac86e7f0c599d5f0389",
      original_route_commit:"f56840285cafeb9f5767ea91e903e1f53808186f",
      original_route_path:"research_checks/X6_TIME_UNIT245_DIRECTED_CENTER_PORT_PAIR_RESULTS_20261121_2200.json",
      unit250_inverse_commit:"33dd0d808ec8733b2147fa5905481b869938a7a1"
    },modulus:24,original_terminal_observer_cases:36,original_route_cases_replayed:2,
    original_replay:base,source_terminal_kernel_up_to_gauge:classes.length,
    remaining_laws_after_first_in_trace_read:afterOne.length,
    remaining_laws_after_both_in_trace_reads:afterTwo.length,
    minimal_extra_scalar_samples_for_linear_additive_law:2,
    extra_native_movement_events_when_original_routes_already_run:0,
    required_extra_noninvasive_mid_trace_C24_samples:2,
    dynamic_counterexample:{same_port_pair:[0,2],six_passage_residuals_C24:localNonstationaryPassageIncrements,terminal_sum_C24:0,first_mid_trace_residual_C24:8},
    exact_integer_assertions:assertions,mismatch_count:0,
    scope:"conditional signed BRC Port/precision model, exact historical certificate replay; no Source-qualified physical Port or sensor operation"
  };
  return result;
})();
if (typeof module !== "undefined" && typeof require !== "undefined" && require.main === module)
  console.log(JSON.stringify(result,null,2));
