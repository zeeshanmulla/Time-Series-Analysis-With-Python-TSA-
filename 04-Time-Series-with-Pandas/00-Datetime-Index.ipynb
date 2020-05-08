{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "___\n",
    "\n",
    "<a href='http://www.pieriandata.com'><img src='../Pierian_Data_Logo.png'/></a>\n",
    "___\n",
    "<center><em>Copyright Pierian Data</em></center>\n",
    "<center><em>For more information, visit us at <a href='http://www.pieriandata.com'>www.pieriandata.com</a></em></center>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Introduction to Time Series with Pandas\n",
    "\n",
    "Most of our data will have a datatime index, so let's learn how to deal with this sort of data with pandas!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Python Datetime Review\n",
    "In the course introduction section we discussed Python datetime objects."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "from datetime import datetime"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# To illustrate the order of arguments\n",
    "my_year = 2017\n",
    "my_month = 1\n",
    "my_day = 2\n",
    "my_hour = 13\n",
    "my_minute = 30\n",
    "my_second = 15"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# January 2nd, 2017\n",
    "my_date = datetime(my_year,my_month,my_day)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "datetime.datetime(2017, 1, 2, 0, 0)"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Defaults to 0:00\n",
    "my_date "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# January 2nd, 2017 at 13:30:15\n",
    "my_date_time = datetime(my_year,my_month,my_day,my_hour,my_minute,my_second)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "datetime.datetime(2017, 1, 2, 13, 30, 15)"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "my_date_time"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "You can grab any part of the datetime object you want"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "my_date.day"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "13"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "my_date_time.hour"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## NumPy Datetime Arrays\n",
    "We mentioned that NumPy handles dates more efficiently than Python's datetime format.<br>\n",
    "The NumPy data type is called <em>datetime64</em> to distinguish it from Python's datetime.\n",
    "\n",
    "In this section we'll show how to set up datetime arrays in NumPy. These will become useful later on in the course.<br>\n",
    "For more info on NumPy visit https://docs.scipy.org/doc/numpy-1.15.4/reference/arrays.datetime.html"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['2016-03-15', '2017-05-24', '2018-08-09'], dtype='datetime64[D]')"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# CREATE AN ARRAY FROM THREE DATES\n",
    "np.array(['2016-03-15', '2017-05-24', '2018-08-09'], dtype='datetime64')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div class=\"alert alert-info\"><strong>NOTE:</strong> We see the dtype listed as <tt>'datetime64[D]'</tt>. This tells us that NumPy applied a day-level date precision.<br>\n",
    "    If we want we can pass in a different measurement, such as <TT>[h]</TT> for hour or <TT>[Y]</TT> for year.</div>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['2016-03-15T00', '2017-05-24T00', '2018-08-09T00'],\n",
       "      dtype='datetime64[h]')"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.array(['2016-03-15', '2017-05-24', '2018-08-09'], dtype='datetime64[h]')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['2016', '2017', '2018'], dtype='datetime64[Y]')"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.array(['2016-03-15', '2017-05-24', '2018-08-09'], dtype='datetime64[Y]')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## NumPy Date Ranges\n",
    "Just as <tt>np.arange(start,stop,step)</tt> can be used to produce an array of evenly-spaced integers, we can pass a <tt>dtype</tt> argument to obtain an array of dates. Remember that the stop date is <em>exclusive</em>."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['2018-06-01', '2018-06-08', '2018-06-15', '2018-06-22'],\n",
       "      dtype='datetime64[D]')"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# AN ARRAY OF DATES FROM 6/1/18 TO 6/22/18 SPACED ONE WEEK APART\n",
    "np.arange('2018-06-01', '2018-06-23', 7, dtype='datetime64[D]')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "By omitting the step value we can obtain every value based on the precision."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975'],\n",
       "      dtype='datetime64[Y]')"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# AN ARRAY OF DATES FOR EVERY YEAR FROM 1968 TO 1975\n",
    "np.arange('1968', '1976', dtype='datetime64[Y]')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Pandas Datetime Index\n",
    "\n",
    "We'll usually deal with time series as a datetime index when working with pandas dataframes. Fortunately pandas has a lot of functions and methods to work with time series!<br>\n",
    "For more on the pandas DatetimeIndex visit https://pandas.pydata.org/pandas-docs/stable/timeseries.html"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The simplest way to build a DatetimeIndex is with the <tt><strong>pd.date_range()</strong></tt> method:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DatetimeIndex(['2018-07-08', '2018-07-09', '2018-07-10', '2018-07-11',\n",
       "               '2018-07-12', '2018-07-13', '2018-07-14'],\n",
       "              dtype='datetime64[ns]', freq='D')"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# THE WEEK OF JULY 8TH, 2018\n",
    "idx = pd.date_range('7/8/2018', periods=7, freq='D')\n",
    "idx"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div class=\"alert alert-info\"><strong>DatetimeIndex Frequencies:</strong> When we used <tt>pd.date_range()</tt> above, we had to pass in a frequency parameter <tt>'D'</tt>. This created a series of 7 dates spaced one day apart. We'll cover this topic in depth in upcoming lectures, but for now, a list of time series offset aliases like <tt>'D'</tt> can be found <a href='http://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#offset-aliases'>here</a>.</div>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Another way is to convert incoming text with the <tt><strong>pd.to_datetime()</strong></tt> method:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DatetimeIndex(['2018-01-01', '2018-01-02', '2018-01-03', 'NaT'], dtype='datetime64[ns]', freq=None)"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "idx = pd.to_datetime(['Jan 01, 2018','1/2/18','03-Jan-2018',None])\n",
    "idx"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "A third way is to pass a list or an array of datetime objects into the <tt><strong>pd.DatetimeIndex()</strong></tt> method:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['2016-03-15', '2017-05-24', '2018-08-09'], dtype='datetime64[D]')"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Create a NumPy datetime array\n",
    "some_dates = np.array(['2016-03-15', '2017-05-24', '2018-08-09'], dtype='datetime64[D]')\n",
    "some_dates"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DatetimeIndex(['2016-03-15', '2017-05-24', '2018-08-09'], dtype='datetime64[ns]', freq=None)"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Convert to an index\n",
    "idx = pd.DatetimeIndex(some_dates)\n",
    "idx"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Notice that even though the dates came into pandas with a day-level precision, pandas assigns a nanosecond-level precision with the expectation that we might want this later on.\n",
    "\n",
    "To set an existing column as the index, use <tt>.set_index()</tt><br>\n",
    "><tt>df.set_index('Date',inplace=True)</tt>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Pandas Datetime Analysis"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[-1.64971705  1.07943894]\n",
      " [ 0.4587492  -0.04201784]\n",
      " [-1.2793774  -1.85383771]]\n"
     ]
    }
   ],
   "source": [
    "# Create some random data\n",
    "data = np.random.randn(3,2)\n",
    "cols = ['A','B']\n",
    "print(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2016-03-15</th>\n",
       "      <td>-1.649717</td>\n",
       "      <td>1.079439</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-05-24</th>\n",
       "      <td>0.458749</td>\n",
       "      <td>-0.042018</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2018-08-09</th>\n",
       "      <td>-1.279377</td>\n",
       "      <td>-1.853838</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   A         B\n",
       "2016-03-15 -1.649717  1.079439\n",
       "2017-05-24  0.458749 -0.042018\n",
       "2018-08-09 -1.279377 -1.853838"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Create a DataFrame with our random data, our date index, and our columns\n",
    "df = pd.DataFrame(data,idx,cols)\n",
    "df"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now we can perform a typical analysis of our DataFrame"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DatetimeIndex(['2016-03-15', '2017-05-24', '2018-08-09'], dtype='datetime64[ns]', freq=None)"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.index"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Timestamp('2018-08-09 00:00:00')"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Latest Date Value\n",
    "df.index.max()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Latest Date Index Location\n",
    "df.index.argmax()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Timestamp('2016-03-15 00:00:00')"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Earliest Date Value\n",
    "df.index.min()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Earliest Date Index Location\n",
    "df.index.argmin()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div class=\"alert alert-info\"><strong>NOTE:</strong> Normally we would find index locations by running <tt>.idxmin()</tt> or <tt>.idxmax()</tt> on <tt>df['column']</tt> since <tt>.argmin()</tt> and <tt>.argmax()</tt> have been deprecated. However, we still use <tt>.argmin()</tt> and <tt>.argmax()</tt> on the index itself.</div>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Great, let's move on!"
   ]
  }
 ],
 "metadata": {
  "anaconda-cloud": {},
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
