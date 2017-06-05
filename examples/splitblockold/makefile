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


PANDOC = pandoc
COPY = cp 

FILTERDIR = ../../
FILTER = --filter $(FILTERDIR)./splitblockold.py  

PANDOCOPT = --standalone

EXAMPLES = splitblockold.md

EXAMPLESPDF = $(EXAMPLES:%.md=%.pdf)
EXAMPLESTEX = $(EXAMPLES:%.md=%.tex)
EXAMPLESHTML = $(EXAMPLES:%.md=%.html)

TEXFILES = fourquad.tex

# --------------------------------------------------------------------------------------
# 
# creating example outputs 


%.pdf: %.md
	$(PANDOC) $(FILTER) $(PANDOCOPT) --from=markdown --to=beamer $< -o $@

%.tex: %.md
	$(PANDOC) $(FILTER) $(PANDOCOPT) --from=markdown --to=beamer $< -o $@

%.html: %.md
	$(PANDOC) $(FILTER) $(PANDOCOPT) --from=markdown --to=html $< -o $@



# --------------------------------------------------------------------------------------
#
#
.PHONY: clean propper version info moreblocks.tex persons.tex 

clean:
	-rm -rf *.synctex.gz *.aux *.log *.out *.vrb *.toc *.nav *.snm 
	-rm -rf $(EXAMPLESPDF) $(EXAMPLESTEX) $(EXAMPLESHTML)

fourquad.tex: 
	$(COPY) ../../fourquad.tex .



# --------------------------------------------------------------------------------------
#
#
propper: clean
	-rm -rf $(TEXFILES)
	echo "Now we are more than clean!"


# --------------------------------------------------------------------------------------
#
#
version: info
	$(PANDOC) --version



all: $(TEXFILES) $(EXAMPLESPDF) $(EXAMPLESTEX) $(EXAMPLESHTML)



info: 
	@echo "########################################################################"
	@echo ""
	@echo "Makefile (C) in 2015-17 by Norman Markgraf"
	@echo "========----------------------------------"
	@echo "Version: $(MAKEFILEVERSION)"
	@echo ""
	@echo "************************************************************************"
