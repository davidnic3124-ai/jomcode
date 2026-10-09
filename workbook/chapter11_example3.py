import logging

logger = logging.getLogger("workshop_hub")
logging.basicConfig(level=logging.INFO,format="%(levelname)s: %(message)s")
workshop_id = "w1"
logger.info("Workshop update rejected: id=%s reason=capacity", workshop_id)
