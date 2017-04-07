drop table item;

create table item (
  id bigserial primary key,
  name varchar(255) not null,
  description_html varchar(1024),
  icon_url varchar(255),
  created_at timestamp not null default current_timestamp
);
