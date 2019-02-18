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
renderView1.OrientationAxesLabelColor = [0.0, 0.0, 0.0]
renderView1.OrientationAxesOutlineColor = [0.0, 0.0, 0.0]
renderView1.CenterOfRotation = [323.799987792969, 79.331, 242.849987792969]
renderView1.StereoType = 0
renderView1.CameraPosition = [-1704.13500065525, -79.8907110083458, 45.0487018036855]
renderView1.CameraFocalPoint = [323.799987792969, -79.8907110083458, 45.0487018036855]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 244.854887649912
renderView1.CameraParallelProjection = 1
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

# create a new 'Legacy VTK Reader'
sclsvtk = LegacyVTKReader(FileNames=['scls-%s.vtk'%sys.argv[1]])

# create a new 'Tube'
tube1 = Tube(Input=sclsvtk)
tube1.Scalars = ['POINTS', 'SCLs']
tube1.Vectors = [None, '']
tube1.NumberofSides = 20
tube1.Radius = 3.238

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get color transfer function/color map for 'SCLs'
sCLsLUT = GetColorTransferFunction('SCLs')
sCLsLUT.LockDataRange = 1
sCLsLUT.RGBPoints = [-2.0, 0.0, 0.0, 1.0, -0.838, 0.0, 0.0, 1.0, -0.831, 1.0, 0.0, 1.0, 0.324000000000001, 1.0, 0.0, 1.0, 0.331, 0.0, 1.0, 1.0, 1.5, 0.0, 1.0, 1.0, 1.507, 0.0, 1.0, 0.0, 2.662, 0.0, 1.0, 0.0, 2.669, 1.0, 1.0, 0.0, 3.824, 1.0, 1.0, 0.0, 3.831, 1.0, 0.0, 0.0, 5.0, 1.0, 0.0, 0.0]
sCLsLUT.ColorSpace = 'HSV'
sCLsLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'SCLs'
sCLsPWF = GetOpacityTransferFunction('SCLs')
sCLsPWF.Points = [-2.0, 0.0, 0.5, 0.0, 5.0, 1.0, 0.5, 0.0]
sCLsPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from teevtk
teevtkDisplay = Show(teevtk, renderView1)
# trace defaults for the display properties.
teevtkDisplay.AmbientColor = [0.0, 0.0, 0.0]
teevtkDisplay.ColorArrayName = ['POINTS', '']
teevtkDisplay.DiffuseColor = [0.576470588235294, 0.576470588235294, 0.576470588235294]
teevtkDisplay.Opacity = 0.6
teevtkDisplay.BackfaceDiffuseColor = [1.0, 0.6666666666666666, 1.0]
teevtkDisplay.OSPRayScaleArray = 'sigma'
teevtkDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
teevtkDisplay.GlyphType = 'Arrow'
teevtkDisplay.ScalarOpacityUnitDistance = 29.0275984280483

# show data from tube1
tube1Display = Show(tube1, renderView1)
# trace defaults for the display properties.
tube1Display.AmbientColor = [0.0, 0.0, 0.0]
tube1Display.ColorArrayName = ['POINTS', 'SCLs']
tube1Display.DiffuseColor = [1.0, 0.6666666666666666, 1.0]
tube1Display.LookupTable = sCLsLUT
tube1Display.BackfaceDiffuseColor = [1.0, 0.6666666666666666, 1.0]
tube1Display.OSPRayScaleArray = 'SCLs'
tube1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube1Display.GlyphType = 'Arrow'

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(None)
# ----------------------------------------------------------------
