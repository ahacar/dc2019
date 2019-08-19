# N346 debugging
#

npoint = 500
p      = qac_ms_ptg('region3by3-7M-leiden-avg.ms','12m.ptg')

if False:
    # this will use all 1345 pointings !!!
    tp2vis('new.cube.spw23-forLeiden.image','new.cube.spw23-forLeiden.image.ms','12m.ptg',rms=0.5)
else:
    # use fewer to test if the crash is due to too many fields/pointings
    p1 = p[:npoint]
    tp2vis('new.cube.spw23-forLeiden.image','new.cube.spw23-forLeiden.image.ms',p1,rms=0.5)    

concat(vis=['region3by3-7M-leiden-avg.ms','new.cube.spw23-forLeiden.image.ms'], concatvis='all.ms',copypointing=False)

field = '0~4499'          # fails
field = '0~1345'          # this still includes calibrators.
field = '0~%d' % npoint   # ok

vis = 'all.ms'
# vis = 'region3by3-7M-leiden-avg.ms'

tclean(vis = vis,
       imagename = 'all_tp2vis.image',
       field = field,
       intent = 'OBSERVE_TARGET#ON_SOURCE',
       phasecenter = 3, #00:59:05.089680 -72.10.33.24000 ICRS
       stokes = 'I',
       spw = '0',
       outframe = 'LSRK',
       restfreq = '230.538GHz', # CO 2-1 lab rest freq
       specmode = 'cube',\
       imsize = [640, 640], # 3500 arcsec x 2000 arcsec
       cell = '1.4arcsec',
       deconvolver = 'hogbom',
       niter = 100,
       weighting = 'briggs',
       robust = 0.5,
       mask = '',
       gridder = 'mosaic',
       pbcor = True,
       threshold = '0.02Jy',
       width = '3.333MHz',
       start = '230.405GHz', 
       nchan = 7, 
       interactive = True
)
