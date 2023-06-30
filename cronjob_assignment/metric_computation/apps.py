from django.apps import AppConfig
from apscheduler.schedulers.background import BackgroundScheduler
from metric_computation.cron import compute_metric

class MetricComputationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'metric_computation'

    def ready(self):
        # Create an instance of BackgroundScheduler
        scheduler = BackgroundScheduler()

        # Add a job to the scheduler
        # The job will run the `compute_metric` function at an interval of 5 minutes
        scheduler.add_job(compute_metric, 'interval', minutes=5)

        # Start the scheduler
        scheduler.start()

default_app_config = 'metric_computation.apps.MetricComputationConfig'
