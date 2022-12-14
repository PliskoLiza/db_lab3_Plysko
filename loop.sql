DO $$
 DECLARE
     award_id   awards.award_id%TYPE;
     award_name awards.award_name%TYPE;

 BEGIN
     award_id := 'Award_number_';
     award_name := 'Award_name_';
     FOR counter IN 1..20
         LOOP
            INSERT INTO awards (award_id, award_name)
             VALUES (award_id || counter, award_name || counter);
         END LOOP;
 END;
 $$
 
--SELECT * FROM awards
--DO $$
-- BEGIN
--     FOR counter IN 1..20
--         LOOP
--		 	DELETE FROM awards WHERE award_id = 'Award_number_'||counter;
--         END LOOP;
-- END;
-- $$