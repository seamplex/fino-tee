import sys
# state file generated using paraview version 5.1.2

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1120, 861]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesVisibility = 0
renderView1.OrientationAxesLabelColor = [0.0, 0.0, 0.0]
renderView1.OrientationAxesOutlineColor = [0.0, 0.0, 0.0]
renderView1.CenterOfRotation = [323.799987792969, 80.9499969482422, 242.849990844727]
renderView1.StereoType = 0
renderView1.CameraPosition = [-713.829393529511, -1359.34800262718, 699.923180519492]
renderView1.CameraFocalPoint = [208.643795277286, -30.6105081733542, 264.369206454588]
renderView1.CameraViewUp = [0.133828884281519, 0.223562321736512, 0.965458294299523]
renderView1.CameraParallelScale = 524.615939758465
renderView1.Background = [1.0, 1.0, 1.0]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView1.AxesGrid.XTitleColor = [0.0, 0.0, 0.0]
renderView1.AxesGrid.YTitleColor = [0.0, 0.0, 0.0]
renderView1.AxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
renderView1.AxesGrid.GridColor = [0.0, 0.0, 0.0]
renderView1.AxesGrid.XLabelColor = [0.0, 0.0, 0.0]
renderView1.AxesGrid.YLabelColor = [0.0, 0.0, 0.0]
renderView1.AxesGrid.ZLabelColor = [0.0, 0.0, 0.0]

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'Legacy VTK Reader'
teevtk = LegacyVTKReader(FileNames=['tee-%s.vtk'%sys.argv[1]])

# create a new 'Warp By Vector'
warpByVector1 = WarpByVector(Input=teevtk)
warpByVector1.Vectors = ['POINTS', 'u-v-w']
warpByVector1.ScaleFactor = 400.0

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get color transfer function/color map for 'sigma'
sigmaLUT = GetColorTransferFunction('sigma')
sigmaLUT.LockDataRange = 1
sigmaLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 225.0, 0.865003, 0.865003, 0.865003, 450.0, 0.705882, 0.0156863, 0.14902]
sigmaLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'sigma'
sigmaPWF = GetOpacityTransferFunction('sigma')
sigmaPWF.Points = [0.0, 0.0, 0.5, 0.0, 450.0, 1.0, 0.5, 0.0]
sigmaPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from warpByVector1
warpByVector1Display = Show(warpByVector1, renderView1)
# trace defaults for the display properties.
warpByVector1Display.AmbientColor = [0.0, 0.0, 0.0]
warpByVector1Display.ColorArrayName = ['POINTS', 'sigma']
warpByVector1Display.DiffuseColor = [1.0, 0.6666666666666666, 1.0]
warpByVector1Display.LookupTable = sigmaLUT
warpByVector1Display.BackfaceDiffuseColor = [1.0, 0.6666666666666666, 1.0]
warpByVector1Display.OSPRayScaleArray = 'sigma'
warpByVector1Display.OSPRayScaleFunction = 'PiecewiseFunction'
warpByVector1Display.GlyphType = 'Arrow'
warpByVector1Display.ScalarOpacityUnitDistance = 28.859754037533

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(None)
# ----------------------------------------------------------------

GetRenderView().ViewSize = [1200,1000]
GetRenderView().Background = [1,1,1]
Render()
WriteImage("tee-post-%s.png"%sys.argv[1])
