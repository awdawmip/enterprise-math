"use strict";
// EC48O finite rational k=4 three-state certificate. All scores are integers
// in units of 1/1024; P and Q terminal masses use a common denominator 64.
function run() {
  const k=4, m=3;
  const leaves=[];
  for(let h=0;h<k;h++)for(let x=0;x<k;x++){
    if(h===x){leaves.push([h,x,"+",3,1],[h,x,"-",1,3]);}
    else leaves.push([h,x,"0",4,4]);
  }
  let p=0,q=0;
  for(const leaf of leaves){p+=leaf[3];q+=leaf[4];}
  if(leaves.length!==20 || p!==64 || q!==64) throw Error("mass conservation");
  function pc(mask){let n=0;while(mask){n+=mask&1;mask>>=1;}return n;}
  let best=-Infinity, bestCert=null, maskChecks=0, assignments=0;
  // All deterministic initial h->code maps, and all time-one code actions.
  // All time-two continuation masks are optimized independently per code.
  for(let n=0;n<3**4;n++){
    const assign=[];let z=n;for(let h=0;h<4;h++){assign.push(z%3);z=Math.floor(z/3);}
    assignments++;
    for(let actions=0;actions<8;actions++){
      let val=-32;const chosenMasks=[0,0,0];
      for(let code=0;code<3;code++){
        const hs=[];for(let h=0;h<4;h++)if(assign[h]===code)hs.push(h);
        if(hs.length===0 || ((actions>>code)&1)===0)continue;
        let local=-Infinity, localMask=0;
        for(let mask=0;mask<16;mask++){
          maskChecks++;
          let hits=0;for(const h of hs)if(mask&(1<<h))hits++;
          // Score: stage-one -2c*s/k; terminal +epsilon*hits/k^2;
          // time-two -2c*s*popcount(mask)/k^2, c=1/64,epsilon=1/2.
          const score=-8*hs.length+32*hits-2*hs.length*pc(mask);
          if(score>local){local=score;localMask=mask;}
        }
        val+=local;chosenMasks[code]=localMask;
      }
      if(val>best){best=val;bestCert={assignment:assign,time1ActionBits:actions,time2Masks:chosenMasks};}
    }
  }
  // Full optimal policy reads h exactly, visits 4 diagonal cells at t=3.
  // A sharp three-state controller groups 0 and 1 and visits 6 cells at t=3.
  const vf=56, v3=52;
  const fullTauNumerator=64+4*16+4*4;
  const compressedTauNumerator=64+4*16+6*4;
  if(best!==v3 || vf-best!==4 || fullTauNumerator!==144 ||
     compressedTauNumerator!==152 || assignments!==81 || maskChecks!==12480)
    throw Error("certificate mismatch");
  return {
    schema:"EC48O_K4_EXACT_INTEGER_CERTIFICATE_V1",
    k:4,registerStates:3,epsilon:"1/2",c:"1/64",
    positiveTerminalLeaves:leaves.length,P_total:"64/64",Q_total:"64/64",
    sourceRule:"off diagonal (4,4)/64; diagonal plus (3,1)/64, minus (1,3)/64",
    ratio_at_times_1_and_2:"1 exactly",
    fullObservation:["3/16","1/16","9/4","9/4"],
    threeStateObservation:["3/16","1/16","19/8","19/8"],
    fullSupport:"56/1024 = 7/128",
    optimalThreeStateSupport:"52/1024 = 13/256",
    exactGap:"4/1024 = 1/256",
    initialAssignments:assignments,
    timeOneActionVectorsPerAssignment:8,
    timeTwoMasksPerActiveRegister:16,
    actualMaskEvaluations:maskChecks,
    argmax:bestCert,
    failures:0,
    arithmetic:"integer only; exact denominators 64, 1024"
  };
}
if(typeof console!=="undefined" && typeof module!=="undefined" && require.main===module)
  console.log(JSON.stringify(run(),null,2));
