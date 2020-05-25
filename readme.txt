Version of Python used : 3.7.4
Version of Django used : 3.0.2
Gettext used : 0.20.1
URL to access your app  : http://localhost:8000/en/lab1app/index 
URL to access any variations of content in your app (if you have implemented multiple templates) :
index2(this is for the user from country Ireland) -> http://localhost:8000/en/lab1app/index2
index3(this is for the user from country Norway) -> http://localhost:8000/en/lab1app/index3

language
norwegian
index(this is for the user from country Uk)-> http://localhost:8000/no/lab1app/index
index2(this is for the user from country Ireland) -> http://localhost:8000/no/lab1app/index2
index3(this is for the user from country Norway) ->  http://localhost:8000/no/lab1app/index3

Irish 
index(this is for the user from country UK) -> http://localhost:8000/ga/lab1app/index
index2(this is for the user from country Ireland) -> http://localhost:8000/ga/lab1app/index2
index3(this is for the user from country Norway) -> http://localhost:8000/ga/lab1app/index3

Any other information relevant to the implementation of the project needed to run the app. : I'm not sure if this is needed,but I used python manage.py collectstatic before in my cmd to 
load the static files,only once. The rest of the time, whenever I ran my app after that, the app has worked. I don't think it's needed anymore, but just in case the static acts weird, I tried this.


To interact with the website:
1)It's going to land on the UK webpage first.
2)You pick the language that you understand at the very top of the page on the left hand side.
3)Then you pick the country, that you are in, which is on the right hand side of the page.
if you are from:

	UK
	stay on  the same page
	you can hover over the menu
	there's breadcrumb nav to go the webpages, you where before, if your finished looking at the page
	you just scroll down or up to read the contents of the page
	
	
	Ireland
	there's a dropdown menu
	there's a dropdown language menu, if you want to change the language
	there's social media, if you want to contact the school and ask a question
	there's a motivational exam youtube video to watch
	at the bottom, there's related content with four pictures and hovering over them will display the text of what the images lead to if you click them. They're fake, but the purpose of the images is to lead you to other sites for more information e.g. timetables, exams info, location of exam, when clicked.
	

	Norway 
	you can hover over the menu
	there's breadcrumb nav to go the webpages, you where before, if your finished looking at the page
	to access the answer to the questions, just hover over the questions and the answers will pop down, and remove the hover from it to let the answer stop displaying
	