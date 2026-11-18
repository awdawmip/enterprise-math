# Seventh exact S23/AV capacity plateau through h=2455068

Date: 2026-11-08 Asia/Shanghai. Frozen scientific pin: 43ec6098b1330ae86d0a7863be336c5d97f6ef34. Predecessor: PROOF.md in this directory, which proves the first six exact intervals and Lemmas 1-4. Author-side analytical proof, independent review pending.

## New exact result

For **every integer 2282518 <= h <= 2455068**, the exact padded-prefix capacity is

N(h) = 14,905,515.

This extends the six-interval theorem to a seventh consecutive exact interval, completing the entire integer range 510..2455068. The first six intervals and first five jump locations remain exactly as in PROOF.md. At 2282518 the new jump is 14,905,515-12,830,310=2,075,205.

## Certificate point

Use the unimodular lattice vectors u=(79,431), w=(380295,2074774), epsilon=79r-431, eta=2074774-380295r, r=ln7/ln(10/7), alpha=eta/epsilon. The strict certified rational enclosure yields
4epsilon < 7eta < 5epsilon,
so a_7=floor(7alpha)=4 and the seventh exact strip point is

(v_7,k_7)=7w+4u=(2662381,14525142),
m_7=v_7+k_7=17187523,
delta_7=k_7-rv_7=7eta-4epsilon in (0,epsilon).

The last sixth-plateau point had v_6=2282007. Put
n_7=m_7-(v_6+1)=14905515.
The new lower-bound horizon is h_7=v_6+511=2282518.

## Exact lower bound

The scaled-gap lemma in predecessor PROOF.md applies for every t>=0, and gives
N(510+t)>=L(t), where L(t)=k_B+v_B-t and B is the smallest positive integer with v_B>=t.

For t=v_6+1=2282008, B=7. Therefore
N(2282518)>=k_7+v_7-(v_6+1)=14905515.
N(h) is nondecreasing, so the same lower bound applies for all h>=2282518.

## Exact all-cell upper bound

For any integer horizon h<=2455068=m_1-1, Lemma 1 of predecessor PROOF.md gives that any bounded threshold cell in T_h has width >=epsilon. In the seventh range 2282518<=h<=2455068 we have

h<v_7=2662381,   h<k_7=14525142.

For any bounded cell with left endpoint (v_L,j_L), necessarily v_L<=h<v_7 and j_L<=h<k_7. Choose the SMALLEST i in {1,...,7} such that v_L<=v_i and j_L<=k_i. This exists by the preceding strict inequalities. Define prefix coordinates

k=k_i-j_L >=0, ell=v_i-v_L >=0.

Its score is E(k,ell)=t(v_L,j_L)+delta_i and lies strictly inside the cell: delta_i in (0,epsilon) and every gap is >=epsilon. Its total prefix length equals m_i-(v_L+j_L). If i=1 this is at most n_1; for i>=2, minimality means v_L>=v_(i-1)+1 OR j_L>=k_(i-1)+1>v_(i-1)+1. Thus the length is <=m_i-(v_(i-1)+1)=n_i. The capacities n_i increase for i=1..7, and hence every bounded cell is reached at prefix length <=n_7.

The exterior left cell has E(0,n_7)=-r n_7<-h. The exterior right cell has E(n_7,0)=n_7>r h because 5<r<6 and n_7>6*2455068. Both are explicit padded-prefix witnesses.

Therefore N(h)<=14905515 throughout the stated interval. With the lower bound, equality follows for all integers h in 2282518..2455068. QED.

## Verifier and next question

VERIFY_SEVENTH.py recomputes strict rational logarithm bounds by 45-term atanh with explicit rational remainder, proves 4epsilon<7eta<5epsilon and the exact integer coordinates, n_7, and exterior inequalities. RUN_SEVENTH.txt contains actual stdout. The quantified all-cell proof is symbolic above.

The seventh interval stops at h=2455068 because at h=m_1=2455069 the lattice difference w itself becomes eligible, so the minimum-separation lemma's hypothesis h<m_1 expires. This is a concrete next transition to analyze: determine exact N(2455069) or prove the next plateau using a sharpened finite-vector gap classification that includes w. Also retain lawful six-source/ten-label S23 mother-model bridge and four-observation minimax delta_4 as separate questions.

BRC application: joint counts of labels 1 and 4 and label-3 padding retained. No native X6 realization or review status is asserted.
