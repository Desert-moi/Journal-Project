# Journal Retrieval API Documentation
## Overview
This API allows you to retrieve journal entries based on the author's name. The API is built using Flask and is designed to handle GET requests.

## Running the API
To run the API, execute the following command:

### Clone the repo

1.  `git clone` https://github.com/Desert-moi/Journal-Project
2. Build and start the docker container: `docker-compose up --build`

### Base URL
The API is hosted at:
http://localhost:5000

### Interactions
Use the drop down menu to select from the various authors in the database. You can also leave the drown down menu
at the default selection and enter your own author to get an error. 

## Endpoints
1. Get Journal Entries by Author
- Endpoint: /get_data/author
- Method: GET
- Description: Retrieves journal entries for the specified author.
### Request Parameters
- author: (string, required) The name of the author whose journal entries you want to retrieve.

## Example Request

`curl -X GET "http://localhost:5000/get_data/Gabriel%20Doesgood"`

If the author exists, this would return:

`{
  "result": [
    {
      "author": "Gabriel Doesgood",
      "date_written": "Sat, 20 Jul 2024 17:00:00 GMT",
      "location": "Denver, USA",
      "text": "Spent the day hiking in the mountains. The scenery was breathtaking, and the fresh air was invigorating. It was a great way to disconnect from work and enjoy nature. I took plenty of photos to remember the experience. Returned home in the evening, feeling refreshed and relaxed.",
      "text_keyword": "hiking, nature, photography, relaxation"
    },
    {
      "author": "Gabriel Doesgood",
      "date_written": "Thu, 15 Aug 2024 18:30:00 GMT",
      "location": "Denver, USA",
      "text": "Participated in a community service event today. We worked on a local park clean-up project, which was both rewarding and fulfilling. In the afternoon, I attended a workshop on sustainability practices. The workshop provided valuable insights and practical tips. Ended the day with a casual dinner at a nearby café.",
      "text_keyword": "community service, park clean-up, sustainability, café"
    }
  ]
}`

If not, the request returns: 

`Error: Network response was not ok`