# Encyclopedia Wiki
This project aims to create a simple wiki platform where users can create, edit, search, and browse encyclopedia entries. It leverages Python's Flask framework for the backend and HTML/CSS for the frontend.

# Google-like Search Engine

This project replicates essential features of Google's search engine using HTML and CSS. It offers a familiar user interface with functionalities such as regular search, image search, and advanced search.

## Features

- Entry Page: Visiting /wiki/TITLE renders a page displaying the contents of the encyclopedia entry.
  -The content is fetched by calling the appropriate util function.
  - If the entry doesn't exist, an error page is shown.
  - If the entry exists, its content is displayed, with the page title including the entry name.
- Index Page: index.html is updated to allow users to click on entry names to navigate directly to the respective entry page.
  - Search: Users can type a query into the search box in the sidebar.
  - If the query matches an entry, the user is redirected to that entry’s page.
  - If not, a search results page displays entries containing the query as a substring.
  - Clicking an entry name on the results page takes the user to that entry’s page.
- New Page: Clicking “Create New Page” takes the user to a page where they can create a new entry.
  - Users enter a title and Markdown content for the page.
  - Clicking a button saves the new page.
  - If an entry with the provided title already exists, an error message is shown.
- Edit Page: Users can click a link on each entry page to edit its Markdown content.
  - The textarea is pre-populated with existing content.
  - Clicking a button saves the changes and redirects back to the entry page.
- Random Page: Clicking “Random Page” in the sidebar takes the user to a random entry.
- Markdown to HTML Conversion: Markdown content in entry files is converted to HTML before being displayed to the user. This is achieved using the markdown2 package.

## Implementation

- HTML: Structured the web pages with HTML elements, including forms, input fields, buttons, and links.
- CSS: Styled the pages in a dark mode aesthetic, focusing on using dark colors, rounded corners, and consistent button styling.

## Development

This project was developed while taking the Harvard virtual class CS50's Web Programming with Python and JavaScript. It served as a practical exercise to reinforce concepts learned during the course.

## Usage

Clone the repository: git clone https://github.com/your_username/encyclopedia-wiki.git
Navigate to the project directory.
Install dependencies: pip install -r requirements.txt
Run the Flask application: python app.py
Open your web browser and go to http://localhost:5000 to start using the Encyclopedia Wiki.

## Demonstrative Video 
https://www.youtube.com/watch?v=XR4Gx4kbuYY
