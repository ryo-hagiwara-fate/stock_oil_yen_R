# 重回帰サンプル
# source("R/重回帰.R",echo=TRUE)

# データ読み込み
cv <- read.csv("datasets/oil_stock_yen.csv",row.names=1)


result <- lm(stock_price~oil_price+yen,data=cv)

# 結果表示
summary(result)

#plot(stock_price~oil_price+yen,data=cv)
#abline(result)