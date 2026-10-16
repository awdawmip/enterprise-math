// FROZEN CANDIDATE ONLY. Do not submit without a new lawful Task/run and
// an actual independent static preaudit of this exact bundle.
// Existing Magma routines; fixed core (9,8); no old fixed233 resources.
SetQuitOnError(true);
print "EM_CORE98_MIXED_V1_BEGIN";
vmajor, vminor, vpatch := GetVersion();
print "VERSION", vmajor, vminor, vpatch;
assert vmajor eq 2 and vminor eq 29 and vpatch eq 10;
print "INITIAL_MEMORY_LIMIT", GetMemoryLimit();
assert GetMemoryLimit() eq 400000000;
assert GetNthreads() eq 1;
SetMemoryLimit(400000000);
SetNthreads(1);
SetSeed(1);
SetColumns(0);
SetVerbose("FourDescent", 1);
SetVerbose("CasselsTate", 2);

QQ := Rationals();
Rx<t> := PolynomialRing(QQ);
pp := QQ!161;
qq := QQ!127;
f := t*(t-pp^2)*(t-qq^2);
E := EllipticCurve([QQ|0,-(pp^2+qq^2),0,pp^2*qq^2,0]);
L0 := (t-pp^2)*(t-qq^2)/(pp^2*qq^2);
d2 := 2-L0;
d3 := 3-2*L0;
assert [Evaluate(d2,z) : z in [QQ|0,pp^2,qq^2]] eq [QQ|1,2,2];
assert [Evaluate(d3,z) : z in [QQ|0,pp^2,qq^2]] eq [QQ|1,3,3];
print "FIXED_E", E;
print "ORDERED_ROOTS", [QQ|0,pp^2,qq^2];
print "SPLIT_CUBIC", f;
print "D2_POLYNOMIAL", d2;
print "D3_POLYNOMIAL", d3;
AA<a> := quo< Rx | f >;

// The optional E target occurs in the current documented TwoCover example.
// Do not substitute an unlabelled Jacobian or rescan all Selmer elements.
H2, map2 := TwoCover(AA!d2 : E:=E);
H3, map3 := TwoCover(AA!d3 : E:=E);
print "U2_TWO_COVER", H2;
print "U2_RETURNED_MAP", map2;
print "U3_TWO_COVER", H3;
print "U3_RETURNED_MAP", map3;

// One ordinary FourDescent, with local and real conditions retained.
// No full TwoDescent/Selmer recomputation, point search or EightDescent.
lifts := FourDescent(H3 : RemoveTorsion:=false, IgnoreRealSolubility:=false);
print "NUMBER_OF_RETURNED_LIFTS", #lifts;
if #lifts eq 0 then
    print "STOP_EMPTY_LIFT_INCONSISTENT_WITH_RETAINED_HYPOTHESES";
    quit;
end if;
C4 := lifts[1];
print "CHOSEN_FOUR_COVER", C4;
isQI, matrices := IsQuadricIntersection(C4);
assert isQI;
print "CHOSEN_FOUR_COVER_MATRICES", matrices;
E4, map4E := AssociatedEllipticCurve(C4 : E:=E);
HC4, map42 := AssociatedHyperellipticCurve(C4);
print "FOUR_COVER_ASSOCIATED_E", E4;
print "FOUR_COVER_RETURNED_MAP_TO_E", map4E;
print "FOUR_COVER_ASSOCIATED_TWO_COVER", HC4;
print "FOUR_COVER_RETURNED_MAP_TO_TWO_COVER", map42;

// Raw printed maps are retained, even if their implementation is a rule.
// A rule-only print is not a portable polynomial certificate.
exported2 := false;
exported3 := false;
exported4E := false;
exported42 := false;
try
    print "U2_MAP_EQUATIONS", DefiningEquations(map2);
    exported2 := true;
catch maperror
    print "U2_MAP_POLYNOMIAL_EXPORT_UNKNOWN", maperror;
end try;
try
    print "U3_MAP_EQUATIONS", DefiningEquations(map3);
    exported3 := true;
catch maperror
    print "U3_MAP_POLYNOMIAL_EXPORT_UNKNOWN", maperror;
end try;
try
    print "FOUR_TO_E_MAP_EQUATIONS", DefiningEquations(map4E);
    exported4E := true;
catch maperror
    print "FOUR_TO_E_MAP_POLYNOMIAL_EXPORT_UNKNOWN", maperror;
end try;
try
    print "FOUR_TO_TWO_MAP_EQUATIONS", DefiningEquations(map42);
    exported42 := true;
catch maperror
    print "FOUR_TO_TWO_MAP_POLYNOMIAL_EXPORT_UNKNOWN", maperror;
end try;
print "POLYNOMIAL_MAP_EXPORT_FLAGS",
      exported2, exported3, exported4E, exported42;

// Exactly one mixed evaluation. No retries, other lifts or parameter sweep.
bit := CasselsTatePairing(C4,H2);
assert bit eq 0 or bit eq 1;
print "IMPLEMENTATION_CANDIDATE_MIXED_BIT", bit;
print "FINAL_MEMORY_LIMIT", GetMemoryLimit();
print "FINAL_THREADS", GetNthreads();
assert GetMemoryLimit() eq 400000000 and GetNthreads() eq 1;
print "PORTABLE_LOCAL_CERTIFICATE_NOT_AUTOMATICALLY_EXPORTED";
print "EM_CORE98_MIXED_V1_END";

