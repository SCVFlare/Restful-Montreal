create table contrevenant (
  id integer primary key,
  adresse  varchar(500),
  categorie  varchar(50),
  date_infraction text,
  date_jugement text,
  description varchar(2000),
  etablissement varchar(200),
  montant real,
  proprietaire varchar(200),
  ville varchar(50)
);
