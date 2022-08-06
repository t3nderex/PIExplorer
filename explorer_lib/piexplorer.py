from genericpath import isdir
import re
from typing import List
from xmlrpc.client import boolean

import os
import magic
import olefile                  # 한글
from pptx import Presentation   # ppt 
from docx import Document       # 워드
import openpyxl as oxl          # 엑셀
import pdfplumber

from piregexp import PIRegExp
from file_reader import FileReader


class PIExplorer(FileReader):
    def __init__(self, regexp_li):
        self.regexp_li = regexp_li
        self.leaked_data = []
        

    def find_pi_in_file(self, file_path, regexp_li = []):   # 기본 정규식으로 할지 새로운 정규식으로 할지
        if not regexp_li:
            leaked_data =self.__detect_pi(file_path, self.regexp_li)
            return leaked_data
        else:
            leaked_data =self.__detect_pi(file_path, regexp_li)
            return leaked_data

    def find_pi_in_dir(self, dir_path, regexp_li = []):
        if not regexp_li:
            leaked_data =self.__detect_pi(dir_path, self.regexp_li)
            return leaked_data
        else:
            leaked_data = self.__detect_pi(dir_path, regexp_li) 
            return leaked_data

    def __detect_pi(self,path, regexp_li):
        """
        중복 제거 할 것
        """
        if os.path.isfile(path):    # 파일일 경우에
            data = super().read_data(path)
            for regexp in self.regexp_li:
                p = re.compile(regexp)
                
                self.leaked_data.append(p.findall(data))
                
            ###
            self.leaked_data = self.__tuple_to_1dim_li(self.leaked_data)
            ###
            
            return self.leaked_data    
        
        elif os.path.isdir(path): 
            file_li = os.listdir(path)
            file_li = self.__add_path(path, file_li)
            for file in file_li:
                
                self.__detect_pi(file_li)
            
            
    def __add_path(self, path, file_li):
        if path[-1] == ("/" or "\\"):
            path = path.rstrip(path[-1])
        temp_li =[]
        for file in file_li:
            temp_li.append(path+file)
        return temp_li
            
    def __tuple_to_1dim_li(self, sleaked_data):
        temp_li = []
    
        self.leaked_data = sum(self.leaked_data, [])
        for data in self.leaked_data:
            if type(data) is tuple:
                
                tuple_data = data[0]
                
                temp_li.append(tuple_data)
            else:
                temp_li.append(data)
        
        return temp_li




if __name__ == '__main__':
    file = "./explorer_lib/test/" 
    pi = PIRegExp()
    
    regexp_li = pi.get_regexps()
    # print(regexp_li)
    explorer = PIExplorer(regexp_li)
    
    leaked_data=explorer.find_pi_in_dir(file)
    # print(leaked_data)