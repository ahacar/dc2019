# various python and casa things
#

# the ones likely we use at DC2019
ALL = uvcombine turbustat QAC WidebandSDINT

help:
	@echo Sorry, No help, read the Makefile

all: $(ALL)

#           Only make this when you have the right python
uvcombine:
	git clone https://github.com/keflavich/uvcombine
	(cd uvcombine; python setup.py install)
	pip install image_registration radio_beam reproject spectral_cube

#   @todo  still need to resolve why
#          import turbustat.simulator
#
#          from turbustat.simulator.gen_field import make_extended
#          from turbustat.statistics import psds
turbustat:
	pip install turbustat sklearn statsmodels scikit-image



QAC:
	git clone https://github.com/teuben/QAC/

analysis_scripts.tar:
	wget ftp://ftp.cv.nrao.edu/pub/casaguides/analysis_scripts.tar


#       rubbl has some new CASA based tools and interfaces via rust
peel:
	git clone https://github.com/pkgw/rubbl-rxpackage
	git clone https://github.com/pkgw/rubbl

#       See also: https://www.rust-lang.org/tools/install
rust:
	curl https://sh.rustup.rs -sSf | sh

sd2018:
	git clone https://github.com/teuben/sd2018

rica:
	git clone https://gitlab.com/mileslucas/rica

WidebandSDINT:
	git clone https://github.com/urvashirau/WidebandSDINT


#     http://montage.ipac.caltech.edu/
montage: Montage
	(cd Montage; make clean all)

Montage:
	git clone https://github.com/Caltech-IPAC/Montage

memo:   DataComb_Memo_Template

DataComb_Memo_Template: 
	git clone https://github.com/teuben/DataComb_Memo_Template

Obit:
	git clone https://github.com/bill-cotton/Obit

# i had to install 'flex' to make the compilation work
carma-miriad:
	git clone https://github.com/pkgw/carma-miriad
	(cd carma-miriad; ./autogen.sh ; ./configure --prefix=`pwd`/build F77=gfortran ; make; make install)
	echo source `pwd`/carma-miriad/automiriad.sh  > miriad_start.sh
	echo source `pwd`/carma-miriad/automiriad.csh > miriad_start.csh

SoFIA:
	git clone https://github.com/SoFiA-Admin/SoFiA
	(cd SoFIA; python setup.py build --no-gui=True )
