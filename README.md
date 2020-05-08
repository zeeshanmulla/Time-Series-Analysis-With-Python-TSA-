
<ol>
<li>Install Quandl as <code>pip install quandl</code></li>
<li>Use following snippet to download data:</li>
</ol>
<pre><code>import quandl
data = quandl.get("WIKI/AAPL",start_date="1990-01-01",end_date="2018-12-31",collapse="weekly")
data = data[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]
data.rename(columns={'Adj. Open':'Open','Adj. High':'High','Adj. Low':'Low','Adj. Close':'Close','Adj. Volume':'Volume'},inplace=True)
data.to_csv('APPL.csv',index=True)
</code></pre>
<h2><a id="user-content-some-terms" class="anchor" aria-hidden="true" href="#some-terms"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Some Terms</h2>
<p><strong>Stationary Time Series :</strong> A stationary Time Series must satisfy these 3 conditions:</p>
<ol>
<li>The mean of the series should not be a function of time. Mean should not increase or decrease over time.</li>
<li>The variance of series should not be a function of time. This is also known as Homoscedasticity.</li>
<li>Covariance of ith and (i+m)th term should not be a function of time. Covariance must be constant throughout the series.</li>
</ol>
<p>A stationary time series (TS) is simple to predict as we can assume that future statistical properties are the same or proportional to current statistical properties.</p>
<p><strong>White Noise :</strong> By definition a time series that is a white noise process has serially uncorrelated errors and the expected mean of those errors is equal to zero. This means that the errors(residuals) are completely drawn at random from some probability distribution, i.e it is independent and identically distributed.
If our time series model results in white noise residuals, it means we have successfully captured the underlying process and explained any form of correlation, only leaving errors(residuals) which are completely random. Our predicted values differ from the observed values only by a random error component that cannot be forecasted or modeled.</p>
<h2><a id="user-content-univariate-time-series-analysis-techniques" class="anchor" aria-hidden="true" href="#univariate-time-series-analysis-techniques"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Univariate Time Series Analysis Techniques</h2>
<h3><a id="user-content-1-ma---moving-average" class="anchor" aria-hidden="true" href="#1-ma---moving-average"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>1. MA - Moving Average</h3>
<p>In time series analysis, the moving-average model (MA model), also known as moving-average process, is a common approach for modeling univariate time series.</p>
<p>The moving average of a period (extent) m is a series of successive averages of m terms at a time. The data set used for calculating the average starts with first, second, third and etc. at a time and m data taken at a time.</p>
<p><strong>Drawbacks</strong> :</p>
<ol>
<li>The main problem is to determine the extent of the moving average which completely eliminates the oscillatory fluctuations.</li>
<li>This method assumes that the trend is linear but it is not always the case.</li>
<li>It does not provide the trend values for all the terms.</li>
<li>This method cannot be used for forecasting future trend which is the main objective of the time series analysis.</li>
</ol>
<h3><a id="user-content-2-ar---autoregression" class="anchor" aria-hidden="true" href="#2-ar---autoregression"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>2. AR - Autoregression</h3>
<p>Autoregression is a time series model that uses observations from previous time steps as input to a regression equation to predict the value at the next time step. It is a very simple idea that can result in accurate forecasts on a range of time series problems.</p>
<p>A regression model, such as linear regression, models an output value based on a linear combination of input values.
<code>X(t+1) = b0 + b1*X(t-1) + b2*X(t-2)</code></p>
<h4><a id="user-content-autocorrelation-" class="anchor" aria-hidden="true" href="#autocorrelation-"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><strong>Autocorrelation</strong> :</h4>
<p>An autoregression model makes an assumption that the observations at previous time steps are useful to predict the value at the next time step. This relationship between variables is called correlation. The stronger the correlation between the output variable and a specific lagged variable, the more weight that autoregression model can put on that variable when modeling.
Again, because the correlation is calculated between the variable and itself at previous time steps, it is called an autocorrelation. It is also called serial correlation because of the sequenced structure of time series data.</p>
<h3><a id="user-content-3-arma---autoregression-moving-average" class="anchor" aria-hidden="true" href="#3-arma---autoregression-moving-average"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>3. ARMA - Autoregression Moving Average</h3>
<p>An ARMA model, or Autoregressive Moving Average model, is used to describe weakly stationary stochastic time series in terms of two polynomials. The first of these polynomials is for autoregression, the second for the moving average.</p>
<p>Often this model is referred to as the ARMA(p,q) model; where:</p>
<ol>
<li>p is the order of the autoregressive polynomial,</li>
<li>q is the order of the moving average polynomial.</li>
</ol>
<p>The equation is given by:</p>
<p><a target="_blank" rel="noopener noreferrer" href="https://camo.githubusercontent.com/cb4581f2ef9a07a6f2570eac519a71165985e6bd/68747470733a2f2f7777772e73746174697374696373686f77746f2e64617461736369656e636563656e7472616c2e636f6d2f77702d636f6e74656e742f75706c6f6164732f323031382f30392f61726d612e6a706567"><img src="https://camo.githubusercontent.com/cb4581f2ef9a07a6f2570eac519a71165985e6bd/68747470733a2f2f7777772e73746174697374696373686f77746f2e64617461736369656e636563656e7472616c2e636f6d2f77702d636f6e74656e742f75706c6f6164732f323031382f30392f61726d612e6a706567" alt="ARMA" data-canonical-src="https://www.statisticshowto.datasciencecentral.com/wp-content/uploads/2018/09/arma.jpeg" style="max-width:100%;"></a></p>
<p>Where:</p>
<p>φ = the autoregressive model’s parameters,</p>
<p>θ = the moving average model’s parameters.</p>
<p>c = a constant,</p>
<p>ε = error terms (white noise).</p>
<h4><a id="user-content-how-do-we-decide-the-values-of-p-and-q" class="anchor" aria-hidden="true" href="#how-do-we-decide-the-values-of-p-and-q"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><strong>How do we decide the values of p and q?</strong></h4>
<p>To fit data to an ARMA model, we use the Akaike Information Criterion (AIC)across a subset of values for p,q to find the model with minimum AIC and then apply the Ljung-Box test to determine if a good fit has been achieved, for particular values of p,q. If the p-value of the test is greater the required significance, we can conclude that the residuals are independent and white noise.</p>
<h3><a id="user-content-3-arima---autoregression-integrated-moving-average" class="anchor" aria-hidden="true" href="#3-arima---autoregression-integrated-moving-average"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>3. ARIMA - Autoregression Integrated Moving Average</h3>
<p>ARIMA is a natural extension to the class of ARMA models—they can reduce a non-stationary series to a stationary series using a sequence of differences. We’ve seen that many of our Time Series are not stationary, however they can be made stationary by differencing.</p>
<p>ARIMA essentially performs same function, but does so repeatedly, d times, in order to reduce a non-stationary series to a stationary one.</p>
<p>A time series x(t) is ARIMA(p,d,q) model if the series is differenced d times, and it then follows an ARMA(p,q) process.</p>
<h2><a id="user-content-must-read" class="anchor" aria-hidden="true" href="#must-read"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Must Read</h2>
<ol>
<li><a href="https://medium.com/auquan/time-series-analysis-for-financial-data-part-1-stationarity-autocorrelation-and-white-noise-1a1cc2fb23f2" rel="nofollow">Basics of TimeSeries Analysis</a></li>
<li><a href="https://medium.com/auquan/time-series-analysis-for-finance-arma-models-21695e14c999" rel="nofollow">ARMA explained</a></li>
<li><a href="https://medium.com/auquan/time-series-analysis-for-finance-arima-models-acb5e39999df" rel="nofollow">ARIMA explained</a></li>
<li><a href="https://machinelearningmastery.com/time-series-forecasting-methods-in-python-cheat-sheet/" rel="nofollow">TSA Techniqes</a></li>
<li><a href="https://machinelearningmastery.com/make-sample-forecasts-arima-python/" rel="nofollow">Forecasting Tutorial</a></li>
<li><a href="https://towardsdatascience.com/forecasting-exchange-rates-using-arima-in-python-f032f313fc56" rel="nofollow">Forecassting Tutorial</a></li>
</ol>
</article>
  </div>

    </div>

  

  <details class="details-reset details-overlay details-overlay-dark">
    <summary data-hotkey="l" aria-label="Jump to line"></summary>
    <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast linejump" aria-label="Jump to line">
      <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-jump-to-line-form Box-body d-flex" action="" accept-charset="UTF-8" method="get">
        <input class="form-control flex-auto mr-3 linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" aria-label="Jump to line" autofocus>
        <button type="submit" class="btn" data-close-dialog>Go</button>
</form>    </details-dialog>
  </details>
