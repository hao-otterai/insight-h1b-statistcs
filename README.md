# Problem

A newspaper editor was researching immigration data trends on H1B(H-1B, H-1B1, E-3) visa application processing over the past years, trying to identify the occupations and states with the most number of approved H1B visas. She has found statistics available from the US Department of Labor and its [Office of Foreign Labor Certification Performance Data](https://www.foreignlaborcert.doleta.gov/performancedata.cfm#dis). But while there are ready-made reports for [2018](https://www.foreignlaborcert.doleta.gov/pdf/PerformanceData/2018/H-1B_Selected_Statistics_FY2018_Q4.pdf) and [2017](https://www.foreignlaborcert.doleta.gov/pdf/PerformanceData/2017/H-1B_Selected_Statistics_FY2017.pdf), the site doesn’t have them for past years.  

In this repository, I created a mechanism to analyze past years data, specificially calculate two metrics: **Top 10 Occupations** and **Top 10 States** for **certified** visa applications. The code works for year 2008-2018, and in principle should be readily applied to data of 2019 and future years.  

# Input Dataset

- This repo uses ";" delimited CSV as input data format.

- Raw data could be found [here](https://www.foreignlaborcert.doleta.gov/performancedata.cfm) under the __Disclosure Data__ tab (i.e., files listed in the __Disclosure File__ column with ".xlsx" extension). Convert the data to the ";" delimited CSV in order for this repo to work.

- **Note - File Structure:** Each year of data can have different columns. check the **File Structure** as described in the link above. If 2019 and future data are to be used as input, please check whether the input data structure have consistent column names as previous years. In particular, pay attention to the column names of occupation code, occupation name, states, case status, etc.  

# Instructions

we provide an example script to analyze the 2016 year data. Check the `run.sh` for details. 
Run the `run.sh` script should produce the results in the `output` folder without needing to change the code. In the run.sh script, the python script python ./src/h1b_counting.py takes 3 arguments for input and output files:  directory of the input csv file, directory of the output file for top occupations, and the directory of the out file for top states.  Feel free to change the 3 arguments to analyze new input data. 


# Output 

This program creates 2 output files:
* `top_10_occupations.txt`: Top 10 occupations for certified visa applications
* `top_10_states.txt`: Top 10 states for certified visa applications

Each line holds one record and each field on each line is separated by a semicolon (;).

Each line of the `top_10_occupations.txt` file contains these fields in this order:
1. __`TOP_OCCUPATIONS`__: Use the occupation name associated with an application's Standard Occupational Classification (SOC) code
2. __`NUMBER_CERTIFIED_APPLICATIONS`__: Number of applications that have been certified for that occupation. An application is considered certified if it has a case status of `Certified`
3. __`PERCENTAGE`__: % of applications that have been certified for that occupation compared to total number of certified applications regardless of occupation. 

The records in the file are sorted by __`NUMBER_CERTIFIED_APPLICATIONS`__, and in case of a tie, alphabetically by __`TOP_OCCUPATIONS`__.

Each line of the `top_10_states.txt` file contains these fields in this order:
1. __`TOP_STATES`__: State where the work will take place
2. __`NUMBER_CERTIFIED_APPLICATIONS`__: Number of applications that have been certified for work in that state. An application is considered certified if it has a case status of `Certified`
3. __`PERCENTAGE`__: % of applications that have been certified in that state compared to total number of certified applications regardless of state.

The records in this file are sorted by __`NUMBER_CERTIFIED_APPLICATIONS`__ field, and in case of a tie, alphabetically by __`TOP_STATES`__. 

Depending on the input (e.g., see the example below), there may be fewer than 10 lines in each file. There, however, should not be more than 10 lines in each file. In case of ties, only list the top 10 based on the sorting instructions given above.

Percentages also should be rounded off to 1 decimal place. For instance, 1.05% should be rounded to 1.1% and 1.04% should be rounded to 1.0%. Also, 1% should be represented by 1.0%

## Example
If you are given the input file, `./input/h1b_input.csv` with the following data:
```
;CASE_NUMBER;CASE_STATUS;CASE_SUBMITTED;DECISION_DATE;VISA_CLASS;EMPLOYMENT_START_DATE;EMPLOYMENT_END_DATE;EMPLOYER_NAME;EMPLOYER_BUSINESS_DBA;EMPLOYER_ADDRESS;EMPLOYER_CITY;EMPLOYER_STATE;EMPLOYER_POSTAL_CODE;EMPLOYER_COUNTRY;EMPLOYER_PROVINCE;EMPLOYER_PHONE;EMPLOYER_PHONE_EXT;AGENT_REPRESENTING_EMPLOYER;AGENT_ATTORNEY_NAME;AGENT_ATTORNEY_CITY;AGENT_ATTORNEY_STATE;JOB_TITLE;SOC_CODE;SOC_NAME;NAICS_CODE;TOTAL_WORKERS;NEW_EMPLOYMENT;CONTINUED_EMPLOYMENT;CHANGE_PREVIOUS_EMPLOYMENT;NEW_CONCURRENT_EMP;CHANGE_EMPLOYER;AMENDED_PETITION;FULL_TIME_POSITION;PREVAILING_WAGE;PW_UNIT_OF_PAY;PW_WAGE_LEVEL;PW_SOURCE;PW_SOURCE_YEAR;PW_SOURCE_OTHER;WAGE_RATE_OF_PAY_FROM;WAGE_RATE_OF_PAY_TO;WAGE_UNIT_OF_PAY;H1B_DEPENDENT;WILLFUL_VIOLATOR;SUPPORT_H1B;LABOR_CON_AGREE;PUBLIC_DISCLOSURE_LOCATION;WORKSITE_CITY;WORKSITE_COUNTY;WORKSITE_STATE;WORKSITE_POSTAL_CODE;ORIGINAL_CERT_DATE
0;I-200-18026-338377;CERTIFIED;2018-01-29;2018-02-02;H-1B;2018-07-28;2021-07-27;MICROSOFT CORPORATION;;1 MICROSOFT WAY;REDMOND;WA;98052;UNITED STATES OF AMERICA;;4258828080;;N;",";;;SOFTWARE ENGINEER;15-1132;"SOFTWARE DEVELOPERS, APPLICATIONS";51121.0;1;0;1;0;0;0;0;Y;112549.0;Year;Level II;OES;2017.0;OFLC ONLINE DATA CENTER;143915.0;0.0;Year;N;N;;;;REDMOND;KING;WA;98052;
1;I-200-17296-353451;CERTIFIED;2017-10-23;2017-10-27;H-1B;2017-11-06;2020-11-06;ERNST & YOUNG U.S. LLP;;200 PLAZA DRIVE;SECAUCUS;NJ;07094;UNITED STATES OF AMERICA;;2018723003;;Y;"BRADSHAW, MELANIE";TORONTO;;TAX SENIOR;13-2011;ACCOUNTANTS AND AUDITORS;541211.0;1;0;0;0;0;1;0;Y;79976.0;Year;Level II;OES;2017.0;OFLC ONLINE DATA CENTER;100000.0;0.0;Year;N;N;;;;SANTA CLARA;SAN JOSE;CA;95110;
2;I-200-18242-524477;CERTIFIED;2018-08-30;2018-09-06;H-1B;2018-09-10;2021-09-09;LOGIXHUB LLC;;320 DECKER DRIVE;IRVING;TX;75062;UNITED STATES OF AMERICA;;2145419305;;N;",";;;DATABASE ADMINISTRATOR;15-1141;DATABASE ADMINISTRATORS;541511.0;1;0;0;0;0;1;0;Y;77792.0;Year;Level II;OES;2018.0;OFLC ONLINE DATA CENTER;78240.0;0.0;Year;N;N;;;;IRVING;DALLAS;TX;75062;
3;I-200-18070-575236;CERTIFIED;;2018-03-30;H-1B;2018-09-10;2021-09-09;"HEXAWARE TECHNOLOGIES, INC.";;101 WOOD AVENUE SOUTH;ISELIN;NJ;08830;UNITED STATES OF AMERICA;;6094096950;;Y;"DUTOT, CHRISTOPHER";TROY;MI;SOFTWARE ENGINEER;15-1132;"SOFTWARE DEVELOPERS, APPLICATIONS";541511.0;5;5;0;0;0;0;0;Y;84406.0;Year;Level II;OES;2017.0;OFLC ONLINE DATA CENTER;84406.0;85000.0;Year;Y;N;Y;;;NEW CASTLE;NEW CASTLE;DE;19720;
4;I-200-18243-850522;CERTIFIED;2018-08-31;2018-09-07;H-1B;2018-09-07;2021-09-06;"ECLOUD LABS,INC.";;120 S WOOD AVENUE;ISELIN;NJ;08830;UNITED STATES OF AMERICA;;7327501323;;Y;"ALLEN, THOMAS";EDISON;NJ;MICROSOFT DYNAMICS CRM APPLICATION DEVELOPER;15-1132;"SOFTWARE DEVELOPERS, APPLICATIONS";541511.0;1;0;0;0;0;0;1;Y;87714.0;Year;Level III;OES;2018.0;OFLC ONLINE DATA CENTER;95000.0;0.0;Year;Y;N;Y;Y;;BIRMINGHAM;SHELBY;AL;35244;
5;I-200-18142-939501;CERTIFIED;2018-05-22;2018-05-29;H-1B;2018-05-29;2021-05-28;OBERON IT;;1404 W WALNUT HILL LN;IRVING;TX;75038;UNITED STATES OF AMERICA;;8666609190;;Y;"GARRITSON, JAMES";RICHARDSON;TX;SENIOR SYSTEM ARCHITECT;15-1132;"SOFTWARE DEVELOPERS, APPLICATIONS";541511.0;1;0;0;0;0;0;1;Y;71864.0;Year;Level II;Other;2017.0;OFLC ONLINE DATA CENTER;74000.0;0.0;Year;Y;N;Y;;;SUNRISE;BROWARD;FL;33323;
6;I-200-18121-552858;CERTIFIED;2018-05-01;2018-05-07;H-1B;2018-05-02;2018-10-26;ICONSOFT INC.;;101 CAMBRIDGE STREET SUITE 360;BURLINGTON;MA;01803;UNITED STATES OF AMERICA;;8882054614;1;N;",";;;SENIOR ORACLE ADF DEVELOPER;15-1132;"SOFTWARE DEVELOPERS, APPLICATIONS";541511.0;1;0;1;0;0;0;0;Y;92331.0;Year;Level III;Other;2017.0;OFLC ONLINE DATA CENTER;114000.0;0.0;Year;Y;N;Y;;;JACKSONVILLE;DUVAL COUNTY;FL;32202;
7;I-200-18215-849606;CERTIFIED;2018-08-03;2018-08-09;H-1B;2018-08-11;2021-08-11;COGNIZANT TECHNOLOGY SOLUTIONS US CORP;;211 QUALITY CIRCLE;COLLEGE STATION;TX;77845;UNITED STATES OF AMERICA;;2019661249;;N;",";;;SENIOR SYSTEMS ANALYST JC60;15-1121;COMPUTER SYSTEMS ANALYST;541512.0;1;0;1;0;0;0;0;Y;80579.0;Year;Level II;OES;2018.0;OFLC ONLINE DATA CENTER;80579.0;0.0;Year;Y;N;Y;;;OWINGS MILLS;BALTIMORE;MD;21117;
8;I-201-17339-472823;CERTIFIED;2017-12-08;2017-12-14;H-1B1 Chile;2017-12-08;2019-06-07;ISHI SYSTEMS INC;;185 HUDSON STREET;JERSEY CITY;NJ;07311;UNITED STATES OF AMERICA;;2013326900;;N;",";;;ASSOCIATE PRODUCT MANAGER(15-1199.09);15-1199;"COMPUTER OCCUPATIONS, ALL OTHER";541511.0;1;0;1;0;0;0;0;Y;88317.0;Year;Level III;OES;2017.0;OFLC ONLINE DATA CENTER;90000.0;0.0;Year;;;;;;JERSEY CITY;HUDSON;NJ;07311;
9;I-200-18233-239931;CERTIFIED;2018-08-21;2018-08-27;H-1B;2018-09-05;2021-09-04;"WB SOLUTIONS, LLC";;7320 E FLETCHER AVE;TAMPA;FL;33637;UNITED STATES OF AMERICA;;8133300099;;Y;"KIDAMBI, VAMAN";TRUMBULL;CT;SENIOR JAVA DEVELOPER;15-1132;"SOFTWARE DEVELOPERS, APPLICATIONS";541511.0;1;0;0;0;0;1;0;Y;104790.0;Year;Level III;OES;2018.0;OFLC ONLINE DATA CENTER;105000.0;0.0;Year;Y;N;Y;Y;;ALPHARETTA;FULTON;GA;30005;
```

then the output files would be:

`./output/top_10_occupations.txt`:
```
TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE
SOFTWARE DEVELOPERS, APPLICATIONS;6;60.0%
ACCOUNTANTS AND AUDITORS;1;10.0%
COMPUTER OCCUPATIONS, ALL OTHER;1;10.0% 
COMPUTER SYSTEMS ANALYST;1;10.0%
DATABASE ADMINISTRATORS;1;10.0%
```
`./output/top_10_states.txt`:
```
TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE
FL;2;20.0%
AL;1;10.0%
CA;1;10.0%
DE;1;10.0%
GA;1;10.0%
MD;1;10.0%
NJ;1;10.0%
TX;1;10.0%
WA;1;10.0%
``` 


## Repo directory structure

The directory structure for your repo should look like this:
```
      ├── README.md 
      ├── run.sh
      ├── src
      │   └──h1b_counting.py
      ├── input
      │   └──h1b_input.csv
      ├── output
      |   └── top_10_occupations.txt
      |   └── top_10_states.txt
      ├── insight_testsuite
          └── run_tests.sh
          └── tests
              └── test_1
              |   ├── input
              |   │   └── h1b_input.csv
              |   |__ output
              |   |   └── top_10_occupations.txt
              |   |   └── top_10_states.txt
              ├── your-own-test_1
                  ├── input
                  │   └── h1b_input.csv
                  |── output
                  |   |   └── top_10_occupations.txt
                  |   |   └── top_10_states.txt
```
