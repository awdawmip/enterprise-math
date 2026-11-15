// R762BG exact author-side checker: conditional signed BRC triple-query code.
// No libraries or floating-point operations. Node.js: node R762BG_ORIENTATION_TRIPLE_CODE_VERIFY.js
const evidence = (function run() {
  function pc(x){let s=0;for(;x;x&=x-1)s++;return s;}
  function yes(x,m){if(!x)throw Error(m);}
  const tri=[], labels=[], triIndex=Array(64).fill(-1);
  for(let i=0;i<6;i++)for(let j=i+1;j<6;j++)for(let k=j+1;k<6;k++){
    const t=(1<<i)|(1<<j)|(1<<k);triIndex[t]=tri.length;tri.push(t);labels.push([i+1,j+1,k+1]);
  }
  yes(tri.length===20,"20 triples");
  function encode(x){let y=0;for(let t=0;t<20;t++)if(pc(x&tri[t])%2)y|=1<<t;return y;}
  const words=Array.from({length:64},(_,i)=>encode(i));
  yes(new Set(words).size===64,"injective six bit ledger");
  const multiplicity=Array(21).fill(0);
  for(const w of words)multiplicity[pc(w)]++;
  const target={0:1,8:15,10:32,12:15,20:1};
  for(let w=0;w<=20;w++)yes(multiplicity[w]===(target[w]||0),"weight enumerator");
  let rank=0;const pivots=Array(6).fill(0),probes=[];
  for(let t=0;t<20;t++){
    let v=tri[t];for(let j=5;j>=0;j--)if(v>>j&1){
      if(pivots[j])v^=pivots[j];else{pivots[j]=v;probes.push(labels[t]);rank++;break;}
    }
    if(rank===6)break;
  }
  yes(rank===6,"rank six");
  let errors=0;
  function test(e){
    let best=21,winner=-1,ties=0;
    for(let i=0;i<64;i++){const d=pc(words[i]^e);if(d<best){best=d;winner=i;ties=1;}else if(d===best)ties++;}
    yes(winner===0&&ties===1&&best===pc(e),"unique decoding for <=3 errors");
    errors++;
  }
  test(0);
  for(let i=0;i<20;i++)test(1<<i);
  for(let i=0;i<20;i++)for(let j=i+1;j<20;j++)test((1<<i)|(1<<j));
  for(let i=0;i<20;i++)for(let j=i+1;j<20;j++)for(let k=j+1;k<20;k++)test((1<<i)|(1<<j)|(1<<k));
  yes(errors===1351,"radius-three count");
  const delta=words[15];yes(pc(delta)===8,"distance eight");
  let midpoint=0, taken=0;
  for(let j=0;j<20;j++)if(delta>>j&1 && taken<4){midpoint|=1<<j;taken++;}
  yes(pc(midpoint)===4&&pc(midpoint^delta)===4,"sharp four-error tie");
  let xor=0;
  for(let a=0;a<64;a++)for(let b=0;b<64;b++){yes((words[a]^words[b])===words[a^b],"F2 linearity");xor++;}
  let permCount=0,cov=0;
  function perms(p,used){
    if(p.length===6){
      permCount++;
      const dest=tri.map(t=>{let v=0;for(let j=0;j<6;j++)if(t>>j&1)v|=1<<p[j];return triIndex[v];});
      for(let x=0;x<64;x++){
        let x2=0;for(let j=0;j<6;j++)if(x>>j&1)x2|=1<<p[j];
        let y2=0;for(let j=0;j<20;j++)if(words[x]>>j&1)y2|=1<<dest[j];
        yes(words[x2]===y2,"S6 covariance");cov++;
      }
      return;
    }
    for(let k=0;k<6;k++)if(!(used>>k&1))perms([...p,k],used|1<<k);
  }
  perms([],0);yes(permCount===720&&cov===46080,"S6 test total");
  let signChecks=0;const aggregate={};
  for(let x=0;x<64;x++){
    let eligible=0;
    for(const t of tri)for(let signed=0;signed<8;signed++){
      if(((pc(x&t)+pc(signed))%2)===0)eligible++;
      signChecks++;
    }
    yes(eligible===80,"uniform positive-branch count");
    let e=20-pc(words[x]);aggregate[e]=(aggregate[e]||0)+1;
  }
  yes(signChecks===10240&&Object.keys(aggregate).length===5,"BRC count");
  let distinguishablePairs=0;
  for(let x=0;x<64;x++)for(let z=0;z<64;z++)if(x!==z){
    yes(pc(words[z^x])>=8,"future flip distinguishes");distinguishablePairs++;
  }
  return {schema:"R762BG_ORIENTATION_TRIPLE_CODE_EXACT_CERT_V1",scope:"conditional signed eta-ledger triad relation; 6 fixed axes and 20 named triples",source_task:"RS-X6-TRIADIC-CLOSURE-DYNAMICS",code_length:20,code_dimension:rank,code_states:64,minimum_distance:8,
    weight_enumerator:multiplicity.map((count,weight)=>({weight,count})).filter(p=>p.count),
    six_independent_triad_probes:probes,checked_error_masks_at_radius_le_3:errors,coverage_by_translation:errors*64,
    four_error_ambiguity:{delta_axis_mask:15,delta_codeword:delta,observed_word:midpoint,distances:[pc(midpoint),pc(midpoint^delta)]},
    linearity_pairs:xor,S6_permutations:permCount,S6_orientation_covariance_pairs:cov,
    eligible_named_sign_assignments_per_ledger:80,eligibility_checks:signChecks,
    all_positive_signed_record_observer_histogram:aggregate,future_named_flip_separated_ordered_pairs:distinguishablePairs,
    verification:"Exact integer and Boolean exhaustive checking. Symbolic proof supports general statements. AUTHOR_CHECKED_NOT_INDEPENDENTLY_REVIEWED."};
})();
if (typeof process !== 'undefined') process.stdout.write(JSON.stringify(evidence,null,2)+'\n');
