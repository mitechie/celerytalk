# QUEUE
def show_queues():
    """List all of the queues in rabbitmq on this host

    :Requires: prerun a environment setting function such as dev/prod
    :Requires: command needs to run with sudo so needs you to enter sudo password

    To view the list of queues on the production server
    ::

        $ fab prod show_queues

    """
    require('hosts', provided_by=[dev])
    sudo('rabbitmqctl list_queues -p /qmail')

def celery_status():
    """List the number of queued items in the celery queue

    Custom version of the ``show_queues`` command to parse celery queues
    """
    require('hosts', provided_by=[dev])
    sudo('rabbitmqctl list_queues -p /qmail name messages messages_unacknowledged messages_ready | grep cel')

def reset_queues():
    """Clear the queues on the machines and reset up the rabbitmq vhost

    :WARNING: This will clear any and all queued items in the queue.

    :Requires: prerun a environment setting function such as dev/prod
    :Requires: command needs to run with sudo so needs you to enter sudo password

    To clear the production servers queues (in case of crash/left over jobs)
    ::

        $ fab prod reset_queues

    """
    if (confirm('Are you sure you want to delete everything in the queue on %(host)s?' % env,
                default=False)):
        commands = [
        'sudo rabbitmqctl stop_app',
        'sudo rabbitmqctl reset',
        'sudo rabbitmqctl start_app',
        'sudo rabbitmqctl add_user codemash codemash',
        'sudo rabbitmqctl add_vhost /codemash',
        'sudo rabbitmqctl set_permissions -p /codemash codemash ".*" ".*" ".*"',
        ]
        require('hosts', provided_by=[dev])

        for c in commands:
            sudo(c)
