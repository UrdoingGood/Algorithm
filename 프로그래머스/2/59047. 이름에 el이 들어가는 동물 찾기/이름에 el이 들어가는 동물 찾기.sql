SELECT animal_id, name 
FROM animal_ins 
WHERE animal_type = "dog" 
    AND (name LIKE "%el%" OR name LIKE "%EL%")
ORDER BY name;