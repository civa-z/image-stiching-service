from django.http import HttpResponse
import cv2
import numpy as np
import sys
 
def on_request(request):
    imagedata = request.read()
    print(sys.getsizeof(imagedata))
    x=np.fromstring(imagedata, dtype='uint8')
    image=cv2.imdecode(x, cv2.IMREAD_UNCHANGED)
    cv2.imshow("Camera", image)
    cv2.waitKey(0)
    #bgrImage = np.array(imagedata).reshape(768,1366,3)
    return HttpResponse("Hello world ! ", "utf-8")