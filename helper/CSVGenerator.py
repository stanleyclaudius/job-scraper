from datetime import datetime


def generate_csv(csv_data):
    file_name = str(datetime.now()).replace(" ", "_").replace(":", "").replace(".", "")
    with open(f'job_data/{file_name}.csv', 'w') as f:
        f.write(csv_data)
    print(f'File saved: {file_name}.csv')
