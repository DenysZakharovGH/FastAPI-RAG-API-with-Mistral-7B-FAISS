import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.StreamHandler(),              # консоль
        logging.FileHandler("app.log"),        # файл
    ],
)

logger = logging.getLogger("llm_api")