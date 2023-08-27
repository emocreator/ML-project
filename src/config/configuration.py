from src.constants import *
import os,sys

ROOT_DIR = ROOT_DIR_KEY

DATASET_PATH = os.path.join(ROOT_DIR, DATA_DIR,DATA_DIR_KEY)

RAW_FILE_PATH = os.path.join(ROOT_DIR, ARTIFACT_DIR, 
                             DATA_INGESTION_KEY, 
                             CURRENT_TIME_STAMP, 
                             DATA_INGESTION_RAW_DATA_DIR, 
                             RAW_DATA_DIR_KEY)

TRAIN_FILE_PATH = os.path.join(ROOT_DIR, 
                               ARTIFACT_DIR, 
                               DATA_INGESTION_KEY, 
                               CURRENT_TIME_STAMP,
                               DATA_INGESTION_INGESTED_DATA_DIR_KEY,
                               TRAIN_DATA_DIR_KEY)

TEST_FILE_PATH =os.path.join(ROOT_DIR, 
                               ARTIFACT_DIR, 
                               DATA_INGESTION_KEY, 
                               CURRENT_TIME_STAMP,
                               DATA_INGESTION_INGESTED_DATA_DIR_KEY,
                               TEST_DATA_DIR_KEY)