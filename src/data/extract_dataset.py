import sys
import os

# Get the directory of the current file
current_file_dir = os.path.dirname(os.path.abspath(__file__))

# Navigate up two levels to reach the parent directory of the 'src' directory
parent_dir = os.path.abspath(os.path.join(current_file_dir, '..', '..'))

# Add the parent directory to the Python path
sys.path.append(parent_dir)


import logging
from zipfile import ZipFile
from pathlib import Path
from src.logger import create_log_path, CustomLogger

# path to save the logs
log_file_path = create_log_path('extract_dataset')

# create custom logger object
extarct_logger = CustomLogger(logger_name="extract_dataset",log_filename=log_file_path)
# set the level of logging to INFO
extarct_logger.set_log_level(level=logging.INFO)


def extract_zip_file_data(input_path: Path, output_path: Path):
    with ZipFile(file=input_path) as f:
        f.extractall(path=output_path)
        input_file_name = input_path.stem + input_path.suffix
        extarct_logger.save_logs(msg=f"{input_file_name} extracted successfully at the Target path",
                                 log_level="info")


    
def main():
    # Extract the current file path 
    current_path = Path(__file__)

    # Extract the root directory path
    root_path = current_path.parent.parent.parent

    # raw data directory path
    raw_data_path = root_path / 'data' / 'raw'

    # output path for the extracted zip files
    output_path = raw_data_path / "extracted"

    # make the directory for the output_path
    output_path.mkdir(parents=True,exist_ok=True)

    # input path for zip files
    input_path = raw_data_path / "zipped"



    #extract the train and test files
    # for train files
    extract_zip_file_data(input_path= input_path/"train.zip",output_path= output_path)

    # for test files
    extract_zip_file_data(input_path= input_path/"test.zip",output_path= output_path)





if __name__ == "__main__":
    # call the main function
    main()



