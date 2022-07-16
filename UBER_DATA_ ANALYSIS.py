{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "eff2b0ab",
   "metadata": {},
   "source": [
    "## Uber data Analysis\n",
    "\n",
    "## Analysis by Stanley Bankesie\n",
    "\n",
    "## stanleyetornam@gmail.com\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e3a86f35",
   "metadata": {},
   "source": [
    "Uber is a ride sharing with their Headquaters in the United States of America. \n",
    "\n",
    "### Problem Statements\n",
    "Dataset used for this analysis were obtain from uber from january 2016 to december 2016. \n",
    "dataset can be downloaded from from Kaggles using this [link](http://www.kaggle.com/zusmani/uberdrives)\n",
    "\n",
    "Questions that this analysis seek to solve are\n",
    "\n",
    "1. Check how long do people travel with uber?\n",
    "2. What hour do most people take uber to their destinations?\n",
    "3. The purpose of trips\n",
    "4. What day has the highest number of trips?\n",
    "5. What are thew number of trips per day in a month?\n",
    "6. The number of trips per month in a year?\n",
    "7. The location with the highest number of start trips\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "67d01a79",
   "metadata": {},
   "source": [
    "#### First we import the necessary libraries that will be used in the Analysis"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "424f2294",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import matplotlib\n",
    "matplotlib.style.use(\"ggplot\")\n",
    "import seaborn as sns\n",
    "import datetime\n",
    "import calendar"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ca9b34ef",
   "metadata": {},
   "source": [
    "#### Then we import our dataset"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "5db82337",
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
       "      <th>START_DATE*</th>\n",
       "      <th>END_DATE*</th>\n",
       "      <th>CATEGORY*</th>\n",
       "      <th>START*</th>\n",
       "      <th>STOP*</th>\n",
       "      <th>MILES*</th>\n",
       "      <th>PURPOSE*</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1/1/2016 21:11</td>\n",
       "      <td>1/1/2016 21:17</td>\n",
       "      <td>Business</td>\n",
       "      <td>Fort Pierce</td>\n",
       "      <td>Fort Pierce</td>\n",
       "      <td>5.1</td>\n",
       "      <td>Meal/Entertain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1/2/2016 1:25</td>\n",
       "      <td>1/2/2016 1:37</td>\n",
       "      <td>Business</td>\n",
       "      <td>Fort Pierce</td>\n",
       "      <td>Fort Pierce</td>\n",
       "      <td>5.0</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1/2/2016 20:25</td>\n",
       "      <td>1/2/2016 20:38</td>\n",
       "      <td>Business</td>\n",
       "      <td>Fort Pierce</td>\n",
       "      <td>Fort Pierce</td>\n",
       "      <td>4.8</td>\n",
       "      <td>Errand/Supplies</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1/5/2016 17:31</td>\n",
       "      <td>1/5/2016 17:45</td>\n",
       "      <td>Business</td>\n",
       "      <td>Fort Pierce</td>\n",
       "      <td>Fort Pierce</td>\n",
       "      <td>4.7</td>\n",
       "      <td>Meeting</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1/6/2016 14:42</td>\n",
       "      <td>1/6/2016 15:49</td>\n",
       "      <td>Business</td>\n",
       "      <td>Fort Pierce</td>\n",
       "      <td>West Palm Beach</td>\n",
       "      <td>63.7</td>\n",
       "      <td>Customer Visit</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1151</th>\n",
       "      <td>12/31/2016 13:24</td>\n",
       "      <td>12/31/2016 13:42</td>\n",
       "      <td>Business</td>\n",
       "      <td>Kar?chi</td>\n",
       "      <td>Unknown Location</td>\n",
       "      <td>3.9</td>\n",
       "      <td>Temporary Site</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1152</th>\n",
       "      <td>12/31/2016 15:03</td>\n",
       "      <td>12/31/2016 15:38</td>\n",
       "      <td>Business</td>\n",
       "      <td>Unknown Location</td>\n",
       "      <td>Unknown Location</td>\n",
       "      <td>16.2</td>\n",
       "      <td>Meeting</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1153</th>\n",
       "      <td>12/31/2016 21:32</td>\n",
       "      <td>12/31/2016 21:50</td>\n",
       "      <td>Business</td>\n",
       "      <td>Katunayake</td>\n",
       "      <td>Gampaha</td>\n",
       "      <td>6.4</td>\n",
       "      <td>Temporary Site</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1154</th>\n",
       "      <td>12/31/2016 22:08</td>\n",
       "      <td>12/31/2016 23:51</td>\n",
       "      <td>Business</td>\n",
       "      <td>Gampaha</td>\n",
       "      <td>Ilukwatta</td>\n",
       "      <td>48.2</td>\n",
       "      <td>Temporary Site</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1155</th>\n",
       "      <td>Totals</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>12204.7</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1156 rows × 7 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "           START_DATE*         END_DATE* CATEGORY*            START*  \\\n",
       "0       1/1/2016 21:11    1/1/2016 21:17  Business       Fort Pierce   \n",
       "1        1/2/2016 1:25     1/2/2016 1:37  Business       Fort Pierce   \n",
       "2       1/2/2016 20:25    1/2/2016 20:38  Business       Fort Pierce   \n",
       "3       1/5/2016 17:31    1/5/2016 17:45  Business       Fort Pierce   \n",
       "4       1/6/2016 14:42    1/6/2016 15:49  Business       Fort Pierce   \n",
       "...                ...               ...       ...               ...   \n",
       "1151  12/31/2016 13:24  12/31/2016 13:42  Business           Kar?chi   \n",
       "1152  12/31/2016 15:03  12/31/2016 15:38  Business  Unknown Location   \n",
       "1153  12/31/2016 21:32  12/31/2016 21:50  Business        Katunayake   \n",
       "1154  12/31/2016 22:08  12/31/2016 23:51  Business           Gampaha   \n",
       "1155            Totals               NaN       NaN               NaN   \n",
       "\n",
       "                 STOP*   MILES*         PURPOSE*  \n",
       "0          Fort Pierce      5.1   Meal/Entertain  \n",
       "1          Fort Pierce      5.0              NaN  \n",
       "2          Fort Pierce      4.8  Errand/Supplies  \n",
       "3          Fort Pierce      4.7          Meeting  \n",
       "4      West Palm Beach     63.7   Customer Visit  \n",
       "...                ...      ...              ...  \n",
       "1151  Unknown Location      3.9   Temporary Site  \n",
       "1152  Unknown Location     16.2          Meeting  \n",
       "1153           Gampaha      6.4   Temporary Site  \n",
       "1154         Ilukwatta     48.2   Temporary Site  \n",
       "1155               NaN  12204.7              NaN  \n",
       "\n",
       "[1156 rows x 7 columns]"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data=pd.read_csv(\"uber_2016.csv\")\n",
    "data"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9c7e583b",
   "metadata": {},
   "source": [
    "#### Checking for Missing Values in the dataset"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "56a50938",
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
       "      <th>START_DATE*</th>\n",
       "      <th>END_DATE*</th>\n",
       "      <th>CATEGORY*</th>\n",
       "      <th>START*</th>\n",
       "      <th>STOP*</th>\n",
       "      <th>MILES*</th>\n",
       "      <th>PURPOSE*</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1151</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1152</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1153</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1154</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1155</th>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1156 rows × 7 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      START_DATE*  END_DATE*  CATEGORY*  START*  STOP*  MILES*  PURPOSE*\n",
       "0           False      False      False   False  False   False     False\n",
       "1           False      False      False   False  False   False      True\n",
       "2           False      False      False   False  False   False     False\n",
       "3           False      False      False   False  False   False     False\n",
       "4           False      False      False   False  False   False     False\n",
       "...           ...        ...        ...     ...    ...     ...       ...\n",
       "1151        False      False      False   False  False   False     False\n",
       "1152        False      False      False   False  False   False     False\n",
       "1153        False      False      False   False  False   False     False\n",
       "1154        False      False      False   False  False   False     False\n",
       "1155        False       True       True    True   True   False      True\n",
       "\n",
       "[1156 rows x 7 columns]"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.isnull()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0fd8b3da",
   "metadata": {},
   "source": [
    "#### Missing values were identified so the next step was to check which columns had the missing values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "9c1bae89",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "START_DATE*    False\n",
       "END_DATE*       True\n",
       "CATEGORY*       True\n",
       "START*          True\n",
       "STOP*           True\n",
       "MILES*         False\n",
       "PURPOSE*        True\n",
       "dtype: bool"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.isnull().any()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f6ee72d9",
   "metadata": {},
   "source": [
    "#### Now checking the number of missing values in each column"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "55595dbe",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "START_DATE*      0\n",
       "END_DATE*        1\n",
       "CATEGORY*        1\n",
       "START*           1\n",
       "STOP*            1\n",
       "MILES*           0\n",
       "PURPOSE*       503\n",
       "dtype: int64"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.isnull().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "17beacc2",
   "metadata": {},
   "source": [
    "#### Removing null/missing values from the dataset "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "2899b0e5",
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
       "      <th>START_DATE*</th>\n",
       "      <th>END_DATE*</th>\n",
       "      <th>CATEGORY*</th>\n",
       "      <th>START*</th>\n",
       "      <th>STOP*</th>\n",
       "      <th>MILES*</th>\n",
       "      <th>PURPOSE*</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1/1/2016 21:11</td>\n",
       "      <td>1/1/2016 21:17</td>\n",
       "      <td>Business</td>\n",
       "      <td>Fort Pierce</td>\n",
       "      <td>Fort Pierce</td>\n",
       "      <td>5.1</td>\n",
       "      <td>Meal/Entertain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1/2/2016 20:25</td>\n",
       "      <td>1/2/2016 20:38</td>\n",
       "      <td>Business</td>\n",
       "      <td>Fort Pierce</td>\n",
       "      <td>Fort Pierce</td>\n",
       "      <td>4.8</td>\n",
       "      <td>Errand/Supplies</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1/5/2016 17:31</td>\n",
       "      <td>1/5/2016 17:45</td>\n",
       "      <td>Business</td>\n",
       "      <td>Fort Pierce</td>\n",
       "      <td>Fort Pierce</td>\n",
       "      <td>4.7</td>\n",
       "      <td>Meeting</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1/6/2016 14:42</td>\n",
       "      <td>1/6/2016 15:49</td>\n",
       "      <td>Business</td>\n",
       "      <td>Fort Pierce</td>\n",
       "      <td>West Palm Beach</td>\n",
       "      <td>63.7</td>\n",
       "      <td>Customer Visit</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>1/6/2016 17:15</td>\n",
       "      <td>1/6/2016 17:19</td>\n",
       "      <td>Business</td>\n",
       "      <td>West Palm Beach</td>\n",
       "      <td>West Palm Beach</td>\n",
       "      <td>4.3</td>\n",
       "      <td>Meal/Entertain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1150</th>\n",
       "      <td>12/31/2016 1:07</td>\n",
       "      <td>12/31/2016 1:14</td>\n",
       "      <td>Business</td>\n",
       "      <td>Kar?chi</td>\n",
       "      <td>Kar?chi</td>\n",
       "      <td>0.7</td>\n",
       "      <td>Meeting</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1151</th>\n",
       "      <td>12/31/2016 13:24</td>\n",
       "      <td>12/31/2016 13:42</td>\n",
       "      <td>Business</td>\n",
       "      <td>Kar?chi</td>\n",
       "      <td>Unknown Location</td>\n",
       "      <td>3.9</td>\n",
       "      <td>Temporary Site</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1152</th>\n",
       "      <td>12/31/2016 15:03</td>\n",
       "      <td>12/31/2016 15:38</td>\n",
       "      <td>Business</td>\n",
       "      <td>Unknown Location</td>\n",
       "      <td>Unknown Location</td>\n",
       "      <td>16.2</td>\n",
       "      <td>Meeting</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1153</th>\n",
       "      <td>12/31/2016 21:32</td>\n",
       "      <td>12/31/2016 21:50</td>\n",
       "      <td>Business</td>\n",
       "      <td>Katunayake</td>\n",
       "      <td>Gampaha</td>\n",
       "      <td>6.4</td>\n",
       "      <td>Temporary Site</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1154</th>\n",
       "      <td>12/31/2016 22:08</td>\n",
       "      <td>12/31/2016 23:51</td>\n",
       "      <td>Business</td>\n",
       "      <td>Gampaha</td>\n",
       "      <td>Ilukwatta</td>\n",
       "      <td>48.2</td>\n",
       "      <td>Temporary Site</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>653 rows × 7 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "           START_DATE*         END_DATE* CATEGORY*            START*  \\\n",
       "0       1/1/2016 21:11    1/1/2016 21:17  Business       Fort Pierce   \n",
       "2       1/2/2016 20:25    1/2/2016 20:38  Business       Fort Pierce   \n",
       "3       1/5/2016 17:31    1/5/2016 17:45  Business       Fort Pierce   \n",
       "4       1/6/2016 14:42    1/6/2016 15:49  Business       Fort Pierce   \n",
       "5       1/6/2016 17:15    1/6/2016 17:19  Business   West Palm Beach   \n",
       "...                ...               ...       ...               ...   \n",
       "1150   12/31/2016 1:07   12/31/2016 1:14  Business           Kar?chi   \n",
       "1151  12/31/2016 13:24  12/31/2016 13:42  Business           Kar?chi   \n",
       "1152  12/31/2016 15:03  12/31/2016 15:38  Business  Unknown Location   \n",
       "1153  12/31/2016 21:32  12/31/2016 21:50  Business        Katunayake   \n",
       "1154  12/31/2016 22:08  12/31/2016 23:51  Business           Gampaha   \n",
       "\n",
       "                 STOP*  MILES*         PURPOSE*  \n",
       "0          Fort Pierce     5.1   Meal/Entertain  \n",
       "2          Fort Pierce     4.8  Errand/Supplies  \n",
       "3          Fort Pierce     4.7          Meeting  \n",
       "4      West Palm Beach    63.7   Customer Visit  \n",
       "5      West Palm Beach     4.3   Meal/Entertain  \n",
       "...                ...     ...              ...  \n",
       "1150           Kar?chi     0.7          Meeting  \n",
       "1151  Unknown Location     3.9   Temporary Site  \n",
       "1152  Unknown Location    16.2          Meeting  \n",
       "1153           Gampaha     6.4   Temporary Site  \n",
       "1154         Ilukwatta    48.2   Temporary Site  \n",
       "\n",
       "[653 rows x 7 columns]"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data=data.dropna()\n",
    "data"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "179e5e28",
   "metadata": {},
   "source": [
    "#### Confirming the removal of missing values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "657423ca",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "START_DATE*    0\n",
       "END_DATE*      0\n",
       "CATEGORY*      0\n",
       "START*         0\n",
       "STOP*          0\n",
       "MILES*         0\n",
       "PURPOSE*       0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.isnull().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a1008910",
   "metadata": {},
   "source": [
    "#### Checking the data type of each column in the dataset"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "37debbfe",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "START_DATE*     object\n",
       "END_DATE*       object\n",
       "CATEGORY*       object\n",
       "START*          object\n",
       "STOP*           object\n",
       "MILES*         float64\n",
       "PURPOSE*        object\n",
       "dtype: object"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.dtypes"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a17b2fab",
   "metadata": {},
   "source": [
    "#### Obtaining further Information of the dataset"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "63fbfed9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Int64Index: 653 entries, 0 to 1154\n",
      "Data columns (total 7 columns):\n",
      " #   Column       Non-Null Count  Dtype  \n",
      "---  ------       --------------  -----  \n",
      " 0   START_DATE*  653 non-null    object \n",
      " 1   END_DATE*    653 non-null    object \n",
      " 2   CATEGORY*    653 non-null    object \n",
      " 3   START*       653 non-null    object \n",
      " 4   STOP*        653 non-null    object \n",
      " 5   MILES*       653 non-null    float64\n",
      " 6   PURPOSE*     653 non-null    object \n",
      "dtypes: float64(1), object(6)\n",
      "memory usage: 40.8+ KB\n"
     ]
    }
   ],
   "source": [
    "data.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "59e75103",
   "metadata": {},
   "source": [
    "#### START_DATE and END_DATE are date and are supposed to be in the datetime format but are in object format so these columns has to be converted to datetime format"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "368d25c9",
   "metadata": {},
   "outputs": [],
   "source": [
    "data[\"START_DATE*\"]=pd.to_datetime(data[\"START_DATE*\"],format=\"%m/%d/%Y %H:%M\")\n",
    "data[\"END_DATE*\"]=pd.to_datetime(data[\"END_DATE*\"],format=\"%m/%d/%Y %H:%M\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1a7c7b2f",
   "metadata": {},
   "source": [
    "#### Confirmation of datatype format convert"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "0095e163",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "START_DATE*    datetime64[ns]\n",
       "END_DATE*      datetime64[ns]\n",
       "CATEGORY*              object\n",
       "START*                 object\n",
       "STOP*                  object\n",
       "MILES*                float64\n",
       "PURPOSE*               object\n",
       "dtype: object"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "eae3f9cd",
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
       "      <th>START_DATE*</th>\n",
       "      <th>END_DATE*</th>\n",
       "      <th>CATEGORY*</th>\n",
       "      <th>START*</th>\n",
       "      <th>STOP*</th>\n",
       "      <th>MILES*</th>\n",
       "      <th>PURPOSE*</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2016-01-01 21:11:00</td>\n",
       "      <td>2016-01-01 21:17:00</td>\n",
       "      <td>Business</td>\n",
       "      <td>Fort Pierce</td>\n",
       "      <td>Fort Pierce</td>\n",
       "      <td>5.1</td>\n",
       "      <td>Meal/Entertain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2016-01-02 20:25:00</td>\n",
       "      <td>2016-01-02 20:38:00</td>\n",
       "      <td>Business</td>\n",
       "      <td>Fort Pierce</td>\n",
       "      <td>Fort Pierce</td>\n",
       "      <td>4.8</td>\n",
       "      <td>Errand/Supplies</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2016-01-05 17:31:00</td>\n",
       "      <td>2016-01-05 17:45:00</td>\n",
       "      <td>Business</td>\n",
       "      <td>Fort Pierce</td>\n",
       "      <td>Fort Pierce</td>\n",
       "      <td>4.7</td>\n",
       "      <td>Meeting</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2016-01-06 14:42:00</td>\n",
       "      <td>2016-01-06 15:49:00</td>\n",
       "      <td>Business</td>\n",
       "      <td>Fort Pierce</td>\n",
       "      <td>West Palm Beach</td>\n",
       "      <td>63.7</td>\n",
       "      <td>Customer Visit</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>2016-01-06 17:15:00</td>\n",
       "      <td>2016-01-06 17:19:00</td>\n",
       "      <td>Business</td>\n",
       "      <td>West Palm Beach</td>\n",
       "      <td>West Palm Beach</td>\n",
       "      <td>4.3</td>\n",
       "      <td>Meal/Entertain</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          START_DATE*           END_DATE* CATEGORY*           START*  \\\n",
       "0 2016-01-01 21:11:00 2016-01-01 21:17:00  Business      Fort Pierce   \n",
       "2 2016-01-02 20:25:00 2016-01-02 20:38:00  Business      Fort Pierce   \n",
       "3 2016-01-05 17:31:00 2016-01-05 17:45:00  Business      Fort Pierce   \n",
       "4 2016-01-06 14:42:00 2016-01-06 15:49:00  Business      Fort Pierce   \n",
       "5 2016-01-06 17:15:00 2016-01-06 17:19:00  Business  West Palm Beach   \n",
       "\n",
       "             STOP*  MILES*         PURPOSE*  \n",
       "0      Fort Pierce     5.1   Meal/Entertain  \n",
       "2      Fort Pierce     4.8  Errand/Supplies  \n",
       "3      Fort Pierce     4.7          Meeting  \n",
       "4  West Palm Beach    63.7   Customer Visit  \n",
       "5  West Palm Beach     4.3   Meal/Entertain  "
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c2b68b7f",
   "metadata": {},
   "source": [
    "#### Date and time are in one column so the format will be changed to seperate the date and time into different column"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "29d5594b",
   "metadata": {},
   "outputs": [],
   "source": [
    "hour=[]\n",
    "day=[]\n",
    "dayofweek=[]\n",
    "month=[]\n",
    "weekday=[]\n",
    "\n",
    "for x in data[\"START_DATE*\"]:\n",
    "    hour.append(x.hour)\n",
    "    day.append(x.day)\n",
    "    dayofweek.append(x.dayofweek)\n",
    "    month.append(x.month)\n",
    "    weekday.append(calendar.day_name[dayofweek[-1]])\n",
    "    \n",
    "data[\"HOUR\"] = hour\n",
    "data[\"DAY\"] = day\n",
    "data[\"DAY_OF_WEEK\"] = dayofweek\n",
    "data[\"MONTH\"] = month\n",
    "data[\"WEEKDAY\"] = weekday\n",
    "    \n",
    "    \n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8c613825",
   "metadata": {},
   "source": [
    "#### Confirmation of splitting date and time into seperate columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "e4aaa9ba",
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
       "      <th>START_DATE*</th>\n",
       "      <th>END_DATE*</th>\n",
       "      <th>CATEGORY*</th>\n",
       "      <th>START*</th>\n",
       "      <th>STOP*</th>\n",
       "      <th>MILES*</th>\n",
       "      <th>PURPOSE*</th>\n",
       "      <th>HOUR</th>\n",
       "      <th>DAY</th>\n",
       "      <th>DAY_OF_WEEK</th>\n",
       "      <th>MONTH</th>\n",
       "      <th>WEEKDAY</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2016-01-01 21:11:00</td>\n",
       "      <td>2016-01-01 21:17:00</td>\n",
       "      <td>Business</td>\n",
       "      <td>Fort Pierce</td>\n",
       "      <td>Fort Pierce</td>\n",
       "      <td>5.1</td>\n",
       "      <td>Meal/Entertain</td>\n",
       "      <td>21</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>Friday</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2016-01-02 20:25:00</td>\n",
       "      <td>2016-01-02 20:38:00</td>\n",
       "      <td>Business</td>\n",
       "      <td>Fort Pierce</td>\n",
       "      <td>Fort Pierce</td>\n",
       "      <td>4.8</td>\n",
       "      <td>Errand/Supplies</td>\n",
       "      <td>20</td>\n",
       "      <td>2</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "      <td>Saturday</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2016-01-05 17:31:00</td>\n",
       "      <td>2016-01-05 17:45:00</td>\n",
       "      <td>Business</td>\n",
       "      <td>Fort Pierce</td>\n",
       "      <td>Fort Pierce</td>\n",
       "      <td>4.7</td>\n",
       "      <td>Meeting</td>\n",
       "      <td>17</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Tuesday</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2016-01-06 14:42:00</td>\n",
       "      <td>2016-01-06 15:49:00</td>\n",
       "      <td>Business</td>\n",
       "      <td>Fort Pierce</td>\n",
       "      <td>West Palm Beach</td>\n",
       "      <td>63.7</td>\n",
       "      <td>Customer Visit</td>\n",
       "      <td>14</td>\n",
       "      <td>6</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>Wednesday</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>2016-01-06 17:15:00</td>\n",
       "      <td>2016-01-06 17:19:00</td>\n",
       "      <td>Business</td>\n",
       "      <td>West Palm Beach</td>\n",
       "      <td>West Palm Beach</td>\n",
       "      <td>4.3</td>\n",
       "      <td>Meal/Entertain</td>\n",
       "      <td>17</td>\n",
       "      <td>6</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>Wednesday</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          START_DATE*           END_DATE* CATEGORY*           START*  \\\n",
       "0 2016-01-01 21:11:00 2016-01-01 21:17:00  Business      Fort Pierce   \n",
       "2 2016-01-02 20:25:00 2016-01-02 20:38:00  Business      Fort Pierce   \n",
       "3 2016-01-05 17:31:00 2016-01-05 17:45:00  Business      Fort Pierce   \n",
       "4 2016-01-06 14:42:00 2016-01-06 15:49:00  Business      Fort Pierce   \n",
       "5 2016-01-06 17:15:00 2016-01-06 17:19:00  Business  West Palm Beach   \n",
       "\n",
       "             STOP*  MILES*         PURPOSE*  HOUR  DAY  DAY_OF_WEEK  MONTH  \\\n",
       "0      Fort Pierce     5.1   Meal/Entertain    21    1            4      1   \n",
       "2      Fort Pierce     4.8  Errand/Supplies    20    2            5      1   \n",
       "3      Fort Pierce     4.7          Meeting    17    5            1      1   \n",
       "4  West Palm Beach    63.7   Customer Visit    14    6            2      1   \n",
       "5  West Palm Beach     4.3   Meal/Entertain    17    6            2      1   \n",
       "\n",
       "     WEEKDAY  \n",
       "0     Friday  \n",
       "2   Saturday  \n",
       "3    Tuesday  \n",
       "4  Wednesday  \n",
       "5  Wednesday  "
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2a989701",
   "metadata": {},
   "source": [
    "#### Category of trips"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "b32a8b0f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Business    647\n",
       "Personal      6\n",
       "Name: CATEGORY*, dtype: int64"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[\"CATEGORY*\"].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "af9dedbd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='CATEGORY*', ylabel='count'>"
      ]
     },
     "execution_count": 76,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(x=\"CATEGORY*\",data=data)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d54c4d48",
   "metadata": {},
   "source": [
    "#### Distance (Miles) Being covered \n",
    "People prefer using uber for shorter trips between 1 to 50 miles"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "id": "98ce1067",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:ylabel='Frequency'>"
      ]
     },
     "execution_count": 77,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "data[\"MILES*\"].plot.hist()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6bf854b6",
   "metadata": {},
   "source": [
    "#### Particular Hours people use uber the most\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "7107bee2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:title={'center':'Number of Trips in an Hour'}, xlabel='Hours', ylabel='Frequency'>"
      ]
     },
     "execution_count": 78,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAmEAAAFTCAYAAABxr9twAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/YYfK9AAAACXBIWXMAAAsTAAALEwEAmpwYAAAvoElEQVR4nO3deVTU9f7H8dcACgrKIqiBpiaauZuApRWadCzzFnW7ama5V6a5YO651dUwU8rr0r1q6k3rZ/4q2vVeUmlXLE2z7KhlXhEXZLsqi8D394fH+Ynr4CwfwefjHM/h+52Z9/s9MwgvPt/vzNgsy7IEAAAAj/IyPQAAAMD1iBAGAABgACEMAADAAEIYAACAAYQwAAAAAwhhAAAABhDCAJRhs9m0atUq02OUUVxcrIEDB6pWrVqy2WzatGmTS+quWLFCPj4+Lql1OdfiYwrAPEIYcI3o37+/bDabRo8efcFl1/sv8XfffVdvvfWWPvroI2VkZKhjx45lLl+xYoVsNttl/02fPv2Cur169VJ6errb58/IyNAjjzzi9j5Xq3///oqLi7voZdf79x7gTu7/ExCAw6pVq6aFCxdq6NChatq0qelxXKqoqEhVq1a9qtvu2bNHERERF4Svs3r16qV7773Xvj1mzBj9/vvveu+99+z7AgIC7F9blqXi4mJVq1ZN1apVu6qZyqNu3bpu71HROfP9AVRUrIQB15COHTuqffv2Gjt27GWvd7HVibi4OPXv39++3bBhQ02ZMkVDhw5VYGCgateurQULFqiwsFDPPvusgoODFRERoQULFlxQ//jx4/rzn/8sf39/hYeHa968eWUuP3HihEaOHKmIiAhVr15d7dq1KxN49u/fL5vNptWrV6t79+7y9/fXpEmTLnpfLMvSK6+8optuuklVq1ZV48aN9eqrr9ov79y5s6ZMmaLffvtNNptNDRs2vKBGtWrVVLduXfu/atWqqWrVqvbtdevWKSgoSBs3blS7du3k6+ur9evXX3A48ux2SkqKWrRoIT8/P8XExOiHH36wXycvL08DBgxQ3bp15evrq/r16yshIeGi9+2s858vm82mRYsW6fHHH1eNGjVUv359vfzyy5etYVmWhgwZosaNG6tatWq66aabNGnSJBUWFtqvM336dEVGRuqDDz5Qs2bN5O/vry5dumjfvn2XrV0eGRkZ6t27t4KCglStWjV17txZW7dutV++adMm2Ww2HTx4sMztfHx8tGLFCknl+/4AKjNCGHCNSUpK0kcffaSNGzc6Xetvf/ubmjRpou+//14jRozQiBEj9NBDD6lRo0ZKS0vT8OHDNWLECP38889lbjdjxgx17txZ27Zt0/jx4zVu3Dh7yLIsS3/605/0448/as2aNfrpp580dOhQ9e7dW59//nmZOuPHj1efPn20c+dODRs27KIzLlq0SFOmTNGECRO0a9cujR07VhMmTNCyZcskSe+9957GjBmjhg0bKiMjQ2lpaVf1WJSWlmrcuHGaO3eudu/erQ4dOlz2eosWLdKWLVtUu3Zt3X///Tp16pQk6fnnn9cPP/ygDz74QHv27NGaNWt0yy23lHueGTNm6K677tL27ds1duxYjR8//rLPuWVZqlOnjt566y398ssvevXVV7V8+XLNmjWrzPUyMjK0ePFirV69Wt98841ycnI0cODAcs93qRni4+O1e/duffzxx9qyZYvq1Kmje+65R5mZmeWu58j3B1CpWQCuCf369bO6du1qWZZl9e7d22rbtq1VUlJiWZZlSbLefPNN+3XP37Ysy+ratavVr18/+3aDBg2sBx980L5dUlJi1ahRw+rRo0eZfUFBQdbf/va3MrX79u1bpvajjz5qderUybIsy9q4caPl6+tr5eTklLnOgAED7P1+//13S5L1wgsvXPF+16tXzxo7dmyZfaNGjbIaNWpk3542bZrVuHHjK9Y6a9CgQVZsbKx9e/ny5ZYk64svvihzveXLl1ve3t4XXC8lJcW+Lysry/L397eWLFliWZZlPfDAA2UeZ0dc7Pl79tlny1zn5ptvtiZMmFCuuvPmzbMiIyPt29OmTbO8vb2to0eP2ve9/fbbls1ms/Lz8y9Zp1+/fpa3t7fl7+9/wb9zZ09JSbEkWbt27bLftqCgwKpbt641Y8YMy7LOfH9Isv7zn/+U6eHt7W0tX77csqzyfX8AlRnnhAHXoMTERDVr1kwrVqxwahWjTZs29q+9vLwUFham1q1bl9lXu3ZtHT16tMztbr/99jLbnTp10rp16yRJaWlpKioqUkRERJnrFBUVqUmTJmX2xcTEXHa+vLw8HTx4UHfddVeZ/bGxsXrttdd06tQpVa9e/Qr30nHR0dEOXe/c+x8cHKxbbrnFvlr4zDPP6M9//rO2bt2q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LbfcooEDB2rHjh365ptvnH7Sc3Nz9fHHH8uyLOXn59v/QpEu/MvualSpUkU//vijTp06JZvNpi1btigmJkY///yzS37wSVK3bt300ksvKT4+Xm3atNGKFSsUExOjn3766aI/rMpj1KhRSk5O1vTp0+3L/UFBQWrfvr1Gjx7tgund/wvOEyHG19dXu3fvVrNmzbR161b76o6Xl5fT30d/+ctfLlljwIABTtU+yxNhu379+i7/GLazoqKiVFBQID8/P/Xu3du+//DhwwoPD3e6fvv27fXTTz+pdevW9n2dO3dWUFCQ3njjDafrn3XuCr+/v7/9jzZX8fLyUtOmTV1a8yxXPM5Xcrn/ryNHjnS6/tkAdr6aNWu69UUGvr6+ql27tsvqVatWzemf/ZdydhX1Ypo1a+Z0/Ur16sg1a9bowQcfLPMSUunMD6bVq1drzJgxLuu1detWvf/++zp69KiWLFnisrqvvvrqZf/CctbatWvLbHfr1k01a9ZUTk6OVq1a5fQrkvbv36/Vq1fLZrOpX79++te//qXU1FSFhIToqaee0s033+xU/bN27dqlf/3rX8rIyFBJSYlCQ0MVHR2tLl26OH2uQXp6uo4fP66mTZu6/OXI0plDqK1bty7zC+5s/TfeeEPz5893qv53332nG2+88aK/JM6GYmf98ccfev3115WRkaH69etr6NChCg8PV15enr766it1797dqfrufEm4dOawf3JysrZu3XpB2I6Pj3fJIUN3c/djdKn627Zts692A3BOpQphl+OKl/Oer6ioSIcPH9aNN97olvrnc3ePil7fFT3c/nLkK+A5qPzPgSt89tlnWrdundseI3fXB3BGpToceTnvvPOOy3+wVq1a1X5umDvqn8/dPSp6fVf0+PzzzzV79mz5+fnp6NGjmjdvno4dO6bu3bu75HDtlfAcVP7nwBVSUlLc+hi5uz6AMypVCHP3y3ndXd8TPSp6fXf3cPfLkSWegyupDM+Bu7n7MfLEcwCgkoUwd7+c1931PdGjotd3dw93vxxZ4jm4ksrwHLibux8jTzwHACpZCHP3y3ndXd8TPSp6fXf3cPfLkSWegyupDM+Bu7n7MfLEcwDgOjoxHwAA4FrimjduAgAAQLkQwgAAAAwghAEAABhACANQ4Q0bNkw7duwos2/Tpk0V4pWOAK5fhDAAcFBJSYnpEQBUIpXqLSoA4GIOHjyopUuXav/+/QoJCVGfPn0UFRUlSZo+fbruvPNOde3aVdKZFbTPP/9cL774oiSpZ8+eGjhwoD799FOVlJRowYIFWrlypb766iudPn1aYWFhGjFihP3TMwDAUYQwAJVacXGxZs+erS5duuj555/X7t279fLLLysxMfGiH3J+MWlpaZo1a5aqVq2qH3/8Ub/88otee+01Va9eXenp6Re86SsAOIIQBqBSmDNnTpk3GC0uLlajRo20Z88eFRQUKD4+Xl5eXmrZsqVuvfVWffXVV+rZs6dDtR966CEFBARIknx8fFRQUKD09HRFRkaqXr16brk/ACo/QhiASmHs2LFq3bq1ffvsYcXs7GyFhobKy+v/T4ENCwtTVlaWw7Vr1apl/7ply5bq1q2bli1bpszMTMXExOjxxx9X9erVXXNHAFw3ODEfQKUWHByszMxMlZaW2vdlZmYqJCREkuTr66vCwkL7ZTk5ORfUsNlsZba7d++u2bNna968ecrIyNCHH37onuEBVGqEMACVWpMmTeTn56cPP/xQxcXF2rVrl77//nt16tRJktSwYUNt2bJFhYWFOnz4sDZs2HDZenv37tWePXtUXFwsX19fValSpcwqGwA4isORACo1Hx8fjRs3TkuXLtX777+vkJAQDR8+XBEREZKk+++/X/v27dOQIUPUoEED3XHHHdq5c+cl6+Xn52vlypU6cuSIqlatqjZt2uiBBx7w1N0BUInwAd4AAAAGsIYOAABgACEMAADAAEIYAACAAYQwAAAAAwhhAAAABhDCAAAADCCEAQAAGEAIAwAAMOD/AEwlHVeHZrGiAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 720x360 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "hours = data[\"START_DATE*\"].dt.hour.value_counts()\n",
    "hours.plot(kind =\"bar\",xlabel = \"Hours\",ylabel=\"Frequency\",title = \"Number of Trips in an Hour\",color=\"green\",figsize=(10,5))\n",
    "#plt.xlabel(\"Hours\")\n",
    "#plt.ylabel(\"Frequency\")\n",
    "#plt.title(\"Number of Trips in an Hour\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4d827cea",
   "metadata": {},
   "source": [
    "#### Purposes of Rides  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "cc2d90e6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 79,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAlYAAAF2CAYAAACs4da0AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/YYfK9AAAACXBIWXMAAAsTAAALEwEAmpwYAABCE0lEQVR4nO3deViU5f4/8PcMOyI7YiCIuKSogCgu4IKKZaseJUszNeuoWef8FHM5tpp5RBE1FfKYpZnVUUs9fS2/dAhDAc0Fd1TcUNkEBAQEHHDm9wcX84XEzJkbnnke3q/r6rqYG4bnc6fOvOd+7kWl0+l0ICIiIiKjqaUugIiIiEgpGKyIiIiIBGGwIiIiIhKEwYqIiIhIEAYrIiIiIkEYrIiIiIgEYbAiIiIiEsRc6gLq5OTkNNu1XF1dUVhY2GzXa27sn7wpuX9K7hvA/skd+ydfzd03Dw+PB36PI1ZEREREgjBYEREREQnCYEVEREQkCIMVERERkSAMVkRERESCMFgRERERCcJgRURERCQIgxURERGRIAxWRERERIIwWBEREREJYjJH2hjCw9PT8Oca8Jyc7GyDr0dERETKxxErIiIiIkEYrIiIiIgEYbAiIiIiEoTBioiIiEgQBisiIiIiQRisiIiIiARhsCIiIiIShMGKiIiISBAGKyIiIiJBGKyIiIiIBGGwIiIiIhKEwYqIiIhIEAYrIiIiIkHMH/YDcXFxSEtLg4ODA2JiYgAAq1atQk5ODgCgoqICtra2iI6ORn5+PmbPng0PDw8AQOfOnTFt2rQmLJ+IiIjIdDw0WIWFhWHkyJGIjY3Vt82ePVv/9ZYtW2Bra6t/3LZtW0RHRwsuk4iIiMj0PfRWoJ+fH+zs7Br9nk6nw8GDBxEaGiq8MCIiIiK5eeiI1R85d+4cHBwc8Nhjj+nb8vPzMW/ePNjY2OCll15Ct27dGn1uQkICEhISAABRUVFwdXU1ppRmIYcaAcDc3Fw2tRqC/ZMvJfcNYP/kjv2TL1Pqm1HBKiUlpcFolZOTE+Li4tC6dWtcuXIF0dHRiImJaXCrsE54eDjCw8P1jwsLCx/5+h6GlW0wQ2qUgqurq2xqNQT7J19K7hvA/skd+ydfzd23urnkjTF4VeC9e/dw+PBhhISE6NssLCzQunVrAICvry/c3d2Rm5tr6CWIiIiIZMXgYHX69Gl4eHjAxcVF31ZaWgqtVgsAuHnzJnJzc+Hu7m58lUREREQy8NBbgatXr0Z6ejrKysowY8YMjBs3DsOGDbvvNiAApKenY/v27TAzM4NarcZf//rXB058JyIiIlKahwarWbNmNdr+5ptv3tfWv39/9O/f3+iiiIiIiOSIO68TERERCcJgRURERCQIgxURERGRIAxWRERERIIwWBEREREJwmBFREREJAiDFREREZEgDFZEREREgjBYEREREQnCYEVEREQkCIMVERERkSAMVkRERESCMFgRERERCcJgRURERCQIgxURERGRIOZSF0AP5uHpafhzDXhOTna2wdcjIiIijlgRERERCcNgRURERCQIgxURERGRIAxWRERERIIwWBEREREJwmBFREREJAiDFREREZEgDFZEREREgjBYEREREQny0J3X4+LikJaWBgcHB8TExAAAtm/fjl9++QX29vYAgPHjxyMoKAgAsGvXLiQmJkKtVuPVV19FYGBg01VPREREZEIeGqzCwsIwcuRIxMbGNmh/5pln8Pzzzzdoy8rKQmpqKlauXIni4mIsXrwYn3zyCdRqDowRERGR8j008fj5+cHOzu5P/bIjR44gJCQEFhYWaNOmDdq2bYtLly4ZXSQRERGRHBh8CHN8fDz2798PX19fTJo0CXZ2digqKkLnzp31P+Ps7IyioiIhhRIRERGZOoOC1RNPPIGIiAgAwLZt27BlyxbMnDkTOp3uT/+OhIQEJCQkAACioqLg6upqSCnNSg41GkMu/TM3N5dNrYZQcv+U3DeA/ZM79k++TKlvBgUrR0dH/dfDhw/HsmXLAAAuLi64deuW/ntFRUVwdnZu9HeEh4cjPDxc/7iwsPCR6/B45GcYx5AajaH0/hnK1dVVNrUaQsn9U3LfAPZP7tg/+Wruvnl4PPgd2qBZ5cXFxfqvDx8+DC8vLwBAnz59kJqaiurqauTn5yM3NxedOnUy5BJEREREsvPQEavVq1cjPT0dZWVlmDFjBsaNG4ezZ88iMzMTKpUKbm5umDZtGgDAy8sLAwYMQGRkJNRqNV577TWuCCQiIqIW46HBatasWfe1DRs27IE/P2bMGIwZM8aoooiIiIjkiMNJRERERIIwWBEREREJwmBFREREJAiDFREREZEgDFZEREREgjBYEREREQnCYEVEREQkCIMVERERkSAMVkRERESCMFgR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\n",
      "text/plain": [
       "<Figure size 720x360 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "data[\"PURPOSE*\"].value_counts().plot(kind=\"bar\",figsize = (10,5), color = \"red\",)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "21e9fd96",
   "metadata": {},
   "source": [
    "#### days of the week with the highest number of trips"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "78e7b23f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 82,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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a8SIETpw4IBGjhyp6dOnW11ayPN6vdq1a5c2bdqkkydPavz48dq/f7+io6P18MMPW11et/TYAqF2N3fuXI0YMUJ33HGHhg4d6t+enZ2tffv2WVhZ6PvlL3+pKVOm6O6771ZkZKR/e2Jior7//e9bWJk9rFixosvTB4SqS+PYDQ79C9zGjRtVUVGh+Ph45eXlafr06YqIiJDX69VDDz1EsLqE9evX64MPPlBmZqYKCgo0aNAg/3MPPfSQhZVdHkasutDW1qbo6Giry0Av1NjYqDfffFO1tbVqb2/3b3/88cctrMo+OHaDQ/8C99prrykvL0/Jyclfea62tpaLAS6hrKxMEydOVFRU1Feea2lpsc18K4JVF9rb21VWVvaV/9zmzJljYVX2cPz4cf32t79VbW2tOjo6/NtXrVplYVX28fTTT2vChAn6wx/+oB/+8IcqLy9XfHw8n3a7iWM3OPQveKdPn77gd5/L5bKwGntpbm7W559/fsG/veHDh1tY0eXjVGAXVq1apdTUVO3Zs0f//u//rvfee09paWlWl2ULa9as0bRp07R+/XotXLhQmzZtsrokW2lqalJeXp42btyo4cOHa/jw4YxWXQaO3eDQv8B98MEHevnll9XQ0KD4+HjV19crLS1Ny5cvt7o0W/jzn/+sjRs3yuPxaODAgaqpqdGQIUNs9/uPBUK78Pnnn+v73/++oqKilJubqwULFrDwZTe1t7crMzNTPp9PycnJmjZtmj766COry7KNiIgvPu84nU5VVVXp8OHD8ng8FldlHxy7waF/gXvttdf0zDPPqH///lq9erUWLVp0wTw1fL2NGzfqv//7v+VyufT4449ryZIlio+Pt7qsy8aIVRfCw8MlSbGxsTpy5Ij69eunuro6i6uyh8jISHm9XvXv31/vvPOOEhMTdfr0aavLso2CggK1tLTo3nvv1bp169TS0qIZM2ZYXZZtcOwGh/4FLjw8XH379pXP55PX69UNN9yg3/zmN1aXZRuRkZH+C546OjqUlpamY8eOWVzV5SNYdcHtdqu5uVl33nmnlixZora2Nk2bNs3qsmxhxowZam9v18yZM/Xaa6/po48+0oMPPmh1WbZx0003SZLS09NtNwQeCjh2g0P/AhcbG6u2tjYNGzZMK1euVEJCgj+o4tISExN15swZjR07Vk8//bRiY2OVmJhodVmX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\n",
      "text/plain": [
       "<Figure size 720x360 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "data[\"WEEKDAY\"].value_counts().plot(kind = \"bar\", figsize = (10,5), color= \"brown\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9149f66b",
   "metadata": {},
   "source": [
    "#### Day with the highest number of trips per month"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "87b86b8e",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 83,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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7ckhhxxyyCGHHPty3G63LTN0xhyPx9PseS36FF5iYqKcTqecTqfGjBmjsrKylsQAAAB0Si0qUBUVFcF/b9++XcnJybYNBAAAEOlCvoS3YsUKffnllzp58qSmT5+uiRMn6osvvtDevXvlcDjUp08fTZs2rT1mBQAAiAghC9SsWbPOO+2Xv/xlW8wCAADQKbASOQAAgCEKFAAAgKEWrwMFAAC6Fu8ab8htDjx8oB0miXwcgQIAADBEgQIAADBEgQIAADBEgQIAADBEgQIAADBEgQIAADBEgQIAADBEgQIAADBEgQIAADBEgQIAADBEgQIAADBEgQIAADBEgQIAADBEgQIAADBEgQIAADBEgQIAADAU3dEDAACArsW7xhtymwMPH2i3nLbAESgAAABDFCgAAABDFCgAAABDFCgAAABDFCgAAABDFCgAAABDFCgAAABDFCgAAABDFCgAAABDFCgAAABDFCgAAABDFCgAAABDIb9MePXq1dq5c6cSEhKUn58vSaqurlZBQYGOHj2qPn36aPbs2YqLi2vzYQEAACJByCNQo0aN0vz58885rbCwUIMGDdLKlSs1aNAgFRYWttV8AAAAESdkgUpNTT3v6FJxcbGysrIkSVlZWSouLm6b6QAAACJQi94DVVlZKZfLJUlyuVyqqqqydSgAAIBIFvI9UK3l9/vl9/slSXl5eXK73UaXN92eHHLIIYcccsghp6mYZTEht6mbV2d0vS0qUAkJCaqoqJDL5VJFRYXi4+Ob3dbn88nn8wV/Li8vN7ou0+3JIYcccsghhxxy7MjxeDzNbt+il/DS0tJUVFQkSSoqKlJ6enpLYgAAADqlkEegVqxYoS+//FInT57U9OnTNXHiRGVnZ6ugoECbN2+W2+1WTk5Oe8wKAAAQEUIWqFmzZl3w9EWLFtk9CwAAQKfASuQAAACGKFAAAACGKFAAAACGKFAAAACGKFAAAACGKFAAAACGKFAAAACGKFAAAACGKFAAAACGKFAAAACGKFAAAACGKFAAAACGKFAAAACGKFAAAACGKFAAAACGKFAAAACGKFAAAACGKFAAAACGKFAAAACGKFAAAACGKFAAAACGKFAAAACGKFAAAACGKFAAAACGKFAAAACGKFAAAACGKFAAAACGKFAAAACGKFAAAACGKFAAAACGKFAAAACGKFAAAACGKFAAAACGoltz4RkzZig2NlZOp1NRUVHKy8uzay4AAICI1aoCJUmLFy9WfHy8HbMAAAB0CryEBwAAYKjVR6CeeOIJSdJNN90kn8933vl+v19+v1+SlJeXJ7fbbZRvuj055JBDDjnkkENOW+e0qkD93//9n5KSklRZWanHH39cHo9Hqamp52zj8/nOKVbl5eVG12G6PTnkkEMOOeSQQ44dOR6Pp9ntW/USXlJSkiQpISFB6enp2r17d2viAAAAOoUWF6ja2lrV1NQE//3ZZ58pJSXFtsEAAAAiVYtfwqusrNTTTz8tSQoEAho5cqSGDh1q11wAAAARq8UFqm/fvlq+fLmdswAAAHQKLGMAAABgiAIFAABgiAIFAABgiAIFAABgiAIFAABgiAIFAABgiAIFAABgiAIFAABgiAIFAABgiAIFAABgiAIFAABgiAIFAABgiAIFAABgiAIFAABgiAIFAABgiAIFAABgiAIFAABgiAIFAABgiAIFAABgiAIFAABgiAIFAABgiAIFAABgiAIFAABgiAIFAABgiAIFAABgiAIFAABgiAIFAABgiAIFAABgiAIFAABgiAIFAABgiAIFAABgiAIFAABgiAIFAABgKLo1Fy4pKdErr7yixsZGjRkzRtnZ2TaNBQAAELlafASqsbFRL730kubPn6+CggJt3bpV+/fvt3M2AACAiNTiArV7927169dPffv2VXR0tG644QYVFxfbORsAAEBEcliWZbXkgtu2bVNJSYmmT58uSdqyZYt27dqlBx988Jzt/H6//H6/JCkvL6+V4wIAAHS8Fh+BulDvcjgc553m8/mUl5cXdnmaO3duS0cihxxyyCGHHHLIaZecFheo3r1769ixY8Gfjx07JpfL1aphAAAAOoMWF6grrrhChw4d0pEjR9TQ0KCPP/5YaWlpds4GAAAQkVq8jEFUVJQeeOABPfHEE2psbNTo0aOVnJzc6oF8Pl+rM8ghhxxyyCGHHHLaMqfFbyIHAAD4qWIlcgAAAEMUKAAAAEMUKAAAAEOt+i48tK9nn31WM2fO7OgxWq2hoUFbt26Vy+XS4MGD9dFHH+mbb76R1+uVz+dTdHTnvFuuX79eGRkZcrvdHT2KJGnXrl3yer3q2bOn6uvrVVhYqD179ujSSy/VHXfcoZ49e3b0iLb4+uuvtXv3biUnJ2vIkCFGl929e7ckacCAAdq/f79KSkrk8Xg0bNiwthj1J+vAgQM6fvy4rrzySsXGxgZPLykp0dChQztuMHQKhw8f1vbt23Xs2DFFRUWpX79+GjlyZIfvw3gTeYR68sknz/nZsix98cUX+sUvfiFJys3N7YixbLFy5UoFAgHV1dWpV69eqq2t1YgRI1RaWirLsmwpiR988IFGjx5tw7ThmzJlimJjY9W3b19lZmbq+uuvV3x8fLvO0FROTo6WL1+uqKgovfDCC4qJidF1112n0tJS7du3T7///e87bLbWmDdvnpYtWybp7DcdbNiwQRkZGfrss880fPjwsL/U/O2331ZJSYkCgYAGDx6sXbt26ZprrlFpaamGDBmiO+64o8Uznjx5UhdddFGLL9+VrF+/Xhs2bJDX69W+fft0//33Kz09XdLZ/dj/7utMVFZWKiEhwa5REYHWr1+vf//730pNTdWnn36qyy+/XL169dL27dv10EMP6Zprrumw2SL2T/0///nPmj9/fljb1tbW6r333tMnn3yiY8eOKTo6Wv369dNNN92kUaNGte2gbeT48ePyer0aM2aMHA6HLMvSnj17dNtttxlnlZWVae3atXK5XLrnnnv03HPPaffu3fJ4PJo2bZp+9rOftcFv0LzvvvtOTz/9tAKBgKZPn64XXnhBTqdTN954o+bMmWPLdaxbty7sAnX69GkVFhbq2LFjuvbaazVy5MjgeS+++KIeeuihsHL69u2rvLw8lZaW6uOPP9a6devUv39/ZWZmasSIEerRo0fY87z77rsqLi5WVVWVJCkhIUFpaWnKzs5Wr169wsqxLEtRUVGSpD179gSfqAYOHNjq27kjn7gCgUDw35s2bdLChQsVHx+v2267TQsWLAi7QG3btk3Lly/XmTNnNG3aND333HPq2bOnJkyYoPnz54ddoN58803ddtttio+PV1lZmQoKCuRwOBQIBDRz5kylpqaGlZObm6uMjAxlZmaqX79+YV3mQpoe1Tl9+rRee+01lZWVKTk5WVOmTFFiYmKLs1ti06ZNevLJJxUbG6sjR47omWee0dGjRzVu3LgLfqNFc6qrq8/52bIszZ8/P3i/jouLs3XurqAlRf7EiRN6++235XA49Jvf/Ebvv/++PvnkE3m9Xk2dOjXsBbPt2o9t2rRJy5cvl9Pp1Pjx47Vs2TItWbJEN910k5566ik99dRTRr/fhZj0jaY6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\n",
      "text/plain": [
       "<Figure size 720x360 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "data['DAY'].value_counts().plot(kind=\"bar\",color=\"green\",figsize=(10,5))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "635c19e4",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "58bc4259",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 84,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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3nuvbrjhBklfTItYu3atnn76aZsrC31/+9vfVFhYqK1bt0qSIiMjba7IWf5+/Uifz6ePP/5Yp06dsq+gIBGsvuTv1676uruVo2vjx4/XCy+8oDNnzqi0tFSbNm3SlClT7C7LMR566KGL/ttjDbXu+aZ86rXL2bNnA6FKkkaMGKGzZ8/aWJFzREREqL29PXD8fv75545fk+lKOr9+pN/vV3h4uFJSUjR79my7y7pszLH6kjvuuEPR0dHy+/1qb28PzHE5P3l9/fr1NlfoDHv37tWePXvk9/s1evRojRw50u6SHKOpqSnwdUdHh7Zv367m5mbdcccdNlblHBf71Ltu3To9//zzNlblHEuXLtV1110XWHtpy5YtOnToEJOwu2Hv3r164403VFtbq1GjRqm6ulpz5szRiBEj7C7NEdrb278yytfR0eG4W6IRrAAHWLRoEZP/u+nvR/zCw8OVnJysadOm6frrr7e5Mmdobm7W73//e1VXV8vv92vYsGH63ve+x5pM3dTU1KQDBw7I7/dr8ODBio+Pt7skx5g/f76effbZS24LdYxRwrh777038B/b+Uu2o6OjGe3rpr+/Msbv9+vQoUPMU+uGgwcPyuPxaPXq1ZKk8vJy7dixQ8nJybr22mttrs454uLiuALVgo6ODsXGxurcuXOqra2VJA0fPtzmqkLbqVOn5PV61d7ersOHDwfmOre2tjryNDTBCsa9/PLLFzzeuXOnDh48aFM1zvPKK68Evg4LC1NycrIKCwttrMgZXnzxxcDCqvv27dOrr76qWbNm6ZNPPtHatWv1yCOP2FxhaLvUqMD5q3zRtV//+tfavn27rr322sCHS5fLRbC6hN27d6uiokInT5684P+P6Oho3XnnnTZWFhyCFYw5d+7cRa+++ta3vqU333zThoqciYnWwfH5fIHTVdu2bdOUKVOUnZ2t7OxsPfroozZXF/pqamrk8Xg0ceJE7jgRpMrKSq1YscJxc4Lslpubq9zcXL333nvKzs62uxzLCFYwZuHChXr22We1Y8eOwLbzp7LQfR0dHdqxY4dOnDghn88X2D5t2jQbqwp9Pp8vEO4//PBD/fCHP7zgOXy9F198UXv37tW7776rd999V2PGjNHEiRNZv+oyXH311Tp37hzBKkjZ2dmqqqrS0aNH1dHREdjutN99BCsYt2vXrsDX5ycPcxqh+5YsWaKYmBhlZGTwC/oyTJw4UU888YT69u2ryMhIDRs2TNIXl7xze6BLCwsL0+jRozV69Gh1dHRo69ateuKJJzRt2jTdeuutdpfnCJGRkXr00UeVmZl5wTILzFnrnhdeeEHt7e366KOPlJeXp/fee8+Ro6cEKxhz+vRpvfXWW1/5hOtyubR582Zu4tpNXq9Xjz32mN1lOM7UqVN1ww036NSpUxo5cmRgjovP59OsWbNsrs4ZOjo6VFVVpa1bt6qurk633nqrxo0bZ3dZjpGVlaWsrCy7y3CsmpqawB1Pvve97+m2225z5P15CVYwxufzqa2tTazgYc2QIUN05MgRpaen212K4wwZMuQr21JTU22oxHlWrVqlo0eP6sYbb9S0adP49xcE7ppgzfk1rKKiouT1ehUXF+fIO6AQrGCM2+123LnwUPLII4/I5XLp3LlzKi8vV0pKivr06RNYnNaJn9zgHFu2bFFUVJSOHz+ut99+O7CdxZEv7fyx2xWO3e4ZM2aMzpw5o9tvv10LFiyQJOXl5dlc1eUjWMEYRqqs8Xq9WrJkid1loJd67bXX7C7Bsc6HgD/96U+SdMGq9efv3oGunV+D7vwH87a2NqWnpys1NdWRU0jC7C4A3xyLFy+2uwRHS0lJUXJycpd/AISm88dodXW1ZsyYofT0dKWnp+vuu+/Wnj177C4v5L344ouByf779u3Tb3/7W+Xn5ysmJkZr1661ubrLx4gVjOGWF9acn/zfFSd+cgN6k7a2Nu3fvz9w+6Tq6mrumtAN37Q16AhWQIhg8j/gbLNnz9bPfvYztbS0SJJiYmI0e/Zsm6sKfd+0NegIVkCIYPI/4GwZGRlaunTpBcEKl/ZNW4OOYAWECEaqAGc7deqUXn31VTU0NGjhwoWqra1VTU2NI69su5K+aWvQMXkdCBFM/gecbc2aNRo1apQaGhokSf3799cf//hHm6tyhiFDhuhb3/qWoqOjA9tSU1OVkZFhY1XBIVgBIYLJ/4CzNTU1acKECYERl/DwcIWF8d9sb8PfOAAABkRFRampqSkQrGpqahw5RwjWuPxM7AAAIGh//OMfNXToUEnS+vXrdfToUQ0YMECNjY0qLCzUwIED7S0QVxTBCgAAC15++WXV1NTos88+U1pamhITEzV8+HBNmDBB8fHxdpeHK4xgBQCAAZ2dnTp06JCqq6tVU1OjAwcOKCYmRsXFxXaXhiuI5RYAADCgvb1dra2tamlpUWtrq9xut9LT0+0uC1cYI1YAAFiwdu1a1dbWKjo6WoMHDw784Urf3omrAgEAsKC+vl4dHR3q16+fEhMTlZSUpNjYWLvLgk0YsQIAwCK/36+jR4+qpqZG1dXVOnr0qOLi4jRkyBBNnz7d7vJwBTHHCgAAi1wul9LT0xUbG6uYmBjFxMSoqqpKBw8eJFj1MoxYAQBgwcaNGwMjVeHh4Ro6dKiGDBmioUOHKj09ndXXexlGrAAAsKCurk7Z2dmaOXOm3G633eXAZoxYAQAAGML4JAAAgCEEKwAAAEMIVgAAAIYQrAAAAAwhWAEAABjy/4Fex2u6ize2AAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 720x360 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "data[\"WEEKDAY\"].value_counts().plot(kind=\"bar\",color=\"green\",figsize=(10,5))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a59e79d8",
   "metadata": {},
   "source": [
    "#### Month with the highest number of trips in a year"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "978ed0d5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 85,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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+Hy+ZI9ghFNySGSxK6dkcUoOiSx25ZQsTskhJT9LWvReJ0QBAAAgblx5HQAAwBCKFQAAgCEUKwAAAEMoVing0qVLam5uVm9v7x3Lm5qakjOQRefOnVNPT48kqb+/XwcPHpTf79d7770XW55KWlpa1NLSIkm6ePGiDh8+rFOnTiV5KjjRb37zm2SPYMw///lPHT58WH//+9+TPUpcjhw5ovb29mSPga8YGBhQQ0ODTp8+LUn6+OOPVVtbqz//+c8aGBhIykycvG5zR44c0QcffKCCggJduHBBK1eu1OzZsyVJ27Zt02uvvZbkCR9cRUWFXn/9dWVkZOjtt9/WqFGjNG/ePDU3N+vChQv6yU9+kuwRH9jvf/97NTU16fbt25o5c6bOnTunGTNmqLm5WUVFRSovL0/2iPgvR48e1aJFi5I9xgP56nM6Go3qzJkz+sY3viHpy+d9KnnppZe0e/duSV9+48YHH3ygOXPm6PTp0/r2t7+tsrKy5A74gH74wx9q9OjRGj9+vJ566inNnz9fWVlZyR7roVdTU6Pbt2+rr69PY8eOVW9vr+bOnavm5mZFo1Ft3Lhx2GdKyOUW7KCnp0eBQEAdHR365je/qe985zux+9555x09//zzSZzuwX344Yd67bXXNHr0aLW2tqqqqkptbW16+umn73mFezuLRqPKyMiQJJ0/fz72AvLkk09q69atyRwtbsePH9frr7+uW7duac2aNXrzzTc1ZswYffe739WOHTscU6x+/etfa8eOHckeY8gOHjyYMsUqHA6roKBAS5YsUVpamqLRqM6fP69ly5YlezRLbt++Hfv3hx9+qFdeeUVZWVlatmyZdu7cmTLFavz48fL7/WpublZjY6MOHjyoKVOm6KmnntLcuXP1yCOPJHvEB9bT06O6ujqFQiF1d3dLkrKzs1VcXKyysjKNHTs2yRM+uM8//1xvvPGGbt++rbVr1+rtt99Wenq6FixYkLTXFccWq3379mnixImaO3eujh49quPHj+uFF17QiBEj7vreQjuLRCIaPXq0JCkvL0+vvvqqKisr1dbWlnLFatKkSbEjB1/72tf073//W0888YQuX74slyu1dsWMjAylp6dr1KhRGj9+vMaMGSNJGjly5F1f32R358+fv+99n3322fANMkT3O+IZjUbV1dU1zNNYt3v3bh05ckSHDh3Ss88+q8mTJ2vkyJGaPn16skezJBqN6saNG4pGo4pGo7GjPKNHj479oZUK0tLSlJ6erqKiIhUVFWlgYEBNTU36+OOPdeDAAdXW1iZ7xAdWXV2tGTNm6NVXX9W4ceMkSdeuXdOxY8dUVVWlV155JbkDxiEajWpgYEC9vb3q6+tTT0+PMjMzdevWrTtK/XBKrVezOFy9ejX2i3bOnDk6dOiQfvGLX+inP/1pkieLz7hx4/TZZ59p8uTJkr78ZbR9+3a9+eab+vzzz5M7XJzWrl2r/fv369ChQ3r00Uf18ssvy+PxyOPx6Ec/+lGyx4uLy+VSX1+fRo0adcf3Xfb09Cg9PbVOXXzppZfu+6L9xRdfDPM01nV1dWnnzp13/bUdjUZT6oUiPT1dS5cu1fz58/Xuu+8qOzs7aS8QJvT09Gj79u2KRqNKS0vTtWvXNG7cOPX29qbUH4dfndXlcqm4uFjFxcXq7+9P0lTWtLa2aufOnXcsGzdunMrKynT06NEkTWXNokWLtHnzZkUiEX3ve99TVVWV8vLydO7cOZWUlCRlJscWq4GBAUUikdiLXHl5uXJycvSzn/3srpPA7Wzjxo13/VWXkZGhjRs3Jv3qsvEaM2aMNmzYoJs3b+rq1auKRCLKycmJ/cWUSn7+859rxIgRknRHkRoYGNCGDRuSNZYljz32mNasWaOJEyfedd+6deuSMJE13/rWt9Tb2xv7I+S/peLRHo/Ho4qKCp06dSql3mb6qr17995zeVpaWkqdArB58+b73jdy5MjhG8SA3Nxcvf/++yotLb3riJXX603ucHFaunRprEDl5OSotLRUzc3N8vl8mjp1alJmcuzJ6++9955mzpypmTNn3rG8qalJv/3tb1VTU5OkyQB7OX78uB5//HHl5+ffdd9f//pXzZkzJwlTAUiUGzduKBAI6MSJE7G3yceNGxf7MEFmZmaSJ0xtji1W/0sqfUIISCaeK8DDhef80KXWySCGHDx4MNkjACmB5wrwcOE5P3SOPcfKKZ8QAhKN5wrwcOE5n1iOLVZO+YQQkGg8V4CHC8/5xHJssXLaJ4SAROG5AjxceM4n1kN58joAAEAiPJQnrwMAACQCxQoAAMAQihUAAIAhFCsAAABDKFYAAACG/B+/nLTDlHCGOgAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 720x360 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "data[\"MONTH\"].value_counts().plot(kind=\"bar\", figsize=(10,5), color = \"blue\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4f11446d",
   "metadata": {},
   "source": [
    "#### location with the highest patronage"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "a4025e1b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 89,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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TZLD4TC8n/PPc3U5/7xYX+efM2fNmqUJEyaoTZs2hutsqPP/rlitVj3yyCPq1q3bFb3GJ598ol69eikiIsKMEluMZh+s3G635syZo7S0ND311FOSpAMHDujkyZOXDVZut1tut1tWa9MauAsICNCcOXN8su9bbrnlip8zYcKEiwLX5bhcLp/2/fzjZuLEiZKk48ePa9OmTY1Ww+nTp7VmzZoWH6x2796tzZs3a/bs2XI4HCopKVFlZaWvy2qQbt26aePGjbrjjjvkcrlUUlKiM2fOeO7Py8vT6NGjlZiYqJSUFEP7WLFihdeC1dKlS3XHHXcoNTVVkvTNN9945XXNdP55cOHChfroo480fPhwORwOTZs2TWFhYZo/f742btyom266ydRajJwXz/erX/3KS5UYd34/t2zZorfeeksvvvhivZ/vcrn0ySefKC4urtZg5etzelPS7IPV9u3bZbfbLzjw4+PjVVZWppdeesnzCe3+++9Xamqq8vPzNWvWLPXs2VO7d+9WamqqTp8+rdGjR0uSsrKy9O233+qhhx7y0Tuq25YtW7Rs2TKFhISoU6dOnu0lJSV6+eWXVVpaqi5dumjLli3KyMhQaGio1q9frw8//FCVlZVKTEzUo48+6jn43377beXm5iogIEBTp05V27Zt9c477ygwMFB33XWX4TpfffVV7du3T+Xl5erbt69GjBghqXokYvDgwfryyy9122236a233tKAAQO0fft2VVVVaezYsXr77bd17Ngx/ehHP9Itt9yi4uJizZ8/X2fOnJHL5dKjjz6qHj16NKyRkrZt23bRcRMVFaX//u//Vn5+vhYuXKhz585JUq2f7KZNm6bHH39ccXFxkqo/nf7sZz9TbGys/vSnP+nQoUOqqqrSfffdp9TUVB06dEiLFy9WZWWl3G63pkyZov/93//VsWPHNHXqVPXq1UujRo3SX/7yF23ZskVS9ehf//79tX37dv3tb39TSEiIDh06pM6dO+vJJ5+UxWJpcB8aQ3FxsUJCQjyjCjUjUVu3btUbb7yhqqoqdenSRT//+c89j1m9erU2b96syspKTZ48We3bt1dpaakWL16s/Px8tWrVSmPHjlXHjh198p66deum119/XZJ0+PBhxcXF6cSJEyotLVWrVq307bffqlOnTvrkk0+0b98+jRkzRosWLVLr1q319ddf68SJ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\n",
      "text/plain": [
       "<Figure size 720x360 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "data[\"START*\"].value_counts().plot(kind=\"line\",figsize=(10,5),color=\"purple\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "51f68eb7",
   "metadata": {},
   "source": [
    "### Conclusion\n",
    "Insight derived from the Analysis above showed that\n",
    "1. Riders prefer using uber for Business purposes than using it for Personal use\n",
    "2. Riders prefer patronising for short distances (1 to 50Miles) as compared to distances further than the 50mile range.\n",
    "3. High patronage of uber rides awere identified in the afternoon and in late afternoon between the hours of 13:00 and 20:00 while low patronage was identified midnights to dawn between the hours of 1:00 and 6:00.\n",
    "4. Majority of riders use uber for their meetings followed by those who use uber Enternainment purposes while very few riders use uber rides for charity for commuting purposes.\n",
    "5. uber rides are patronised largely on fridays than any other days of the week\n",
    "6. December had the highest patronage per ride as compared to other months of the year.\n",
    "7. Most trips were started in cary"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "46a82242",
   "metadata": {},
   "source": [
    "### Recommendation \n",
    "1. Advertisement about uber rides for Personal purposes must be emphasized.\n",
    "2. Short distance rides must be available for easy accessibilty for it has high potential of patronage in the future.\n",
    "3. promotions and discouts should be rewarded to riders who patronises the midnight and dawn rides to increase patronage at that time of the day.\n",
    "4. Enough vehicles must be available awaiting higher patronage on fridays\n",
    "5. Promotions and discouts should the rewarded to riders who patronises uber in other months of the year apart from the december festive season and the new year \n",
    "6. Advertidements should be done in other catchment areas as well"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
