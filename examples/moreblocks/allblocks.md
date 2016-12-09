---
author: Norman Markgraf
title: Pandoc some block examples
lang: en
theme: Boadilla
papersize: A4
fontsize: 10pt
header-includes: \input{moreblocks.tex}
moreblocks:
	theorem: theorem
---
# pandoc moreblocks example

## Give some more block types

Three kind of new BlockTypes:

#### One Example {.example}

This is a single example.


#### A couple of Examples {.examples}
- This is a single example.
- This is anotherone.

#### A Definition Block {.definition}
The master Thesis:
\begin{equation*}
	e=mc^2
\end{equation*}
to be or not to be!

## Next page

#### A Theorem {.theorem}

Yes! We need some! ;-)

#### Some facts {.facts}
- Mmmm
- Maybe some more facts

#### A fact {.fact}

Just a fact to believ!

## Another page

#### An exercise {.exercise}

Do it!

#### The solution {.solution}

I did it!

#### Lemma {.lemma}

Not the one of Zorn!

## And another one

#### Proof ... {.proof}

... it or not!

## The endblock tag:

Normal Text

#### A Remark {.remark}
Some remarks

#### {.endblock}

Normal Text

#### Some remarks {.remarks}
- One
- Two
- Three

## The End!

Well, much to do!

To process this try:

```
pandoc --from=markdown --to=json allblocks.md  | \
./moreblocks.py beamer | \
pandoc --from=json --to=beamer -s -o allblocks.pdf
```