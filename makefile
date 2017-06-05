# ######################################################################################
# Makefile (C) in 2016 by Norman Markgraf
# ========
# Version 1.0 	nm (09. Dec. 2016) 	First Release
MAKEFILEVERSION=1.0
#
# ######################################################################################

# --------------------------------------------------------------------------------------
#  Setup local variables
#


PANDOCNEW = pandoc
PANDOCOLD = ~/Development/pandoc-1.17.2/.stack-work/install/x86_64-osx/nightly-2016-07-11/8.0.1/bin/pandoc

PANDOC = $(PANDOCNEW)

# --------------------------------------------------------------------------------------
#
#
.PHONY: clean propper all examples


# --------------------------------------------------------------------------------------
# 
# for testing purpos generate some 'in the middle' output 

%.json: %.md
	$(PANDOC) --from=markdown --to=json $< -o $@

%.native: %.md
	$(PANDOC) --from=markdown --to=native $< -o $@


%.old.json: %.md
	$(PANDOCOLD) --from=markdown --to=json $< -o $@

%.old.native: %.md
	$(PANDOCOLD) --from=markdown --to=native $< -o $@

%.old.filtered.json: %.md
	$(PANDOCOLD) --from=markdown --to=json --filter ./moreblocks $< -o $@

%.old.filtered.native: %.md
	$(PANDOCOLD) --from=markdown --to=native --filter ./moreblocks $< -o $@


%.new.json: %.md
	$(PANDOCNEW) --from=markdown --to=json $< -o $@

%.new.native: %.md
	$(PANDOCNEW) --from=markdown --to=native $< -o $@

%.pdf: %.md
	$(PANDOC) --filter moreblocks --from=markdown --to=beamer $< -o $@

%.tex: %.md
	$(PANDOC) --filter moreblocks --from=markdown --to=beamer $< -o $@

%.new.filtered.json: %.md
	$(PANDOCOLD) --from=markdown --to=json --filter ./moreblock.py $< -o $@

%.new.filtered.native: %.md
	$(PANDOCOLD) --from=markdown --to=native --filter ./moreblock.py $< -o $@


# --------------------------------------------------------------------------------------
#
# Gerate the README.(rst/tex/pdf) files out of the (main) README.md file, if needed
#
READMEOPTS = --from=markdown+backtick_code_blocks --highlight-style=tango --normalize --smart --standalone

README.rst:
	$(PANDOC) $(READMEOPTS) --to=rst README.md --output=README.rst

README.pdf:
	$(PANDOC) $(READMEOPTS) --to=latex README.md --output=README.pdf

README.tex:
	$(PANDOC) $(READMEOPTS) --to=latex README.md --output=README.tex


# --------------------------------------------------------------------------------------
#
#
clean:
	-rm -rf moreblocks.hi moreblocks.o
	-rm -rf README.pdf README.tex
	-rm -rf *.synctex.gz *.aux *.log *.out *.vrb *.toc *.nav *.snm 
	$(MAKE) -C examples clean


# --------------------------------------------------------------------------------------
#
#
propper: clean
	-rm -rf README.rst
	$(MAKE) -C examples propper


# --------------------------------------------------------------------------------------
#
#
examples:
	$(MAKE) -C examples


# --------------------------------------------------------------------------------------
#
#
all: examples

info: 
	@echo "########################################################################"
	@echo ""
	@echo "Makefile (C) in 2015-17 by Norman Markgraf"
	@echo "========----------------------------------"
	@echo "Version: $(MAKEFILEVERSION)"
	@echo ""
	@echo "************************************************************************"
