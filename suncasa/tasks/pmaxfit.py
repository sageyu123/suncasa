#
# This file was generated using xslt from its XML file
#
# Copyright 2009, Associated Universities Inc., Washington DC
#
import sys
import os
from  casac import *
import string
from taskinit import casalog
from taskinit import xmlpath
#from taskmanager import tm
import task_pmaxfit
def pmaxfit(imagefiles=[''], ncpu=8, box='', width=5):

        """Find maximum and do parabolic fit in the sky


        EXAMPLE:

        Here is how one might fit two gaussians to multiple channels of a cube using the fit
        from the previous channel as the initial estimate for the next. It also illustrates
        how one can specify a region in the associated continuum image as the region to use
        as the fit for the channel.


        
        default pmaxfit
        imagename = "co_cube.im"
        # specify region using region from continuum
        box = "100,120,200,200"
        pmaxfit()
    
        """
        if type(imagefiles)==str: imagefiles=[imagefiles]

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['imagefiles'] = imagefiles
        mytmp['ncpu'] = ncpu
        mytmp['box'] = box
        mytmp['width'] = width
	pathname="file:///Users/fisher/Dropbox/PycharmProjects/suncasa/tasks/"
	trec = casac.utils().torecord(pathname+'pmaxfit.xml')

        casalog.origin('pmaxfit')
        if trec.has_key('pmaxfit') and casac.utils().verify(mytmp, trec['pmaxfit']) :
	    result = task_pmaxfit.pmaxfit(imagefiles, ncpu, box, width)

	else :
	  result = False
        return result
