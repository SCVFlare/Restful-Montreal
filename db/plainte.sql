create table plainte(
  id integer unique primary key,
  etablissement varchar(50),
  adresse  varchar(100),
  ville varchar(50),
  date_visite text,
  prenom varchar(50),
  nom varchar(50),
  description varchar(1000)
);
