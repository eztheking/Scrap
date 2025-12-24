import requests
from bs4 import BeautifulSoup
import json
import datetime

# 1. 공지사항 페이지 접속 (예시 URL, 실제 RISE ETF 공지사항 경로로 수정 필요)
URL = "https://www.riseetf.com/customer/notice/list" 

def get_dividend_data():
    # 실제 환경에서는 requests로 HTML을 가져온 후 BeautifulSoup으로 파싱합니다.
    # 여기서는 구조 예시를 보여드립니다.
    
    # 임시 데이터 (크롤링 결과값 가정)
    new_data = {
        "date": datetime.datetime.now().strftime("%Y-%m"),
        "name": "RISE 200위클리커버드콜",
        "expected_div": 160,  # 예상분배금
        "tax_div": 5          # 과세분배금
    }
    
    # 기존 데이터 로드 및 업데이트
    try:
        with open('data.json', 'r', encoding='utf-8') as f:
            data_list = json.load(f)
    except FileNotFoundError:
        data_list = []

    # 중복 체크 후 추가
    if not any(d['date'] == new_data['date'] for d in data_list):
        data_list.insert(0, new_data) # 최신순 정렬

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data_list, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    get_dividend_data()
