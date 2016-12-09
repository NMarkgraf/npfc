---
author: Norman Markgraf
title: Pandoc some block examples
lang: en
theme: Boadilla
papersize: A4
fontsize: 10pt
header-includes: 
	\input{persons.tex}
	\input{moreblocks.tex}
moreblocks:
	theorem: theorem
---
# pandoc persons example

## Just put in some pictures of great scientist

### {.personbegin person=Vieta}

#### of Vieta {.theorem}

If $x_0$ and $x_1$ are the roots of $x^2+px+q=0$, than $p=-(x_0 + x_1)$ and $q=x_0 \cdot x_1$.

#### {.proof}

$(x-x_0) \cdot (x-x_1) = x^2 - (x_0+x_1) \cdot x + x_0 \cdot x_1$

### {.personend}

Wow!

## The End!

Well, much to do!

To process this try:

```
pandoc --from=markdown --to=json addpersons.md  | \
./moreblocks.py beamer | ./addperson.py beamer | \
pandoc --from=json --to=beamer -s -o addpersons.pdf
```

or

```
pandoc --from=markdown --to=beamer \
--filter=moreblocks.py --filter=addperson.py \ 
addpersons.md -o addpersons.pdf
```