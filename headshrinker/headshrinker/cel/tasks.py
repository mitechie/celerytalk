from celery.task import Task
import os
from PIL import Image


class GenerateThumbnail(Task):

    def _shrinkme(self, image_file):
        """Turn this image into a 128x128 pixel size of itself"""
        size = 128, 128

        file, ext = os.path.splitext(image_file)
        im = Image.open(image_file)
        im.thumbnail(size, Image.ANTIALIAS)
        im.save(file + ".thumbnail", "JPEG")
        return file + ".thumbnail"

    def run(self, filename, **kwargs):
        """Run the task on command

        We only need the filename of the original to perform this task

        """
        thumb = self._shrinkme(filename)

        logger = self.get_logger(**kwargs)
        logger.info("Created thumbnail for task: " + kwargs['task_id'])

        # store the resulting new filename as a return value
        return thumb


from celery.decorators import task

@task
def generate_thumbnail(filename):
    # can do the same stuff here, just looks different
    pass

class RunStats(Task):
    def run(self, **kwargs):
        """Just pretend to generate some stats"""
        logger = self.get_logger(**kwargs)
        logger.info('Running Stats...will run again ...')
