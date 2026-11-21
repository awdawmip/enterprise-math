function check(){
 const A=[[1,0,0,0,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0],[-1,0,0,0,0,0],[0,-1,0,0,0,0],[0,0,-1,0,0,0]];
 const zero=[0,0,0,0,0,0];
 const add=(a,b)=>a.map((x,i)=>x+b[i]),sub=(a,b)=>a.map((x,i)=>x-b[i]);
 const mod=(x,n)=>(x%n+n)%n,sq=a=>a.reduce((s,x)=>s+x*x,0);
 function signedStep(v){let index=-1,sign=0;for(let i=0;i<6;i++){if(v[i]!==0){if(index!==-1||Math.abs(v[i])!==1)throw Error("non primitive step");index=i;sign=v[i];}}if(index===-1)throw Error("zero step");return(sign>0?"+":"-")+"E"+(index+1);}
 let assertions=0,cases={};
 function verify(test,message){assertions++;if(!test)throw Error(message);}
 for(let W of [1,2]){
  const N=6*W,all=new Set(),withWord=new Set(),roots=new Set(),byOrientation={};let histReference=null,eligible=0;
  for(let epsilon of [-1,1]){
   let full=new Set(),bare=new Set(),edgeHistogramRef=null;
   for(let mask=0;mask<2**N;mask++){
    const hist=Object.fromEntries(Array.from({length:6},(_,i)=>["+E"+(i+1),"-E"+(i+1)]).flat().map(k=>[k,0]));
    let edgeHistograms=[],words=[],bits=[],r=0;
    for(let j=0;j<N;j++){
     const dest=mod(r+epsilon,6),x=A[r],y=A[dest],outer=(mask>>>j)&1;
     const mid=outer?add(x,y):zero,moves=[sub(mid,x),sub(y,mid)];
     const names=moves.map(signedStep);
     const eh=names.slice().sort().join(",");
     edgeHistograms.push(eh);
     for(const nm of names)hist[nm]++;
     verify(sq(mid)===(outer?2:0),"wrong intermediate norm");
     verify(moves.every(v=>sq(v)===1),"non primitive edge");
     verify(add(moves[0],moves[1]).every((z,i)=>z===y[i]-x[i]),"wrong displacement");
     const expected=[signedStep(A[dest]),signedStep(A[r].map(x=>-x))].sort().join(",");
     verify(eh===expected,"wrong unordered multiset");
     words.push(names.join(">"));bits.push(outer);r=dest;
    }
    verify(r===0,"bad return");
    for(let i=0;i<6;i++){verify(hist["+E"+(i+1)]===(i<3?2*W:0),"wrong positive frequency");verify(hist["-E"+(i+1)]===(i<3?2*W:0),"wrong negative frequency");}
    const h=JSON.stringify(hist);if(histReference===null)histReference=h;verify(h===histReference,"different histograms");
    const w=words.join("|");verify(!full.has(w),"repeated ordered step word");full.add(w);
    const b=bits.join("");verify(!bare.has(b),"repeated branch code");bare.add(b);
    all.add(w);withWord.add(epsilon+":"+b);
    if(bits.every(x=>x===1)){eligible++;roots.add(epsilon===1?"+3":"-3");}else roots.add("UNDEFINED");
    if(edgeHistogramRef===null)edgeHistogramRef=edgeHistograms.join("|");
    verify(edgeHistogramRef===edgeHistograms.join("|"),"per-edge histogram depends on branch code");
   }
   verify(full.size===2**N,"oriented word count");verify(bare.size===2**N,"oriented branch count");
   byOrientation[epsilon===1?"positive":"negative"]={history_count:full.size,ordered_macro_histogram_classes:1};
  }
  verify(all.size===2**(N+1),"joint history collision");
  verify(withWord.size===2**(N+1),"joint code collision");
  verify(eligible===2,"eligible count");verify(roots.size===3,"typed root states");
  cases["W"+W]={macro_edges:N,total_complete_histories:all.size,per_orientation:byOrientation,global_signed_histogram:JSON.parse(histReference),global_histogram_classes:1,all_outer_root_eligible_histories:eligible,typed_C12_root_states:[...roots].sort(),minimum_bits_full_history:N+1,minimum_bits_branch_given_orientation:N,minimum_bits_root_typed_C12:2};
 }
 return {schema:"X6_TIME_SIGNED_HISTOGRAM_FIBER_CHECK_V1",science_unit:"237",coverage:"all 2^(6W+1) ordered paths for W=1,2; symbolic theorem for all W>=1",assertions,mismatches:0,cases};
}
if (typeof module !== 'undefined' && require.main===module) console.log(JSON.stringify(check(),null,2));
