from headshrinker.tests import *

class TestThumbnailController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='thumbnail', action='index'))
        # Test response...
