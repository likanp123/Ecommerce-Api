from celery import shared_task
from .models import Product, Customer
import logging

logger = logging.getLogger(__name__)

@shared_task
def sync_data():
    try:
        # Dummy external API fetch simulation
        external_products = [
            {"sku": "abc123", "name": "Product A", "price": 10.5, "inventory_count": 5, "source_platform": "platform1"},
        ]
        for p in external_products:
            Product.objects.update_or_create(sku=p["sku"], defaults=p)
        logger.info("Sync completed.")
    except Exception as e:
        logger.error(f"Sync failed: {str(e)}")
