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
import task_pimfit
def pimfit(imagefiles=[''], ncpu=8, doreg=False, ephemfile='', timestamps=[''], msinfofile='', box='', region='', chans='', stokes='', mask='', includepix=[], excludepix=[], residual='', model='', estimates='', logfile='', append=True, newestimates='', complist='', overwrite=False, dooff=False, offset=0.0, fixoffset=False, stretch=False, rms=-1, noisefwhm='', summary=''):

        """Fit one or more elliptical Gaussian components on an image region(s)
PARAMETER SUMMARY
imagename        Name of the input image
box              Rectangular region(s) to select in direction plane. See "help par.box"
                 for details. Default is to use the entire direction plane.
                 eg "100, 120, 200, 220, 300, 300, 400, 400" to use two boxes.
region           Region selection. See "help par.region" for details. Default is to use
                 the full image.
chans            Channels to use. See "help par.chans" for details. Default is to use all
                 channels.
stokes           Stokes planes to use. See "help par.stokes" for details. Default is to
                 use first Stokes plane.
mask             Mask to use. See help par.mask. Default is none.
includepix       Range of pixel values to include for fitting. Array of two numeric
                 values assumed to have same units as image pixel values. Only one
                 of includepix or excludepix can be specified.
excludepix       Range of pixel values to exclude for fitting. Array of two numeric
                 values assumed to have same units as image pixel values. Only one
                 of includepix or excludepix can be specified.
residual         Name of the residual image to write.
model            Name of the model image to write.
estimates        Name of file containing initial estimates of component parameters
                 (see below for formatting details).
logfile          Name of file to write fit results.
append           If logfile exists, append to it (True) or overwrite it (False).
newestimates     File to write fit results which can be used as initial estimates
                 for next run.
complist         Name of output component list table.
overwrite        Overwrite component list table if it exists?
dooff            Simultaneously fit a zero-level offset?
offset           Initial estimate for the zero-level offset. Only used if dooff is True.
fixoffset        Hold zero-level offset constant during fit? Only used if dooff is True.
stretch          Stretch the input mask if necessary and possible. Only used if a mask is specified.
                 See help par.stretch.
rms              RMS to use in calculation of various uncertainties, assumed to have units of the input
                 image. If not positve, the rms of the residual image is used.
noisefwhm        Noise correlation beam FWHM. If numeric value, interpreted as pixel widths. If
                 quantity (dictionary, string), it must have angular units.
summary          File name to which to write table of fit parameters.

OVERVIEW
This application is used to fit one or more two dimensional gaussians to sources in an image as
well as an optional zero-level offset. Fitting is limited to a single polarization
but can be performed over several contiguous spectral channels.
If the image has a clean beam, the report and returned dictionary will contain both the convolved
and the deconvolved fit results.

When dooff is False, the method returns a dictionary with three keys, 'converged', 'results',
and 'deconvolved'. The value of 'converged' is a boolean array which indicates if the fit
converged on a channel by channel basis. The value of 'results' is a dictionary representing
a component list reflecting the fit results. In the case of an image containing beam information,
the sizes and position angles in the 'results' dictionary are those of the source(s) convolved
with the restoring beam, while the same parameters in the 'deconvolved' dictionary represent the
source sizes deconvolved from the beam. In the case where the image does not contain a beam,
'deconvolved' will be absent. Both the 'results' and 'deconvolved' dictionaries can
be read into a component list tool (default tool is named cl) using the fromrecord() method
for easier inspection using tool methods, eg

cl.fromrecord(res['results'])

although this currently only works if the flux density units are conformant with Jy.

There are also values in each component subdictionary not used by cl.fromrecord() but meant to
supply additional information. There is a 'peak' subdictionary for each component that provides the
peak intensity of the component. It is present for both 'results' and 'deconvolved' components.
There is also a 'sum' subdictionary for each component indicated the simple sum of pixel values in
the the original image enclosed by the fitted ellipse. There is a 'channel' entry in the 'spectrum'
subdictionary which provides the zero-based channel number in the input image for which the solution
applies. In addtion, if the image has a beam(s), then there will be a 'beam' subdictionary associated
with each component in both the 'results' and 'deconvolved' dictionaries. This subdictionary will
have three keys: 'beamarcsec' will be a subdictionary giving the beam dimensions in arcsec,
'beampixels' will have the value of the beam area expressed in pixels, and 'beamster' will have the
value of the beam area epressed in steradians. Also, if the image has a beam(s), in the component level
dictionaries will be an 'ispoint' entry with an associated boolean value describing if the component
is consistent with a point source.

If dooff is True, in addtion to the specified number of
gaussians, a zero-level offset will also be fit. The initial estimate for this
offset is specified using the offset parameter. Units are assumed to be the
same as the image brightness units. The zero level offset can be held constant during
the fit by specifying fixoffset=True. In the case of dooff=True, the returned
dictionary contains two additional keys, 'zerooff' and 'zeroofferr', which are both
dictionaries containing 'unit' and 'value' keys. The values associated with the 'value'
keys are arrays containing the the fitted zero level offset value and its error, respectively,
for each channel. In cases where the fit did not converge, these values are set to NaN.
The value associated with 'unit' is just the i`mage brightness unit.

The region can either be specified by a box(es) or a region.
Ranges of pixel values can be included or excluded from the fit. If specified using
the box parameter, multiple boxes can be given using the format
box="blcx1, blcy1, trcx1, trcy1, blcx2, blcy2, trcx2, trcy2, ... , blcxN, blcyN, trcxN, trcyN"
where N is the number of boxes. In this case, the union of the specified boxes will be used.

If specified, the residual and/or model images for successful fits will be written.

If an estimates file is not specified, an attempt is made to estimate
initial parameters and fit a single Gaussian. If a multiple Gaussian fit
is desired, the user must specify initial estimates via a text file
(see below for details). 

The user has the option of writing the result of the fit to a log file,
and has the option of either appending to or overwriting an existing file.

The user has the option of writing the (convolved) parameters of a successful
fit to a file which can be fed back to fitcomponents() as the estimates file for a
subsequent run.

The user has the option of writing the fit results in tabular format to a file whose
name is specified using the summary parameter.

If specified and positive, the value of rms is used to calculate the parameter uncertainties,
otherwise, the rms in the selected region in the relevant channel is used for these calculations.

The noisefwhm parameter represents the noise-correlation beam FWHM. If specified as a quantity,
it should have angular units. If specified as a numerical value, it is set equal to that number
of pixels. If specified and greater than or equal to the pixel size, it is used to calculate
parameter uncertainties using the correlated noise equations (see below). If it is specified but
less than a pixel width, the the uncorrelated noise equations (see below) are used to
compute the parameter uncertainties. If it is not specified and the image has a restoring beam(s),
the the correlated noise equations are used to compute parameter uncertainties using the
geometric mean of the relevant beam major and minor axes as the noise-correlation beam FWHM. If
noisefwhm is not specified and the image does not have a restoring beam, then the uncorrelated
noise equations are used to compute the parameter uncertainties.

SUPPORTED UNITS

Currently only images with brightness units conformant with Jy/beam, Jy.km/s/beam, and K are fully
supported for fitting. If your image has some other base brightness unit, that unit will be assumed
to be equivalent to Jy/pixel and results will be calculated accordingly. In particular,
the flux density (reported as Integrated Flux in the logger and associated with the "flux" key
in the returned component subdictionary(ies)) for such a case represents the sum of pixel values.

Note also that converting the returned results subdictionary to a component list via cl.fromrecord() currently
only works properly if the flux density units in the results dictionary are conformant with Jy.
If you need to be able to run cl.fromrecord() on the resulting dictionary you can first modify the
flux density units by hand to be (some prefix)Jy and then run cl.fromrecord() on that dictionary,
bearing in mind your unit conversion.

If the input image has units of K, the flux density of components will be reported in units
of [prefix]K*rad*rad, where prefix is an SI prefix used so that the numerical value is between
1 and 1000. To convert to units of K*beam, determine the area of the appropriate beam,
which is given by pi/(4*ln(2))*bmaj*bmin, where bmaj and bmin are the major and minor axes
of the beam, and convert to steradians (=rad*rad). This value is included in the beam portion
of the component subdictionary (key 'beamster'). Then divide the numerical value of the
logged flux density by the beam area in steradians. So, for example


# run on an image with K brightness units
res = imfit(...)
# get the I flux density in K*beam of component 0
comp = res['results']['component0']
flux_density_kbeam = comp['flux']['value'][0]/comp['beam']['beamster']


FITTING OVER MULTIPLE CHANNELS

For fitting over multiple channels, the result of the previous successful fit is used as
the estimate for the next channel. The number of gaussians fit cannot be varied on a channel
by channel basis. Thus the variation of source structure should be reasonably smooth in
frequency to produce reliable fit results.

MASK SPECIFICATION

Mask specification can be done using an LEL expression. For example

mask = '"myimage"\>5' will use only pixels with values greater than 5.

INCLUDING AND EXCLUDING PIXELS

Pixels can be included or excluded from the fit based on their values
using these parameters. Note that specifying both is not permitted and
will cause an error. If specified, both take an array of two numeric
values.

ESTIMATES

Initial estimates of fit parameters may be specified via an estimates
text file. Each line of this file should contain a set of parameters for
a single gaussian. Optionally, some of these parameters can be fixed during
the fit. The format of each line is

peak intensity, peak x-pixel value, peak y-pixel value, major axis, minor axis, position angle, fixed

The fixed parameter is optional. The peak intensity is assumed to be in the
same units as the image pixel values (eg Jy/beam). The peak coordinates are specified
in pixel coordinates. The major and minor axes and the position angle are the convolved
parameters if the image has been convolved with a clean beam and are specified as quantities.
The fixed parameter is optional and is a string. It may contain any combination of the
following characters 'f' (peak intensity), 'x' (peak x position), 'y' (peak y position),
'a' (major axis), 'b' (minor axis), 'p' (position angle).

In addition, lines in the file starting with a \# are considered comments.

An example of such a file is:


# peak intensity must be in map units
120, 150, 110, 23.5arcsec, 18.9arcsec, 120deg  
90, 60, 200, 46arcsec, 23arcsec, 140deg, fxp



This is a file which specifies that two gaussians are to be simultaneously fit,
and for the second gaussian the specified peak intensity, x position, and position angle
are to be held fixed during the fit.

ERROR ESTIMATES

Error estimates are based on the work of Condon 1997, PASP, 109, 166. Key assumptions made are:
  * The given model (elliptical Gaussian, or elliptical Gaussian plus constant offset) is an
    adequate representation of the data
  * An accurate estimate of the pixel noise is provided or can be derived (see above). For the
    case of correlated noise (e.g., a CLEAN map), the fit region should contain many "beams" or
    an independent value of rms should be provided.
  * The signal-to-noise ratio (SNR) or the Gaussian component is large. This is necessary because
    a Taylor series is used to linearize the problem. Condon (1997) states that the fractional
    bias in the fitted amplitude due to this assumption is of order 1/(S*S), where S is the overall
    SNR of the Gaussian with respect to the given data set (defined more precisely below). For a 5
    sigma "detection" of the Gaussian, this is a 4% effect.
  * All (or practically all) of the flux in the component being fit falls within the selected region.
    If a constant offset term is simultaneously fit and not fixed, the region of interest should be
    even larger. The derivations of the expressions summarized in this note assume an effectively
    infinite region.
    
Two sets of equations are used to calculate the parameter uncertainties, based on if
the noise is correlated or uncorrelated. The rules governing which set of equations are 
used have been described above in the description of the noisefwhm parameter. 

In the case of uncorrelated noise, the equations used are

f(A) = f(I) = f(M) = f(m) = k*s(x)/M = k*s(y)/m = (s(p)/sqrt(2))*((M*M - m*m)/(M*m))
   = sqrt(2)/S

where s(z) is the uncertainty associated with parameter z, f(z) = s(z)/abs(z) is the
fractional uncertainty associated with parameter z, A is the peak intensity, I is the flux
density, M  and m are the FWHM major and minor axes, p is the position angle of the
component, and k = sqrt(8*ln(2)). s(x) and s(y) are the direction
uncertainties of the component measured along the major and minor axes; the resulting
uncertainties measured along the principle axes of the image direction coordinate are
calculated by propagation of errors using the 2D rotation matrix which enacts the rotation through
the position angle plus 90 degrees. S is the overall signal to noise ratio of the component,
which, for the uncorrelated noise case is given by

S = (A/(k*h*r))*sqrt(pi*M*m)

where h is the pixel width of the direction coordinate and r is the rms noise (see the
discussion above for the rules governing how the value of r is determined).

For the correlated noise case, the same equations are used to determine the uncertainties
as in the uncorrelated noise case, except for the uncertainty in I (see below). However,
S is given by

S = (A/(2*r*N)) * sqrt(M*m) * (1 + ((N*N/(M*M)))**(a/2)) * (1 + ((N*N/(m*m)))**(b/2))

where N is the noise-correlation beam FWHM (see discussion of the noisefwhm parameter for 
rules governing how this value is determined). "**" indicates exponentiation and a and b
depend on which uncertainty is being calculated. For sigma(A), a = b = 3/2. For M and x,
a = 5/2 and b = 1/2. For m, y, and p, a = 1/2 and b = 5/2. f(I) is calculated in the
correlated noise case according to

f(I) = sqrt( f(A)*f(A) + (N*N/(M*m))*(f(M*f(M) + f(m)*f(m))) )

Note well the following caveats:
  * Fixing Gaussian component parameters will tend to cause the parameter uncertainties reported for free
    parameters to be overestimated.
  * Fitting a zero level offset that is not fixed will tend to cause the reported parameter
    uncertainties to be slightly underestimated.
  * The parameter uncertainties will be inaccurate at low SNR (a ~10% for SNR = 3).
  * If the fitted region is not considerably larger than the largest component that is fit,
    parameter uncertainties may be mis-estimated.
  * An accurate rms noise measurement, r, for the region in question must be supplied.
    Alternatively, a sufficiently large signal-free region must be present in the selected region
    (at least about 25 noise beams in area) to auto-derive such an estimate.
  * If the image noise is not statistically independent from pixel to pixel, a reasonably accurate noise
    correlation scale, N, must be provided. If the noise correlation function is not approximately Gaussian,
    the correlation length can be estimated using
    
    N = sqrt(2*ln(2)/pi)* double-integral(dx dy C(x,y))/sqrt(double-integral(dx dy C(x, y) * C(x,y)))
    
    where C(x,y) is the associated noise-smoothing function
  * If fitted model components have significan spatial overlap, the parameter uncertainties are likely to
    be mis-estimated (i.e., correlations between the parameters of separate components are not accounted
    for).
  * If the image being analyzed is an interferometric image with poor uv sampling, the parameter
    uncertainties may be significantly underestimated.

The deconvolved size and position angle errors are computed by taking the maximum of the absolute values of the
differences of the best fit deconvolved value of the given parameter and the deconvolved size of the eight
possible combinations of (FWHM major axis +/- major axis error), (FWHM minor axis +/- minor axis error),
and (position andle +/- position angle error). If the source cannot be deconvolved from the beam (if the best
fit convolved source size cannot be deconvolved from the beam), upper limits on the deconvolved source size
are sometimes reported. These limits simply come from the maximum major and minor axes of the deconvolved
gaussians taken from trying all eight of the aforementioned combinations. In the case none of these combinations
produces a deconvolved size, no upper limit is reported.

EXAMPLE:

Here is how one might fit two gaussians to multiple channels of a cube using the fit
from the previous channel as the initial estimate for the next. It also illustrates
how one can specify a region in the associated continuum image as the region to use
as the fit for the channel.



default imfit
imagename = "co_cube.im"
# specify region using region from continuum
region = "continuum.im:source.rgn"
chans = "2~20"
# only use pixels with positive values in the fit
excludepix = [-1e10,0]
# estimates file contains initial parameters for two Gaussians in channel 2
estimates = "initial_estimates.txt"
logfile = "co_fit.log"
# append results to the log file for all the channels
append = "True"
imfit()


        """
        if type(imagefiles)==str: imagefiles=[imagefiles]
        if type(timestamps)==str: timestamps=[timestamps]
        if type(includepix)==int: includepix=[includepix]
        if type(excludepix)==int: excludepix=[excludepix]

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['imagefiles'] = imagefiles
        mytmp['ncpu'] = ncpu
        mytmp['doreg'] = doreg
        mytmp['ephemfile'] = ephemfile
        mytmp['timestamps'] = timestamps
        mytmp['msinfofile'] = msinfofile
        mytmp['box'] = box
        mytmp['region'] = region
        mytmp['chans'] = chans
        mytmp['stokes'] = stokes
        mytmp['mask'] = mask
        mytmp['includepix'] = includepix
        mytmp['excludepix'] = excludepix
        mytmp['residual'] = residual
        mytmp['model'] = model
        mytmp['estimates'] = estimates
        mytmp['logfile'] = logfile
        mytmp['append'] = append
        mytmp['newestimates'] = newestimates
        mytmp['complist'] = complist
        mytmp['overwrite'] = overwrite
        mytmp['dooff'] = dooff
        mytmp['offset'] = offset
        mytmp['fixoffset'] = fixoffset
        mytmp['stretch'] = stretch
        mytmp['rms'] = rms
        mytmp['noisefwhm'] = noisefwhm
        mytmp['summary'] = summary
	pathname="file:///Users/fisher/Dropbox/PycharmProjects/suncasa/tasks/"
	trec = casac.utils().torecord(pathname+'pimfit.xml')

        casalog.origin('pimfit')
        if trec.has_key('pimfit') and casac.utils().verify(mytmp, trec['pimfit']) :
	    result = task_pimfit.pimfit(imagefiles, ncpu, doreg, ephemfile, timestamps, msinfofile, box, region, chans, stokes, mask, includepix, excludepix, residual, model, estimates, logfile, append, newestimates, complist, overwrite, dooff, offset, fixoffset, stretch, rms, noisefwhm, summary)

	else :
	  result = False
        return result
