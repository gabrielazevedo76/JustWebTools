import os

from django.shortcuts import render
from watermark.models import WatermarkModel
from django.http import FileResponse, HttpResponseRedirect, HttpResponse, Http404

import mimetypes
from PIL import Image

from .utils.watermark.watermark import Watermark
from watermark.forms import WatermarkForm


# Create your views here.

def uploadForm(request):
    if request.method == "POST":
        form = WatermarkForm(request.POST, request.FILES)
        if form.is_valid():
            wm = form.save()
            return HttpResponseRedirect(f'{wm.pk}')
    else:
        form = WatermarkForm()
        return render(request, 'watermark/pages/upload-form.html', {"form":form})

def handleForm(request, pk):
        wmModel = WatermarkModel.objects.get(id=pk)
        wm = Watermark(wmModel.img, wmModel.logo)

        if request.method == "POST":
            res = request.POST.get('position')
            if res == "UpperLeft":
                return HttpResponseRedirect(f"^{pk}^width={0}&height={0}/download")
            if res == "UpperRight":
                return HttpResponseRedirect(f"^{pk}^width={wm.widthImg - 125}&height={0}/download")
            if res == "Center":
                return HttpResponseRedirect(f"^{pk}^width={(wm.widthImg - 125) // 2}&height={(wm.heightImg - 125) // 2}/download")
            if res == "LowerLeft":
                return HttpResponseRedirect(f"^{pk}^width={0}&height={wm.heightImg - 125}/download")
            if res == "LowerRight":
                return HttpResponseRedirect(f"^{pk}^width={wm.widthImg - 125}&height={wm.heightImg - 125}/download")
        else:
            return render(request, 'watermark/pages/handle-form.html', {"wm":wm})



def download(request, pk, width, height):
    if request.method == "GET":
        wmModel = WatermarkModel.objects.get(id=pk)
        wmPath = f"media/watermark/media/watermarked/{wmModel.pk}.png"

        wm = Watermark(wmModel.img, wmModel.logo)
        wm.resize(0.4)
        im = wm.merge(width, height)
        im.save(wmPath)
        wmModel.watermarked = wmPath
        wmModel.save()

        wrapper = open(wmPath, "rb").read()
        content_type = mimetypes.guess_type(wmPath)[0]
        response = HttpResponse(wrapper, content_type=content_type)
        response['Content-Length'] = os.path.getsize(wmPath)
        response['Content-Disposition'] = "attachment; filename=%s" % f"{wmModel.pk}.png"
        return response
