CREATE TABLE Topics (
    id INTEGER PRIMARY KEY IDENTITY(1,1),
    title TEXT NOT NULL,
    content TEXT,
    source TEXT,
    url TEXT,
    image_url TEXT,
    date_added DATETIME DEFAULT CURRENT_TIMESTAMP,
    last_updated DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Relationships (
    id INTEGER PRIMARY KEY IDENTITY(1,1),
    parent_id INTEGER,
    child_id INTEGER,
    relationship_type TEXT,
    FOREIGN KEY (parent_id) REFERENCES Topics(id),
    FOREIGN KEY (child_id) REFERENCES Topics(id)
);