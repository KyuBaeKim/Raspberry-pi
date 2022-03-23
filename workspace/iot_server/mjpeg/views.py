from django.views.generic import TemplateView
from django.http import HttpResponse, StreamingHttpResponse
from .picam import MJpegStreamCam
from time import sleep

mjpegstream = MJpegStreamCam()
class CamView(TemplateView):
    template_name = "cam.html" # 렌더링할 템플릿 파일 경로
    def get_context_data(self): # context 변수 구성
        context = super().get_context_data()
        context["mode"] = self.request.GET.get("mode", "#")
        return context

def snapshot(request):
    sleep(0.3)
    image = mjpegstream.snapshot()
    return HttpResponse(image, content_type = "image/jpeg")

def stream(request):
    return StreamingHttpResponse(mjpegstream, content_type = 'multipart/x-mixed-replace;boundary=--myboundary')