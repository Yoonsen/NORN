import os

DATA_BASE_PATH = "data"
KONSENSUS_KORPUS_PATH = os.path.join(DATA_BASE_PATH, "konsensus-korpus.xlsx")
KORPUS_1800_PATH = os.path.join(DATA_BASE_PATH, "1800-1839.xlsx")
KORPUS_1840_PATH = os.path.join(DATA_BASE_PATH, "1840-1869.xlsx")

corpus_dict = {"konsensus-korpus": KONSENSUS_KORPUS_PATH,
                "1800-1839": KORPUS_1800_PATH,
                "1840-1869": KORPUS_1840_PATH}