""" Wraps the tasks file with loading the pylons env for running the celeryd

This code is already done when importing tasks.py from the pylons app in the
controllers. In order to allow the workers to have access to things like
models/etc it needs this in the daemon side.

This is the file imported by the celeryd config file while the pylons app just
loads celery_app.tasks

"""
import headshrinker
#headshrinker.get_appconfig(with_pylons=True)

import tasks
