---
author: Norman Markgraf
title: Pandoc some block examples
lang: en
theme: Boadilla
papersize: A4
fontsize: 10pt
header-includes: 
	\input{fourquad.tex}
---
# pandoc splitblockold example

## Customizing layout: two columns

### Left {.twocolumnsbegin}

**This is an *old method* to split up the page into two sections.**

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren.

Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat.

### Right {.twocolumnsep}

**It is just for older documents!**

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren.

Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat.

### End {.twocolumnsend}

## Customizing layout: three columns

### Left {.threecolumnsbegin}

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren.

Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat.

### Middle {.threecolumnsep}

Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat. 


### Right {.threecolumnsep}

Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi. 

### End {.threecolumnsend}

## Customizing layout: two columns, one big left

### Left (big) {.twocolumnsbigleftbegin}

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren.

Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat.

Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat. 

### Right (small) {.twocolumnsbigleftsep}

Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi.

### End {.twocolumnsbigleftend}

## Customizing layout: four boxes

### Upper left  {.fourquadone}
ONE is upper left!

### Upper right {.fourquadtwo}
TWO is upper right!

### Lower left  {.fourquadthree}
THREE is lower left!

### Lower right {.fourquadfour}
FOUR is lower right!

### End         {.fourquadend}

## The End! {.twocolumnsbigleftend}

Well, much to do!

To process this try:

```
pandoc --from=markdown --to=json splitblockold.md  | \
./splitblockold.py beamer | \
pandoc --from=json --to=beamer -s -o splitblockold.pdf
```