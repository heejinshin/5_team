def dictfetchall(cursor):
    """
    [('ID', <cx_Oracle.DbType DB_TYPE_NUMBER>, 20, None, 19, 0, 0), ('TITLE', <cx_Oracle.DbType DB_TYPE_NVARCHAR>, 100, 400, None, None, 1), ('WRITER', <cx_Oracle.DbType DB_TYPE_NVARCHAR>, 100, 400, None, None, 1), ('CONTENTS', <cx_Oracle.DbType DB_TYPE_NCLOB>, None, None, None, None, 1), ('WDATE', <cx_Oracle.DbType DB_TYPE_TIMESTAMP>, 23, None, 0, 6, 0), ('HIT', <cx_Oracle.DbType DB_TYPE_NUMBER>, 12, None, 11, 0, 0)]
    """
    #print( cursor.description )
   
    
    #cursor의  description에 각 필드 이름 정보 - 배열 
    #colums ['id', 'title', 'contents', 'writer']
    #[1, '제목1', '내용1', '작성자1']
    #{'id':1, 'title':'제목1' , .....}
    columns = [ col[0].lower() for col in cursor.description]
    #print( columns  )
    return [dict(zip(columns, row)) for row in cursor.fetchall()]

    """
    [(1, "제목1', '내용1')
    cursor.description
    [{"id":1, "title":"제목1"}]
    """

# << < 1 2 3 4 5 6 7 8 9 10 > >> 
# << : 첫번째 페이지, 항상 
# < : 현재페이지로부터 앞으로 이동할 페이지가 있는지   현재 9페이지 이전< 8페이지  
# 0,1,2,....9     첫번째 그룹 : 1~10    현재 :4           1번그룹 
# 10,,,,   19     두번째 그룹 : 11~20       :12           2번그룹
# 30,,,,  39      세번째 그룹 : 21~30       :29           3번그룹 
# > :  현재페이지로부터 뒤로 이동할 페이지가 있는지   현재 9  다음> 10페이지 
# >> 마지막 페이지 

import math 
class CommonPage:
    #페이징에 필요한 3가지 정보 (전체개수, 한페이지에 표시될개수, 현재페이지)
    #totalCnt :  전체데이터 개수   
    #pageSize :  한페이지에 데이터를 몇건씩 보여줄건지 
    #전체페이지개수 :  ceil(totalCnt / pageSize)   
    #232/10 - 23.2 - 올림 - 24페이지  
    #curPage :  현재페이지 
    #파이썬에 클래스 설계할때 가급적 생성자에서 변수를 만드는게 낫다
    def __init__(self, totalCnt=1, curPage=0, pageSize=10):
        self.curPage = curPage
        self.totalCnt = totalCnt
        self.totalPage = math.ceil(totalCnt/pageSize)-1
        self.start = (self.curPage // pageSize)*10 #그룹시작
        self.end =self.start+10  # 그룹종료
        if self.end > self.totalPage:
            self.end = self.totalPage+1

        #3      0    10 
        #12     10   20
        #32     30   40
        if self.curPage>=1: #앞으로 이동가능 
            self.isPrev=True 
            self.prev_page=self.curPage-1 
        else: #더이상 앞으로 갈 수 없음 
            self.isPrev=False 
            self.prev_page=0
        
        if self.curPage<self.totalPage: #뒤으로 이동가능 
            self.isNext=True 
            self.next_page=self.curPage+1 
        else: #더이상 뒤로 갈 수 없음 
            self.isNext=False 
            self.next_page=self.curPage

        self.page_range= range(self.start, self.end)    



