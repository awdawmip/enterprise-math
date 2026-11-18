#include <bits/stdc++.h>
using namespace std;
using U64=uint64_t;
static const U64 N=(U64(1)<<32), T=33*N;
static const int LO=262145, HI=524287, COUNT=131072;
static int S[16]={262147,280001,300001,320003,340007,360007,380003,400009,420001,440003,460001,480007,500383,510007,520001,524285};
U64 gcd_u64(U64 a,U64 b){while(b){U64 r=a%b;a=b;b=r;}return a;}
U64 inv_u64(U64 a,U64 m){int64_t old_r=a,r=m,old_s=1,s=0;while(r){int64_t q=old_r/r;tie(old_r,r)=make_pair(r,old_r-q*r);tie(old_s,s)=make_pair(s,old_s-q*s);}if(old_r!=1)abort();return (old_s%(int64_t)m+(int64_t)m)%(int64_t)m;}
U64 ceildiv(U64 a,U64 b){return (a+b-1)/b;}
struct Witness{U64 x=0,u=0;int bit=-1;bool down=false;};
bool endpoint(U64 a,U64 b,Witness* wit){if(gcd_u64(a,b)>1)return false;U64 inv=inv_u64(a%b,b);U64 r=inv,bit=1;for(int i=0;i<32;i++,bit<<=1){
 if(r*a <= N-1){if(wit){wit->u=N-1;wit->x=wit->u-r*a;wit->bit=i;wit->down=true;}return true;}
 if((b-r)*a + bit <= N-1){if(wit){wit->u=N-1-bit;wit->x=wit->u-(b-r)*a;wit->bit=i;wit->down=false;}return true;}
 r*=2;if(r>=b)r-=b;
}return false;}
bool witness_valid(U64 a,U64 b,const Witness&w){if(w.bit<0||w.bit>=32||w.x>=N||w.u>=N)return false;U64 v=w.u^(U64(1)<<w.bit);return w.x%a==w.u%a && w.x%b==v%b && w.x!=w.u;}
int main(){vector<int> q;vector<char> isU(COUNT,false),isR(COUNT,false);
 for(int x=LO;x<=HI;x+=2){bool inU=false;for(int s:S)if(x==s)inU=true;
 if((400011<=x&&x<=400521)||(480011<=x&&x<=480521))inU=true;
 for(int h=1;h<32;h++){U64 pow2=(U64(1)<<h);if((pow2-1)%x==0||(pow2+1)%x==0){inU=true;break;}}
 q.push_back(x);isU[(x-LO)/2]=inU;}
 assert(count(isU.begin(),isU.end(),true)==552);
 for(int j=0;j<64;j++){int v=510001+194*j;assert(v%2&&v>=LO&&v<=HI);int k=(v-LO)/2;if(isU[k]){cerr<<"selected row in U: "<<v<<"\n";return 2;}isR[k]=true;}
 U64 checked=0,preexcluded=0,delta=0,intersect=0,up=0,down=0;
 U64 prior_capacity=0,prior_special=0,prior_zz=0,prior_fiber=0;
 int example_a=0,example_b=0;Witness example;
 vector<array<U64,3>> rows;
 for(int a=LO;a<=HI;a+=2)if(isR[(a-LO)/2]){
  U64 old=0,hits=0,n=0;for(int b:q){checked++;
   U64 g=gcd_u64(a,b);
   bool oldhit;
   if(U64(a)*b<T){prior_capacity++;oldhit=true;}
   else if(isU[(b-LO)/2]){prior_special++;oldhit=true;}
   else if((U64(a)/g)*b<N){prior_zz++;oldhit=true;}
   else if(33*ceildiv(N,a)>U64(b) || 33*ceildiv(N,b)>U64(a)){prior_fiber++;oldhit=true;}
   else oldhit=false;
   if(oldhit){old++;preexcluded++;continue;}
   n++;
   Witness w; if(endpoint(a,b,&w)){
    assert(witness_valid(a,b,w));hits++;delta++;
    if(w.down)down++;else up++;
    if(isR[(b-LO)/2])intersect++;
    if(!example_a){example_a=a;example_b=b;example=w;}
    assert(endpoint(b,a,nullptr));
   }
  }
  rows.push_back({U64(a),n,hits});
 }
 assert(rows.size()==64);assert(checked==64ULL*131072);assert(prior_capacity+prior_special+prior_zz+prior_fiber==preexcluded);
 cout<<"{\n\"model\":\"p32 named zero/one xor two-port\",\n\"rows_rule\":\"a=510001+194*j, j=0..63\",\n\"domain\":\"q1,q2 odd 262145..524287\",\n\"source_pin\":\"f42f2906d77f24085c123f3ccfe9667d41caa96d\",\n";
 cout<<"\"examined_rows\":"<<rows.size()<<",\n\"examined_pairs\":"<<checked<<",\n\"already_covered_in_rows\":"<<preexcluded<<",\n\"prior_capacity\":"<<prior_capacity<<",\n\"prior_special_only\":"<<prior_special<<",\n\"prior_zz_only\":"<<prior_zz<<",\n\"prior_fiber_only\":"<<prior_fiber<<",\n\"old_union_negative_in_rows\":"<<checked-preexcluded<<",\n\"new_ZF_positive_in_rows\":"<<delta<<",\n\"direction_down\":"<<down<<",\n\"direction_up\":"<<up<<",\n\"new_ZF_positive_row_column_intersection\":"<<intersect<<",\n\"new_ZF_positive_symmetric_union\":"<<2*delta-intersect<<",\n";
 cout<<"\"first_witness\":{\"q1\":"<<example_a<<",\"q2\":"<<example_b<<",\"zero_x\":"<<example.x<<",\"flip_start\":"<<example.u<<",\"flip_source_bit\":"<<example.bit<<",\"flip_down\":"<<(example.down?"true":"false")<<"},\n";
 cout<<"\"rows\":[\n";
 for(int i=0;i<(int)rows.size();i++)cout<<"["<<rows[i][0]<<","<<rows[i][1]<<","<<rows[i][2]<<"]"<<(i+1==(int)rows.size()?"\n":",\n");
 cout<<"]\n}\n";
}
