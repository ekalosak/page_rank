# Implement PageRank algorithm

# INTRODUCTION
# page is a body of text, a string of 10^3s of characters in an array
# in a page are links to other pages (often e.g. "http://")
# links to that page are backlinks

# a page's score is determined by the number of backlinks to the page.
# That is, $sco(p_j) = \sum_{p\in P} l_{p,j} = \sum_{p\in P} b_{j,p}$.

# when keywords are searched, the crawled text of the internet is indexed for
# keywords, and pages from the keyword search are ordered by score.

# search a small library of pages for keyword containment
# each page has an associated list of backlinks
# the score of a page is the length of its list of backlinks
#   i.e. how many pages link to it
#
# SOURCES
# 1. https://stackoverflow.com/questions/7851077/how-to-return-index-of-a-sorted-list
# 2. Bryan-Leise-SIAM2006

# BEGIN CODE
import random as r
import string as s
import math as m
import pdb
from itertools import compress

r.seed(33)

# voc = s.ascii_lowercase
voc_sz = 3
voc = [s.ascii_lowercase[i] for i in range(voc_sz)]
kw = "a"
p_len = 2
n_pgs = 4
n_rescore = 5
print("using vocab:", voc)

# Generate pages with process on limited vocabulary
make_page = lambda: r.sample(voc, p_len) # w.o replacement
# p0 = make_page() # make one, see what it looks like
# print(p0)

P = [make_page() for i in range(n_pgs)]
assert(len(P)==n_pgs)
print("made", len(P), "pages:")
for p in P:
    print(p)

# Generate random links to other pages
make_len_b = lambda: m.floor(r.uniform(0, n_pgs))
B = [r.sample(range(n_pgs), make_len_b()) for i in range(n_pgs)]
print("made backlinks:", B)

# Score pages by number of backlinks
S0 = [len(b) for b in B]
print("initial page scores:", S0)

# Update scoring function with scores of linking pages
# i.e. new score is sum of scores of every backlinked page
rescore = lambda S: [sum([S[p] for p in b]) for b in B]
S = S0
for i in range(n_rescore):
    S = rescore(S)
print("final page scores:", S)

# Return best scored pages out of all pages (not kw filtered)
R = list(reversed(sorted(range(len(S)), key=lambda k: S[k])))
print("scored pages in order:", R)

# Search by keyword
print("searching for:", kw)
contains_kw = lambda k, p: k in p
p_kw = [contains_kw(kw, p) for p in P]
p_kw_ix = list(compress(range(n_pgs), p_kw))
print("pages containing", kw, p_kw_ix)

# Return kw matches sorted by score
Q = [r for r in R if r in p_kw_ix]
print("returning query:", Q)

# END CODE

# MAINLOOP
if __name__ == '__main__':
    pass
