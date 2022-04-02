import daangn_my as daangn
import pandas as pd

if __name__ == "__main__":
    # 크롤러 실행
    daangn.crawling_daangn()
    # bunjang.crawling_bunjang()

    # # 엑셀 merge
    # fileList=['당근마켓_220313_.xlsx', '번개장터_220313.xlsx']
    #
    # df1 = pd.read_excel('당근마켓_220313_.xlsx')
    # df2 = pd.read_excel('번개장터_220313.xlsx')
    # df3 = pd.read_excel('중고나라_220313.xlsx')
    #
    # df = pd.concat([df1, df2, df3], ignore_index=True)
    # df.to_csv("total_t1.csv", index=False, encodings='utf-8')



