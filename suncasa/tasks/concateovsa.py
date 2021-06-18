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
import task_concateovsa
def concateovsa(vis='', concatvis='', datacolumn='corrected', keep_orig_ms=True, cols2rm='model,corrected', freqtol='', dirtol='', respectname=False, timesort=True, copypointing=True, visweightscale=[], forcesingleephemfield=''):

        """Concatenate several EOVSA visibility data sets.
        concateovsa(vis=['UDB20180102161402.ms','UDB20180102173518.ms'], concatvis='UDB20180102_allday.ms')
        will concatenate 'UDB20180102161402.ms' and 'UDB20180102173518.ms' into 'UDB20180102_allday.ms'
    
        """
        if type(visweightscale)==float: visweightscale=[visweightscale]

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['concatvis'] = concatvis
        mytmp['datacolumn'] = datacolumn
        mytmp['keep_orig_ms'] = keep_orig_ms
        mytmp['cols2rm'] = cols2rm
        mytmp['freqtol'] = freqtol
        mytmp['dirtol'] = dirtol
        mytmp['respectname'] = respectname
        mytmp['timesort'] = timesort
        mytmp['copypointing'] = copypointing
        mytmp['visweightscale'] = visweightscale
        mytmp['forcesingleephemfield'] = forcesingleephemfield
	pathname="file:///Users/fisher/Dropbox/PycharmProjects/suncasa/tasks/"
	trec = casac.utils().torecord(pathname+'concateovsa.xml')

        casalog.origin('concateovsa')
        if trec.has_key('concateovsa') and casac.utils().verify(mytmp, trec['concateovsa']) :
	    result = task_concateovsa.concateovsa(vis, concatvis, datacolumn, keep_orig_ms, cols2rm, freqtol, dirtol, respectname, timesort, copypointing, visweightscale, forcesingleephemfield)

	else :
	  result = False
        return result
