-- Creates the database
CREATE DATABASE IF NOT EXISTS journal_entries
       CHARACTER SET utf8
       COLLATE utf8_unicode_ci;


-- Uses the database
USE journal_entries;

#ALTER DATABASE journal_entries

-- Create a person table
CREATE TABLE IF NOT EXISTS person (
    person_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

-- Creates the journal table
CREATE TABLE IF NOT EXISTS journal (
    jid INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    person_id INT NOT NULL,
    text TEXT,
    date_written DATETIME,
    author VARCHAR(35),
    text_keyword VARCHAR(300),
    location VARCHAR (30),
    FOREIGN KEY (person_id) REFERENCES person(person_id)
);

-- sample people
INSERT INTO person
    (name)
VALUES
    ('Janey Jackay'),
    ('Bob Bert'),
    ('Liam Strongman'),
    ('Gabriel Doesgood'),
    ('Francisco Holdon');

-- sample journal entries
-- Insert sample data into the journal table
INSERT INTO journal (jid, person_id, text, date_written, author, text_keyword, location)
VALUES
(1, 101, 'Today was a mixed bag. I started my morning with a yoga session, which was quite refreshing. The rest of the day was spent in meetings and brainstorming sessions with the team. We have a lot of exciting projects lined up for the next quarter, and I am eager to see them come to fruition. In the evening, I took a leisurely walk in the park and enjoyed the peaceful environment.', '2024-01-15 08:30:00', 'Janey Jackay', 'yoga, meetings, brainstorming, park', 'Chicago, USA'),
(2, 101, 'Spent the day working on a new project proposal. It involved a lot of research and writing, but I managed to get a solid draft ready by the end of the day. In the afternoon, I had a video call with a client to discuss the project details. The call went well, and we were able to finalize the requirements. Finished the day with a relaxing dinner at home.', '2024-02-20 18:00:00', 'Janey Jackay', 'project proposal, research, client call, dinner', 'Chicago, USA'),
(3, 102, 'Had a productive day at work. We implemented a new feature in our application that will greatly enhance user experience. The team collaborated effectively, and we managed to test the feature by the end of the day. I also had some time to catch up on industry news and trends. In the evening, I went out for a dinner with friends at a new restaurant downtown.', '2024-03-12 20:00:00', 'Bob Bert', 'feature implementation, teamwork, industry news, dinner', 'New York, USA'),
(4, 102, 'Attended a conference on tech innovations today. The keynote speeches were insightful, and I learned about some exciting new technologies. I spent most of the afternoon networking with other professionals in the field. The conference concluded with a panel discussion, which was quite engaging. Ended the day with a quiet walk through Central Park.', '2024-04-25 17:00:00', 'Bob Bert', 'conference, tech innovations, networking, Central Park', 'New York, USA'),
(5, 103, 'Had an early start today with a long workout at the gym. It was intense but energizing. The rest of the day was spent on a project with tight deadlines. I managed to meet all the deadlines and even had some time to catch up on personal tasks. In the evening, I went out for dinner with family and enjoyed some quality time together.', '2024-05-05 19:30:00', 'Liam Strongman', 'workout, project deadlines, family dinner', 'Los Angeles, USA'),
(6, 103, 'Visited a local art gallery today. The exhibits were fascinating, and I spent a few hours exploring the different pieces. I also had a chance to meet some local artists and learn about their work. The evening was spent at a cozy café, reflecting on the day\'s experiences and enjoying a good book.', '2024-06-10 15:00:00', 'Liam Strongman', 'art gallery, local artists, café, book', 'Los Angeles, USA'),
(7, 104, 'Spent the day hiking in the mountains. The scenery was breathtaking, and the fresh air was invigorating. It was a great way to disconnect from work and enjoy nature. I took plenty of photos to remember the experience. Returned home in the evening, feeling refreshed and relaxed.', '2024-07-20 17:00:00', 'Gabriel Doesgood', 'hiking, nature, photography, relaxation', 'Denver, USA'),
(8, 104, 'Participated in a community service event today. We worked on a local park clean-up project, which was both rewarding and fulfilling. In the afternoon, I attended a workshop on sustainability practices. The workshop provided valuable insights and practical tips. Ended the day with a casual dinner at a nearby café.', '2024-08-15 18:30:00', 'Gabriel Doesgood', 'community service, park clean-up, sustainability, café', 'Denver, USA'),
(9, 105, 'Visited a historical site today. The guided tour was informative and provided a lot of interesting facts about the history of the area. Spent some time exploring the museum exhibits as well. The evening was spent with friends at a local pub, where we had a great time catching up and enjoying some live music.', '2024-09-25 19:00:00', 'Francisco Holdon', 'historical site, museum, live music, pub', 'San Francisco, USA'),
(10, 105, 'Spent the day volunteering at an animal shelter. It was a heartwarming experience, and I enjoyed interacting with the animals. I also had the opportunity to help with some administrative tasks. In the evening, I relaxed at home and watched a documentary on wildlife conservation.', '2024-10-10 16:00:00', 'Francisco Holdon', 'volunteering, animal shelter, wildlife conservation', 'San Francisco, USA'),
(11, 105, 'Had a busy day working on a new product launch. The team worked hard to finalize all the details, and we managed to complete everything on schedule. In the evening, I attended a networking event with industry professionals. It was a great opportunity to make new connections and discuss potential collaborations.', '2024-11-05 20:00:00', 'Francisco Holdon', 'product launch, team collaboration, networking', 'San Francisco, USA');
