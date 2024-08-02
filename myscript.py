import logging
import os, sys
import shutil




file_extensions_map = {
    # Document files
    'doc': 'Documents',
    'docx': 'Documents',
    'pdf': 'Documents',
    'txt': 'Documents',
    'rtf': 'Documents',
    'odt': 'Documents',
    'xls': 'Spreadsheets',
    'xlsx': 'Spreadsheets',
    'csv': 'Spreadsheets',
    'ppt': 'Presentations',
    'pptx': 'Presentations',
    'jpg': 'Images',
    'jpeg': 'Images',
    'png': 'Images',
    'gif': 'Images',
    'bmp': 'Images',
    'svg': 'Images',
    'mp3': 'Audio',
    'wav': 'Audio',
    'aac': 'Audio',
    'flac': 'Audio',
    'mp4': 'Videos',
    'avi': 'Videos',
    'mov': 'Videos',
    'mkv': 'Videos',
    'zip': 'Archives',
    'rar': 'Archives',
    'tar': 'Archives',
    'gz': 'Archives',

    # Code files
    'py': 'Codes',
    'java': 'Codes',
    'c': 'Codes',
    'cpp': 'Codes',
    'js': 'Codes',
    'html': 'Codes',
    'css': 'Codes',

    # Web files
    'xml': 'Web',
    'json': 'Web',

    # System files
    'exe': 'Executables',
    'dll': 'Libraries',
    'bat': 'Scripts',

    # Miscellaneous files
    'iso': 'Disk Images',
    'md': 'Documents',  # Markdown files
}









logger = logging.getLogger("fileOrganizerLogger")
logger.setLevel(logging.DEBUG)

# file handler logger
file_handler = logging.FileHandler(f'C:/PythonScripts/logs/app.log','a', encoding="utf-8")
handlerFormatter = logging.Formatter(
    '{asctime} - {name} - {levelname} - {message}',
    style='{',
    datefmt='%Y-%m-%d %H:%M',
)
file_handler.setFormatter(handlerFormatter)
file_handler.setLevel(logging.DEBUG)

# console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# attach the handler
logger.addHandler(file_handler)
logger.addHandler(console_handler)






def createFolder(folderName:str):
    try:
        os.makedirs(folderName, exist_ok=True)
        logger.info("Folder Created Succesfully")
    except:
        print("Error creating folder: ", folderName)
        logger.info("Error creating folder")



def handleFileSegregation(path):


    logger.info('Starting to organize files in')
    dirList = os.listdir(path=path)
    for file in dirList:
        if os.path.isfile(os.path.join(path, file)):
            file_ext_typ = file.split('.')[-1]
            try:
                file_ext_folder_type = file_extensions_map[file_ext_typ]
                destFolder = os.path.join(path, file_ext_folder_type)
                createFolder(folderName=destFolder)
                shutil.move(file, os.path.join(destFolder, file))
                logger.debug(f"{file} was added to {destFolder}")
            except KeyError:
                logger.warning(f'Ignored ==> Special File Type [{file}]')
        else:
            logger.warning(f"Skipped ==> [{file}] type [Folder]")


if __name__=='__main__':
    pathname = os.path.dirname(os.getcwd())
    handleFileSegregation(pathname)
    # createFolder("Images")