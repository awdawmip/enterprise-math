// Unit255. Run: node X6_TIME_UNIT255_GUARDED_SIGNED_COMPATIBILITY_CHECK_20261122_0700.js <path-to-Unit245-original-results.json>
function verify(c){
 const b=[[1,0,0],[0,1,0],[0,0,1],[-1,0,0],[0,-1,0],[0,0,-1]];
 const cells=Array.from({length:12},(_,k)=>k%2===0?[...b[k/2]]:b[(k-1)/2].map((v,j)=>v+b[((k+1)/2)%6][j]));cells.push([0,0,0]);
 const rows=[],totals={cases:0,events:0,positive:0,negative:0,positive_spokes:0,negative_spokes:0,positive_ring:0,negative_ring:0},errors=[];
 const ck=(ok,label,r,t)=>{if(!ok)errors.push([r.ingress,r.egress,t,label]);};
 for(const r of c.cases){
  let pos=[0,2],w=[0,0],p=[0,0,0],n=[0,0,0],pr=0,nr=0,ps=0,ns=0,by=Array.from({length:2},()=>Array.from({length:3},()=>[0,0]));
  for(let t=0;t<r.route.length;t++){
   const ch=r.route[t],isA=ch>="A"&&ch<="M",tri=isA?0:1,dst=ch.charCodeAt(0)-(isA?65:97),src=pos[tri];
   ck(dst!==pos[1-tri],"occupied",r,t);
   const d=cells[dst].map((v,j)=>v-cells[src][j]),ax=d.findIndex(v=>v!==0),nz=d.filter(v=>v!==0).length;
   ck(nz===1&&Math.abs(d[ax])===1,"primitive",r,t);
   const positive=d[ax]>0;by[tri][ax][positive?0:1]++;(positive?p:n)[ax]++;
   if(src===12||dst===12){ck(src===12?dst===r.egress:src===r.ingress,"port",r,t);if(positive)ps++;else ns++;}
   else {const k=(dst-src+12)%12;ck(k===1||k===11,"ring",r,t);w[tri]+=k===1?1:-1;if(positive)pr++;else nr++;}
   pos[tri]=dst;
  }
  const P=p.reduce((a,v)=>a+v,0),N=n.reduce((a,v)=>a+v,0);
  ck(pos[0]===0&&pos[1]===2&&w[0]===-12&&w[1]===12,"return",r,r.route.length);
  ck(r.route.length===r.cost&&P===N&&P+N===r.cost,"balanced_cost",r,r.route.length);
  ck(pr+nr===r.ring_events&&ps+ns===r.spoke_events,"edge_count",r,r.route.length);
  for(let tr=0;tr<2;tr++)for(let ax=0;ax<3;ax++)ck(by[tr][ax][0]===by[tr][ax][1],"triad_axis_balance",r,r.route.length);
  rows.push({ingress:r.ingress,egress:r.egress,events:r.cost,negative:N,negative_ring:nr,negative_spokes:ns,positive_ring:pr,positive_spokes:ps,axis_positive:p,axis_negative:n});
  totals.cases++;totals.events+=r.cost;totals.positive+=P;totals.negative+=N;totals.positive_spokes+=ps;totals.negative_spokes+=ns;totals.positive_ring+=pr;totals.negative_ring+=nr;
 }
 return {schema:"X6_TIME_UNIT255_SIGNED_CANDIDATE_AUDIT_V1",input:"Unit245 original immutable BRC certificates",candidate:"2026-11-18 guarded triad positive-only transfer",status:"EXACT_CONDITIONAL_SOURCE_COMPARISON_NO_PHYSICAL_EXECUTION",totals,negative_matrix:[0,2,4,6,8,10].map(i=>rows.filter(r=>r.ingress===i).map(r=>r.negative)),optimal_details:rows.filter(r=>r.events===28),rows,failures:errors};
}
const fs=require("fs");
const result=verify(JSON.parse(fs.readFileSync(process.argv[2],"utf8")));
if(result.failures.length)throw Error(JSON.stringify(result.failures));
console.log(JSON.stringify(result,null,2));
