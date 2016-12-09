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

EXAMPLEDIRS = addpersons
EXAMPLEDIRS += moreblocks
EXAMPLEDIRS += splitbockold

# --------------------------------------------------------------------------------------
#
#
.PHONY: clean propper all

# --------------------------------------------------------------------------------------
#
#

all: 
	for dir in $(EXAMPLEDIRS); do \
		$(MAKE) -C $$dir all; \
	done 

propper: 
	for dir in $(EXAMPLEDIRS); do \
		$(MAKE) -C $$dir propper; \
	done 

clean: 
	for dir in $(EXAMPLEDIRS); do \
		$(MAKE) -C $$dir clean; \
	done 

# --------------------------------------------------------------------------------------
#
#

info: 
	@echo "########################################################################"
	@echo ""
	@echo "Makefile (C) in 2015,16 by Norman Markgraf"
	@echo "========-------------------------------"
	@echo "Version: $(MAKEFILEVERSION)"
	@echo ""
	@echo "************************************************************************"
