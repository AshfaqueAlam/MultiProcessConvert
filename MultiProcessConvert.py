# Total time taken if ran sequentially: 4 mins 6.23 secs, 2nd attempt took: 5 min 9 secs, 3rd attempt took: 6 mins

import os
from ashfaquecodes.ashfaquecodes import get_execution_start_time, get_execution_end_time
from Convert2PDF.ConvertToPDF import docx2pdfConvert, pptx2pdfConvert, img2pdfConvert, bmp2pdfConvert, txt2pdfConvert, mergePdfs
from datetime import datetime


start = get_execution_start_time()

# docx = docx2pdfConvert(f'{os.getcwd()}/test_files/demo.docx', f'{os.getcwd()}/output/')    # 7.62 secs
# doc = docx2pdfConvert(f'{os.getcwd()}/test_files/SampleDOCFile 5000kb.doc', f'{os.getcwd()}/output/')    # 3 mins 18 secs
# jpeg = img2pdfConvert(f'{os.getcwd()}/test_files/Large Sample-Image-download-for-Testing.jpeg', f'{os.getcwd()}/output/Large Sample-Image-download-for-Testing.pdf')    # 420.06 ms
# jpg = img2pdfConvert(f'{os.getcwd()}/test_files/Large-Sample-Image-download-for Testing.jpg', f'{os.getcwd()}/output/Large-Sample-Image-download-for Testing.pdf')    # 260.51 ms
# pptx = pptx2pdfConvert(f'{os.getcwd()}/test_files/PPT-56-Months.Eng 1st-Feb_2019RevisedLR.pptx', f'{os.getcwd()}/output/')    # 17.8 secs
# ppt = pptx2pdfConvert(f'{os.getcwd()}/test_files/SamplePPTFile 1000kb.ppt', f'{os.getcwd()}/output/')    # 2.21 secs
# png = img2pdfConvert(f'{os.getcwd()}/test_files/SamplePNGImage 30mb.png', f'{os.getcwd()}/output/SamplePNGImage 30mb.pdf')    # 15.8 secs
# bmp = bmp2pdfConvert(f'{os.getcwd()}/test_files/sample 5184x3456.bmp', f'{os.getcwd()}/output/sample 5184x3456.pdf')    # 460.3 ms
# txt = txt2pdfConvert(f'{os.getcwd()}/test_files/SampleTextFile 1000kb.txt', f'{os.getcwd()}/output/SampleTextFile 1000kb.pdf')    # 761.02 ms

# all_pdfs_tuple = (
#             f'{os.getcwd()}/test_files/[READ] Malvino_Electronic-Principles.pdf'
#             , f'{os.getcwd()}/output/demo.pdf'
#             , f'{os.getcwd()}/output/Large Sample-Image-download-for-Testing.pdf'
#             , f'{os.getcwd()}/output/Large-Sample-Image-download-for Testing.pdf'
#             , f'{os.getcwd()}/output/PPT-56-Months.Eng 1st-Feb_2019RevisedLR.pdf'
#             # , f'{os.getcwd()}/output/prague contour lines.pdf'
#             , f'{os.getcwd()}/output/sample 5184x3456.pdf'
#             , f'{os.getcwd()}/output/SampleDOCFile 5000kb.pdf'
#             , f'{os.getcwd()}/output/SamplePNGImage 30mb.pdf'
#             , f'{os.getcwd()}/output/SamplePPTFile 1000kb.pdf'
#             , f'{os.getcwd()}/output/SampleTextFile 1000kb.pdf'
#         )
# # time taken: 23.76 secs
# merged = mergePdfs(*all_pdfs_tuple, output_pdf_file_path=f'{os.getcwd()}/output/merged.pdf')    # * unpacks it, so each element in the tuple will be treated as a single argument of the method, else entire tuple will be passed as an argument.

# ---------------------------------------------------------------------------------------------------------------


files_path_list = [
    f'{os.getcwd()}/test_files/PPT-56-Months.Eng1st-Feb_2019RevisedLR.pptx'
    , f'{os.getcwd()}/test_files/SampleDOCFile 5000kb.doc'
    , f'{os.getcwd()}/test_files/demo.docx'
    , f'{os.getcwd()}/test_files/pptexamples.ppt'
    , f'{os.getcwd()}/test_files/[READ] Malvino_Electronic-Principles.pdf'
    , f'{os.getcwd()}/test_files/Large Sample-Image-download-for-Testing.jpeg'
    , f'{os.getcwd()}/test_files/Large-Sample-Image-download-for Testing.jpg'
    , f'{os.getcwd()}/test_files/SamplePNGImage 30mb.png'
    , f'{os.getcwd()}/test_files/sample 5184x3456.bmp'
    , f'{os.getcwd()}/test_files/SampleTextFile 1000kb.txt'
]



output_dir_path = f"{os.getcwd()}/output/{datetime.now().strftime('%Y%m%d%H%M%S%f')}"

if not os.path.exists(output_dir_path):
    os.makedirs(output_dir_path)

from multiprocessing import Process as multiProcess, Manager

def multi_convert(file_path : str, output_pdf_paths_list : str) -> bool:
    status = False
    output_pdf_path = os.path.join(output_dir_path, (os.path.splitext(file_path)[0]).split('\\')[-1]+'.pdf' if '\\' in file_path else (os.path.splitext(file_path)[0]).split('/')[-1]+'.pdf')
    extension = os.path.splitext(file_path)[-1].lower()

    if extension in ('.pdf'):
        output_pdf_paths_list.append(file_path)
    elif extension in ('.docx', '.doc'):
        status = docx2pdfConvert(file_path, output_dir_path)
    elif extension in ('.pptx', '.ppt'):
        status = pptx2pdfConvert(file_path, output_dir_path)
    elif extension in ('.jpeg', '.jpg', '.png'):
        status = img2pdfConvert(file_path, output_pdf_path)
    elif extension == '.bmp':
        status = bmp2pdfConvert(file_path, output_pdf_path)
    elif extension == '.txt':
        status = txt2pdfConvert(file_path, output_pdf_path)

    if status:
        output_pdf_paths_list.append(output_pdf_path)

    return output_pdf_paths_list, status
    # ! not able to return `status` in process thread.



# manager = Manager()
# process_list, output_pdf_paths_list = [], manager.list()
# max_process_running = 5
# process_running = 0
process_list, output_pdf_paths_list = [], []

for each_file_path in files_path_list:
    multi_convert(each_file_path, output_pdf_paths_list)

    # ! how to get informed if one or more process fails. And how to handle error???
    # p = multiProcess(target=multi_convert, args=(each_file_path, output_pdf_paths_list))
    # process_list.append(p)
    # p.start()
    # process_running += 1
    
    # if process_running >= max_process_running:
    #     while process_running >= max_process_running:
    #         process_running = 0
    #         process_running += p.is_alive()
    #         print('---->',process_running)

# for each_process in process_list:
#     each_process.join()

print('-----#####################################################################################-----')
print('output_pdf_paths_list-->', len(output_pdf_paths_list))

status = mergePdfs(*output_pdf_paths_list, output_pdf_file_path=f"{os.path.join(output_dir_path, 'output_merged_file.pdf')}")


print('Total time taken::::: ', get_execution_end_time(start))
