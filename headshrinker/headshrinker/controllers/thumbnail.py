import logging

from pylons import request, response, tmpl_context as c, url
from pylons.controllers.util import redirect, abort
from pylons import config

import os
from PIL import Image
from tempfile import mkstemp
import shutil

from headshrinker.lib.base import BaseController, render
from headshrinker.cel import celeryconfig
from headshrinker.cel.tasks import GenerateThumbnail

log = logging.getLogger(__name__)

class ThumbnailController(BaseController):

    def index(self):
        redirect(url(controller="thumbnail", action="upload"))

    def upload(self):
        return render('/upload_form.mako')

    def savefile(self):
        """Store the uploaded image into the image path"""
        image_dir = config['app_conf']['image_path']

        if 'image' in request.params:
            image = request.params['image']

            new_file = mkstemp(suffix='.jpg', dir=image_dir)
            shutil.copyfileobj(image.file, open(new_file[1], 'w'))

            result = GenerateThumbnail.delay(new_file[1])

            # .get waits for the task to complete and then gets the result
            thumb = result.get()

        else:
            abort(500)

        c.filename = os.path.basename(new_file[1])
        c.thumbnail = os.path.basename(thumb)

        return render('/saved.mako')

    def viewfile(self, id):
        """Return the rendered image file"""
        image_dir = config['app_conf']['image_path']

        try:
            image_file = open(os.path.join(image_dir, id))

        except IOError, e:
            abort(404)

        response.headers['Content-type'] = 'image/jpg'
        return image_file

