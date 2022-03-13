import daangn_my as daangn
import bunjang_yj as bunjang
import pandas as pd

if __name__ == "__main__":
    # 크롤러 실행
    daangn.crawling_daangn()
    # bunjang.crawling_bunjang()

    # 엑셀 merge
    # fileList=['당근마켓_t1.xlsx', '번개장터_t1.xlsx']
    #
    # df1 = pd.read_excel('당근마켓_t1.xlsx')
    # df2 = pd.read_excel('당근마켓_0313.xlsx')
    #
    # df3 = pd.concat([df1, df2], ignore_index=True)
    # df3.to_csv("total_t1.csv", index=False)



