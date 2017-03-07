create table champion (
  id bigserial not null,
  key varchar(255) primary key,
  name varchar(255) not null,
  icon_url varchar(255),
  created_at timestamp not null default current_timestamp
);
