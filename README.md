# stock_oil_yen_R
被説明変数  => 日経平均株価 / 説明変数 => WTI原油先物価格とドル円為替レート

# やったこと
- 3つのcsv結合  
- Rで重回帰分析  

# 結果

```
Call:
lm(formula = stock_price ~ oil_price + yen, data = cv)

Residuals:
    Min      1Q  Median      3Q     Max 
-6692.3 -1601.9  -429.8  1916.5  9255.9 

Coefficients:
             Estimate Std. Error t value Pr(>|t|)    
(Intercept) -3577.762    740.352  -4.833 1.43e-06 ***
oil_price     -56.031      3.087 -18.151  < 2e-16 ***
yen           237.345      5.576  42.562  < 2e-16 ***
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 2610 on 2418 degrees of freedom
Multiple R-squared:  0.7216,	Adjusted R-squared:  0.7214 
F-statistic:  3134 on 2 and 2418 DF,  p-value: < 2.2e-16
```
