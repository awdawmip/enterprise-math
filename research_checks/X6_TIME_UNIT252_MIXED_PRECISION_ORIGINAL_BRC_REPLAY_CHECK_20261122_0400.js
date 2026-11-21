"use strict";
// Unit252: conditional native-route replay; NO PHYSICAL PORT/SENSOR EXECUTION.
// Immutable Unit245 source commit f56840285cafeb9f5767ea91e903e1f53808186f, blob 113d2102fe393bfd6f77bf7cca093b4cecf6796f.
const ORIGINAL_SOURCE_ROUTES=[{"ingress":0,"egress":0,"cost":30,"route":"BdefghijklamALKJIHGFEDCBALabAc"},{"ingress":0,"egress":2,"cost":38,"route":"MdCBAMCBAMCBAMCBAMCBAMefghijklabcdCBAc"},{"ingress":0,"egress":4,"cost":36,"route":"MdefEDCBAMEDCBAMghijklabcdefEDCBAedc"},{"ingress":0,"egress":6,"cost":38,"route":"BdefghijklamALKJIHGFEDCBghijklamAgfedc"},{"ingress":0,"egress":8,"cost":38,"route":"MdefghijIHGFEDCBAMIHGFEDCBAMIkJlKaLbAc"},{"ingress":0,"egress":10,"cost":46,"route":"LKJIHGFEDbCaBmALKJklamklamklamklamklamklKaLbAc"},{"ingress":2,"egress":0,"cost":38,"route":"LKJIHGFEDmCBALabcmabcmabcmabcmabcmabAc"},{"ingress":2,"egress":2,"cost":30,"route":"LKJIHGFEDbCMcdefghijklabcdCBAc"},{"ingress":2,"egress":4,"cost":46,"route":"BdCMefEDCMEDCMEDCMEDCMEDCMghijklabcdefEDCBAedc"},{"ingress":2,"egress":6,"cost":38,"route":"LKJIHGFEDmghijklabcmghijklabcmCBAgfedc"},{"ingress":2,"egress":8,"cost":38,"route":"LKJIHGFEDbCMIHGFEDCMcdefghijIkJlKaLbAc"},{"ingress":2,"egress":10,"cost":36,"route":"LKJIHGFEDmCBALKJklabcmklabcmklKaLbAc"},{"ingress":4,"egress":0,"cost":32,"route":"LKJIHGFdemEDCBALabcdemabcdemabAc"},{"ingress":4,"egress":2,"cost":36,"route":"LKJIHGFdemEDCBAcdemcdemcdemcdemcdemc"},{"ingress":4,"egress":4,"cost":32,"route":"LKJIHGFEMdefghijklabcdefEDCBAedc"},{"ingress":4,"egress":6,"cost":48,"route":"LKJIHGFEMGFEMGFEMGFEMGFEMGFEMdefghGiHjIkJlKaLbAc"},{"ingress":4,"egress":8,"cost":38,"route":"LKJIHGFEMIHGFEMIHGFEMdefghijIkJlKaLbAc"},{"ingress":4,"egress":10,"cost":32,"route":"LKJIHGFEMKJIHGFEMdefghijklKaLbAc"},{"ingress":6,"egress":0,"cost":28,"route":"LKJIHGMALKJIHGMdefghijklabAc"},{"ingress":6,"egress":2,"cost":30,"route":"LKJIHdefgmGFEDCBAcdefgmcdefgmc"},{"ingress":6,"egress":4,"cost":40,"route":"LKJIHdefgmGFEDCBAefgmefgmefgmefgmefgmedc"},{"ingress":6,"egress":6,"cost":36,"route":"LKJIHGMdefghijklabcdefghGFEDCBAgfedc"},{"ingress":6,"egress":8,"cost":44,"route":"LKJIHGMIHGMIHGMIHGMIHGMIHGMdefghijIkJlKaLbAc"},{"ingress":6,"egress":10,"cost":34,"route":"LKJIHGMKJIHGMKJIHGMdefghijklKaLbAc"},{"ingress":8,"egress":0,"cost":30,"route":"LKJIMALKJIMALKJIMdefghijklabAc"},{"ingress":8,"egress":2,"cost":28,"route":"LKJdefghimIHGFEDCBAcdefghimc"},{"ingress":8,"egress":4,"cost":34,"route":"LKJdefghimIHGFEDCBAefghimefghimedc"},{"ingress":8,"egress":6,"cost":44,"route":"LKJdefghimIHGFEDCBAghimghimghimghimghimgfedc"},{"ingress":8,"egress":8,"cost":36,"route":"LKJdefghimIHGFEDCBALKJIHijIkJlKaLbAc"},{"ingress":8,"egress":10,"cost":40,"route":"LKJIMKJIMKJIMKJIMKJIMKJIMdefghijklKaLbAc"},{"ingress":10,"egress":0,"cost":36,"route":"LKMALKMALKMALKMALKMALKMdefghijklabAc"},{"ingress":10,"egress":2,"cost":32,"route":"LKMdCBALKMCBALKMefghijklabcdCBAc"},{"ingress":10,"egress":4,"cost":32,"route":"LdefghijkmKJIHGFEDCBAefghijkmedc"},{"ingress":10,"egress":6,"cost":38,"route":"LdefghijkmKJIHGFEDCBAghijkmghijkmgfedc"},{"ingress":10,"egress":8,"cost":48,"route":"LdefghijkmKJIHGFEDCBAijkmijkmijkmijkmijkmihgfedc"},{"ingress":10,"egress":10,"cost":32,"route":"LdefghijkmKJIHGFEDCBALKJklKaLbAc"}];
const check=function check(cases){
  "use strict";
  let assertions=0;const ok=(v,m)=>{assertions++;if(!v)throw Error(m)};const md=(x,n)=>(x%n+n)%n;
  const gcd=(a,b)=>b?gcd(b,a%b):a;
  function crt(a,b){for(let x=0;x<24;x++)if(x%8===a&&x%3===b)return x;throw Error("CRT")}
  let classes=[];
  for(let t of [0,4])for(let p=0;p<3;p++)for(let q=0;q<3;q++){
   const r=[0,p,q],a=Array.from({length:6},(_,k)=>crt(k%2?t:0,r[k%3]));
   classes.push({t,p,q,a,b:a.map(v=>md(-v,24))});
  }
  const f=c=>md(c.a[0]+c.b[1],24),g=c=>md(c.a[1]+c.b[2],24);
  const nuniq=items=>new Set(items.map(x=>JSON.stringify(x))).size;
  ok(classes.length===18,"18 kernel classes");
  for(let c of classes)for(let i=0;i<6;i++)for(let j=0;j<6;j++){
   const count=12/gcd(12,md(2*(j-i),12));
   ok(md(count*(c.a[i]+c.b[j]),24)===0,"all 36 source terminal observations");
  }
  ok(nuniq(classes.map(f))===6,"C24 first six symbols");
  ok(nuniq(classes.map(c=>md(f(c),12)))===3,"C12 first three symbols");
  ok(nuniq(classes.map(c=>md(f(c),8)))===2,"C8 first two symbols");
  ok(nuniq(classes.map(c=>md(g(c),3)))===3,"C3 second three symbols");
  ok(nuniq(classes.map(c=>[f(c),md(g(c),3)]))===18,"C24+C3 full rank");
  ok(nuniq(classes.map(c=>[md(f(c),12),md(g(c),12)]))===9,"C12+C12 incomplete");
  const odd=[0,12,0,12,0,12],zero=Array(6).fill(0),G=Array(12).fill(0);G[5]=3;G[10]=3;
  function replay(o,a,b){
   let pos={A:0,B:2},L={A:0,B:0},P={A:0,B:0},timeline=[];
   for(let k=0;k<o.route.length;k++){
    let z=o.route[k],who=z>="A"&&z<="M"?"A":"B",other=who==="A"?"B":"A";
    let to=z.charCodeAt(0)-(who==="A"?65:97),from=pos[who],inc;
    ok(to>=0&&to<=12,"typed Cell");ok(to!==pos[other],"exclusion");
    if(to===12){ok(from===o.ingress,"ingress");inc=a[o.ingress/2]}
    else if(from===12){ok(to===o.egress,"egress");inc=b[o.egress/2]}
    else {
     let sign=to===md(from+1,12)?1:to===md(from-1,12)?-1:0;
     ok(sign!==0,"signed primitive step");L[who]+=sign;inc=sign===1?G[from]:-G[to];
    }
    P[who]=md(P[who]+inc,24);pos[who]=to;
    timeline.push({who,cell:to,A:P.A,B:P.B});
   }
   ok(pos.A===0&&pos.B===2&&L.A===-12&&L.B===12,"native return and signed winding");
   ok(o.cost===o.route.length,"source route length");
   return {P,timeline};
  }
  let totalEvents=0;
  for(let o of cases){
   const base=replay(o,zero,zero),alt=replay(o,odd,odd);totalEvents+=o.route.length;
   ok(base.P.A===alt.P.A&&base.P.B===alt.P.B,"original C24 terminal blind");
   for(let k=0;k<o.route.length;k++){
    ok(md(base.timeline[k].A-alt.timeline[k].A,12)===0,"all prefixes A C12 blind");
    ok(md(base.timeline[k].B-alt.timeline[k].B,12)===0,"all prefixes B C12 blind");
   }
  }
  let a=cases.find(o=>o.ingress===0&&o.egress===2),b=cases.find(o=>o.ingress===2&&o.egress===4);
  ok(!!a&&!!b&&a.cost===38&&b.cost===46,"selected existing routes");
  let ta=replay(a,zero,zero).timeline[2],tb=replay(b,zero,zero).timeline[6];
  ok(ta.who==="A"&&ta.cell===2,"original event 3");
  ok(tb.who==="A"&&tb.cell===4,"original event 7");
  return {
    schema:"X6_UNIT252_MIXED_RESOLUTION_SENSOR_CERT_V1",date:"2026-11-22",
    task:"RS-X6-NATIVE-TIME-DYNAMICS",frozen_p000:"a72226e2430ffa4786321ac86e7f0c599d5f0389",
    original_unit245_commit:"f56840285cafeb9f5767ea91e903e1f53808186f",
    original_unit245_blob:"113d2102fe393bfd6f77bf7cca093b4cecf6796f",
    original_route_cases_replayed:cases.length,ordered_signed_events_replayed:totalEvents,
    source_terminal_fibre_up_to_centre_gauge:18,
    initial_C24_symbol_count:6,initial_C12_symbol_count:3,
    initial_C8_symbol_count:2,final_C3_symbol_count:3,
    C24_plus_C3_joint_classes:18,C12_plus_C12_joint_classes:9,
    minimum_fixed_binary_bits:5,attained_fixed_width_bits:[3,2],
    all_C12_intrace_reads_insufficient:true,
    parity_counterlaw:{alpha:[0,12,0,12,0,12],beta:[0,12,0,12,0,12]},
    readings:[{route:[0,2],after_event:3,required:"C24"},{route:[2,4],after_event:7,required:"C3 residue of same C24 observer"}],
    exact_integer_assertions:assertions,failures:0,
    model_status:"CONDITIONAL_EXACT_SOURCE_ROUTE_REPLAY_NOT_PHYSICAL_NATIVE_EXECUTION"
  };
};
const result=check(ORIGINAL_SOURCE_ROUTES);
if(typeof module!=="undefined" && require.main===module)console.log(JSON.stringify(result,null,2));
module.exports={check,result};
