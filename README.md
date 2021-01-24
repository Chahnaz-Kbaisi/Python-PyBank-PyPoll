# Python - Py Me Up, Charlie

This is a two-part python analysis, in [Part-I](https://github.com/Chahnaz-Kbaisi/Python-PyBank-PyPoll/tree/master/PyBank) python script was developed for analyzing the financial records of the company. And, in [Part-II](https://github.com/Chahnaz-Kbaisi/Python-PyBank-PyPoll/tree/master/PyPoll) a python script was developed to help a small, rural town modernize its vote counting process.

## Part-I: [PyBank](https://github.com/Chahnaz-Kbaisi/Python-PyBank-PyPoll/tree/master/PyBank)

* A Python script was created for analyzing the financial records of a company. To tackle this task, a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv) is provided. The dataset is composed of two columns: `Date` and `Profit/Losses`. 

* I created a Python script that analyzed the records and calculated each of the following:

  * The total number of months included in the dataset

  * The net total amount of "Profit/Losses" over the entire period

  * The average of the changes in "Profit/Losses" over the entire period

  * The greatest increase in profits (date and amount) over the entire period

  * The greatest decrease in losses (date and amount) over the entire period

* Below is the [output](https://github.com/Chahnaz-Kbaisi/Python-PyBank-PyPoll/blob/master/PyBank/Analysis/output.csv) analysis:

  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
  ```

## Part-II: [PyPoll](https://github.com/Chahnaz-Kbaisi/Python-PyBank-PyPoll/tree/master/PyPoll)

* A python script was developed to help a small, rural town modernize its vote counting process.

* A set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv) was provided. The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. A Python script was created to analyze the votes and calculate each of the following:

  * The total number of votes cast

  * A complete list of candidates who received votes

  * The percentage of votes each candidate won

  * The total number of votes each candidate won

  * The winner of the election based on popular vote.

* Below is the [output analysis](https://github.com/Chahnaz-Kbaisi/Python-PyBank-PyPoll/blob/master/PyPoll/Analysis/Output_election.csv):

  ```text
  Election Results
  -------------------------
  Total Votes: 3521001
  -------------------------
  Khan: 63.000% (2218231)
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -------------------------
  Winner: Khan
  -------------------------
  ```

