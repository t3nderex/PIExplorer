from genericpath import isdir
import re
from typing import List
from xmlrpc.client import boolean
from pprint import pprint as prt
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
        if os.path.isfile(file_path):
            if not regexp_li:
                leaked_data =self.__detect_pi(file_path, self.regexp_li)
                print(f"파일: {file_path}")
                print(f"내장되어 있는 기본 정규표현식을 이용합니다.")
                return leaked_data
            else:
                leaked_data =self.__detect_pi(file_path, regexp_li)
                print(f"파일: {file_path}")
                print(f"입력한 정규표현식을 이용하여 탐색합니다.")
                return leaked_data
        else:
            return "파일이 아닙니다."

    def find_pi_in_dir(self, dir_path, regexp_li = []):
        #디렉터리
        
        leaked_data = []
        if os.path.isdir(dir_path):                         #디렉터리 인지 검사
            file_li = os.listdir(dir_path)                  
            file_li = self.__add_path(dir_path, file_li)    # 각각의 파일 경로 생성
            
            if not regexp_li:                               # PIRegEXP 사용
                for file in file_li:    
                    temp = self.__detect_pi(file,self.regexp_li)
                    leaked_data.append(temp)
                    
                
                return leaked_data
            else:
                leaked_data = self.__detect_pi(dir_path, regexp_li) 
                return leaked_data

        else:
            return False




    def __detect_pi(self,path, regexp_li):
        """
        TODO:
        결과 값 최적화: 빈 리스트, 중복 리스트, 튜플 제거하기 
        """
        temp ={}
        leaked_data_li =[] 
        if os.path.isfile(path):    # 파일일 경우에
            
            data = super().read_data(path)
            for regexp in self.regexp_li:
                p = re.compile(regexp)
                
                leaked_data_li.append(p.findall(data)) 
            
            temp[path] =leaked_data_li 

            self.leaked_data.append(temp)
                

            
            
            return self.leaked_data    
        


    def __add_path(self, path, file_li):
        if path[-1] == ("/" or "\\"):
            path = path.rstrip(path[-1])
        temp_li =[]
        for file in file_li:
            temp_li.append(path+"/"+file)
        return temp_li
            

if __name__ == '__main__':
    file = "./explorer_lib/test/" 
    pi = PIRegExp()
    
    regexp_li = pi.get_regexps()
    explorer = PIExplorer(regexp_li)
    
    leaked_data=explorer.find_pi_in_file(file)
    prt(leaked_data)
    leaked_data=explorer.find_pi_in_dir(file)
    prt(leaked_data)
    