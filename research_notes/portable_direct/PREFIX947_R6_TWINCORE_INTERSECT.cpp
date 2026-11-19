#include <cstdint>
#include <fstream>
#include <iostream>
#include <stdexcept>
using namespace std;using u64=uint64_t;
struct Reader{ifstream f;u64 val;bool has;Reader(const char*n):f(n,ios::binary){if(!f)throw runtime_error("missing input");next();}void next(){has=bool(f.read((char*)&val,8));if(!has&&!f.eof())throw runtime_error("truncated file");}};
int main(){
 Reader s("PREFIX946_W21.bin"),t("PREFIX947_W23.bin"), n("PREFIX946_NEW21.bin");
 ofstream x("PREFIX947_W21_W23_INTERSECTION.bin",ios::binary),y("PREFIX947_NEW21_W23_INTERSECTION.bin",ios::binary);
 u64 common=0,new_common=0,first=0,first_new=0;
 while(s.has&&t.has){if(s.val<t.val)s.next();else if(s.val>t.val)t.next();else{if(!first)first=s.val;x.write((char*)&s.val,8);common++;s.next();t.next();}}
 t.f.clear();t.f.seekg(0);t.next();
 while(n.has&&t.has){if(n.val<t.val)n.next();else if(n.val>t.val)t.next();else{if(!first_new)first_new=n.val;y.write((char*)&n.val,8);new_common++;n.next();t.next();}}
 cout<<"W21_intersect_W23="<<common<<" first_id="<<first<<" NEW21_intersect_W23="<<new_common<<" first_new_id="<<first_new<<"\n";
 if(new_common!=2237)throw runtime_error("new21 intersection disagrees with independent old-bucket count");
 cout<<"ALL_TWINCORE_INTERSECTION_ASSERTIONS_PASSED\n";
}
