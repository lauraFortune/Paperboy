# Paperboy

Python Desktop News Application
Data sourced from the external news API – https://newsapi.org. 
The application ‘Paperboy’ displays news data from three categories: Sports, Business and Technology. The user can save their
favourite news stories to the ‘My News’ section. Favourite news articles are stored in a local ‘Sqlite’ database.

## Built With

#### Modules/Middleware:
- [Sqlite3](https://docs.python.org/3/library/sqlite3.html), &nbsp;[Tkinter](https://docs.python.org/3/library/tkinter.html), &nbsp;[Python Imaging Library(PIL)](https://pillow.readthedocs.io/en/stable/), &nbsp; [Webbrowser](https://docs.python.org/3/library/webbrowser.html),  &nbsp; [Datetime](https://docs.python.org/3/library/datetime.html)

#### Languages:
- [Python](https://www.python.org/)

## Screenshots 
Click the following Images to view demos of the site in action:

- Welcome screen - Welcome message is displayed to the user along with instructions on how to use the application. 

![welcome2](https://user-images.githubusercontent.com/48602973/132321189-bdda25e8-38f0-458a-a249-7a902ab2b614.png)

- Browse News - News is displayed to the user in a scrollable news feed, filtered by category. 

![browse_categories](https://user-images.githubusercontent.com/48602973/132321202-1a0162be-8e83-4f63-a2a0-efd58b1a2c18.png)

- My News - News saved by the user is visible here. View gets updated as items are saved or deleted.

![mynews](https://user-images.githubusercontent.com/48602973/132321207-d1f4299e-fd53-4d35-99d5-fbada1a13013.png)


## Setting Up

### Python 3.7.1
1. Download and install Python 3.7.1 - https://www.python.org/downloads/release/python-371/
   
### News API
1. Navigate to newsapi.org and select 'Get API key' - https://newsapi.org/
2. Register to recieve your unique API KEY. 
 
   
## Running the application in your local environment

1. Clone project 

   ```bash
   git clone https://github.com/lauraFortune/paperboy.git
   ```
2. Open file news_api.py. Nagvigate to line 27. Update the API_KEY variable with the api key you recieved from newsapi.org.

   ```bash
   API_KEY = 'your_api_key'
   ```

3. Run app

   ```bash
   python main_gui.py
   ```

## Acknowledgments
### Tutorials
- Codemy.com - [Python Tkinter - Adding a Full Screen ScrollBar](https://www.youtube.com/watch?v=0WafQCaok6g)
### Fonts
- Hugo Victor - [Paxel](https://www.dafont.com/search.php?q=pixel)
- Markus Schroppel - [LLPIXEL](https://www.dafont.com/llpixel.font)
