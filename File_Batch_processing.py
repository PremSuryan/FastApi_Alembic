# File batch processing:

from concurrent.futures import ThreadPoolExecutor,as_completed

def process_file(file):
    #file processing...
    result = file.split('\\')[-1]
    return result


def processing_file(files,max_workers=5):
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {}
        for file in files[:max_workers]:
            future = executor.submit(process_file, file)
            print("future", future)
            futures[future]=file

        remaining_files = iter(files[max_workers:])

        while futures:
            for future in as_completed(futures):
                file = futures.pop(future)
                
                yield future.result()

            try:
                next_file = next(remaining_files)
                new_future = executor.submit(
                    process_file,
                    next_file
                )

                futures[new_future]= next_file
            except StopIteration:
                pass

            break



import os
file_dir = os.getcwd()
#E:\Fast Api Alembic\Project-Management-Sample-Data.xlsx
file_path = os.path.join(file_dir,'Project-Management-Sample-Data.xlsx')
for res in processing_file([file_path]):
    print(res)