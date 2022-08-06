class PIRegExp():
    def __init__(self):
        
        self.resident_registration_num = '(?:[0-9]{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[1,2][0-9]|3[0,1])).[1-4][0-9]{6}'
        self.passport_num = '([a-zA-Z]{1}|[a-zA-Z]{2})\d{8}'
        # 정확도 높이려면 ([M|S|R|G|D]{1}|[TC|PM|PR|PO|PD|PT]{2})\d{8}
        self.alien_registration_num = '([01][0-9]{5}[[:space:]~-]+[1-8][0-9]{6}|[2-9][0-9]{5}[[:space:]~-]+[1256][0-9]{6})'
        self.driver_license_num =r'(\d{2}-\d{2}-\d{6}-\d{2})'


        self.ko_name = '^[가-힣]{2,4}$'
        self.en_name = '^[a-zA-Z]{2,10}\s[a-zA-Z]{2,10}$'

        self.road_name_addr = '(([가-힣A-Za-z·\d~\-\.]{2,}(로|길).[\d]+)|([가-힣A-Za-z·\d~\-\.]+(읍|동)\s)[\d]+)'
        self.land_num_addr = '(([가-힣A-Za-z·\d~\-\.]+(읍|면|동)\s)[\d-]+)|(([가-힣A-Za-z·\d~\-\.]+(읍|면|동)\s)[\d][^시]+)'
        # 지번부터 다시 짜면 됌

        self.phone_num = '(\d{2,3}[ ,-]-?\d{2,4}[ ,-]-?\d{4})'                                       # 전화번호
        self.bank_account_num = '([0-9,\-]{3,6}\-[0-9,\-]{2,6}\-[0-9,\-])'                           # 계좌번호
        self.health_insurance_num = '[1257][-~.[:space:]][0-9]{10}'                                  # 건강보험번호
        self.credit_card_num = '[34569][0-9]{3}[-~.[ ]][0-9]{4}[-~.[ ]][0-9]{4}[-~.[ ]][0-9]{4}'     # 신용카드번호
        self.car_num1 = '^[가-힣]{2}\\d{2}[가-힣]{1}\\d{4}$'                                         # 자동차 번호1
        self.car_num2 = '^\\d{2}[가-힣]{1}\\d{4}$'                                                   # 자동차 번호2

        self.url = '(http(s)?:\/\/)([a-z0-9\w]+\.*)+[a-z0-9]{2,4}'
        self.mail = '(([\w!-_\.])*@([\w!-_\.])*\.[\w]{2,3})'
        self.ipv4 = '(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}'
        self.ipv6 = '(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))'
        self.mac = '([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}'
        self.id = '^[A-Za-z]{1}[A-Za-z0-9]{3,19}$'
        # self.pw = r''
        self.military_serial_num = '^[0-9a-zA-Z]+([_0-9a-zA-Z]+)*$'                          # 군번
        self.business_registration_num = '^(\d{3,3})+[-]+(\d{2,2})+[-]+(\d{5,5})'            # 사업자등록번호

        # 견적서, 신청서 등 문서양식
    def get_regexps(self):
        reg_exp_list = [self.resident_registration_num,self.passport_num,self.alien_registration_num,self.driver_license_num,self.ko_name,
        self.en_name, self.road_name_addr, self.land_num_addr,self.phone_num,self.bank_account_num,self.health_insurance_num,self.credit_card_num, self.car_num1, self.car_num2,
        self.url,  self.mail, self.ipv4, self.ipv6, self.mac, self.id, self.military_serial_num, self.business_registration_num] 
        return reg_exp_list

    def get_regexp(self, rtype):
        pass

if __name__ =="main":
    pi= PIRegExp()
    li = pi.get_regexp

    

        # elif rtype ==
        # else:
        #     print('[!] wrong arguments')
        #     return False


        #https://easylaw.go.kr/CSP/CnpClsMain.laf?popMenu=ov&csmSeq=1257&ccfNo=1&cciNo=1&cnpClsNo=1
        # 학력사항
        # - 학교명
        # - 학위
        # - 전공
        # - 학점
        # - 소재지
        # 자격증 및 교육사항
        # - 자격/면허
        # - 취득일자
        # - 자격 및 교육명
        # - 발급 기관
        # - 점수/등급
        # 수상경력
        # 경력사항
        # 회사명
        # 근무기간
        # 근무부서
        # 직위
        # ※ 출처 : 행자부‧KISA "김대리, 개인정보보호 달인되기" 15면
        # 일반정보 – 성명, 주민등록번호, 주소 연락처 등
        # 경제정보 – 소득, 재산상황, 신용, 부채 등
        # 사회정보 – 학력, 성적, 병역, 직업, 자격 등
        # 통신정보 – 전자우편, 통화내용, 인터넷 IP 등
        # 민감정보 – 사상, 신념, 노동조합, 정당의 가입탈퇴, 정치적 견해, 건강, 성생활정보 등