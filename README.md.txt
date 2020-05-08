# Time-Series-Analysis-Techniques

## How to get data
1. Install Quandl as `pip install quandl`
2. Use following snippet to download data:
```
import quandl
data = quandl.get("WIKI/AAPL",start_date="1990-01-01",end_date="2018-12-31",collapse="weekly")
data = data[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]
data.rename(columns={'Adj. Open':'Open','Adj. High':'High','Adj. Low':'Low','Adj. Close':'Close','Adj. Volume':'Volume'},inplace=True)
data.to_csv('APPL.csv',index=True)
```
## Some Terms
**Stationary Time Series :** A stationary Time Series must satisfy these 3 conditions:
1. The mean of the series should not be a function of time. Mean should not increase or decrease over time.
2. The variance of series should not be a function of time. This is also known as Homoscedasticity.
3. Covariance of ith and (i+m)th term should not be a function of time. Covariance must be constant throughout the series.

A stationary time series (TS) is simple to predict as we can assume that future statistical properties are the same or proportional to current statistical properties.

**White Noise :** By definition a time series that is a white noise process has serially uncorrelated errors and the expected mean of those errors is equal to zero. This means that the errors(residuals) are completely drawn at random from some probability distribution, i.e it is independent and identically distributed.
If our time series model results in white noise residuals, it means we have successfully captured the underlying process and explained any form of correlation, only leaving errors(residuals) which are completely random. Our predicted values differ from the observed values only by a random error component that cannot be forecasted or modeled.

## Univariate Time Series Analysis Techniques
### 1. MA - Moving Average
In time series analysis, the moving-average model (MA model), also known as moving-average process, is a common approach for modeling univariate time series.

The moving average of a period (extent) m is a series of successive averages of m terms at a time. The data set used for calculating the average starts with first, second, third and etc. at a time and m data taken at a time.

**Drawbacks** :
1. The main problem is to determine the extent of the moving average which completely eliminates the oscillatory fluctuations.
2. This method assumes that the trend is linear but it is not always the case.
3. It does not provide the trend values for all the terms.
4. This method cannot be used for forecasting future trend which is the main objective of the time series analysis.

### 2. AR - Autoregression
Autoregression is a time series model that uses observations from previous time steps as input to a regression equation to predict the value at the next time step. It is a very simple idea that can result in accurate forecasts on a range of time series problems.

A regression model, such as linear regression, models an output value based on a linear combination of input values.
``` X(t+1) = b0 + b1*X(t-1) + b2*X(t-2) ```
#### **Autocorrelation** : 
An autoregression model makes an assumption that the observations at previous time steps are useful to predict the value at the next time step. This relationship between variables is called correlation. The stronger the correlation between the output variable and a specific lagged variable, the more weight that autoregression model can put on that variable when modeling.
Again, because the correlation is calculated between the variable and itself at previous time steps, it is called an autocorrelation. It is also called serial correlation because of the sequenced structure of time series data.

### 3. ARMA - Autoregression Moving Average
An ARMA model, or Autoregressive Moving Average model, is used to describe weakly stationary stochastic time series in terms of two polynomials. The first of these polynomials is for autoregression, the second for the moving average.

Often this model is referred to as the ARMA(p,q) model; where:
1. p is the order of the autoregressive polynomial,
2. q is the order of the moving average polynomial.

The equation is given by:

![ARMA](https://www.statisticshowto.datasciencecentral.com/wp-content/uploads/2018/09/arma.jpeg)

Where:

φ = the autoregressive model’s parameters,

θ = the moving average model’s parameters.

c = a constant,

ε = error terms (white noise).

#### **How do we decide the values of p and q?**
To fit data to an ARMA model, we use the Akaike Information Criterion (AIC)across a subset of values for p,q to find the model with minimum AIC and then apply the Ljung-Box test to determine if a good fit has been achieved, for particular values of p,q. If the p-value of the test is greater the required significance, we can conclude that the residuals are independent and white noise.

### 3. ARIMA - Autoregression Integrated Moving Average
ARIMA is a natural extension to the class of ARMA models—they can reduce a non-stationary series to a stationary series using a sequence of differences. We’ve seen that many of our Time Series are not stationary, however they can be made stationary by differencing.

ARIMA essentially performs same function, but does so repeatedly, d times, in order to reduce a non-stationary series to a stationary one.

A time series x(t) is ARIMA(p,d,q) model if the series is differenced d times, and it then follows an ARMA(p,q) process.


## Must Read
1. [Basics of TimeSeries Analysis](https://medium.com/auquan/time-series-analysis-for-financial-data-part-1-stationarity-autocorrelation-and-white-noise-1a1cc2fb23f2)
2. [ARMA explained](https://medium.com/auquan/time-series-analysis-for-finance-arma-models-21695e14c999)
3. [ARIMA explained](https://medium.com/auquan/time-series-analysis-for-finance-arima-models-acb5e39999df)
4. [TSA Techniqes](https://machinelearningmastery.com/time-series-forecasting-methods-in-python-cheat-sheet/)
5. [Forecasting Tutorial](https://machinelearningmastery.com/make-sample-forecasts-arima-python/)
6. [Forecassting Tutorial](https://towardsdatascience.com/forecasting-exchange-rates-using-arima-in-python-f032f313fc56)
