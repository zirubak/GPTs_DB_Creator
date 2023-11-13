# Auto GPTs DB Text Creator

The current GPTs configration has issue to use mutiple file and performance is not good. This is a simple tool to combine all the text files into one file. You can use this tool to create a text file for GPTs DB and upload to GPTs Configuration.
This Streamlit-based application automates appending text data from various file formats (PDF, Word, Text, Excel, CSV) into a single text file. It's designed for aggregating and storing text data, facilitating easier data management with GPTs.

## Prerequisites

- Python 3
- Conda (for environment management)

## Installation

1. Clone or download the repository.
2. Use Conda to create an environment from the provided `environment.yml` file:

   ```bash
   conda env create --name my-env-name --file environment.yml
   ```

3. Activate the new environment:

    ```bash
    conda activate my-env-name
    ```
4. Navigate to the directory containing the application files.

## Usage
Run the application with Streamlit:
``` base
streamlit run [script_name].py
```

Replace [script_name] with the name of the Python script.

## Features
- File Upload: Supports PDF, DOCX, TXT, XLSX, XLS, CSV.
- Automatic Text Extraction: Extracts text from uploaded files.
- Appending to Database File: Appends text to gpts_db_<current_date>.txt in db directory.
- Timestamps: Each entry is timestamped.
- Progress Indication: Visual feedback during file processing.


## License
This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

