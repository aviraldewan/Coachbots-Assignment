import logging

# Get the logger for the current module
logger = logging.getLogger(__name__)

def compute_metric():
    # Import the Entry model from metric_computation.models
    from metric_computation.models import Entry

    # Retrieve the latest 3 entries from the Entry model
    entries = Entry.objects.order_by('-created_at')[:3]

    # Calculate the total value of the entries
    total = 0
    for entry in entries:
        total += entry.value

    # Calculate the average by dividing the total by 3
    avg = total / 3

    # Log the computed average using the logger
    logger.info(f'Average of latest 3 values is: {avg}')
