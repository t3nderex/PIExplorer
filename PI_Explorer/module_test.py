from pathlib import Path
from sys import argv

from explorer_lib.pi_explorer import PI_Explorer
from explorer_lib.pi_regexp import PI_RegExp



from utils import util



if __name__ == '__main__':


    # 매개변수가 없는 경우
    if len(argv) == 1:
        print("매개변수를 확인 하세요. \'-h, -help\'를 통해 사용법을 확인할 수 있습니다.")
        exit()


    # 매개변수가 1개인 경우
    elif len(argv) == 2:
        if argv[1] == '-h' or '-help':
            print('-r : 개인정보를 탐색할 범위를 지정합니다. \'-r [file]or[dircetory]\' 형태로 사용합니다.')
            exit()

        else:
            print('매개변수를 확인 하세요. \'-h, -help\'를 통해 사용법을 확인할 수 있습니다.')

    # 매개변수가 2개인 경우
    elif len(argv) == 3:
        if argv[1] == '-r' or '-range':

            regexp = PI_RegExp()
            regexp_li = regexp.get_pi_regexps()



    
            if argv[2] == 'all':
                print('전체 경로 탐색을 시작합니다.')
                # 탐색 함수 추가
            else:
                path = Path(argv[2])
                if not path.exists():        
                    print('파일 또는 디렉터리가 존재하지 않습니다.')
                    
                
                elif path.is_file():             # 파일인 경우
                    file_path = str(path)
                    print(f'{file_path}에서 개인정보 탐색을 시작합니다.')
                    file_name = './test/test.hwp'

                    pr = PI_RegExp()
                    px = PI_Explorer()

                    regexp_li = pr.get_pi_regexps()
                    data = px.read_data(file_name)

                    leaked_data = px.find_pi(data, regexp_li)
                    # print(f"읽은 데이터 {type(leaked_data)}")
                    
                    
                     
                    
                
                elif path.is_dir():              # 디렉터리인 경우
                    dir_path = str(path)
                    print(f'{dir_path}탐색에서 개인정보 탐색을 시작합니다.')

                    dir_list = util.search_dir(dir_path)  # 디렉터리 탐색
                        
                
                exit()   
        else:
            print('[Exit] wrong arguments2')
            exit()
    else:
        print('[Exit] wrong arguments3')
        exit()