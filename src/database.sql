CREATE DATABASE mini_pipeline;

USE mini_pipeline;

-- Student Registration database schema
-- -------------------------------------
CREATE TABLE load_third_party (
	ticket_id INT,
	trans_date INT,
	event_id INT,
	event_name VARCHAR(50),
    event_date DATE,
    event_type VARCHAR(10),
    event_city VARCHAR(20),
    customer_id INT,
    price DECIMAL,
    num_tickets INT
);