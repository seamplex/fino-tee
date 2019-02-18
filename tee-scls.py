execfile("tee-scls-yz.py")

GetRenderView().ViewSize = [1200,1000]
GetRenderView().Background = [1,1,1]
Render()
WriteImage("tee-scls-yz-%s.png"%sys.argv[1])

#renderView1.OrientationAxesVisibility = 0
renderView1.OrientationAxesLabelColor = [0.0, 0.0, 0.0]
renderView1.OrientationAxesOutlineColor = [0.0, 0.0, 0.0]
renderView1.CenterOfRotation = [323.7999877929687, 79.331, 242.84998779296876]
renderView1.StereoType = 0
renderView1.CameraPosition = [176.84939525047312, -1948.6039884482195, 0.5514372834825004]
renderView1.CameraFocalPoint = [176.84939525047312, 79.331, 0.5514372834825004]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 202.3594112809192

GetRenderView().ViewSize = [1200,1000]
GetRenderView().Background = [1,1,1]
Render()
WriteImage("tee-scls-xz-%s.png"%sys.argv[1])
