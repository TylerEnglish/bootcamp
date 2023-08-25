
# What is Pandas?

Pandas is a Python library used for working with data sets (think of Excel spreadsheets). It has functions for analyzing, cleaning, exploring, and manipulating data.

## Loading in Pandas to your Python Notebook

To use the Pandas library, you first need to import it. You can import Pandas using the following code:

```python
import pandas as pd
```

We can load in a CSV file using the `read_csv()` function. The `read_csv()` function returns a DataFrame object.

```python
df = pd.read_csv('https://github.com/ajaverett/data/blob/main/YoungAdults.csv')
```


## Basic Pandas Concepts

 - **DataFrames**
   - A Pandas DataFrame is a 2-dimensional data structure, like a 2-dimensional array, or a table with rows and columns.
   - The `df` variable is now a Pandas DataFrame. 
 - **Series**
   - A Pandas Series is like a column in a table. It is a one-dimensional array holding data of any type.
   - Each column in a DataFrame is a Series. We can access any of these like so: `df['column_name']`. For example, `df['Age']` returns a Series object containing the ages of the young adults in our dataset.


## Exploring the Data

**Below are functions over the DataFrame**

 - We can use the `head()` function to view the first 5 rows of the DataFrame. This is useful for getting a quick overview of the data.

```python
df.head()
```

 - We can use the `columns` attribute to view the column names of the DataFrame.

```python
df.columns
```

 - We can use the `info()` function to view the data types of each column and the number of non-null values.

```python
df.info()
```


# Data Manipulation

## The workflow

**Goal**: Seeing what a function does to our DataFrame
**Process**: `df.something()`

<br>

**Goal**: Updating our DataFrame with the result of a function
**Process**: `df = df.something()`

<br>

**Goal**: Seeing what a function does to a column in our DataFrame
**Process**: `df['column_name'].something()`

<br>

**Goal**: Updating a column in our DataFrame with the result of a function
**Process**: `df['column_name'] = df['column_name'].something()`


## Keeping only the columns we want 

We can select a column in a DataFrame using the following syntax:

```python
df.filter(['column_name'])
```

We can select multiple columns in a DataFrame using the following syntax:

```python
df.filter(['column_name1', 'column_name2', 'column_name3'])
```

## Keeping only the rows we want using a condition (query)

We can query rows in a DataFrame using a condition using the following syntax:

```python
df.query("column_name == value")
df.query("column_name > value")
df.query("column_name <= value")
df.query("column_name != value")

# note: if the value is a string, it must be in quotes
df.query("state == 'Texas'")
```

## Sorting the rows in our DataFrame

We can sort the rows in a DataFrame using the following syntax:

```python
df.sort_values(by='column_name')
df.sort_values(by='column_name', ascending=False)
```