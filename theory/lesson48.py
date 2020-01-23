import zipfile
import os

folder_path = 'C:\\laragon\\www\\python\\webfor_python\\theory\\folder'
zip_path = 'C:\\laragon\\www\\python\\webfor_python\\theory\\folder\\test.zip'
zip_name = 'test.zip'

my_zip = zipfile.ZipFile(zip_path, 'w')

# my_zip.write(
#     'C:\\laragon\\www\\python\\webfor_python\\theory\\file.txt',
#     compress_type=zipfile.ZIP_DEFLATED,
#     arcname='file.txt'
# )

for folder, subfolders, files in os.walk(folder_path):
    for file in files:
        if file == zip_name:
            continue
        my_zip.write(
            os.path.join(folder, file),
            os.path.realpath(os.path.join(folder, file), folder_path),
            compress_type=zipfile.ZIP_DEFLATED)

my_zip.close()