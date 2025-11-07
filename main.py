from classe import Film, Salle, Reservation

# test des classes a supprimer erreur les exceptions ne sont pas vraiment géré
film1 = Film("Inception", 148)
salle1 = Salle(1, 50, film1)
res = Reservation("Alice", film1, salle1, 3)
res.confirmer()
