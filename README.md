# Logs_Analysis
# Description
  - This project involves creating a reporting tool that prints out reports (in plain text) 
    based on the data in the database. 
  - This reporting tool is a Python program using the psycopg2 module to connect to the database.
# Software Requirements
  - Python 3 and PostgreSQL 9.3 are required to run this project.
  - Vagrant and VirtualBox should be installed on your system.
# Setting up the virtual machine and loading the data
  - Download FSND-Virtual-Machine.zip This will give you a directory called FSND-Virtual-Machine. 
  - Alternately, you can use Github to fork and clone the repository https://github.com/udacity/fullstack-nanodegree-vm.
  - Change to the FSND-Virtual-Machine directory in your terminal with cd.
  - Inside, you will find another directory called vagrant.
  - Change directory to the vagrant directory
  - Launch your VM using the command vagrant up
  - Login to your VM using the command vagrant ssh
  - Download the file newsdata.zip
  - Navigate to the shared vagrant directory after logging in
  - To load the data, use the command psql -d news -f newsdata.sql
  - Once you have the data loaded into your database, connect to your database using psql -d news
# Tables in the Database
  - The authors table includes information about the authors of articles.
  - The articles table includes the articles themselves.
  - The log table includes one entry for each time a user has accessed the site.
# Running the project
  - To answer questions 1 and 2 create the following view
      - create view info_view as select title,author,count(*) as visit_count from articles,log 
    where log.path like concat('%',articles.slug) group by articles.title,articles.author 
    order by visit_count desc;
  - Clone this repository and place the code file inside vagrant directory that is shared to the VM.
  - Make sure you are in the right directory.
  - To view the results run the command python3 logs_analysis.py
  
  
