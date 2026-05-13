import pandas as pd
import matplotlib.pyplot as plt
import os

# 1. 한글 깨짐 방지 설정 (Windows용)
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

def create_and_plot():
    # 2. 임의의 데이터 생성 (최근 7일간의 방문자 수 추이)
    data = {
        '날짜': ['2026-05-07', '2026-05-08', '2026-05-09', '2026-05-10', '2026-05-11', '2026-05-12', '2026-05-13'],
        '방문자수': [120, 155, 142, 190, 210, 185, 230]
    }
    
    file_name = 'sample_data.csv'
    df_new = pd.DataFrame(data)
    df_new.to_csv(file_name, index=False, encoding='utf-8-sig')
    print(f"'{file_name}' 파일이 생성되었습니다.")

    # 3. 데이터 읽기
    df = pd.read_csv(file_name)
    df['날짜'] = pd.to_datetime(df['날짜']) # 날짜 형식 변환

    # 4. 그래프 작성
    plt.figure(figsize=(10, 5))
    plt.plot(df['날짜'], df['방문자수'], marker='o', color='#2ecc71', linewidth=2, label='일별 방문자')
    
    # 그래프 꾸미기
    plt.title('주간 웹사이트 방문자 추이', fontsize=16, pad=15)
    plt.xlabel('날짜', fontsize=12)
    plt.ylabel('방문자 수(명)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()

    # 5. 저장 및 출력
    plt.tight_layout()
    plt.savefig('visitor_trend.png')
    print("그래프가 'visitor_trend.png'로 저장되었습니다.")
    plt.show()

if __name__ == "__main__":
    create_and_plot()