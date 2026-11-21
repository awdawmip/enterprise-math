// X6 Native Time Unit246: exact original BRC certificate replay and Port gcd accounting.
// Usage: node X6_TIME_UNIT246_PORT_GCD_WINDING_ACCOUNTING_CHECK_20261121_2300.js <Unit245-results.json>
// Source pin: awdawmip/enterprise-math@f56840285cafeb9f5767ea91e903e1f53808186f:research_checks/X6_TIME_UNIT245_DIRECTED_CENTER_PORT_PAIR_RESULTS_20261121_2200.json
const fs=require('node:fs');
function checkSource(data) {
  let assertions=0;
  function demand(ok,msg){assertions++;if(!ok)throw new Error(msg)}
  const v=[[1,0,0],[0,1,0],[0,0,1],[-1,0,0],[0,-1,0],[0,0,-1]];
  const cells=[];
  for(let r=0;r<6;r++){
    cells.push([...v[r]]);
    cells.push(v[r].map((x,k)=>x+v[(r+1)%6][k]));
  }
  cells.push([0,0,0]); // x12=P, the relative native Cell anchor, not a carrier gate
  function gcd(a,b){return b===0?a:gcd(b,a%b)}
  demand(data.cases.length===36,"case count");
  let matrices=Array.from({length:6},()=>Array(6).fill(null));
  let summary=Array.from({length:6},()=>({offset:null,m:null,cases:0,minimum:null,maximum:null,zero_extra:0}));
  const records=[];
  for(const item of data.cases){
    const {ingress:i,egress:j,cost,route}=item;
    const ii=i/2,jj=j/2;
    demand(Number.isInteger(ii)&&ii>=0&&ii<6&&Number.isInteger(jj)&&jj>=0&&jj<6,"spoke indices");
    demand(matrices[ii][jj]===null,"unique pair");
    let at=[0,2],ring=[0,0],plus=[0,0],minus=[0,0],excursions=[0,0],spokes=0;
    for(const char of route){
      const code=char.charCodeAt(0);
      const mover=(code>=65&&code<=77)?0:(code>=97&&code<=109)?1:-1;
      demand(mover!==-1,"route character");
      const dst=(mover===0?code-65:code-97);
      const from=at[mover],other=at[1-mover];
      demand(dst!==from&&dst!==other,"whole-triad target-empty");
      const d=cells[dst].map((x,k)=>x-cells[from][k]);
      demand(d.reduce((c,x)=>c+(x!==0),0)===1&&d.some(x=>Math.abs(x)===1),"signed primitive Cell edge");
      if(dst===12){demand(from===i,"only declared ingress");excursions[mover]++;spokes++}
      else if(from===12){demand(dst===j,"only declared egress");spokes++}
      else{
        const dir=(dst-from+12)%12;
        demand(dir===1||dir===11,"adjacent OUTER ring");
        ring[mover]++; if(dir===1)plus[mover]++;else minus[mover]++;
      }
      at[mover]=dst;
    }
    demand(at[0]===0&&at[1]===2,"labelled full Cell return");
    demand(plus[0]-minus[0]===-12&&plus[1]-minus[1]===12,"exact opposite signed ring windings");
    demand(spokes===2*(excursions[0]+excursions[1]),"complete directed centre excursions");
    demand(route.length===cost&&ring[0]+ring[1]+spokes===cost,"full event cost");
    const offset=(j-i+12)%12,m=12/gcd(12,offset),c=excursions[0]+excursions[1];
    demand((offset*excursions[0])%12===0&&(offset*excursions[1])%12===0,"modular closure both labels");
    demand(excursions[0]%m===0&&excursions[1]%m===0,"gcd divisibility both labels");
    demand(c===m,"attained minimal mandatory centre excursions in provided shortest witness");
    demand(excursions[0]*excursions[1]===0,"one labelled triad makes all centre trips in witness");
    const backA=(ring[0]-12)/2,backB=(ring[1]-12)/2,back=backA+backB;
    demand(Number.isInteger(backA)&&backA>=0&&Number.isInteger(backB)&&backB>=0,"nonnegative backtrack pairs");
    demand(cost===24+2*c+2*back,"exact count budget");
    demand(back===(cost-24-2*m)/2,"optimal cost residual");
    demand(data.matrix_ingress_rows_egress_columns[ii][jj]===cost,"matches inherited exact cost");
    matrices[ii][jj]=back;
    const s=summary[offset/2];
    s.offset=offset;s.m=m;s.cases++;s.minimum=s.minimum===null?cost:Math.min(s.minimum,cost);s.maximum=s.maximum===null?cost:Math.max(s.maximum,cost);
    if(back===0)s.zero_extra++;
    records.push({ingress:i,egress:j,min_cost:cost,offset,m,excursions_A:excursions[0],excursions_B:excursions[1],ring_backtrack_pairs_A:backA,ring_backtrack_pairs_B:backB,excess_pairs:back,spoke_events:spokes,ring_events:ring[0]+ring[1]});
  }
  demand(records.length===36&&matrices.every(row=>row.every(x=>Number.isInteger(x))),"complete grid");
  demand(summary.every(x=>x.cases===6),"six offsets and six cases each");
  return {actual_integer_assertions:assertions,failures:0,all_36_shortest_witnesses_have_exact_minimal_spoke_excursions:true,all_36_witnesses_have_one_centre_using_label:true,excess_backtrack_pair_matrix_ingress_rows_egress_columns:matrices,offset_groups:summary,case_metrics:records};
};
const input=JSON.parse(fs.readFileSync(process.argv[2],'utf8'));
console.log(JSON.stringify({schema:'X6_TIME_UNIT246_GCD_PORT_BUDGET_CERT_V1',source_unit245_commit:'f56840285cafeb9f5767ea91e903e1f53808186f',source_unit245_path:'research_checks/X6_TIME_UNIT245_DIRECTED_CENTER_PORT_PAIR_RESULTS_20261121_2200.json',...checkSource(input)},null,2));
