from celery import Celery
from celery.schedules import crontab

from xur import where_xur, xur_weapon

celery_app = Celery('task', broker='redis://localhost:6379/0')

@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(crontab(minute='*/1'), xur_map.s())
    sender.add_periodic_task(crontab(minute='*/2'), xur_armor.s())


@celery_app.task
def xur_map():
    where_xur()


@celery_app.task
def xur_armor():
    xur_weapon()


