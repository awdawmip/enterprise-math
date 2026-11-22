/* Unit260 exact checker: run node <this-file> [relative-path-to-original-Unit245-JSON]. No network or extra dependencies. */
'use strict';
const fs=require('node:fs');
function verify(d){
  let assertions=0;
  function ok(v, msg){assertions++;if(!v)throw Error("CHECK_FAILED: "+msg);}
  const indexOf=(ch)=>ch.toLowerCase().charCodeAt(0)-97;
  function audit(route,i,j,withOther){
    const pos=withOther?[0,2]:[0,null],wind=[0,0],enter=[0,0],exit=[0,0],clock=[0,0],counter=[0,0],events=[0,0];
    for(const ch of route){
      const who=(ch===ch.toUpperCase())?0:1,dest=indexOf(ch),src=pos[who];
      ok(src!==null&&dest>=0&&dest<=12,"valid actor,destination");
      if(withOther)ok(dest!==pos[1-who],"exclusive Cell");
      if(src===12){ok(dest===j,"only center egress");exit[who]++;}
      else if(dest===12){ok(src===i,"only center ingress");enter[who]++;}
      else if(dest===(src+1)%12){wind[who]++;if(src===11)clock[who]++;}
      else if(dest===(src+11)%12){wind[who]--;if(src===0)counter[who]++;}
      else throw Error("invalid ring edge "+src+"->"+dest);
      pos[who]=dest;events[who]++;
    }
    for(let t=0;t<(withOther?2:1);t++){
      ok(enter[t]===exit[t],"closed center visits");
      ok(wind[t]===enter[t]*(i-j)+12*(clock[t]-counter[t]),"signed winding conservation");
      ok(pos[t]===(t===0?0:2),"source Cell return");
    }
    return {wind,enter,clock,counter,events};
  }
  ok(d.cases.length===36,"original 36 cases");
  let auditedEvents=0;
  const rows=[];
  for(const c of d.cases){
    ok(c.ingress%2===0&&c.egress%2===0,"even center Ports");
    const a=audit(c.route,c.ingress,c.egress,true);
    ok(a.wind[0]===-12&&a.wind[1]===12,"both signed winding targets");
    ok(a.events[0]+a.events[1]===c.cost,"original event length");
    if(c.ingress>=c.egress)ok(a.counter[0]>=1,"universal negative wrap necessary");
    if(c.ingress===6&&c.egress===0)ok(a.enter[0]===2&&a.counter[0]===2&&a.clock[0]===0,"optimal 6,0");
    if(c.ingress===8&&c.egress===2)ok(a.enter[0]===0&&a.counter[0]===1&&a.clock[0]===0,"optimal 8,2");
    auditedEvents+=c.cost;
    rows.push({ingress:c.ingress,egress:c.egress,source_cost:c.cost,A:{center_traversals:a.enter[0],clockwise_wraps:a.clock[0],counterclockwise_wraps:a.counter[0],winding:a.wind[0]},B:{center_traversals:a.enter[1],clockwise_wraps:a.clock[1],counterclockwise_wraps:a.counter[1],winding:a.wind[1]}});
  }
  ok(auditedEvents===1312,"original total event count");
  function gcd(a,b){return b?gcd(b,a%b):a;}
  const bypass=[];
  for(let i=0;i<=10;i+=2)for(let j=i+2;j<=10;j+=2){
    const g=gcd(12,j-i),R=12/g,K=(j-i)/g-1,stops=[];
    for(let k=1;k<=i;k++)stops.push(k);
    for(let n=0;n<R;n++){
      stops.push(12,j);
      const endpoint=(n<R-1?i:0);
      for(let k=j-1;k>=endpoint;k--)stops.push(k);
    }
    for(let l=0;l<K;l++)for(let k=1;k<=12;k++)stops.push(k%12);
    const route=stops.map(s=>String.fromCharCode(65+s)).join("");
    const v=audit(route,i,j,false);
    ok(v.wind[0]===-12&&v.counter[0]===0&&v.enter[0]===R&&v.clock[0]===K,"constructive negative-wrap bypass");
    bypass.push({ingress:i,egress:j,center_traversals:R,clockwise_wraps:K,negative_wraps:0,path_length:route.length,route});
  }
  ok(bypass.length===15,"15 converse single-triad ports");
  const universalCut=rows.filter(v=>v.ingress>=v.egress).length;
  ok(universalCut===21,"21/36 universal A directed wrap edge cases");
  return {schema:"X6_TIME_UNIT260_GLOBAL_WINDING_CUT_CERT_V1",original_source:{commit:"f56840285cafeb9f5767ea91e903e1f53808186f",path:"research_checks/X6_TIME_UNIT245_DIRECTED_CENTER_PORT_PAIR_RESULTS_20261121_2200.json",git_blob_sha1:"113d2102fe393bfd6f77bf7cca093b4cecf6796f"},frozen_P000:"a72226e2430ffa4786321ac86e7f0c599d5f0389",identity:"W_T=R_T*(i-j)+12*(U_T-D_T)",port_count:36,original_events_audited:auditedEvents,universal_negative_A_wrap_ports:universalCut,converse_A_only_constructive_ports:bypass.length,all_original_routes:rows,constructive_single_triad_bypasses:bypass,assertions_checked:assertions,failed:0,native_physical_event_executed:false,independent_review:false,formal_admission:false};
}
const originalPath=process.argv[2]||'research_checks/X6_TIME_UNIT245_DIRECTED_CENTER_PORT_PAIR_RESULTS_20261121_2200.json';
const certificate=verify(JSON.parse(fs.readFileSync(originalPath,'utf8')));
process.stdout.write(JSON.stringify(certificate,null,2)+'\n');
