SET @row := -1;
SET @counter := 0;

  
CREATE TEMPORARY TABLE IF NOT EXISTS temp1
as
(
select image_id,round(score) as score from (select @counter := @counter+1, image_id,score from  (
SELECT * FROM 
 ( SELECT @row := @row +1 as rownum , image_id, score  
  FROM unlabeled_image_predictions  
  order by score desc ) as DT
WHERE mod(rownum,3)=0 and score>= 0.5
)
as DT1
  where @counter<5) DT2);
 
  



SET @row := -1;
SET @counter := 0;

  
CREATE TEMPORARY TABLE IF NOT EXISTS temp2
as
(
select image_id,round(score) as score from (select @counter := @counter+1, image_id,score from  (
SELECT * FROM 
 ( SELECT @row := @row +1 as rownum , image_id, score  
  FROM unlabeled_image_predictions  
  order by score ) as DT
WHERE mod(rownum,3)=0 and score < 0.5
)
as DT1
  where @counter<5) DT2);
 
  
select * from temp2
union
select * from temp1
order by image_id;


