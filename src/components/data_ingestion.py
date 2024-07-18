import os
import sys

from src.exception import CustomException
from src.logger import logging

import pandas as pd
# we can import other modules if we are reading data from different sources

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass

# creating config class
class DataIngestionConfig:
    
    train_data_path : str = os.path.join('artifacts' , 'train.csv')
    test_data_path : str = os.path.join('artifacts' , 'test.csv')
    raw_data_path : str = os.path.join('artifacts' , 'raw_data.csv')

class DataIngestion:
    
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")

        try:
            # reading the dataset and storing it in a new variable
            df = pd.read_csv('notebook\student data.csv')
            logging.info("exported/read the dataset")

            # saving raw data , train data and test data respectively after fetching them

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path) , exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            logging.info('saved raw data')

            train_set , test_set = train_test_split(df , test_size=0.2,random_state=25)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Inmgestion of the data iss completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

            
        


        except Exception as e:
            raise CustomException(e,sys)


if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    