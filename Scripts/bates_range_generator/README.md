Purpose: This script is used to generate bates range breakdown by feeding in a list of begbates and endbates

Usage: generate a file contains begbates,endbates in ascending order from any platform (Relativity, Concordance, Summation and etc; use this script to parse the file, and the outputs will be the bates range breakdown

Example: 

you export a txt file containing begbates and endbates in ascending order from one of your Relativity workspaces like below

ABC001,ABC004 
ABC005,ABC007 
ABC009,ABC011 
ABC012,ABC015
ABCD0001,ABCD0002 
ABCD0003,ABCD0005 

After using the script to parse the content of the txt file, it will create a new output txt file, and its content is like below

ABC001,ABC007
ABC009,ABC015 
ABCD0001,ABCD0005 

So This bates range report is very useful for managing a case, especially the case is large and containing many different prefixes, also gaps.
