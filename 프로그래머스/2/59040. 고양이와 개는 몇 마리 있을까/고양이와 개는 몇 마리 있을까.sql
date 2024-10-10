SELECT animal_type, COUNT(animal_id) as count
FROM animal_ins 
GROUP BY animal_type
HAVING animal_type in ('Cat', 'Dog')
ORDER BY animal_type;
