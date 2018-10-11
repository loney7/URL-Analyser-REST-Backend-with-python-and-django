# Hi ! Welcome to the Url analyser application 

##  Index 

  <ul>
  
  <li>1. Problem Statement</li>
  
  <li>2. Steps towards building the solution</li>
  
  <li>3. Assumptions/ Decisions</li>
  
  <li>4. Problems/Challenges Faced</li>
  
  <li>5. Requirements/ Machine Setup</li>
  
  </ul>
  
  <br>
  <br>
  
  
  
  
  
  
  

![Screenshot](Screen%20Shot%202018-10-11%20at%2012.46.25%20AM.png)
![alt text](https://github.com/loney7/demo/blob/master/Screen%20Shot%202018-10-11%20at%2012.51.57%20AM.png)
<br>
<br>
<br>
## 1. Problem Statement 
  
  
### Functional Requirements

* The backend should receive the URL of the webpage being analyzed as a parameter. 


* After processing the results should be returned to the user. The result comprises the following information:

  ** What HTML version has the document?

  ** What is the page title?

  ** How many headings of what level are in the document?

  ** How many internal and external links are in the document? Are there any inaccessible links and how many?

** Did the page contain a login-form?

In case the URL given by the user is not reachable an error message should be sent as a response. The message should contain the HTTP status-code and some useful error description.

### Non-Functional Requirements:


The backend should cache the scraping results for each URL for 24 hours such that your backend does not have to redo the scraping for any given URL within the next 24 hours.
<br>
<br>
<br>


## 2. Steps towards building the solution


### Baby Steps

I had no prior experience of working with Django, so my first step was 
to quickly skim through some video tutorials on Django. This was followed by
going through the Django documentation thouroughly and implementing the steps.


### Problem Analysis

The problem basically asks us:

- Take input from the user
- If the url is present in the cache :
      *return the results by directing the user to a new page.
-else 
      *Hit the url and do the required analysis.
      
-  Redirect the user to the results page.


#### Step 1 :

Setup the machine to support django and python 3. Turns out, I got stuck in trivial issues with machine setup and it ended up consuming some time.


#### Step 2 : 

Creating  a model to store values in our database. This was followed by creating a super user and running migration scripts. This was followed by creating a form to get user input. This was fairly easy. I found it easy to navigate through the documentation and get the desired result.


#### Step 3 :

Creating the result view.



## Challenges/ Problems Faced/ Decisions


### 1.Technical Stack
I had primarily worked on Java before. This was the first time, I was working with django and python3.
As a result, it took me some extra time to grasp the fundamentals and get going.

### 2. Setting up cache for soup objects

If you have nested tags with a depth of about 480 levels, and you want to convert this tag to string/unicode, you get the RuntimeError maximum recursion depth reached. Every level needs two nested method calls and soon you hit the default of 1000 nested python calls. 

As a result, it is not possibe to cache soup objects directly.

I was using a field

soup.title.string : to display the Title of a web page.

I somehow ended up assuming that this field must be a string. However soup.title.string does not return a python string. As a result for some pages, my cache wasn't working.

#### Approach 1
After investing some time on the above issue, I figured out that the problem is due to the usage of soup objects. I thought of converting the result object to a string. This was definitely a hack around the problem i was facing. However, for serializing and deserializing, I ended up adding a lot of unnecessary code. Seeing my code get messy , I decided to drop this approach and further investigate the problem.

#### Approach 2
On further investigation, I found out that the problem was with soup.title.string field. I also realized the importance of setting up an IDE and the debugger. Had I used a debugger earlier, I would have solved this issue very quickly. 
I finally found a way to get the title string by using soup.title.text. After making this change the code started working perfectly.

### 3. Choice of Library for analysis of web pages

I had to choose between two libraries beautiful soup and scrapy
Factors I considered :

* Learning Curve
BeautifulSoup is very easy to learn, you can quickly use it to extract the data you want, in most cases, you will also need a downloader to help you get the HTML source. Since Scrapy does no only deal with content extraction but also many other tasks such as downloading HTML, learning curve of Scrapy is much steeper.

* Extensibility
So if the project is small, beautiful soup is preferred. If your project needs more customization such as proxy, data pipeline, then Scrapy becomes an obvious choice.

As a result I decided to use Beautiful Soup for analysing web pages.

### 4. Opening https sites

During testing I realized that my code did not work for https connections. 
This was due to SSL certificate errors. I ended up adding some code to ignore to ignore SSL certificate errors and the system started working fine.

### 5. Detecting login forms

Any kind of login form would defin






 








To run the web application, your system must fulfill the following requirements:

* Django - 2.1.2
* urllib3 - 1.23
* beautifulsoup4 - 4.6.3
* Python 3
* Pip 3


Steps for setting up a virtual environment on your mac to run this code:

$ brew install python3


Pip3 is installed with Python3

Installation


To install virtualenv via pip run:

<pre> $ pip3 install virtualenv</pre>

<b>Usage</b>


Creation of virtualenv:

<pre>$ virtualenv -p python3 <desired-path></pre>
Activate the virtualenv:

<pre>$ source <desired-path>/bin/activate</pre>

Deactivate the virtualenv:

<pre>$ deactivate</pre>


After you’ve created and activated a virtual environment, enter the command 

<pre>pip install Django</pre>

at the shell prompt/ terminal.

Now, move to the directory where you want to store the project


<pre> django-admin startproject webAnalyser</pre>


