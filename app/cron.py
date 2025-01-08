import logging

logger = logging.getLogger(__name__)


def my_scheduled_job():
    print("hello")
    logger.info('This is an info message')