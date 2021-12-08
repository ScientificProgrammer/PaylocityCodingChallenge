WITH f AS (
	SELECT n
	FROM (VALUES (0),(1),(2),(3),(4),(5),(6),(7),(8),(9)) v(n)
)
SELECT ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS rownum, gen_random_uuid() AS uuid
FROM f ones, f tens, f hundreds
ORDER BY 1;