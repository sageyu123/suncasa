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
import task_ptclean2
def ptclean2(vis='', imageprefix='', imagesuffix='', ncpu=8, twidth=1, doreg=False, usephacenter=False, reftime='', toTb=False, overwrite=False, selectdata=True, field='', spw='', timerange='', uvrange='', antenna='', scan='', observation='', intent='', datacolumn='corrected', imsize=[100], cell=["1arcsec"], phasecenter='', stokes='I', projection='SIN', startmodel='', specmode='mfs', reffreq='', nchan=-1, start='', width='', outframe='LSRK', veltype='radio', restfreq=[], interpolation='linear', gridder='standard', facets=1, chanchunks=1, wprojplanes=1, vptable='', usepointing=False, mosweight=True, aterm=True, psterm=False, wbawp=True, conjbeams=True, cfcache='', computepastep=360.0, rotatepastep=360.0, pblimit=0.2, normtype='flatnoise', deconvolver='hogbom', scales=[], nterms=2, smallscalebias=0.6, restoration=True, restoringbeam=[], pbcor=False, outlierfile='', weighting='natural', robust=0.5, npixels=0, uvtaper=[''], niter=0, gain=0.1, threshold=0.0, nsigma=0.0, cycleniter=-1, cyclefactor=1.0, minpsffraction=0.05, maxpsffraction=0.8, interactive=False, usemask='user', mask='', pbmask=0.0, sidelobethreshold=3.0, noisethreshold=5.0, lownoisethreshold=1.5, negativethreshold=0.0, smoothfactor=1.0, minbeamfrac=0.3, cutthreshold=0.01, growiterations=75, dogrowprune=True, minpercentchange=-1.0, verbose=False, restart=True, savemodel='none', calcres=True, calcpsf=True, parallel=False):

        """Parallelized tclean in consecutive time steps

     This is the first release of our refactored imager code. Although most features have
     been used and validated, there are many details that have not been thoroughly tested.
     Feedback will be much appreciated.


     Usage Examples :
     -----------------------

     (A) A suite of test programs that demo all usable modes of tclean on small test datasets
           https://svn.cv.nrao.edu/svn/casa/branches/release-4_5/gcwrap/python/scripts/tests/test_refimager.py
     (B) A set of demo examples for ALMA imaging
           https://casaguides.nrao.edu/index.php/TCLEAN_and_ALMA



  
        """
        if type(uvtaper)==str: uvtaper=[uvtaper]

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['imageprefix'] = imageprefix
        mytmp['imagesuffix'] = imagesuffix
        mytmp['ncpu'] = ncpu
        mytmp['twidth'] = twidth
        mytmp['doreg'] = doreg
        mytmp['usephacenter'] = usephacenter
        mytmp['reftime'] = reftime
        mytmp['toTb'] = toTb
        mytmp['overwrite'] = overwrite
        mytmp['selectdata'] = selectdata
        mytmp['field'] = field
        mytmp['spw'] = spw
        mytmp['timerange'] = timerange
        mytmp['uvrange'] = uvrange
        mytmp['antenna'] = antenna
        mytmp['scan'] = scan
        mytmp['observation'] = observation
        mytmp['intent'] = intent
        mytmp['datacolumn'] = datacolumn
        mytmp['imsize'] = imsize
        mytmp['cell'] = cell
        mytmp['phasecenter'] = phasecenter
        mytmp['stokes'] = stokes
        mytmp['projection'] = projection
        mytmp['startmodel'] = startmodel
        mytmp['specmode'] = specmode
        mytmp['reffreq'] = reffreq
        mytmp['nchan'] = nchan
        mytmp['start'] = start
        mytmp['width'] = width
        mytmp['outframe'] = outframe
        mytmp['veltype'] = veltype
        mytmp['restfreq'] = restfreq
        mytmp['interpolation'] = interpolation
        mytmp['gridder'] = gridder
        mytmp['facets'] = facets
        mytmp['chanchunks'] = chanchunks
        mytmp['wprojplanes'] = wprojplanes
        mytmp['vptable'] = vptable
        mytmp['usepointing'] = usepointing
        mytmp['mosweight'] = mosweight
        mytmp['aterm'] = aterm
        mytmp['psterm'] = psterm
        mytmp['wbawp'] = wbawp
        mytmp['conjbeams'] = conjbeams
        mytmp['cfcache'] = cfcache
        mytmp['computepastep'] = computepastep
        mytmp['rotatepastep'] = rotatepastep
        mytmp['pblimit'] = pblimit
        mytmp['normtype'] = normtype
        mytmp['deconvolver'] = deconvolver
        mytmp['scales'] = scales
        mytmp['nterms'] = nterms
        mytmp['smallscalebias'] = smallscalebias
        mytmp['restoration'] = restoration
        mytmp['restoringbeam'] = restoringbeam
        mytmp['pbcor'] = pbcor
        mytmp['outlierfile'] = outlierfile
        mytmp['weighting'] = weighting
        mytmp['robust'] = robust
        mytmp['npixels'] = npixels
        mytmp['uvtaper'] = uvtaper
        mytmp['niter'] = niter
        mytmp['gain'] = gain
        mytmp['threshold'] = threshold
        mytmp['nsigma'] = nsigma
        mytmp['cycleniter'] = cycleniter
        mytmp['cyclefactor'] = cyclefactor
        mytmp['minpsffraction'] = minpsffraction
        mytmp['maxpsffraction'] = maxpsffraction
        mytmp['interactive'] = interactive
        mytmp['usemask'] = usemask
        mytmp['mask'] = mask
        mytmp['pbmask'] = pbmask
        mytmp['sidelobethreshold'] = sidelobethreshold
        mytmp['noisethreshold'] = noisethreshold
        mytmp['lownoisethreshold'] = lownoisethreshold
        mytmp['negativethreshold'] = negativethreshold
        mytmp['smoothfactor'] = smoothfactor
        mytmp['minbeamfrac'] = minbeamfrac
        mytmp['cutthreshold'] = cutthreshold
        mytmp['growiterations'] = growiterations
        mytmp['dogrowprune'] = dogrowprune
        mytmp['minpercentchange'] = minpercentchange
        mytmp['verbose'] = verbose
        mytmp['restart'] = restart
        mytmp['savemodel'] = savemodel
        mytmp['calcres'] = calcres
        mytmp['calcpsf'] = calcpsf
        mytmp['parallel'] = parallel
	pathname="file:///Users/fisher/Dropbox/PycharmProjects/suncasa/tasks/"
	trec = casac.utils().torecord(pathname+'ptclean2.xml')

        casalog.origin('ptclean2')
        if trec.has_key('ptclean2') and casac.utils().verify(mytmp, trec['ptclean2']) :
	    result = task_ptclean2.ptclean2(vis, imageprefix, imagesuffix, ncpu, twidth, doreg, usephacenter, reftime, toTb, overwrite, selectdata, field, spw, timerange, uvrange, antenna, scan, observation, intent, datacolumn, imsize, cell, phasecenter, stokes, projection, startmodel, specmode, reffreq, nchan, start, width, outframe, veltype, restfreq, interpolation, gridder, facets, chanchunks, wprojplanes, vptable, usepointing, mosweight, aterm, psterm, wbawp, conjbeams, cfcache, computepastep, rotatepastep, pblimit, normtype, deconvolver, scales, nterms, smallscalebias, restoration, restoringbeam, pbcor, outlierfile, weighting, robust, npixels, uvtaper, niter, gain, threshold, nsigma, cycleniter, cyclefactor, minpsffraction, maxpsffraction, interactive, usemask, mask, pbmask, sidelobethreshold, noisethreshold, lownoisethreshold, negativethreshold, smoothfactor, minbeamfrac, cutthreshold, growiterations, dogrowprune, minpercentchange, verbose, restart, savemodel, calcres, calcpsf, parallel)

	else :
	  result = False
        return result
