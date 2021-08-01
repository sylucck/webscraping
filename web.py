#importing requests to request the website URL
import requests

#importing BeautifulSoup to be to parse the web page(parsing data structures)
from bs4 import BeautifulSoup

#web_URL variable has the website value we want to scrap. We want to webscrap this URL to get all job listings. 
web_URL = "https://realpython.github.io/fake-jobs/"

#web_page variable has the requests. Requesting the HTML contents of the web_URL
web_page = requests.get(web_URL)

#we can decide to print() the web_page to see the web_URL HTML contents
#print(web_page)

#soup variable has the BeautifulSoup with two parameters, the web_page.content and html.parser for parsing data structures
soup = BeautifulSoup(web_page.content, "html.parser")

#html_element_ID_finder variable has the soup.find(id="ResultsContainer"). This helps find the elements by id.
html_element_ID_finder = soup.find(id="ResultsContainer")

#little=html_element_ID_finder.find("div", class_="card")
#print(little)

#we can decide to print() the html_element_ID_finder using .prettify(). .prettify() helps to display all elements contained in a <div>
#print(html_element_ID_finder.prettify())

# We can decide to find all class="card-content" elements contained in "div".
web_job_elements = html_element_ID_finder.find_all("div", class_="card-content")

#we use a for loop to loop through to print each elements one after the other given two spaces each.
#for job_element in web_job_elements:
 #   print(job_element, end="\n"*2)

#We use a for loop to loop through to and print only title, company, location elements. We add .text to the variables contained in the print() function. This is a BeautifulSoup object to get only text in the HMTL contents.
#Note!!! the title, company, location elements is contained in the "h2", "h3", "p" HMTL tags respectively.
#We use .strip() python object to erase any unnecessary whitespace. This is possible cos we are using python strings to web scrap.

for job_element in web_job_elements:
    web_title_element = job_element.find("h2", class_="title")
    web_company_element = job_element.find("h3", class_="company")
    web_location_element = job_element.find("p", class_="location")
    print(web_title_element.text.strip())
    print(web_company_element.text.strip())
    print(web_location_element.text.strip())
    print()

# We may need a specific job title. The above prints all job title available not specifying the one we may be keen to.
# We use the string function to filter and get a specific job title. So we may want only "Python" job listings.
# Note!!! The code below finds all <h2> elements where the contained string matches "Python" exactly. When we use string= , the program looks for that string exactly. Any differences in the spelling, capitalization, or whitespace will prevent the element from matching. We will comment out the code below to help us move ahead and avoid bug.

# web_python_jobs = html_element_ID_finder.find_all("h2", string="Python")


# We can sometimes pass functions as arguments to Beautifulsoup.
# We are passing an anonymous function to the string=argument. The lambda function below looks at the text of each <h2> element, converts it to lowercase, and checks whether the substring "python" is found anywhere.
web_python_jobs = html_element_ID_finder.find_all("h2", string=lambda text: "python" in text.lower()
)
for python_jobs in web_python_jobs:
   print(python_jobs.text.strip(), end="\n"*2)

# The code above only prints out avialable "python" job listings without providing the full details like the company and location.
# One way to get access to all the information we need is to step up in the hierarchy of the DOM starting from the <h2> elements that was identified. We take another look at the HTML of a single job posting. We find the <h2> element that contains the job title as well as its closest parent element that contains all the information that we’re interested in.
# The <div> element with the card-content class contains all the information you want. It’s a third-level parent of the <h2> title element that you found using your filter. With this information in mind, we can now use the elements in python_jobs and fetch their great-grandparent elements instead to get access to all the information you want.

web_python_job_elements = [
    h2_element.parent.parent.parent for h2_element in web_python_jobs
]

# In the code above, we added a list comprehension that operates on each of the <h2> title elements in python_jobs that we got by filtering with the lambda expression. We are selecting the parent element of the parent element of the parent element of each <h2> title element. That’s three generations up! When we were looking at the HTML of a single job posting, we identified that this specific parent element with the class name card-content contains all the information you need.

# We will now iterate the parents elements using the for loop.... but we will comment out the code below

#for job_elements in web_python_job_elements:
 #   print(job_elements.text.strip(), end="\n")
    

# We may need the link to apply for any of the "python" jobs since we have full details now.
# The URL of a link element is associated with the href attribute. The specific URL that we’re looking for is the value of the href attribute of the second <a> tag at the bottom the HTML of a single job posting

for job_elements in web_python_job_elements:
    print(job_elements.text.strip(), end="\n")
    link_url = job_element.find_all("a")[1]["href"]
    print(f"Apply here: {link_url}\n")

#In this code snippet above, we first fetched all links from each of the filtered job postings. Then we extracted the href attribute, which contains the URL, using ["href"] and printed it to our console.