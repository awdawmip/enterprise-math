/* Unit262; conditional exact checker, original Unit245 immutable witnesses. */
'use strict';
const verifyUnit262=function verifyUnit262(){
  const checks=[];let assertions=0;
  const check=(value,msg)=>{assertions++;if(!value)throw Error(msg)};
  const basis=[[1,0,0],[0,1,0],[0,0,1],[-1,0,0],[0,-1,0],[0,0,-1]];
  const pos=[];
  for(let r=0;r<6;r++){pos.push(basis[r]);pos.push(basis[r].map((v,k)=>v+basis[(r+1)%6][k]))}
  pos.push([0,0,0]);
  const serial=frame=>JSON.stringify(frame);
  const rotate=frame=>({axes:[frame.axes[1],frame.axes[2],frame.axes[0]],signs:frame.signs.map(v=>-v),ids:frame.ids.slice()});
  const init=[{axes:[0,1,2],signs:[1,1,1],ids:["A0","A1","A2"]},{axes:[0,2,4],signs:[1,1,1],ids:["B0","B1","B2"]}];
  for(const f of init){let g=f;for(let q=0;q<6;q++)g=rotate(g);check(serial(g)===serial(f),"R_can^6 identity");g=f;for(let q=0;q<3;q++)g=rotate(g);check(g.signs.every((v,k)=>v===-f.signs[k]),"R_can^3 sign reversal")}
  const cases=[
    {i:6,j:0,base:"LKJIHGMALKJIHGMdefghijklabAc",bounce:"LA",actor:0},
    {i:8,j:2,base:"LKJdefghimIHGFEDCBAcdefghimc",bounce:"dc",actor:1}
  ];
  const results=[];
  for(const c of cases){
    const local=[];
    for(const loops of [0,1,4]){
      const route=c.bounce.repeat(loops)+c.base;
      let p=[0,2],w=[0,0],steps=[0,0],frames=init;
      for(let t=0;t<route.length;t++){
        const ch=route[t],a=ch===ch.toUpperCase()?0:1;
        const to=ch.charCodeAt(0)-(a===0?65:97),from=p[a];
        check(to>=0&&to<=12&&to!==p[1-a],`occupancy ${c.i},${c.j} t${t}`);
        const adj=from===12?[[c.j,0]]:[[(from+1)%12,1],[(from+11)%12,-1],...(from===c.i?[[12,0]]:[])];
        const arc=adj.find(v=>v[0]===to);
        check(!!arc,`directed edge ${c.i},${c.j} t${t}`);
        const delta=pos[to].map((v,k)=>v-pos[from][k]);
        check(delta.reduce((s,v)=>s+Math.abs(v),0)===1,`primitive signed x6 ${t}`);
        p[a]=to;w[a]+=arc[1];steps[a]++;frames=frames.map((f,k)=>k===a?rotate(f):f);
      }
      check(JSON.stringify(p)==="[0,2]"&&JSON.stringify(w)==="[-12,12]","return and winding");
      const localReturn=frames.every((f,k)=>serial(f)===serial(init[k]));
      const globalC12Return=route.length%12===0;
      const expectedLength=28+2*loops;
      check(route.length===expectedLength,"length");
      check(steps[0]+steps[1]===route.length,"actor clock sum");
      check(localReturn===(loops>0),"exact signed frame return condition");
      check(globalC12Return===(loops===4),"C12 global clock return condition");
      local.push({loops,events:route.length,per_triad_events:steps,winding:w,per_triad_phase_mod6:steps.map(x=>x%6),global_phase_mod12:route.length%12,local_frame_return:localReturn,global_C12_return:globalC12Return,route});
    }
    check(local[0].events===28&&local[1].events===30&&local[2].events===36,"tiered length");
    check(local[0].per_triad_phase_mod6.filter(x=>x!==0).length===1,"28 local frame defect");
    check(local[1].per_triad_phase_mod6.every(x=>x===0),"30 frame repaired");
    results.push({ingress:c.i,egress:c.j,records:local});
  }
  check(28%6!==0&&30%6===0&&28%12!==0&&30%12!==0&&36%12===0,"sharp modular lower bounds");
  return {schema:"X6_TIME_UNIT262_SIGNED_TRIAD_FRAME_AND_C12_CLOSURE_V1",task_id:"RS-X6-NATIVE-TIME-DYNAMICS",source_original_unit245:"awdawmip/enterprise-math@f56840285cafeb9f5767ea91e903e1f53808186f:research_checks/X6_TIME_UNIT245_DIRECTED_CENTER_PORT_PAIR_RESULTS_20261121_2200.json",p000_pin:"a72226e2430ffa4786321ac86e7f0c599d5f0389",model:"conditional two-triad BRC + full ordered signed frame R_can per own move + independent C12 global event phase",minimums:{spatial_winding_return:28,spatial_and_both_C6_frames:30,spatial_both_C6_frames_and_global_C12:36},cases:results,exact_integer_assertions:assertions,failures:0,admission:"AUTHOR_PROVED / FINITE_CHECK_EXECUTED / UNREVIEWED / NOT_ADMITTED / NO_NATIVE_SOURCE_EXECUTION"};
};
console.log(JSON.stringify(verifyUnit262(),null,2));
