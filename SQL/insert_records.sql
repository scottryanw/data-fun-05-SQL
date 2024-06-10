-- Insert authors
INSERT INTO authors (author_id, first_name, last_name)
VALUES 
    ('94a8b542-1e82-4e46-9ba4-4854df8c94d2', 'Fyodor', 'Dostoevsky'),
    ('2194e2bf-16f6-4f91-8a1d-5145ed0c52dc', 'Oscar', 'Wilde'),
    ('9f38195a-1c81-4bc5-a447-8719c41f0331', 'Gabriel', 'Garcia Marquez'),
    ('5565ed3b-269d-489f-af49-b449ff223c22', 'Fyodor', 'Dostoevsky'),
    ('f6a9900f-53de-4963-9b29-37e08766e7cb', 'Leo', 'Tolstoy'),
    ('850fa60b-df6f-459d-ba1b-5487d84c07a7', 'Vladimir', 'Nabokov'),
    ('8317a524-48dc-4b3a-b7b1-5c5ff78097f0', 'Kurt', 'Vonnegut'),
    ('3b929f95-2fd5-4290-8133-99b69a42977d', 'John', 'Steinbeck'),
    ('44d0356e-5e61-4a14-b3ec-0ec2c0ef88c1', 'Sylvia', 'Plath');

-- Insert books
INSERT INTO books (book_id, title, year_published, author_id)
VALUES 
    ('16b6232c-f3bc-429e-b747-890e3ef86fd7', 'Crime and Punishment', 1866, '94a8b542-1e82-4e46-9ba4-4854df8c94d2'),
    ('6f5cf3d0-01d7-437e-94d7-bc858aa94777', 'The Picture of Dorian Gray', 1890, '2194e2bf-16f6-4f91-8a1d-5145ed0c52dc'),
    ('c30a2453-1a28-4e7e-a309-59fb14f1e462', 'One Hundred Years of Solitude', 1967, '9f38195a-1c81-4bc5-a447-8719c41f0331'),
    ('0e3dd7a3-45e8-4ab5-a4a0-f2bda0dab30c', 'The Brothers Karamazov', 1880, '5565ed3b-269d-489f-af49-b449ff223c22'),
    ('c98d0a85-3d5b-4465-8e0d-39cf3e8b34a9', 'Anna Karenina', 1877, 'f6a9900f-53de-4963-9b29-37e08766e7cb'),
    ('b812c3c5-ebf8-47d7-a746-28e7bfec70e1', 'Lolita', 1955, '850fa60b-df6f-459d-ba1b-5487d84c07a7'),
    ('d7e86f1b-b0ee-4745-a6e8-cd091e352d94', 'Slaughterhouse-Five', 1969, '8317a524-48dc-4b3a-b7b1-5c5ff78097f0'),
    ('80f49c69-3c84-4c6d-987f-01706a17a43d', 'The Grapes of Wrath', 1939, '3b929f95-2fd5-4290-8133-99b69a42977d'),
    ('97d66ec7-bd47-4b52-8a62-d6fbb2b5ae6e', 'The Bell Jar', 1963, '44d0356e-5e61-4a14-b3ec-0ec2c0ef88c1');