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
from itertools import compress

r.seed(33)

# voc = s.ascii_lowercase
voc_sz = 8
voc = [s.ascii_lowercase[i] for i in range(voc_sz)]
kw = "e"
p_len = 4
n_pgs = 8
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

# Search by keyword
print("searching for:", kw)
contains_kw = lambda k, p: k in p
p_kw = [contains_kw(kw, p) for p in P]
p_kw_ix = list(compress(range(n_pgs), p_kw))
print("pages containing", kw, p_kw_ix)

# Score pages by number of backlinks
S = [len(b) for b in B]
print("page scores:", S)

# Return best scored page containing the keyword
# TODO sort this out
R = sorted(range(len(p_kw)), key=lambda k: p_kw[k])
print("found pages in order:", R)

# END CODE

# MAINLOOP
if __name__ == '__main__':
    pass
