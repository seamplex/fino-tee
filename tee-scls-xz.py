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
renderView1.CenterOfRotation = [323.7999877929687, 79.331, 242.84998779296876]
renderView1.StereoType = 0
renderView1.CameraPosition = [176.84939525047312, -1948.6039884482195, 0.5514372834825004]
renderView1.CameraFocalPoint = [176.84939525047312, 79.331, 0.5514372834825004]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 202.3594112809192
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
tee4vtk = LegacyVTKReader(FileNames=['/home/gtheler/run/fino/tee/tee-4.vtk'])

# create a new 'Legacy VTK Reader'
scls4vtk = LegacyVTKReader(FileNames=['/home/gtheler/run/fino/tee/scls-4.vtk'])

# create a new 'Tube'
tube1 = Tube(Input=scls4vtk)
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

# show data from tee4vtk
tee4vtkDisplay = Show(tee4vtk, renderView1)
# trace defaults for the display properties.
tee4vtkDisplay.AmbientColor = [0.0, 0.0, 0.0]
tee4vtkDisplay.ColorArrayName = ['POINTS', '']
tee4vtkDisplay.DiffuseColor = [0.576470588235294, 0.576470588235294, 0.576470588235294]
tee4vtkDisplay.Opacity = 0.6
tee4vtkDisplay.BackfaceDiffuseColor = [1.0, 0.6666666666666666, 1.0]
tee4vtkDisplay.OSPRayScaleArray = 'sigma'
tee4vtkDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
tee4vtkDisplay.GlyphType = 'Arrow'
tee4vtkDisplay.ScalarOpacityUnitDistance = 29.0275984280483

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