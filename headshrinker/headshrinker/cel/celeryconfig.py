BROKER_HOST = "localhost"
BROKER_PORT = 5672
BROKER_USER = "codemash"
BROKER_PASSWORD = "codemash"
BROKER_VHOST = "/codemash"
CELERY_RESULT_BACKEND = "amqp"
CELERY_IMPORTS = ("headshrinker.cel.pylons_tasks", )

# running settings
CELERYD_CONCURRENCY = 10
CELERYD_PREFETCH_MULTIPLIER = 10
CELERY_DISABLE_RATE_LIMITS = True

# email errors
CELERY_SEND_TASK_ERROR_EMAILS = True
ADMINS = [('Rick', 'rharding@morpace.com'),]
SERVER_EMAIL = 'celery@morpace.com'
MAIL_HOST = 'morpace.com'
