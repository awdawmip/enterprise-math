// R343: independent GMP exact BRC-Newton interior 2x2 / 3x3 verification.
// Only low-degree truncation t^(cap+1)=0, exact in Z[t]/(t^(cap+1)).
// No signed term with degree <=cap is removed.
#include <gmpxx.h>
#include <openssl/sha.h>
#include <array>
#include <algorithm>
#include <cstdlib>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;
using Z=mpz_class;
using Poly=vector<Z>;
long long C(int n,int k){if(n<0||k<0||k>n)return 0; long long x=1;for(int i=1;i<=k;++i)x=x*(n-k+i)/i;return x;}
void add_term(Poly& p,int n,long long coefficient,int shift){if(n<0||coefficient==0)return;for(int j=0;j<=n&&shift+j<(int)p.size();++j)p[shift+j]+=(long)(coefficient*C(n,j));}
Poly kernel(int i,int cap){
 Poly p(cap+1);
 long long d[]={-C(4,i)+C(2,i-1),C(5,i-1)-C(5,i-2),C(7,i-2),-C(9,i-3)};
 for(int h=1;h<=4;++h)add_term(p,i+1-h,-d[h-1],i-1);
 return p;
}
Poly forcing(int s,int cap){Poly p(cap+1);if(s>10)return p;add_term(p,s,-C(3,s-1),s);add_term(p,s-1,-C(6,s-1),s);add_term(p,s-2,C(8,s-2),s);return p;}
struct Digest{
 SHA256_CTX ctx;Digest(){SHA256_Init(&ctx);}void add(const string& s){SHA256_Update(&ctx,s.data(),s.size());}
 string out(){unsigned char b[SHA256_DIGEST_LENGTH];SHA256_Final(b,&ctx);ostringstream o;for(int i=0;i<SHA256_DIGEST_LENGTH;i++)o<<hex<<setw(2)<<setfill('0')<<(int)b[i];return o.str();}
};
Z det3(const vector<vector<Z>>& D,int q,int k){
 const Z &a=D[q][k],&b=D[q][k+1],&c=D[q][k+2],&d=D[q+1][k],&e=D[q+1][k+1],&f=D[q+1][k+2],&g=D[q+2][k],&h=D[q+2][k+1],&j=D[q+2][k+2];
 return a*(e*j-f*h)-b*(d*j-f*g)+c*(d*h-e*g);
}
int main(int argc,char**argv){
 try{
 int n=argc>1?stoi(argv[1]):640; string output=argc>2?argv[2]:"R343_evidence.json";
 if(n<320||n>2000)throw runtime_error("q_max expected 320..1000");
 const int cap=n+2, max_s=2*(n+2);
 vector<Poly> K(13);for(int i=1;i<=12;i++)K[i]=kernel(i,cap);
 vector<Poly> B;B.reserve(max_s+1);B.emplace_back(cap+1);B[0][0]=1;B[0][1]=1;
 for(int s=1;s<=max_s;++s){
  Poly p=forcing(s,cap);
  for(int i=1;i<=12&&i<=s;i++){
   for(int kd=0;kd<=cap;kd++)if(K[i][kd]!=0){
    const auto& prev=B[s-i];
    for(int j=0;j+kd<=cap;++j) if(prev[j]!=0)p[j+kd]+=K[i][kd]*prev[j];
   }
  }
  B.push_back(move(p));
 }
 vector<vector<Z>> D(n+3);Z pow5=1;
 long long dneg=0, d0=0, exterior_neg=0,triangle_checked=0,triangle_neg=0;
 for(int q=0;q<=n+2;q++){
  vector<Z> z(q+1);for(int v=0;v<=q;v++){z[v]=B[q+v][q];mpz_mul_2exp(z[v].get_mpz_t(),z[v].get_mpz_t(),q-v);}
  D[q].reserve(q+1);
  for(int k=0;k<=q;k++){
   D[q].push_back(z[0]);
   if(z[0]<0)dneg++;if(z[0]==0)d0++;
   for(int i=0;i<q-k;i++)z[i]=z[i+1]-z[i];
  }
  if(D[q][q]!=pow5)throw runtime_error("D diagonal !=5^q at q="+to_string(q));
  pow5*=5;
 }
 for(int s=0;s<=max_s;s++)for(int j=0;j<=cap;j++){
  if(j<=s){triangle_checked++;if(B[s][j]<=0)triangle_neg++;}
  else if(B[s][j]<0)exterior_neg++;
 }
 long long pos2=0,neg2=0,zero2=0,interiorPos=0,interiorNeg=0,interiorZero=0;
 long long pos3=0,neg3=0,zero3=0;
 vector<string> neg2_locations,neg3_locations;
 Digest interior320,edge320,interiorFull,edgeFull,tp3Full;
 for(int q=1;q<=n;q++){
  for(int k=0;k<q;k++){
   Z m=D[q][k]*D[q+1][k+1]-D[q][k+1]*D[q+1][k];
   string row=(k==0?to_string(q)+":"+m.get_str()+"\n":to_string(q)+","+to_string(k)+":"+m.get_str()+"\n");
   if(m>0)pos2++;else if(m<0){neg2++;if(neg2_locations.size()<30)neg2_locations.push_back("("+to_string(q)+","+to_string(k)+")");}else zero2++;
   if(k==0){edgeFull.add(row);if(q<=320)edge320.add(row);}else{
    interiorFull.add(row);if(q<=320)interior320.add(row);
    if(m>0)interiorPos++;else if(m<0)interiorNeg++;else interiorZero++;
   }
  }
  if(q>=3)for(int k=1;k<q-1;k++){
   Z m=det3(D,q,k);
   tp3Full.add(to_string(q)+","+to_string(k)+":"+m.get_str()+"\n");
   if(m>0)pos3++;else if(m<0){neg3++;if(neg3_locations.size()<40)neg3_locations.push_back("("+to_string(q)+","+to_string(k)+")");}else zero3++;
  }
 }
 string h320=interior320.out(),e320=edge320.out();
 string expectedH="f7ab9b1cdb8edb82e8c0d29b604cd1129748faaf9449fbe711fe8f3acb6b63ff";
 string expectedE="5d7e481d4bd9eb9f698376406b28fe2fc5dc85f85a1cd0be06c98e5f6d7c7c83";
 if(h320!=expectedH||e320!=expectedE)throw runtime_error("R340 q320 digest mismatch; inspect recurrence");
 if(det3(D,8,1)!=Z("-11584498914207849250816"))throw runtime_error("R342 first TP3 counterexample mismatch");
 auto json_arr=[](const vector<string>& a){string z="[";for(size_t i=0;i<a.size();i++)z+=(i?",":"")+string("\"")+a[i]+"\"";return z+"]";};
 ostringstream out;
 out<<"{\n  \"schema\": \"EM_R343_EXACT_GMP_V1\",\n"
    <<"  \"status\": \"PASS\",\n  \"q_max\": "<<n<<",\n  \"max_s\": "<<max_s<<",\n"
    <<"  \"low_degree_cap\": "<<cap<<",\n  \"low_degree_semantics\": \"exact mod t^(cap+1); no negative term is discarded within cap\",\n"
    <<"  \"D_negative\": "<<dneg<<",\n  \"D_zero\": "<<d0<<",\n  \"D_checked\": "<<(n+3LL)*(n+4LL)/2<<",\n"
    <<"  \"B_coefficients_checked_within_truncated_triangle\": "<<triangle_checked<<",\n  \"B_triangle_nonpositive\": "<<triangle_neg<<",\n"
    <<"  \"B_signed_exterior_negative_within_cap\": "<<exterior_neg<<",\n"
    <<"  \"minor2_positive\": "<<pos2<<",\n  \"minor2_negative\": "<<neg2<<",\n  \"minor2_zero\": "<<zero2<<",\n"
    <<"  \"interior_minor2_positive\": "<<interiorPos<<",\n  \"interior_minor2_negative\": "<<interiorNeg<<",\n  \"interior_minor2_zero\": "<<interiorZero<<",\n"
    <<"  \"minor2_negative_first30\": "<<json_arr(neg2_locations)<<",\n"
    <<"  \"minor3_positive\": "<<pos3<<",\n  \"minor3_negative\": "<<neg3<<",\n  \"minor3_zero\": "<<zero3<<",\n"
    <<"  \"minor3_negative_first40\": "<<json_arr(neg3_locations)<<",\n"
    <<"  \"r340_interior_q320_sha256\": \""<<h320<<"\",\n"
    <<"  \"r340_edge_q320_sha256\": \""<<e320<<"\",\n"
    <<"  \"interior_qmax_sha256\": \""<<interiorFull.out()<<"\",\n"
    <<"  \"edge_qmax_sha256\": \""<<edgeFull.out()<<"\",\n"
    <<"  \"tp3_qmax_sha256\": \""<<tp3Full.out()<<"\",\n"
    <<"  \"arithmetic\": \"C++17 GMP exact integers, OpenSSL SHA256; no floating point\",\n"
    <<"  \"scope\": \"finite exhaustive over stated q,k ranges only; no unbounded theorem\"\n}\n";
 ofstream f(output);if(!f)throw runtime_error("cannot open output");f<<out.str();f.close();
 cerr<<"R343 PASS q="<<n<<" TP2_inner+="<<interiorPos<<" inner-="<<interiorNeg<<" TP3-="<<neg3<<"\n";
 cout<<out.str();
 }catch(const exception&e){cerr<<"R343 FAIL "<<e.what()<<"\n";return 1;}
}
