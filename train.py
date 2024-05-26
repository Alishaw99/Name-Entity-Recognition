import os
import sys
from ner.exception import NerException
from ner.pipeline.train_pipeline import TrainPipeline

from ner.constants import *


def training():
    try:
        train_pipeline = TrainPipeline()

        train_pipeline.run_pipeline()

    except Exception as e:
        raise NerException(e, sys) from e


if __name__ == "__main__":
    training()




# import os
# from ner.configuration.gcloud import GCloud

# # Create an instance of the GCloud class
# obj = GCloud()

# # Call the sync_folder_from_gcloud method on the instance
# obj.sync_folder_from_gcloud(gcp_bucket_url="ner-using-bert-72", filename="archive.zip", destination="test")
