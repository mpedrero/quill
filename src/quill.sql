DROP TABLE IF EXISTS "author";
CREATE TABLE "author" 
( "name"  VARCHAR PRIMARY KEY NOT NULL, 
  "email" VARCHAR NOT NULL UNIQUE, 
  "avatar" BLOB
);


DROP TABLE IF EXISTS "entry";
CREATE TABLE "entry" 
( "id" NUMERIC PRIMARY KEY NOT NULL, 
  "title" VARCHAR, 
  "date" DATETIME DEFAULT CURRENT_TIMESTAMP, 
  "status" INTEGER, 
  "text" BLOB,
  "author" VARCHAR NOT NULL,
  FOREIGN KEY ("author") REFERENCES author("name")
);

DROP TABLE IF EXISTS "tag";
CREATE TABLE "tag" 
( "name" VARCHAR PRIMARY KEY NOT NULL 
);


DROP TABLE IF EXISTS "entry-tag";
CREATE TABLE "entry-tag" 
( "id_entry" NUMERIC NOT NULL, 
  "tag_name" VARCHAR NOT NULL, 
  PRIMARY KEY ("id_entry", "tag_name"),
  FOREIGN KEY ("id_entry") REFERENCES entry("id"),
  FOREIGN KEY ("tag_name") REFERENCES tag("name")
);
