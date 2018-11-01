#!/bin/bash
#

#data download links for 2017 - 2008
#wget -O ./input/H1B_FY_2017.xlsx https://www.foreignlaborcert.doleta.gov/pdf/PerformanceData/2017/H-1B_Disclosure_Data_FY17.xlsx
#wget -O ./input/H1B_FY_2016.xlsx https://www.foreignlaborcert.doleta.gov/docs/Performance_Data/Disclosure/FY15-FY16/H-1B_Disclosure_Data_FY16.xlsx
#wget -O ./input/H1B_FY_2015.xlsx https://www.foreignlaborcert.doleta.gov/docs/py2015q4/H-1B_Disclosure_Data_FY15_Q4.xlsx
#wget -O ./input/H1B_FY_2014.xlsx https://www.foreignlaborcert.doleta.gov/docs/py2014q4/H-1B_FY14_Q4.xlsx
#wget -O ./input/H1B_FY_2013.xlsx https://www.foreignlaborcert.doleta.gov/docs/lca/LCA_FY2013.xlsx
#wget -O ./input/H1B_FY_2012.xlsx https://www.foreignlaborcert.doleta.gov/docs/py2012_q4/LCA_FY2012_Q4.xlsx
#wget -O ./input/H1B_FY_2011.xlsx https://www.foreignlaborcert.doleta.gov/docs/lca/H-1B_iCert_LCA_FY2011_Q4.xlsx
#wget -O ./input/H1B_FY_2010.xlsx https://www.foreignlaborcert.doleta.gov/docs/lca/H-1B_FY2010.xlsx
#wget -O ./input/H1B_FY_2009.xlsx https://www.foreignlaborcert.doleta.gov/docs/lca/Icert_%20LCA_%20FY2009.xlsx
#wget -O ./input/H1B_FY_2008.xlsx https://www.foreignlaborcert.doleta.gov/docs/lca/H-1B_Case_Data_FY2008.xlsx


# Use this shell script to compile (if necessary) your code and then execute it. 
# Below is an example of what might be found in this file if your program was written in Python
python ./src/h1b_counting.py ./input/h1b_input.csv ./output/top_10_occupations.txt ./output/top_10_states.txt




