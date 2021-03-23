# SP_data_pipeline_mini-project
![Design Blocks](https://images.unsplash.com/photo-1565086101813-41318972d895?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1934&q=80)
Image by: Rachel C, Unsplash

## Table of contents
* [Project Context](#project-context)
* [Project Deliverables](#project-deliverables)
* [Technologies](#technologies)
* [Setup](#setup)


### Project Context
In this project, you are provided with a ticket system database with ticket sales event table. This table tracks all ticket sales for various events, including when
a third-party reseller submits their records of ticket sales for a new day. The records are submitted as a CSV file.

With this-mini project, you’ll practice Python and SQL skills by creating a basic data pipeline. You’ll learn how to use the Python database connector to perform data loading and query
databases programmatically.

__Your task is to:__

- Write the table definition DDL and use it to create the sales table.
- Read the CSV file and load the new sales records into the ticket sales table.


### Project Deliverables:
- Push the Python code to your GitHub repo.
- Add a readme file to include steps to run your code and verify the result.
- Attach the command line execution log for the successful job run. You can capture it in a text file.

### Technologies
Project is created with:
* JupyterLab version: 3.0.7
* Python version: 3.8.5
* conda version: 4.9.2
* conda-build version: 3.21.4


### Setup
To run this project, install it locally using npm:

```
* import package
* import mysql.connector
* import csv
* import pandas as pd
* from pandas import DataFrame
* from mysql.connector import errorcode
```
_____