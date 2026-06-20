import gdown
import os

os.makedirs('data', exist_ok=True)

# field_id : local filename
datasets = { "1RmihQXqpuiH5mYD217LDphOrsydBDfh-" : "dataset_business.json",
             "1efdtWL-vA1cFehPr6W4c5vC570tGxpW9" : "dataset_reviews.json"
}

for file_id, filename in datasets.items():
    url = f"https://drive.google.com/uc?id={file_id}"
    output = os.path.join('data', filename)
    gdown.download(url, output, quiet=False)